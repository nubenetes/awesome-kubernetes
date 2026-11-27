---
type: curation-hub
okf_version: "0.3"
name: "Nordics Green Cloud and AI Factories"
dimension: "European Sovereign Cloud & Private DCs"
resource_count: 13
fresh_2025_2026_count: 13
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/eu-cloud-nordics.md"
description: "Curated, AI-ranked Nordics Green Cloud & AI Factories resources for the 2026 Cloud Native architect: top-tier tools, guides and references (European Sovereign."
---
# Nordics Green Cloud and AI Factories

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/eu-cloud-nordics/).

!!! info "Architectural Context"
    Detailed reference for Nordics Green Cloud and AI Factories in the context of European Sovereign Cloud & Private DCs.

!!! abstract "Deep-Dive Topic Pages"
    [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Germany Sovereign Cloud & Private DCs](eu-cloud-germany.md) · [Netherlands & Benelux Cloud & DCs](eu-cloud-benelux.md) · [United Kingdom Sovereign Cloud & DCs](eu-cloud-uk.md) · [IaC Automation & Maturity](eu-cloud-iac-maturity.md) · [Hypervisors, IaaS, K8s & AI](eu-cloud-workloads-stack.md) · [RPO, RTO, SLAs & DRP](eu-cloud-resilience-sla.md)

## Pre-Sales Field Guide: Nordics Green Cloud and AI Factories

1. [Why the Nordics Lead Europe in Green Compute and AI PUE](#why-the-nordics-lead-europe-in-green-compute-and-ai-pue)
2. [Comprehensive Nordic Cloud, 3-AZ OpenStack and AI Factory Matrix](#comprehensive-nordic-cloud-3-az-openstack-and-ai-factory-matrix)
3. [US Hyperscaler Nordic Regions vs Nordic 3-AZ Sovereign Clouds](#us-hyperscaler-nordic-regions-vs-nordic-3-az-sovereign-clouds)
4. [Nordic Enterprise and Green AI Pre-Sales Playbooks](#nordic-enterprise-and-green-ai-pre-sales-playbooks)

### Why the Nordics Lead Europe in Green Compute and AI PUE

Sweden and Finland (*EU Member States*) together with Norway and Iceland (*EEA GDPR Perimeter*) combine Europe's cleanest energy grid with pioneering open-source **3-Availability-Zone OpenStack** engineering:

- **100% Renewable Hydro/Geothermal Power &amp; Sub-1.20 PUE:** Industrial Nordic power prices run **30–55% cheaper** than Central Europe (Frankfurt/Amsterdam), while ambient Arctic/fjord free-cooling drops data center **PUE to 1.08–1.20** across [**Green Mountain**](https://greenmountain.no), [**atNorth**](https://www.atnorth.com), [**Verne**](https://www.verne.co), and [**Bulk Infrastructure**](https://bulkinfrastructure.com) — cutting AI GPU training TCO by **35–50%**.
- **Genuine 3-AZ European OpenStack ([Elastx](https://elastx.se/en) &amp; [Cleura](https://cleura.com)):** Unlike single-DC VPS vendors, Swedish pioneers [**Elastx**](https://elastx.se/en) (Stockholm 3-AZ) and [**Cleura**](https://cleura.com) engineered physically separated three-zone [**OpenStack**](https://www.openstack.org) &amp; Kubernetes clusters capable of true **3-way quorum** (etcd, [CloudNativePG](https://cloudnative-pg.io), Kafka) without AWS.
- **Public Sector Schrems II Rigor ([Digg](https://www.digg.se/en) / `eSam` Sweden):** Swedish and Norwegian public agencies enforce `eSam` and [**Digg**](https://www.digg.se/en) guidelines, systematically favoring [**Safespring**](https://www.safespring.com), [**Cleura**](https://cleura.com), [**Elastx**](https://elastx.se/en), [**Bahnhof**](https://bahnhof.se), and [**GleSYS**](https://glesys.com) over US-owned hyperscalers for citizen/health systems.
- **Cross-European Bridge ([UpCloud](https://upcloud.com/docs) Madrid + [Nebius](https://nebius.com) Mantsala + [LUMI](https://lumi-supercomputer.eu)):** Nordic infrastructure powers workloads across the entire continent — from **UpCloud's `es-mad1` Madrid region** (paired with Helsinki) to **Nebius's Finnish H200/B200 clusters** and [**LUMI EuroHPC**](https://lumi-supercomputer.eu).

### Comprehensive Nordic Cloud, 3-AZ OpenStack and AI Factory Matrix

| Provider / Operator (Clickable) | HQ and Nordic / EU Footprint | Sovereignty and Certs | Core Platforms and AI Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [**Elastx**](https://elastx.se/en) | **Stockholm (SE)**; **3 physically separated Stockholm AZs** | **100% Swedish Owned**, 100% hydro energy, ISO 27001/27017/27018, DORA-aligned | Enterprise **3-AZ [OpenStack](https://www.openstack.org)**, **Elastx Kubernetes (OKD/upstream)**, Managed PG/Kafka/RabbitMQ, S3 | **~75–80%** ([`openstack` Terraform](https://github.com/terraform-provider-openstack/terraform-provider-openstack) + [`CAPO`](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) + Managed DB automation) | True **3-AZ synchronous Stockholm quorum**; transparent EUR/SEK pricing | **Nordic fintech, healthcare, e-commerce** needing genuine 3-AZ resilience off AWS `eu-north-1` |
| [**Cleura**](https://cleura.com) | **Karlskrona (SE)**; **3-AZ Sweden**, Karlskrona, Frankfurt, Munich | **100% EU Owned**, **[Sovereign Cloud Stack (SCS)](https://scs.community)** leader, ISO 27001, DORA/NIS2 | Compliant OpenStack Public &amp; Dedicated Cloud + [**SAP Gardener**](https://gardener.cloud) **Managed Kubernetes** | **~75–80%** ([`openstack` Terraform](https://github.com/terraform-provider-openstack/terraform-provider-openstack) + Gardener Shoot API + SCS conformance) | Multi-region **Sweden + Germany** OpenStack portability; strong EU exit guarantees | Regulated European enterprises demanding **SCS-compliant OpenStack + Gardener Kubernetes** across Nordics &amp; DACH |
| [**UpCloud**](https://upcloud.com/docs) | **Helsinki (FI)**; Helsinki, **Madrid (`es-mad1`)**, Frankfurt, Amsterdam, Warsaw, London | **L4 Finnish Owned**, ISO 27001, GDPR strict, **MaxIOPS (~100k IOPS)** | High-IOPS Cloud Servers, **Managed Kubernetes (UKS)**, Managed Databases, SDN Private Networks, Object Storage | **~75%** ([`UpCloudLtd/upcloud`](https://github.com/UpCloudLtd/terraform-provider-upcloud) Official Terraform + [Packer](https://developer.hashicorp.com/packer) + [Ansible](https://docs.ansible.com)) | Sub-millisecond NVMe local quorum; cross-EU SDN replication including Madrid | Database-heavy European SaaS wanting **Madrid (`es-mad1`) + Helsinki/Frankfurt** under one Finnish API |
| [**GleSYS**](https://glesys.com) &amp; [**Bahnhof**](https://bahnhof.se) | **Falkenberg / Stockholm (SE)**, Oulu (FI); nuclear-bunker Stockholm DCs (`Bahnhof Pionen`) | **100% Swedish Independent**, ISO 27001/14001, 100% renewable power, district heat reuse | OpenStack/VMware Cloud Infrastructure, Bare Metal, Sovereign Kubernetes, High-Security Bunker Colocation | **~65–75%** (OpenStack/REST Terraform + [Ansible](https://docs.ansible.com) + private cloud APIs) | Owned dual-country SE–FI infrastructure + generous regional bandwidth | Swedish/Nordic regulated platforms needing **ultra-resilient physical security (`Bahnhof`)** or custom hybrid cloud (`GleSYS`) |
| [**Safespring**](https://www.safespring.com) | **Stockholm / Oslo**; 100% Swedish &amp; Norwegian academic/public DCs | **[Digg](https://www.digg.se/en) / `eSam` Schrems II Public Compliant**, zero non-Nordic ownership, 100% hydro | **Pure [OpenStack](https://www.openstack.org) IaaS + High-Throughput S3**, tailored for Sunet/academic &amp; public clouds | **~75%** (Pure [`openstack` Terraform](https://github.com/terraform-provider-openstack/terraform-provider-openstack) + [Ansible](https://docs.ansible.com) + standard Swift/S3 APIs) | Multi-site SE–NO research/public federation; strict zero commercial data mining | **Nordic universities, municipalities, hospitals, research institutes** bound by eSam/Schrems II |
| [**Green Mountain**](https://greenmountain.no) · [**atNorth**](https://www.atnorth.com) · [**Verne**](https://www.verne.co) · [**Bulk**](https://bulkinfrastructure.com) · [**evroc**](https://evroc.com) · [**LUMI**](https://lumi-supercomputer.eu) | **Norway, Iceland, Finland, Sweden, Denmark** (Stavanger, Keflavik, Kajaani LUMI, NO1) | **100% Hydro / Geothermal**, PUE **1.08–1.18**, ISO 27001/50001, heat export | Ultra-dense **Liquid-Cooled NVIDIA AI Colo** (50–150+ kW/rack), [**LUMI EuroHPC**](https://lumi-supercomputer.eu), [**evroc**](https://evroc.com) sovereign EU cloud | **~75–90%** ([`bpg/proxmox`](https://github.com/bpg/terraform-provider-proxmox), Slurm, [OpenShift AI](https://www.redhat.com/en/products/ai/openshift-ai), KubeRay on GPU clusters) | Gigawatt renewable grid resilience + [**Netnod**](https://www.netnod.se) peering + transatlantic dark fiber | **Large-scale LLM training, HPC batch AI, ESG-mandated enterprise AI factories** |

### US Hyperscaler Nordic Regions vs Nordic 3-AZ Sovereign Clouds

*Evaluating `AWS eu-north-1 (Stockholm)` / `Azure Sweden Central (Gavle)` / `GCP europe-north1 (Hamina Finland)` vs Nordic sovereign champions:*

| Dimension | US Hyperscalers (`AWS Stockholm` / `Azure Sweden` / `GCP Finland`) | Native Nordic Platforms ([Elastx](https://elastx.se/en) / [Cleura](https://cleura.com) / [UpCloud](https://upcloud.com/docs) / [Safespring](https://www.safespring.com) / [atNorth](https://www.atnorth.com)) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Public Sector / `eSam` Eligibility** | Disqualified for many sensitive Swedish/Norwegian citizen &amp; healthcare systems due to US CLOUD Act | **100% cleared** under Swedish `eSam` / [Digg](https://www.digg.se/en), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), and open [SCS](https://scs.community) rules | Decisive winner in public tenders and academic/research clouds. |
| **3-AZ OpenStack Parity** | Proprietary AWS AZ constructs + high inter-AZ data transfer fees (~EUR 0.02/GB each way) | **[Elastx](https://elastx.se/en)** &amp; **[Cleura](https://cleura.com)** run true **3-AZ physical Stockholm DCs** on standard OpenStack + [Gardener](https://gardener.cloud) | Delivers HA multi-AZ resilience **without AWS lock-in or inter-AZ surprise invoices**. |
| **Large-Scale Liquid-Cooled AI Economics** | Hyperscaler GPU regions mark up energy, cooling, and egress | **[atNorth](https://www.atnorth.com), [Green Mountain](https://greenmountain.no), [Verne](https://www.verne.co), [Nebius](https://nebius.com)** pass Nordic hydro cost floor directly to customers | **35–50% total TCO savings** on sustained LLM pre-training, distillation, &amp; synthetic data generation. |

### Nordic Enterprise and Green AI Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in the Nordics"
    1. **True 3-AZ AWS `eu-north-1` Exit (`Sweden FinTech / SaaS`):** Migrate EKS + RDS workloads onto [**Elastx**](https://elastx.se/en) Stockholm 3-AZ (`Managed K8s + PostgreSQL + OpenStack Terraform`), keeping 3-zone synchronous quorum with 100% Swedish jurisdiction.
    2. **European Cross-Border OpenStack (`Nordics + Germany`):** Standardize on [**Cleura**](https://cleura.com) (Sweden 3-AZ + Frankfurt/Munich), exploiting identical [**OpenStack**](https://www.openstack.org) + [**SAP Gardener**](https://gardener.cloud) APIs for DORA-compliant sovereign portability.
    3. **Spanish-to-Nordic Database + Latency Pairing (`Madrid + Helsinki`):** Run low-latency API &amp; MaxIOPS PostgreSQL nodes in [**UpCloud `es-mad1` (Madrid)**](https://upcloud.com/docs) with encrypted warm replication to **Helsinki/Frankfurt** using [`UpCloudLtd/upcloud`](https://github.com/UpCloudLtd/terraform-provider-upcloud).
    4. **AI Model Training Factory (`&gt;1 MW or Multi-Node H200/B200`):** Host latency-insensitive training/fine-tuning in [**Nebius**](https://nebius.com) Finland, [**atNorth**](https://www.atnorth.com), [**Green Mountain**](https://greenmountain.no), or [**Verne**](https://www.verne.co), streaming LoRA weights south to Paris/Madrid/Milan inference nodes.
    5. **Nordic Municipality / University Research Cloud (`eSam + Schrems II`):** Deploy [**Safespring**](https://www.safespring.com), [**Bahnhof**](https://bahnhof.se), or [**GleSYS**](https://glesys.com) on standardized OpenStack + [OpenTofu](https://opentofu.org) templates, meeting strict public procurement law cleanly.


## Hydro And Geothermal AI Data Centers And Eurohpc Supercomputing

  - **(2026)** [Bulk Infrastructure Nordic Green Data Centers](https://bulkinfrastructure.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Norwegian hyperscale data center and dark-fiber subsea carrier operating Norway's massive renewable-powered NO1 campus and ultra-low-latency transatlantic/Nordic connectivity.
  - **(2026)** [Green Mountain Hydro-Powered Data Centers (Norway and UK)](https://greenmountain.no) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — World-renowned Norwegian ultra-low-PUE colocation operator running fjord-cooled and 100% hydro-powered AI and sovereign enterprise data centers (Stavanger, Rjukan, Oslo).
  - **(2026)** [LUMI Pre-Exascale Supercomputer (CSC Kajaani Finland)](https://lumi-supercomputer.eu) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — One of Europe's cleanest pre-exascale EuroHPC supercomputers in Kajaani powered 100% by hydroelectricity with waste heat exported directly to the local municipal district heating grid.
  - **(2026)** [Verne Sustainable AI Data Centers (Iceland, Finland and UK)](https://www.verne.co) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> — High-density HPC and AI colocation specialist running 100% geothermal and hydro campuses across Keflavik (Iceland) and Finland tailored for multi-megawatt LLM training clusters.
## Nordic Interconnection And Sovereign Governance

  - **(2026)** [Digg: Swedish Agency for Digital Government](https://www.digg.se/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Swedish public-sector digital authority issuing sovereign cloud procurement, security, and Schrems II compliance guidance across Sweden.
  - **(2026)** [Netnod Neutral Nordic Internet Exchange](https://www.netnod.se) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Non-profit Swedish foundation operating critical Nordic IXP peering across Stockholm, Copenhagen, Gothenburg, Lulea, and Helsinki plus root DNS infrastructure.
## Nordic Sovereign Cloud And 3-AZ Openstack Providers

  - **(2026)** [Bahnhof Swedish Sovereign Cloud and Bunker Data Centers](https://bahnhof.se) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Iconic independent Swedish ISP and cloud operator running ultra-resilient underground Stockholm facilities (including Pionen) with strict Swedish privacy governance and renewable power.
  - **(2026)** [evroc: European Sovereign Hyperscale Cloud Initiative](https://evroc.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Stockholm-headquartered initiative engineering high-security, sustainable European hyperscale cloud and AI data center regions exclusively under EU jurisdiction.
  - **(2026)** [GleSYS Green European Cloud Infrastructure](https://glesys.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Swedish independent sovereign cloud, bare metal, and colocation provider operating owned eco-friendly facilities in Falkenberg, Stockholm, and Oulu with full API/Terraform automation and zero US CLOUD Act ties.
  - **(2026)** [Safespring Swedish and Norwegian Public-Sector Cloud](https://www.safespring.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Nordic OpenStack cloud built specifically for European academia, municipalities, and public sector (**eSam / Schrems II** compliant), featuring fast automated S3/Compute APIs on 100% renewable energy.
## Nordics Switzerland And Benelux Cloud And AI Providers

  - **(2026)** [Cleura: Compliant European OpenStack Cloud](https://cleura.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Swedish pioneer in open-source Sovereign Cloud Stack (OpenStack + Gardener Kubernetes) offering 3-AZ Swedish regions, Frankfurt/Karlskrona zones, DORA/NIS2 readiness, and strict European legal jurisdiction.
  - **(2026)** [Elastx: Swedish 3-AZ Sovereign OpenStack Cloud](https://elastx.se/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Swedish enterprise cloud running genuine 3-Availability-Zone OpenStack IaaS and Managed Kubernetes across three physically separated Stockholm data centers powered by 100% renewable hydro energy.
  - **(2026)** [UpCloud Sovereign European Cloud](https://upcloud.com/docs) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Finnish-owned cloud infrastructure provider operating high-IOPS MaxIOPS NVMe VMs, Managed Kubernetes, Managed Databases, and an active Madrid (`es-mad1`) region alongside Frankfurt, Amsterdam, Helsinki, and Warsaw.

---
💡 **Explore Related:** [EU Sovereign Cloud Overview & TCO](./eu-sovereign-cloud.md) | [Spain Sovereign Cloud & Private DCs](./eu-cloud-spain.md) | [Germany Sovereign Cloud & Private DCs](./eu-cloud-germany.md)

🔗 **See Also:** [Demos](./demos.md) | [DevOps](./devops.md)

