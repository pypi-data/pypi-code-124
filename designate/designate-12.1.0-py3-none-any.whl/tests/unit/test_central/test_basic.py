# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Author: Federico Ceratto <federico.ceratto@hpe.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import unittest
from unittest import mock
from unittest.mock import patch

import fixtures
import testtools
from oslo_config import cfg
from oslo_config import fixture as cfg_fixture
from oslo_log import log as logging
from oslo_messaging.rpc import dispatcher as rpc_dispatcher
from oslotest import base

import designate.central.service
from designate import exceptions
from designate import objects
from designate.central.service import Service
from designate.tests import TestCase
from designate.tests.fixtures import random_seed

LOG = logging.getLogger(__name__)


# TODO(Federico): move this
def unwrap(f):
    """Unwrap a decorated function
    Requires __wrapped_function and __wrapper_name to be set
    """
    for _ in range(42):
        try:
            uf = getattr(f, '__wrapped_function')
            LOG.debug("Unwrapping %s from %s" %
                      (f.func_name, f.__wrapper_name))
            f = uf
        except AttributeError:
            return f

    return f


class RwObject(object):
    """Object mock: raise exception on __setitem__ or __setattr__
    on any item/attr created after initialization.
    Allows updating existing items/attrs
    """
    def __init__(self, d=None, **kw):
        if d:
            kw.update(d)
        self.__dict__.update(kw)

    def __getitem__(self, k):
        try:
            return self.__dict__[k]
        except KeyError:
            cn = self.__class__.__name__
            raise NotImplementedError(
                "Attempt to perform __getitem__"
                " %r on %s %r" % (cn, k, self.__dict__)
            )

    def __setitem__(self, k, v):
        if k in self.__dict__:
            self.__dict__.update({k: v})
            return

        cn = self.__class__.__name__
        raise NotImplementedError(
            "Attempt to perform __setitem__ or __setattr__"
            " %r on %s %r" % (cn, k, self.__dict__)
        )

    def __setattr__(self, k, v):
        self.__setitem__(k, v)


class RoObject(RwObject):
    """Read-only Object mock: raise exception on unexpected
    __setitem__ or __setattr__
    """
    def __setitem__(self, k, v):
        cn = self.__class__.__name__
        raise NotImplementedError(
            "Attempt to perform __setitem__ or __setattr__"
            " %r on %s %r" % (cn, k, self.__dict__)
        )


class MockObjectTest(base.BaseTestCase):
    def test_ro(self):
        o = RoObject(a=1)
        self.assertEqual(1, o['a'])
        self.assertEqual(1, o.a)
        with testtools.ExpectedException(NotImplementedError):
            o.a = 2
        with testtools.ExpectedException(NotImplementedError):
            o.new = 1
        with testtools.ExpectedException(NotImplementedError):
            o['a'] = 2
        with testtools.ExpectedException(NotImplementedError):
            o['new'] = 1

    def test_rw(self):
        o = RwObject(a=1)
        self.assertEqual(1, o['a'])
        self.assertEqual(1, o.a)
        o.a = 2
        self.assertEqual(2, o.a)
        self.assertEqual(2, o['a'])
        o['a'] = 3
        self.assertEqual(3, o.a)
        self.assertEqual(3, o['a'])
        with testtools.ExpectedException(NotImplementedError):
            o.new = 1
        with testtools.ExpectedException(NotImplementedError):
            o['new'] = 1


def mock_out(name):
    def decorator(meth):
        def wrapper(self, a):
            return meth(self, a)

        wrapper = mock.patch(name)(wrapper)
        return wrapper
    return decorator


class Mockzone(object):
    id = 1
    name = 'example.org'
    pool_id = 1
    tenant_id = 3
    ttl = 1
    type = "PRIMARY"
    serial = 123

    def obj_attr_is_set(self, n):
        if n == 'recordsets':
            return False
        raise NotImplementedError()

    def __getitem__(self, k):
        items = {
            'id': 3,
            'email': 'foo@example.org',
            'serial': 123,
            'refresh': 20,
            'retry': 33,
            'expire': 9999,
            'minimum': 2,
            'name': 'example.org.',
        }
        try:
            return items[k]
        except KeyError:
            raise NotImplementedError(k)


class MockRecordSet(object):
    id = 1
    name = 'example.org.'
    pool_id = 1
    tenant_id = 3
    ttl = 1
    type = "PRIMARY"
    serial = 123

    def obj_attr_is_set(self, n):
        if n == 'records':
            return False
        raise NotImplementedError()


class MockRecord(object):
    hostname = 'bar'

    def __getitem__(self, n):
        assert n == 'hostname'
        return 'bar'


class MockPool(object):
    ns_records = [MockRecord(), ]


# Fixtures
fx_mdns_api = fixtures.MockPatch('designate.central.service.mdns_rpcapi')

mdns_api = mock.PropertyMock(
    return_value=mock.NonCallableMagicMock(spec_set=[
        'a'
    ])
)


fx_worker = fixtures.MockPatch(
    'designate.central.service.worker_rpcapi.WorkerAPI.get_instance',
    mock.MagicMock(spec_set=[
        'create_zone',
        'update_zone',
        'delete_zone'
    ])
)

fx_disable_notification = fixtures.MockPatch('designate.central.notification')


class NotMockedError(NotImplementedError):
    pass


@patch('designate.central.service.storage',
       mock.NonCallableMock(side_effect=NotMockedError))
class CentralBasic(TestCase):
    def setUp(self):
        super(CentralBasic, self).setUp()
        self.CONF = self.useFixture(cfg_fixture.Config(cfg.CONF)).conf
        self.CONF([], project='designate')
        mock_storage = mock.Mock(spec=designate.storage.base.Storage)

        pool_list = objects.PoolList.from_list(
            [
                {'id': '794ccc2c-d751-44fe-b57f-8894c9f5c842'}
            ]
        )

        attrs = {
            'count_zones.return_value': 0,
            'find_zone.return_value': Mockzone(),
            'get_pool.return_value': MockPool(),
            'find_pools.return_value': pool_list,
        }
        mock_storage.configure_mock(**attrs)

        self.useFixture(fixtures.MockPatchObject(
            designate.central.service.storage, 'get_storage',
            return_value=mock_storage)
        )

        designate.central.service.policy = mock.NonCallableMock(spec_set=[
            'reset',
            'set_rules',
            'init',
            'check',
            'enforce_new_defaults',
        ])

        designate.central.service.quota = mock.NonCallableMock(spec_set=[
            'get_quota',
        ])

        designate.central.service.storage = mock.NonCallableMock(spec_set=[
            'get_storage',
        ])
        designate.central.service.rpcapi = mock.Mock()
        designate.central.service.worker_rpcapi = mock.Mock()
        self.context = mock.NonCallableMock(spec_set=[
            'elevated',
            'sudo',
            'abandon',
            'all_tenants',
        ])

        self.service = Service()
        self.service.check_for_tlds = True
        self.service.notifier = mock.Mock()


class CentralServiceTestCase(CentralBasic):

    def test_mdns_api_patch(self):
        with fx_mdns_api:
            q = self.service.mdns_api
            assert 'mdns_rpcapi.MdnsAPI.get_instance' in repr(q)

    def test_conf_fixture(self):
        assert 'service:central' in designate.central.service.cfg.CONF

    def test_init(self):
        self.assertTrue(self.service.check_for_tlds)

        # Ensure these attributes are lazy
        self.assertFalse(designate.central.service.storage.get_storage.called)
        self.assertFalse(designate.central.service.quota.get_quota.called)

    def test_storage_loads_lazily(self):
        assert self.service.storage
        self.assertTrue(designate.central.service.storage.get_storage.called)

    def test_quota_loads_lazily(self):
        assert self.service.quota
        self.assertTrue(designate.central.service.quota.get_quota.called)

    def test_is_valid_ttl(self):
        self.CONF.set_override('min_ttl', 10, 'service:central')
        self.service._is_valid_ttl(self.context, 20)

        # policy.check() not to raise: the user is allowed to create low TTLs
        designate.central.service.policy.check = mock.Mock(return_value=None)
        self.service._is_valid_ttl(self.context, None)
        self.service._is_valid_ttl(self.context, 1)

        # policy.check() to raise
        designate.central.service.policy.check = mock.Mock(
            side_effect=exceptions.Forbidden
        )

        with testtools.ExpectedException(exceptions.InvalidTTL):
            self.service._is_valid_ttl(self.context, 3)

    def test_update_soa_secondary(self):
        ctx = mock.Mock()
        mock_zone = RoObject(type='SECONDARY')

        self.service._update_soa(ctx, mock_zone)
        self.assertFalse(ctx.elevated.called)

    def test_update_soa(self):
        class MockZone(dict):
            type = 'PRIMARY'
            pool_id = 1

        class MockRecord(object):
            data = None

        mock_soa = RoObject(records=[MockRecord()])

        self.context.elevated = mock.Mock()
        self.service._update_zone_in_storage = mock.Mock()
        self.service.storage.get_pool = mock.Mock(
            return_value=MockPool())
        self.service.find_recordset = mock.Mock(return_value=mock_soa)
        self.service._build_soa_record = mock.Mock()
        self.service._update_recordset_in_storage = mock.Mock()

        self.service._update_soa(self.context, Mockzone())

        self.assertTrue(
            self.service._update_recordset_in_storage.called)
        self.assertTrue(self.context.elevated.called)

    def test_count_zones(self):
        self.service.count_zones(self.context)
        self.service.storage.count_zones.assert_called_once_with(
            self.context, {}
        )

    def test_count_zones_criterion(self):
        self.service.count_zones(self.context, criterion={'a': 1})
        self.service.storage.count_zones.assert_called_once_with(
            self.context, {'a': 1}
        )

    def test_validate_new_recordset(self):
        central_service = self.central_service

        central_service._is_valid_recordset_name = mock.Mock()
        central_service._is_valid_recordset_placement = mock.Mock()
        central_service._is_valid_recordset_placement_subzone = mock.Mock()
        central_service._is_valid_ttl = mock.Mock()

        MockRecordSet.id = None

        central_service._validate_recordset(
            self.context, Mockzone, MockRecordSet
        )

        self.assertTrue(central_service._is_valid_recordset_name.called)
        self.assertTrue(central_service._is_valid_recordset_placement.called)
        self.assertTrue(
            central_service._is_valid_recordset_placement_subzone.called)
        self.assertTrue(central_service._is_valid_ttl.called)

    def test_validate_existing_recordset(self):
        central_service = self.central_service

        central_service._is_valid_recordset_name = mock.Mock()
        central_service._is_valid_recordset_placement = mock.Mock()
        central_service._is_valid_recordset_placement_subzone = mock.Mock()
        central_service._is_valid_ttl = mock.Mock()

        MockRecordSet.obj_get_changes = mock.Mock(return_value={'ttl': 3600})

        central_service._validate_recordset(
            self.context, Mockzone, MockRecordSet
        )

        self.assertTrue(central_service._is_valid_recordset_name.called)
        self.assertTrue(central_service._is_valid_recordset_placement.called)
        self.assertTrue(
            central_service._is_valid_recordset_placement_subzone.called)
        self.assertTrue(central_service._is_valid_ttl.called)

    def test_create_recordset_in_storage(self):
        self.service._enforce_recordset_quota = mock.Mock()
        self.service._validate_recordset = mock.Mock()

        self.service.storage.create_recordset = mock.Mock(return_value='rs')
        self.service._update_zone_in_storage = mock.Mock()

        rs, zone = self.service._create_recordset_in_storage(
            self.context, Mockzone(), MockRecordSet()
        )
        self.assertEqual(rs, 'rs')
        self.assertFalse(self.service._update_zone_in_storage.called)

    def test_create_recordset_with_records_in_storage(self):
        central_service = self.central_service

        central_service._enforce_recordset_quota = mock.Mock()
        central_service._enforce_record_quota = mock.Mock()
        central_service._is_valid_recordset_name = mock.Mock()
        central_service._is_valid_recordset_placement = mock.Mock()
        central_service._is_valid_recordset_placement_subzone = mock.Mock()
        central_service._is_valid_ttl = mock.Mock()

        central_service.storage.create_recordset = mock.Mock(return_value='rs')
        central_service._update_zone_in_storage = mock.Mock()

        recordset = mock.Mock()
        recordset.obj_attr_is_set.return_value = True
        recordset.records = [MockRecord()]

        rs, zone = central_service._create_recordset_in_storage(
            self.context, Mockzone(), recordset
        )

        self.assertTrue(central_service._enforce_record_quota.called)
        self.assertTrue(central_service._update_zone_in_storage.called)

    def test_create_recordset_checking_DBDeadLock(self):
        self.service._enforce_recordset_quota = mock.Mock()
        self.service._enforce_record_quota = mock.Mock()
        self.service._is_valid_recordset_name = mock.Mock()
        self.service._is_valid_recordset_placement = mock.Mock()
        self.service._is_valid_recordset_placement_subzone = mock.Mock()
        self.service._is_valid_ttl = mock.Mock()

        self.service.storage.create_recordset = mock.Mock(return_value='rs')
        self.service._update_zone_in_storage = mock.Mock()

        # NOTE(thirose): Since this is a race condition we assume that
        #  we will hit it if we try to do the operations in a loop 100 times.
        for num in range(100):
            recordset = mock.Mock()
            recordset.name = "b{}".format(num)
            recordset.obj_attr_is_set.return_value = True
            recordset.records = [MockRecord()]

            rs, zone = self.service._create_recordset_in_storage(
                self.context, Mockzone(), recordset
            )
            assert not self.service.storage._retry_on_deadlock.called
            assert self.service._update_zone_in_storage.called
            assert self.service.storage.create_recordset.called

    def test_create_soa(self):
        central_service = self.central_service

        central_service._create_recordset_in_storage = mock.Mock(
            return_value=(None, None)
        )
        central_service._build_soa_record = mock.Mock(
            return_value='example.org. foo.bar 1 60 5 999 1'
        )
        zone = Mockzone()
        central_service._create_soa(self.context, zone)

        _, _, rset = central_service._create_recordset_in_storage.call_args[0]

        self.assertEqual('example.org.', rset.name)
        self.assertEqual('SOA', rset.type)
        self.assertEqual('SOA', rset.type)
        self.assertEqual(1, len(rset.records.objects))
        self.assertTrue(rset.records.objects[0].managed)

    def test_create_zone_in_storage(self):
        self.service._create_soa = mock.Mock()
        self.service._create_ns = mock.Mock()
        self.service.get_zone_ns_records = mock.Mock(
            return_value=[RoObject(hostname='host_foo')]
        )

        def cr_dom(ctx, zone):
            return zone

        self.service.storage.create_zone = cr_dom

        zone = self.service._create_zone_in_storage(
            self.context, Mockzone()
        )
        self.assertEqual('PENDING', zone.status)
        self.assertEqual('CREATE', zone.action)
        ctx, zone, hostnames = self.service._create_ns.call_args[0]
        self.assertEqual(['host_foo'], hostnames)

    @unittest.expectedFailure  # FIXME
    def test_create_zone_forbidden(self):
        self.assertFalse(self.service.storage.count_zones.called)
        designate.central.service.policy.check = mock.Mock(return_value=None)
        self.service._enforce_zone_quota = mock.Mock(return_value=None)
        self.service._is_valid_zone_name = mock.Mock(return_value=None)
        self.service._is_valid_ttl = mock.Mock(return_value=True)
        self.service._is_subzone = mock.Mock()
        self.service._create_zone_in_storage = mock.Mock(
            return_value=Mockzone()
        )
        self.service.storage.find_zone(self.context, {})

        parent_zone = self.service._is_subzone(
            self.context, 'bogusname', 1234)

        # self.assertEqual('', parent_zone)
        self.service.check_for_tlds = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.create_zone,
                                self.context, Mockzone())

        self.assertEqual(exceptions.Forbidden, exc.exc_info[0])

        # TODO(Federico) add more create_zone tests
        assert parent_zone


class CentralZoneTestCase(CentralBasic):

    zone__id = '1c85d9b0-1e9d-4e99-aede-a06664f1af2e'
    zone__id_2 = '7c85d9b0-1e9d-4e99-aede-a06664f1af2e'
    record__id = 'b81ebcfb-6236-4424-b77f-2dd0179fa041'
    record__id_2 = 'c81ebcfb-6236-4424-b77f-2dd0179fa041'
    pool__id = '769ca3fc-5924-4a44-8c1f-7efbe52fbd59'
    recordset__id = '9c85d9b0-1e9d-4e99-aede-a06664f1af2e'
    recordset__id_2 = 'dc85d9b0-1e9d-4e99-aede-a06664f1af2e'
    recordset__id_3 = '2a94a9fe-30d1-4a15-9071-0bb21996d971'
    zone_export__id = 'e887597f-9697-47dd-a202-7a2711f8669c'

    def setUp(self):
        super(CentralZoneTestCase, self).setUp()

        def storage_find_tld(c, d):
            if d['name'] not in ('org',):
                raise exceptions.TldNotFound

        def storage_find_tlds(c):
            return objects.TldList.from_list(
                [objects.Tld.from_dict({'name': 'org'})]
            )

        self.service.storage.find_tlds = storage_find_tlds
        self.service.storage.find_tld = storage_find_tld

    def test_is_valid_zone_name_valid(self):
        self.service._is_blacklisted_zone_name = mock.Mock()
        self.service._is_valid_zone_name(self.context, 'valid.org.')

    def test_is_valid_zone_name_invalid(self):
        self.service._is_blacklisted_zone_name = mock.Mock()
        with testtools.ExpectedException(exceptions.InvalidZoneName):
            self.service._is_valid_zone_name(self.context,
                                             'example^org.')

    def test_is_valid_zone_name_invalid_2(self):
        self.service._is_blacklisted_zone_name = mock.Mock()
        with testtools.ExpectedException(exceptions.InvalidZoneName):
            self.service._is_valid_zone_name(self.context,
                                             'example.tld.')

    def test_is_valid_zone_name_invalid_same_as_tld(self):
        self.service._is_blacklisted_zone_name = mock.Mock()
        with testtools.ExpectedException(exceptions.InvalidZoneName):
            self.service._is_valid_zone_name(self.context, 'com.com.')

    def test_is_valid_zone_name_invalid_tld(self):
        self.service._is_blacklisted_zone_name = mock.Mock()
        with testtools.ExpectedException(exceptions.InvalidZoneName):
            self.service._is_valid_zone_name(self.context, 'tld.')

    def test_is_valid_zone_name_blacklisted(self):
        self.service._is_blacklisted_zone_name = mock.Mock(
            side_effect=exceptions.InvalidZoneName)
        with testtools.ExpectedException(exceptions.InvalidZoneName):
            self.service._is_valid_zone_name(self.context,
                                             'valid.com.')

    def test_is_blacklisted_zone_name(self):
        self.service.storage.find_blacklists.return_value = [
            RoObject(pattern='a'), RoObject(pattern='b')
        ]
        blacklist_tests = (
            ('example.org', True),
            ('example.net', True),
            ('hi', False),
            ('', False)
        )
        for zone, expected in blacklist_tests:
            self.assertEqual(
                self.service._is_blacklisted_zone_name(self.context, zone),
                expected
            )

    def test_is_valid_recordset_name(self):
        zone = RoObject(name='example.org.')
        self.service._is_valid_recordset_name(self.context, zone,
                                              'foo..example.org.')

    def test_is_valid_recordset_name_no_dot(self):
        zone = RoObject(name='example.org.')
        with testtools.ExpectedException(ValueError):
            self.service._is_valid_recordset_name(self.context, zone,
                                                  'foo.example.org')

    def test_is_valid_recordset_name_too_long(self):
        zone = RoObject(name='example.org.')
        designate.central.service.cfg.CONF['service:central'].\
            max_recordset_name_len = 255
        rs_name = 'a' * 255 + '.org.'
        with testtools.ExpectedException(exceptions.InvalidRecordSetName) as e:
            self.service._is_valid_recordset_name(self.context, zone, rs_name)
            self.assertEqual(str(e), 'Name too long')

    def test_is_valid_recordset_name_wrong_zone(self):
        zone = RoObject(name='example.org.')
        with testtools.ExpectedException(exceptions.InvalidRecordSetLocation):
            self.service._is_valid_recordset_name(self.context, zone,
                                                  'foo.example.com.')

    def test_is_valid_recordset_placement_cname(self):
        zone = RoObject(name='example.org.')
        with testtools.ExpectedException(
                exceptions.InvalidRecordSetLocation) as e:
            self.service._is_valid_recordset_placement(
                self.context,
                zone,
                'example.org.',
                'CNAME',
            )
            self.assertEqual(
                'CNAME recordsets may not be created at the zone apex',
                str(e))

    def test_is_valid_recordset_placement_failing(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service.storage.find_recordsets.return_value = [
            RoObject(id=CentralZoneTestCase.recordset__id)
        ]
        with testtools.ExpectedException(
                exceptions.InvalidRecordSetLocation) as e:
            self.service._is_valid_recordset_placement(
                self.context,
                zone,
                'example.org.',
                'A',
            )
            self.assertEqual(
                'CNAME recordsets may not share a name with any other records',
                str(e))

    def test_is_valid_recordset_placement_failing_2(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service.storage.find_recordsets.return_value = [
            RoObject(),
            RoObject()
        ]
        with testtools.ExpectedException(
                exceptions.InvalidRecordSetLocation) as e:
            self.service._is_valid_recordset_placement(
                self.context,
                zone,
                'example.org.',
                'A',
            )
            self.assertEqual(
                'CNAME recordsets may not share a name with any other records',
                str(e))

    def test_is_valid_recordset_placement(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service.storage.find_recordsets.return_value = []
        ret = self.service._is_valid_recordset_placement(
            self.context,
            zone,
            'example.org.',
            'A',
        )
        self.assertTrue(ret)

    def test_is_valid_recordset_placement_subzone(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service._is_valid_recordset_placement_subzone(
            self.context,
            zone,
            'example.org.'
        )

    def test_is_valid_recordset_placement_subzone_2(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service._is_valid_recordset_name = mock.Mock(
            side_effect=Exception)
        self.service.storage.find_zones.return_value = [
            RoObject(name='foo.example.org.')
        ]
        self.service._is_valid_recordset_placement_subzone(
            self.context,
            zone,
            'bar.example.org.'
        )

    def test_is_valid_recordset_placement_subzone_failing(self):
        zone = RoObject(name='example.org.', id=CentralZoneTestCase.zone__id)
        self.service._is_valid_recordset_name = mock.Mock()
        self.service.storage.find_zones.return_value = [
            RoObject(name='foo.example.org.')
        ]
        with testtools.ExpectedException(exceptions.InvalidRecordSetLocation):
            self.service._is_valid_recordset_placement_subzone(
                self.context,
                zone,
                'bar.example.org.'
            )

    def test_is_valid_recordset_records(self):
        recordset = RoObject(
            records=[
                'ww1.example.com.',
                'ww2.example.com.'
            ],
            type='CNAME'
        )
        with testtools.ExpectedException(exceptions.BadRequest):
            self.service._is_valid_recordset_records(
                recordset
            )

    def test_is_superzone(self):
        central_service = self.central_service

        central_service.storage.find_zones = mock.Mock()
        central_service._is_superzone(self.context, 'example.org.', '1')
        _, crit = self.service.storage.find_zones.call_args[0]
        self.assertEqual({'name': '%.example.org.', 'pool_id': '1'}, crit)

    @patch('designate.central.service.utils.increment_serial')
    def FIXME_test_increment_zone_serial(self, utils_inc_ser):
        fixtures.MockPatch('designate.central.service.utils.increment_serial')
        zone = RoObject(serial=1)
        self.service._increment_zone_serial(self.context, zone)

    def test_create_ns(self):
        self.service._create_recordset_in_storage = mock.Mock(
            return_value=(0, 0))
        self.service._create_ns(
            self.context,
            RoObject(type='PRIMARY', name='example.org.'),
            [RoObject(), RoObject(), RoObject()]
        )
        ctx, zone, rset = \
            self.service._create_recordset_in_storage.call_args[0]

        self.assertEqual('example.org.', rset.name)
        self.assertEqual('NS', rset.type)
        self.assertEqual(3, len(rset.records))
        self.assertTrue(rset.records[0].managed)

    def test_create_ns_skip(self):
        self.service._create_recordset_in_storage = mock.Mock()
        self.service._create_ns(
            self.context,
            RoObject(type='SECONDARY', name='example.org.'),
            [],
        )
        self.assertFalse(
            self.service._create_recordset_in_storage.called)

    def test_add_ns_creation(self):
        self.service._create_ns = mock.Mock()

        self.service.find_recordset = mock.Mock(
            side_effect=exceptions.RecordSetNotFound()
        )

        self.service._add_ns(
            self.context,
            RoObject(name='foo', id=CentralZoneTestCase.zone__id),
            RoObject(name='bar')
        )
        ctx, zone, records = self.service._create_ns.call_args[0]
        self.assertTrue(len(records), 1)

    def test_add_ns(self):
        self.service._update_recordset_in_storage = mock.Mock()

        self.service.find_recordset = mock.Mock(
            return_value=RoObject(
                records=objects.RecordList.from_list([]), managed=True
            )
        )

        self.service._add_ns(
            self.context,
            RoObject(name='foo', id=CentralZoneTestCase.zone__id),
            RoObject(name='bar')
        )
        ctx, zone, rset = \
            self.service._update_recordset_in_storage.call_args[0]
        self.assertEqual(len(rset.records), 1)
        self.assertTrue(rset.records[0].managed)
        self.assertEqual('bar', rset.records[0].data.name)

    def test_create_zone_no_servers(self):
        self.service._enforce_zone_quota = mock.Mock()
        self.service._is_valid_zone_name = mock.Mock()
        self.service._is_valid_ttl = mock.Mock()
        self.service._is_subzone = mock.Mock(
            return_value=False
        )
        self.service._is_superzone = mock.Mock(
            return_value=[]
        )
        self.service.storage.get_pool.return_value = RoObject(
            ns_records=[]
        )

        self.useFixture(
            fixtures.MockPatchObject(
                self.service.storage,
                'find_pools',
                return_value=objects.PoolList.from_list(
                    [
                        {'id': '94ccc2c1-d751-44fe-b57f-8894c9f5c842'}
                    ]
                )
            )
        )

        z = objects.Zone(tenant_id='1',
                         name='example.com.', ttl=60,
                         pool_id=CentralZoneTestCase.pool__id)

        self.assertRaises(exceptions.NoServersConfigured,
                          self.service.create_zone,
                          self.context, z)

    def test_create_zone(self):
        self.service._enforce_zone_quota = mock.Mock()
        self.service._create_zone_in_storage = mock.Mock(
            return_value=objects.Zone(
                name='example.com.',
                type='PRIMARY',
            )
        )
        self.service._is_valid_zone_name = mock.Mock()
        self.service._is_valid_ttl = mock.Mock()
        self.service._is_subzone = mock.Mock(
            return_value=False
        )
        self.service._is_superzone = mock.Mock(
            return_value=[]
        )
        self.service.storage.get_pool.return_value = RoObject(
            ns_records=[RoObject()]
        )
        self.useFixture(
            fixtures.MockPatchObject(
                self.service.storage,
                'find_pools',
                return_value=objects.PoolList.from_list(
                    [
                        {'id': '94ccc2c1-d751-44fe-b57f-8894c9f5c842'}
                    ]
                )
            )
        )

        out = self.service.create_zone(
            self.context,
            objects.Zone(
                tenant_id='1',
                name='example.com.',
                ttl=60,
                pool_id=CentralZoneTestCase.pool__id,
                refresh=0,
                type='PRIMARY'
            )
        )
        self.assertEqual('example.com.', out.name)

    def test_get_zone(self):
        self.service.storage.get_zone.return_value = RoObject(
            name='foo',
            tenant_id='2',
        )
        self.service.get_zone(self.context,
                              CentralZoneTestCase.zone__id)
        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual(CentralZoneTestCase.zone__id, target['zone_id'])
        self.assertEqual('foo', target['zone_name'])
        self.assertEqual('2', target['project_id'])

    def test_get_zone_servers(self):
        self.service.storage.get_zone.return_value = RoObject(
            name='foo',
            tenant_id='2',
            pool_id=CentralZoneTestCase.pool__id,
        )

        self.service.get_zone_ns_records(
            self.context,
            zone_id=CentralZoneTestCase.zone__id
        )

        ctx, pool_id = self.service.storage.get_pool.call_args[0]
        self.assertEqual(CentralZoneTestCase.pool__id, pool_id)

    def test_find_zones(self):
        self.context = RoObject(project_id='t')
        self.service.storage.find_zones = mock.Mock()
        self.service.find_zones(self.context)
        self.assertTrue(self.service.storage.find_zones.called)
        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('find_zones', pcheck)

    def test_find_zone(self):
        self.context = RoObject(project_id='t')
        self.service.storage.find_zone = mock.Mock()
        self.service.find_zone(self.context)
        self.assertTrue(self.service.storage.find_zone.called)
        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('find_zone', pcheck)

    def test_delete_zone_has_subzone(self):
        self.context.abandon = False
        self.service.storage.get_zone.return_value = RoObject(
            name='foo',
            tenant_id='2',
        )
        self.service.storage.count_zones.return_value = 2

        self.assertRaises(exceptions.ZoneHasSubZone,
                          self.service.delete_zone,
                          self.context,
                          CentralZoneTestCase.zone__id)

        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('delete_zone', pcheck)

    def test_delete_zone_abandon(self):
        self.service.storage.get_zone.return_value = RoObject(
            name='foo',
            tenant_id='2',
            id=CentralZoneTestCase.zone__id_2
        )
        designate.central.service.policy = mock.NonCallableMock(spec_set=[
            'reset',
            'set_rules',
            'init',
            'check',
            'enforce_new_defaults',
        ])
        self.context.abandon = True
        self.service.storage.count_zones.return_value = 0
        self.service.delete_zone(self.context,
                                 CentralZoneTestCase.zone__id)
        self.assertTrue(self.service.storage.delete_zone.called)
        self.assertFalse(self.service.zone_api.delete_zone.called)
        pcheck, _, _ = designate.central.service.policy.check.call_args[0]
        self.assertEqual('abandon_zone', pcheck)

    def test_delete_zone(self):
        self.context.abandon = False
        self.service.storage.get_zone.return_value = RoObject(
            name='foo',
            tenant_id='2',
        )
        self.service._delete_zone_in_storage = mock.Mock(
            return_value=RoObject(
                name='foo'
            )
        )
        self.service.storage.count_zones.return_value = 0
        out = self.service.delete_zone(self.context,
                                       CentralZoneTestCase.zone__id)
        self.assertFalse(self.service.storage.delete_zone.called)
        self.assertTrue(self.service.zone_api.delete_zone.called)
        self.assertTrue(designate.central.service.policy.check.called)
        ctx, deleted_dom = \
            self.service.zone_api.delete_zone.call_args[0]

        self.assertEqual('foo', deleted_dom.name)
        self.assertEqual('foo', out.name)
        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('delete_zone', pcheck)

    def test_delete_zone_in_storage(self):
        self.service._delete_zone_in_storage(
            self.context,
            RwObject(action='', status=''),
        )
        d = self.service.storage.update_zone.call_args[0][1]
        self.assertEqual('DELETE', d.action)
        self.assertEqual('PENDING', d.status)

    def test_xfr_zone_secondary(self):
        self.service.storage.get_zone.return_value = RoObject(
            name='example.org.',
            tenant_id='2',
            type='SECONDARY',
            masters=[RoObject(host='10.0.0.1', port=53)],
            serial=1,
        )
        with fx_mdns_api:
            self.service.mdns_api.get_serial_number.return_value = \
                "SUCCESS", 2, 1
            self.service.xfr_zone(
                self.context, CentralZoneTestCase.zone__id)
            self.assertTrue(
                self.service.mdns_api.perform_zone_xfr.called)

            self.assertTrue(designate.central.service.policy.check.called)
        self.assertEqual(
            'xfr_zone',
            designate.central.service.policy.check.call_args[0][0]
        )

    def test_xfr_zone_not_secondary(self):
        self.service.storage.get_zone.return_value = RoObject(
            name='example.org.',
            tenant_id='2',
            type='PRIMARY'
        )

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.xfr_zone,
                                self.context,
                                CentralZoneTestCase.zone__id)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_count_report(self):
        self.service.count_zones = mock.Mock(return_value=1)
        self.service.count_records = mock.Mock(return_value=2)
        self.service.count_tenants = mock.Mock(return_value=3)
        reports = self.service.count_report(
            self.context,
            criterion=None
        )
        self.assertEqual([{'zones': 1, 'records': 2, 'tenants': 3}], reports)

    def test_count_report_zones(self):
        self.service.count_zones = mock.Mock(return_value=1)
        self.service.count_records = mock.Mock(return_value=2)
        self.service.count_tenants = mock.Mock(return_value=3)
        reports = self.service.count_report(
            self.context,
            criterion='zones'
        )
        self.assertEqual([{'zones': 1}], reports)

    def test_count_report_records(self):
        self.service.count_zones = mock.Mock(return_value=1)
        self.service.count_records = mock.Mock(return_value=2)
        self.service.count_tenants = mock.Mock(return_value=3)
        reports = self.service.count_report(
            self.context,
            criterion='records'
        )
        self.assertEqual([{'records': 2}], reports)

    def test_count_report_tenants(self):
        self.service.count_zones = mock.Mock(return_value=1)
        self.service.count_records = mock.Mock(return_value=2)
        self.service.count_tenants = mock.Mock(return_value=3)
        reports = self.service.count_report(
            self.context,
            criterion='tenants'
        )
        self.assertEqual([{'tenants': 3}], reports)

    def test_count_report_not_found(self):
        self.service.count_zones = mock.Mock(return_value=1)
        self.service.count_records = mock.Mock(return_value=2)
        self.service.count_tenants = mock.Mock(return_value=3)

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.count_report,
                                self.context,
                                criterion='bogus')

        self.assertEqual(exceptions.ReportNotFound, exc.exc_info[0])

    def test_touch_zone_with_worker_model(self):
        self.service._touch_zone_in_storage = mock.Mock()
        self.service.storage.get_zone.return_value = RoObject(
            name='example.org.',
            tenant_id='2',
        )

        with fx_worker:
            self.service.touch_zone(self.context,
                                    CentralZoneTestCase.zone__id)
            self.assertTrue(designate.central.service.policy.check.called)
        self.assertEqual(
            'touch_zone',
            designate.central.service.policy.check.call_args[0][0]
        )

    def test_get_recordset_not_found(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id_2
        )

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.get_recordset,
                                self.context,
                                CentralZoneTestCase.zone__id,
                                CentralZoneTestCase.recordset__id)

        self.assertEqual(exceptions.RecordSetNotFound, exc.exc_info[0])

    def test_get_recordset(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
        )
        self.service.storage.get_recordset.return_value = (
            objects.RecordSet(
                zone_id=CentralZoneTestCase.zone__id_2,
                zone_name='example.org.',
                id=CentralZoneTestCase.recordset__id
            ))
        self.service.get_recordset(
            self.context,
            CentralZoneTestCase.zone__id_2,
            CentralZoneTestCase.recordset__id,
        )
        self.assertEqual(
            'get_recordset',
            designate.central.service.policy.check.call_args[0][0]
        )
        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('get_recordset', t)
        self.assertEqual({
            'zone_id': CentralZoneTestCase.zone__id_2,
            'zone_name': 'example.org.',
            'recordset_id': CentralZoneTestCase.recordset__id,
            'project_id': '2'}, target)

    def test_find_recordsets(self):
        self.context = mock.Mock()
        self.context.project_id = 't'
        self.service.find_recordsets(self.context)
        self.assertTrue(self.service.storage.find_recordsets.called)
        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('find_recordsets', n)
        self.assertEqual({'project_id': 't'}, target)

    def test_find_recordset(self):
        self.context = mock.Mock()
        self.context.project_id = 't'
        self.service.find_recordset(self.context)
        self.assertTrue(self.service.storage.find_recordset.called)
        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('find_recordset', n)
        self.assertEqual({'project_id': 't'}, target)

    def test_update_recordset_fail_on_changes(self):
        self.service.storage.get_zone.return_value = RoObject()
        recordset = mock.Mock()
        recordset.obj_get_original_value.return_value = '1'

        recordset.obj_get_changes.return_value = ['tenant_id', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_recordset,
                                self.context,
                                recordset)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

        recordset.obj_get_changes.return_value = ['zone_id', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_recordset,
                                self.context,
                                recordset)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

        recordset.obj_get_changes.return_value = ['type', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_recordset,
                                self.context,
                                recordset)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_recordset_action_delete(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='DELETE',
        )
        recordset = mock.Mock()
        recordset.obj_get_changes.return_value = ['foo']

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_recordset,
                                self.context,
                                recordset)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_recordset_action_fail_on_managed(self):
        self.service.storage.get_zone.return_value = RoObject(
            type='foo',
            name='example.org.',
            tenant_id='2',
            action='bogus',
        )
        recordset = mock.Mock()
        recordset.obj_get_changes.return_value = ['foo']
        recordset.managed = True
        self.context = mock.Mock()
        self.context.edit_managed_records = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_recordset,
                                self.context,
                                recordset)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_recordset_worker_model(self):
        self.service.storage.get_zone.return_value = RoObject(
            type='foo',
            name='example.org.',
            tenant_id='2',
            action='bogus',
        )
        recordset = mock.Mock()
        recordset.obj_get_changes.return_value = ['foo']
        recordset.obj_get_original_value.return_value =\
            '9c85d9b0-1e9d-4e99-aede-a06664f1af2e'
        recordset.managed = False
        self.service._update_recordset_in_storage = mock.Mock(
            return_value=('x', 'y')
        )

        with fx_worker:
            self.service.update_recordset(self.context, recordset)
        self.assertTrue(
            self.service._update_recordset_in_storage.called)

        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('update_recordset', n)
        self.assertEqual({
            'zone_id': '9c85d9b0-1e9d-4e99-aede-a06664f1af2e',
            'zone_name': 'example.org.',
            'zone_type': 'foo',
            'recordset_id': '9c85d9b0-1e9d-4e99-aede-a06664f1af2e',
            'project_id': '2'}, target)

    def test__update_recordset_in_storage(self):
        recordset = mock.Mock()
        recordset.name = 'n'
        recordset.type = 't'
        recordset.id = CentralZoneTestCase.recordset__id
        recordset.obj_get_changes.return_value = {'ttl': 90}
        recordset.ttl = 90
        recordset.records = []
        self.service._is_valid_recordset_name = mock.Mock()
        self.service._is_valid_recordset_placement = mock.Mock()
        self.service._is_valid_recordset_placement_subzone = mock.Mock()
        self.service._is_valid_ttl = mock.Mock()
        self.service._update_zone_in_storage = mock.Mock()

        self.service._update_recordset_in_storage(
            self.context,
            RoObject(serial=3),
            recordset,
        )

        self.assertEqual(
            'n',
            self.service._is_valid_recordset_name.call_args[0][2]
        )
        self.assertEqual(
            ('n', 't', CentralZoneTestCase.recordset__id),
            self.service._is_valid_recordset_placement.call_args[0][2:]
        )
        self.assertEqual(
            'n',
            self.service._is_valid_recordset_placement_subzone.
            call_args[0][2]
        )
        self.assertEqual(
            90,
            self.service._is_valid_ttl.call_args[0][1]
        )
        self.assertTrue(self.service.storage.update_recordset.called)
        self.assertTrue(self.service._update_zone_in_storage.called)

    def test_update_recordset_in_storage_2(self):
        recordset = mock.Mock()
        recordset.name = 'n'
        recordset.type = 't'
        recordset.id = CentralZoneTestCase.recordset__id
        recordset.ttl = None
        recordset.obj_get_changes.return_value = {'ttl': None}
        recordset.records = [RwObject(
            action='a',
            status='s',
            serial=9,
        )]
        self.service._is_valid_recordset_name = mock.Mock()
        self.service._is_valid_recordset_placement = mock.Mock()
        self.service._is_valid_recordset_placement_subzone = mock.Mock()
        self.service._update_zone_in_storage = mock.Mock()
        self.service._enforce_record_quota = mock.Mock()

        self.service._update_recordset_in_storage(
            self.context,
            RoObject(serial=3),
            recordset,
            increment_serial=False,
        )

        self.assertEqual(
            'n',
            self.service._is_valid_recordset_name.call_args[0][2]
        )
        self.assertEqual(
            ('n', 't', CentralZoneTestCase.recordset__id),
            self.service._is_valid_recordset_placement.call_args[0][2:]
        )
        self.assertEqual(
            'n',
            self.service._is_valid_recordset_placement_subzone.
            call_args[0][2]
        )
        self.assertFalse(self.service._update_zone_in_storage.called)
        self.assertTrue(self.service.storage.update_recordset.called)
        self.assertTrue(self.service._enforce_record_quota.called)

    def test_delete_recordset_not_found(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='bogus',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id,
            id=CentralZoneTestCase.recordset__id,
            managed=False,
        )
        self.context = mock.Mock()
        self.context.edit_managed_records = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_recordset,
                                self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id)

        self.assertEqual(exceptions.RecordSetNotFound, exc.exc_info[0])

    def test_delete_recordset_action_delete(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='DELETE',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id_2,
            id=CentralZoneTestCase.recordset__id,
            managed=False,
        )
        self.context = mock.Mock()
        self.context.edit_managed_records = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_recordset,
                                self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_delete_recordset_managed(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='foo',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id_2,
            id=CentralZoneTestCase.recordset__id,
            managed=True,
        )
        self.context = mock.Mock()
        self.context.edit_managed_records = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_recordset,
                                self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_delete_recordset_worker(self):
        mock_zone = RoObject(
            action='foo',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        mock_rs = objects.RecordSet(
            zone_id=CentralZoneTestCase.zone__id_2,
            zone_name='example.org.',
            id=CentralZoneTestCase.recordset__id,
            records=objects.RecordList.from_list([]),
        )

        self.service.storage.get_zone.return_value = mock_zone
        self.service.storage.get_recordset.return_value = mock_rs
        self.context = mock.Mock()
        self.context.edit_managed_records = False
        self.service._delete_recordset_in_storage = mock.Mock(
            return_value=(mock_rs, mock_zone)
        )

        with fx_worker:
            self.service.delete_recordset(self.context,
                CentralZoneTestCase.zone__id_2,
                CentralZoneTestCase.recordset__id)
            self.assertTrue(
                self.service.zone_api.update_zone.called)

        self.assertTrue(
            self.service._delete_recordset_in_storage.called)

    def test__delete_recordset_in_storage(self):
        def mock_uds(c, zone, inc):
            return zone
        self.service._update_zone_in_storage = mock_uds
        self.service._delete_recordset_in_storage(
            self.context,
            RoObject(serial=1),
            RoObject(id=2, records=[
                RwObject(
                    action='',
                    status='',
                    serial=0,
                )
            ])
        )
        self.assertTrue(self.service.storage.update_recordset.called)
        self.assertTrue(self.service.storage.delete_recordset.called)
        rs = self.service.storage.update_recordset.call_args[0][1]
        self.assertEqual(1, len(rs.records))
        self.assertEqual('DELETE', rs.records[0].action)
        self.assertEqual('PENDING', rs.records[0].status)
        self.assertEqual(1, rs.records[0].serial)

    def test_delete_recordset_in_storage_no_increment_serial(self):
        self.service._update_zone_in_storage = mock.Mock()
        self.service._delete_recordset_in_storage(
            self.context,
            RoObject(serial=1),
            RoObject(id=2, records=[
                RwObject(
                    action='',
                    status='',
                    serial=0,
                )
            ]),
            increment_serial=False,
        )
        self.assertTrue(self.service.storage.update_recordset.called)
        self.assertTrue(self.service.storage.delete_recordset.called)
        self.assertFalse(self.service._update_zone_in_storage.called)

    def test_count_recordset(self):
        self.service.count_recordsets(self.context)
        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('count_recordsets', n)
        self.assertEqual({'project_id': None}, target)
        self.assertEqual(
            {},
            self.service.storage.count_recordsets.call_args[0][1]
        )

    def test_create_record_fail_on_delete(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='DELETE',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.create_record,
                                self.context,
                                CentralZoneTestCase.zone__id,
                                CentralZoneTestCase.recordset__id,
                                RoObject())

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def _test_create_record(self):
        self.service._create_record_in_storage = mock.Mock(
            return_value=(None, None)
        )
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id='2',
            type='foo',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            name='rs',
        )

        with fx_worker:
            self.service.create_record(
                self.context,
                CentralZoneTestCase.zone__id,
                CentralZoneTestCase.recordset__id,
                RoObject())
            self.assertTrue(
                self.service.zone_api.update_zone.called)

        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('create_record', n)
        self.assertEqual({
            'zone_id': CentralZoneTestCase.zone__id,
            'zone_name': 'example.org.',
            'zone_type': 'foo',
            'recordset_id': CentralZoneTestCase.recordset__id,
            'recordset_name': 'rs',
            'project_id': '2'}, target)

    def test_create_record_worker(self):
        self._test_create_record()

    def test__create_record_in_storage(self):
        self.service._enforce_record_quota = mock.Mock()
        self.service._create_record_in_storage(
            self.context,
            RoObject(id=CentralZoneTestCase.zone__id, serial=4),
            RoObject(id=CentralZoneTestCase.recordset__id),
            RwObject(
                action='',
                status='',
                serial='',
            ),
            increment_serial=False
        )
        create_record = self.service.storage.create_record

        ctx, did, rid, record = create_record.call_args[0]
        self.assertEqual(CentralZoneTestCase.zone__id, did)
        self.assertEqual(CentralZoneTestCase.recordset__id, rid)
        self.assertEqual('CREATE', record.action)
        self.assertEqual('PENDING', record.status)
        self.assertEqual(4, record.serial)

    def test_get_record_not_found(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id_2,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.recordset__id
        )

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.get_record,
                                self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id,
                                CentralZoneTestCase.record__id)

        self.assertEqual(exceptions.RecordNotFound, exc.exc_info[0])

    def test_get_record_not_found_2(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id_2,
            name='example.org.',
            tenant_id=2,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id_2,
            id=999,  # not matching record.recordset_id
            name='foo'
        )
        self.service.storage.get_record.return_value = RoObject(
            id=CentralZoneTestCase.record__id,
            zone_id=CentralZoneTestCase.zone__id_2,
            recordset_id=CentralZoneTestCase.recordset__id
        )

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.get_record,
                                self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id,
                                CentralZoneTestCase.record__id)

        self.assertEqual(exceptions.RecordNotFound, exc.exc_info[0])

    def test_get_record(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id,
            name='example.org.',
            tenant_id=2,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            zone_id=CentralZoneTestCase.zone__id,
            id=CentralZoneTestCase.recordset__id,
            name='foo'
        )
        self.service.storage.get_record.return_value = RoObject(
            id=CentralZoneTestCase.record__id,
            zone_id=CentralZoneTestCase.zone__id,
            recordset_id=CentralZoneTestCase.recordset__id
        )
        self.service.get_record(self.context,
                                CentralZoneTestCase.zone__id_2,
                                CentralZoneTestCase.recordset__id_2,
                                CentralZoneTestCase.record__id_2)
        self.assertEqual(
            'get_record',
            designate.central.service.policy.check.call_args[0][0]
        )
        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('get_record', t)
        self.assertEqual({
            'zone_id': CentralZoneTestCase.zone__id_2,
            'zone_name': 'example.org.',
            'record_id': CentralZoneTestCase.record__id,
            'recordset_id': CentralZoneTestCase.recordset__id_2,
            'recordset_name': 'foo',
            'project_id': 2}, target)

    def test_update_record_fail_on_changes(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            name='n',
            type='t',
            tenant_id='tid',
        )
        record = mock.Mock()
        record.obj_get_original_value.return_value = 1

        record.obj_get_changes.return_value = ['tenant_id', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_record,
                                self.context, record)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

        record.obj_get_changes.return_value = ['zone_id', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_record,
                                self.context, record)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

        record.obj_get_changes.return_value = ['recordset_id', 'foo']
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_record,
                                self.context, record)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_record_action_delete(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='DELETE',
        )
        record = mock.Mock()
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_record,
                                self.context, record)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_record_action_fail_on_managed(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            name='n',
            tenant_id='tid',
            type='t',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            name='rsn',
            managed=True
        )
        record = mock.Mock()
        record.obj_get_changes.return_value = ['foo']
        self.context = mock.Mock()
        self.context.edit_managed_records = False

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.update_record,
                                self.context, record)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_update_record_worker(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            name='n',
            tenant_id='tid',
            type='t',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            name='rsn',
            managed=False
        )
        record = mock.Mock()
        record.obj_get_changes.return_value = ['foo']
        record.obj_get_original_value.return_value =\
            'abc12a-1e9d-4e99-aede-a06664f1af2e'
        record.managed = False
        self.service._update_record_in_storage = mock.Mock(
            return_value=('x', 'y')
        )

        with fx_worker:
            self.service.update_record(self.context, record)

        self.assertTrue(self.service._update_record_in_storage.called)

        n, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('update_record', n)
        self.assertEqual({
            'zone_id': 'abc12a-1e9d-4e99-aede-a06664f1af2e',
            'zone_name': 'n',
            'zone_type': 't',
            'record_id': 'abc12a-1e9d-4e99-aede-a06664f1af2e',
            'recordset_id': 'abc12a-1e9d-4e99-aede-a06664f1af2e',
            'recordset_name': 'rsn',
            'project_id': 'tid'}, target)

    def test__update_record_in_storage(self):
        self.service._update_zone_in_storage = mock.Mock()
        self.service._update_record_in_storage(
            self.context,
            RoObject(serial=1),
            RwObject(
                action='',
                status='',
                serial='',
            ),
            increment_serial=False
        )
        ctx, record = self.service.storage.update_record.call_args[0]
        self.assertEqual('UPDATE', record.action)
        self.assertEqual('PENDING', record.status)
        self.assertEqual(1, record.serial)

    def test_delete_record_action_delete(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='DELETE',
        )

        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_record,
                                self.context, 1, 2, 3)

        self.assertEqual(exceptions.BadRequest, exc.exc_info[0])

    def test_delete_record_not_found(self):
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            id=CentralZoneTestCase.zone__id
        )
        self.service.storage.get_record.return_value = RoObject(
            zone_id=CentralZoneTestCase.record__id_2,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            id=CentralZoneTestCase.recordset__id_2,
        )

        # zone.id != record.zone_id
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_record,
                                self.context,
                                CentralZoneTestCase.zone__id,
                                CentralZoneTestCase.recordset__id,
                                CentralZoneTestCase.record__id)

        self.assertEqual(exceptions.RecordNotFound, exc.exc_info[0])

        self.service.storage.get_record.return_value = RoObject(
            id=CentralZoneTestCase.record__id,
            zone_id=CentralZoneTestCase.zone__id,
            recordset_id=CentralZoneTestCase.recordset__id_3,
        )
        #  recordset.id != record.recordset_id
        exc = self.assertRaises(rpc_dispatcher.ExpectedException,
                                self.service.delete_record,
                                self.context,
                                CentralZoneTestCase.zone__id,
                                CentralZoneTestCase.recordset__id,
                                CentralZoneTestCase.record__id)

        self.assertEqual(exceptions.RecordNotFound, exc.exc_info[0])

    def test_delete_record_worker(self):
        self.service._delete_record_in_storage = mock.Mock(
            return_value=(None, None)
        )
        self.service.storage.get_zone.return_value = RoObject(
            action='a',
            id=CentralZoneTestCase.zone__id,
            name='dn',
            tenant_id='tid',
            type='t',
        )
        self.service.storage.get_record.return_value = RoObject(
            id=CentralZoneTestCase.record__id_2,
            zone_id=CentralZoneTestCase.zone__id,
            recordset_id=CentralZoneTestCase.recordset__id,
        )
        self.service.storage.get_recordset.return_value = RoObject(
            name='rsn',
            id=CentralZoneTestCase.recordset__id,
            managed=False,
        )

        with fx_worker:
            self.service.delete_record(self.context,
                CentralZoneTestCase.zone__id_2,
                CentralZoneTestCase.recordset__id_2,
                CentralZoneTestCase.record__id)

        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('delete_record', t)
        self.assertEqual({
            'zone_id': CentralZoneTestCase.zone__id_2,
            'zone_name': 'dn',
            'zone_type': 't',
            'record_id': CentralZoneTestCase.record__id_2,
            'recordset_id': CentralZoneTestCase.recordset__id_2,
            'recordset_name': 'rsn',
            'project_id': 'tid'}, target)

    def test_delete_record_in_storage(self):
        self.service._delete_record_in_storage(
            self.context,
            RoObject(serial=2),
            RwObject(action='', status='', serial=''),
            increment_serial=False
        )
        r = self.service.storage.update_record.call_args[0][1]
        self.assertEqual('DELETE', r.action)
        self.assertEqual('PENDING', r.status)
        self.assertEqual(2, r.serial)

    def test_count_records(self):
        self.service.count_records(self.context)
        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('count_records', t)
        self.assertEqual({'project_id': None}, target)

    def test_sync_zones(self):
        self.service._sync_zone = mock.Mock()
        self.service.storage.find_zones.return_value = [
            RoObject(id=CentralZoneTestCase.zone__id),
            RoObject(id=CentralZoneTestCase.zone__id_2)
        ]

        res = self.service.sync_zones(self.context)
        t, ctx = designate.central.service.policy.check.call_args[0]
        self.assertEqual('diagnostics_sync_zones', t)
        self.assertEqual(2, len(res))

    def test_sync_zone(self):
        self.service._sync_zone = mock.Mock()
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id,
            name='n',
            tenant_id='tid',
        )

        self.service.sync_zone(self.context,
                               CentralZoneTestCase.zone__id)

        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('diagnostics_sync_zone', t)
        self.assertEqual({'project_id': 'tid',
                          'zone_id': CentralZoneTestCase.zone__id,
                          'zone_name': 'n'}, target)

    def test_sync_record(self):
        self.service.storage.get_zone.return_value = RoObject(
            id=CentralZoneTestCase.zone__id,
            name='n',
            tenant_id='tid',
        )
        self.service.storage.get_recordset.return_value = RoObject(
            name='n',
        )

        self.service.sync_record(
            self.context, CentralZoneTestCase.zone__id,
            CentralZoneTestCase.recordset__id,
            CentralZoneTestCase.record__id)

        t, ctx, target = designate.central.service.policy.check.call_args[0]
        self.assertEqual('diagnostics_sync_record', t)
        self.assertEqual({
            'zone_id': CentralZoneTestCase.zone__id,
            'zone_name': 'n',
            'record_id': CentralZoneTestCase.record__id,
            'recordset_id': CentralZoneTestCase.recordset__id,
            'recordset_name': 'n',
            'project_id': 'tid'}, target)

    def test_ping(self):
        self.service.storage.ping.return_value = True
        r = self.service.ping(self.context)
        self.assertEqual({'status': None}, r['backend'])
        self.assertTrue(r['status'])
        self.assertTrue(r['storage'])

    def test_ping2(self):
        self.service.storage.ping.return_value = False
        r = self.service.ping(self.context)
        self.assertEqual({'status': None}, r['backend'])
        self.assertFalse(r['status'])
        self.assertFalse(r['storage'])

    def test_determine_floatingips(self):
        self.context = mock.Mock()
        self.context.project_id = 'tnt'
        self.service.find_records = mock.Mock(return_value=[
            RoObject(managed_extra='')
        ])

        fips = {}
        data, invalid = self.service._determine_floatingips(
            self.context, fips)
        self.assertEqual({}, data)
        self.assertEqual([], invalid)

    def test_determine_floatingips_with_data(self):
        self.context = mock.Mock()
        self.context.project_id = 2
        self.service.find_records = mock.Mock(return_value=[
            RoObject(managed_extra=1, managed_tenant_id=1),
            RoObject(managed_extra=2, managed_tenant_id=2),
        ])

        fips = {
            'k': {'address': 1},
            'k2': {'address': 2},
        }
        data, invalid = self.service._determine_floatingips(
            self.context, fips)
        self.assertEqual(1, len(invalid))
        self.assertEqual(1, invalid[0].managed_tenant_id)
        self.assertEqual(data['k'], ({'address': 1}, None))

    def test_generate_soa_refresh_interval(self):
        central_service = self.central_service
        with random_seed(42):
            refresh_time = central_service._generate_soa_refresh_interval()
            self.assertEqual(3563, refresh_time)


class IsSubzoneTestCase(CentralBasic):
    def setUp(self):
        super(IsSubzoneTestCase, self).setUp()

        def find_zone(ctx, criterion):
            LOG.debug("Calling find_zone on %r" % criterion)
            if criterion['name'] == 'example.com.':
                LOG.debug("Returning %r" % criterion['name'])
                return criterion['name']

            LOG.debug("Not found")
            raise exceptions.ZoneNotFound

        self.service.storage.find_zone = find_zone

    def test_is_subzone_false(self):
        r = self.service._is_subzone(self.context, 'com',
                                     CentralZoneTestCase.pool__id)
        self.assertFalse(r)

    def FIXME_test_is_subzone_false2(self):
        r = self.service._is_subzone(self.context, 'com.',
                                     CentralZoneTestCase.pool__id)
        self.assertEqual('com.', r)

    def FIXME_test_is_subzone_false3(self):
        r = self.service._is_subzone(self.context, 'example.com.',
                                     CentralZoneTestCase.pool__id)
        self.assertEqual('example.com.', r)

    def test_is_subzone_false4(self):
        r = self.service._is_subzone(
            self.context, 'foo.a.b.example.com.',
            CentralZoneTestCase.pool__id)
        self.assertEqual('example.com.', r)


class CentralZoneExportTests(CentralBasic):
    def setUp(self):
        super(CentralZoneExportTests, self).setUp()

        def storage_find_tld(c, d):
            if d['name'] not in ('org',):
                raise exceptions.TldNotFound

        self.service.storage.find_tld = storage_find_tld

    def test_create_zone_export(self):
        self.context = mock.Mock()
        self.context.project_id = 't'

        self.service.storage.get_zone.return_value = RoObject(
            name='example.com.',
            id=CentralZoneTestCase.zone__id
        )

        self.service.storage.create_zone_export = mock.Mock(
            return_value=RwObject(
                id=CentralZoneTestCase.zone_export__id,
                zone_id=CentralZoneTestCase.zone__id,
                task_type='EXPORT',
                status='PENDING',
                message=None,
                tenant_id='t',
                location=None,
            )
        )

        self.service.zone_api.start_zone_export = mock.Mock()

        out = self.service.create_zone_export(
            self.context,
            CentralZoneTestCase.zone_export__id
        )
        self.assertEqual(CentralZoneTestCase.zone__id, out.zone_id)
        self.assertEqual('PENDING', out.status)
        self.assertEqual('EXPORT', out.task_type)
        self.assertIsNone(out.message)
        self.assertEqual('t', out.tenant_id)

    def test_get_zone_export(self):
        self.context = mock.Mock()
        self.context.project_id = 't'

        self.service.storage.get_zone_export.return_value = RoObject(
                zone_id=CentralZoneTestCase.zone__id,
                task_type='EXPORT',
                status='PENDING',
                message=None,
                tenant_id='t'
        )

        out = self.service.get_zone_export(
            self.context,
            CentralZoneTestCase.zone_export__id)

        n, ctx, target = designate.central.service.policy.check.call_args[0]

        # Check arguments to policy
        self.assertEqual('t', target['project_id'])

        # Check output
        self.assertEqual(CentralZoneTestCase.zone__id, out.zone_id)
        self.assertEqual('PENDING', out.status)
        self.assertEqual('EXPORT', out.task_type)
        self.assertIsNone(out.message)
        self.assertEqual('t', out.tenant_id)

    def test_find_zone_exports(self):
        self.context = mock.Mock()
        self.context.project_id = 't'
        self.service.storage.find_zone_exports = mock.Mock()

        self.service.find_zone_exports(self.context)

        self.assertTrue(self.service.storage.find_zone_exports.called)
        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('find_zone_exports', pcheck)

    def test_delete_zone_export(self):
        self.context = mock.Mock()
        self.context.project_id = 't'

        self.service.storage.delete_zone_export = mock.Mock(
            return_value=RoObject(
                zone_id=CentralZoneTestCase.zone__id,
                task_type='EXPORT',
                status='PENDING',
                message=None,
                tenant_id='t'
            )
        )

        out = self.service.delete_zone_export(
            self.context,
            CentralZoneTestCase.zone_export__id)

        self.assertTrue(self.service.storage.delete_zone_export.called)

        self.assertEqual(CentralZoneTestCase.zone__id, out.zone_id)
        self.assertEqual('PENDING', out.status)
        self.assertEqual('EXPORT', out.task_type)
        self.assertIsNone(out.message)
        self.assertEqual('t', out.tenant_id)

        self.assertTrue(designate.central.service.policy.check.called)
        pcheck, ctx, target = \
            designate.central.service.policy.check.call_args[0]
        self.assertEqual('delete_zone_export', pcheck)
        self.assertEqual(pcheck, 'delete_zone_export')


class CentralStatusTests(CentralBasic):

    def test_update_zone_or_record_status_no_zone(self):
        zone = RwObject(
                    action='UPDATE',
                    status='SUCCESS',
                    serial=0,
                )
        dom, deleted = self.service._update_zone_or_record_status(
            zone, 'NO_ZONE', 0)

        self.assertEqual(dom.action, 'CREATE')
        self.assertEqual(dom.status, 'ERROR')


class CentralQuotaTest(unittest.TestCase):

    def setUp(self):
        self.CONF = cfg_fixture.Config(cfg.CONF)
        cfg.CONF([], project='designate')
        self.CONF.config(quota_driver="noop")
        self.context = mock.Mock()
        self.zone = mock.Mock()
        self.quotas_of_one = {'zones': 1,
                              'zone_recordsets': 1,
                              'zone_records': 1,
                              'recordset_records': 1,
                              'api_export_size': 1}

    @patch('designate.central.service.storage')
    @patch('designate.central.service.quota')
    def test_zone_record_quota_allows_lowering_value(self, quota, storage):
        service = Service()
        service.storage.count_records.return_value = 10

        recordset = mock.Mock()
        recordset.managed = False
        recordset.records = ['1.1.1.%i' % (i + 1) for i in range(5)]

        service._enforce_record_quota(
            self.context, self.zone, recordset
        )

        # Ensure we check against the number of records that will
        # result in the API call. The 5 value is as if there were 10
        # unmanaged records unders a single recordset. We find 10
        # total - 10 for the recordset being passed in and add the 5
        # from the new recordset.
        check_zone_records = mock.call(
            self.context, self.zone.tenant_id, zone_records=10 - 10 + 5
        )
        assert check_zone_records in service.quota.limit_check.mock_calls

        # Check the recordset limit as well
        check_recordset_records = mock.call(
            self.context, self.zone.tenant_id, recordset_records=5
        )
        assert check_recordset_records in service.quota.limit_check.mock_calls

    @patch('designate.quota.base.Quota.get_quotas')
    @patch('designate.central.service.storage')
    def test_enforce_zone_quota(self, storage, mock_get_quotas):
        service = Service()
        mock_get_quotas.return_value = self.quotas_of_one

        # Test creating one zone, 1 quota, no existing zones
        service.storage.count_zones.return_value = 0
        self.assertIsNone(service._enforce_zone_quota(self.context,
                                                      'fake_project_id'))

        # Test creating one zone, 1 quota, one existing zone
        service.storage.count_zones.return_value = 1
        self.assertRaises(exceptions.OverQuota, service._enforce_zone_quota,
                          self.context, 'fake_project_id')

    @patch('designate.quota.base.Quota.get_quotas')
    @patch('designate.central.service.storage')
    def test_enforce_recordset_quota(self, storage, mock_get_quotas):
        service = Service()
        mock_get_quotas.return_value = self.quotas_of_one

        # Test creating one recordset, 1 quota, no existing recordsets
        service.storage.count_recordsets.return_value = 0
        self.assertIsNone(service._enforce_recordset_quota(self.context,
                                                           self.zone))

        # Test creating one recordset, 1 quota, one existing recordset
        service.storage.count_recordsets.return_value = 1
        self.assertRaises(exceptions.OverQuota,
                          service._enforce_recordset_quota,
                          self.context, self.zone)

    @patch('designate.quota.base.Quota.get_quotas')
    @patch('designate.central.service.storage')
    def test_enforce_record_quota(self, storage, mock_get_quotas):
        service = Service()
        mock_get_quotas.return_value = self.quotas_of_one

        service.storage.count_records.side_effect = [
            0, 0,
            1, 0,
            0, 1,
            1, 1,
            1, 1,
        ]

        managed_recordset = mock.Mock()
        managed_recordset.managed = True

        recordset_one_record = mock.Mock()
        recordset_one_record.managed = False
        recordset_one_record.records = ['192.0.2.1']

        # Test that managed recordsets have no quota limit
        self.assertIsNone(service._enforce_record_quota(self.context,
                                                        self.zone,
                                                        managed_recordset))
        service.storage.count_records.assert_not_called()

        # Test creating recordset with one record, no existing zone records,
        # no existing recordsets
        self.assertIsNone(service._enforce_record_quota(self.context,
                                                        self.zone,
                                                        recordset_one_record))

        # Test creating recordset with one record, one existing zone record,
        # no exiting recordsets
        self.assertRaises(exceptions.OverQuota, service._enforce_record_quota,
                          self.context, self.zone, recordset_one_record)

        # Test creating recordset with one record, one existing zone record,
        # no exiting recordsets
        # Note: Recordsets replace the existing recordset
        self.assertIsNone(service._enforce_record_quota(self.context,
                                                        self.zone,
                                                        recordset_one_record))

        # Test creating recordset with one record, no existing zone record,
        # one exiting recordsets
        # Note: Recordsets replace the existing recordset
        self.assertIsNone(service._enforce_record_quota(self.context,
                                                        self.zone,
                                                        recordset_one_record))

        recordset_two_record = mock.Mock()
        recordset_two_record.managed = False
        recordset_two_record.records = ['192.0.2.1', '192.0.2.2']

        # Test creating recordset with two records, one existing zone record,
        # one exiting recordsets
        self.assertRaises(exceptions.OverQuota, service._enforce_record_quota,
                          self.context, self.zone, recordset_two_record)
