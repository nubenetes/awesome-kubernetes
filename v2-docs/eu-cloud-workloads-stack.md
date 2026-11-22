---
type: curation-hub
okf_version: "0.3"
name: "Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks in Europe"
dimension: "European Sovereign Cloud & Private DCs"
resource_count: 14
fresh_2025_2026_count: 14
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/eu-cloud-workloads-stack.md"
description: "Top Hypervisors, IaaS, K8s & Sovereign AI resources for 2026, AI-ranked: Apache CloudStack, Arsys Managed Kubernetes and more — curated Cloud Native tools."
---
# Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks in Europe

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/eu-cloud-workloads-stack/).

!!! info "Architectural Context"
    Detailed reference for Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks in Europe in the context of European Sovereign Cloud & Private DCs.

!!! abstract "Deep-Dive Topic Pages"
    [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Germany Sovereign Cloud & Private DCs](eu-cloud-germany.md) · [France Sovereign Cloud & Private DCs](eu-cloud-france.md) · [Netherlands & Benelux Cloud & DCs](eu-cloud-benelux.md) · [Nordics Green Cloud & AI Factories](eu-cloud-nordics.md) · [IaC Automation & Maturity](eu-cloud-iac-maturity.md) · [RPO, RTO, SLAs & DRP](eu-cloud-resilience-sla.md) · [Kubernetes On-Premise](kubernetes-on-premise.md) · [Enterprise AI Platforms](enterprise-ai-platforms.md)

## Pre-Sales Engineering Guide: Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks

1. [Post-Broadcom Hypervisor Modernization Matrix](#post-broadcom-hypervisor-modernization-matrix)
2. [Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)](#virtualized-iaas-vs-dedicated-bare-metal-when-metal-wins)
3. [European Managed Kubernetes vs Declarative DIY Stack](#european-managed-kubernetes-vs-declarative-diy-stack)
4. [Sovereign AI and NVIDIA GPU Factories in Europe (2026)](#sovereign-ai-and-nvidia-gpu-factories-in-europe-2026)

### Post-Broadcom Hypervisor Modernization Matrix

With Broadcom's **VMware Cloud Foundation (VCF)** per-core subscription shifts raising renewal TCO by 2x–4x across Europe, pre-sales architects must clearly position the 7 production hypervisor architectures available in EU Sovereign Clouds and Private Data Centers:

| Hypervisor / Stack | Licensing & Commercial Model | Storage & HA Capabilities | IaC and Kubernetes Integration | Enterprise Support & Maturity | When to Recommend (Pre-Sales Rule) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proxmox VE + Ceph + PBS** | **Open Source (AGPLv3)**; optional **EUR 110–1,050 / socket / yr** Enterprise support (Vienna HQ) | Native **Ceph HCI**, ZFS local/replication, live migration, SDN VXLAN/EVPN | **`bpg/proxmox`** Terraform + **IONOS `CAPMOX`** Cluster API + Packer | Huge European partner ecosystem (Spain/DE MSPs) | **#1 Default VMware exit** for SMB & mid-market private DCs / Hetzner / OVH Metal needing 70–85% license savings |
| **OpenStack (SCS / Sunbeam / Kolla)** | Open Source (Apache-2.0); Commercial SLAs via **STACKIT, Stackscale, Cleura, Elastx, Canonical** | **Ceph RBD**, NetApp Cinder, OVN multi-tenant SDN, L3/BGP routing | **Standard `openstack` Terraform** + **`CAPO` Cluster API** | Industrial-scale proven across Europe's largest public clouds | **Service providers, telcos, and >20-rack enterprises** building an internal multi-tenant AWS-like private cloud |
| **Red Hat OpenShift Virtualization 5 (KubeVirt)** | Enterprise Red Hat per-core/node subscription (**RHCOS 10 / RHEL 10.2**, **K8s 1.36**) | Ceph / ODF / Trident / Portworx CSI + live VM migration inside K8s pods | **100% GitOps YAML / K8s API / Crossplane / Argo CD** | Top-tier enterprise SLA; **MTV Migration Toolkit** from vSphere | **Mission-critical banking/telco/public sector** unifying VMs and containers on ONE Red Hat platform + RHOAI |
| **Apache CloudStack** | Open Source (Apache-2.0); Commercial support via ShapeBlue | Supports KVM, XCP-ng, NFS, Ceph, StorPool, SANs | **Official CloudStack Terraform + `CAPC` Cluster API** | Very lightweight control plane (~10% op complexity of OpenStack) | Regional MSPs and enterprises wanting AWS-style VPC/zone IaaS with minimal SRE headcount |
| **SUSE Harvester (KubeVirt + Longhorn)** | Open Source (Apache-2.0); Optional SUSE Rancher Prime support | Native **Longhorn** distributed NVMe block + VLAN trunking | Rancher Terraform + **CAPI / Fleet GitOps** | Rapidly adopted by edge/telco & Kubernetes-first teams | Edge campuses, factories, retail stores running unified **Rancher + K8s + light VMs** |
| **VMware Cloud Director (EU VCSP)** | **Broadcom VCSP Partner Program** pooled RAM/core OPEX model | vSAN / NetApp / Dell PowerStore; **Zerto / Veeam CDP** DRaaS | **`vmware/vcd` Terraform + `CAPVCD`** | Highest zero-refactoring stability (familiar vCenter/NSX) | **Time-boxed 12–36 month bridge:** customer has Oracle/ERP appliances that cannot be migrated before hardware EOL |
| **Nutanix AHV** | Per-core HCI subscription (usually 25–40% below aggressive VCF tiers) | Distributed AOS HCI + native asynchronous Metro HA | Official **Nutanix Terraform** + NKP | Turnkey 1-click upgrades; easiest vSphere GUI parallel | Risk-averse private DC teams wanting **VMware-like appliance simplicity** without managing Linux/Ceph internals |

### Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)

Do **not** blindly put every workload on virtualized cloud instances. Pitch **Dedicated Bare Metal** (on **OVHcloud Metal, Scaleway Elastic Metal, Hetzner Robot, Stackscale Bare Metal, or Arsys Dedicated**) whenever ANY of these 4 triggers applies:

1. **Core-Licensed Commercial Software (Oracle DB, Microsoft SQL Server Enterprise, SAP):** Physical bare-metal core pinning cuts software licensing exposure compared to vCPU sprawl on shared public clouds.
2. **Sustained High Storage IOPS / Low Tail Latency (<1 ms):** Dedicated dual-NVMe RAID or local Ceph eliminates noisy-neighbor hypervisor I/O jitter.
3. **Hyperconverged Private K8s / VM Fleet (>32 vCPUs / >128 GB RAM per node):** Running **Talos Linux** or **Proxmox VE** directly on **EUR 180–450/month bare-metal hosts** with 10–25 Gbps unmetered private networking delivers **2.5x–3.5x better compute density per EUR** than public IaaS VMs.
4. **Physical Hardware Compliance Isolation (PCI-DSS L1 / Banking / Defense):** Dedicated single-tenant chassis guarantees physical isolation and auditability without paying hyperscaler `Dedicated Host` 200% markups.

### European Managed Kubernetes vs Declarative DIY Stack

| Platform | Provider / Origin | Control Plane Cost | Multi-AZ / HA Maturity | Networking (CNI) & Load Balancers | GPU Worker Support | Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OVHcloud MKS** | OVHcloud (FR) | **Free** | **3-AZ** in Paris; Multi-node etcd | Cilium / Calico + OVH Octavia LB | L40S, A100, H100 | Default zero-control-plane-tax EU Managed K8s |
| **Scaleway Kapsule / Kosmos** | Scaleway (FR) | **Free** (Ded. paid tier) | **3-AZ** Paris + Multi-Cloud **Kosmos** | Cilium eBPF + Scaleway LB | **L4, L40S, H100, B200** | Best developer UX + hybrid **Kosmos** nodes (attach Hetzner/Arsys nodes into Scaleway!) |
| **STACKIT SKE** | STACKIT (DE — Gardener) | Transparent metered | **3-AZ** Germany | **Cilium eBPF** + OpenStack Octavia LB | NVIDIA AI SKUs | German enterprise stability; automated Gardener self-healing |
| **IONOS Managed K8s** | IONOS (DE) | **Free** control plane | Multi-DC EU (Frankfurt/Berlin/Spain link) | Calico + IONOS NLB | NVIDIA H200 / Enterprise VMs | Pairs cleanly with **Arsys Spain** & native Crossplane workflows |
| **SysEleven MetaKube** | SysEleven (DE — Kubermatic) | Managed tier | **3-AZ** Germany | Cilium/Calico + LB | Dedicated / OpenStack GPU | SLA-backed production German DevOps clusters |
| **Exoscale SKS** | Exoscale (CH/AT) | Free Starter / SLA Pro | Multi-zone CH/EU | Calico + NLB | NVIDIA RTX / A100 / H100 | Swiss/Austrian regulated K8s simplicity |
| **Civo K8s / Talos** | Civo (UK) | Very low fixed node cost | Multi-region UK / EU | Cilium / Flannel + LB | H100 / B200 GPU instances | Sub-2-minute spin-up for CI/CD, UK Sovereign K8s & AI |
| **Arsys Managed K8s** | Arsys (ES) | Node-based EUR pricing | **Spain ENS Alto** | Managed CNI + LB | Enterprise IaaS GPUs | Spanish public-sector & ENS Alto container workloads |
| **DIY: Talos Linux + Cilium + CAPI** | Any Bare Metal (Hetzner / OVH / Stackscale / Proxmox) | **$0** | 3-DC or 3-AZ customer-controlled | **Cilium eBPF + BGP Gateway API** | **Full NVIDIA DRA / GPU Operator** | Maximum TCO victory (60–75% cheaper than EKS/AKS) for teams with 2+ Kubernetes SREs |

### Sovereign AI and NVIDIA GPU Factories in Europe (2026)

| EU AI Platform / Host | GPU Catalog & Interconnect | Jurisdictional Protection | Software & Serving Stack (`2026`) | Typical Pre-Sales Sweet Spot |
| :--- | :--- | :--- | :--- | :--- |
| **Nebius AI Cloud** | **H100, H200, Blackwell B200** clusters w/ **3.2 Tbps InfiniBand NDR** | **Amsterdam HQ (L4 EU)** + Finland/France clean energy | Managed Kubernetes (MK8s), Slurm, S3, `vLLM`, Ray, Terraform | Multi-node foundation model training, LoRA fine-tuning, high-throughput batch AI in Europe |
| **Scaleway AI & Serverless** | **L4, L40S, H100 SXM, B200/B300** + Serverless AI Endpoints | **French/EU L4** + GDPR / EU AI Act alignment | Kapsule K8s, Managed Inference (`vLLM`), **Mistral/Llama EU APIs** | Fastest elastic GPU spin-up + pay-per-token EU serverless inference with zero US transit |
| **OVHcloud AI** | L40S, H100, AI Deploy, AI Notebooks | **French/EU L4** + SecNumCloud roadmap | MKS K8s, Triton/vLLM containers, **zero egress** for training datasets | Dataset-heavy vision/RAG pipelines moving TBs of European files without egress fees |
| **Seeweb (Italy)** | Dedicated **H100 / L40S / A100** pods & K8s nodes | **Italy/EU L4** (GDPR + EU AI Act ready) | K8s GPU nodes, bare-metal inference, custom RAG stacks | Southern European / Italian enterprises requiring bespoke dedicated GPU servers in EU |
| **Merlin-Edged & Spain Colocation** | Liquid-cooled **100 kW+ racks** ready for **NVIDIA GB200 NVL72** | **100% Spanish Private Facility (`ENS Alto` capable)** | **Red Hat OpenShift AI (RHOAI) + `llm-d` + Mistral/EuroLLM/OKF** | Sovereign Spanish banking, defense, telco AI factories requiring physical air-gap / direct rack custody |
| **MareNostrum 5 (BSC Barcelona)** | Thousands of **NVIDIA Hopper H100** GPUs | **European / Spanish EuroHPC Public AI Factory** | Slurm, PyTorch, **Salamandra / ALIA** multilingual European models | R&D consortia, European SMEs (AI Factory grants), Iberian/European sovereign foundation model training |


## France Sovereign Cloud and Private Dcs

### French Sovereign Cloud Providers Secnumcloud And AI Factories

  - **(2026)** [Mistral AI Sovereign Frontier Models](https://mistral.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Paris-based European AI champion delivering open-weight (Mistral/Mixtral/Codestral) and enterprise models optimized for self-hosted Kubernetes vLLM and European sovereign cloud AI endpoints.
  - **(2026)** [OVHcloud Managed Kubernetes Service (MKS)](https://www.ovhcloud.com/en-ie/public-cloud/kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — CNCF-certified Managed Kubernetes with free multi-master control plane, Cinder/Octavia OpenStack integration, NVIDIA H100/L40S worker pools, and multi-AZ support in Paris.
## Germany Sovereign Cloud and Private Dcs

### German Sovereign Cloud Providers BSI C5 And High-efficiency Bare Metal

  - **(2026)** [SysEleven MetaKube Managed Kubernetes](https://www.syseleven.de/en/metakube) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Berlin-based OpenStack and CNCF Kubernetes provider offering Kubermatic/MetaKube managed clusters across multi-AZ German data centers for German financial and SaaS workloads.
## Italy Sovereign Cloud and Private Dcs

### Italy Sovereign Cloud And ACN Qualified Providers

  - **(2026)** [Seeweb Cloud and GPU AI Infrastructure](https://www.seeweb.it/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Independent Italian cloud and data center pioneer specializing in NVIDIA H100/L40S/A100 GPU clusters, Kubernetes, sovereign AI inference, and zero hyperscaler egress traps.
## Managed And Declarative Kubernetes On European Infrastructure

  - **(2026)** [SAP Gardener Multi-Cloud Kubernetes Fleet Engine](https://gardener.cloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-originated open-source Kubernetes-as-a-Service control plane powering STACKIT SKE, SysEleven MetaKube, and Cleura multi-AZ managed clusters.
  - **(2026)** [Talos Linux by Sidero Labs](https://www.talos.dev) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Immutable, API-driven Kubernetes OS eliminating SSH and mutable Linux packages — the gold standard for running secure, declarative Kubernetes on Hetzner bare metal, OVH/Scaleway metal, Proxmox, or colocation.
## Netherlands and Benelux Cloud and Dcs

### Nordics Switzerland And Benelux Cloud And AI Providers

  - **(2026)** [Nebius Sovereign AI Cloud (Amsterdam HQ)](https://nebius.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-headquartered AI hyperscaler operating massive InfiniBand-interconnected NVIDIA H100, H200, and Blackwell B200 superclusters in Finland and France with Kubernetes (MK8s), Slurm, and Sovereign S3 storage.
## Spain Sovereign Cloud and Private Dcs

### Spanish National Compliance And Supercomputing

  - **(2026)** [Barcelona Supercomputing Center: MareNostrum 5](https://www.bsc.es/marenostrum/marenostrum-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — European EuroHPC pre-exascale supercomputer hosted in Barcelona powered by thousands of NVIDIA Hopper H100 GPUs, anchoring Spain's AI Factory and sovereign foundation model ecosystem (Salamandra / ALIA).
### Spanish Sovereign Cloud And Managed Iaas Providers

  - **(2026)** [Arsys Managed Kubernetes](https://www.arsys.es/cloud/kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Managed Kubernetes service hosted in Spain under ENS Alto and European GDPR jurisdiction with native load balancers, block storage, and IONOS Cloud API / Terraform integration.
## Traditional Hypervisors And Post-vmware Modernization

  - **(2026)** [Apache CloudStack](https://cloudstack.apache.org) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> — Lightweight, turn-key multi-hypervisor (KVM, XCP-ng, VMware) IaaS orchestrator widely adopted by European MSPs seeking simpler day-2 operations than full OpenStack deployments.
  - **(2026)** [Nutanix AHV Enterprise Hypervisor](https://www.nutanix.com/products/ahv) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> — Turnkey enterprise KVM-based hyperconverged platform providing Prism Central automation and VMware ESXi migration tooling for risk-averse enterprise private data centers.
  - **(2026)** [OpenStack Open Source Cloud Infrastructure](https://www.openstack.org) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Battle-tested open-source IaaS control plane powering Europe's Sovereign Cloud Stack (SCS), OVHcloud, STACKIT, Open Telekom Cloud, Elastx, Cleura, and Stackscale.
  - **(2026)** [Proxmox Virtual Environment (Proxmox VE)](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> — Open-source European KVM and LXC enterprise virtualization platform (Vienna, Austria) featuring Ceph HCI storage, Software-Defined Networking, live migration, and zero per-core Broadcom lock-in.
  - **(2026)** [SUSE Harvester Hyperconverged Infrastructure](https://harvesterhci.io) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Kubernetes-native open-source HCI built on KubeVirt and Longhorn, running legacy VMs and modern containers side-by-side in Rancher-managed private data centers.

---
💡 **Explore Related:** [EU Sovereign Cloud Overview & TCO](./eu-sovereign-cloud.md) | [Spain Sovereign Cloud & Private DCs](./eu-cloud-spain.md) | [Germany Sovereign Cloud & Private DCs](./eu-cloud-germany.md)

🔗 **See Also:** [Demos](./demos.md) | [DevOps](./devops.md)

