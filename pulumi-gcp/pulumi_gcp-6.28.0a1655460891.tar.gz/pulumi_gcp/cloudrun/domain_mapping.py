# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DomainMappingArgs', 'DomainMapping']

@pulumi.input_type
class DomainMappingArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 metadata: pulumi.Input['DomainMappingMetadataArgs'],
                 spec: pulumi.Input['DomainMappingSpecArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DomainMapping resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input['DomainMappingMetadataArgs'] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input['DomainMappingSpecArgs'] spec: The spec for this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "metadata", metadata)
        pulumi.set(__self__, "spec", spec)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the cloud run instance. eg us-central1
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Input['DomainMappingMetadataArgs']:
        """
        Metadata associated with this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: pulumi.Input['DomainMappingMetadataArgs']):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['DomainMappingSpecArgs']:
        """
        The spec for this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['DomainMappingSpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _DomainMappingState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['DomainMappingMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input['DomainMappingSpecArgs']] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input['DomainMappingStatusArgs']]]] = None):
        """
        Input properties used for looking up and filtering DomainMapping resources.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input['DomainMappingMetadataArgs'] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input['DomainMappingSpecArgs'] spec: The spec for this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input['DomainMappingStatusArgs']]] statuses: The current status of the DomainMapping.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if statuses is not None:
            pulumi.set(__self__, "statuses", statuses)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the cloud run instance. eg us-central1
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['DomainMappingMetadataArgs']]:
        """
        Metadata associated with this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['DomainMappingMetadataArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['DomainMappingSpecArgs']]:
        """
        The spec for this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['DomainMappingSpecArgs']]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainMappingStatusArgs']]]]:
        """
        The current status of the DomainMapping.
        """
        return pulumi.get(self, "statuses")

    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainMappingStatusArgs']]]]):
        pulumi.set(self, "statuses", value)


class DomainMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
                 __props__=None):
        """
        Resource to hold the state and status of a user's domain mapping.

        To get more information about DomainMapping, see:

        * [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.domainmappings)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/run/docs/mapping-custom-domains)

        ## Example Usage
        ### Cloud Run Domain Mapping Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_service = gcp.cloudrun.Service("defaultService",
            location="us-central1",
            metadata=gcp.cloudrun.ServiceMetadataArgs(
                namespace="my-project-name",
            ),
            template=gcp.cloudrun.ServiceTemplateArgs(
                spec=gcp.cloudrun.ServiceTemplateSpecArgs(
                    containers=[gcp.cloudrun.ServiceTemplateSpecContainerArgs(
                        image="us-docker.pkg.dev/cloudrun/container/hello",
                    )],
                ),
            ))
        default_domain_mapping = gcp.cloudrun.DomainMapping("defaultDomainMapping",
            location="us-central1",
            metadata=gcp.cloudrun.DomainMappingMetadataArgs(
                namespace="my-project-name",
            ),
            spec=gcp.cloudrun.DomainMappingSpecArgs(
                route_name=default_service.name,
            ))
        ```

        ## Import

        DomainMapping can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default locations/{{location}}/namespaces/{{project}}/domainmappings/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default {{location}}/{{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']] spec: The spec for this DomainMapping.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource to hold the state and status of a user's domain mapping.

        To get more information about DomainMapping, see:

        * [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.domainmappings)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/run/docs/mapping-custom-domains)

        ## Example Usage
        ### Cloud Run Domain Mapping Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_service = gcp.cloudrun.Service("defaultService",
            location="us-central1",
            metadata=gcp.cloudrun.ServiceMetadataArgs(
                namespace="my-project-name",
            ),
            template=gcp.cloudrun.ServiceTemplateArgs(
                spec=gcp.cloudrun.ServiceTemplateSpecArgs(
                    containers=[gcp.cloudrun.ServiceTemplateSpecContainerArgs(
                        image="us-docker.pkg.dev/cloudrun/container/hello",
                    )],
                ),
            ))
        default_domain_mapping = gcp.cloudrun.DomainMapping("defaultDomainMapping",
            location="us-central1",
            metadata=gcp.cloudrun.DomainMappingMetadataArgs(
                namespace="my-project-name",
            ),
            spec=gcp.cloudrun.DomainMappingSpecArgs(
                route_name=default_service.name,
            ))
        ```

        ## Import

        DomainMapping can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default locations/{{location}}/namespaces/{{project}}/domainmappings/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default {{location}}/{{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudrun/domainMapping:DomainMapping default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param DomainMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainMappingArgs.__new__(DomainMappingArgs)

            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if metadata is None and not opts.urn:
                raise TypeError("Missing required property 'metadata'")
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["statuses"] = None
        super(DomainMapping, __self__).__init__(
            'gcp:cloudrun/domainMapping:DomainMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
            statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainMappingStatusArgs']]]]] = None) -> 'DomainMapping':
        """
        Get an existing DomainMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']] spec: The spec for this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainMappingStatusArgs']]]] statuses: The current status of the DomainMapping.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainMappingState.__new__(_DomainMappingState)

        __props__.__dict__["location"] = location
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["spec"] = spec
        __props__.__dict__["statuses"] = statuses
        return DomainMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the cloud run instance. eg us-central1
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.DomainMappingMetadata']:
        """
        Metadata associated with this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name should be a [verified](https://support.google.com/webmasters/answer/9008080) domain
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.DomainMappingSpec']:
        """
        The spec for this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.DomainMappingStatus']]:
        """
        The current status of the DomainMapping.
        """
        return pulumi.get(self, "statuses")

