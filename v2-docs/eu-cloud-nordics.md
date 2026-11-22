---
type: curation-hub
okf_version: "0.3"
name: "Nordics Green Cloud and AI Factories"
dimension: "European Sovereign Cloud & Private DCs"
resource_count: 12
fresh_2025_2026_count: 12
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

Sweden, Finland, Norway, and Iceland combine Europe's cleanest energy grid with pioneering open-source **3-Availability-Zone OpenStack** engineering:

- **100% Renewable Hydro/Geothermal Power & Sub-1.20 PUE:** Industrial Nordic power prices run **30–55% cheaper** than Central Europe (Frankfurt/Amsterdam), while ambient Arctic/fjord free-cooling drops data center **PUE to 1.08–1.20** — cutting AI GPU training total TCO by **35–50%**.
- **Genuine 3-AZ European OpenStack (`Elastx` & `Cleura`):** Unlike single-DC European VPS vendors, Swedish pioneers **Elastx (Stockholm 3-AZ)** and **Cleura** engineered physically separated three-zone OpenStack & Kubernetes clusters capable of true **3-way quorum** (etcd, PostgreSQL Patroni/CNPG, Kafka) without AWS.
- **Public Sector Schrems II Rigor (`eSam` Sweden):** Swedish and Norwegian public agencies strictly enforce the **eSam framework**, systematically disqualifying US-owned hyperscalers for citizen/health systems and favoring **Safespring, Cleura, Elastx, and GleSYS**.
- **Cross-European Bridge (`UpCloud Madrid` + `Nebius Mantsala` + `LUMI`):** Nordic cloud infrastructure powers workloads across the entire continent — from **UpCloud's `es-mad1` Madrid region** (paired with Helsinki) to **Nebius's Finnish H200/B200 clusters** and **CSC's LUMI EuroHPC**.

### Comprehensive Nordic Cloud, 3-AZ OpenStack and AI Factory Matrix

| Provider / Operator | HQ and Nordic / EU Footprint | Sovereignty and Certs | Core Platforms and AI Stack | IaC Automation and Coverage | SLA, Multi-DC DRP and Egress | Optimal Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Elastx** | **Stockholm (SE)**; **3 physically separated Stockholm AZs** | **100% Swedish Owned**, 100% hydro energy, ISO 27001/27017/27018, DORA-aligned | Enterprise **3-AZ OpenStack**, **Elastx Kubernetes (OKD/upstream)**, Managed PG/Kafka/RabbitMQ, S3 | **~75–80%** (`openstack` Terraform + `CAPO` + Managed DB automation) | True **3-AZ synchronous Stockholm quorum**; transparent EUR/SEK pricing | **Nordic fintech, healthcare, e-commerce** needing genuine 3-AZ resilience off AWS `eu-north-1` |
| **Cleura** | **Karlskrona (SE)**; **3-AZ Sweden**, Karlskrona, Frankfurt, Munich | **100% EU Owned (Iver group)**, **Sovereign Cloud Stack (SCS)** leader, ISO 27001, DORA/NIS2 | Compliant OpenStack Public & Dedicated Cloud + **SAP Gardener Managed Kubernetes** | **~75–80%** (`openstack` Terraform + Gardener Shoot API + SCS conformance) | Multi-region **Sweden + Germany** OpenStack portability; strong EU exit guarantees | Regulated European enterprises demanding **SCS-compliant OpenStack + Gardener Kubernetes** across Nordics & DACH |
| **UpCloud** | **Helsinki (FI)**; Helsinki, **Madrid (`es-mad1`)**, Frankfurt, Amsterdam, Warsaw, London | **L4 Finnish Owned**, ISO 27001, GDPR strict, **MaxIOPS (~100k IOPS)** | High-IOPS Cloud Servers, **Managed Kubernetes (UKS)**, Managed Databases, SDN Private Networks, Object Storage | **~75%** (`UpCloudLtd/upcloud` Official Terraform + Packer + Ansible) | Sub-millisecond NVMe local quorum; cross-EU SDN replication including Madrid | Database-heavy European SaaS wanting **Madrid (`es-mad1`) + Helsinki/Frankfurt** under one Finnish API |
| **GleSYS** | **Falkenberg (SE)**; owned DCs in Falkenberg, Stockholm, Oulu (FI) | **100% Swedish Independent**, ISO 27001/14001, 100% renewable power, heat reuse | OpenStack/VMware Cloud Infrastructure, Bare Metal, Private Racks, Colocation | **~65–70%** (REST/Terraform automation + Ansible + private cloud APIs) | Owned dual-country SE–FI infrastructure + unlimited generous regional bandwidth | Swedish/Nordic SMB & mid-market platforms needing custom **VMware-to-Linux/K8s + colocation** |
| **Safespring** | **Stockholm / Oslo**; 100% Swedish & Norwegian academic/public DCs | **eSam / Schrems II Public Compliant**, zero non-Nordic ownership, 100% hydro | **Pure OpenStack IaaS + High-Throughput S3**, tailored for Sunet/academic & public clouds | **~75%** (Pure `openstack` Terraform + Ansible + standard Swift/S3 APIs) | Multi-site SE–NO research/public federation; strict zero commercial data mining | **Nordic universities, municipalities, hospitals, research institutes** bound by eSam/Schrems II |
| **Green Mountain / atNorth / Verne / Bulk + LUMI** | **Norway, Iceland, Finland, Sweden, Denmark** (Stavanger, Keflavik, Kajaani LUMI, NO1) | **100% Hydro / Geothermal**, PUE **1.08–1.18**, ISO 27001/50001, heat export | Ultra-dense **Liquid-Cooled NVIDIA AI Colo** (50–150+ kW/rack), **LUMI EuroHPC**, **evroc** sovereign EU cloud | **~75–90%** (`bpg/proxmox`, Slurm, OpenShift AI, KubeRay on dedicated GPU clusters) | Gigawatt renewable grid resilience + **Netnod** peering + transatlantic dark fiber | **Large-scale LLM training, HPC batch AI, ESG-mandated enterprise AI factories** |

### US Hyperscaler Nordic Regions vs Nordic 3-AZ Sovereign Clouds

*Evaluating `AWS eu-north-1 (Stockholm)` / `Azure Sweden Central (Gavle)` / `GCP europe-north1 (Hamina Finland)` vs Nordic sovereign champions:*

| Dimension | US Hyperscalers (`AWS Stockholm` / `Azure Sweden` / `GCP Finland`) | Native Nordic Platforms (`Elastx` / `Cleura` / `UpCloud` / `Safespring` / `atNorth`) | Pre-Sales Guidance |
| :--- | :--- | :--- | :--- |
| **Public Sector / `eSam` Eligibility** | Disqualified for many sensitive Swedish/Norwegian citizen & healthcare systems due to US CLOUD Act | **100% cleared** under Swedish `eSam`, **DORA**, and open **Sovereign Cloud Stack** rules | Decisive winner in public tenders and academic/research clouds. |
| **3-AZ OpenStack Parity** | Proprietary AWS AZ constructs + high inter-AZ data transfer fees (~EUR 0.02/GB each way) | **Elastx** & **Cleura** run true **3-AZ physical Stockholm DCs** on standard OpenStack + Gardener | Delivers HA multi-AZ resilience **without AWS lock-in or inter-AZ surprise invoices**. |
| **Large-Scale Liquid-Cooled AI Economics** | Hyperscaler GPU regions mark up energy, cooling, and egress | **atNorth, Green Mountain, Verne, Nebius Mantsala** pass Nordic hydro cost floor directly to customers | **35–50% total TCO savings** on sustained LLM pre-training, distillation, & synthetic data generation. |

### Nordic Enterprise and Green AI Pre-Sales Playbooks

!!! success "5 High-Conversion Deals in the Nordics"
    1. **True 3-AZ AWS `eu-north-1` Exit (`Sweden FinTech / SaaS`):** Migrate EKS + RDS workloads onto **Elastx Stockholm 3-AZ** (`Managed K8s + PostgreSQL + OpenStack Terraform`), keeping 3-zone synchronous quorum with 100% Swedish jurisdiction.
    2. **European Cross-Border OpenStack (`Nordics + Germany`):** Standardize on **Cleura** (Sweden 3-AZ + Frankfurt/Munich), exploiting identical **OpenStack + SAP Gardener** APIs for DORA-compliant sovereign portability.
    3. **Spanish-to-Nordic Database + Latency Pairing (`Madrid + Helsinki`):** Run low-latency API & MaxIOPS PostgreSQL nodes in **UpCloud `es-mad1` (Madrid)** with encrypted warm replication to **Helsinki/Frankfurt** using one Terraform provider.
    4. **AI Model Training Factory (`>1 MW or Multi-Node H200/B200`):** Host latency-insensitive training/fine-tuning in **Nebius Finland**, **atNorth Iceland/Finland**, **Green Mountain**, or **Verne**, streaming LoRA weights south to Paris/Madrid/Milan inference nodes.
    5. **Nordic Municipality / University Research Cloud (`eSam + Schrems II`):** Deploy **Safespring** or **GleSYS** on standardized OpenStack + OpenTofu templates, meeting strict public procurement law cleanly.


## Hydro And Geothermal AI Data Centers And Eurohpc Supercomputing

  - **(2026)** [atNorth Nordic High-Density AI Data Centers](https://www.atnorth.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Pan-Nordic high-density colocation and liquid-cooled GPU infrastructure operator spanning Iceland, Sweden, Finland, and Denmark with sub-1.15 PUE and geothermal/hydro electricity.
  - **(2026)** [Bulk Infrastructure Nordic Green Data Centers](https://bulkinfrastructure.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Norwegian hyperscale data center and dark-fiber subsea carrier operating Norway's massive renewable-powered NO1 campus and ultra-low-latency transatlantic/Nordic connectivity.
  - **(2026)** [Green Mountain Hydro-Powered Data Centers (Norway and UK)](https://greenmountain.no) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — World-renowned Norwegian ultra-low-PUE colocation operator running fjord-cooled and 100% hydro-powered AI and sovereign enterprise data centers (Stavanger, Rjukan, Oslo).
  - **(2026)** [LUMI Pre-Exascale Supercomputer (CSC Kajaani Finland)](https://lumi-supercomputer.eu) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — One of Europe's cleanest pre-exascale EuroHPC supercomputers in Kajaani powered 100% by hydroelectricity with waste heat exported directly to the local municipal district heating grid.
  - **(2026)** [Verne Sustainable AI Data Centers (Iceland, Finland and UK)](https://www.verne.co) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> — High-density HPC and AI colocation specialist running 100% geothermal and hydro campuses across Keflavik (Iceland) and Finland tailored for multi-megawatt LLM training clusters.
## Nordic Interconnection And Sovereign Governance

  - **(2026)** [Netnod Neutral Nordic Internet Exchange](https://www.netnod.se) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Non-profit Swedish foundation operating critical Nordic IXP peering across Stockholm, Copenhagen, Gothenburg, Lulea, and Helsinki plus root DNS infrastructure.
## Nordic Sovereign Cloud And 3-AZ Openstack Providers

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

