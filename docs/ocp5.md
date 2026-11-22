# OCP 5

Curated architectural reference and resource hub for **Red Hat OpenShift Container Platform 5 (OCP 5)** — built on **Kubernetes 1.36**, **CRI-O 1.36**, and **Red Hat Enterprise Linux CoreOS 10 (RHCOS 10 / RHEL 10.2)**, introducing agentic cluster operations with **OpenShift Lightspeed and MCP**, **Post-Quantum Cryptography (PQC)**, **Operator Lifecycle Manager v1 (OLM v1)**, **OpenShift Virtualization 5**, **Hosted Control Planes (HyperShift)**, and up to **5-year Extended Lifecycle Support (ELC)**.

1. [OpenShift Container Platform 5 Overview](#openshift-container-platform-5-overview)
2. [Official Documentation, Release Notes and Lifecycle](#official-documentation-release-notes-and-lifecycle)
3. [Intelligent and Agentic Operations with OpenShift Lightspeed and MCP](#intelligent-and-agentic-operations-with-openshift-lightspeed-and-mcp)
4. [Zero Trust Security, Post-Quantum Cryptography and Digital Sovereignty](#zero-trust-security-post-quantum-cryptography-and-digital-sovereignty)
5. [Operator Lifecycle Manager v1 and Disconnected Operations](#operator-lifecycle-manager-v1-and-disconnected-operations)
6. [OpenShift Virtualization 5 and Unified Workloads](#openshift-virtualization-5-and-unified-workloads)
7. [Hosted Control Planes, Managed Cloud Services and Edge](#hosted-control-planes-managed-cloud-services-and-edge)
8. [Observability and Native Perses Dashboards](#observability-and-native-perses-dashboards)
9. [OKD 5 Community Distribution](#okd-5-community-distribution)

## OpenShift Container Platform 5 Overview

!!! info "Generational Shift: OCP 4 vs OCP 5 (2026)"
    Announced and generally available in November 2026, **Red Hat OpenShift 5** converges containers, virtual machines, and enterprise AI workloads on a single hardened hybrid cloud platform while delivering a direct in-place upgrade path from **OpenShift 4.22**.

| Architectural Dimension | OpenShift 4 (OCP 4.x) | OpenShift 5 (OCP 5.0+) |
| :--- | :--- | :--- |
| **Kubernetes and Runtime** | Kubernetes 1.13–1.35 / CRI-O 1.x | **Kubernetes 1.36** and **CRI-O 1.36** |
| **Node Operating System** | RHCOS 8 / RHCOS 9 | **RHCOS 10 (RHEL 10.2 base)** with RHCOS 9/10 cluster coexistence during migration |
| **Cluster Operations** | Conversational assistant (OLS Q&A) | **Agentic OpenShift Lightspeed** (supervised triage, remediation, native MCP server and gateway) |
| **Security Baseline** | FIPS 140-2/3, TLS 1.3, SCCs | **Post-Quantum Cryptography (PQC)** for control plane communications, SBOM transparency, sovereign multi-tenancy |
| **Operator Management** | OLM v0 (Subscriptions, InstallPlans) | **Operator Lifecycle Manager v1 (OLM v1)** with `ClusterExtension` APIs and standard Kubernetes RBAC |
| **Support Lifecycle** | 18 months standard (EUS up to 3 years) | **24 months standard** (12 full + 12 maintenance) and up to **5 years Extended Lifecycle Support (ELC)** |
| **Virtualization** | OpenShift Virtualization 4 (KubeVirt) | **OpenShift Virtualization 5** (Autopilot Day-1 baseline, native VM templates, Hyper-V direct migration) |
| **Cloud Control Planes** | Standalone masters and optional HCP | **Hosted Control Planes (HyperShift)** as the default standard for ROSA and ARO |
| **Observability UI** | Static Console Dashboards | Native **Perses** dashboards with natural-language generation via Lightspeed |

- **(2026)** [Red Hat OpenShift 5 Product Overview](https://www.redhat.com/en/technologies/cloud-computing/openshift-5) 🌟 - Official Red Hat product portal for OpenShift 5 covering agentic operations, zero-trust post-quantum security, unified container/VM/AI workloads, and predictable multi-year lifecycles.
- **(2026)** [Announcing Red Hat OpenShift 5](https://www.redhat.com/en/blog/announcing-red-hat-openshift-5) 🌟 - Official Red Hat engineering launch blog detailing the core architectural pillars of OCP 5.0, including Kubernetes 1.36, agentic Lightspeed workflows, OLM v1, RHCOS 10, and streamlined upgrades from OCP 4.22.
- **(2026)** [Red Hat Press Release: OpenShift 5 Transforms Hybrid Cloud Operations with Real-Time Intelligence and Zero Trust Security](https://www.redhat.com/en/about/press-releases/red-hat-openshift-5-transforms-hybrid-cloud-operations-real-time-intelligence-and-zero-trust-security) 🌟 - Official launch announcement from KubeCon + CloudNativeCon highlighting post-quantum cryptography readiness, sovereign cloud multi-tenancy, and AI-assisted operational resilience.
- **(2026)** [Red Hat OpenShift 5 for Developers](https://developers.redhat.com/articles/2026/11/09/red-hat-openshift-5-for-developers) 🌟 - Technical developer overview examining what is new in OCP 5.0 for application engineers, including MCP tool integration, local sandboxes, secure software supply chains, and Red Hat Developer Hub workflows.

## Official Documentation, Release Notes and Lifecycle

- **(2026)** [OpenShift Container Platform 5.0 Official Documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/5.0) 🌟 - Complete official Red Hat documentation library for OCP 5.0 spanning installation, in-place upgrades from 4.22, OVN-Kubernetes networking, storage, security, virtualization, and AI workloads.
- **(2026)** [OpenShift Container Platform 5.0 Release Notes](https://docs.redhat.com/en/documentation/openshift_container_platform/5.0/html/release_notes/ocp-5-0-release-notes) 🌟 - Authoritative OCP 5.0 release notes documenting Kubernetes 1.36 and CRI-O 1.36 updates, RHCOS 10 (RHEL 10.2) baseline, OLM v1 changes, `oc-mirror` v2 transition, deprecations, and known issues.
- **(2026)** [Red Hat OpenShift 5 Predictable Lifecycles and Extended Support](https://www.redhat.com/en/technologies/cloud-computing/openshift-5/predictable) 🌟 - Overview of OpenShift 5's 24-month standard support lifecycle, up to 5-year Extended Lifecycle Support (ELC) cadence (starting with OCP 5.2), and pre-flight upgrade planning.
- **(2026)** [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift) 🌟 - Official Red Hat support matrix detailing Full Support, Maintenance Support, Extended Update Support (EUS), and Extended Lifecycle Support (ELC) windows across OCP 4.x and OCP 5.x releases.

## Intelligent and Agentic Operations with OpenShift Lightspeed and MCP

- **(2026)** [Red Hat OpenShift Lightspeed Developer Hub](https://developers.redhat.com/products/openshift/lightspeed) 🌟 - Official hub for OpenShift Lightspeed, which evolves in OCP 5 into an active agentic operations platform with supervised alert triage, root-cause diagnostics, natural-language VM management, and Bring Your Own Knowledge (BYOK).
- **(2026)** [GitHub: openshift/lightspeed-service](https://github.com/openshift/lightspeed-service) 🌟 - Core open-source backend service powering OpenShift Lightspeed (OLS), integrating cluster context and RAG documentation with OpenAI, Azure OpenAI, IBM watsonx, RHEL AI, and Red Hat OpenShift AI.
- **(2026)** [GitHub: openshift/lightspeed-operator](https://github.com/openshift/lightspeed-operator) 🌟 - Kubernetes operator managing the deployment, configuration, and lifecycle of OpenShift Lightspeed components natively on OpenShift clusters.
- **(2026)** [GitHub: openshift/lightspeed-agentic-operator](https://github.com/openshift/lightspeed-agentic-operator) 🌟 - Open-source operator enabling supervised agentic workflows, automated incident investigations, and human-in-the-loop remediation proposals in OpenShift 5.
- **(2026)** [GitHub: containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) 🌟 - High-velocity Model Context Protocol (MCP) server for Kubernetes and Red Hat OpenShift, allowing AI agents and coding assistants to securely inspect pods, logs, KubeVirt VMs, and cluster APIs.
- **(2026)** [GitHub: Kuadrant/kuadrant-operator (Red Hat Connectivity Link)](https://github.com/Kuadrant/kuadrant-operator) 🌟 - Upstream Kubernetes-native connectivity, Gateway API policy, and MCP gateway operator powering Red Hat Connectivity Link for zero-trust AI agent and ingress governance on OpenShift 5.

## Zero Trust Security, Post-Quantum Cryptography and Digital Sovereignty

- **(2026)** [Post-Quantum Cryptography in Red Hat Enterprise Linux 10](https://www.redhat.com/en/blog/post-quantum-cryptography-red-hat-enterprise-linux-10) 🌟 - Deep dive into the RHEL 10 / RHCOS 10 cryptographic foundation underpinning OpenShift 5's control-plane post-quantum cryptography (PQC) support and NIST ML-KEM/ML-DSA readiness.
- **(2026)** [Red Hat Post-Quantum Cryptography Architecture](https://www.redhat.com/en/topics/security/post-quantum-cryptography) 🌟 - Architectural primer on defending long-lived hybrid cloud platforms against harvest-now-decrypt-later threats with quantum-resistant TLS, crypto-agility, and sovereign key policies.
- **(2026)** [GitHub: ComplianceAsCode/compliance-operator](https://github.com/ComplianceAsCode/compliance-operator) 🌟 - Official OpenShift Compliance Operator allowing platform teams to define security and regulatory profiles once (CIS, PCI-DSS, NIST, FedRAMP) and enforce them uniformly across hybrid OCP 5 fleets.
- **(2026)** [GitHub: openshift/cert-manager-operator](https://github.com/openshift/cert-manager-operator) 🌟 - OpenShift cert-manager Operator for automated zero-trust X.509 certificate issuance, rotation, and lifecycle management across ingress, workloads, and control-plane endpoints.

## Operator Lifecycle Manager v1 and Disconnected Operations

- **(2026)** [GitHub: operator-framework/operator-controller (OLM v1)](https://github.com/operator-framework/operator-controller) 🌟 - Core controller of Operator Lifecycle Manager v1 (OLM v1) adopted in OpenShift 5, introducing declarative `ClusterExtension` APIs, simplified dependency resolution, and standard Kubernetes RBAC scoping.
- **(2026)** [GitHub: openshift/oc-mirror](https://github.com/openshift/oc-mirror) 🌟 - Official OpenShift CLI plugin (`oc-mirror` v2) for mirroring OCP 5 release payloads, OLM operator catalogs, Helm charts, and container images into air-gapped and disconnected enterprise registries.

## OpenShift Virtualization 5 and Unified Workloads

- **(2026)** [What is New in Red Hat OpenShift Virtualization 5](https://www.redhat.com/en/blog/unlocking-next-generation-workloads-whats-new-red-hat-openshift-virtualization-5) 🌟 - Official Red Hat deep dive into OpenShift Virtualization 5, introducing Virtualization Autopilot Day-1 baselines, native VM templates, natural-language VM provisioning via Lightspeed, and direct migration from Microsoft Hyper-V.
- **(2026)** [GitHub: kubevirt/kubevirt](https://github.com/kubevirt/kubevirt) 🌟 - Upstream CNCF virtualization engine powering OpenShift Virtualization 5, enabling side-by-side orchestration of enterprise virtual machines and containers on a single Kubernetes control plane.

## Hosted Control Planes, Managed Cloud Services and Edge

- **(2026)** [How Red Hat OpenShift 5 Transforms ROSA Operations on AWS](https://www.redhat.com/en/blog/how-red-hat-openshift-5-transforms-red-hat-openshift-service-aws-operations) 🌟 - Architectural breakdown of Red Hat OpenShift Service on AWS (ROSA) on OCP 5 with Hosted Control Planes (HCP) as the default cloud topology for faster provisioning and reduced control-plane cost.
- **(2026)** [Red Hat OpenShift 5 Now Available on Azure Red Hat OpenShift (ARO)](https://www.redhat.com/en/blog/red-hat-openshift-5-now-available-azure-red-hat-openshift) 🌟 - Announcement and architectural overview of OpenShift 5 on Microsoft Azure Red Hat OpenShift (ARO), integrating Hosted Control Planes, enterprise Azure networking, and unified managed lifecycle operations.
- **(2026)** [GitHub: openshift/hypershift](https://github.com/openshift/hypershift) 🌟 - Core Hosted Control Planes (HCP) middleware for OpenShift 5 that decouples Kubernetes control planes from worker nodes and runs them as dense, isolated pods on a management cluster.
- **(2026)** [GitHub: openshift/rosa](https://github.com/openshift/rosa) 🌟 - Official CLI for provisioning, upgrading, and managing Red Hat OpenShift Service on AWS (ROSA) clusters with Hosted Control Planes.
- **(2026)** [GitHub: openshift/microshift](https://github.com/openshift/microshift) 🌟 - Lightweight, single-node edge distribution derived from OpenShift 5 and RHEL 10 designed for resource-constrained far-edge, industrial, and telco deployments.

## Observability and Native Perses Dashboards

- **(2026)** [Guide to Observability in Red Hat OpenShift 5](https://www.redhat.com/en/blog/guide-observability-red-hat-openshift-5) 🌟 - Official technical guide to OpenShift 5 observability covering OpenTelemetry pipelines, Cluster Observability Operator, Perses native dashboards, and Lightspeed-assisted alert correlation.
- **(2026)** [GitHub: perses/perses](https://github.com/perses/perses) 🌟 - CNCF Sandbox open-source dashboarding and visualization engine integrated natively into OpenShift 5 for declarative GitOps-friendly metrics dashboards and AI-generated incident views.

## OKD 5 Community Distribution

- **(2026)** [GitHub: okd-project/okd-scos (OKD 5 on CentOS Stream CoreOS)](https://github.com/okd-project/okd-scos) 🌟 - Upstream CentOS Stream CoreOS (SCOS) build and release repository powering OKD 5, aligning community OpenShift releases with Kubernetes 1.36, RHEL 10 lineage, and OLM v1.
- **(2026)** [OKD Official Blog](https://okd.io/blog/) 🌟 - Official OKD working group announcements covering OKD 5 milestones, Stream CoreOS transitions, community operator updates, and architectural deep dives.
- **(2026)** [GitHub: okd-project/okd (OKD 5)](https://github.com/okd-project/okd) 🌟 - Official upstream community distribution of Kubernetes powering Red Hat OpenShift 5, tracking Kubernetes 1.36, CentOS Stream CoreOS (SCOS) / Fedora CoreOS foundations, and OLM v1 releases.

---
*See also: [Red Hat OpenShift](openshift.md), [OCP 4](ocp4.md), [OpenShift Pipelines](openshift-pipelines.md), [Enterprise AI Platforms and OpenShift AI (RHOAI)](enterprise-ai-platforms.md), and [Model Context Protocol (MCP) and AI Agents](ai-agents-mcp.md).*
