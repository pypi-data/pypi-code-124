# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetNetblockIPRangesResult',
    'AwaitableGetNetblockIPRangesResult',
    'get_netblock_ip_ranges',
    'get_netblock_ip_ranges_output',
]

@pulumi.output_type
class GetNetblockIPRangesResult:
    """
    A collection of values returned by getNetblockIPRanges.
    """
    def __init__(__self__, cidr_blocks=None, cidr_blocks_ipv4s=None, cidr_blocks_ipv6s=None, id=None, range_type=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError("Expected argument 'cidr_blocks' to be a list")
        pulumi.set(__self__, "cidr_blocks", cidr_blocks)
        if cidr_blocks_ipv4s and not isinstance(cidr_blocks_ipv4s, list):
            raise TypeError("Expected argument 'cidr_blocks_ipv4s' to be a list")
        pulumi.set(__self__, "cidr_blocks_ipv4s", cidr_blocks_ipv4s)
        if cidr_blocks_ipv6s and not isinstance(cidr_blocks_ipv6s, list):
            raise TypeError("Expected argument 'cidr_blocks_ipv6s' to be a list")
        pulumi.set(__self__, "cidr_blocks_ipv6s", cidr_blocks_ipv6s)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if range_type and not isinstance(range_type, str):
            raise TypeError("Expected argument 'range_type' to be a str")
        pulumi.set(__self__, "range_type", range_type)

    @property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[str]:
        """
        Retrieve list of all CIDR blocks.
        """
        return pulumi.get(self, "cidr_blocks")

    @property
    @pulumi.getter(name="cidrBlocksIpv4s")
    def cidr_blocks_ipv4s(self) -> Sequence[str]:
        """
        Retrieve list of the IPv4 CIDR blocks
        """
        return pulumi.get(self, "cidr_blocks_ipv4s")

    @property
    @pulumi.getter(name="cidrBlocksIpv6s")
    def cidr_blocks_ipv6s(self) -> Sequence[str]:
        """
        Retrieve list of the IPv6 CIDR blocks, if available.
        """
        return pulumi.get(self, "cidr_blocks_ipv6s")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="rangeType")
    def range_type(self) -> Optional[str]:
        return pulumi.get(self, "range_type")


class AwaitableGetNetblockIPRangesResult(GetNetblockIPRangesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetblockIPRangesResult(
            cidr_blocks=self.cidr_blocks,
            cidr_blocks_ipv4s=self.cidr_blocks_ipv4s,
            cidr_blocks_ipv6s=self.cidr_blocks_ipv6s,
            id=self.id,
            range_type=self.range_type)


def get_netblock_ip_ranges(range_type: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetblockIPRangesResult:
    """
    Use this data source to get the IP addresses from different special IP ranges on Google Cloud Platform.

    ## Example Usage
    ### Cloud Ranges

    ```python
    import pulumi
    import pulumi_gcp as gcp

    netblock = gcp.compute.get_netblock_ip_ranges()
    pulumi.export("cidrBlocks", netblock.cidr_blocks)
    pulumi.export("cidrBlocksIpv4", netblock.cidr_blocks_ipv4s)
    pulumi.export("cidrBlocksIpv6", netblock.cidr_blocks_ipv6s)
    ```
    ### Allow Health Checks

    ```python
    import pulumi
    import pulumi_gcp as gcp

    legacy_hcs = gcp.compute.get_netblock_ip_ranges(range_type="legacy-health-checkers")
    default = gcp.compute.Network("default")
    allow_hcs = gcp.compute.Firewall("allow-hcs",
        network=default.name,
        allows=[gcp.compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["80"],
        )],
        source_ranges=legacy_hcs.cidr_blocks_ipv4s)
    ```


    :param str range_type: The type of range for which to provide results.
    """
    __args__ = dict()
    __args__['rangeType'] = range_type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getNetblockIPRanges:getNetblockIPRanges', __args__, opts=opts, typ=GetNetblockIPRangesResult).value

    return AwaitableGetNetblockIPRangesResult(
        cidr_blocks=__ret__.cidr_blocks,
        cidr_blocks_ipv4s=__ret__.cidr_blocks_ipv4s,
        cidr_blocks_ipv6s=__ret__.cidr_blocks_ipv6s,
        id=__ret__.id,
        range_type=__ret__.range_type)


@_utilities.lift_output_func(get_netblock_ip_ranges)
def get_netblock_ip_ranges_output(range_type: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetblockIPRangesResult]:
    """
    Use this data source to get the IP addresses from different special IP ranges on Google Cloud Platform.

    ## Example Usage
    ### Cloud Ranges

    ```python
    import pulumi
    import pulumi_gcp as gcp

    netblock = gcp.compute.get_netblock_ip_ranges()
    pulumi.export("cidrBlocks", netblock.cidr_blocks)
    pulumi.export("cidrBlocksIpv4", netblock.cidr_blocks_ipv4s)
    pulumi.export("cidrBlocksIpv6", netblock.cidr_blocks_ipv6s)
    ```
    ### Allow Health Checks

    ```python
    import pulumi
    import pulumi_gcp as gcp

    legacy_hcs = gcp.compute.get_netblock_ip_ranges(range_type="legacy-health-checkers")
    default = gcp.compute.Network("default")
    allow_hcs = gcp.compute.Firewall("allow-hcs",
        network=default.name,
        allows=[gcp.compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["80"],
        )],
        source_ranges=legacy_hcs.cidr_blocks_ipv4s)
    ```


    :param str range_type: The type of range for which to provide results.
    """
    ...
