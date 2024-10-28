// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package matchbox

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-matchbox/sdk/go/matchbox/internal"
)

// ## # Profile Resource
//
// A Profile defines network boot and declarative provisioning configurations.
//
// ```go
// package main
//
// import (
//
//	"fmt"
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			cfg := config.New(ctx, "")
//			// Fedora CoreOS release stream (e.g. testing, stable)
//			osStream := "stable"
//			if param := cfg.Get("osStream"); param != "" {
//				osStream = param
//			}
//			// Fedora CoreOS version to PXE and install (e.g. 32.20200715.3.0)
//			osVersion := cfg.Require("osVersion")
//			_ := fmt.Sprintf("https://builds.coreos.fedoraproject.org/prod/streams/%v/builds/%v/x86_64/fedora-coreos-%v-live-kernel-x86_64", osStream, osVersion, osVersion)
//			_ := fmt.Sprintf("https://builds.coreos.fedoraproject.org/prod/streams/%v/builds/%v/x86_64/fedora-coreos-%v-live-initramfs.x86_64.img", osStream, osVersion, osVersion)
//			return nil
//		})
//	}
//
// ```
type Profile struct {
	pulumi.CustomResourceState

	// List of kernel arguments
	Args pulumi.StringArrayOutput `pulumi:"args"`
	// CoreOS Container Linux Config (CLC) (for backwards compatibility)
	ContainerLinuxConfig pulumi.StringPtrOutput `pulumi:"containerLinuxConfig"`
	// Generic configuration
	GenericConfig pulumi.StringPtrOutput `pulumi:"genericConfig"`
	// List of URLs to init RAM filesystems
	Initrds pulumi.StringArrayOutput `pulumi:"initrds"`
	// URL of the kernel image to boot
	Kernel pulumi.StringPtrOutput `pulumi:"kernel"`
	// Unqiue name for the machine matcher
	Name        pulumi.StringOutput    `pulumi:"name"`
	RawIgnition pulumi.StringPtrOutput `pulumi:"rawIgnition"`
}

// NewProfile registers a new resource with the given unique name, arguments, and options.
func NewProfile(ctx *pulumi.Context,
	name string, args *ProfileArgs, opts ...pulumi.ResourceOption) (*Profile, error) {
	if args == nil {
		args = &ProfileArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Profile
	err := ctx.RegisterResource("matchbox:index/profile:Profile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProfile gets an existing Profile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProfileState, opts ...pulumi.ResourceOption) (*Profile, error) {
	var resource Profile
	err := ctx.ReadResource("matchbox:index/profile:Profile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Profile resources.
type profileState struct {
	// List of kernel arguments
	Args []string `pulumi:"args"`
	// CoreOS Container Linux Config (CLC) (for backwards compatibility)
	ContainerLinuxConfig *string `pulumi:"containerLinuxConfig"`
	// Generic configuration
	GenericConfig *string `pulumi:"genericConfig"`
	// List of URLs to init RAM filesystems
	Initrds []string `pulumi:"initrds"`
	// URL of the kernel image to boot
	Kernel *string `pulumi:"kernel"`
	// Unqiue name for the machine matcher
	Name        *string `pulumi:"name"`
	RawIgnition *string `pulumi:"rawIgnition"`
}

type ProfileState struct {
	// List of kernel arguments
	Args pulumi.StringArrayInput
	// CoreOS Container Linux Config (CLC) (for backwards compatibility)
	ContainerLinuxConfig pulumi.StringPtrInput
	// Generic configuration
	GenericConfig pulumi.StringPtrInput
	// List of URLs to init RAM filesystems
	Initrds pulumi.StringArrayInput
	// URL of the kernel image to boot
	Kernel pulumi.StringPtrInput
	// Unqiue name for the machine matcher
	Name        pulumi.StringPtrInput
	RawIgnition pulumi.StringPtrInput
}

func (ProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*profileState)(nil)).Elem()
}

type profileArgs struct {
	// List of kernel arguments
	Args []string `pulumi:"args"`
	// CoreOS Container Linux Config (CLC) (for backwards compatibility)
	ContainerLinuxConfig *string `pulumi:"containerLinuxConfig"`
	// Generic configuration
	GenericConfig *string `pulumi:"genericConfig"`
	// List of URLs to init RAM filesystems
	Initrds []string `pulumi:"initrds"`
	// URL of the kernel image to boot
	Kernel *string `pulumi:"kernel"`
	// Unqiue name for the machine matcher
	Name        *string `pulumi:"name"`
	RawIgnition *string `pulumi:"rawIgnition"`
}

// The set of arguments for constructing a Profile resource.
type ProfileArgs struct {
	// List of kernel arguments
	Args pulumi.StringArrayInput
	// CoreOS Container Linux Config (CLC) (for backwards compatibility)
	ContainerLinuxConfig pulumi.StringPtrInput
	// Generic configuration
	GenericConfig pulumi.StringPtrInput
	// List of URLs to init RAM filesystems
	Initrds pulumi.StringArrayInput
	// URL of the kernel image to boot
	Kernel pulumi.StringPtrInput
	// Unqiue name for the machine matcher
	Name        pulumi.StringPtrInput
	RawIgnition pulumi.StringPtrInput
}

func (ProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*profileArgs)(nil)).Elem()
}

type ProfileInput interface {
	pulumi.Input

	ToProfileOutput() ProfileOutput
	ToProfileOutputWithContext(ctx context.Context) ProfileOutput
}

func (*Profile) ElementType() reflect.Type {
	return reflect.TypeOf((**Profile)(nil)).Elem()
}

func (i *Profile) ToProfileOutput() ProfileOutput {
	return i.ToProfileOutputWithContext(context.Background())
}

func (i *Profile) ToProfileOutputWithContext(ctx context.Context) ProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileOutput)
}

// ProfileArrayInput is an input type that accepts ProfileArray and ProfileArrayOutput values.
// You can construct a concrete instance of `ProfileArrayInput` via:
//
//	ProfileArray{ ProfileArgs{...} }
type ProfileArrayInput interface {
	pulumi.Input

	ToProfileArrayOutput() ProfileArrayOutput
	ToProfileArrayOutputWithContext(context.Context) ProfileArrayOutput
}

type ProfileArray []ProfileInput

func (ProfileArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Profile)(nil)).Elem()
}

func (i ProfileArray) ToProfileArrayOutput() ProfileArrayOutput {
	return i.ToProfileArrayOutputWithContext(context.Background())
}

func (i ProfileArray) ToProfileArrayOutputWithContext(ctx context.Context) ProfileArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileArrayOutput)
}

// ProfileMapInput is an input type that accepts ProfileMap and ProfileMapOutput values.
// You can construct a concrete instance of `ProfileMapInput` via:
//
//	ProfileMap{ "key": ProfileArgs{...} }
type ProfileMapInput interface {
	pulumi.Input

	ToProfileMapOutput() ProfileMapOutput
	ToProfileMapOutputWithContext(context.Context) ProfileMapOutput
}

type ProfileMap map[string]ProfileInput

func (ProfileMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Profile)(nil)).Elem()
}

func (i ProfileMap) ToProfileMapOutput() ProfileMapOutput {
	return i.ToProfileMapOutputWithContext(context.Background())
}

func (i ProfileMap) ToProfileMapOutputWithContext(ctx context.Context) ProfileMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMapOutput)
}

type ProfileOutput struct{ *pulumi.OutputState }

func (ProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Profile)(nil)).Elem()
}

func (o ProfileOutput) ToProfileOutput() ProfileOutput {
	return o
}

func (o ProfileOutput) ToProfileOutputWithContext(ctx context.Context) ProfileOutput {
	return o
}

// List of kernel arguments
func (o ProfileOutput) Args() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringArrayOutput { return v.Args }).(pulumi.StringArrayOutput)
}

// CoreOS Container Linux Config (CLC) (for backwards compatibility)
func (o ProfileOutput) ContainerLinuxConfig() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringPtrOutput { return v.ContainerLinuxConfig }).(pulumi.StringPtrOutput)
}

// Generic configuration
func (o ProfileOutput) GenericConfig() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringPtrOutput { return v.GenericConfig }).(pulumi.StringPtrOutput)
}

// List of URLs to init RAM filesystems
func (o ProfileOutput) Initrds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringArrayOutput { return v.Initrds }).(pulumi.StringArrayOutput)
}

// URL of the kernel image to boot
func (o ProfileOutput) Kernel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringPtrOutput { return v.Kernel }).(pulumi.StringPtrOutput)
}

// Unqiue name for the machine matcher
func (o ProfileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ProfileOutput) RawIgnition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringPtrOutput { return v.RawIgnition }).(pulumi.StringPtrOutput)
}

type ProfileArrayOutput struct{ *pulumi.OutputState }

func (ProfileArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Profile)(nil)).Elem()
}

func (o ProfileArrayOutput) ToProfileArrayOutput() ProfileArrayOutput {
	return o
}

func (o ProfileArrayOutput) ToProfileArrayOutputWithContext(ctx context.Context) ProfileArrayOutput {
	return o
}

func (o ProfileArrayOutput) Index(i pulumi.IntInput) ProfileOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Profile {
		return vs[0].([]*Profile)[vs[1].(int)]
	}).(ProfileOutput)
}

type ProfileMapOutput struct{ *pulumi.OutputState }

func (ProfileMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Profile)(nil)).Elem()
}

func (o ProfileMapOutput) ToProfileMapOutput() ProfileMapOutput {
	return o
}

func (o ProfileMapOutput) ToProfileMapOutputWithContext(ctx context.Context) ProfileMapOutput {
	return o
}

func (o ProfileMapOutput) MapIndex(k pulumi.StringInput) ProfileOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Profile {
		return vs[0].(map[string]*Profile)[vs[1].(string)]
	}).(ProfileOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileInput)(nil)).Elem(), &Profile{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileArrayInput)(nil)).Elem(), ProfileArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileMapInput)(nil)).Elem(), ProfileMap{})
	pulumi.RegisterOutputType(ProfileOutput{})
	pulumi.RegisterOutputType(ProfileArrayOutput{})
	pulumi.RegisterOutputType(ProfileMapOutput{})
}
