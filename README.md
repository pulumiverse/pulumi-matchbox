# Pulumi Provider for Matchbox

`pulumi-matchbox` allows defining [Matchbox](https://github.com/poseidon/matchbox) Profiles and Groups in Pulumi. Matchbox matches machines, by label (e.g. MAC address), to Profiles with iPXE configs, Ignition configs, or generic free-form configs to provision clusters. Resources are created via the client certificate authenticated Matchbox API.

## Usage

[Setup](https://matchbox.psdn.io/network-setup/) a PXE network boot environment and [deploy](https://matchbox.psdn.io/deployment/) a Matchbox instance. Be sure to enable the gRPC API and follow the instructions to generate TLS credentials.

* [Configure the Matchbox provider](https://www.pulumi.com/registry/packages/matchbox/installation-configuration/) with the Matchbox API endpoint and client certificate.
* Define a Matchbox [Profile](https://www.pulumi.com/registry/packages/matchbox/api-docs/profile/) or [Group](https://www.pulumi.com/registry/packages/matchbox/api-docs/group/) resource in Pulumi.
* Run `pulumi up` to ensure plugin version requirements are met.

```
$ pulumi up
```

See [examples](./examples) for Pulumi configs which PXE boot, install CoreOS, and provision entire clusters.

## Requirements

* Pulumi v3 [installed](https://www.pulumi.com/docs/get-started/)
* Matchbox v0.8+ [installed](https://matchbox.psdn.io/deployment/)
* Matchbox credentials `client.crt`, `client.key`, `ca.crt`

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumiverse/matchbox
```

or `yarn`:

```bash
yarn add @pulumiverse/matchbox
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumiverse_matchbox
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumiverse/pulumi-matchbox/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumiverse.Matchbox
```

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/matchbox/api-docs/).
