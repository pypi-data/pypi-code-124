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

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 managed: Optional[pulumi.Input['CertificateManagedArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 self_managed: Optional[pulumi.Input['CertificateSelfManagedArgs']] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the EdgeCache resource.
        :param pulumi.Input['CertificateManagedArgs'] managed: Configuration and state of a Managed Certificate.
               Certificate Manager provisions and renews Managed Certificates
               automatically, for as long as it's authorized to do so.
               Structure is documented below.
        :param pulumi.Input[str] name: A user-defined name of the certificate. Certificate names must be unique
               The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
               and all following characters must be a dash, underscore, letter or digit.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] scope: The scope of the certificate.
               Certificates with default scope are served from core Google data centers.
               If unsure, choose this option.
               Certificates with scope EDGE_CACHE are special-purposed certificates,
               served from non-core Google data centers.
               Currently allowed only for managed certificates.
               Default value is `DEFAULT`.
               Possible values are `DEFAULT` and `EDGE_CACHE`.
        :param pulumi.Input['CertificateSelfManagedArgs'] self_managed: Certificate data for a SelfManaged Certificate.
               SelfManaged Certificates are uploaded by the user. Updating such
               certificates before they expire remains the user's responsibility.
               Structure is documented below.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if self_managed is not None:
            pulumi.set(__self__, "self_managed", self_managed)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of label tags associated with the EdgeCache resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input['CertificateManagedArgs']]:
        """
        Configuration and state of a Managed Certificate.
        Certificate Manager provisions and renews Managed Certificates
        automatically, for as long as it's authorized to do so.
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input['CertificateManagedArgs']]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-defined name of the certificate. Certificate names must be unique
        The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
        and all following characters must be a dash, underscore, letter or digit.
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
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of the certificate.
        Certificates with default scope are served from core Google data centers.
        If unsure, choose this option.
        Certificates with scope EDGE_CACHE are special-purposed certificates,
        served from non-core Google data centers.
        Currently allowed only for managed certificates.
        Default value is `DEFAULT`.
        Possible values are `DEFAULT` and `EDGE_CACHE`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> Optional[pulumi.Input['CertificateSelfManagedArgs']]:
        """
        Certificate data for a SelfManaged Certificate.
        SelfManaged Certificates are uploaded by the user. Updating such
        certificates before they expire remains the user's responsibility.
        Structure is documented below.
        """
        return pulumi.get(self, "self_managed")

    @self_managed.setter
    def self_managed(self, value: Optional[pulumi.Input['CertificateSelfManagedArgs']]):
        pulumi.set(self, "self_managed", value)


@pulumi.input_type
class _CertificateState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 managed: Optional[pulumi.Input['CertificateManagedArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 self_managed: Optional[pulumi.Input['CertificateSelfManagedArgs']] = None):
        """
        Input properties used for looking up and filtering Certificate resources.
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the EdgeCache resource.
        :param pulumi.Input['CertificateManagedArgs'] managed: Configuration and state of a Managed Certificate.
               Certificate Manager provisions and renews Managed Certificates
               automatically, for as long as it's authorized to do so.
               Structure is documented below.
        :param pulumi.Input[str] name: A user-defined name of the certificate. Certificate names must be unique
               The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
               and all following characters must be a dash, underscore, letter or digit.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] scope: The scope of the certificate.
               Certificates with default scope are served from core Google data centers.
               If unsure, choose this option.
               Certificates with scope EDGE_CACHE are special-purposed certificates,
               served from non-core Google data centers.
               Currently allowed only for managed certificates.
               Default value is `DEFAULT`.
               Possible values are `DEFAULT` and `EDGE_CACHE`.
        :param pulumi.Input['CertificateSelfManagedArgs'] self_managed: Certificate data for a SelfManaged Certificate.
               SelfManaged Certificates are uploaded by the user. Updating such
               certificates before they expire remains the user's responsibility.
               Structure is documented below.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if self_managed is not None:
            pulumi.set(__self__, "self_managed", self_managed)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of label tags associated with the EdgeCache resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input['CertificateManagedArgs']]:
        """
        Configuration and state of a Managed Certificate.
        Certificate Manager provisions and renews Managed Certificates
        automatically, for as long as it's authorized to do so.
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input['CertificateManagedArgs']]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-defined name of the certificate. Certificate names must be unique
        The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
        and all following characters must be a dash, underscore, letter or digit.
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
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of the certificate.
        Certificates with default scope are served from core Google data centers.
        If unsure, choose this option.
        Certificates with scope EDGE_CACHE are special-purposed certificates,
        served from non-core Google data centers.
        Currently allowed only for managed certificates.
        Default value is `DEFAULT`.
        Possible values are `DEFAULT` and `EDGE_CACHE`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> Optional[pulumi.Input['CertificateSelfManagedArgs']]:
        """
        Certificate data for a SelfManaged Certificate.
        SelfManaged Certificates are uploaded by the user. Updating such
        certificates before they expire remains the user's responsibility.
        Structure is documented below.
        """
        return pulumi.get(self, "self_managed")

    @self_managed.setter
    def self_managed(self, value: Optional[pulumi.Input['CertificateSelfManagedArgs']]):
        pulumi.set(self, "self_managed", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 managed: Optional[pulumi.Input[pulumi.InputType['CertificateManagedArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 self_managed: Optional[pulumi.Input[pulumi.InputType['CertificateSelfManagedArgs']]] = None,
                 __props__=None):
        """
        Certificate represents a HTTP-reachable backend for an Certificate.

        > **Warning:** These resources require allow-listing to use, and are not openly available to all Cloud customers. Engage with your Cloud account team to discuss how to onboard.

        > **Warning:** All arguments including `self_managed.certificate_pem` and `self_managed.private_key_pem` will be stored in the raw
        state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/language/state/sensitive-data.html).

        ## Example Usage
        ### Certificate Manager Certificate Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.certificatemanager.DnsAuthorization("instance",
            description="The default dnss",
            domain="subdomain.hashicorptest.com")
        instance2 = gcp.certificatemanager.DnsAuthorization("instance2",
            description="The default dnss",
            domain="subdomain2.hashicorptest.com")
        default = gcp.certificatemanager.Certificate("default",
            description="The default cert",
            scope="EDGE_CACHE",
            managed=gcp.certificatemanager.CertificateManagedArgs(
                domains=[
                    instance.domain,
                    instance2.domain,
                ],
                dns_authorizations=[
                    instance.id,
                    instance2.id,
                ],
            ))
        ```

        ## Import

        Certificate can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default projects/{{project}}/locations/global/certificates/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the EdgeCache resource.
        :param pulumi.Input[pulumi.InputType['CertificateManagedArgs']] managed: Configuration and state of a Managed Certificate.
               Certificate Manager provisions and renews Managed Certificates
               automatically, for as long as it's authorized to do so.
               Structure is documented below.
        :param pulumi.Input[str] name: A user-defined name of the certificate. Certificate names must be unique
               The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
               and all following characters must be a dash, underscore, letter or digit.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] scope: The scope of the certificate.
               Certificates with default scope are served from core Google data centers.
               If unsure, choose this option.
               Certificates with scope EDGE_CACHE are special-purposed certificates,
               served from non-core Google data centers.
               Currently allowed only for managed certificates.
               Default value is `DEFAULT`.
               Possible values are `DEFAULT` and `EDGE_CACHE`.
        :param pulumi.Input[pulumi.InputType['CertificateSelfManagedArgs']] self_managed: Certificate data for a SelfManaged Certificate.
               SelfManaged Certificates are uploaded by the user. Updating such
               certificates before they expire remains the user's responsibility.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CertificateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Certificate represents a HTTP-reachable backend for an Certificate.

        > **Warning:** These resources require allow-listing to use, and are not openly available to all Cloud customers. Engage with your Cloud account team to discuss how to onboard.

        > **Warning:** All arguments including `self_managed.certificate_pem` and `self_managed.private_key_pem` will be stored in the raw
        state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/language/state/sensitive-data.html).

        ## Example Usage
        ### Certificate Manager Certificate Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.certificatemanager.DnsAuthorization("instance",
            description="The default dnss",
            domain="subdomain.hashicorptest.com")
        instance2 = gcp.certificatemanager.DnsAuthorization("instance2",
            description="The default dnss",
            domain="subdomain2.hashicorptest.com")
        default = gcp.certificatemanager.Certificate("default",
            description="The default cert",
            scope="EDGE_CACHE",
            managed=gcp.certificatemanager.CertificateManagedArgs(
                domains=[
                    instance.domain,
                    instance2.domain,
                ],
                dns_authorizations=[
                    instance.id,
                    instance2.id,
                ],
            ))
        ```

        ## Import

        Certificate can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default projects/{{project}}/locations/global/certificates/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificate:Certificate default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 managed: Optional[pulumi.Input[pulumi.InputType['CertificateManagedArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 self_managed: Optional[pulumi.Input[pulumi.InputType['CertificateSelfManagedArgs']]] = None,
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
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["managed"] = managed
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["scope"] = scope
            __props__.__dict__["self_managed"] = self_managed
        super(Certificate, __self__).__init__(
            'gcp:certificatemanager/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            managed: Optional[pulumi.Input[pulumi.InputType['CertificateManagedArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            self_managed: Optional[pulumi.Input[pulumi.InputType['CertificateSelfManagedArgs']]] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the EdgeCache resource.
        :param pulumi.Input[pulumi.InputType['CertificateManagedArgs']] managed: Configuration and state of a Managed Certificate.
               Certificate Manager provisions and renews Managed Certificates
               automatically, for as long as it's authorized to do so.
               Structure is documented below.
        :param pulumi.Input[str] name: A user-defined name of the certificate. Certificate names must be unique
               The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
               and all following characters must be a dash, underscore, letter or digit.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] scope: The scope of the certificate.
               Certificates with default scope are served from core Google data centers.
               If unsure, choose this option.
               Certificates with scope EDGE_CACHE are special-purposed certificates,
               served from non-core Google data centers.
               Currently allowed only for managed certificates.
               Default value is `DEFAULT`.
               Possible values are `DEFAULT` and `EDGE_CACHE`.
        :param pulumi.Input[pulumi.InputType['CertificateSelfManagedArgs']] self_managed: Certificate data for a SelfManaged Certificate.
               SelfManaged Certificates are uploaded by the user. Updating such
               certificates before they expire remains the user's responsibility.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CertificateState.__new__(_CertificateState)

        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["managed"] = managed
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["scope"] = scope
        __props__.__dict__["self_managed"] = self_managed
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Set of label tags associated with the EdgeCache resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def managed(self) -> pulumi.Output[Optional['outputs.CertificateManaged']]:
        """
        Configuration and state of a Managed Certificate.
        Certificate Manager provisions and renews Managed Certificates
        automatically, for as long as it's authorized to do so.
        Structure is documented below.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-defined name of the certificate. Certificate names must be unique
        The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
        and all following characters must be a dash, underscore, letter or digit.
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
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of the certificate.
        Certificates with default scope are served from core Google data centers.
        If unsure, choose this option.
        Certificates with scope EDGE_CACHE are special-purposed certificates,
        served from non-core Google data centers.
        Currently allowed only for managed certificates.
        Default value is `DEFAULT`.
        Possible values are `DEFAULT` and `EDGE_CACHE`.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> pulumi.Output[Optional['outputs.CertificateSelfManaged']]:
        """
        Certificate data for a SelfManaged Certificate.
        SelfManaged Certificates are uploaded by the user. Updating such
        certificates before they expire remains the user's responsibility.
        Structure is documented below.
        """
        return pulumi.get(self, "self_managed")

