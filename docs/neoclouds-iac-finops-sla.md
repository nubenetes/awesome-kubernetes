# Neocloud IaC Maturity, GPU FinOps and Goodput SLAs

Curated engineering reference for automating GPU Neoclouds with **Terraform, OpenTofu, Cluster API, and SkyPilot**, designing **goodput and MTBF/checkpoint resilience SLAs**, optimizing **spot vs bare-metal GPU FinOps**, and enforcing multi-provider exit portability under **EU DORA and the AI Act**.

1. [Neocloud IaC Providers and Multi-Cloud Schedulers](#neocloud-iac-providers-and-multi-cloud-schedulers)
2. [GPU Health, Telemetry and Inference AI Gateways](#gpu-health-telemetry-and-inference-ai-gateways)

## Neocloud IaC Providers and Multi-Cloud Schedulers

- **(2026)** [SkyPilot: Cross-Neocloud Compute Broker](https://github.com/skypilot-org/skypilot) 🌟 - Single YAML abstraction automatically hunting cheapest available GPUs across Nebius, Lambda, RunPod, Fluidstack, Civo, AWS, Azure, and GCP with automatic spot recovery.
- **(2026)** [Nebius Official Terraform Provider (`nebius/nebius`)](https://github.com/nebius/terraform-provider-nebius) 🌟 - Official OpenTofu/Terraform provider automating Nebius GPU clusters, Managed Kubernetes (MK8s) node groups, InfiniBand fabrics, Shared Filesystems, and S3 buckets.
- **(2026)** [Nscale Official Terraform Provider (`nscaledev/nscale`)](https://github.com/nscaledev/terraform-provider-nscale) 🌟 - Declarative IaC provider managing Nscale sovereign UK/European GPU instances, AI cluster networking, and parallel storage volumes.
- **(2026)** [Crusoe Official Terraform Provider (`crusoecloud/crusoe`)](https://github.com/crusoecloud/terraform-provider-crusoe) 🌟 - Terraform provider provisioning clean-energy Crusoe H100/H200/Blackwell VMs, InfiniBand partition networks, Kubernetes clusters, and NVMe disks.
- **(2026)** [Vultr Official Terraform Provider (`vultr/vultr`)](https://github.com/vultr/terraform-provider-vultr) 🌟 - Full-lifecycle Terraform/OpenTofu automation covering Vultr Cloud GPU VMs, bare-metal hosts, VKE Kubernetes clusters, and VPC networking worldwide.
- **(2026)** [Scaleway Official Terraform Provider (`scaleway/scaleway`)](https://github.com/scaleway/terraform-provider-scaleway) 🌟 - Mature European Terraform/OpenTofu provider (85% coverage) automating Scaleway H100/L40S instances, Kapsule Kubernetes GPU pools, Private VPCs, and S3 buckets.
- **(2026)** [Civo Official Terraform Provider (`civo/civo`)](https://github.com/civo/terraform-provider-civo) 🌟 - Lightweight Terraform provider automating sub-2-minute Civo Kubernetes and sovereign UK GPU worker pools.
- **(2026)** [RunPod Official Terraform Provider (`runpod/runpod`)](https://github.com/runpod/terraform-provider-runpod) 🌟 - Declarative IaC provider automating RunPod Secure Cloud GPU pods, Serverless vLLM workers, and Network Volumes.
- **(2026)** [CoreWeave NCCL Multi-Node Health Tests](https://github.com/coreweave/nccl-tests) 🌟 - Reference distributed GPU fabric burn-in tests measuring AllReduce bus bandwidth and catching degraded InfiniBand/NVLink links before paying for long training epochs.

## GPU Health, Telemetry and Inference AI Gateways

- **(2026)** [NVIDIA DCGM Exporter for Prometheus](https://github.com/NVIDIA/dcgm-exporter) 🌟 - Essential Kubernetes DaemonSet exporting per-GPU SM occupancy, NVLink errors, XID fault codes, memory bandwidth, and power telemetry for goodput SLA enforcement.
- **(2026)** [NVIDIA DCGM User Guide (Proactive Health Checks)](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide) 🌟 - Official reference for automated active diagnostics, XID hardware failure policy alerts, and node cordon/drain triggers before silent GPU hangs corrupt training checkpoints.
- **(2026)** [OpenCost: Multi-Cloud Kubernetes and GPU FinOps](https://github.com/opencost/opencost) 🌟 - CNCF cost-allocation engine tracking per-namespace GPU utilization, idle accelerator waste, and Neocloud vs hyperscaler unit token costs in Grafana.
- **(2026)** [Gateway API Inference Extension (Kubernetes SIG Network)](https://github.com/kubernetes-sigs/gateway-api-inference-extension) 🌟 - Upstream Kubernetes L7 AI Gateway standard routing OpenAI-compatible prompts across multi-provider Neocloud vLLM backends using KV-cache pressure and LoRA adapter locality.
- **(2026)** [LiteLLM Open-Source AI Gateway and Failover Proxy](https://github.com/BerriAI/litellm) 🌟 - Unified OpenAI-format proxy routing inference traffic seamlessly across Neocloud vLLM endpoints (Nebius, Scaleway, Together, Fireworks, Regolo) and hyperscalers with latency/cost fallbacks.
- **(2026)** [SGLang: High-Performance Structured LLM Serving](https://github.com/sgl-project/sglang) 🌟 - Fast open-source LLM runtime leveraging RadixAttention prefix caching to slash Neocloud GPU compute requirements on agentic and multi-turn RAG workloads.
- **(2026)** [Kubernetes LeaderWorkerSet (`lws`) for Multi-Node AI](https://github.com/kubernetes-sigs/lws) 🌟 - SIG-Apps Kubernetes API modeling multi-host distributed model inference (e.g., 2x8x H200 DeepSeek/405B deployments) as atomic gang-restarted units across Neoclouds.
