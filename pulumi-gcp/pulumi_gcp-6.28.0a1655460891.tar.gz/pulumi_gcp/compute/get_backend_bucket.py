# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetBackendBucketResult',
    'AwaitableGetBackendBucketResult',
    'get_backend_bucket',
    'get_backend_bucket_output',
]

@pulumi.output_type
class GetBackendBucketResult:
    """
    A collection of values returned by getBackendBucket.
    """
    def __init__(__self__, bucket_name=None, cdn_policies=None, creation_timestamp=None, custom_response_headers=None, description=None, edge_security_policy=None, enable_cdn=None, id=None, name=None, project=None, self_link=None):
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if cdn_policies and not isinstance(cdn_policies, list):
            raise TypeError("Expected argument 'cdn_policies' to be a list")
        pulumi.set(__self__, "cdn_policies", cdn_policies)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if custom_response_headers and not isinstance(custom_response_headers, list):
            raise TypeError("Expected argument 'custom_response_headers' to be a list")
        pulumi.set(__self__, "custom_response_headers", custom_response_headers)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if edge_security_policy and not isinstance(edge_security_policy, str):
            raise TypeError("Expected argument 'edge_security_policy' to be a str")
        pulumi.set(__self__, "edge_security_policy", edge_security_policy)
        if enable_cdn and not isinstance(enable_cdn, bool):
            raise TypeError("Expected argument 'enable_cdn' to be a bool")
        pulumi.set(__self__, "enable_cdn", enable_cdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="cdnPolicies")
    def cdn_policies(self) -> Sequence['outputs.GetBackendBucketCdnPolicyResult']:
        return pulumi.get(self, "cdn_policies")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(self) -> Sequence[str]:
        return pulumi.get(self, "custom_response_headers")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> str:
        return pulumi.get(self, "edge_security_policy")

    @property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> bool:
        return pulumi.get(self, "enable_cdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")


class AwaitableGetBackendBucketResult(GetBackendBucketResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackendBucketResult(
            bucket_name=self.bucket_name,
            cdn_policies=self.cdn_policies,
            creation_timestamp=self.creation_timestamp,
            custom_response_headers=self.custom_response_headers,
            description=self.description,
            edge_security_policy=self.edge_security_policy,
            enable_cdn=self.enable_cdn,
            id=self.id,
            name=self.name,
            project=self.project,
            self_link=self.self_link)


def get_backend_bucket(name: Optional[str] = None,
                       project: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackendBucketResult:
    """
    Get information about a BackendBucket.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_backend_bucket = gcp.compute.get_backend_bucket(name="my-backend")
    ```


    :param str name: Name of the resource.
    :param str project: The ID of the project in which the resource belongs. If it
           is not provided, the provider project is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getBackendBucket:getBackendBucket', __args__, opts=opts, typ=GetBackendBucketResult).value

    return AwaitableGetBackendBucketResult(
        bucket_name=__ret__.bucket_name,
        cdn_policies=__ret__.cdn_policies,
        creation_timestamp=__ret__.creation_timestamp,
        custom_response_headers=__ret__.custom_response_headers,
        description=__ret__.description,
        edge_security_policy=__ret__.edge_security_policy,
        enable_cdn=__ret__.enable_cdn,
        id=__ret__.id,
        name=__ret__.name,
        project=__ret__.project,
        self_link=__ret__.self_link)


@_utilities.lift_output_func(get_backend_bucket)
def get_backend_bucket_output(name: Optional[pulumi.Input[str]] = None,
                              project: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackendBucketResult]:
    """
    Get information about a BackendBucket.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_backend_bucket = gcp.compute.get_backend_bucket(name="my-backend")
    ```


    :param str name: Name of the resource.
    :param str project: The ID of the project in which the resource belongs. If it
           is not provided, the provider project is used.
    """
    ...
