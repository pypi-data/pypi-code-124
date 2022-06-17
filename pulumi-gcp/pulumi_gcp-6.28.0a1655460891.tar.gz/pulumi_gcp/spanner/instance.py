# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 config: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 processing_units: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] config: The name of the instance's configuration (similar but not
               quite the same as a region) which defines the geographic placement and
               replication of your databases in this instance. It determines where your data
               is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
               In order to obtain a valid list please consult the
               [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        :param pulumi.Input[str] display_name: The descriptive name for this instance as it appears in UIs. Must be
               unique per project and between 4 and 30 characters in length.
        :param pulumi.Input[bool] force_destroy: When deleting a spanner instance, this boolean option will delete all backups of this instance.
               This must be set to true if you created a backup manually in the console.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: A unique identifier for the instance, which cannot be changed after
               the instance is created. The name must be between 6 and 30 characters
               in length.
        :param pulumi.Input[int] num_nodes: The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
               terraform.
        :param pulumi.Input[int] processing_units: The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
               in terraform.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "display_name", display_name)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if num_nodes is not None:
            pulumi.set(__self__, "num_nodes", num_nodes)
        if processing_units is not None:
            pulumi.set(__self__, "processing_units", processing_units)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input[str]:
        """
        The name of the instance's configuration (similar but not
        quite the same as a region) which defines the geographic placement and
        replication of your databases in this instance. It determines where your data
        is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
        In order to obtain a valid list please consult the
        [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input[str]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The descriptive name for this instance as it appears in UIs. Must be
        unique per project and between 4 and 30 characters in length.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        When deleting a spanner instance, this boolean option will delete all backups of this instance.
        This must be set to true if you created a backup manually in the console.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for the instance, which cannot be changed after
        the instance is created. The name must be between 6 and 30 characters
        in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
        terraform.
        """
        return pulumi.get(self, "num_nodes")

    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_nodes", value)

    @property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> Optional[pulumi.Input[int]]:
        """
        The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
        in terraform.
        """
        return pulumi.get(self, "processing_units")

    @processing_units.setter
    def processing_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "processing_units", value)

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
class _InstanceState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 processing_units: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input[str] config: The name of the instance's configuration (similar but not
               quite the same as a region) which defines the geographic placement and
               replication of your databases in this instance. It determines where your data
               is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
               In order to obtain a valid list please consult the
               [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        :param pulumi.Input[str] display_name: The descriptive name for this instance as it appears in UIs. Must be
               unique per project and between 4 and 30 characters in length.
        :param pulumi.Input[bool] force_destroy: When deleting a spanner instance, this boolean option will delete all backups of this instance.
               This must be set to true if you created a backup manually in the console.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: A unique identifier for the instance, which cannot be changed after
               the instance is created. The name must be between 6 and 30 characters
               in length.
        :param pulumi.Input[int] num_nodes: The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
               terraform.
        :param pulumi.Input[int] processing_units: The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
               in terraform.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] state: Instance status: 'CREATING' or 'READY'.
        """
        if config is not None:
            pulumi.set(__self__, "config", config)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if num_nodes is not None:
            pulumi.set(__self__, "num_nodes", num_nodes)
        if processing_units is not None:
            pulumi.set(__self__, "processing_units", processing_units)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the instance's configuration (similar but not
        quite the same as a region) which defines the geographic placement and
        replication of your databases in this instance. It determines where your data
        is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
        In order to obtain a valid list please consult the
        [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The descriptive name for this instance as it appears in UIs. Must be
        unique per project and between 4 and 30 characters in length.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        When deleting a spanner instance, this boolean option will delete all backups of this instance.
        This must be set to true if you created a backup manually in the console.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for the instance, which cannot be changed after
        the instance is created. The name must be between 6 and 30 characters
        in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
        terraform.
        """
        return pulumi.get(self, "num_nodes")

    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_nodes", value)

    @property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> Optional[pulumi.Input[int]]:
        """
        The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
        in terraform.
        """
        return pulumi.get(self, "processing_units")

    @processing_units.setter
    def processing_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "processing_units", value)

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
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Instance status: 'CREATING' or 'READY'.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 processing_units: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An isolated set of Cloud Spanner resources on which databases can be
        hosted.

        To get more information about Instance, see:

        * [API documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/spanner/)

        ## Example Usage
        ### Spanner Instance Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="regional-us-central1",
            display_name="Test Spanner Instance",
            labels={
                "foo": "bar",
            },
            num_nodes=2)
        ```
        ### Spanner Instance Processing Units

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="regional-us-central1",
            display_name="Test Spanner Instance",
            labels={
                "foo": "bar",
            },
            processing_units=200)
        ```
        ### Spanner Instance Multi Regional

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="nam-eur-asia1",
            display_name="Multi Regional Instance",
            labels={
                "foo": "bar",
            },
            num_nodes=2)
        ```

        ## Import

        Instance can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default projects/{{project}}/instances/{{name}}
        ```

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: The name of the instance's configuration (similar but not
               quite the same as a region) which defines the geographic placement and
               replication of your databases in this instance. It determines where your data
               is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
               In order to obtain a valid list please consult the
               [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        :param pulumi.Input[str] display_name: The descriptive name for this instance as it appears in UIs. Must be
               unique per project and between 4 and 30 characters in length.
        :param pulumi.Input[bool] force_destroy: When deleting a spanner instance, this boolean option will delete all backups of this instance.
               This must be set to true if you created a backup manually in the console.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: A unique identifier for the instance, which cannot be changed after
               the instance is created. The name must be between 6 and 30 characters
               in length.
        :param pulumi.Input[int] num_nodes: The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
               terraform.
        :param pulumi.Input[int] processing_units: The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
               in terraform.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An isolated set of Cloud Spanner resources on which databases can be
        hosted.

        To get more information about Instance, see:

        * [API documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/spanner/)

        ## Example Usage
        ### Spanner Instance Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="regional-us-central1",
            display_name="Test Spanner Instance",
            labels={
                "foo": "bar",
            },
            num_nodes=2)
        ```
        ### Spanner Instance Processing Units

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="regional-us-central1",
            display_name="Test Spanner Instance",
            labels={
                "foo": "bar",
            },
            processing_units=200)
        ```
        ### Spanner Instance Multi Regional

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.spanner.Instance("example",
            config="nam-eur-asia1",
            display_name="Multi Regional Instance",
            labels={
                "foo": "bar",
            },
            num_nodes=2)
        ```

        ## Import

        Instance can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default projects/{{project}}/instances/{{name}}
        ```

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:spanner/instance:Instance default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 processing_units: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = InstanceArgs.__new__(InstanceArgs)

            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["force_destroy"] = force_destroy
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["num_nodes"] = num_nodes
            __props__.__dict__["processing_units"] = processing_units
            __props__.__dict__["project"] = project
            __props__.__dict__["state"] = None
        super(Instance, __self__).__init__(
            'gcp:spanner/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            num_nodes: Optional[pulumi.Input[int]] = None,
            processing_units: Optional[pulumi.Input[int]] = None,
            project: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: The name of the instance's configuration (similar but not
               quite the same as a region) which defines the geographic placement and
               replication of your databases in this instance. It determines where your data
               is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
               In order to obtain a valid list please consult the
               [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        :param pulumi.Input[str] display_name: The descriptive name for this instance as it appears in UIs. Must be
               unique per project and between 4 and 30 characters in length.
        :param pulumi.Input[bool] force_destroy: When deleting a spanner instance, this boolean option will delete all backups of this instance.
               This must be set to true if you created a backup manually in the console.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: A unique identifier for the instance, which cannot be changed after
               the instance is created. The name must be between 6 and 30 characters
               in length.
        :param pulumi.Input[int] num_nodes: The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
               terraform.
        :param pulumi.Input[int] processing_units: The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
               in terraform.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] state: Instance status: 'CREATING' or 'READY'.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["config"] = config
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["force_destroy"] = force_destroy
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["num_nodes"] = num_nodes
        __props__.__dict__["processing_units"] = processing_units
        __props__.__dict__["project"] = project
        __props__.__dict__["state"] = state
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[str]:
        """
        The name of the instance's configuration (similar but not
        quite the same as a region) which defines the geographic placement and
        replication of your databases in this instance. It determines where your data
        is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
        In order to obtain a valid list please consult the
        [Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The descriptive name for this instance as it appears in UIs. Must be
        unique per project and between 4 and 30 characters in length.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        When deleting a spanner instance, this boolean option will delete all backups of this instance.
        This must be set to true if you created a backup manually in the console.
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique identifier for the instance, which cannot be changed after
        the instance is created. The name must be between 6 and 30 characters
        in length.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> pulumi.Output[int]:
        """
        The number of nodes allocated to this instance. Exactly one of either node_count or processing_units must be present in
        terraform.
        """
        return pulumi.get(self, "num_nodes")

    @property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> pulumi.Output[int]:
        """
        The number of processing units allocated to this instance. Exactly one of processing_units or node_count must be present
        in terraform.
        """
        return pulumi.get(self, "processing_units")

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
    def state(self) -> pulumi.Output[str]:
        """
        Instance status: 'CREATING' or 'READY'.
        """
        return pulumi.get(self, "state")

