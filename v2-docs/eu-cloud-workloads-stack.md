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
    [EU Sovereign Cloud Overview & TCO](eu-sovereign-cloud.md) · [Germany Sovereign Cloud & Private DCs](eu-cloud-germany.md) · [France Sovereign Cloud & Private DCs](eu-cloud-france.md) · [Netherlands & Benelux Cloud & DCs](eu-cloud-benelux.md) · [Nordics Green Cloud & AI Factories](eu-cloud-nordics.md) · [IaC Automation & Maturity](eu-cloud-iac-maturity.md) · [RPO, RTO, SLAs & DRP](eu-cloud-resilience-sla.md) · [Kubernetes On-Premise](kubernetes-on-premise.md) · [Enterprise AI Platforms](enterprise-ai-platforms.md) · [European Neoclouds & AI Factories](neoclouds-europe.md)

## Pre-Sales Engineering Guide: Hypervisors, IaaS, Kubernetes and Sovereign AI Stacks

1. [Post-Broadcom Hypervisor Modernization Matrix](#post-broadcom-hypervisor-modernization-matrix)
2. [Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)](#virtualized-iaas-vs-dedicated-bare-metal-when-metal-wins)
3. [European Managed Kubernetes vs Declarative DIY Stack](#european-managed-kubernetes-vs-declarative-diy-stack)
4. [Sovereign AI and NVIDIA GPU Factories in Europe (2026)](#sovereign-ai-and-nvidia-gpu-factories-in-europe-2026)

### Post-Broadcom Hypervisor Modernization Matrix

With Broadcom's **VMware Cloud Foundation (VCF)** per-core subscription shifts raising renewal TCO by 2x–4x across Europe, pre-sales architects must clearly position the 7 production hypervisor architectures available in EU Sovereign Clouds and Private Data Centers:

| Hypervisor / Stack (Clickable) | Licensing &amp; Commercial Model | Storage &amp; HA Capabilities | IaC and Kubernetes Integration | Enterprise Support &amp; Maturity | When to Recommend (Pre-Sales Rule) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Proxmox VE**](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) + Ceph + [**PBS**](https://www.proxmox.com/en/products/proxmox-backup-server/overview) | **Open Source (AGPLv3)**; optional **EUR 110–1,050 / socket / yr** Enterprise support (Vienna HQ) | Native **Ceph HCI**, ZFS local/replication, live migration, SDN VXLAN/EVPN | [**`bpg/proxmox`**](https://github.com/bpg/terraform-provider-proxmox) + [**IONOS `CAPMOX`**](https://github.com/ionos-cloud/cluster-api-provider-proxmox) + [Packer](https://developer.hashicorp.com/packer) | Huge European partner ecosystem (Spain/DE MSPs) | **#1 Default VMware exit** for SMB &amp; mid-market private DCs / [Hetzner](https://www.hetzner.com/cloud) / [OVH](https://www.ovhcloud.com/en-ie) Metal needing 70–85% license savings |
| [**OpenStack**](https://www.openstack.org) ([**SCS**](https://scs.community) / [**Canonical**](https://ubuntu.com/openstack)) | Open Source (Apache-2.0); Commercial SLAs via [STACKIT](https://stackit.com/en), [Stackscale](https://www.stackscale.com), [Cleura](https://cleura.com), [Elastx](https://elastx.se/en), [Canonical](https://ubuntu.com/openstack) | **Ceph RBD**, NetApp Cinder, OVN multi-tenant SDN, L3/BGP routing | [**`openstack` Terraform**](https://github.com/terraform-provider-openstack/terraform-provider-openstack) + [**`CAPO`**](https://github.com/kubernetes-sigs/cluster-api-provider-openstack) | Industrial-scale proven across Europe's largest public clouds | **Service providers, telcos, and &gt;20-rack enterprises** building an internal multi-tenant AWS-like private cloud |
| [**Red Hat OpenShift Virtualization**](https://www.redhat.com/en/technologies/cloud-computing/openshift/virtualization) | Enterprise Red Hat per-core/node subscription (**RHCOS 10 / RHEL 10.2**, **K8s 1.36**) | [Rook-Ceph](https://github.com/rook/rook) / ODF / Trident CSI + live VM migration inside K8s pods | **100% GitOps YAML / K8s API / [Crossplane](https://www.crossplane.io) / [Argo CD](https://argo-cd.readthedocs.io)** | Top-tier enterprise SLA; **MTV Migration Toolkit** from vSphere | **Mission-critical banking/telco/public sector** unifying VMs and containers on ONE Red Hat platform + [RHOAI](https://www.redhat.com/en/products/ai/openshift-ai) |
| [**Apache CloudStack**](https://cloudstack.apache.org) | Open Source (Apache-2.0); Commercial support via [**ShapeBlue**](https://www.shapeblue.com) | Supports KVM, XCP-ng, NFS, Ceph, StorPool, SANs | Official CloudStack Terraform + [**`CAPC`**](https://github.com/kubernetes-sigs/cluster-api-provider-cloudstack) | Very lightweight control plane (~10% op complexity of OpenStack) | Regional MSPs and enterprises wanting AWS-style VPC/zone IaaS with minimal SRE headcount |
| [**SUSE Harvester**](https://harvesterhci.io) | Open Source (Apache-2.0); Optional SUSE Rancher Prime support | Native [**Longhorn**](https://github.com/longhorn/longhorn) distributed NVMe block + VLAN trunking | Rancher Terraform + [**CAPI**](https://cluster-api.sigs.k8s.io) / Fleet GitOps | Rapidly adopted by edge/telco &amp; Kubernetes-first teams | Edge campuses, factories, retail stores running unified **Rancher + K8s + light VMs** |
| **VMware Cloud Director (EU VCSP)** | **Broadcom VCSP Partner Program** pooled RAM/core OPEX ([Arsys](https://www.arsys.es/cloud), [Gigas](https://gigas.com/en), [PlusServer](https://www.plusserver.com/en), [Aruba](https://www.arubacloud.com)) | vSAN / NetApp / Dell PowerStore; [**Zerto**](https://www.zerto.com) / [**Veeam**](https://www.veeam.com) CDP DRaaS | [**`vmware/vcd`**](https://github.com/vmware/terraform-provider-vcd) + [**`CAPVCD`**](https://github.com/vmware/cluster-api-provider-cloud-director) | Highest zero-refactoring stability (familiar vCenter/NSX) | **Time-boxed 12–36 month bridge:** customer has Oracle/ERP appliances that cannot be migrated before hardware EOL |
| [**Nutanix AHV**](https://www.nutanix.com/products/ahv) | Per-core HCI subscription (usually 25–40% below aggressive VCF tiers) | Distributed AOS HCI + native asynchronous Metro HA | Official **Nutanix Terraform** + NKP | Turnkey 1-click upgrades; easiest vSphere GUI parallel | Risk-averse private DC teams wanting **VMware-like appliance simplicity** without managing Linux/Ceph internals |

### Virtualized IaaS vs Dedicated Bare Metal (When Metal Wins)

Do **not** blindly put every workload on virtualized cloud instances. Pitch **Dedicated Bare Metal** (on [**OVHcloud**](https://www.ovhcloud.com/en-ie), [**Scaleway**](https://www.scaleway.com/en), [**Hetzner**](https://www.hetzner.com/cloud), [**Stackscale**](https://www.stackscale.com), [**Leaseweb**](https://www.leaseweb.com), or [**Arsys**](https://www.arsys.es/cloud)) whenever ANY of these 4 triggers applies:

1. **Core-Licensed Commercial Software (Oracle DB, Microsoft SQL Server Enterprise, SAP):** Physical bare-metal core pinning cuts software licensing exposure compared to vCPU sprawl on shared public clouds.
2. **Sustained High Storage IOPS / Low Tail Latency (&lt;1 ms):** Dedicated dual-NVMe RAID or local Ceph eliminates noisy-neighbor hypervisor I/O jitter.
3. **Hyperconverged Private K8s / VM Fleet (&gt;32 vCPUs / &gt;128 GB RAM per node):** Running [**Talos Linux**](https://www.talos.dev) or [**Proxmox VE**](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) directly on **EUR 180–450/month bare-metal hosts** with 10–25 Gbps unmetered private networking delivers **2.5x–3.5x better compute density per EUR** than public IaaS VMs.
4. **Physical Hardware Compliance Isolation (PCI-DSS L1 / Banking / Defense):** Dedicated single-tenant chassis guarantees physical isolation and auditability without paying hyperscaler `Dedicated Host` 200% markups.

### European Managed Kubernetes vs Declarative DIY Stack

| Platform (Clickable) | Provider / Origin | Control Plane Cost | Multi-AZ / HA Maturity | Networking (CNI) &amp; Load Balancers | GPU Worker Support | Pre-Sales Fit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [**OVHcloud MKS**](https://www.ovhcloud.com/en-ie/public-cloud/kubernetes) | [OVHcloud](https://www.ovhcloud.com/en-ie) (FR) | **Free** | **3-AZ** in Paris; Multi-node etcd | [Cilium](https://cilium.io) / Calico + OVH Octavia LB | L40S, A100, H100 | Default zero-control-plane-tax EU Managed K8s |
| [**Scaleway Kapsule / Kosmos**](https://www.scaleway.com/en) | [Scaleway](https://www.scaleway.com/en) (FR) | **Free** (Ded. paid tier) | **3-AZ** Paris + Multi-Cloud **Kosmos** | [Cilium](https://cilium.io) eBPF + Scaleway LB | **L4, L40S, H100, B200** | Best developer UX + hybrid **Kosmos** nodes (attach [Hetzner](https://www.hetzner.com/cloud)/[Arsys](https://www.arsys.es/cloud) nodes!) |
| [**STACKIT SKE**](https://docs.stackit.cloud) | [STACKIT](https://stackit.com/en) (DE — [Gardener](https://gardener.cloud)) | Transparent metered | **3-AZ** Germany | [**Cilium**](https://cilium.io) eBPF + OpenStack Octavia LB | NVIDIA AI SKUs | German enterprise stability; automated Gardener self-healing |
| [**IONOS Managed K8s**](https://docs.ionos.com/cloud) | [IONOS](https://cloud.ionos.com) (DE) | **Free** control plane | Multi-DC EU (Frankfurt/Berlin/Spain link) | Calico + IONOS NLB | NVIDIA H200 / Enterprise VMs | Pairs cleanly with [**Arsys Spain**](https://www.arsys.es/cloud/kubernetes) &amp; [native Crossplane](https://github.com/ionos-cloud/crossplane-provider-ionoscloud) |
| [**secunet / MetaKube**](https://documentation.syseleven.de) | [secunet](https://www.secunet.cloud/en) (DE — Kubermatic) | Managed tier | **3-AZ** Germany | Cilium/Calico + LB | Dedicated / OpenStack GPU | SLA-backed production German DevOps clusters |
| [**Exoscale SKS**](https://www.exoscale.com) | [Exoscale](https://www.exoscale.com) (CH/AT) | Free Starter / SLA Pro | Multi-zone CH/EU | Calico + NLB | NVIDIA RTX / A100 / H100 | Swiss/Austrian regulated K8s simplicity |
| [**Civo K8s / Talos**](https://www.civo.com) | [Civo](https://www.civo.com) (UK) | Very low fixed node cost | Multi-region UK / EU | Cilium / Flannel + LB | H100 / B200 GPU instances | Sub-2-minute spin-up for CI/CD, UK Sovereign K8s &amp; AI |
| [**Arsys Managed K8s**](https://www.arsys.es/cloud/kubernetes) | [Arsys](https://www.arsys.es/cloud) (ES) | Node-based EUR pricing | **Spain [ENS Alto](https://ens.ccn.cni.es/en)** | Managed CNI + LB | Enterprise IaaS GPUs | Spanish public-sector &amp; ENS Alto container workloads |
| **DIY: [Talos Linux](https://www.talos.dev) + [Cilium](https://cilium.io) + [CAPI](https://cluster-api.sigs.k8s.io)** | Any Bare Metal ([Hetzner](https://www.hetzner.com/cloud) / [OVH](https://www.ovhcloud.com/en-ie) / [Stackscale](https://www.stackscale.com) / [Proxmox](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview)) | **EUR 0.00** | 3-DC or 3-AZ customer-controlled | [**Cilium**](https://cilium.io) eBPF + BGP Gateway API | **Full NVIDIA DRA / GPU Operator** | Maximum TCO victory (60–75% cheaper than EKS/AKS) for teams with 2+ Kubernetes SREs |

### Sovereign AI and NVIDIA GPU Factories in Europe (2026)

| EU AI Platform / Host (Clickable) | GPU Catalog &amp; Interconnect | Jurisdictional Protection | Software &amp; Serving Stack (`2026`) | Typical Pre-Sales Sweet Spot |
| :--- | :--- | :--- | :--- | :--- |
| [**Nebius AI Cloud**](https://nebius.com) | **H100, H200, Blackwell B200** clusters w/ **3.2 Tbps InfiniBand NDR** | **Amsterdam HQ (L4 EU)** + Finland/France clean energy | Managed Kubernetes (MK8s), Slurm, S3, `vLLM`, Ray, [Terraform](https://github.com/nebius/terraform-provider-nebius) | Multi-node foundation model training, LoRA fine-tuning, high-throughput batch AI in Europe |
| [**Scaleway AI &amp; Serverless**](https://www.scaleway.com/en) | **L4, L40S, H100 SXM, B200/B300** + Serverless AI Endpoints | **French/EU L4** + GDPR / [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) alignment | Kapsule K8s, Managed Inference (`vLLM`), [**Mistral AI**](https://mistral.ai)/Llama EU APIs | Fastest elastic GPU spin-up + pay-per-token EU serverless inference with zero US transit |
| [**OVHcloud AI**](https://www.ovhcloud.com/en-ie) | L40S, H100, AI Deploy, AI Notebooks | **French/EU L4** + [SecNumCloud](https://cyber.gouv.fr/en/secnumcloud-for-cloud-service-providers) roadmap | [MKS K8s](https://www.ovhcloud.com/en-ie/public-cloud/kubernetes), Triton/`vLLM` containers, **zero egress** for training datasets | Dataset-heavy vision/RAG pipelines moving TBs of European files without egress fees |
| [**Seeweb (Italy)**](https://www.seeweb.it/en) | Dedicated **H100 / L40S / A100** pods &amp; K8s nodes | **Italy/EU L4** (GDPR + EU AI Act ready) | K8s GPU nodes, bare-metal inference, custom RAG stacks | Southern European / Italian enterprises requiring bespoke dedicated GPU servers in EU |
| [**Nscale (UK &amp; Nordics)**](https://www.nscale.com) | **NVIDIA H100 / GB200** renewable superclusters | **UK HQ + European Green Campuses** | Kubernetes + Slurm GPU fabrics, `vLLM` serving | Sovereign British &amp; Northern European enterprise AI training &amp; inference |
| [**Merlin-Edged**](https://www.merlinproperties.com/en/data-centers) &amp; **Spain Colo** | Liquid-cooled **100 kW+ racks** ready for **NVIDIA GB200 NVL72** | **100% Spanish Private Facility ([`ENS Alto`](https://ens.ccn.cni.es/en) capable)** | [**Red Hat OpenShift AI**](https://www.redhat.com/en/products/ai/openshift-ai) + `llm-d` + [Mistral](https://mistral.ai) | Sovereign Spanish banking, defense, telco AI factories requiring physical air-gap / direct rack custody |
| [**MareNostrum 5 (BSC)**](https://www.bsc.es/marenostrum/marenostrum-5) · [**JUPITER**](https://www.fz-juelich.de/en/jsc/systems/supercomputers/jupiter) · [**LUMI**](https://lumi-supercomputer.eu) | Exascale / Pre-Exascale **NVIDIA GH200 / H100** supercomputers | **Public European EuroHPC AI Factories** | Slurm, PyTorch, **Salamandra / ALIA / Open European Models** | R&amp;D consortia, European SMEs (AI Factory access), sovereign foundation model training |

*Deep-dive companion guide: [European Neoclouds &amp; Country AI Factories](/neoclouds-europe/) · [GPU Fabrics, InfiniBand, Slurm vs K8s &amp; AI Storage](/neoclouds-architecture-stack/).*


## France Sovereign Cloud and Private Dcs

### French Sovereign Cloud Providers Secnumcloud And AI Factories

  - **(2026)** [Mistral AI Sovereign Frontier Models](https://mistral.ai) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Paris-based European AI champion delivering open-weight (Mistral/Mixtral/Codestral) and enterprise models optimized for self-hosted Kubernetes vLLM and European sovereign cloud AI endpoints.
  - **(2026)** [OVHcloud Managed Kubernetes Service (MKS)](https://www.ovhcloud.com/en-ie/public-cloud/kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — CNCF-certified Managed Kubernetes with free multi-master control plane, Cinder/Octavia OpenStack integration, NVIDIA H100/L40S worker pools, and multi-AZ support in Paris.
## Germany Sovereign Cloud and Private Dcs

### German Sovereign Cloud And Managed Kubernetes Providers

  - **(2026)** [SysEleven MetaKube Managed Kubernetes Documentation](https://documentation.syseleven.de) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Berlin-based OpenStack and CNCF Kubernetes documentation hub covering Kubermatic/MetaKube managed clusters across multi-AZ German sovereign data centers (part of the secunet Group).
## Italy Sovereign Cloud and Private Dcs

### Italy Sovereign Cloud And ACN Qualified Providers

  - **(2026)** [Seeweb Cloud and GPU AI Infrastructure](https://www.seeweb.it/en) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Independent Italian cloud and data center pioneer specializing in NVIDIA H100/L40S/A100 GPU clusters, Kubernetes, sovereign AI inference, and zero hyperscaler egress traps.
## Managed And Declarative Kubernetes On European Infrastructure

  - **(2026)** [SAP Gardener Multi-Cloud Kubernetes Fleet Engine](https://gardener.cloud) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-originated open-source Kubernetes-as-a-Service control plane powering STACKIT SKE, SysEleven MetaKube, and Cleura multi-AZ managed clusters.
  - **(2026)** [Talos Linux by Sidero Labs](https://www.talos.dev) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[HYPERVISOR]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Immutable, API-driven Kubernetes OS eliminating SSH and mutable Linux packages — the gold standard for running secure, declarative Kubernetes on Hetzner bare metal, OVH/Scaleway metal, Proxmox, or colocation.
## Netherlands and Benelux Cloud and Dcs

### Nordics Switzerland And Benelux Cloud And AI Providers

  - **(2026)** [Nebius Sovereign AI Cloud (Amsterdam HQ)](https://nebius.com) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — European-headquartered AI hyperscaler operating massive InfiniBand-interconnected NVIDIA H100, H200, and Blackwell B200 superclusters in Finland and France with Kubernetes (MK8s), Slurm, and Sovereign S3 storage.
## Spain Sovereign Cloud and Private Dcs

### Spanish National Compliance And Supercomputing

  - **(2026)** [Barcelona Supercomputing Center: MareNostrum 5](https://www.bsc.es/marenostrum/marenostrum-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — European EuroHPC pre-exascale supercomputer hosted in Barcelona powered by thousands of NVIDIA Hopper H100 GPUs, anchoring Spain's AI Factory and sovereign foundation model ecosystem (Salamandra / ALIA).
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

🔗 **See Also:** [European Neoclouds & Country AI Factories](./neoclouds-europe.md) | [Demos](./demos.md)

