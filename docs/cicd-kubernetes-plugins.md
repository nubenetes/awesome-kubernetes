# CI/CD Kubernetes Plugins

1. [Jenkins Kubernetes Plugins](#jenkins-kubernetes-plugins)
2. [Jenkins OpenShift Plugins](#jenkins-openshift-plugins)
3. [Argo CD Config Management Plugins](#argo-cd-config-management-plugins)
4. [GitLab Kubernetes Agent](#gitlab-kubernetes-agent)

## Jenkins Kubernetes Plugins

- [Jenkins Kubernetes Plugin](https://plugins.jenkins.io/kubernetes)
- [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd)

## Jenkins OpenShift Plugins

- [openshift-pipeline](https://plugins.jenkins.io/openshift-pipeline)
- [openshift-sync](https://plugins.jenkins.io/openshift-sync)
- [openshift-client](https://plugins.jenkins.io/openshift-client)

## Argo CD Config Management Plugins

## GitLab Kubernetes Agent

- [GitLab Kubernetes Agent](https://docs.gitlab.com/user/clusters/agent)

## Kubernetes Job Scheduling
  - **(2026)** [How Netflix Simplified Batch Compute with Kueue](https://netflixtechblog.com/how-netflix-simplified-batch-compute-with-kueue-87860682629c?gi=b7df13ef57ad&source=rss----2615bd06b42e---4) 🌟 - Netflix details its architectural migration from their proprietary Compute Managed Batch system to Kueue, a native Kubernetes queuing and job scheduling controller.
  - **(2026)** [How Netflix Simplified Batch Compute with Kueue](https://netflixtechblog.com/how-netflix-simplified-batch-compute-with-kueue-87860682629c?source=rss----2615bd06b42e---4) 🌟 - Netflix details its transition to a more Kubernetes-native compute infrastructure by migrating millions of batch jobs to Kueue.

  - **(2026)** [From Working Group to SIG Architecture: spotlight on AI Conformance](https://kubernetes.io/blog/2026/10/29/sig-arch-ai-conformance-2026) 🌟 - In this post, we explore the elevation of AI Conformance to a SIG Architecture focus, standardizing AI workloads across Kubernetes environments.

  - **(2026)** [Announcing the Workload Conformance Working Group](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg) 🌟 - We are excited to announce the new Workload Conformance Working Group aimed at standardizing enterprise workload behavior.

  - **(2026)** [The Shift to cgroup v2 in Kubernetes: What You Need to Know](https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift) 🌟 - In Linux, cgroups are a kernel feature used for managing system resources. Kubernetes uses cgroup v2 to unlock advanced memory and CPU controls.

  - **(2026)** [Scaling Kubernetes Workloads with Node Swap](https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap) 🌟 - Memory is often the first hard limit a Kubernetes cluster hits. Learn how Node Swap helps safely overcommit cluster memory.

  - **(2026)** [Spotlight on SIG Apps](https://kubernetes.io/blog/2026/09/22/sig-apps-spotlight) 🌟 - As Kubernetes adoption has grown, the conversation has shifted. Here is a spotlight on the latest developments from SIG Apps.

  - **(2026)** [Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta](https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta) 🌟 - With the release of Kubernetes v1.37, the Pod-Level Resource Managers feature has graduated to Beta status.

  - **(2026)** [Spotlight on WG Device Management](https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026) 🌟 - An in-depth look at the Working Group for Device Management, detailing the shift to Dynamic Resource Allocation (DRA) for specialized edge and AI hardware.

  - **(2026)** [Shipping huggingface_hub every week with AI, open tools, and a human in the loop](https://huggingface.co/blog/huggingface-hub-release-ci) 🌟 - How huggingface_hub shifted to a weekly release cycle using AI-assisted GitHub Actions and open-source models.

  - **(2026)** [Migrating Your GitHub CI to Hugging Face Jobs](https://huggingface.co/blog/github-ci-hf-jobs) 🌟 - A step-by-step guide to migrating GitHub CI workflows to leverage Hugging Face Jobs compute.

  - **(2026)** [Build a Validated Kubernetes Runtime for NVIDIA Dynamo](https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo) 🌟 - A technical guide on using the NVIDIA AI Cluster Runtime (AICR) to deploy the Dynamo distributed inference framework on Kubernetes.
  - **(2026)** [Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4) 🌟 - A guide on using the GPU Fractioning Operator and KAI Scheduler to securely divide and share GPU resources with memory enforcement in Kubernetes.

  - **(2026)** [How NVIDIA Mission Control 2.5 Brings Autonomous Recovery to Kubernetes](https://developer.nvidia.com/blog/how-nvidia-mission-control-2-5-brings-autonomous-recovery-to-kubernetes) 🌟 - Explores how NVIDIA Mission Control automates fault remediation and resilient cluster recovery for massive-scale AI training workloads deployed natively on Kubernetes.
  - **(2026)** [NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform) 🌟 - NVIDIA releases the Run:ai platform as open source, expanding the DSX AI Factory Platform with robust GPU and Kubernetes orchestration tools.

  - **(2026)** [AICR v1.0: Open, stable, and verifiable GPU cluster configuration](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration) 🌟 - NVIDIA's AI Cluster Runtime (AICR) v1.0 delivers a verified and reproducible configuration baseline for GPU-accelerated Kubernetes clusters.

  - **(2026)** [Validate GPU Cluster Readiness Before AI Workloads Land](https://developer.nvidia.com/blog/validate-gpu-cluster-readiness-before-ai-workloads-land) 🌟 - NVIDIA Cluster Readiness Engine (NVCRE) is an open-source Kubernetes controller that validates GPU cluster health using real distributed workloads.

  - **(2026)** [Manage Kubernetes Node Fleets with NodeWright](https://developer.nvidia.com/blog/manage-kubernetes-node-fleets-with-nodewright) 🌟 - NodeWright is an open-source Kubernetes-native package manager for declarative configuration and safe updating of host operating systems on GPU fleets.

  - **(2026)** [CUDA Toolkit 13.4 Adds Windows on Arm Support and Greater Control over Shared GPUs](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus) 🌟 - Highlights the release of CUDA Toolkit 13.4, featuring native Windows on Arm compatibility and memory-enforced GPU sharing mechanisms for Kubernetes environments.

  - **(2014)** [Kubernetes](https://github.com/kubernetes/kubernetes) 🌟 - Production-Grade Container Scheduling and Management.
