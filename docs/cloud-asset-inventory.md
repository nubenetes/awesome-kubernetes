# Cloud Asset Inventory

1. [CloudQuery](#cloudquery)
2. [Steampipe](#steampipe)
3. [Azure Architecture](#azure-architecture)
4. [kubernetes-storage](#kubernetes-storage)

## CloudQuery

- https://github.com/cloudquery/cloudquery
- [cloudquery.io: Cloud Query: The open-source cloud asset inventory powered by SQL](https://www.cloudquery.io) CloudQuery enables you to assess, audit, and evaluate the configurations of your cloud assets.
- [cloudquery.io: Building an Open-Source Cloud Asset Inventory with CloudQuery and Grafana](https://www.cloudquery.io/learning-center/cloud-asset-management)

## Steampipe
  - [ServerlessHorrors: A Web Compiling Nightmares in the Serverless World](https://revistacloud.com/serverlesshorrors-la-web-que-recoge-las-peores-pesadillas-del-mundo-serverless) - *(Related to serverless topic)*

## Azure Architecture

- **(2026)** [==Microsoft Azure Resource Inventory (ARI)==](https://github.com/microsoft/ARI) 🌟 - High-value MIT-licensed PowerShell `7.0+` engine (`★1.7k+`) for read-only, low-impact discovery across Azure Tenants, Management Groups, Subscriptions, and Resource Groups, generating multi-tab Excel workbooks (`ImportExcel`) and interactive **Draw.io** diagrams (Network Topology with peering/hover metadata, Organization, and Resources views).
  - **Key Capabilities**: Supports Service Principal / Device Login auth, cross-platform execution (Windows, Linux, macOS, Azure Cloud Shell), Azure Automation (`-Automation`, `-StorageAccount`), Azure Security Center (`-SecurityCenter`), Azure Policy & Advisor (`-SkipPolicy`, `-SkipAdvisory`), Resource Tags (`-IncludeTags`, `-TagKey`/`-TagValue`), VM quota/vCPU/memory specs (`-SkipVMDetails`), Cost Management (`-IncludeCosts`), and lightweight Excel mode (`-Lite`).
  - **Why and When to Use It**: Ideal for rapid brownfield cloud discovery, M&A/tenant handovers, security/FinOps/compliance audits, and instant stakeholder-ready Excel + Draw.io architecture documentation without deploying persistent agents. Use **CloudQuery** or **Steampipe** instead when you need continuous real-time SQL querying across **multi-cloud** (AWS, GCP, Azure, Kubernetes) into PostgreSQL or Grafana.
  - **Example Use Cases**:
    - *Enterprise Management Group + FinOps Audit*: `Invoke-ARI -TenantID <Tenant-ID> -ManagementGroup <MG-ID> -IncludeTags -IncludeCosts`
    - *Security Posture and Compliance Snapshot*: `Invoke-ARI -TenantID <Tenant-ID> -SubscriptionID <Sub-ID> -SecurityCenter`
    - *Full Network Topology Diagramming (Draw.io)*: `Invoke-ARI -TenantID <Tenant-ID> -SubscriptionID <Sub-ID> -DiagramFullEnvironment`
    - *Unattended Scheduled Governance*: `Invoke-ARI -TenantID <Tenant-ID> -AppId <App-ID> -Secret <Secret> -Automation -StorageAccount <SA> -StorageContainer <Container>`

## kubernetes-storage
  - [Ceph: A Distributed Object, Block, and File Storage Platform](https://github.com/ceph/ceph) - *(Related to kubernetes-storage topic)*
  - [AWS Cloud Practitioner - Curso Completo 2023](https://www.youtube.com/watch?v=zQyrhjEAqLs) - *(Related to aws-training topic)*
  - [CloudCanvas - Diagramming for Cloud Infrastructure](https://cloudcanvas.co) - *(Related to cloud-arch-diagrams topic)*
  - [Transitioning an Existing Azure Environment to the Azure Landing Zone Reference Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/transition) - *(Related to azure topic)*
  - [Subscription Vending Implementation Guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) - *(Related to azure topic)*

- [steampipe](https://steampipe.io) Steampipe is an open source tool for querying cloud APIs in a universal way and reasoning about the data in SQL. 
- [==Querying AWS at scale across APIs, Regions, and accounts==](https://aws.amazon.com/blogs/opensource/querying-aws-at-scale-across-apis-regions-and-accounts)