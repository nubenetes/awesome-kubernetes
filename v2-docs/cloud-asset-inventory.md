# Cloud Asset Inventory

!!! info "Architectural Context"
    Detailed reference for Cloud Asset Inventory in the context of Architectural Foundations.

## Cloud Infrastructure

### AWS

#### Asset Management

  - [Querying AWS at scale across APIs, Regions, and accounts](https://aws.amazon.com/blogs/opensource/querying-aws-at-scale-across-apis-regions-and-accounts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS blog post analyzing strategies and open-source tools (like Steampipe) to query and audit AWS resources at massive multi-region, multi-account scales. It breaks down API rate-limiting workarounds and security posture assessment methodologies.
### Azure

#### Enterprise Architecture

  - [Transitioning an Existing Azure Environment to the Azure Landing Zone Reference Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/transition) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Official Microsoft guidance outlining the migration roadmap of legacy brownfield Azure environments to the Azure Landing Zone (ALZ) conceptual architecture. It focuses on governance, subscription organization, network topology convergence, and security policy enforcement at scale.
#### Platform Engineering

  - [Subscription Vending Implementation Guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the architectural pattern of automated subscription vending on Azure.

*   Guides cloud platform teams to construct GitOps-driven workflows.
*   Automatically provisions fully governed, secure, and networked Azure subscriptions using Bicep or Terraform.
### Training

#### AWS Official

  - [AWS Cloud Practitioner - Curso Completo 2023](https://www.youtube.com/watch?v=zQyrhjEAqLs) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A complete video guide systematically mapping the official AWS Cloud Practitioner certification domains in Spanish. [SPANISH CONTENT]
## Cloud Security

### Asset Management (1)

#### Infrastructure-as-Code

  - [cloudquery.io: Cloud Query: The open-source cloud asset inventory powered' by SQL](https://www.cloudquery.io)  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source cloud asset inventory tool that transforms infrastructure metadata into queryable SQL databases. By decoupling extraction (APIs) from storage (PostgreSQL, ClickHouse), it enables security and platform teams to perform advanced compliance auditing, cost optimization, and drift detection.
  - [steampipe 🌟](https://steampipe.io)  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A zero-dependency CLI tool that allows querying of APIs and cloud infrastructure (AWS, Azure, GitHub, etc.) dynamically using Postgres-compatible SQL. It simplifies cloud infrastructure compliance, security audits, and resource inspection by exposing multi-platform APIs as regular database tables.
#### Observability

  - **(2023)** [cloudquery.io: Building an Open-Source Cloud Asset Inventory with CloudQuery and Grafana](https://www.cloudquery.io/learning-center/cloud-asset-management)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on deployment guide detailing how to build a unified cloud-native asset inventory. It guides architects through configuring CloudQuery pipelines to extract multi-cloud metadata and visualize security posture and infrastructure footprint dynamically via Grafana dashboards.
## Software Architecture

### Cloud Patterns

#### Serverless

  - [ServerlessHorrors: A Web Compiling Nightmares in the Serverless World](https://revistacloud.com/serverlesshorrors-la-web-que-recoge-las-peores-pesadillas-del-mundo-serverless) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Un compendio técnico sobre los errores más comunes y costosos en el diseño de arquitecturas serverless. Ofrece un análisis crítico de fallos reales de concurrencia, inicios en frío ("cold starts"), costos fuera de control e integración de servicios, sirviendo como guía de advertencia para diseñadores de sistemas distribuidos. [SPANISH CONTENT]

---
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Linux](./linux.md) | [Helm](./helm.md)

