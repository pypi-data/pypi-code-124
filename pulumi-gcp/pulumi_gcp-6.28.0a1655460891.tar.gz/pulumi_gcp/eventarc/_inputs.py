# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'TriggerDestinationArgs',
    'TriggerDestinationCloudRunServiceArgs',
    'TriggerDestinationGkeArgs',
    'TriggerMatchingCriteriaArgs',
    'TriggerTransportArgs',
    'TriggerTransportPubsubArgs',
]

@pulumi.input_type
class TriggerDestinationArgs:
    def __init__(__self__, *,
                 cloud_function: Optional[pulumi.Input[str]] = None,
                 cloud_run_service: Optional[pulumi.Input['TriggerDestinationCloudRunServiceArgs']] = None,
                 gke: Optional[pulumi.Input['TriggerDestinationGkeArgs']] = None,
                 workflow: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cloud_function: [WARNING] Configuring a Cloud Function in Trigger is not supported as of today. The Cloud Function resource name. Format: projects/{project}/locations/{location}/functions/{function}
        :param pulumi.Input['TriggerDestinationCloudRunServiceArgs'] cloud_run_service: Cloud Run fully-managed service that receives the events. The service should be running in the same project of the trigger.
        :param pulumi.Input['TriggerDestinationGkeArgs'] gke: A GKE service capable of receiving events. The service should be running in the same project as the trigger.
        :param pulumi.Input[str] workflow: The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: `projects/{project}/locations/{location}/workflows/{workflow}`
        """
        if cloud_function is not None:
            pulumi.set(__self__, "cloud_function", cloud_function)
        if cloud_run_service is not None:
            pulumi.set(__self__, "cloud_run_service", cloud_run_service)
        if gke is not None:
            pulumi.set(__self__, "gke", gke)
        if workflow is not None:
            pulumi.set(__self__, "workflow", workflow)

    @property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> Optional[pulumi.Input[str]]:
        """
        [WARNING] Configuring a Cloud Function in Trigger is not supported as of today. The Cloud Function resource name. Format: projects/{project}/locations/{location}/functions/{function}
        """
        return pulumi.get(self, "cloud_function")

    @cloud_function.setter
    def cloud_function(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_function", value)

    @property
    @pulumi.getter(name="cloudRunService")
    def cloud_run_service(self) -> Optional[pulumi.Input['TriggerDestinationCloudRunServiceArgs']]:
        """
        Cloud Run fully-managed service that receives the events. The service should be running in the same project of the trigger.
        """
        return pulumi.get(self, "cloud_run_service")

    @cloud_run_service.setter
    def cloud_run_service(self, value: Optional[pulumi.Input['TriggerDestinationCloudRunServiceArgs']]):
        pulumi.set(self, "cloud_run_service", value)

    @property
    @pulumi.getter
    def gke(self) -> Optional[pulumi.Input['TriggerDestinationGkeArgs']]:
        """
        A GKE service capable of receiving events. The service should be running in the same project as the trigger.
        """
        return pulumi.get(self, "gke")

    @gke.setter
    def gke(self, value: Optional[pulumi.Input['TriggerDestinationGkeArgs']]):
        pulumi.set(self, "gke", value)

    @property
    @pulumi.getter
    def workflow(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the Workflow whose Executions are triggered by the events. The Workflow resource should be deployed in the same project as the trigger. Format: `projects/{project}/locations/{location}/workflows/{workflow}`
        """
        return pulumi.get(self, "workflow")

    @workflow.setter
    def workflow(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workflow", value)


@pulumi.input_type
class TriggerDestinationCloudRunServiceArgs:
    def __init__(__self__, *,
                 service: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] service: Required. Name of the GKE service.
        :param pulumi.Input[str] path: Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        :param pulumi.Input[str] region: Required. The region the Cloud Run service is deployed in.
        """
        pulumi.set(__self__, "service", service)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        Required. Name of the GKE service.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The region the Cloud Run service is deployed in.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class TriggerDestinationGkeArgs:
    def __init__(__self__, *,
                 cluster: pulumi.Input[str],
                 location: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 service: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cluster: Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created.
        :param pulumi.Input[str] location: Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters.
        :param pulumi.Input[str] namespace: Required. The namespace the GKE service is running in.
        :param pulumi.Input[str] service: Required. Name of the GKE service.
        :param pulumi.Input[str] path: Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "service", service)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[str]:
        """
        Required. The name of the cluster the GKE service is running in. The cluster must be running in the same project as the trigger being created.
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Required. The name of the Google Compute Engine in which the cluster resides, which can either be compute zone (for example, us-central1-a) for the zonal clusters or region (for example, us-central1) for regional clusters.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        Required. The namespace the GKE service is running in.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        Required. Name of the GKE service.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The relative path on the GKE service the events should be sent to. The value must conform to the definition of a URI path segment (section 3.3 of RFC2396). Examples: "/route", "route", "route/subroute".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


@pulumi.input_type
class TriggerMatchingCriteriaArgs:
    def __init__(__self__, *,
                 attribute: pulumi.Input[str],
                 value: pulumi.Input[str],
                 operator: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] attribute: Required. The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute.
        :param pulumi.Input[str] value: Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values.
        :param pulumi.Input[str] operator: Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is `match-path-pattern`.
        """
        pulumi.set(__self__, "attribute", attribute)
        pulumi.set(__self__, "value", value)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)

    @property
    @pulumi.getter
    def attribute(self) -> pulumi.Input[str]:
        """
        Required. The name of a CloudEvents attribute. Currently, only a subset of attributes are supported for filtering. All triggers MUST provide a filter for the 'type' attribute.
        """
        return pulumi.get(self, "attribute")

    @attribute.setter
    def attribute(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Required. The value for the attribute. See https://cloud.google.com/eventarc/docs/creating-triggers#trigger-gcloud for available values.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is `match-path-pattern`.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator", value)


@pulumi.input_type
class TriggerTransportArgs:
    def __init__(__self__, *,
                 pubsubs: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTransportPubsubArgs']]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['TriggerTransportPubsubArgs']]] pubsubs: The Pub/Sub topic and subscription used by Eventarc as delivery intermediary.
        """
        if pubsubs is not None:
            pulumi.set(__self__, "pubsubs", pubsubs)

    @property
    @pulumi.getter
    def pubsubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTransportPubsubArgs']]]]:
        """
        The Pub/Sub topic and subscription used by Eventarc as delivery intermediary.
        """
        return pulumi.get(self, "pubsubs")

    @pubsubs.setter
    def pubsubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTransportPubsubArgs']]]]):
        pulumi.set(self, "pubsubs", value)


@pulumi.input_type
class TriggerTransportPubsubArgs:
    def __init__(__self__, *,
                 subscription: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] subscription: -
               Output only. The name of the Pub/Sub subscription created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}`.
        :param pulumi.Input[str] topic: Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished` only. The topic you provide here will not be deleted by Eventarc at trigger deletion.
        """
        if subscription is not None:
            pulumi.set(__self__, "subscription", subscription)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def subscription(self) -> Optional[pulumi.Input[str]]:
        """
        -
        Output only. The name of the Pub/Sub subscription created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}`.
        """
        return pulumi.get(self, "subscription")

    @subscription.setter
    def subscription(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{PROJECT_ID}/topics/{TOPIC_NAME}. You may set an existing topic for triggers of the type google.cloud.pubsub.topic.v1.messagePublished` only. The topic you provide here will not be deleted by Eventarc at trigger deletion.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


