---
title: Matchbox
meta_desc: Provides an overview of the Matchbox Provider for Pulumi.
layout: overview
---

The Matchbox provider for Pulumi can be used to provision the [Matchbox](https://matchbox.psdn.io) iPXE server.
The Matchbox provider must be configured with certificates to connect correctly to the server.

## Example

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
import * as matchbox from "@pulumiverse/matchbox";

const db = new matchbox.Group("example", {
    cloudProvider: "azure",
    keyspace: "default",
    regions: ["westus2"],
    name: "example-db"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumiverse_matchbox as matchbox

db = matchbox.Group("example",
    cloud_provider="azure",
    keyspace="default",
    regions=["westus2"],
    name="example-db"
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"fmt"
	matchbox "github.com/pulumiverse/pulumi-matchbox/sdk/go/matchbox"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		db, err := Matchbox.NewGroup(ctx, "example", &matchbox.GroupArgs{
            CloudProvider: pulumi.String("azure"),
            Keyspace: pulumi.String("default"),
            Regions: pulumi.StringArray{
                pulumi.String("westus2")
            },
            Name: pulumi.String("example-db"),
		})
		if err != nil {
			return fmt.Errorf("error creating instance server: %v", err)
		}

		ctx.Export("dbId", db.Id)

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumiverse.Matchbox;

class MatchboxSetup : Stack
{
    public MatchboxSetup()
    {
        var db = new Group("example", new GroupArgs{
            CloudProvider: "azure",
            Keyspace: "default",
            Regions: new[] {"westus2"},
            Name: "example-db"
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}
