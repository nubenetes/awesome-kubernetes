---
type: curation-hub
okf_version: "0.3"
name: "Cloud Asset Inventory"
dimension: "Architectural Foundations"
resource_count: 11
fresh_2025_2026_count: 6
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/cloud-asset-inventory.md"
description: "Curated, AI-ranked Cloud Asset Inventory resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Architectural Foundations)."
---
# Cloud Asset Inventory

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/cloud-asset-inventory/).

!!! info "Architectural Context"
    Detailed reference for Cloud Asset Inventory in the context of Architectural Foundations.

## High-Value Spotlight: Microsoft Azure Resource Inventory (ARI)

!!! tip "When to Use Microsoft ARI vs CloudQuery / Steampipe"
    - **[Azure Resource Inventory (`microsoft/ARI`)](https://github.com/microsoft/ARI)** (`MIT`, PowerShell `7.0+`, cross-platform) is the fastest read-only tool for generating **stakeholder-ready multi-tab Excel workbooks (`ImportExcel`)** and interactive **Draw.io network/organization/resource diagrams** from any Azure Tenant or Management Group with zero persistent infrastructure.
    - **Use ARI** for brownfield cloud discovery, M&amp;A tenant handovers, FinOps tag/cost audits (`-IncludeTags`, `-IncludeCosts`), Azure Security Center/Policy/Advisor reviews (`-SecurityCenter`), pre-migration Landing Zone assessments, and scheduled monthly snapshots via Azure Automation (`-Automation`).
    - **Use CloudQuery or Steampipe** when you need continuous, real-time **multi-cloud** (AWS, GCP, Azure, Kubernetes) SQL querying into PostgreSQL, Parquet, or Grafana dashboards.

### Example ARI Workflows

```powershell
# 1. Full Management Group inventory with Tags and Cost Management
Invoke-ARI -TenantID <Tenant-ID> -ManagementGroup <MG-ID> -IncludeTags -IncludeCosts

# 2. Security posture & Advisor audit on a target subscription
Invoke-ARI -TenantID <Tenant-ID> -SubscriptionID <Sub-ID> -SecurityCenter

# 3. Full Draw.io Network Topology, Organization, and Resources diagrams
Invoke-ARI -TenantID <Tenant-ID> -SubscriptionID <Sub-ID> -DiagramFullEnvironment

# 4. Unattended scheduled snapshots in Azure Automation -> Blob Storage
Invoke-ARI -TenantID <Tenant-ID> -AppId <App-ID> -Secret <Secret> -Automation -StorageAccount <SA> -StorageContainer <Container>
```


## Cloud Infrastructure and Orchestration

### Asset Management and Governance

#### Cloud Analytics

  - **(2026)** [cloudquery.io: Cloud Query: The open-source cloud asset inventory powered by SQL](https://www.cloudquery.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source high-performance security and asset discovery tool that parses cloud configuration APIs into standard SQL databases. Enables infrastructure teams to perform complex auditing, compliance mapping, and security reporting.
  - **(2026)** [steampipe](https://steampipe.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extensible open-source command-line framework that translates APIs and cloud inventories into virtual SQL tables. Enables DevOps engineers to construct real-time dashboards and audit configuration profiles on multi-cloud hosts.
  - **(2023)** [cloudquery.io: Building an Open-Source Cloud Asset Inventory with CloudQuery and Grafana](https://www.cloudquery.io/learning-center/cloud-asset-management) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step implementation guide detailing how to ingest cloud infrastructure state via CloudQuery and visualize data patterns within Grafana. Outlines pipeline construction, scheduling, and database optimization.
  - **(2022)** [Querying AWS at scale across APIs, Regions, and accounts](https://aws.amazon.com/blogs/opensource/querying-aws-at-scale-across-apis-regions-and-accounts) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enterprise guide mapping performance configurations designed to query massive multi-account, multi-region AWS environments. Analyzes API latency limitations, concurrency protocols, and security audits utilizing SQL query abstractions.
### Public Cloud Administration

#### AWS Fundamentals

  - **(2023)** [AWS Cloud Practitioner - Curso Completo 2023](https://www.youtube.com/watch?v=zQyrhjEAqLs) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive Spanish instructional syllabus targeting the AWS Certified Cloud Practitioner domain. Details key global infrastructure components, core services (EC2, S3, RDS, VPC), billing architectures, and foundational security frameworks.
#### Azure Architecture

  - **(2025)** [Subscription Vending Implementation Guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) <span class='md-tag md-tag--warning'>[BICEP CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--primary'>[DRP-RESILIENCE]</span> — Automated governance framework detailing Azure Subscription Vending models. Outlines how to programmatically create subscription structures incorporating secure routing, virtual network configurations, policies, and role-based access management.
  - **(2025)** [Transitioning an Existing Azure Environment to the Azure Landing Zone Reference Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/transition) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Architectural migration playbook addressing transitioning legacy cloud setups to formal Microsoft Azure Landing Zones. Covers organizational tier hierarchies, network architectures, and systemic governance patterns.
### Serverless Architecture

#### Case Studies

  - **(2021)** [ServerlessHorrors: A Web Compiling Nightmares in the Serverless World](https://revistacloud.com/serverlesshorrors-la-web-que-recoge-las-peores-pesadillas-del-mundo-serverless)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A catalog documenting real-world runtime failures, billing anomalies, database connection exhaustion, cold start latency bottlenecks, and unexpected vendor configurations within modern serverless cloud setups.
### Storage and Databases

#### Distributed Block Storage

  - **(2026)** [==Ceph: A Distributed Object, Block, and File Storage Platform==](https://github.com/ceph/ceph) <span class='md-tag md-tag--info'>⭐ 16707</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2d010a68" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 2 L 20 3 L 30 2 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-2d010a68)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[C++ CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An enterprise-grade, highly scalable distributed storage ecosystem providing object, block, and file system storage on a single unified cluster. Widely adopted as the primary storage layer backing cloud platforms and Kubernetes orchestration (Rook-Ceph).
## Cloud Platform Management

### Microsoft Azure

#### Inventory Auditing

##### Azure Resource Inventory

  - **(2026)** [==github.com/microsoft/ARI: Azure Resource Inventory 🌟🌟🌟==](https://github.com/microsoft/ARI) <span class='md-tag md-tag--info'>⭐ 1749</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a55b92ac" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 10 L 20 8 L 30 7 L 40 5 L 50 2" fill="none" stroke="url(#spark-grad-a55b92ac)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--info' title='Open-source license'>⚖️ MIT</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — High-value MIT-licensed PowerShell 7.0+ engine from Microsoft (1,749 stars) for read-only, zero-agent discovery across Azure Tenants, Management Groups, Subscriptions, and Resource Groups. Generates multi-tab interactive Excel workbooks (ImportExcel) with Azure Security Center, Policy, Advisor, Tags, VM quotas, and Cost Management data, plus interactive Draw.io architecture diagrams (Network Topology with peering/hover metadata, Organization, and Resources views). Ideal for brownfield onboarding, M&A tenant handovers, FinOps/security audits, and scheduled Azure Automation governance.
## Infrastructure As Code

### Architecture

#### Diagrams

  - **(2024)** [CloudCanvas - Diagramming for Cloud Infrastructure](https://cloudcanvas.co) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — CloudCanvas is an emerging interactive workspace tool tailored for designing cloud topologies and auto-generating infrastructure-as-code manifests. By linking architectural nodes directly to API-driven configurations, it helps bridge the gap between architectural diagramming and operational execution.

---
💡 **Explore Related:** [Introduction](./introduction.md) | [FAQ](./faq.md) | [Kubernetes](./kubernetes.md)

🔗 **See Also:** [AI Agents & MCP](./ai-agents-mcp.md) | [AI RAG & OKF](./ai-rag-okf.md)

