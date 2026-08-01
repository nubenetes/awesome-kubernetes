---
description: "Curated, AI-ranked Kubernetes Releases resources for the 2026 Cloud Native architect: top-tier tools, guides and references (The Container Stack)."
---
# Kubernetes Releases

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-releases/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Releases in the context of The Container Stack.

## Cloud Integrations

### AWS

#### Security

  - **(2023)** [Private Access to the AWS Management Console is generally available](https://aws.amazon.com/about-aws/whats-new/2023/05/aws-management-console-private-access)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the general availability of Private Access to the AWS Management Console. This feature allows enterprise customers to limit console access to connections originating from specific network endpoints or VPCs, drastically reducing potential attack surfaces and ensuring secure administration paths.
## Kubernetes Core

### API Evolution

#### V1.16

  - **(2019)** [Kubernetes v1.16 API deprecation testing](https://gist.github.com/jimangel/0014770713cdca8b363816930ef2520f) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight features a test script for identifying deprecated Kubernetes v1.16 APIs. Live engineering truth in 2026 finds this script outdated, though historically valuable for understanding the mechanics of migrating extensions/v1beta1 API resources.
#### V1.22

  - **(2021)** [kubernetes.io: Kubernetes API and Feature Removals In 1.22: Here’s What You Need To Know](https://kubernetes.io/blog/2021/07/14/upcoming-changes-in-kubernetes-1-22) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight points to the critical official guide regarding upcoming 1.22 API removals. In 2026, this remains the historical checklist template used by platform engineers to design deprecation checklists.
#### V1.25

  - **(2022)** [kubernetes.io: Kubernetes Removals and Major Changes In 1.25](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the upcoming removals in 1.25. Live grounding in 2026 registers 1.25 as the ultimate removal point for PodSecurityPolicy (PSP), finalizing the modern security validation ecosystem.
### Cluster Security

#### V1.21

  - **(2021)** [devclass.com: Kubernetes 1.21 unloads pod security, adds dual IPv4/IPv6 networking, and shuts down gracefully](https://www.devclass.com/containers/2021/04/09/kubernetes-121-unloads-pod-security-adds-dual-ipv4/ipv6-networking-and-shuts-down-gracefully/1623619)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight discusses Kubernetes 1.21 dropping PodSecurityPolicy, adding dual IPv4/IPv6 networking, and implementing graceful shutdowns. In 2026, dual-stack networking is highly standard, having originated from these architectural changes.
#### V1.23

  - **(2021)** [blog.aquasec.com: Kubernetes Version 1.23: What's New for Security?](https://blog.aquasec.com/kubernetes-version-1.23-security-features)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight duplicates security focuses in 1.23. In 2026, it remains useful for security compliance audits when checking clusters against legacy security postures.
### Container Runtimes

#### Dockershim Deprecation

  - **(2021)** [kubernetes.io: Dockershim removal is coming. Are you ready?](https://kubernetes.io/blog/2021/11/12/are-you-ready-for-dockershim-removal) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on Dockershim removal readiness. In 2026, this remains a valuable reference artifact for migrating air-gapped systems or old enterprise clusters from Docker to containerd.
  - **(2020)** [zdnet.com: Kubernetes dropping Docker is not that big of a deal](https://www.zdnet.com/article/kubernetes-dropping-docker-is-not-that-big-of-a-deal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight notes ZDNet's perspective that removing Dockershim is not a disruptive disaster. Live grounding in 2026 confirms this prediction was correct, as the ecosystem successfully migrated to containerd and CRI-O without massive developer friction.
  - **(2020)** [openshift.com: Kubernetes is Removing Docker Support, Kubernetes is Not Removing Docker Support](https://www.redhat.com/en/blog/kubernetes-is-removing-docker-support-kubernetes-is-not-removing-docker-support)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight identifies Red Hat's explanatory guide on the nuance of Docker support removal. Live grounding in 2026 verifies this piece as a classic, helping teams comprehend that standard OCI-compliant Docker containers remained compatible despite runtime changes.
#### V1.24

  - **(2022)** [infoq.com: Kubernetes Proceeding with Deprecation of Dockershim in Upcoming 1.24 Release](https://www.infoq.com/news/2022/01/kubernetes-dockershim-removal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines InfoQ's coverage of Dockershim's imminent demise in 1.24. Live grounding in 2026 records this as the definitive end of direct Docker Engine support within the kubelet codebase.
  - **(2022)** [kubernetes.io: Updated: Dockershim Removal FAQ](https://kubernetes.io/blog/2022/02/17/dockershim-faq) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight provides the updated Dockershim FAQ. In 2026, it serves as an excellent reference troubleshooting tool for understanding CRI-dockerd shims and standard CRI integrations.
### Infrastructure

#### Registry

  - **(2022)** [kubernetes.io: registry.k8s.io: faster, cheaper and Generally Available (GA)](https://kubernetes.io/blog/2022/11/28/registry-k8s-io-faster-cheaper-ga) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces the transition of the primary Kubernetes container registry from 'k8s.gcr.io' to the community-owned, CDN-backed 'registry.k8s.io'. This infrastructural pivot reduces data egress costs and latency by intelligently routing traffic to regional cloud storage providers near the client nodes. Engineers must audit existing configuration files and pipelines to refer to the new endpoint to avoid build failures.
### Job Scheduling

#### V1.21 (1)

  - **(2021)** [kubernetes.io: kubernetes 1.21: CronJob Reaches GA](https://kubernetes.io/blog/2021/04/09/kubernetes-release-1.21-cronjob-ga) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight provides the official blog announcement of CronJob reaching GA in Kubernetes 1.21. Live analysis in 2026 acknowledges this as the milestone that finalized the performance and controller upgrades for batch scheduling.
  - **(2021)** [kubernetes.io: Introducing Suspended Jobs in Kubernetes 1.21](https://kubernetes.io/blog/2021/04/12/introducing-suspended-jobs) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces suspended jobs in 1.21. Live grounding in 2026 indicates this feature was a crucial building block for modern external batch orchestrators like Kueue to control execution pauses.
### Node Management

#### Fault Tolerance

  - **(2022)** [kubernetes.io: Kubernetes 1.26: Non-Graceful Node Shutdown Moves to Beta](https://kubernetes.io/blog/2022/12/16/kubernetes-1-26-non-graceful-node-shutdown-beta) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces the promotion of Non-Graceful Node Shutdown capabilities to Beta in Kubernetes 1.26. This feature enables stateful workloads (such as databases on StatefulSets) to recover gracefully on active nodes when a cluster host crashes abruptly without a proper shutdown path. This addresses a common issue where volume attachments remained locked to failed instances indefinitely.
#### V1.22 (1)

  - **(2021)** [kubernetes.io: Graceful Node Shutdown Goes Beta](https://kubernetes.io/blog/2021/04/21/graceful-node-shutdown-beta) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights Graceful Node Shutdown transitioning to Beta in 1.22. Live grounding in 2026 confirms this functionality prevents database corruption and packet drops on spot instances by coordinating termination steps with systemd.
### Observability

#### V1.21 (2)

  - **(2021)** [kubernetes.io: Kubernetes 1.21: Metrics Stability hits GA](https://kubernetes.io/blog/2021/04/23/kubernetes-release-1.21-metrics-stability-ga) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight records the GA of Metrics Stability in 1.21. Live analysis in 2026 confirms this stabilization framework remains critical for maintaining backwards-compatible prometheus exporters without breaking monitoring dashboards.
### Operator Framework

#### V1.20

  - **(2020)** [thenewstack.io: Kubernetes 1.20 Enhances the Operator Experience and Brings New Features to the Container Runtime](https://thenewstack.io/kubernetes-1-20-enhances-the-operator-experience-and-brings-new-features-to-the-container-runtime)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the operator and container runtime interface advancements in 1.20. Live engineering review in 2026 uses this context to study early attempts to standardize execution metrics for operational tooling.
### Release Lifecycle

#### Documentation

  - **(2026)** [relnotes.k8s.io: Kubernetes Release Notes](https://relnotes.k8s.io) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the official Kubernetes Release Notes portal. Live grounding in 2026 demonstrates this tool's constant utility for DevOps engineers running automated deprecation pipelines and tracking version-to-version API mutations.
#### Process

  - **(2021)** [kubernetes.io: Kubernetes Release Cadence Change: Here’s What You Need To Know](https://kubernetes.io/blog/2021/07/20/new-kubernetes-release-cadence) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight addresses the Kubernetes Release Cadence shift from 4 to 3 releases per year. Live grounding in 2026 confirms this release model has brought predictability and stability to platform teams everywhere.
#### V1.20 (1)

  - **(2020)** [thenewstack.io: Kubernetes 1.20 Lands with 44 Enhancements](https://thenewstack.io/kubernetes-1-20-lands-with-44-enhancements)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on the 44 enhancements landing with Kubernetes 1.20. In 2026, this resource provides historic data on the stabilization of volume snapshots, PID limits, and early steps toward API deprecation tracking.
#### V1.21 (3)

  - **(2021)** [devopscube.com: Kubernetes v1.21 Released: Here is What you should know](https://devopscube.com/kubernetes-v1-21-released)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight offers an overview of Kubernetes 1.21. In 2026, we track this release as a major evolution that brought CronJobs to GA and introduced PodDisruptionBudget stability.
  - **(2021)** [kubernetes.io: Kubernetes 1.21: Power to the Community](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents the official 1.21 release announcement 'Power to the Community'. From a 2026 perspective, 1.21 initiated the long-awaited deprecation of PodSecurityPolicy, shifting the community towards Pod Security Standards.
  - **(2021)** [analyticsindiamag.com: Kubernetes v1.21 Released: Major Updates & Latest Features](https://analyticsindiamag.com/kubernetes-v1-21-released-major-updates-latest-features)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight notes major updates in 1.21 from Analytics India Mag. Modern review in 2026 confirms the article effectively summarized regional interest in memory topology and scheduling refinements.
  - **(2021)** [openshift.com: Kubernetes 1.21 Grows Innovative New Features](https://www.redhat.com/en/blog/kubernetes-1.21-grows-innovative-new-features)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents Red Hat's analysis of 1.21 features. Live grounding in 2026 reviews this for enterprise adaptation paths, specifically outlining how OpenShift clients prepared for eventual PSP deprecations.
#### V1.22 (2)

  - **(2021)** [sysdig.com: Kubernetes 1.22 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-22-whats-new)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight highlights Sysdig's review of Kubernetes 1.22. Live grounding in 2026 views 1.22 as the milestone where major legacy APIs (like v1beta1 Ingress) were fully removed, causing teams to aggressively update Helm charts.
  - **(2021)** [kubernetes.io: Kubernetes 1.22: Reaching New Peaks](https://kubernetes.io/blog/2021/08/04/kubernetes-1-22-release-announcement) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents the 1.22 release announcement 'Reaching New Peaks'. In 2026, this represents the definitive documentation on client credential plugins and early server-side apply stabilization.
  - **(2021)** [thenewstack.io: Less Is More with Kubernetes 1.22](https://thenewstack.io/less-is-more-with-kubernetes-1-22)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight analyzes the 'Less Is More' paradigm of 1.22. Live grounding in 2026 reflects on how API cleanliness made the control plane leaner, decreasing memory footprint and etcd payload overhead.
  - **(2021)** [acloudguru.com: What’s new with Kubernetes 1.22?](https://www.pluralsight.com/resources/blog/cloud/whats-new-with-kubernetes-1-22)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight points to Pluralsight's educational summary of 1.22. In 2026, it serves as a baseline tutorial explaining the transition to cgroups v2, which has since become standard in all production distros.
#### V1.23 (1)

  - **(2021)** [sysdig.com: Kubernetes 1.23 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-23-whats-new)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents Sysdig's assessment of Kubernetes 1.23. Live review in 2026 shows this release solidified Dual-stack IPv4/IPv6 services to GA and introduced Ephemeral Volumes.
  - **(2021)** [thenewstack.io: Kubernetes 1.23: Dual Stack IPv4/IPv6, CronJobs, Ephemeral Volumes](https://thenewstack.io/kubernetes-1-23-dual-stack-ipv4-ipv6-cronjobs-ephemeral-volumes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight summarizes the GA of Dual-stack and CronJobs in 1.23. Live engineering analysis in 2026 verifies these features are highly mature, having stabilized completely during the 1.23 release cycle.
  - **(2021)** [kubernetes.io: Kubernetes 1.23: The Next Frontier](https://kubernetes.io/blog/2021/12/07/kubernetes-1-23-release-announcement) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the official Kubernetes 1.23 announcement 'The Next Frontier'. In 2026, this announcement marks the stabilization of ephemeral containers for interactive debugging.
#### V1.24 (1)

  - **(2022)** [sysdig.com: Kubernetes 1.24 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-24-whats-new)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents Sysdig's review of 1.24. Live analysis in 2026 reminds us that 1.24 removed Dockershim, introduced Beta volume expansion, and made gRPC probes standard.
#### V1.25 (1)

  - **(2022)** [sysdig.com: Kubernetes 1.25 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-25-whats-new)  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Curator Insight reviews what is new in 1.25. In 2026, this is remembered for bringing Pod Security Admission to GA, KMS v2 alpha, and cgroups v2 enhancements.
### Releases

#### V1.25 (2)

  - **(2022)** [kubernetes.io: Kubernetes v1.25: Combiner](https://kubernetes.io/blog/2022/08/23/kubernetes-v1-25-release) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubernetes v1.25, dubbed 'Combiner', represents a major milestone in core stability and API maturation. The release is architecturally significant for the formal removal of PodSecurityPolicy (PSP) in favor of Pod Security Admission (PSA) and the promotion of several storage features to General Availability. Operators must adapt to these security and storage modifications to ensure workload compatibility.
#### V1.26 Analysis

  - **(2022)** [armosec.io: Kubernetes Version 1.26: Everything You Should Know](https://www.armosec.io/blog/kubernetes-1-26-everything-you-should-know)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A security-focused architectural assessment of Kubernetes 1.26. The paper highlights the deprecation of non-CSI storage plugins, the expansion of dynamic security standards, and the introduction of CEL validations in admission controllers. This analysis provides key insights for security engineers seeking to implement finer control policies directly within API servers.
#### V1.26 Features

  - **(2022)** [sysdig.com: Kubernetes 1.26 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-26-whats-new)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed technical review of the architectural enhancements shipped in Kubernetes 1.26. Key features highlighted include Common Expression Language (CEL) validation in CustomResourceDefinitions (CRDs), improvements to Pod Scheduling Readiness, and container registry migrations. This summary acts as an essential checklist for systems engineering teams coordinating scheduled cluster upgrades.
#### V1.27

  - **(2023)** [kubernetes.io: Kubernetes v1.27: Chill Vibes](https://kubernetes.io/blog/2023/04/11/kubernetes-v1-27-release) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official documentation for the Kubernetes 1.27 release ('Chill Vibes'). Featuring 40 enhancement proposals, this release emphasizes security posture hardening, scheduling optimizations, and resource isolation. Prominent updates include the graduation of SeccompDefault to GA and the introduction of in-place container resource resizing.
#### V1.27 Features

  - **(2023)** [sysdig.com: Kubernetes 1.27 – What’s new?](https://www.sysdig.com/blog/kubernetes-1-27-whats-new)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical overview of Kubernetes 1.27's flagship updates. Features evaluated include the stabilization of SeccompDefault, container image signature verification workflows, and advancements in dynamic resource allocation. This serves as a vital blueprint for enterprise platform teams coordinating upcoming cluster upgrades.
#### V1.27 Industry

  - **(2023)** [thenewstack.io: Kubernetes 1.27 Arrives](https://thenewstack.io/kubernetes-1-27-arrives)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Industry reporting on the release of Kubernetes 1.27, detailing the major developer and operator benefits. It focuses on how security stabilization, API cleanup, and enhanced cluster control interfaces enable enterprise systems to scale more safely and cost-effectively.
#### V1.27 Security

  - **(2023)** [armosec.io: Kubernetes 1.27 Release: Enhancements and Security Updates](https://www.armosec.io/blog/kubernetes-1-27-release)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth security analysis detailing the security updates and modifications introduced in Kubernetes 1.27. It discusses shifts in default container security profiles, RBAC configurations, and validation tools, providing actionable guidelines for compliance and cluster hardening.
#### V1.28 Features

  - **(2023)** [thenewstack.io: Kubernetes 1.28 Accommodates the Service Mesh, Sudden Outages](https://thenewstack.io/kubernetes-1-28-accommodates-the-service-mesh-sudden-outages)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry report covering Kubernetes 1.28's key updates, notably native support for sidecar container lifecycles to aid service mesh deployments, and automated recovery controls for sudden node failures. These updates greatly reduce the coordination code needed for robust, multi-tenant microservices clusters.
### Resource Allocation

#### V1.21 (4)

  - **(2021)** [thenewstack.io: Kubernetes 1.21 Brings a New Memory Manager, More Flexible Scheduling](https://thenewstack.io/kubernetes-1-21-brings-a-new-memory-manager-more-flexible-scheduling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the introduction of a new Memory Manager and flexible scheduling in 1.21. Live grounding in 2026 shows these scheduling frameworks laid the groundwork for modern NUMA-aware multi-core resource allocation in HPC/AI setups.
#### V1.22 (3)

  - **(2021)** [kubernetes.io: Kubernetes Memory Manager moves to beta](https://kubernetes.io/blog/2021/08/11/kubernetes-1-22-feature-memory-manager-moves-to-beta) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight explains the Kubernetes Memory Manager moving to Beta. Live engineering in 2026 points to this as the genesis of modern NUMA alignment for performance-sensitive low-latency microservices.
### Resource Management

#### Cpumanager

  - **(2022)** [kubernetes.io: Kubernetes v1.26: CPUManager goes GA](https://kubernetes.io/blog/2022/12/27/cpumanager-ga) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Celebrates the General Availability (GA) of the CPUManager in Kubernetes 1.26. This sub-system allows high-performance workloads to pin CPU cores, offering deterministic scheduling profiles by enforcing NUMA node alignment. Architects can exploit these improvements to drastically reduce latency in database pipelines, streaming engines, and high-frequency trading workloads.
#### Pod Resize

  - **(2023)** [kubernetes.io: Kubernetes 1.27: In-place Resource Resize for Kubernetes Pods (alpha)](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Reviews the highly anticipated alpha feature in Kubernetes 1.27: In-place Resource Resize for Pods. This allows engineers to dynamically scale CPU and memory resources allocated to running containers without requiring a pod restart. This capability drastically improves availability and operational costs for scaling-heavy stateful applications and microservices.
### Scheduling

#### Resource Allocation (1)

  - **(2022)** [kubernetes.io: Kubernetes 1.26: Pod Scheduling Readiness](https://kubernetes.io/blog/2022/12/26/pod-scheduling-readiness-alpha) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the newly introduced Pod Scheduling Readiness feature in Kubernetes 1.26. This allows external controllers to declare scheduling gates on a pod, signaling the scheduler to ignore the resource until specific dependencies are resolved (e.g., custom network setups or resource pre-allocation). This significantly reduces scheduler queue overhead in dynamic, automated environments.
## Kubernetes Networking

### Traffic Engineering

#### Load Balancing

  - **(2022)** [kubernetes.io: Kubernetes v1.26: Advancements in Kubernetes Traffic Engineering](https://kubernetes.io/blog/2022/12/30/advancements-in-kubernetes-traffic-engineering) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights advancements in Kubernetes Traffic Engineering during the 1.26 release lifecycle, focusing on Service Internal Traffic Policy and Topology Aware Routing. These adjustments allow clusters to minimize latency and cross-AZ data transfer fees by dynamically routing traffic closer to the requesting endpoint. Excellent resource for networking engineers designing large-scale cloud topologies.
## Kubernetes Orchestration

### Batch Jobs

#### Job Tracking

  - **(2022)** [kubernetes.io: Kubernetes 1.26: Job Tracking, to Support Massively Parallel Batch Workloads, Is Generally Available](https://kubernetes.io/blog/2022/12/29/scalable-job-tracking-ga) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the GA milestone of Scalable Job Tracking in Kubernetes 1.26. By offloading job tracking from querying all remaining pods to an optimized finalizer architecture, the API server can efficiently orchestrate massively parallel processing workloads. This enhancement dramatically lowers memory consumption and API server load in large-scale machine learning and batch-processing frameworks.
## Kubernetes Security

### Policies

#### Deprecation Critique

  - **(2022)** [macchaffee.com: The Fumbled Deprecation of PodSecurityPolicies](https://www.macchaffee.com/blog/2022/psp-deprecation) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — This architectural critique analyzes the friction caused by the rapid deprecation of PodSecurityPolicies (PSP). The author highlights gaps in transition paths and the operational challenges encountered by platform engineering teams moving legacy workloads to alternative admission controllers like Gatekeeper or Kyverno. It serves as an informative case study on upstream platform stewardship and API migration management.
#### Pod Security Policy

  - **(2022)** [kubernetes.io: PodSecurityPolicy: The Historical Context 🌟](https://kubernetes.io/blog/2022/08/23/podsecuritypolicy-the-historical-context) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed post-mortem on PodSecurityPolicy (PSP) providing the architectural context behind its deprecation and eventual removal in v1.25. The publication details structural flaws in PSP's design, including complex API authorization models and the lack of a dry-run capability. This serves as critical foundational reading for security architects migrating clusters to modern Pod Security Standards (PSS) or third-party engines.
## Kubernetes Storage

### CSI

#### Volume Mounts

  - **(2022)** [kubernetes.io: Kubernetes 1.26: Support for Passing Pod fsGroup to CSI Drivers At Mount Time](https://kubernetes.io/blog/2022/12/23/kubernetes-12-06-fsgroup-on-mount) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the Kubernetes 1.26 enhancement enabling Pod fsGroup parameters to be passed directly to CSI drivers during volume mounting operations. By delegating directory permissions and ownership shifts to the underlying storage provider rather than executing local chown recursions, this update dramatically speeds up pod boot times on massive datasets. This optimization represents a major advancement in storage management efficiency.
## Managed Kubernetes

### AWS EKS

#### V1.22 (4)

  - **(2022)** [aws.amazon.com: Amazon EKS now supports Kubernetes 1.22](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-kubernetes-1-22)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight covers EKS supporting Kubernetes 1.22. Live grounding in 2026 treats this as historical information; modern EKS runs vastly newer versions, but this article highlights EKS migration paths and deprecation management.
### EKS

#### Upgrades

  - **(2022)** [datree.io: EKS 1.22 Upgrade Tutorial](https://www.datree.io/resources/eks-1-22-upgrade-tutorial)  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An operations-oriented technical walkthrough focusing on upgrading Amazon EKS clusters to version 1.22. It documents the impact of deprecated v1beta1 API removals, specifically detailing transitions for Ingress and CustomResourceDefinition objects. SREs can leverage this guide to configure validation scripts and preventative gatekeeping within CI/CD pipelines prior to AWS control-plane updates.

---
💡 **Explore Related:** [Kubernetes On Premise](./kubernetes-on-premise.md) | [Container Managers](./container-managers.md) | [Docker](./docker.md)

🔗 **See Also:** [Project Management Methodology](./project-management-methodology.md) | [AWS Databases](./aws-databases.md)

