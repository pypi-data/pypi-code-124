"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2022.06.16
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import agilicus_api
from agilicus_api.model.application_assignment import ApplicationAssignment
from agilicus_api.model.application_monitoring_config import ApplicationMonitoringConfig
from agilicus_api.model.application_state_selector import ApplicationStateSelector
from agilicus_api.model.definition import Definition
from agilicus_api.model.environment import Environment
from agilicus_api.model.k8s_slug import K8sSlug
from agilicus_api.model.role_list import RoleList
from agilicus_api.model.roles_config import RolesConfig
from agilicus_api.model.rules_config import RulesConfig
from agilicus_api.model.workload_configuration import WorkloadConfiguration
globals()['ApplicationAssignment'] = ApplicationAssignment
globals()['ApplicationMonitoringConfig'] = ApplicationMonitoringConfig
globals()['ApplicationStateSelector'] = ApplicationStateSelector
globals()['Definition'] = Definition
globals()['Environment'] = Environment
globals()['K8sSlug'] = K8sSlug
globals()['RoleList'] = RoleList
globals()['RolesConfig'] = RolesConfig
globals()['RulesConfig'] = RulesConfig
globals()['WorkloadConfiguration'] = WorkloadConfiguration
from agilicus_api.model.application import Application


class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplication(self):
        """Test Application"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Application()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
