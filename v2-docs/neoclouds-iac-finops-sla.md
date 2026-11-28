---
type: curation-hub
okf_version: "0.3"
name: "Neocloud IaC Maturity, GPU FinOps and Goodput SLAs"
dimension: "Neoclouds & GPU AI Clouds"
resource_count: 18
fresh_2025_2026_count: 18
trust: verified
freshness: active
provenance: "https://github.com/nubenetes/awesome-kubernetes/blob/master/docs/neoclouds-iac-finops-sla.md"
description: "Curated, AI-ranked Neocloud IaC Maturity, GPU FinOps & SLAs resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Neoclouds & GPU."
---
# Neocloud IaC Maturity, GPU FinOps and Goodput SLAs

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/neoclouds-iac-finops-sla/).

!!! info "Architectural Context"
    Detailed reference for Neocloud IaC Maturity, GPU FinOps and Goodput SLAs in the context of Neoclouds & GPU AI Clouds.

!!! abstract "Deep-Dive Topic Pages"
    [Neoclouds Overview & Sovereign Overlap](neoclouds.md) · [GPU Fabrics, InfiniBand, Slurm vs K8s & Storage](neoclouds-architecture-stack.md) · [EU Sovereign IaC Maturity Scorecard](eu-cloud-iac-maturity.md) · [EU Sovereign RPO, RTO & SLAs](eu-cloud-resilience-sla.md) · [Terraform & OpenTofu](terraform.md) · [Cloud FinOps](finops.md)

## Pre-Sales Engineering Guide: Neocloud IaC Maturity, GPU FinOps and Goodput SLAs

1. [Neocloud IaC Coverage Scorecard (vs Hyperscalers = 100%)](#neocloud-iac-coverage-scorecard-vs-hyperscalers-100)
2. [Multi-Neocloud Portability Pattern (OpenTofu + SkyPilot + LiteLLM)](#multi-neocloud-portability-pattern-opentofu-skypilot-litellm)
3. [Goodput vs Uptime: Multi-Node GPU MTBF and Checkpointing SLAs](#goodput-vs-uptime-multi-node-gpu-mtbf-and-checkpointing-slas)
4. [GPU FinOps: Spot vs Bare Metal vs Token API Break-Even Rules](#gpu-finops-spot-vs-bare-metal-vs-token-api-break-even-rules)

### Neocloud IaC Coverage Scorecard (vs Hyperscalers = 100%)

Do **not** promise hyperscaler-style 250-resource Terraform breadth on every Neocloud. Instead, audit whether a provider automates the **5 critical GPU lifecycle primitives** (`GPU Cluster/NodeGroup, InfiniBand VPC, Parallel FS, S3, OIDC/IAM`) in [**OpenTofu**](https://opentofu.org) / Terraform:

| Provider (Clickable) | [OpenTofu](https://opentofu.org) / Terraform Coverage (vs AWS/Azure = 100%) | Official Provider / Repo | Managed Kubernetes &amp; [Slurm](https://slurm.schedmd.com) Provisioning | Primary Day-2 IaC Gaps &amp; Mitigation Strategy |
| :--- | :---: | :--- | :--- | :--- |
| [**Scaleway**](https://www.scaleway.com/en/gpu-instances) (FR/EU) | **85%** | [`scaleway/scaleway`](https://github.com/scaleway/terraform-provider-scaleway) + [Crossplane](https://github.com/scaleway/crossplane-provider-scaleway) | Declarative **Kapsule / Kosmos K8s** GPU node pools + IAM + S3 + VPC | Top EU DevOps experience; minor frontier Blackwell allocation limits still use console/account quota requests. |
| [**Vultr**](https://docs.vultr.com/products/compute/instances/cloud-gpu) &amp; [**DigitalOcean**](https://www.digitalocean.com/products/gpu-droplets) | **80%** | [`vultr/vultr`](https://github.com/vultr/terraform-provider-vultr) · [`digitalocean`](https://github.com/digitalocean/terraform-provider-digitalocean) | Official VKE/DOKS K8s + Cloud GPU VMs + Bare Metal + BGP/VPC | Lacks multi-node lossless InfiniBand fabrics; treat as distributed single-node inference/CI target. |
| [**Nebius**](https://nebius.com) (NL/FI/FR/US) | **75%** | [`nebius/nebius`](https://github.com/nebius/terraform-provider-nebius) ([docs](https://docs.nebius.com)) | [**MK8s GPU node groups**](https://nebius.com/compute/kubernetes), InfiniBand fabrics, Shared FS, S3, IAM cleanly in HCL | Younger provider surface for non-GPU PaaS; pair cleanly with [**Argo CD**](https://argo-cd.readthedocs.io) &amp; [**CloudNativePG**](https://cloudnative-pg.io) inside MK8s. |
| [**CoreWeave**](https://coreweave.com) (US/EU) | **70%** *(K8s-First)* | [CoreWeave Docs](https://docs.coreweave.com) + [**`coreweave/sunk-anywhere`**](https://github.com/coreweave/sunk-anywhere) | Everything centers on Kubernetes CRDs (`CKS`, `SUNK`, virtual-servers via K8s API) | Different mental model from AWS EC2 IAM: **treat CoreWeave Kubernetes itself as your control plane** via [Argo CD](https://argo-cd.readthedocs.io) / [Helm](https://helm.sh). |
| [**Crusoe Cloud**](https://crusoe.ai) (US/IS) | **70%** | [`crusoecloud/crusoe`](https://github.com/crusoecloud/terraform-provider-crusoe) ([docs](https://docs.crusoe.ai)) | Declarative InfiniBand partition networks, GPU VMs, K8s &amp; NVMe volumes | Multi-hundred-GPU physical InfiniBand topology reservations remain account-coordinated upfront. |
| [**Civo**](https://www.civo.com/ai) (UK) &amp; [**Gcore**](https://gcore.com/cloud/ai-gpu) (LU) | **75%** | [`civo/civo`](https://github.com/civo/terraform-provider-civo) · [`G-Core/gcore`](https://github.com/G-Core/terraform-provider-gcore) | Ultra-fast declarative K3s/[Talos](https://www.talos.dev) + GPU worker pools + S3 + Edge AI | Smaller DC catalogs; easy multi-cloud inclusion via standard K8s/[Helm](https://helm.sh)/[Pulumi](https://www.pulumi.com). |
| [**Nscale**](https://nscale.com) (UK/EU) &amp; [**Verda**](https://verda.com) (FI) | **65%** | [`nscaledev/nscale`](https://github.com/nscaledev/terraform-provider-nscale) + Verda REST/SDK | Declarative VPCs, GPU clusters, AI filesystems &amp; compute instances | Rapidly evolving provider APIs; verify multi-node [Slurm](https://slurm.schedmd.com)/K8s cluster bootstrapping scripts in POC. |
| [**RunPod**](https://www.runpod.io) · [**Modal**](https://modal.com) · [**Baseten**](https://www.baseten.co) | **65–75%** | [`runpod/runpod`](https://github.com/runpod/terraform-provider-runpod) + Python-as-Code SDKs | Automates GPU pods, Serverless [vLLM](https://github.com/vllm-project/vllm)/[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) endpoints, Network Volumes | Lack of enterprise L2/BGP peering restricts them to containerized inference or stateless CI bursts. |
| [**Lambda**](https://lambda.ai) / [**Voltage Park**](https://voltagepark.com) / Regional | **45 – 60%** | Cloud REST APIs + [**SkyPilot**](https://github.com/skypilot-org/skypilot) + [Ansible](https://docs.ansible.com) (`1-Click` Slurm/SSH) | Reservation-based cluster spin-up; heavy reliance on post-provision Ansible/Slurm | Wrap bare-metal clusters declaratively via **SkyPilot + [Ansible](https://docs.ansible.com) + [Argo CD](https://argo-cd.readthedocs.io)** rather than bespoke scripts. |

### Multi-Neocloud Portability Pattern (OpenTofu + SkyPilot + LiteLLM)

Never let a single GPU vendor hold your AI roadmap hostage when spot prices spike or new silicon launches. Enforce this **3-Layer Decoupling Stack**:

```yaml
# 1. SkyPilot task YAML: portable across Nebius, Lambda, Crusoe, RunPod, Civo, AWS, GCP
resources:
  accelerators: H100:8
  infra: nebius          # Fail over automatically across clouds/regions (`any_of`)
  disk_size: 2048
file_mounts:
  /checkpoints:
    source: s3://acme-eu-sovereign-checkpoints/llama-ft/
    mode: MOUNT
run: |
  torchrun --nproc_per_node=8 train.py --resume-from /checkpoints/latest
```

1. **Compute Layer ([`OpenTofu`](https://opentofu.org) `+` [`SkyPilot`](https://github.com/skypilot-org/skypilot) `+` [`Cluster API`](https://cluster-api.sigs.k8s.io)):** Provision base clusters cleanly via OpenTofu, or let **SkyPilot** ([docs](https://skypilot.readthedocs.io)) hunt spare `8x H100 / H200` capacity automatically across [**Nebius**](https://nebius.com), [**Lambda**](https://lambda.ai), [**Crusoe**](https://crusoe.ai), [**Fluidstack**](https://fluidstack.io), [**RunPod**](https://www.runpod.io), and hyperscalers with automated spot recovery.
2. **State &amp; Weight Layer (`EU/Local S3 + Async Sync`):** Store datasets, tokenized shards, and safetensors checkpoints outside proprietary local disks inside **cross-region S3 buckets** ([**Scaleway FR**](https://www.scaleway.com/en/gpu-instances) / [**OVHcloud**](https://www.ovhcloud.com/en/public-cloud/ai-training) / [**Nebius**](https://nebius.com) / [AWS](https://aws.amazon.com)) and stream cold boots via [**Tensorizer**](https://github.com/coreweave/tensorizer).
3. **Inference Routing Layer ([`Gateway API Inference Extension`](https://github.com/kubernetes-sigs/gateway-api-inference-extension) `+` [`LeaderWorkerSet`](https://github.com/kubernetes-sigs/lws) `+` [`LiteLLM`](https://github.com/BerriAI/litellm)):** Expose a single internal OpenAI-compatible URL to apps; dynamically split traffic between **on-prem/Neocloud [vLLM](https://github.com/vllm-project/vllm)/[`SGLang`](https://github.com/sgl-project/sglang)/[`llm-d`](https://github.com/llm-d/llm-d) pods** and **Serverless fallback APIs** ([Together](https://www.together.ai) / [Fireworks](https://fireworks.ai) / [Baseten](https://www.baseten.co) / [Regolo](https://regolo.ai) / [Bedrock](https://aws.amazon.com/bedrock)).

### Goodput vs Uptime: Multi-Node GPU MTBF and Checkpointing SLAs

!!! danger "Why Standard 99.9% Cloud Uptime SLAs Mislead Distributed Training Teams"
    A single [**NVIDIA H100**](https://www.nvidia.com/en-us/data-center/h100)/[**GB200**](https://www.nvidia.com/en-us/data-center/gb200-nvl72) SXM system contains thousands of high-power solder joints, optical transceivers, HBM dies, and liquid cooling manifolds. Across a **1,024-GPU training cluster**, empirical hardware/IB link **Mean Time Between Interruptions (MTBI)** drops to roughly **1–3 failures per day**! A naive provider boasting "99.9% host uptime" gives you **zero protection** if silent InfiniBand bit errors slow training by 35% without triggering a VM reboot.

Pre-sales architects MUST replace generic VM uptime clauses with **Goodput &amp; Fabric SLAs**:

| Metric / SLA Clause | Naive Hyperscaler VM Contract | Production Neocloud ([`ClusterMAX Platinum/Gold`](https://www.clustermax.ai)) Standard | Mandatory Automation &amp; Pre-Sales Check |
| :--- | :--- | :--- | :--- |
| **Effective Goodput Ratio** | Not guaranteed (noisy neighbors / TCP backoff silently cut MFU) | **85%+ of theoretical `nccl-tests` AllReduce bus bandwidth** guaranteed continuously | Run [**`coreweave/nccl-tests`**](https://github.com/coreweave/nccl-tests) burn-in **before** accepting handover of any multi-node reservation. |
| **Proactive XID / ECC Replacement** | Ticket required; slow multi-hour VM stop/start &amp; manual investigation | Automated [**NVIDIA DCGM Exporter**](https://github.com/NVIDIA/dcgm-exporter) detecting XID critical errors ([**DCGM Guide**](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide)) and hot-swapping warm spares in **&lt; 5 min** | Require pre-allocated **2–5% hot-standby spare nodes** in every `&gt;= 128-GPU` reserved contract. |
| **Inference RPO / RTO (Serving)** | Multi-AZ load balancing within single hyperscaler region | **RPO = 0** (immutable [Argo CD](https://argo-cd.readthedocs.io) prompts + S3 weights) · **RTO &lt; 30s** via active-active [**LiteLLM**](https://github.com/BerriAI/litellm) / [Gateway API](https://github.com/kubernetes-sigs/gateway-api-inference-extension) multi-vendor failover | Never serve mission-critical RAG from a **single-DC Neocloud zone**; mirror quantized [vLLM](https://github.com/vllm-project/vllm) replica across a secondary DC/provider. |
| **Training Checkpoint RPO** | Customer-managed EBS/S3 scripts | **RPO = 15–30 min** via **async [WEKA](https://docs.weka.io)/[VAST](https://www.vastdata.com)/[Lustre](https://www.lustre.org) write + S3 mirror** | Verify **checkpoint serialization latency &lt; 60s** so frequent saves consume `&lt; 3%` of paid GPU-hours. |

### GPU FinOps: Spot vs Bare Metal vs Token API Break-Even Rules

*Financial engineering rules validated via [**OpenCost**](https://github.com/opencost/opencost), [**Grafana**](https://grafana.com), and real-time cluster telemetry (`EUR` baseline):*

1. **Break-Even Threshold (Serverless Token API vs Dedicated 24x7 GPUs):** Stay on pay-per-token APIs ([**Together AI**](https://www.together.ai), [**Fireworks**](https://fireworks.ai), [**Baseten**](https://www.baseten.co), [**Scaleway Generative APIs**](https://www.scaleway.com/en/generative-apis), [**Regolo.ai**](https://regolo.ai), [**AWS Bedrock**](https://aws.amazon.com/bedrock), [**Azure AI Foundry**](https://azure.microsoft.com/en-us/products/ai-foundry), [**Vertex AI**](https://cloud.google.com/vertex-ai)) whenever aggregate sustained concurrency utilizes **`&lt; 35–45%`** of a dedicated **8x H100/L40S pod** over 24 hours. Above **45% continuous duty cycle**, self-hosting quantized [**vLLM**](https://github.com/vllm-project/vllm) / [**SGLang**](https://github.com/sgl-project/sglang) / [**`llm-d`**](https://github.com/llm-d/llm-d) on a Neocloud yields **40–70% immediate monthly EUR savings**.
2. **Preemptible Spot vs Reserved Bare Metal:** Use **Spot / On-Demand Preemptible (`30–50% cheaper`)** via [**SkyPilot**](https://github.com/skypilot-org/skypilot) exclusively for stateless evals, synthetic data generation, embeddings, and LoRA sweeps (`&lt; 4h` jobs). Lock **3-to-12-month Reserved Bare-Metal Clusters** ONLY once training architectures stabilize above 60% schedule fill.
3. **Eliminate 'Zombie Notebooks &amp; Idle H100s':** Enforce [**NVIDIA KAI Scheduler**](https://github.com/NVIDIA/KAI-Scheduler) / [**Kueue**](https://github.com/kubernetes-sigs/kueue) / [**Volcano**](https://volcano.sh) time-slicing or MIG (`1g.10gb` / `3g.40gb`) for developer notebooks and automated idle-reaper policies (`scale-to-zero` after 15 min idle VRAM) so **EUR 2.00+/hr GPUs** never sit burning budget overnight.


## European Sovereign Cloud and Private Dcs

### IaC Automation and Maturity Vs Hyperscalers

#### Official Terraform And Opentofu Providers For European Clouds

  - **(2026)** [Civo Official Terraform Provider](https://github.com/civo/terraform-provider-civo) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Lightweight IaC provider for Civo K3s/Talos Managed Kubernetes clusters, firewalls, networks, and UK Sovereign workloads.
  - **(2026)** [Nebius Official Terraform Provider](https://github.com/nebius/terraform-provider-nebius) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Official OpenTofu/Terraform provider for Nebius AI GPU clusters, MK8s Kubernetes, Filesystem/S3 storage, and InfiniBand GPU fabrics.
  - **(2026)** [Scaleway Official Terraform Provider](https://github.com/scaleway/terraform-provider-scaleway) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — High-coverage IaC provider automating Scaleway Instances, Kapsule/Kosmos Kubernetes, Managed PostgreSQL/Redis, IAM/RBAC, Serverless Containers/Functions, and AI Endpoints.
## GPU Health Telemetry And Inference AI Gateways

  - **(2026)** [Gateway API Inference Extension (Kubernetes SIG Network)](https://github.com/kubernetes-sigs/gateway-api-inference-extension) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Upstream Kubernetes L7 AI Gateway standard routing OpenAI-compatible prompts across multi-provider Neocloud vLLM backends using KV-cache pressure and LoRA adapter locality.
  - **(2026)** [Kubernetes LeaderWorkerSet (`lws`) for Multi-Node AI](https://github.com/kubernetes-sigs/lws) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — SIG-Apps Kubernetes API modeling multi-host distributed model inference (e.g., 2x8x H200 DeepSeek/405B deployments) as atomic gang-restarted units across Neoclouds.
  - **(2026)** [LiteLLM Open-Source AI Gateway and Failover Proxy](https://github.com/BerriAI/litellm) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Unified OpenAI-format proxy routing inference traffic seamlessly across Neocloud vLLM endpoints (Nebius, Scaleway, Together, Fireworks, Regolo) and hyperscalers with latency/cost fallbacks.
  - **(2026)** [NVIDIA DCGM Exporter for Prometheus](https://github.com/NVIDIA/dcgm-exporter) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Essential Kubernetes DaemonSet exporting per-GPU SM occupancy, NVLink errors, XID fault codes, memory bandwidth, and power telemetry for goodput SLA enforcement.
  - **(2026)** [NVIDIA DCGM User Guide (Proactive Health Checks)](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Official reference for automated active diagnostics, XID hardware failure policy alerts, and node cordon/drain triggers before silent GPU hangs corrupt training checkpoints.
  - **(2026)** [SGLang: High-Performance Structured LLM Serving](https://github.com/sgl-project/sglang) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Fast open-source LLM runtime leveraging RadixAttention prefix caching to slash Neocloud GPU compute requirements on agentic and multi-turn RAG workloads.
## Infrastructure As Code

### Multi-cloud Provisioning

#### Pulumi

  - **(2026)** [Pulumi](https://www.pulumi.com) <span class='md-tag md-tag--warning'>[POLYGLOT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pulumi is an industry-leading infrastructure-as-code platform enabling multi-cloud resource provisioning through standard programming languages. It provides rich testing utilities, compiler-driven schema safety, and scalable cloud state backends.
## Infrastructure Optimization

### Cost Management

#### Tooling

  - **(2024)** [==github.com/kubecost: kubecost-exporter - Running Kubecost as a Prometheus metric exporter==](https://github.com/opencost/opencost) <span class='md-tag md-tag--info'>⭐ 6590</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-16b8fe89" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 5 L 20 13 L 30 11 L 40 2 L 50 4" fill="none" stroke="url(#spark-grad-16b8fe89)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--primary'>[CNCF INCUBATING]</span> <span class='md-tag md-tag--info' title='Open-source license'>⚖️ Apache-2.0</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official repository for OpenCost, the CNCF sandbox standard defining vendor-neutral APIs for cloud-native cost allocation. Operates as an open-source real-time metrics exporter for Prometheus, serving as the industry standard benchmark across multi-cloud deployments.
## Neocloud IaC Providers And Multi-cloud Schedulers

  - **(2026)** [CoreWeave NCCL Multi-Node Health Tests](https://github.com/coreweave/nccl-tests) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Reference distributed GPU fabric burn-in tests measuring AllReduce bus bandwidth and catching degraded InfiniBand/NVLink links before paying for long training epochs.
  - **(2026)** [Crusoe Official Terraform Provider (`crusoecloud/crusoe`)](https://github.com/crusoecloud/terraform-provider-crusoe) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Terraform provider provisioning clean-energy Crusoe H100/H200/Blackwell VMs, InfiniBand partition networks, Kubernetes clusters, and NVMe disks.
  - **(2026)** [DigitalOcean Official Terraform Provider (`digitalocean/digitalocean`)](https://github.com/digitalocean/terraform-provider-digitalocean) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Mature Terraform/OpenTofu provider automating DigitalOcean GPU Droplets (H100/H200/MI300X), DOKS Kubernetes GPU node pools, VPCs, and Spaces S3 storage.
  - **(2026)** [Nscale Official Terraform Provider (`nscaledev/nscale`)](https://github.com/nscaledev/terraform-provider-nscale) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Declarative IaC provider managing Nscale sovereign UK/European GPU instances, AI cluster networking, and parallel storage volumes.
  - **(2026)** [RunPod Official Terraform Provider (`runpod/runpod`)](https://github.com/runpod/terraform-provider-runpod) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[LLM]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> — Declarative IaC provider automating RunPod Secure Cloud GPU pods, Serverless vLLM workers, and Network Volumes.
  - **(2026)** [SkyPilot: Cross-Neocloud Compute Broker](https://github.com/skypilot-org/skypilot) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NEOCLOUD]</span> <span class='md-tag md-tag--primary'>[SOVEREIGN-EU]</span> — Single YAML abstraction automatically hunting cheapest available GPUs across Nebius, Lambda, RunPod, Fluidstack, Civo, AWS, Azure, and GCP with automatic spot recovery.
  - **(2026)** [Vultr Official Terraform Provider (`vultr/vultr`)](https://github.com/vultr/terraform-provider-vultr) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> — Full-lifecycle Terraform/OpenTofu automation covering Vultr Cloud GPU VMs, bare-metal hosts, VKE Kubernetes clusters, and VPC networking worldwide.

---
💡 **Explore Related:** [Neoclouds Overview, Sovereign Overlap & TCO](./neoclouds.md) | [European Neoclouds & Country AI Factories](./neoclouds-europe.md) | [North America Neoclouds (US & Canada)](./neoclouds-north-america.md)

🔗 **See Also:** [Hypervisors, IaaS, K8s & Sovereign AI](./eu-cloud-workloads-stack.md) | [MLOps](./mlops.md)

