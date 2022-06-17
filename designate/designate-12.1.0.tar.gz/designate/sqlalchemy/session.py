# Copyright 2010 United States Government as represented by the
#   Administrator of the National Aeronautics and Space Administration.
#   All Rights Reserved.
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

"""Session Handling for SQLAlchemy backend."""

from oslo_config import cfg
from oslo_db.sqlalchemy import session
from oslo_log import log as logging


LOG = logging.getLogger(__name__)

CONF = cfg.CONF


_FACADES = {}


def _create_facade_lazily(cfg_group, connection=None, discriminator=None):
    connection = connection or cfg.CONF[cfg_group].connection
    cache_name = "%s:%s" % (cfg_group, discriminator)

    if cache_name not in _FACADES:
        conf = dict(cfg.CONF[cfg_group].items())
        _FACADES[cache_name] = session.EngineFacade(
            connection,
            **conf
        )

    return _FACADES[cache_name]


def get_engine(cfg_group):
    facade = _create_facade_lazily(cfg_group)
    return facade.get_engine()


def get_session(cfg_group, connection=None, discriminator=None, **kwargs):
    facade = _create_facade_lazily(cfg_group, connection, discriminator)
    return facade.get_session(**kwargs)
