# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 container_linux_config: Optional[pulumi.Input[str]] = None,
                 generic_config: Optional[pulumi.Input[str]] = None,
                 initrds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kernel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 raw_ignition: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] args: List of kernel arguments
        :param pulumi.Input[str] container_linux_config: CoreOS Container Linux Config (CLC) (for backwards compatibility)
        :param pulumi.Input[str] generic_config: Generic configuration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] initrds: List of URLs to init RAM filesystems
        :param pulumi.Input[str] kernel: URL of the kernel image to boot
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        """
        if args is not None:
            pulumi.set(__self__, "args", args)
        if container_linux_config is not None:
            pulumi.set(__self__, "container_linux_config", container_linux_config)
        if generic_config is not None:
            pulumi.set(__self__, "generic_config", generic_config)
        if initrds is not None:
            pulumi.set(__self__, "initrds", initrds)
        if kernel is not None:
            pulumi.set(__self__, "kernel", kernel)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if raw_ignition is not None:
            pulumi.set(__self__, "raw_ignition", raw_ignition)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of kernel arguments
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter(name="containerLinuxConfig")
    def container_linux_config(self) -> Optional[pulumi.Input[str]]:
        """
        CoreOS Container Linux Config (CLC) (for backwards compatibility)
        """
        return pulumi.get(self, "container_linux_config")

    @container_linux_config.setter
    def container_linux_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_linux_config", value)

    @property
    @pulumi.getter(name="genericConfig")
    def generic_config(self) -> Optional[pulumi.Input[str]]:
        """
        Generic configuration
        """
        return pulumi.get(self, "generic_config")

    @generic_config.setter
    def generic_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generic_config", value)

    @property
    @pulumi.getter
    def initrds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of URLs to init RAM filesystems
        """
        return pulumi.get(self, "initrds")

    @initrds.setter
    def initrds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "initrds", value)

    @property
    @pulumi.getter
    def kernel(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the kernel image to boot
        """
        return pulumi.get(self, "kernel")

    @kernel.setter
    def kernel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kernel", value)

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
    @pulumi.getter(name="rawIgnition")
    def raw_ignition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "raw_ignition")

    @raw_ignition.setter
    def raw_ignition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raw_ignition", value)


@pulumi.input_type
class _ProfileState:
    def __init__(__self__, *,
                 args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 container_linux_config: Optional[pulumi.Input[str]] = None,
                 generic_config: Optional[pulumi.Input[str]] = None,
                 initrds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kernel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 raw_ignition: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Profile resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] args: List of kernel arguments
        :param pulumi.Input[str] container_linux_config: CoreOS Container Linux Config (CLC) (for backwards compatibility)
        :param pulumi.Input[str] generic_config: Generic configuration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] initrds: List of URLs to init RAM filesystems
        :param pulumi.Input[str] kernel: URL of the kernel image to boot
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        """
        if args is not None:
            pulumi.set(__self__, "args", args)
        if container_linux_config is not None:
            pulumi.set(__self__, "container_linux_config", container_linux_config)
        if generic_config is not None:
            pulumi.set(__self__, "generic_config", generic_config)
        if initrds is not None:
            pulumi.set(__self__, "initrds", initrds)
        if kernel is not None:
            pulumi.set(__self__, "kernel", kernel)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if raw_ignition is not None:
            pulumi.set(__self__, "raw_ignition", raw_ignition)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of kernel arguments
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter(name="containerLinuxConfig")
    def container_linux_config(self) -> Optional[pulumi.Input[str]]:
        """
        CoreOS Container Linux Config (CLC) (for backwards compatibility)
        """
        return pulumi.get(self, "container_linux_config")

    @container_linux_config.setter
    def container_linux_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_linux_config", value)

    @property
    @pulumi.getter(name="genericConfig")
    def generic_config(self) -> Optional[pulumi.Input[str]]:
        """
        Generic configuration
        """
        return pulumi.get(self, "generic_config")

    @generic_config.setter
    def generic_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generic_config", value)

    @property
    @pulumi.getter
    def initrds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of URLs to init RAM filesystems
        """
        return pulumi.get(self, "initrds")

    @initrds.setter
    def initrds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "initrds", value)

    @property
    @pulumi.getter
    def kernel(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the kernel image to boot
        """
        return pulumi.get(self, "kernel")

    @kernel.setter
    def kernel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kernel", value)

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
    @pulumi.getter(name="rawIgnition")
    def raw_ignition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "raw_ignition")

    @raw_ignition.setter
    def raw_ignition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raw_ignition", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 container_linux_config: Optional[pulumi.Input[str]] = None,
                 generic_config: Optional[pulumi.Input[str]] = None,
                 initrds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kernel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 raw_ignition: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Profile Resource

        A Profile defines network boot and declarative provisioning configurations.

        ```python
        import pulumi

        config = pulumi.Config()
        # Fedora CoreOS release stream (e.g. testing, stable)
        os_stream = config.get("osStream")
        if os_stream is None:
            os_stream = "stable"
        # Fedora CoreOS version to PXE and install (e.g. 32.20200715.3.0)
        os_version = config.require("osVersion")
        kernel = f"https://builds.coreos.fedoraproject.org/prod/streams/{os_stream}/builds/{os_version}/x86_64/fedora-coreos-{os_version}-live-kernel-x86_64"
        initrd = f"https://builds.coreos.fedoraproject.org/prod/streams/{os_stream}/builds/{os_version}/x86_64/fedora-coreos-{os_version}-live-initramfs.x86_64.img"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] args: List of kernel arguments
        :param pulumi.Input[str] container_linux_config: CoreOS Container Linux Config (CLC) (for backwards compatibility)
        :param pulumi.Input[str] generic_config: Generic configuration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] initrds: List of URLs to init RAM filesystems
        :param pulumi.Input[str] kernel: URL of the kernel image to boot
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProfileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Profile Resource

        A Profile defines network boot and declarative provisioning configurations.

        ```python
        import pulumi

        config = pulumi.Config()
        # Fedora CoreOS release stream (e.g. testing, stable)
        os_stream = config.get("osStream")
        if os_stream is None:
            os_stream = "stable"
        # Fedora CoreOS version to PXE and install (e.g. 32.20200715.3.0)
        os_version = config.require("osVersion")
        kernel = f"https://builds.coreos.fedoraproject.org/prod/streams/{os_stream}/builds/{os_version}/x86_64/fedora-coreos-{os_version}-live-kernel-x86_64"
        initrd = f"https://builds.coreos.fedoraproject.org/prod/streams/{os_stream}/builds/{os_version}/x86_64/fedora-coreos-{os_version}-live-initramfs.x86_64.img"
        ```

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 container_linux_config: Optional[pulumi.Input[str]] = None,
                 generic_config: Optional[pulumi.Input[str]] = None,
                 initrds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kernel: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 raw_ignition: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            __props__.__dict__["args"] = args
            __props__.__dict__["container_linux_config"] = container_linux_config
            __props__.__dict__["generic_config"] = generic_config
            __props__.__dict__["initrds"] = initrds
            __props__.__dict__["kernel"] = kernel
            __props__.__dict__["name"] = name
            __props__.__dict__["raw_ignition"] = raw_ignition
        super(Profile, __self__).__init__(
            'matchbox:index/profile:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            container_linux_config: Optional[pulumi.Input[str]] = None,
            generic_config: Optional[pulumi.Input[str]] = None,
            initrds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            kernel: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            raw_ignition: Optional[pulumi.Input[str]] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] args: List of kernel arguments
        :param pulumi.Input[str] container_linux_config: CoreOS Container Linux Config (CLC) (for backwards compatibility)
        :param pulumi.Input[str] generic_config: Generic configuration
        :param pulumi.Input[Sequence[pulumi.Input[str]]] initrds: List of URLs to init RAM filesystems
        :param pulumi.Input[str] kernel: URL of the kernel image to boot
        :param pulumi.Input[str] name: Unqiue name for the machine matcher
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProfileState.__new__(_ProfileState)

        __props__.__dict__["args"] = args
        __props__.__dict__["container_linux_config"] = container_linux_config
        __props__.__dict__["generic_config"] = generic_config
        __props__.__dict__["initrds"] = initrds
        __props__.__dict__["kernel"] = kernel
        __props__.__dict__["name"] = name
        __props__.__dict__["raw_ignition"] = raw_ignition
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def args(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of kernel arguments
        """
        return pulumi.get(self, "args")

    @property
    @pulumi.getter(name="containerLinuxConfig")
    def container_linux_config(self) -> pulumi.Output[Optional[str]]:
        """
        CoreOS Container Linux Config (CLC) (for backwards compatibility)
        """
        return pulumi.get(self, "container_linux_config")

    @property
    @pulumi.getter(name="genericConfig")
    def generic_config(self) -> pulumi.Output[Optional[str]]:
        """
        Generic configuration
        """
        return pulumi.get(self, "generic_config")

    @property
    @pulumi.getter
    def initrds(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of URLs to init RAM filesystems
        """
        return pulumi.get(self, "initrds")

    @property
    @pulumi.getter
    def kernel(self) -> pulumi.Output[Optional[str]]:
        """
        URL of the kernel image to boot
        """
        return pulumi.get(self, "kernel")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unqiue name for the machine matcher
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rawIgnition")
    def raw_ignition(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "raw_ignition")

