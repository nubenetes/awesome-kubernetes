---
description: "Top OCP 5 resources for 2026, AI-ranked: kubevirt, OKD Official Blog and more — curated Cloud Native tools, guides and references."
---
# OCP 5

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ocp5/).

!!! info "Architectural Context"
    Detailed reference for OCP 5 in the context of The Container Stack.

!!! abstract "Deep-Dive Topic Pages"
    [OpenShift Overview](./openshift/) · [OCP 4](./ocp4/) · [OpenShift Pipelines](./openshift-pipelines/) · [OpenShift AI (RHOAI)](./enterprise-ai-platforms/) · [AI Agents & MCP](./ai-agents-mcp/)


## Generational Shift: OCP 4 vs OCP 5 (2026)

!!! info "Red Hat OpenShift Container Platform 5 (OCP 5)"
    Announced and generally available in November 2026, **Red Hat OpenShift 5** converges containers, virtual machines, and enterprise AI workloads on **Kubernetes 1.36**, **CRI-O 1.36**, and **RHCOS 10 (RHEL 10.2)** while offering direct in-place upgrades from **OpenShift 4.22**.

| Architectural Dimension | OpenShift 4 (OCP 4.x) | OpenShift 5 (OCP 5.0+) |
| :--- | :--- | :--- |
| **Kubernetes and Runtime** | Kubernetes 1.13–1.35 / CRI-O 1.x | **Kubernetes 1.36** and **CRI-O 1.36** |
| **Node Operating System** | RHCOS 8 / RHCOS 9 | **RHCOS 10 (RHEL 10.2 base)** with RHCOS 9/10 cluster coexistence |
| **Cluster Operations** | Conversational assistant (OLS Q&A) | **Agentic OpenShift Lightspeed** (supervised triage, remediation, native MCP server and gateway) |
| **Security Baseline** | FIPS 140-2/3, TLS 1.3, SCCs | **Post-Quantum Cryptography (PQC)** control plane, SBOM transparency, sovereign multi-tenancy |
| **Operator Management** | OLM v0 (Subscriptions, InstallPlans) | **Operator Lifecycle Manager v1 (OLM v1)** with `ClusterExtension` APIs and standard K8s RBAC |
| **Support Lifecycle** | 18 months standard (EUS up to 3 years) | **24 months standard** (12 full + 12 maintenance) and up to **5 years Extended Lifecycle Support (ELC)** |
| **Virtualization** | OpenShift Virtualization 4 (KubeVirt) | **OpenShift Virtualization 5** (Autopilot Day-1 baseline, VM templates, Hyper-V direct migration) |
| **Cloud Control Planes** | Standalone masters and optional HCP | **Hosted Control Planes (HyperShift)** as the default standard for ROSA and ARO |
| **Observability UI** | Static Console Dashboards | Native **Perses** dashboards with natural-language generation via Lightspeed |

## Enterprise Kubernetes

### Multi-cluster Management

#### Hosted Control Planes

  - **(2022)** [==github.com/openshift/hypershift: HyperShift==](https://github.com/openshift/hypershift) <span class='md-tag md-tag--info'>⭐ 526</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-55890bf2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 2 L 20 5 L 30 13 L 40 7 L 50 2" fill="none" stroke="url(#spark-grad-55890bf2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — HyperShift decouples the OpenShift control plane from the infrastructure, hosting it as standard containerized workloads within a central management cluster. This architecture enables lightning-fast provisioning, significantly lower operational overhead, and highly cost-effective multi-tenant fleet management.
## Hosted Control Planes Managed Cloud Services And Edge

  - **(2026)** [How Red Hat OpenShift 5 Transforms ROSA Operations on AWS](https://www.redhat.com/en/blog/how-red-hat-openshift-5-transforms-red-hat-openshift-service-aws-operations) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Architectural breakdown of Red Hat OpenShift Service on AWS (ROSA) on OCP 5 with Hosted Control Planes (HCP) as the default cloud topology for faster provisioning and reduced control-plane cost.
  - **(2026)** [Red Hat OpenShift 5 Now Available on Azure Red Hat OpenShift (ARO)](https://www.redhat.com/en/blog/red-hat-openshift-5-now-available-azure-red-hat-openshift) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Announcement and architectural overview of OpenShift 5 on Microsoft Azure Red Hat OpenShift (ARO), integrating Hosted Control Planes, enterprise Azure networking, and unified managed lifecycle operations.
  - **(2026)** [GitHub: openshift/rosa](https://github.com/openshift/rosa) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official CLI for provisioning, upgrading, and managing Red Hat OpenShift Service on AWS (ROSA) clusters with Hosted Control Planes.
  - **(2026)** [GitHub: openshift/microshift](https://github.com/openshift/microshift) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Lightweight, single-node edge distribution derived from OpenShift 5 and RHEL 10 designed for resource-constrained far-edge, industrial, and telco deployments.
## Intelligent And Agentic Operations With Openshift Lightspeed And MCP

  - **(2026)** [Red Hat OpenShift Lightspeed Developer Hub](https://developers.redhat.com/products/openshift/lightspeed) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official hub for OpenShift Lightspeed, which evolves in OCP 5 into an active agentic operations platform with supervised alert triage, root-cause diagnostics, natural-language VM management, and Bring Your Own Knowledge (BYOK).
  - **(2026)** [GitHub: openshift/lightspeed-service](https://github.com/openshift/lightspeed-service) 🌟🌟🌟 <span class='md-tag md-tag--primary'>[CLOUD-AI]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> — Core open-source backend service powering OpenShift Lightspeed (OLS), integrating cluster context and RAG documentation with OpenAI, Azure OpenAI, IBM watsonx, RHEL AI, and Red Hat OpenShift AI.
  - **(2026)** [GitHub: openshift/lightspeed-operator](https://github.com/openshift/lightspeed-operator) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Kubernetes operator managing the deployment, configuration, and lifecycle of OpenShift Lightspeed components natively on OpenShift clusters.
  - **(2026)** [GitHub: openshift/lightspeed-agentic-operator](https://github.com/openshift/lightspeed-agentic-operator) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Open-source operator enabling supervised agentic workflows, automated incident investigations, and human-in-the-loop remediation proposals in OpenShift 5.
  - **(2026)** [GitHub: containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[MCP]</span> — High-velocity Model Context Protocol (MCP) server for Kubernetes and Red Hat OpenShift, allowing AI agents and coding assistants to securely inspect pods, logs, KubeVirt VMs, and cluster APIs.
  - **(2026)** [GitHub: Kuadrant/kuadrant-operator (Red Hat Connectivity Link)](https://github.com/Kuadrant/kuadrant-operator) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[MCP]</span> — Upstream Kubernetes-native connectivity, Gateway API policy, and MCP gateway operator powering Red Hat Connectivity Link for zero-trust AI agent and ingress governance on OpenShift 5.
## OKD 5 Community Distribution

  - **(2026)** [GitHub: okd-project/okd-scos (OKD 5 on CentOS Stream CoreOS)](https://github.com/okd-project/okd-scos) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Upstream CentOS Stream CoreOS (SCOS) build and release repository powering OKD 5, aligning community OpenShift releases with Kubernetes 1.36, RHEL 10 lineage, and OLM v1.
  - **(2026)** [OKD Official Blog](https://okd.io/blog) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official OKD working group announcements covering OKD 5 milestones, Stream CoreOS transitions, community operator updates, and architectural deep dives.
## Observability And Native Perses Dashboards

  - **(2026)** [Guide to Observability in Red Hat OpenShift 5](https://www.redhat.com/en/blog/guide-observability-red-hat-openshift-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official technical guide to OpenShift 5 observability covering OpenTelemetry pipelines, Cluster Observability Operator, Perses native dashboards, and Lightspeed-assisted alert correlation.
  - **(2026)** [GitHub: perses/perses](https://github.com/perses/perses) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — CNCF Sandbox open-source dashboarding and visualization engine integrated natively into OpenShift 5 for declarative GitOps-friendly metrics dashboards and AI-generated incident views.
## Official Documentation Release Notes And Lifecycle

  - **(2026)** [OpenShift Container Platform 5.0 Official Documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/5.0) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Complete official Red Hat documentation library for OCP 5.0 spanning installation, in-place upgrades from 4.22, OVN-Kubernetes networking, storage, security, virtualization, and AI workloads.
  - **(2026)** [OpenShift Container Platform 5.0 Release Notes](https://docs.redhat.com/en/documentation/openshift_container_platform/5.0/html/release_notes/ocp-5-0-release-notes) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Authoritative OCP 5.0 release notes documenting Kubernetes 1.36 and CRI-O 1.36 updates, RHCOS 10 (RHEL 10.2) baseline, OLM v1 changes, `oc-mirror` v2 transition, deprecations, and known issues.
  - **(2026)** [Red Hat OpenShift 5 Predictable Lifecycles and Extended Support](https://www.redhat.com/en/technologies/cloud-computing/openshift-5/predictable) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Overview of OpenShift 5's 24-month standard support lifecycle, up to 5-year Extended Lifecycle Support (ELC) cadence (starting with OCP 5.2), and pre-flight upgrade planning.
  - **(2026)** [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official Red Hat support matrix detailing Full Support, Maintenance Support, Extended Update Support (EUS), and Extended Lifecycle Support (ELC) windows across OCP 4.x and OCP 5.x releases.
## Openshift Container Platform 5 Overview

  - **(2026)** [Red Hat OpenShift 5 Product Overview](https://www.redhat.com/en/technologies/cloud-computing/openshift-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official Red Hat product portal for OpenShift 5 covering agentic operations, zero-trust post-quantum security, unified container/VM/AI workloads, and predictable multi-year lifecycles.
  - **(2026)** [Announcing Red Hat OpenShift 5](https://www.redhat.com/en/blog/announcing-red-hat-openshift-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official Red Hat engineering launch blog detailing the core architectural pillars of OCP 5.0, including Kubernetes 1.36, agentic Lightspeed workflows, OLM v1, RHCOS 10, and streamlined upgrades from OCP 4.22.
  - **(2026)** [Red Hat Press Release: OpenShift 5 Transforms Hybrid Cloud Operations with Real-Time Intelligence and Zero Trust Security](https://www.redhat.com/en/about/press-releases/red-hat-openshift-5-transforms-hybrid-cloud-operations-real-time-intelligence-and-zero-trust-security) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official launch announcement from KubeCon + CloudNativeCon highlighting post-quantum cryptography readiness, sovereign cloud multi-tenancy, and AI-assisted operational resilience.
  - **(2026)** [Red Hat OpenShift 5 for Developers](https://developers.redhat.com/articles/2026/11/09/red-hat-openshift-5-for-developers) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--primary'>[MCP]</span> — Technical developer overview examining what is new in OCP 5.0 for application engineers, including MCP tool integration, local sandboxes, secure software supply chains, and Red Hat Developer Hub workflows.
## Openshift Virtualization 5 And Unified Workloads

  - **(2026)** [What is New in Red Hat OpenShift Virtualization 5](https://www.redhat.com/en/blog/unlocking-next-generation-workloads-whats-new-red-hat-openshift-virtualization-5) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official Red Hat deep dive into OpenShift Virtualization 5, introducing Virtualization Autopilot Day-1 baselines, native VM templates, natural-language VM provisioning via Lightspeed, and direct migration from Microsoft Hyper-V.
## Operator Lifecycle Manager V1 And Disconnected Operations

  - **(2026)** [GitHub: operator-framework/operator-controller (OLM v1)](https://github.com/operator-framework/operator-controller) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Core controller of Operator Lifecycle Manager v1 (OLM v1) adopted in OpenShift 5, introducing declarative `ClusterExtension` APIs, simplified dependency resolution, and standard Kubernetes RBAC scoping.
  - **(2026)** [GitHub: openshift/oc-mirror](https://github.com/openshift/oc-mirror) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official OpenShift CLI plugin (`oc-mirror` v2) for mirroring OCP 5 release payloads, OLM operator catalogs, Helm charts, and container images into air-gapped and disconnected enterprise registries.
## Virtualization

### VM Orchestration

#### Hyperconverged Infrastructure

  - **(2026)** [**kubevirt**](https://github.com/kubevirt/kubevirt) <span class='md-tag md-tag--info'>⭐ 7166</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0e333d98" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 9 L 20 9 L 30 9 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-0e333d98)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — KubeVirt is a graduated CNCF project that allows virtual machines to run natively alongside standard container workloads on Kubernetes. By utilizing KVM virtualization inside Pods, it helps enterprises transition legacy virtual machine applications to modern cloud-native platforms. It has become the de facto standard for hyperconverged infrastructure setups, allowing unified management of containers and VMs.
## Zero Trust Security Post-quantum Cryptography And Digital Sovereignty

  - **(2026)** [Post-Quantum Cryptography in Red Hat Enterprise Linux 10](https://www.redhat.com/en/blog/post-quantum-cryptography-red-hat-enterprise-linux-10) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Deep dive into the RHEL 10 / RHCOS 10 cryptographic foundation underpinning OpenShift 5's control-plane post-quantum cryptography (PQC) support and NIST ML-KEM/ML-DSA readiness.
  - **(2026)** [Red Hat Post-Quantum Cryptography Architecture](https://www.redhat.com/en/topics/security/post-quantum-cryptography) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Architectural primer on defending long-lived hybrid cloud platforms against harvest-now-decrypt-later threats with quantum-resistant TLS, crypto-agility, and sovereign key policies.
  - **(2026)** [GitHub: ComplianceAsCode/compliance-operator](https://github.com/ComplianceAsCode/compliance-operator) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — Official OpenShift Compliance Operator allowing platform teams to define security and regulatory profiles once (CIS, PCI-DSS, NIST, FedRAMP) and enforce them uniformly across hybrid OCP 5 fleets.
  - **(2026)** [GitHub: openshift/cert-manager-operator](https://github.com/openshift/cert-manager-operator) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — OpenShift cert-manager Operator for automated zero-trust X.509 certificate issuance, rotation, and lifecycle management across ingress, workloads, and control-plane endpoints.

---
💡 **Explore Related:** [Serverless](./serverless.md) | [Kubernetes Storage](./kubernetes-storage.md) | [Noops](./noops.md)

🔗 **See Also:** [AWS Pricing](./aws-pricing.md) | [AWS](./aws.md)

