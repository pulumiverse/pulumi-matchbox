// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # Group Resource
 *
 * A Group matches (one or more) machines and declares a machine should be boot with a named `profile`.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as matchbox from "@pulumiverse/matchbox";
 *
 * const node1 = new matchbox.Group("node1", {
 *     metadata: {
 *         custom_variable: "machine_specific_value_here",
 *     },
 *     profile: matchbox_profile.myprofile.name,
 *     selector: {
 *         mac: "52:54:00:a1:9c:ae",
 *     },
 * });
 * ```
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'matchbox:index/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * Map of group metadata (optional, seldom used)
     */
    public readonly metadata!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Unqiue name for the machine matcher
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Name of a Matchbox profile
     */
    public readonly profile!: pulumi.Output<string>;
    /**
     * Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
     */
    public readonly selector!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["metadata"] = state ? state.metadata : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["profile"] = state ? state.profile : undefined;
            resourceInputs["selector"] = state ? state.selector : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            if ((!args || args.profile === undefined) && !opts.urn) {
                throw new Error("Missing required property 'profile'");
            }
            resourceInputs["metadata"] = args ? args.metadata : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["profile"] = args ? args.profile : undefined;
            resourceInputs["selector"] = args ? args.selector : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * Map of group metadata (optional, seldom used)
     */
    metadata?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Unqiue name for the machine matcher
     */
    name?: pulumi.Input<string>;
    /**
     * Name of a Matchbox profile
     */
    profile?: pulumi.Input<string>;
    /**
     * Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
     */
    selector?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * Map of group metadata (optional, seldom used)
     */
    metadata?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Unqiue name for the machine matcher
     */
    name?: pulumi.Input<string>;
    /**
     * Name of a Matchbox profile
     */
    profile: pulumi.Input<string>;
    /**
     * Map of hardware machine selectors. See [reserved selectors](https://matchbox.psdn.io/matchbox/#reserved-selectors). An empty selector becomes a global default group that matches machines.
     */
    selector?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
