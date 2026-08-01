---
description: "Top OCP 3 resources for 2026, AI-ranked: **KubeFed Operator**, None and more — curated Cloud Native tools, guides and references."
---
# OCP 3

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ocp3/).

!!! info "Architectural Context"
    Detailed reference for OCP 3 in the context of The Container Stack.

## App Development

### Packaging

#### Helm Charts

  - **(2019)** [blog.openshift.com/: From Templates to Openshift Helm Charts](https://www.redhat.com/en/blog/from-templates-to-openshift-helm-charts) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on porting proprietary OpenShift templates into standard Helm Charts, improving cross-platform compatibility and simplifying application rollout processes.
  - **(2019)** [Templating on OpenShift: should I use Helm templates or OpenShift templates? 🌟](https://www.theodo.com/en-fr/blog/openshift-what-templates-should-you-use-helm-or-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comparative analysis contrasting OpenShift native templates with Helm charts. Outlines how Helm's global community, revision tracking, and subchart structures provide a superior template solution for complex microservice environments.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [dzone: 8 Options for Capturing Thread Dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: 8 Options for Capturing Thread Dumps in the Kubernetes Tools ecosystem.
  - **(None)** [](https://www.redhat.com/en/blog/using-openshift-3-on-your-local-environment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.redhat.com in the Kubernetes Tools ecosystem.
  - **(None)** [](https://www.redhat.com/en/blog/how-full-is-my-cluster-part-5-a-capacity-management-dashboard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.redhat.com in the Kubernetes Tools ecosystem.
## CICD

### Gitops

#### Migration Strategies

  - **(2021)** [blog.openshift.com/: is it too late to integrate GitOps?](https://www.redhat.com/en/blog/is-it-too-late-to-integrate-gitops) 🌟🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight maps the path for legacy environments migrating to continuous sync models. Live Grounding reviews incremental conversion blueprints to safe declarative setups under OpenShift. It acts as an advisory piece for migration architects.
#### Openshift

  - **(2020)** [**blog.openshift.com/: Introduction to GitOps with OpenShift**](https://www.redhat.com/en/blog/introduction-to-gitops-with-openshift) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight defines the OpenShift declarative application delivery model. Live Grounding details the Red Hat OpenShift GitOps operator powered by Argo CD. This is the official blueprint for establishing structured continuous integration on Red Hat environments.
## Kubernetes Cluster Operations

### Autoscaling

#### Vertical Pod Autoscaler

  - **(2020)** [**blog.openshift.com/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler**](https://www.redhat.com/en/blog/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight focuses on the role of Vertical Pod Autoscalers (VPA). Live Grounding evaluates recommendation engines, safety limits, and automatic resource reallocations on OpenShift. Important reference for auto-scaling and efficiency.
### Multi-cluster

#### Legacy Federation

  - **(2019)** [Multi-cluster Federation in OpenShift 4 is called **KubeFed**](https://www.redhat.com/en/blog/federation-v2-is-now-kubefed) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces the KubeFed system in OpenShift 4. Live Grounding highlights its mechanism for template distribution and configuration sync across multiple clusters. Valuable for understanding historical cross-cluster patterns before modern gateway patterns.
  - **(2018)** [OpenShift 3.11 Multi-cluster Federation](https://www.redhat.com/en/blog/kubernetes-federation-v2-on-openshift-3-11) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight looks at multi-cluster federation on older OpenShift 3.11 setups. Live Grounding illustrates early architectural attempts to distribute workloads across cloud regions. Crucial historical context before modern GitOps and Cluster API paradigms took over.
### Resource Management

#### Openshift (1)

  - **(2019)** [blog.openshift.com/full-cluster-capacity-management-monitoring-openshift](https://www.redhat.com/en/blog/full-cluster-capacity-management-monitoring-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight initiates a series on OpenShift capacity planning. Live Grounding details Prometheus and Grafana alerts, memory saturation metrics, and CPU scheduling limits. Essential for cluster administrators managing highly dense node resources.
  - **(2019)** [blog.openshift.com/full-cluster-part-2-protecting-nodes](https://www.redhat.com/en/blog/full-cluster-part-2-protecting-nodes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on securing host resources from rogue applications. Live Grounding details eviction thresholds, pod limits, and system-reserved configuration paths inside OpenShift clusters. Vital for maintaining node reliability.
  - **(2019)** [full-cluster-part-3-capacity-management](https://www.redhat.com/en/blog/full-cluster-part-3-capacity-management) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight reviews multi-tenant resource optimization. Live Grounding analyzes quotas, LimitRanges, and tenant isolation layers in enterprise workloads. Highly effective for designing multi-team cluster footprints.
## Platform Architecture

### Administration

#### Automation

  - **(2020)** [developers.redhat.com: Customizing OpenShift project creation 🌟](https://developers.redhat.com/blog/2020/02/05/customizing-openshift-project-creation) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details dynamic project onboarding techniques for OpenShift administrators. Teaches how to configure customized templates that automatically enforce security contexts, default quotas, and custom networking parameters upon namespace creation.
### Automation (1)

#### Ansible

  - **(2023)** [GitHub redhat-cop: Ansible Role 🌟](https://github.com/redhat-cop/infra-ansible) <span class='md-tag md-tag--info'>⭐ 219</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e0754050" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 6 L 20 13 L 30 10 L 40 10 L 50 12" fill="none" stroke="url(#spark-grad-e0754050)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A structured repository of Ansible automation roles customized for provisioning, maintaining, and configuring OpenShift resources. Simplifies operations such as authentication, user management, and day-2 configurations.
#### Community Tools

  - **(2026)** [Red Hat Communities of Practice](https://github.com/redhat-cop) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The master platform profile of Red Hat's Communities of Practice. Contains scripts, custom operator codes, and automated scaffolding for cluster setups, management, and resource governing processes.
### Core Concepts

#### Kubernetes Pods

  - **(2018)** [blog.openshift.com/ - Kubernetes: A Pod’s Life 🌟](https://www.redhat.com/en/blog/kubernetes-pods-life) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A fundamental exploration of the life cycle of a Kubernetes Pod. Outlines start sequences, init container routines, readiness/liveness checks, and termination processes, establishing a baseline for container orchestration troubleshooting.
### High Availability

#### Disaster Recovery

  - **(2019)** [blog.openshift.com/: Stateful Workloads and the Two Data Center Conundrum](https://www.redhat.com/en/blog/stateful-workloads-and-the-two-data-center-conundrum) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the persistence challenges associated with stateful microservices running across multi-site cluster architectures. Evaluates split-brain hazards and suggests synchronous storage configurations to guarantee data integrity.
#### Stretch Clusters

  - **(2019)** [blog.openshift.com/: How to survive an outage and live to tell about it!](https://www.redhat.com/en/blog/metro-area-openshift-stretch-cluster-how-to-survive-an-outage-and-live-to-tell-about-it) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Analyzes the design of Metro-Area stretch clusters on OpenShift, ensuring high availability in case of datacenter outages. Discusses network transit criteria, ETCD consensus configurations, and storage replications.
### Infrastructure

#### Comparisons

  - **(2020)** [claydesk.com: Google Cloud App Engine Vs Red Hat OpenShift](https://www.claydesk.com/ecampus/google-cloud-app-engine-vs-red-hat) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes key platform differences between Google Cloud App Engine and OpenShift. Compares scaling, cluster management boundaries, provider dependencies, and operational flexibility when deploying enterprise workloads.
### Multicluster

#### Disaster Recovery (1)

  - **(2021)** [blog.openshift.com/tag/multi-datacenter](https://www.redhat.com/en/blog?f[0]=taxonomy_blog_post_category_tid:107161&f[1]=taxonomy_topic_tid:75521) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A thematic curation of architectural entries covering multi-cluster synchronization, active-active topologies, global service routing, and deployment configurations utilizing Advanced Cluster Management.
#### Kubernetes Federation

  - **(2021)** [**KubeFed Operator**](https://operatorhub.io/operator/kubefed-operator) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — The Kubernetes Federation (KubeFed) Operator designed to coordinate configurations across multiple distinct clusters. In 2026, KubeFed has been largely archived, superseded by Red Hat Advanced Cluster Management (RHACM) and Open Cluster Management (OCM).
### Resource Management (1)

#### Autoscaling (1)

  - **(2020)** [developers.redhat.com: Testing memory-based horizontal pod autoscaling on OpenShift 🌟](https://developers.redhat.com/blog/2020/03/19/testing-memory-based-horizontal-pod-autoscaling-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A diagnostic tutorial explaining how to design, execute, and inspect Horizontal Pod Autoscaler scaling metrics based on container RAM thresholds. Includes guidelines for generating stable test scenarios.
#### Governance

  - **(2020)** [OpenShift 4 Resource Management](https://www.youtube.com/watch?v=JC_PB1yZcIc) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An informative session demonstrating effective scheduling, configuration, and governing mechanics of OpenShift 4 resources. Highlights the use of LimitRanges, ResourceQuotas, and Node selectors.
  - **(2019)** [techbeatly.com: How to create, increase or decrease project quota](https://techbeatly.com/how-to-create-increase-or-decrease-project-quota-in-openshift) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on managing project resource limits inside OpenShift namespaces. Explores configuring quotas via the oc CLI to enforce hard boundaries on CPU, RAM, and storage allocations.
### Resources

#### Learning Paths

  - **(2019)** [certdepot.net: OpenShift Free available resources 🌟](https://www.certdepot.net/openshift-free-available-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An educational index detailing free courses, interactive sandbox playgrounds, and study materials for professionals pursuing official Red Hat OpenShift certifications.
## Platform Engineering

### Gitops (1)

#### Authentication and SSO

##### Openshift (2)

  - **(2022)** [**openshift.com: OpenShift Authentication Integration with ArgoCD**](https://www.redhat.com/en/blog/openshift-authentication-integration-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the integration of OpenShift's native OAuth server with ArgoCD. Explains how to map OpenShift user groups to ArgoCD RBAC roles, establishing a secure, unified single sign-on (SSO) experience for enterprise platforms.
## Security

### Encryption

#### .NET Core

  - **(2018)** [developers.redhat.com: Securing .NET Core on OpenShift using HTTPS](https://developers.redhat.com/blog/2018/10/12/securing-net-core-on-openshift-using-https) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through configuring ASP.NET Core microservices with end-to-end TLS encryption on OpenShift. Discusses dynamic integration of local server certificates using OpenShift's service serving certificates feature.

---
💡 **Explore Related:** [Kubernetes On Premise](./kubernetes-on-premise.md) | [Container Managers](./container-managers.md) | [Docker](./docker.md)

🔗 **See Also:** [Project Management Methodology](./project-management-methodology.md) | [AWS Databases](./aws-databases.md)

