# GPU Fabrics, InfiniBand, Slurm vs Kubernetes and AI Storage

Curated systems-engineering guide to Neocloud hardware and software internals: **NVIDIA GB200 NVL72 / AMD Instinct MI300X silicon, Quantum-2 InfiniBand vs Spectrum-X Ethernet, SUNK (Slurm on Kubernetes) vs KubeRay/Kueue/vLLM/llm-d, and WEKA/VAST/Lustre checkpoint storage**.

1. [GPU Silicon and Non-Blocking AI Networking Fabrics](#gpu-silicon-and-non-blocking-ai-networking-fabrics)
2. [Slurm vs Kubernetes GPU Schedulers and Distributed Inference](#slurm-vs-kubernetes-gpu-schedulers-and-distributed-inference)
3. [Parallel NVMe Filesystems and Checkpoint Storage](#parallel-nvme-filesystems-and-checkpoint-storage)

## GPU Silicon and Non-Blocking AI Networking Fabrics

- **(2026)** [NVIDIA GB200 NVL72 Rack-Scale Exascale Architecture](https://www.nvidia.com/en-us/data-center/gb200-nvl72) 🌟 - Liquid-cooled 72-Blackwell-GPU NVLink coherence domain delivering 130 TB/s intra-rack bandwidth, turning an entire Neocloud rack into a single giant accelerator for trillion-parameter training and MoE inference.
- **(2026)** [NVIDIA Quantum-2 InfiniBand AI Platform](https://www.nvidia.com/en-us/networking/quantum2) 🌟 - 400 Gbps (NDR) lossless RDMA switched fabric with in-network SHARP aggregation delivering microsecond tail latency critical for multi-thousand-GPU AllReduce training convergence.
- **(2026)** [NVIDIA Spectrum-X Ethernet for AI Fabrics](https://www.nvidia.com/en-us/networking/spectrumx) 🌟 - Adaptive-routing, congestion-controlled RoCEv2 Ethernet fabric achieving up to 95% effective network utilization across multi-tenant Neoclouds and enterprise K8s clusters without proprietary InfiniBand switches.
- **(2026)** [AMD Instinct MI300X HBM3 Accelerators](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) 🌟 - 192 GB HBM3 per-GPU accelerator powering TensorWave and Oracle/Crusoe clusters to host whole 70B–405B models with minimal tensor-parallelism splitting overhead.
- **(2026)** [AMD ROCm Open Software Stack Documentation](https://rocm.docs.amd.com) 🌟 - Official open-source GPU compute documentation covering HIP, RCCL collective communications, PyTorch integration, and vLLM acceleration on AMD Neocloud hardware.

## Slurm vs Kubernetes GPU Schedulers and Distributed Inference

- **(2026)** [CoreWeave SUNK: Slurm on Kubernetes Anywhere](https://github.com/coreweave/sunk-anywhere) 🌟 - Production pattern co-running Slurm HPC job scheduling and Kubernetes control planes natively inside one cluster so research and serving share the same GPU pool dynamically.
- **(2026)** [Slurm Workload Manager Documentation](https://slurm.schedmd.com) 🌟 - De facto bare-metal HPC batch scheduler still preferred by frontier training teams needing rigid topology-aware InfiniBand gang scheduling and zero-overhead PMIx launches.
- **(2026)** [NVIDIA GPU Operator for Kubernetes](https://github.com/NVIDIA/gpu-operator) 🌟 - Automated Kubernetes lifecycle management for NVIDIA drivers, container toolkits, MIG partitioning, DCGM monitoring, GPUDirect RDMA, and Dynamic Resource Allocation (DRA).
- **(2026)** [NVIDIA KAI Scheduler (Open-Source Run:ai Engine)](https://github.com/NVIDIA/KAI-Scheduler) 🌟 - Kubernetes-native GPU scheduler enabling gang scheduling, fractional GPU sharing, fair-share team queues, and preemption across Neocloud and on-prem clusters.
- **(2026)** [Kubernetes Kueue: Cloud-Native Batch Queueing](https://github.com/kubernetes-sigs/kueue) 🌟 - CNCF/SIG-Scheduling controller turning standard Kubernetes into a multi-tenant AI batch queue with quota borrowing, topology-aware placement, and Fair Sharing.
- **(2026)** [vLLM High-Throughput Open-Source Inference Engine](https://github.com/vllm-project/vllm) 🌟 - PagedAttention LLM serving runtime maximizing tokens/sec per GPU dollar across NVIDIA and AMD Neocloud fleets with OpenAI-compatible APIs.
- **(2026)** [llm-d: Kubernetes-Native Distributed LLM Inference](https://github.com/llm-d/llm-d) 🌟 - Red Hat, Google, and IBM backed Kubernetes-native disaggregated prefill/decode architecture scheduling vLLM KV-cache-aware pods over Gateway API Inference Extension.
- **(2026)** [KubeRay: Distributed Ray Clusters on Kubernetes](https://github.com/ray-project/kuberay) 🌟 - CNCF/Kubernetes operator orchestrating heterogeneous distributed reinforcement learning (RLHF), Ray Data pipelines, and multi-node RayServe fleets.

## Parallel NVMe Filesystems and Checkpoint Storage

- **(2026)** [WEKA AI-Native Parallel Data Platform Documentation](https://docs.weka.io) 🌟 - Sub-millisecond POSIX and S3 NVMe-over-Fabrics parallel filesystem widely deployed inside CoreWeave, Nscale, and European AI Factories to eliminate training checkpoint stalls.
- **(2026)** [VAST Data AI Operating System](https://www.vastdata.com) 🌟 - Disaggregated shared-everything (DASE) exabyte storage architecture combining GPUDirect Storage throughput with vector database and S3 object tiering inside sovereign Neoclouds.
- **(2026)** [DDN EXAScaler Lustre High-Performance Storage](https://www.ddn.com) 🌟 - Enterprise Lustre parallel filesystem powering JUPITER, Leonardo, and NVIDIA DGX SuperPOD reference architectures at extreme sequential checkpoint bandwidth.
