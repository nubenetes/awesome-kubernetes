# Cloud Asset Inventory

!!! info "Architectural Context"
    Detailed reference for Cloud Asset Inventory in the context of Architectural Foundations.

## Cloud Infrastructure

### AWS

#### Asset Management

  - [Querying AWS at scale across APIs, Regions, and accounts](https://aws.amazon.com/blogs/opensource/querying-aws-at-scale-across-apis-regions-and-accounts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS blog post analyzing strategies and open-source tools (like Steampipe) to query and audit AWS resources at massive multi-region, multi-account scales. It breaks down API rate-limiting workarounds and security posture assessment methodologies.
## Cloud Security

### Asset Management (1)

#### Infrastructure-as-Code

  - [cloudquery.io: Cloud Query: The open-source cloud asset inventory powered' by SQL](https://www.cloudquery.io)  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source cloud asset inventory tool that transforms infrastructure metadata into queryable SQL databases. By decoupling extraction (APIs) from storage (PostgreSQL, ClickHouse), it enables security and platform teams to perform advanced compliance auditing, cost optimization, and drift detection.
  - [steampipe 🌟](https://steampipe.io)  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A zero-dependency CLI tool that allows querying of APIs and cloud infrastructure (AWS, Azure, GitHub, etc.) dynamically using Postgres-compatible SQL. It simplifies cloud infrastructure compliance, security audits, and resource inspection by exposing multi-platform APIs as regular database tables.
#### Observability

  - **(2023)** [cloudquery.io: Building an Open-Source Cloud Asset Inventory with CloudQuery and Grafana](https://www.cloudquery.io/learning-center/cloud-asset-management)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on deployment guide detailing how to build a unified cloud-native asset inventory. It guides architects through configuring CloudQuery pipelines to extract multi-cloud metadata and visualize security posture and infrastructure footprint dynamically via Grafana dashboards.

---
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Cheatsheets](./cheatsheets.md) | [Git](./git.md)

