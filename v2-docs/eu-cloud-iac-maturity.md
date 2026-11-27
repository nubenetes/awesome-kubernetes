---
type: curation-hub
okf_version: "0.3"
name: "IaC Automation and Portability on European Sovereign Clouds"
dimension: "European Sovereign Cloud & Private DCs"
resource_count: 27
fresh_2025_2026_count: 27
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/eu-cloud-iac-maturity.md"
description: "Curated, AI-ranked IaC Automation & Maturity vs Hyperscalers resources for the 2026 Cloud Native architect: top-tier tools, guides and references (European."
---
# IaC Automation and Portability on European Sovereign Clouds

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/eu-cloud-iac-maturity/).

!!! info "Architectural Context"
    Detailed reference for IaC Automation and Portability on European Sovereign Clouds in the context of European Sovereign Cloud & Private DCs.

!!! abstract "Deep-Dive Topic Pages"
    [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Germany Sovereign Cloud & Private DCs](eu-cloud-germany.md) · [France Sovereign Cloud & Private DCs](eu-cloud-france.md) · [Spain Sovereign Cloud & Private DCs](eu-cloud-spain.md) · [Hypervisors, IaaS, K8s & AI](eu-cloud-workloads-stack.md) · [Terraform & OpenTofu](terraform.md) · [Crossplane](crossplane.md)

## Pre-Sales Analysis: IaC Automation and Coverage vs Hyperscalers (100% Baseline)

1. [Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)](#master-iac-coverage-scorecard-vs-awsazuregcp-100)
2. [The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox](#the-api-portability-hack-standardizing-on-openstack-vcd-and-proxmox)
3. [Sovereign OpenTofu State Architecture (Zero US Dependency)](#sovereign-opentofu-state-architecture-zero-us-dependency)
4. [The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)](#the-6-real-iac-gaps-vs-hyperscalers-and-how-to-mitigate-them)

### Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)

A critical pre-sales honesty check: **AWS, Azure, and GCP maintain ~98–100% IaC API coverage** across every service from day one. European Sovereign Clouds cover **45% to 85%** natively — which is more than enough for **90% of IaaS + Kubernetes + DBaaS workloads** *if you design around the gaps upfront*:

| Provider / Platform (Clickable) | [OpenTofu](https://opentofu.org) / Terraform Score | [Crossplane](https://www.crossplane.io) Support | [Cluster API (CAPI)](https://cluster-api.sigs.k8s.io) | Pulumi / [Ansible](https://docs.ansible.com) | Underlying Standard API Layer | Real Pre-Sales Coverage Assessment |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| [**Scaleway**](https://www.scaleway.com/en) | **85%** ([provider](https://github.com/scaleway/terraform-provider-scaleway)) | Official ([`crossplane-provider-scaleway`](https://github.com/scaleway/crossplane-provider-scaleway)) | Community / Kosmos | Official Pulumi + Ansible | Custom REST + S3 | **EU Leader for DevOps DX:** Covers IAM, Kapsule K8s, DBaaS, S3, Serverless, VPCs cleanly. |
| [**OVHcloud**](https://www.ovhcloud.com/en-ie) | **80%** ([provider](https://github.com/ovh/terraform-provider-ovh)) | Community / Upjet | Community / Bare Metal | Pulumi bridge + Ansible | [OpenStack](https://www.openstack.org) + OVH v6 API | Great coverage for Public Cloud, MKS K8s, vRack, DBs; legacy Bare Metal parts mix OVH v6 APIs. |
| [**IONOS Cloud**](https://cloud.ionos.com) | **80%** ([provider](https://github.com/ionos-cloud/terraform-provider-ionoscloud)) | [**Official Native Crossplane**](https://github.com/ionos-cloud/crossplane-provider-ionoscloud) | [**Built `CAPMOX` (Proxmox)**](https://github.com/ionos-cloud/cluster-api-provider-proxmox) | Pulumi + Official Ansible | IONOS CloudAPIv6 | Strong enterprise automation for VDCs, K8s, S3, DBaaS; Crossplane support is top-tier in EU. |
| [**STACKIT**](https://stackit.com/en) | **75%** ([provider](https://github.com/stackitcloud/terraform-provider-stackit)) | Via Upjet / `provider-terraform` | [Gardener](https://gardener.cloud) Shoot CRDs | Official Ansible / OpenTofu | OpenStack + STACKIT REST | Very clean OpenTofu for SKE (Gardener K8s), OpenStack VMs, Postgres/MariaDB, Observability. |
| [**Hetzner**](https://www.hetzner.com/cloud) | **75% IaaS** ([`hcloud`](https://github.com/hetznercloud/terraform-provider-hcloud)) | Community / Upjet | [**Best-in-Class (`CAPH` Syself)**](https://github.com/syself/cluster-api-provider-hetzner) | Pulumi + `hcloud` Ansible | Hetzner Cloud REST | **100% coverage of its narrow IaaS scope**; pair with [Talos](https://www.talos.dev)/[`kube-hetzner`](https://github.com/kube-hetzner/terraform-hcloud-kube-hetzner)/[CNPG](https://cloudnative-pg.io). |
| [**3DS OUTSCALE**](https://en.outscale.com) | **75%** ([provider](https://github.com/outscale/terraform-provider-outscale)) | Via Upjet | OKS / Cockpit APIs | Official Ansible + OpenTofu | AWS-like Cockpit REST | SecNumCloud 3.2 automation covering OKS K8s, Nets/VPCs, volumes, and security groups. |
| [**Exoscale**](https://www.exoscale.com) | **75%** ([provider](https://github.com/exoscale/terraform-provider-exoscale)) | Upjet / `provider-terraform` | Community | Pulumi + Ansible | [CloudStack](https://cloudstack.apache.org)-rooted REST + S3 | Clean, fast Terraform for Compute, SKS Kubernetes, DBaaS, Security Groups, SOS S3. |
| [**cloudscale.ch**](https://www.cloudscale.ch/en) | **75%** ([provider](https://github.com/cloudscale-ch/terraform-provider-cloudscale)) | Upjet / [APPUiO](https://www.appuio.ch) | OpenStack [`CAPO`](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) | OpenTofu + Ansible | Swiss OpenStack + REST | Pure Swiss-owned API covering VMs, volumes, private networks, &amp; S3 cleanly. |
| [**Leaseweb**](https://www.leaseweb.com) | **65%** ([provider](https://github.com/leaseweb/terraform-provider-leaseweb)) | Upjet / `provider-terraform` | Bare Metal / K8s PXE | OpenTofu + Ansible | Leaseweb REST + CloudStack | Automates NL/EU dedicated bare metal, private networking, &amp; bandwidth bundles cleanly. |
| [**Anexia**](https://anexia.com/en) | **70%** ([provider](https://github.com/anexia-it/terraform-provider-anxcloud)) | Native Crossplane + Upjet | Anexia Kubernetes Service | Official Terraform + Ansible | AnxCloud REST | Mature Austrian/DACH Terraform &amp; Crossplane coverage (`anexia-it/anxcloud`). |
| [**UpCloud**](https://upcloud.com/docs) | **75%** ([provider](https://github.com/UpCloudLtd/terraform-provider-upcloud)) | Upjet / `provider-terraform` | Community | Ansible + OpenTofu | UpCloud REST + S3 | Full lifecycle for Madrid (`es-mad1`)/EU VMs, MaxIOPS, Managed K8s, Managed DBs, SDN routers. |
| [**Open Telekom Cloud**](https://www.open-telekom-cloud.com/en) | **75%** ([provider](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud)) | Upjet / OpenStack CRDs | OpenStack [`CAPO`](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) | Official Ansible + OpenTofu | OpenStack + OTC APIs | Mature coverage for VPCs, CCE Kubernetes, RDS, KMS, EVSs; strong BSI C5 governance. |
| [**Civo (UK)**](https://www.civo.com) &amp; [**Brightbox**](https://www.brightbox.com) | **75%** ([`civo`](https://github.com/civo/terraform-provider-civo) · [`brightbox`](https://github.com/brightbox/terraform-provider-brightbox)) | Upjet / `provider-terraform` | K3s/[Talos](https://www.talos.dev) native | Pulumi + Ansible | Civo / Brightbox REST + S3 | Built for Terraform + Kubernetes-first UK Sovereign automation. |
| [**Nebius**](https://nebius.com) &amp; [**Gcore**](https://gcore.com) | **70–75%** ([`nebius`](https://github.com/nebius/terraform-provider-nebius) · [`gcore`](https://github.com/G-Core/terraform-provider-gcore)) | Upjet / `provider-terraform` | MK8s GPU pools | OpenTofu + Ansible | Nebius gRPC / Gcore REST | Declarative H100/H200/B200 GPU clusters, Shared Filesystems, MK8s, and S3. |
| [**Arsys**](https://www.arsys.es/cloud) · [**Gigas**](https://gigas.com/en) · [**Alhambra IT**](https://alhambrait.com/en) · [**Telefonica Tech**](https://telefonicatech.com/en) | **50–75%** *([`ionoscloud`](https://github.com/ionos-cloud/terraform-provider-ionoscloud) / [`vmware/vcd`](https://github.com/vmware/terraform-provider-vcd))* | Via IONOS Crossplane / Upjet | [`CAPVCD`](https://github.com/vmware/cluster-api-provider-cloud-director) / [`CAPO`](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) | Ansible + `vmware/vcd` | **IONOS CloudAPI** + **VMware vCD** / OpenStack | Use Enterprise API/vCD tiers (not legacy SMB panels); MPLS/BGP edge cross-connects remain ticketed. |
| **Private DC ([Proxmox](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) / [OpenStack](https://www.openstack.org) / [CloudStack](https://cloudstack.apache.org))** | **75–90%** ([`bpg/proxmox`](https://github.com/bpg/terraform-provider-proxmox) · [`openstack`](https://github.com/terraform-provider-openstack/terraform-provider-openstack)) | Upjet / OpenStack CRDs | [**`CAPMOX`**](https://github.com/ionos-cloud/cluster-api-provider-proxmox) · [**`CAPO`**](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) · [**`CAPC`**](https://github.com/kubernetes-sigs/cluster-api-provider-cloudstack) | [Ansible](https://docs.ansible.com) + [Packer](https://developer.hashicorp.com/packer) | **Proxmox VE / OpenStack / CloudStack API** | **Best long-term portability:** Customer owns 100% of APIs from physical VLAN to K8s CAPI. |

### The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox

!!! success "How Senior Architects Beat Proprietary Cloud Lock-In (80–90% Module Reuse)"
    Never write custom glue against 5 different niche portals. Anchor your [**OpenTofu**](https://opentofu.org) modules and [**Cluster API (CAPI)**](https://cluster-api.sigs.k8s.io) fleets on one of Europe's **three universal infrastructure API standards**:

    1. **OpenStack Standard ([`terraform-provider-openstack`](https://github.com/terraform-provider-openstack/terraform-provider-openstack) + [`CAPO`](https://github.com/kubernetes-sigs/cluster-api-provider-openstack)):** Write ONE network/security-group/VM/Cinder module and deploy identically across [**Stackscale**](https://www.stackscale.com), [**Cleura**](https://cleura.com), [**Elastx**](https://elastx.se/en), [**Cyso Cloud**](https://cyso.com), [**Leafcloud**](https://leafcloud.com), [**Safespring**](https://www.safespring.com), [**OVHcloud**](https://www.ovhcloud.com/en-ie), [**STACKIT**](https://stackit.com/en), [**Open Telekom Cloud**](https://www.open-telekom-cloud.com/en), and [**Infomaniak**](https://www.infomaniak.com/en/hosting/public-cloud).
    2. **VMware Cloud Director Standard ([`vmware/vcd`](https://github.com/vmware/terraform-provider-vcd) + [`CAPVCD`](https://github.com/vmware/cluster-api-provider-cloud-director)):** Standardize on `vmware/vcd` OrgVDC + NSX-T Edge Gateway resources across [**Arsys**](https://www.arsys.es/cloud), [**Gigas**](https://gigas.com/en), [**Alhambra IT**](https://alhambrait.com/en), [**Telefonica Tech**](https://telefonicatech.com/en), [**Acens**](https://www.acens.com), [**PlusServer**](https://www.plusserver.com/en), and [**Aruba Cloud**](https://www.arubacloud.com).
    3. **Proxmox VE API Standard ([`bpg/proxmox`](https://github.com/bpg/terraform-provider-proxmox) + IONOS [`CAPMOX`](https://github.com/ionos-cloud/cluster-api-provider-proxmox)):** Standardize private bare-metal colocation in [**Digital Realty**](https://www.digitalrealty.com/data-centers/emea/madrid), [**Equinix**](https://www.equinix.com/data-centers/europe-colocation/germany-colocation/frankfurt-data-centers), [**Nabiax**](https://nabiax.com), [**DATA4**](https://www.data4group.com/en), or [**Hetzner**](https://www.hetzner.com/cloud)/[**OVHcloud**](https://www.ovhcloud.com/en-ie) Metal on [**Proxmox VE**](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) + Ceph at **zero per-core hypervisor tax**.

### Sovereign OpenTofu State Architecture (Zero US Dependency)

Avoid storing European sovereign [**OpenTofu**](https://opentofu.org) state in AWS S3 or HashiCorp Cloud (`HCP`). Store remote state and locking inside an **EU-owned S3 Object Lock backend** (OpenTofu &gt;= 1.10 native S3 lockfile `use_lockfile = true`, zero DynamoDB needed):

```hcl
terraform {
  required_version = ">= 1.10.0"

  backend "s3" {
    bucket                      = "acme-es-sovereign-tfstate-mad"
    key                         = "prod/platform-core/terraform.tfstate"
    region                      = "eu-south-mad" # or rbx / fr-par / de-fra
    use_lockfile                = true           # Native S3 conditional lock (zero DynamoDB needed)
    skip_credentials_validation = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true
    endpoints = {
      s3 = "https://s3.fr-par.scw.cloud"         # Or OVH / IONOS / Arsys / STACKIT S3
    }
  }
}
```

### The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)

| IaC Gap Category | What Breaks Coming From AWS/Azure/GCP | Practical Mitigation Pattern (Clickable Open-Source Stack) |
| :--- | :--- | :--- |
| **1. Workload IAM &amp; OIDC Federation** | Fewer fine-grained resource-policy IAM JSON engines (like AWS IAM Policies / Azure RBAC) for micro-services. | Standardize app &amp; CI auth inside Kubernetes via [**Keycloak**](https://www.keycloak.org) OIDC, [**External Secrets Operator**](https://external-secrets.io) + [**OpenBao**](https://openbao.org), and GitHub Actions OIDC. |
| **2. Ticket-Driven BGP, MPLS &amp; VLANs** | In MSPs ([Gigas](https://gigas.com/en), [Alhambra](https://alhambrait.com/en), [Telefonica](https://telefonicatech.com/en)), telco MPLS cross-connects or L2 trunk changes often require a NOC ticket. | Treat physical/BGP edge as an **immutable Level-0 landing zone** provisioned once; manage dynamic app routing inside SDN or [**Cilium**](https://cilium.io) BGP. |
| **3. Managed DB / Kafka Day-2 Parity** | Some local providers lack Terraform resources for point-in-time recovery triggers, read-replica promotion, or extension flags. | Run [**CloudNativePG**](https://cloudnative-pg.io) + [**Strimzi Kafka**](https://strimzi.io) directly inside your Managed/[Talos](https://www.talos.dev) Kubernetes cluster — **100% GitOps-controlled across every provider**. |
| **4. Missing Native Crossplane Providers** | Upbound maintains AWS/Azure/GCP Crossplane providers; smaller EU clouds lack first-party Go providers. | Use [**Crossplane**](https://www.crossplane.io) wrapping official [OpenTofu](https://opentofu.org) providers, OR delegate cleanly to **OpenTofu (Landing Zone) + [Argo CD](https://argo-cd.readthedocs.io) + [CAPI](https://cluster-api.sigs.k8s.io)**. |
| **5. Golden Image Pipelines** | Fewer cloud-native AMIs/Marketplace images pre-hardened to CIS/[ENS Alto](https://ens.ccn.cni.es/en) on smaller MSPs. | Run [**Packer**](https://developer.hashicorp.com/packer) + [**Ansible**](https://docs.ansible.com) CIS/ENS Lockdown (or [**Talos Linux**](https://www.talos.dev) Image Factory) exporting immutable QCOW2/OVA/Raw images. |
| **6. Granular FinOps / Showback Tagging APIs** | Billing APIs rarely match AWS Cost &amp; Usage Reports (CUR) granularity at sub-resource tag level. | Install [**OpenCost**](https://www.opencost.io) + Prometheus inside every Kubernetes cluster and scrape provider billing APIs into Grafana. |


## Crossplane And Cluster API CAPI Multi-cloud Control Planes

  - **(2026)** [Cluster API Provider Hetzner (CAPH by Syself)](https://github.com/syself/cluster-api-provider-hetzner) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — CNCF Cluster API provider managing full self-healing Kubernetes lifecycle across Hetzner Cloud VMs and Dedicated bare-metal Robot servers.
  - **(2026)** [Cluster API Provider OpenStack (CAPO)](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Kubernetes SIGs CAPI provider delivering standardized multi-cluster lifecycle across European OpenStack sovereign clouds.
  - **(2026)** [Cluster API Provider Proxmox (CAPMOX by IONOS)](https://github.com/ionos-cloud/cluster-api-provider-proxmox) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Enterprise Cluster API provider built by IONOS Cloud for declarative multi-cluster Kubernetes orchestration directly on Proxmox VE clusters.
  - **(2026)** [Cluster API Provider VMware Cloud Director (CAPVCD)](https://github.com/vmware/cluster-api-provider-cloud-director) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Declarative Cluster API lifecycle driver for Spanish and European sovereign MSPs running VMware Cloud Director.
  - **(2026)** [IONOS Cloud Official Crossplane Provider](https://github.com/ionos-cloud/crossplane-provider-ionoscloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Native Kubernetes control plane allowing GitOps teams to reconcile IONOS Virtual Data Centers and Managed K8s continuously via Argo CD and Crossplane XRDs.
  - **(2026)** [Scaleway Official Crossplane Provider](https://github.com/scaleway/crossplane-provider-scaleway) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Upjet-based Crossplane provider exposing Scaleway compute, Kubernetes, and database primitives as Kubernetes CRDs.
## Official Terraform And Opentofu Providers For European Clouds

  - **(2026)** [3DS OUTSCALE Official Terraform Provider](https://github.com/outscale/terraform-provider-outscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official IaC provider for SecNumCloud-qualified 3DS OUTSCALE infrastructure covering OKS Kubernetes, Nets/VPCs, security groups, and volumes.
  - **(2026)** [Anexia Engine (ANXCloud) Official Terraform Provider](https://github.com/anexia-it/terraform-provider-anxcloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Austrian/DACH IaC provider automating Anexia VMs, Managed Kubernetes clusters, VLANs, DNS, and Load Balancers.
  - **(2026)** [Brightbox Official Terraform Provider](https://github.com/brightbox/terraform-provider-brightbox) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official British IaaS provider automating UK cloud servers, cloud IPs, load balancers, firewall policies, and Orbit storage.
  - **(2026)** [Civo Official Terraform Provider](https://github.com/civo/terraform-provider-civo) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Lightweight IaC provider for Civo K3s/Talos Managed Kubernetes clusters, firewalls, networks, and UK Sovereign workloads.
  - **(2026)** [Clever Cloud Official Terraform Provider](https://github.com/CleverCloud/terraform-provider-clevercloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official French PaaS Terraform provider managing zero-ops runtimes, PostgreSQL/Redis/Materia databases, and Keycloak add-ons.
  - **(2026)** [cloudscale.ch Official Terraform Provider](https://github.com/cloudscale-ch/terraform-provider-cloudscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Swiss OpenStack/REST IaC provider automating Zurich and Lupfig servers, block volumes, private networks, load balancers, and S3 object users.
  - **(2026)** [Exoscale Official Terraform Provider](https://github.com/exoscale/terraform-provider-exoscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official provider for Swiss/EU Exoscale Compute, SKS Managed Kubernetes, DBAAS, SOS Object Storage, and IAM API keys.
  - **(2026)** [Gcore Official Terraform Provider](https://github.com/G-Core/terraform-provider-gcore) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Official Luxembourg-HQ cloud and Edge AI provider managing bare metal, VMs, Managed Kubernetes, CDN, and European GPU instances.
  - **(2026)** [Hetzner Cloud Official Terraform Provider](https://github.com/hetznercloud/terraform-provider-hcloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Fast, ultra-reliable OpenTofu/Terraform provider for Hetzner Cloud servers, private networks, firewalls, volumes, load balancers, and autoscaling node pools.
  - **(2026)** [IONOS Cloud Official Terraform Provider](https://github.com/ionos-cloud/terraform-provider-ionoscloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Comprehensive provider for IONOS Virtual Data Centers (VDC), Managed Kubernetes, MariaDB/Postgres DBaaS, Network Load Balancers, and S3 Object Storage.
  - **(2026)** [Leaseweb Official Terraform Provider](https://github.com/leaseweb/terraform-provider-leaseweb) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Dutch bare-metal and public-cloud Terraform provider managing dedicated server provisioning, private networking, and IPs.
  - **(2026)** [Nebius Official Terraform Provider](https://github.com/nebius/terraform-provider-nebius) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official OpenTofu/Terraform provider for Nebius AI GPU clusters, MK8s Kubernetes, Filesystem/S3 storage, and InfiniBand GPU fabrics.
  - **(2026)** [Open Telekom Cloud Terraform Provider](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Mature enterprise IaC provider covering Open Telekom Cloud VPCs, CCE Kubernetes, RDS, KMS, and German sovereign compliance policies.
  - **(2026)** [OVHcloud Official Terraform Provider](https://github.com/ovh/terraform-provider-ovh) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official OpenTofu/Terraform provider automating OVHcloud Public Cloud, Managed Kubernetes (MKS), vRack networking, KMS, IAM, Object Storage, and dedicated servers.
  - **(2026)** [Scaleway Official Terraform Provider](https://github.com/scaleway/terraform-provider-scaleway) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — High-coverage IaC provider automating Scaleway Instances, Kapsule/Kosmos Kubernetes, Managed PostgreSQL/Redis, IAM/RBAC, Serverless Containers/Functions, and AI Endpoints.
  - **(2026)** [STACKIT Official Terraform Provider](https://github.com/stackitcloud/terraform-provider-stackit) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Schwarz Digits IaC provider managing STACKIT Kubernetes Engine (SKE), OpenStack VMs, Load Balancers, Observability, and DBaaS resources.
  - **(2026)** [UpCloud Official Terraform Provider](https://github.com/UpCloudLtd/terraform-provider-upcloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official provider supporting UpCloud Managed Kubernetes, MaxIOPS storage, Managed Databases, SDN private networks, and Madrid (`es-mad1`) deployments.
## Portable Hypervisor And Private Cloud IaC Providers

  - **(2026)** [Kube-Hetzner: Production Talos/K3s Terraform Module](https://github.com/kube-hetzner/terraform-hcloud-kube-hetzner) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Battle-tested OpenTofu/Terraform module deploying HA auto-upgrading Kubernetes clusters with MicroOS/k3s on Hetzner Cloud at a fraction of hyperscaler EKS/AKS cost.
  - **(2026)** [OpenStack Standard Terraform Provider](https://github.com/terraform-provider-openstack/terraform-provider-openstack) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Universal open-source IaC provider enabling write-once infrastructure modules across European OpenStack sovereign clouds (Cleura, Elastx, Stackscale, City Cloud, OVH/STACKIT OpenStack layers).
  - **(2026)** [Proxmox VE Terraform Provider (bpg/proxmox)](https://github.com/bpg/terraform-provider-proxmox) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> — Actively maintained declarative provider enabling hyperscaler-grade VM, LXC, SDN, cloud-init, and Ceph/ZFS automation inside private Proxmox data centers.
  - **(2026)** [VMware Cloud Director (VCD) Terraform Provider](https://github.com/vmware/terraform-provider-vcd) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Standardized IaC provider widely compatible with Spanish and European VCSP clouds (Arsys, Gigas, Alhambra IT, Telefonica Tech VDC, Acens) running vCD NSX-T Edge Gateways and OrgVDCs.

---
💡 **Explore Related:** [EU Sovereign Cloud Overview & TCO](./eu-sovereign-cloud.md) | [Spain Sovereign Cloud & Private DCs](./eu-cloud-spain.md) | [Germany Sovereign Cloud & Private DCs](./eu-cloud-germany.md)

🔗 **See Also:** [European Neoclouds & Country AI Factories](./neoclouds-europe.md) | [Demos](./demos.md)

