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
from agilicus_api.model.certificate_transparency_settings import CertificateTransparencySettings
from agilicus_api.model.content_type_options_settings import ContentTypeOptionsSettings
from agilicus_api.model.cors_settings import CORSSettings
from agilicus_api.model.cross_origin_embedder_policy_settings import CrossOriginEmbedderPolicySettings
from agilicus_api.model.cross_origin_opener_policy_settings import CrossOriginOpenerPolicySettings
from agilicus_api.model.cross_origin_resource_policy_settings import CrossOriginResourcePolicySettings
from agilicus_api.model.csp_settings import CSPSettings
from agilicus_api.model.frame_options_settings import FrameOptionsSettings
from agilicus_api.model.hsts_settings import HSTSSettings
from agilicus_api.model.permitted_cross_domain_policies_settings import PermittedCrossDomainPoliciesSettings
from agilicus_api.model.referrer_policy_settings import ReferrerPolicySettings
from agilicus_api.model.xss_settings import XSSSettings
globals()['CORSSettings'] = CORSSettings
globals()['CSPSettings'] = CSPSettings
globals()['CertificateTransparencySettings'] = CertificateTransparencySettings
globals()['ContentTypeOptionsSettings'] = ContentTypeOptionsSettings
globals()['CrossOriginEmbedderPolicySettings'] = CrossOriginEmbedderPolicySettings
globals()['CrossOriginOpenerPolicySettings'] = CrossOriginOpenerPolicySettings
globals()['CrossOriginResourcePolicySettings'] = CrossOriginResourcePolicySettings
globals()['FrameOptionsSettings'] = FrameOptionsSettings
globals()['HSTSSettings'] = HSTSSettings
globals()['PermittedCrossDomainPoliciesSettings'] = PermittedCrossDomainPoliciesSettings
globals()['ReferrerPolicySettings'] = ReferrerPolicySettings
globals()['XSSSettings'] = XSSSettings
from agilicus_api.model.http_security_settings import HTTPSecuritySettings


class TestHTTPSecuritySettings(unittest.TestCase):
    """HTTPSecuritySettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHTTPSecuritySettings(self):
        """Test HTTPSecuritySettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HTTPSecuritySettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
