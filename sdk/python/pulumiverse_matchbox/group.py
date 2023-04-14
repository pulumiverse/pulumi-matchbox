# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 profile: pulumi.Input[str],
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 selector: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[str] profile: Name of a Matchbox profile
        :param pulumi.Input[Mapping[str, Any]] metadata: Map of group metadata (optional, seldom used)
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        :param pulumi.Input[Mapping[str, Any]] selector: Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        pulumi.set(__self__, "profile", profile)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if selector is not None:
            pulumi.set(__self__, "selector", selector)

    @property
    @pulumi.getter
    def profile(self) -> pulumi.Input[str]:
        """
        Name of a Matchbox profile
        """
        return pulumi.get(self, "profile")

    @profile.setter
    def profile(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of group metadata (optional, seldom used)
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unqiue name for the machine matcher
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        return pulumi.get(self, "selector")

    @selector.setter
    def selector(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "selector", value)


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 selector: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering Group resources.
        :param pulumi.Input[Mapping[str, Any]] metadata: Map of group metadata (optional, seldom used)
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        :param pulumi.Input[str] profile: Name of a Matchbox profile
        :param pulumi.Input[Mapping[str, Any]] selector: Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if profile is not None:
            pulumi.set(__self__, "profile", profile)
        if selector is not None:
            pulumi.set(__self__, "selector", selector)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of group metadata (optional, seldom used)
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unqiue name for the machine matcher
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[str]]:
        """
        Name of a Matchbox profile
        """
        return pulumi.get(self, "profile")

    @profile.setter
    def profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile", value)

    @property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        return pulumi.get(self, "selector")

    @selector.setter
    def selector(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "selector", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 selector: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        ## # Group Resource

        A Group matches (one or more) machines and declares a machine should be boot with a named `profile`.

        ```python
        import pulumi
        import pulumiverse_matchbox as matchbox

        node1 = matchbox.Group("node1",
            metadata={
                "custom_variable": "machine_specific_value_here",
            },
            profile=matchbox_profile["myprofile"]["name"],
            selector={
                "mac": "52:54:00:a1:9c:ae",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] metadata: Map of group metadata (optional, seldom used)
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        :param pulumi.Input[str] profile: Name of a Matchbox profile
        :param pulumi.Input[Mapping[str, Any]] selector: Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Group Resource

        A Group matches (one or more) machines and declares a machine should be boot with a named `profile`.

        ```python
        import pulumi
        import pulumiverse_matchbox as matchbox

        node1 = matchbox.Group("node1",
            metadata={
                "custom_variable": "machine_specific_value_here",
            },
            profile=matchbox_profile["myprofile"]["name"],
            selector={
                "mac": "52:54:00:a1:9c:ae",
            })
        ```

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 selector: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if profile is None and not opts.urn:
                raise TypeError("Missing required property 'profile'")
            __props__.__dict__["profile"] = profile
            __props__.__dict__["selector"] = selector
        super(Group, __self__).__init__(
            'matchbox:index/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            profile: Optional[pulumi.Input[str]] = None,
            selector: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] metadata: Map of group metadata (optional, seldom used)
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        :param pulumi.Input[str] profile: Name of a Matchbox profile
        :param pulumi.Input[Mapping[str, Any]] selector: Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupState.__new__(_GroupState)

        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["profile"] = profile
        __props__.__dict__["selector"] = selector
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of group metadata (optional, seldom used)
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unqiue name for the machine matcher
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def profile(self) -> pulumi.Output[str]:
        """
        Name of a Matchbox profile
        """
        return pulumi.get(self, "profile")

    @property
    @pulumi.getter
    def selector(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
        """
        return pulumi.get(self, "selector")

