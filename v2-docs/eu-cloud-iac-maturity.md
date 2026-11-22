---
type: curation-hub
okf_version: "0.3"
name: "IaC Automation and Portability on European Sovereign Clouds"
dimension: "European Sovereign Cloud & Private DCs"
resource_count: 22
fresh_2025_2026_count: 22
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
    [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Spain Sovereign Cloud & Private DCs](eu-cloud-spain.md) · [France & Germany Cloud Champions](eu-cloud-france-germany.md) · [Hypervisors, IaaS, K8s & AI](eu-cloud-workloads-stack.md) · [Terraform & OpenTofu](terraform.md) · [Crossplane](crossplane.md)

## Pre-Sales Analysis: IaC Automation and Coverage vs Hyperscalers (100% Baseline)

1. [Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)](#master-iac-coverage-scorecard-vs-awsazuregcp-100)
2. [The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox](#the-api-portability-hack-standardizing-on-openstack-vcd-and-proxmox)
3. [Sovereign OpenTofu State Architecture (Zero US Dependency)](#sovereign-opentofu-state-architecture-zero-us-dependency)
4. [The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)](#the-6-real-iac-gaps-vs-hyperscalers-and-how-to-mitigate-them)

### Master IaC Coverage Scorecard (vs AWS/Azure/GCP = 100%)

A critical pre-sales honesty check: **AWS, Azure, and GCP maintain ~98–100% IaC API coverage** across every service from day one. European Sovereign Clouds cover **45% to 85%** natively — which is more than enough for **90% of IaaS + Kubernetes + DBaaS workloads** *if you design around the gaps upfront*:

| Provider / Platform | Terraform / OpenTofu Score | Crossplane Support | Cluster API (CAPI) | Pulumi / Ansible | Underlying Standard API Layer | Real Pre-Sales Coverage Assessment |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Scaleway** | **85%** | Official (`crossplane-provider-scaleway`) | Community / Kosmos | Official Pulumi + Ansible | Custom REST + S3 | **EU Leader for DevOps DX:** Covers IAM, Kapsule K8s, DBaaS, S3, Serverless, VPCs cleanly. |
| **OVHcloud** | **80%** | Community / Upjet (`provider-terraform`) | Community / Bare Metal | Pulumi bridge + Ansible | OpenStack + OVH v6 API | Great coverage for Public Cloud, MKS K8s, vRack, DBs; legacy Bare Metal parts mix OVH v6 APIs. |
| **IONOS Cloud** | **80%** | **Official Native Crossplane** | **Built `CAPMOX` (Proxmox)** | Pulumi + Official Ansible | IONOS CloudAPIv6 | Strong enterprise automation for VDCs, K8s, S3, DBaaS; Crossplane support is top-tier in EU. |
| **STACKIT** | **75%** | Via Upjet / `provider-terraform` | Gardener Shoot CRDs | Official Ansible / OpenTofu | OpenStack + STACKIT REST | Very clean OpenTofu for SKE (Gardener K8s), OpenStack VMs, Postgres/MariaDB, Observability. |
| **Hetzner** | **75% IaaS / 40% Total** | Community / Upjet | **Best-in-Class (`CAPH` Syself)** | Pulumi + `hcloud` Ansible | Hetzner Cloud REST | **100% coverage of its narrow IaaS scope**, but zero managed K8s/DBaaS — you automate those with Talos/K3s/CNPG. |
| **Exoscale** | **75%** | Upjet / `provider-terraform` | Community | Pulumi + Ansible | CloudStack-rooted REST + S3 | Clean, fast Terraform for Compute, SKS Kubernetes, DBaaS, Security Groups, SOS S3. |
| **UpCloud** | **75%** | Upjet / `provider-terraform` | Community | Ansible + OpenTofu | UpCloud REST + S3 | Full lifecycle for Madrid (`es-mad1`)/EU VMs, MaxIOPS, Managed K8s, Managed DBs, SDN routers. |
| **Open Telekom Cloud** | **75%** | Upjet / OpenStack CRDs | OpenStack `CAPO` compatible | Official Ansible + OpenTofu | OpenStack + Huawei/OTC APIs | Mature coverage for VPCs, CCE Kubernetes, RDS, KMS, EVSs; slower feature velocity than Scaleway. |
| **Civo (UK)** | **75%** | Upjet / `provider-terraform` | K3s/Talos native | Pulumi + Ansible | Civo REST + S3 | Built specifically for Terraform + Kubernetes-first automation; tiny IaaS surface makes 75%+ easy. |
| **Nebius** | **70%** | Upjet / `provider-terraform` | MK8s GPU pools | OpenTofu + Ansible | Nebius API + gRPC | Rapidly maturing Terraform coverage for H100/H200 clusters, Shared Filesystems, MK8s, S3. |
| **Arsys (Spain)** | **55–75%** *(tier dependent)* | Via IONOS Crossplane (Public) / Upjet | Via `CAPVCD` (Enterprise Cloud) | `vcd` + IONOS Ansible | **IONOS CloudAPI** (Public) + **VMware vCD** (Enterprise) | Use **Enterprise/IONOS-backed API tiers**, NOT legacy SMB VPS panels; unlocks full Terraform/vCD automation. |
| **Gigas (Spain)** | **50–65%** | Via `provider-terraform` (`vcd`) | **`CAPVCD` / `CAPO`** | Ansible + `vmware/vcd` | **VMware Cloud Director / OpenStack** | VMs, vApps, NSX Edge firewall/NAT, disks are scriptable via `vmware/vcd`; telco MPLS/cross-connects remain ticketed. |
| **Alhambra IT (Spain)** | **45–65%** | Via `provider-terraform` | `CAPVCD` / Proxmox `CAPMOX` | **Ansible + OpenTofu** | **VMware vCD / Proxmox / K8s** | Compute & Kubernetes layers automate cleanly; contractual bespoke firewall/BGP changes involve MSP change tickets. |
| **Telefonica Tech VDC** | **50–65%** *(95% on Google Sov.)* | Via `provider-terraform` | `CAPVCD` / Anthos | Ansible + Terraform (`vcd` / `google`) | **VMware vCD / OpenStack / GCP** | Use `vmware/vcd` for VDC; if near-100% hyperscaler IaC is non-negotiable, Telefonica + Google Sovereign wins. |
| **Private DC (Proxmox / OpenStack)** | **75–90%** | Upjet / OpenStack CRDs | **`CAPMOX` / `CAPO` / `CAPC`** | **Ansible + `bpg/proxmox` / `openstack`** | **Proxmox VE / OpenStack / CloudStack API** | **Best long-term portability:** Customer owns 100% of APIs from physical switch/VLAN (Ansible/NetBox) to K8s CAPI. |

### The API Portability Hack: Standardizing on OpenStack, vCD and Proxmox

!!! success "How Senior Architects Beat Proprietary Cloud Lock-In (80–90% Module Reuse)"
    Never write custom glue against 5 different niche Spanish/European portals. Anchor your **OpenTofu modules** and **Cluster API (CAPI) fleets** on one of Europe's **three universal infrastructure API standards**:

    1. **OpenStack Standard (`terraform-provider-openstack` + `CAPO`):** Write ONE network/security-group/VM/Cinder module and deploy identically across **Stackscale (Madrid/Amsterdam), Cleura (Sweden/Germany), Elastx (Sweden), OVHcloud Public Cloud (PCI layer), STACKIT core, Open Telekom Cloud, and Infomaniak**.
    2. **VMware Cloud Director Standard (`vmware/vcd` + `CAPVCD`):** Standardize on `vmware/vcd` OrgVDC + NSX-T Edge Gateway resources to deploy consistently across **Arsys, Gigas, Alhambra IT, Telefonica Tech VDC, Acens, PlusServer, and Aruba VCSP**.
    3. **Proxmox VE API Standard (`bpg/proxmox` + IONOS `CAPMOX`):** Standardize private bare-metal colocation in **Digital Realty, Equinix, Nabiax, DATA4, or Hetzner/OVH Metal** on Proxmox VE 8/9 + Ceph, getting clean cloud-init VMs, SDN VXLANs, and declarative Kubernetes node lifecycle at **zero per-core hypervisor tax**.

### Sovereign OpenTofu State Architecture (Zero US Dependency)

Avoid storing European sovereign OpenTofu state in AWS S3 or HashiCorp Cloud (`HCP`). Store remote state and locking inside an **EU-owned S3 Object Lock backend** (OpenTofu >= 1.10 native S3 lockfile `use_lockfile = true`, or DynamoDB-free locking):

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
      s3 = "https://s3.fr-par.scw.cloud"         # Or OVH / IONOS / Arsys / MinIO Sovereign Madrid
    }
  }
}
```

### The 6 Real IaC Gaps vs Hyperscalers (and How to Mitigate Them)

| IaC Gap Category | What Breaks Coming From AWS/Azure/GCP | Practical Mitigation Pattern (2026 Pre-Sales Design) |
| :--- | :--- | :--- |
| **1. Workload IAM & OIDC Federation** | Fewer fine-grained resource-policy IAM JSON engines (like AWS IAM Policies / Azure RBAC) for micro-services. | Standardize app & CI auth inside Kubernetes via **Keycloak / Dex OIDC**, **External Secrets Operator + OpenBao/Vault**, and GitHub Actions OIDC -> Envoy/WireGuard. |
| **2. Ticket-Driven BGP, MPLS & VLANs** | In Spanish MSPs (Gigas, Alhambra, Telefonica VDC), telco MPLS cross-connects or L2 trunk changes often still require a human NOC ticket. | Treat physical/BGP edge as an **immutable Level-0 landing zone** provisioned once at onboarding; manage all dynamic app routing inside NSX/SDN or **Cilium BGP**. |
| **3. Managed DB / Kafka Day-2 Parity** | Some local providers lack Terraform resources for point-in-time recovery triggers, read-replica promotion, or extension flags. | Run **CloudNativePG** + **Strimzi Kafka** directly inside your Managed/Talos Kubernetes cluster on NVMe volumes — **100% GitOps-controlled across every provider**. |
| **4. Missing Native Crossplane Providers** | Upbound officially maintains AWS/Azure/GCP Crossplane providers; smaller EU clouds lack first-party Go providers. | Use **Crossplane `provider-opentofu` / Upjet** wrapping official OpenTofu providers, OR delegate infrastructure lifecycle cleanly to **OpenTofu (Landing Zone) + Argo CD + CAPI (Clusters)**. |
| **5. Golden Image Pipelines** | Fewer cloud-native AMIs/Marketplace images pre-hardened to CIS/ENS Alto on smaller MSPs. | Run **HashiCorp Packer + Ansible CIS/ENS Lockdown** (or **Talos Linux Image Factory**) exporting immutable QCOW2/OVA/Raw images uploaded via API. |
| **6. Granular FinOps / Showback Tagging APIs** | Billing APIs rarely match AWS Cost & Usage Reports (CUR) granularity at sub-resource tag level. | Install **OpenCost + Prometheus** inside every Kubernetes cluster and scrape provider billing CSV/APIs into a central Grafana FinOps dashboard. |


## Crossplane And Cluster API CAPI Multi-cloud Control Planes

  - **(2026)** [Cluster API Provider CloudStack (CAPC)](https://github.com/kubernetes-sigs/cluster-api-provider-cloudstack) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> — Official Kubernetes SIGs provider turning Apache CloudStack private DCs into declarative GitOps Kubernetes fleets.
  - **(2026)** [Cluster API Provider Hetzner (CAPH by Syself)](https://github.com/syself/cluster-api-provider-hetzner) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — CNCF Cluster API provider managing full self-healing Kubernetes lifecycle across Hetzner Cloud VMs and Dedicated bare-metal Robot servers.
  - **(2026)** [Cluster API Provider OpenStack (CAPO)](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Kubernetes SIGs CAPI provider delivering standardized multi-cluster lifecycle across European OpenStack sovereign clouds.
  - **(2026)** [Cluster API Provider Proxmox (CAPMOX by IONOS)](https://github.com/ionos-cloud/cluster-api-provider-proxmox) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Enterprise Cluster API provider built by IONOS Cloud for declarative multi-cluster Kubernetes orchestration directly on Proxmox VE clusters.
  - **(2026)** [Cluster API Provider VMware Cloud Director (CAPVCD)](https://github.com/vmware/cluster-api-provider-cloud-director) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Declarative Cluster API lifecycle driver for Spanish and European sovereign MSPs running VMware Cloud Director.
  - **(2026)** [IONOS Cloud Official Crossplane Provider](https://github.com/ionos-cloud/crossplane-provider-ionoscloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Native Kubernetes control plane allowing GitOps teams to reconcile IONOS Virtual Data Centers and Managed K8s continuously via Argo CD and Crossplane XRDs.
  - **(2026)** [Scaleway Official Crossplane Provider](https://github.com/scaleway/crossplane-provider-scaleway) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official Upjet-based Crossplane provider exposing Scaleway compute, Kubernetes, and database primitives as Kubernetes CRDs.
## Official Terraform And Opentofu Providers For European Clouds

  - **(2026)** [3DS OUTSCALE Official Terraform Provider](https://github.com/outscale/terraform-provider-outscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official IaC provider for SecNumCloud-qualified 3DS OUTSCALE infrastructure covering OKS Kubernetes, Nets/VPCs, security groups, and volumes.
  - **(2026)** [Civo Official Terraform Provider](https://github.com/civo/terraform-provider-civo) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Lightweight IaC provider for Civo K3s/Talos Managed Kubernetes clusters, firewalls, networks, and UK Sovereign workloads.
  - **(2026)** [Exoscale Official Terraform Provider](https://github.com/exoscale/terraform-provider-exoscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official provider for Swiss/EU Exoscale Compute, SKS Managed Kubernetes, DBAAS, SOS Object Storage, and IAM API keys.
  - **(2026)** [Hetzner Cloud Official Terraform Provider](https://github.com/hetznercloud/terraform-provider-hcloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Fast, ultra-reliable OpenTofu/Terraform provider for Hetzner Cloud servers, private networks, firewalls, volumes, load balancers, and autoscaling node pools.
  - **(2026)** [IONOS Cloud Official Terraform Provider](https://github.com/ionos-cloud/terraform-provider-ionoscloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Comprehensive provider for IONOS Virtual Data Centers (VDC), Managed Kubernetes, MariaDB/Postgres DBaaS, Network Load Balancers, and S3 Object Storage.
  - **(2026)** [Nebius Official Terraform Provider](https://github.com/nebius/terraform-provider-nebius) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official OpenTofu/Terraform provider for Nebius AI GPU clusters, MK8s Kubernetes, Filesystem/S3 storage, and InfiniBand GPU fabrics.
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
💡 **Explore Related:** [EU Sovereign Cloud Overview & TCO](./eu-sovereign-cloud.md) | [Spain Sovereign Cloud & Private DCs](./eu-cloud-spain.md) | [France & Germany Cloud Champions](./eu-cloud-france-germany.md)

🔗 **See Also:** [Demos](./demos.md) | [DevOps](./devops.md)

