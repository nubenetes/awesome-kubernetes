---
description: "Top CI/CD Kubernetes Plugins resources for 2026, AI-ranked: Jenkins Kubernetes Plugin, GitLab Kubernetes Agent and more — curated Cloud Native tools, guides and."
---
# CI/CD Kubernetes Plugins

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/cicd-kubernetes-plugins/).

!!! info "Architectural Context"
    Detailed reference for CI/CD Kubernetes Plugins in the context of Engineering Pipeline.

## CICD

### Automation

#### Deployment Tools

  - **(2023)** [==Kubernetes Continuous Deploy==](https://plugins.jenkins.io/kubernetes-cd) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized Jenkins plugin designed to coordinate container deployment pipelines, allowing seamless application delivery onto Kubernetes clusters. It handles cluster authentication, manifest interpolation, and rollout verification, although modern enterprise GitOps architectures have largely transitioned target deployments to ArgoCD or Flux.
#### Jenkins Integration

  - **(2024)** [==Jenkins Kubernetes Plugin==](https://plugins.jenkins.io/kubernetes) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A foundational plugin that integrates Jenkins with Kubernetes clusters to dynamically provision Jenkins agent pods on-demand. By leveraging Kubernetes namespaces and resources, it ensures isolated build environments, scaling agent capacity up during intensive test stages and scaling down to save compute budget.
### Gitops

#### Gitlab Integration

  - **(2024)** [==GitLab Kubernetes Agent==](https://docs.gitlab.com/user/clusters/agent) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A secure, bidirectional, and active cluster integration agent (now known as the GitLab Agent for Kubernetes) that enables enterprise GitOps workflows. Operating inside the target cluster, it pulls configurations from Git repositories, avoiding the security risk of exposing Kube-apiserver endpoints to external CI runners.
### Openshift

#### CLI Tools

  - **(2022)** [==openshift-client==](https://plugins.jenkins.io/openshift-client) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A vital Jenkins plugin that packages and injects the OpenShift CLI (oc) command tool directly into pipeline execution containers. It enables automation scripts to easily authenticate, query, and manipulate OpenShift namespaces, security context constraints (SCCs), and route resources.
#### Pipelines

  - **(2022)** [==openshift-pipeline==](https://plugins.jenkins.io/openshift-pipeline) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A key Jenkins integration designed to trigger and coordinate OpenShift source-to-image (S2I) and binary-to-image build pipelines directly from Jenkins stages. It bridges traditional centralized orchestration with OpenShift-native application delivery models. Modern workloads are increasingly migrating toward Tekton-based OpenShift Pipelines.
#### Synchronization

  - **(2022)** [==openshift-sync==](https://plugins.jenkins.io/openshift-sync) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized Jenkins plugin designed to continuously synchronize Jenkins Job states, configurations, and build logs directly with OpenShift’s Build configurations and pipelines. By unifying build states, it provides developers with a single dashboard experience within the native OpenShift console interface.
### Workflows

#### Hugging Face Jobs

  - **(2026)** [**Migrating Your GitHub CI to Hugging Face Jobs**](https://huggingface.co/blog/github-ci-hf-jobs) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[CICD]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GITHUB-ACTIONS]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--primary'>[MLOPS]</span> — **Curator Insight:** This infrastructure guide addresses the computational bottlenecks frequently encountered when running heavy machine learning tests in standard CI environments. **Live Grounding:** By modifying the `runs-on` directive and integrating a custom dispatcher, the tutorial shows how to seamlessly offload GitHub Actions workflows to Hugging Face Jobs. This allows CI/CD pipelines to leverage specialized GPU compute resources on-demand, significantly reducing test suite latency.
## Cloud Native

### Kubernetes

#### Architecture

##### AI Conformance

###### Sigs

  - **(2026)** [**From Working Group to SIG Architecture: spotlight on AI Conformance**](https://kubernetes.io/blog/2026/10/29/sig-arch-ai-conformance-2026) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[AI]</span> <span class='md-tag md-tag--primary'>[ARCHITECTURE]</span> <span class='md-tag md-tag--primary'>[CONFORMANCE]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[MLOPS]</span> — Explores the elevation of AI Conformance from a Working Group to SIG Architecture in Kubernetes. It establishes formal architectural standards and conformance tests for running AI/ML workloads efficiently across diverse clusters. Grounded analysis indicates this is a crucial step towards standardizing GPU/NPU orchestration and eliminating fragmentation in enterprise AI deployments.
#### Autonomous Operations

  - **(2026)** [**How NVIDIA Mission Control 2.5 Brings Autonomous Recovery to Kubernetes**](https://developer.nvidia.com/blog/how-nvidia-mission-control-2-5-brings-autonomous-recovery-to-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[AIOPS]</span> <span class='md-tag md-tag--primary'>[AUTONOMOUS-RECOVERY]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU-ORCHESTRATION]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[RESILIENCY]</span> — NVIDIA Mission Control 2.5 integrates sophisticated autonomous recovery mechanisms into Kubernetes environments orchestrating large-scale AI training clusters. The platform implements proactive monitoring and automated remediation strategies to handle transient hardware failures and GPU node degradation without human intervention. By embedding these resiliency patterns directly into the container orchestration layer, Mission Control significantly reduces downtime and protects the progression of expensive, multi-node AI training workloads.
#### Community

##### SIG Apps

###### Workload Apis

  - **(2026)** [**Spotlight on SIG Apps**](https://kubernetes.io/blog/2026/09/22/sig-apps-spotlight) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[ARCHITECTURE]</span> <span class='md-tag md-tag--primary'>[BATCH-PROCESSING]</span> <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> <span class='md-tag md-tag--primary'>[MLOPS]</span> <span class='md-tag md-tag--primary'>[STATEFULSETS]</span> <span class='md-tag md-tag--primary'>[WORKLOADS]</span> — Curator Insight identifies this update as a foundational blueprint for modern platform engineering, bridging the gap between legacy microservices and next-generation batch processing. Live Grounding confirms that SIG Apps actively focuses on adapting core primitives—such as StatefulSets, Jobs, and DaemonSets—to natively support complex AI workloads and dynamic scaling events without sacrificing infrastructure reliability.
* **Architectural Role**: Serves as the canonical standard for deploying, updating, and operating complex distributed applications across cloud-native environments.
* **Production Trade-offs**: Utilizing native controllers guarantees universal ecosystem compatibility, though highly specialized GenAI training pipelines may still necessitate custom CRDs or Kueue integration for advanced scheduling.
* **K8s Compatibility**: 100% native; these primitive APIs form the essential backbone of every conformant Kubernetes cluster.
##### Working Groups

###### Workload Conformance

  - **(2026)** [**Announcing the Workload Conformance Working Group**](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[CONFORMANCE]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[MULTI-CLOUD]</span> <span class='md-tag md-tag--primary'>[WORKLOADS]</span> — Introduces the new Workload Conformance Working Group aimed at standardizing how complex workloads operate across different Kubernetes distributions. By defining strict conformance baselines for custom resources and workload controllers, the initiative ensures portability and predictable behavior for enterprise applications. This addresses long-standing operational inconsistencies in multi-cloud and hybrid deployments.
#### Machine Learning Operations

  - **(2026)** [**Build a Validated Kubernetes Runtime for NVIDIA Dynamo**](https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU-OPERATOR]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[INFERENCE]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> — NVIDIA introduces the AI Cluster Runtime (AICR) to streamline the deployment of the Dynamo distributed inference framework on Kubernetes. By packaging GPU driver stacks, Dynamic Resource Allocation, and gang scheduling into reproducible pinned recipes, AICR ensures a validated environment for production AI workloads. This approach abstracts the complexities of cache-aware routing and simplifies model serving across distributed GPU clusters.
#### Nodes

##### Memory Management

###### Swap

  - **(2026)** [**Scaling Kubernetes Workloads with Node Swap**](https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[COST-OPTIMIZATION]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> <span class='md-tag md-tag--primary'>[MEMORY-MANAGEMENT]</span> <span class='md-tag md-tag--primary'>[SCHEDULING]</span> — Explores the stabilization of Node Swap support in Kubernetes, allowing workloads to leverage disk-based virtual memory to prevent sudden eviction during bursty memory spikes. The article contrasts legacy unswappable architecture with the modern kubelet swap mechanics, enabling safer overcommit ratios. This feature dramatically improves cluster cost-efficiency for non-latency-sensitive batch processing.
##### Resource Management

###### Cgroup V2

  - **(2026)** [**The Shift to cgroup v2 in Kubernetes: What You Need to Know**](https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[CGROUPS]</span> <span class='md-tag md-tag--primary'>[EBPF]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[LINUX]</span> <span class='md-tag md-tag--primary'>[PERFORMANCE]</span> <span class='md-tag md-tag--primary'>[RESOURCE-MANAGEMENT]</span> — Details the architectural transition to cgroup v2 as the default resource management subsystem in Linux and Kubernetes. The shift unlocks advanced memory QoS, unified hierarchical control, and eBPF-based accounting mechanisms. For platform engineers, understanding this migration is critical to preventing OOM kills and optimizing high-density container scheduling.
###### Pod-level Managers

  - **(2026)** [**Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta**](https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[HPC]</span> <span class='md-tag md-tag--primary'>[NUMA]</span> <span class='md-tag md-tag--primary'>[PERFORMANCE]</span> <span class='md-tag md-tag--primary'>[RESOURCE-MANAGEMENT]</span> — Analyzes the beta graduation of Pod-Level Resource Managers in Kubernetes v1.37, transitioning fine-grained hardware allocation from the node level to the pod specification. This enables precise NUMA topology awareness and CPU pinning directly tied to workload deployments rather than global kubelet configuration. It is a transformative capability for high-performance computing (HPC) and telco workloads requiring predictable microsecond latencies.
#### Resource Scheduling

  - **(2026)** [**Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4**](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU-SHARING]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[RESOURCE-MANAGEMENT]</span> — NVIDIA CUDA 13.4 introduces advanced memory-enforced GPU sharing in Kubernetes, leveraging the open-source GPU Fractioning Operator and KAI Scheduler to securely divide GPU capacity. This capability allows platform engineers to enforce strict per-workload memory limits, effectively preventing out-of-memory errors and noisy neighbor problems in multi-tenant clusters. The integration substantially improves hardware utilization by allowing multiple AI microservices to safely coexist on a single physical device.
### Kubernetes Orchestration

#### GPU Cluster Provisioning

  - **(2026)** [**AICR v1.0: Open, stable, and verifiable GPU cluster configuration**](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[INFRASTRUCTURE-AS-CODE]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[SBOM]</span> — NVIDIA's AI Cluster Runtime (AICR) v1.0 delivers a verified and reproducible configuration baseline for GPU-accelerated Kubernetes clusters. It addresses the complexity of maintaining compatible versions across host kernels, GPU drivers, API servers, and cluster agents for large-scale AI operations. By providing layered recipes with SLSA Level 3 provenance and signed SBOMs, it ensures high reliability for training and inference workloads on infrastructure like Amazon EKS with NVIDIA accelerators.
## Cloud Native and Orchestration

### Kubernetes Ecosystem

#### GPU Management

  - **(2026)** [**Validate GPU Cluster Readiness Before AI Workloads Land**](https://developer.nvidia.com/blog/validate-gpu-cluster-readiness-before-ai-workloads-land) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU-ORCHESTRATION]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[NVCRE]</span> — The NVIDIA Cluster Readiness Engine (NVCRE) transitions cluster validation from basic hardware pinging to comprehensive workload-driven testing prior to production deployment. Curator insight highlights its use of Certification, Workflow, and Job custom resources to pinpoint failures in topology-aware node groups, specifically isolating NCCL communication degradations. Live grounding shows this Kubernetes controller employs adaptive fault isolation to split failing groups, catching network stalls that pass standard telemetry checks before expensive multi-node training jobs are launched.
#### Node Management

  - **(2026)** [**Manage Kubernetes Node Fleets with NodeWright**](https://developer.nvidia.com/blog/manage-kubernetes-node-fleets-with-nodewright) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[FLEET-MANAGEMENT]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[NODEWRIGHT]</span> <span class='md-tag md-tag--primary'>[OS-LIFECYCLE]</span> — NodeWright extends Kubernetes declarative management down to the host OS level, providing a specialized package manager for GPU cluster environments. Curator insight reveals it handles complex dependencies like kernel settings, storage layouts, and security agents without relying on destructive node-recreation strategies. Live grounding confirms that its DeploymentPolicy resource enables safe, progressive rollouts (e.g., canary nodes) that respect long-running training jobs, PodDisruptionBudgets, and hardware scarcity in dense AI factories.
## Cloud Native Infrastructure

### Kubernetes Orchestration (1)

#### GPU Scheduling

  - **(2026)** [**NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform**](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[AI-INFRASTRUCTURE]</span> <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[SCHEDULING]</span> — NVIDIA has made the complete Run:ai platform available as open source software, expanding the DSX AI Factory Platform to provide production-grade AI workload and GPU orchestration capabilities. The release includes modular components such as the KAI Scheduler for GPU-aware Kubernetes scheduling, the GPU Fractioning Operator for CUDA-native GPU sharing, and KAI Resource Management. This move allows the broader ecosystem to independently adopt these components and accelerate the development of differentiated AI factory solutions.
## Compute Infrastructure

### GPU Acceleration

#### CUDA Framework

  - **(2026)** [**CUDA Toolkit 13.4 Adds Windows on Arm Support and Greater Control over Shared GPUs**](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[ARM]</span> <span class='md-tag md-tag--primary'>[CUDA]</span> <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[KUBERNETES]</span> <span class='md-tag md-tag--primary'>[MULTI-TENANT]</span> — This release overview details the critical features introduced in NVIDIA CUDA Toolkit 13.4, notably extending native development support to Windows on Arm architectures. Furthermore, the toolkit introduces advanced, memory-enforced GPU sharing controls, allowing precise resource allocation in multi-tenant environments like Kubernetes. By providing stricter isolation and granular memory management at the driver level, it prevents noisy-neighbor problems when partitioning hardware among disparate workloads. These foundational improvements enable developers to maximize hardware utilization while bridging the gap between mobile-class architecture and enterprise cloud orchestration.
## DevOps

### CICD (1)

#### Ai-assisted Automation

  - **(2026)** [**Shipping huggingface_hub every week with AI, open tools, and a human in the loop**](https://huggingface.co/blog/huggingface-hub-release-ci) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[AI-AGENTS]</span> <span class='md-tag md-tag--primary'>[AUTOMATION]</span> <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Hugging Face transformed its release cycle for the `huggingface_hub` Python client from a monthly cadence to a weekly rhythm by integrating AI into their GitHub Actions pipeline. By utilizing open-weights models to draft release notes and PR summaries, the team decoupled creative drafting from deterministic code validation while maintaining a critical human-in-the-loop checkpoint for final judgment. This architecture demonstrates how maintainers can construct cost-effective, agentic CI/CD workflows using entirely open-source infrastructure.
## Kubernetes Architecture

### Node Management (1)

#### Hardware Accelerators

  - **(2026)** [**Spotlight on WG Device Management**](https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--primary'>[AI-INFRASTRUCTURE]</span> <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--primary'>[DRA]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--primary'>[GPU]</span> <span class='md-tag md-tag--primary'>[HARDWARE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — This spotlight highlights the vital work of the Kubernetes WG Device Management in accommodating modern hardware like GPUs and TPUs for AI and telecommunications workloads. Grounded analysis indicates that the graduation of Dynamic Resource Allocation (DRA) to General Availability marks a fundamental shift, moving beyond legacy device plugins to highly programmable hardware scheduling. This evolution is architecturally critical for platform teams managing hardware-intensive edge and machine learning clusters.
## Kubernetes Job Scheduling

  - **(2026)** [How Netflix Simplified Batch Compute with Kueue](https://netflixtechblog.com/how-netflix-simplified-batch-compute-with-kueue-87860682629c?gi=b7df13ef57ad&source=rss----2615bd06b42e---4) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--primary'>[MLOPS]</span> — Technical documentation and implementation reference for How Netflix Simplified Batch Compute with Kueue covering Kubernetes Job Scheduling in CI/CD Kubernetes Plugins (netflixtechblog.com).

---
💡 **Explore Related:** [CI/CD](./cicd.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Jenkins](./jenkins.md)

🔗 **See Also:** [Stackstorm](./stackstorm.md) | [Private Cloud Solutions](./private-cloud-solutions.md)

