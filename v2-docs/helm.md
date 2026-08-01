---
description: "Top Helm resources for 2026, AI-ranked: Helm, Artifact Hub and more — curated Cloud Native tools, guides and references."
---
# Helm Kubernetes Tool

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/helm/).

!!! info "Architectural Context"
    Detailed reference for Helm Kubernetes Tool in the context of Architectural Foundations.

## Application Delivery

### Helm

#### Registries

  - **(2024)** [Choerodon Nexus3 🌟](https://artifacthub.io/packages/helm/choerodon/nexus3) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active Helm package designed to configure and orchestrate Sonatype Nexus3 instances. It handles data persistence, ingress routing, and performance tuning configurations optimized for enterprise container workloads.
## Automation and Orchestration

### Package Management

#### Helm (1)

  - **(2026)** [==Helm==](https://github.com/helm/helm) <span class='md-tag md-tag--info'>⭐ 29874</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-690133b2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 3 L 20 7 L 30 4 L 40 11 L 50 2" fill="none" stroke="url(#spark-grad-690133b2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official Go implementation of the Helm client, acting as the package manager for Kubernetes. Helm manages complex application definitions through charts, providing repeatable deployments, in-place upgrades, and robust rollback capabilities.
## Cloud Native

### Application Delivery (1)

#### Design Patterns

##### Advanced Templating

  - **(2021)** [blog.flant.com: Making the most out of Helm templates 🌟](https://palark.com/blog/advanced-helm-templating) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced tutorial highlighting powerful features in Helm’s templating engine (Go templates/Sprig library). Outlines loops, conditional formatting, dictionary manipulation, and helper functions to reduce manifest duplication.
##### Best Practices

  - **(2021)** [jfrog.com: Steering Straight with Helm Charts Best Practices 🌟](https://jfrog.com/blog/helm-charts-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Industry recommendations for designing robust Helm charts. Explores standard naming conventions, managing optional dependencies, versioning strategies (Semantic Versioning), and optimizing values files for enterprise-grade registries.
  - **(2020)** [codersociety.com: 13 Best Practices for using Helm](https://codersociety.com/blog/articles/helm-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curated list of 13 foundational design patterns and practices for Helm charts. Topics include semantic versioning compliance, clean separation of concerns within values files, and keeping dependencies decoupled.
##### HULL Library

  - **(2021)** [dev.to: HULL Tutorial 01: Introducing HULL, the Helm Universal Layer Library](https://dev.to/gre9ory/hull-tutorial-01-introducing-hull-the-helm-universal-layer-library-4njb) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical introduction to HULL (Helm Universal Layer Library), a standardized, library-chart-driven mechanism to dramatically simplify Kubernetes manifest configuration without writing massive custom Go templates.
#### Documentation Automation

  - **(2022)** [chart-doc-gen: Helm Chart Documentation Generator](https://github.com/kubepack/chart-doc-gen) <span class='md-tag md-tag--info'>⭐ 122</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d2f3319e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 4 L 20 12 L 30 11 L 40 9 L 50 7" fill="none" stroke="url(#spark-grad-d2f3319e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Command-line utility that extracts configuration variables directly from values.yaml to compile uniform Markdown files. Speeds up delivery by ensuring user manuals and codebases stay perfectly aligned.
  - **(2026)** [Frigate](https://frigate.readthedocs.io/en/latest) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Open-source documentation generator specializing in extracting complex metadata profiles from Helm values files. Provides teams with structural consistency by eliminating manual developer intervention when writing chart readmes.
#### Helm Plugins

##### API Migration

  - **(2026)** [Helm mapkubeapis Plugin](https://github.com/helm/helm-mapkubeapis) <span class='md-tag md-tag--info'>⭐ 1035</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ab83c767" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 6 L 20 6 L 30 8 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-ab83c767)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — Fundamental operator utility that edits release metadata in-place to update deprecated or removed Kubernetes APIs. Prevents release locks and upgrade failures when cluster components transition to newer API versions.
##### Release Management

  - **(2022)** [JovianX/helm-release-plugin](https://github.com/JovianX/helm-release-plugin) <span class='md-tag md-tag--info'>⭐ 109</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-fcd70b4b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 9 L 20 6 L 30 13 L 40 10 L 50 2" fill="none" stroke="url(#spark-grad-fcd70b4b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Utility command plugin allowing cluster administrators to inspect, unpack, and export deployment releases easily. Facilitates troubleshooting across multi-environment states and eases visual configuration comparisons.
##### Topology Visualization

  - **(2026)** [Helm Kanvas Snapshot](https://github.com/meshery-extensions/helm-kanvas-snapshot) <span class='md-tag md-tag--info'>⭐ 43</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b88865a1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 11 L 20 12 L 30 7 L 40 12 L 50 10" fill="none" stroke="url(#spark-grad-b88865a1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Integrates Meshery's visualization layer into Helm pipelines. Enables engineers to capture runtime topology models and visually document deployed resource layouts directly from active releases.
#### Operators

##### Helm Integration

  - **(2020)** [cloud.redhat.com: Application Management in Kubernetes Environments with Helm Charts and Kubernetes Operators](https://www.redhat.com/en/blog/application-management-in-kubernetes-environments-with-helm-charts-and-kubernetes-operators)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Contrasts and complements application packaging methods with Helm Charts versus the Kubernetes Operator Framework. Illustrates how developers choose Helm for simpler, template-based deployments and Operators for complex, stateful operations.
#### Package Management (1)

##### Chart Validation

  - **(2021)** [Helm 3: Validating Helm Chart Values with JSON Schemas 🌟](https://www.arthurkoziel.com/validate-helm-chart-values-with-json-schemas) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep technical guide on leveraging JSON Schema definitions (`values.schema.json`) to enforce parameter validation prior to execution. Mitigates run-time failures and schema mismatches in multi-tenant environments by validating configuration inputs during build time.
##### Demystifying

  - **(2020)** [youtube.com: Demystifying Helm 🌟](https://www.youtube.com/watch?v=2HPsPOwHOlY&ab_channel=DonovanBrown)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explanatory session demystifying Helm internals. Illustrates how manifest rendering works on the client-side and describes the storage of release history as Secrets inside target Kubernetes namespaces.
##### Helm (2)

###### DevOps

  - **(2022)** [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dive educational video analyzing advanced templating, customized hooks, and Helm execution patterns in Enterprise environments. Explains structural lifecycle hooks and complex value manipulation to secure production-ready application pipelines.
###### Documentation

  - **(2026)** [helm.sh](https://helm.sh) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation and getting started guide for Helm. Serves as the authoritative resource for understanding chart anatomy, template engines, and client commands, ensuring standardization in continuous integration pipelines.
###### Tutorials

  - **(2021)** [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introductory video course establishing foundational Kubernetes packaging concepts. Covers basic chart configuration, deployment lifecycles, and initial client interactions to transition from manual manifests to structured releases.
  - **(2020)** [thoughtworks.com: Helm](https://www.thoughtworks.com/radar/tools/helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A professional evaluation of Helm from ThoughtWorks Technology Radar. While earlier iterations (Helm v2) posed architectural concerns due to the elevated privileges of Tiller, Helm v3's client-only architecture secures its position as a stable choice for Kubernetes deployment standardization.
##### Helm Hooks

  - **(2021)** [rafay.co: Helm Chart Hooks Tutorial](https://rafay.co/ai-and-cloud-native-blog/helm-chart-hooks-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive breakdown of Helm lifecycle hooks (e.g., pre-install, post-upgrade). Explains how to coordinate prerequisite checks, execute database migrations, or trigger custom operations outside of standard deployment routines.
##### Helm Migration

  - **(2020)** [helm.sh: How to migrate from Helm v2 to Helm v3](https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Standardized blueprint detailing the technical steps to transition environments from Helm v2 to Helm v3. Focuses on state-store conversion (ConfigMaps/Secrets), Tiller cleanup, and avoiding release disruption during metadata migrations.
##### Introductory

  - **(2021)** [freecodecamp.org: What is a Helm Chart? A Tutorial for Kubernetes Beginners](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive beginner tutorial exploring Helm fundamentals. Translates Kubernetes packaging logic into relatable analogies and guides developers through editing templates and launching basic infrastructure releases.
  - **(2021)** [thedeveloperstory.com: Helm 101: Brief introduction to kubernetes package manager](https://thedeveloperstory.com/2021/07/12/helm-101-brief-introduction-to-kubernetes-package-manager)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Fundamental introduction outlining the role of Helm in managing the complexity of Kubernetes infrastructure. Discusses key files (values.yaml, templates directory) and common installation command sequences.
  - **(2021)** [mattias.engineer/courses/kubernetes/helm: Kubernetes-101: Helm 🌟](https://mattias.engineer/courses/kubernetes/helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive instructional module exploring basic and intermediate Helm tasks. Integrates localized labs covering chart structuring, release revisions management, and customized CLI command execution.
  - **(2020)** [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — High-level overview of Helm's architecture and its role in scaling Kubernetes software rollouts. Walks developers through how template definitions replace raw YAML, reducing repetitive work and config drift across microservices.
  - **(2020)** [dev.to: Introduction to Helm 🌟](https://dev.to/leading-edje/introduction-to-helm-50jl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical introduction outlining the foundational structure of Helm charts, releases, and CLI workflows. Discusses core mechanics of template compilation and value injection for developers new to Kubernetes package management.
#### Testing

##### Unit Testing

  - **(2021)** [blog.heyal.co.uk: How to unit-test your helm charts with Golang 🌟](https://blog.heyal.co.uk/unit-testing-helm-charts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep technical look into executing unit testing on Helm chart outputs using Go tests instead of simple bash scripts. Ensures template logic parses properly and conforms to runtime requirements prior to deploy.
### Cloud Platforms

#### Azure AKS

##### Helm Integration (1)

  - **(2022)** [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Integration guide demonstrating the deployment of multi-tier applications onto Azure Kubernetes Service (AKS) using Helm. Clarifies Managed Identity setups and DevOps pipelines optimized for cloud-native workloads.
### Continuous Delivery

#### Gitops

##### Hashicorp Waypoint

  - **(2021)** [**learn.hashicorp.com: Deploy a Helm-based application automatically with GitOps**](https://github.com/hashicorp/waypoint/tree/main/website/content/docs) <span class='md-tag md-tag--info'>⭐ 4727</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-29d81a2f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 5 L 20 7 L 30 12 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-29d81a2f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical guide deploying Helm-based software within HashiCorp Waypoint pipelines. Compares native Waypoint continuous operations with declarative GitOps reconciliations, establishing streamlined automation protocols.
##### Helm Integration (2)

  - **(2021)** [codefresh.io: Using Helm with GitOps 🌟](https://octopus.com/blog/using-helm-with-gitops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the synergies and friction points of matching the declarative GitOps model with Helm's transactional release engine. Recommends strategies for separating configuration definitions from package logic.
##### Red Hat Openshift

  - **(2021)** [youtube: GitOps Guide to the Galaxy: Working with Helm](https://www.youtube.com/watch?v=1FzOlSed5ts&ab_channel=OpenShift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video detailing best practices when pairing Helm with GitOps engines (such as Argo CD). Investigates template-rendering synchronization patterns, managing secret encryption, and maintaining single-source-of-truth states in git.
#### Helm Integration (3)

  - **(2022)** [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual and technical walkthrough illustrating the orchestration of continuous delivery models with Helm. Emphasizes declarative rollouts, blue-green strategy alignment, and handling configurations inside unified CI/CD systems.
### Continuous Integration

#### CICD

##### Jenkins

  - **(2021)** [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates rapid bootstrap of a Jenkins-driven CI/CD workflow utilizing Helm charts for packaging. Showcases how automation systems leverage the Helm CLI to rapidly package, version, and deploy builds into target namespaces.
### Enterprise Platforms

#### Red Hat Openshift (1)

##### Certifications

  - **(2021)** [redhat.com: Red Hat OpenShift Certification extends support for Kubernetes-native technologies with Helm 🌟](https://www.redhat.com/en/blog/red-hat-openshift-certification-extends-support-kubernetes-native-technologies-helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Press release outlining Red Hat's native support and certification paths for Helm charts in OpenShift. Reinforces Helm's status as a first-class citizen in Enterprise hybrid-cloud orchestration frameworks.
##### Microservices

  - **(2021)** [developers.redhat.com: Deploy Node.js applications to Red Hat OpenShift with Helm](https://developers.redhat.com/articles/2021/07/20/deploy-nodejs-applications-red-hat-openshift-helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hands-on guide focusing on containerizing and deploying Node.js microservices to OpenShift 4 using Helm charts. Covers localized template customization and resource quota alignments for developer-driven environments.
### Infrastructure

#### Cost Optimization

##### Temporary Environments

  - **(2021)** [dev.to: Helm Release Time-To-Live(TTL)⏳💀 for Temporary Environments](https://dev.to/rtpro/helm-release-time-to-livettl-for-temporary-environments-1239)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines techniques to implement a TTL (Time-To-Live) mechanism for Helm releases. Crucial for optimizing cloud spend in ephemeral testing environments by garbage-collecting resources after pre-defined lifetimes.
### Observability

#### Prometheus Integration

##### Metrics

  - **(2021)** [blog.knell.it: Making your Helm Chart observable for Prometheus](https://christianhuth.de/making-your-helm-chart-observable-for-prometheus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to embed ServiceMonitor or PodMonitor definitions natively into Helm templates. Simplifies application observability by automatically registering target resources for Prometheus scraping post-deployment.
### Reliability

#### Post-mortems

##### Deployment Failures

  - **(2021)** [dev.to/francoislp: Post-mortem: 1h30 downtime on a Saturday morning](https://dev.to/francoislp/post-mortem-1h30-downtime-on-a-saturday-morning-5af0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Real-world operational post-mortem detailing high-severity production downtime triggered by a silent failure in a Helm upgrade. Explains the critical importance of dry-runs, strict testing, and canary stages for chart deployment.
### Security

#### Hardening

##### Helm Security

  - **(2021)** [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://www.suse.com/c/rancher_blog/create-reproducible-security-in-kubernetes-with-helm-3-and-helm-charts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical guide discussing Helm 3 security baselines, image registry verification, and using secure defaults in charts. Addresses how declarative configurations align with modern threat model structures inside production networks.
##### Sysdig Standards

  - **(2021)** [sysdig.com: Helm security and best practices](https://www.sysdig.com/blog/how-to-secure-helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hardening guidelines detailing secure Helm usage. Discusses securing helm charts against common configuration risks, managing credentials in secret layers instead of source files, and verifying container images in pipeline states.
#### Vulnerabilities

##### Argo CD Security

  - **(2022)** [apiiro.com: Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments](https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Crucial security report highlighting vulnerabilities where malicious or compromised Helm charts exploit the template-rendering engine of GitOps systems (like Argo CD) to expose sensitive secrets or execute side-channel attacks.
##### CVE-2021-32690

  - **(2021)** [thenewstack.io: Upgrade Helm if You Don’t Want to Share Your Username and Password (Helm’s CVE-2021-32690) 🌟](https://thenewstack.io/upgrade-helm-if-you-dont-want-to-share-your-username-and-password)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Critical analysis of Helm security vulnerability CVE-2021-32690. Investigates how auth credentials could be inadvertently leaked to third-party domains during chart installations, emphasizing immediate upgrades to safe client versions.
## Cloud Native Architecture

### Development Methodologies

#### Operator Perspectives

  - **(2021)** [opensource.com: What Kubernetes taught me about development](https://opensource.com/article/21/12/kubernetes-developer) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural reflection detailing key developer-centric shifts encountered when adapting to Kubernetes environments. It explores paradigms like declarative APIs, container-first test loops, and how platform engineers must redefine application boundaries in microservice environments.
## Infrastructure As Code

### Helm (3)

#### Prometheus Deployment

  - **(2023)** [Setup Prometheus Using Helm Chart on Kubernetes](https://devopscube.com/setup-prometheus-helm-chart) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide on installing a production-ready Prometheus instance into Kubernetes using Helm. Explains configuring persistent storage claims, setting retention policies, and overriding default ingress objects.
## Kubernetes Tools

### General Reference

  - [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: managing helm releases the gitops way in the Kubernetes Tools ecosystem.
  - [dzone: 15 useful helm chart tools](https://dzone.com/articles/15-useful-helm-charts-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: 15 useful helm chart tools in the Kubernetes Tools ecosystem.
  - [dzone: create install upgrade and rollback a helm chart - part 1](https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: create install upgrade and rollback a helm chart - part 1 in the Kubernetes Tools ecosystem.
  - [dzone: cicd with kubernetes and helm](https://dzone.com/articles/cicd-with-kubernetes-and-helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: cicd with kubernetes and helm in the Kubernetes Tools ecosystem.
  - [cncf.io: Add Java Agents to Existing Kubernetes and Helm Applications Instantly](https://www.cncf.io/blog/2021/03/24/add-java-agents-to-existing-kubernetes-and-helm-applications-instantly)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io: Add Java Agents to Existing Kubernetes and Helm Applications Instantly in the Kubernetes Tools ecosystem.
## Multi-cluster Management

### Project Sveltos

#### Validation Tools

  - **(2025)** [github.com/projectsveltos: sveltosctl](https://github.com/projectsveltos/sveltosctl) <span class='md-tag md-tag--info'>⭐ 36</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e7d8570d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 10 L 20 8 L 30 13 L 40 12 L 50 6" fill="none" stroke="url(#spark-grad-e7d8570d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The CLI dashboard for Project Sveltos. It specializes in executing dry-runs and drift validations on declarative ClusterProfiles to ensure configuration validity prior to propagating resources to remote edge clusters.
## Networking and Ingress

### Ingress Controllers

#### Haproxy Deployments

  - **(2026)** [artifacthub.io: Official Helm charts for HAProxy and the HAProxy Kubernetes Ingress Controller on Artifact Hub 🌟](https://artifacthub.io/packages/search?repo=haproxytech) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official, production-grade Helm packages for HAProxy load balancers and Ingress Controllers. They offer high-performance routing, custom security profiles, proxy-protocol support, and robust SSL/TLS termination configs suitable for web traffic at scale.
## Observability (1)

### Scraping and Exporters

#### Kubernetes Exporters

  - **(2023)** [==sstarcher/helm-exporter==](https://github.com/sstarcher/helm-exporter) <span class='md-tag md-tag--info'>⭐ 301</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-150b93f1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 8 L 20 10 L 30 6 L 40 7 L 50 7" fill="none" stroke="url(#spark-grad-150b93f1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A Prometheus exporter designed to surface real-time metrics for deployed Helm releases. It monitors charts metadata, tracking status, revisions, and health states across namespaces to empower advanced alert rules.
## Observability and Monitoring

### Prometheus Ecosystem

#### Helm Deployments

  - **(2026)** [prometheus-community.github.io: Prometheus Community Kubernetes Helm Charts 🌟](https://prometheus-community.github.io/helm-charts) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official Prometheus community Helm charts registry, housing the essential kube-prometheus-stack. This remains the absolute industry standard for managing Prometheus, Grafana dashboards, Alertmanager definitions, and metrics-collector sidecars.
## Platform Engineering

### Application Delivery (2)

#### Catalog UI

  - **(2025)** [==kubeapps.dev 🌟==](https://kubeapps.dev) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A web-based control plane for deploying and managing packaged cloud-native applications on Kubernetes. Provides visual tooling to interact with Helm charts, Operators, and Carvel packages with integrated RBAC and multi-cluster deployment scopes.
### Kubernetes Gitops and Packaging

#### Alternative Deployment Engines

  - **(2026)** [**Nelm: A Helm Alternative for Kubernetes Deployments**](https://github.com/werf/nelm) <span class='md-tag md-tag--info'>⭐ 1083</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-842b63c3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 3 L 20 11 L 30 9 L 40 9 L 50 4" fill="none" stroke="url(#spark-grad-842b63c3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A high-performance deployment engine embedded in Werf that provides a drop-in, robust alternative to standard Helm tracking. It addresses Helm's native state validation limitations by offering deep, real-time resource validation and status monitoring.
#### Auditing and Maintenance

  - **(2025)** [github: Nova 🌟](https://github.com/fairwindsops/nova) <span class='md-tag md-tag--info'>⭐ 864</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-66197f0b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 4 L 20 6 L 30 6 L 40 11 L 50 4" fill="none" stroke="url(#spark-grad-66197f0b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A critical cluster auditing utility that proactively scans running environments for outdated, insecure, or orphaned Helm releases. It cross-references current cluster deployments against upstream registries to alert operators of crucial patch requirements.
  - **(2024)** [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog) <span class='md-tag md-tag--info'>⭐ 43</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3fd8f2a0" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 3 L 20 9 L 30 7 L 40 5 L 50 8" fill="none" stroke="url(#spark-grad-3fd8f2a0)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A smart CLI helper designed to parse git commit logs and automatically compile detailed changelogs for Helm releases. Ideal for maintaining human-readable release histories without manual maintenance bottlenecks during major release cycles.
#### Best Practices (1)

  - **(2022)** [boxunix.com: Developer’s Guide to Writing a Good Helm Chart](https://boxunix.com/2022/02/05/developers-guide-to-writing-a-good-helm-chart) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive authoring guide establishing best practices in Helm chart architecture. Topics include variable scoping, values encapsulation patterns, schema validation structures, and managing complex multi-service subchart dependencies cleanly.
#### Chart Discovery

  - **(2026)** [==Artifact Hub 🌟==](https://artifacthub.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The authoritative, CNCF-hosted decentralized web hub designed for discovering, installing, and monitoring cloud-native packages. It aggregates active Helm charts, Kubernetes operators, Tekton tasks, and OCI artifacts with comprehensive security and maintenance tracking.
  - **(2020)** [codeengineered.com: 4 Places To Find Helm Charts](https://codeengineered.com/blog/2020/helm-find-charts) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical landscape overview detailing key public repositories and search indexes for sourcing verified Helm charts. This serves as a foundational reference for understanding the historical transition from disparate registries to modern unified catalogs.
#### Chart Publishing

  - **(2022)** [harness.io: Tutorial: Turning a GitHub Repo Into a Helm Chart Repo](https://www.harness.io/blog/helm-chart-repo) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical hands-on tutorial demonstrating how to turn a standard GitHub repository into a fully compliant Helm Chart registry. It outlines automating publishing workflows utilizing GitHub Pages, Chart Releaser Actions, and package distribution.
#### Chart Repositories

  - **(2024)** [JFrog ChartCenter](https://chartcenter.io) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A legacy public Helm registry launched by JFrog to provide security insights, dependency maps, and automated vulnerability scanning for Helm packages. It serves as a historical architectural reference for secure dependency-chain structures.
  - **(2020)** [New Location For Stable and Incubator Charts](https://helm.sh/blog/new-location-stable-incubator-charts) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — The landmark Helm blog announcement detailing the official deprecation and migration path of the legacy 'stable' and 'incubator' Helm repositories. This resource documents the organizational move toward decentralized chart ownership and independent project hosting.
#### Compliance and Validation

  - **(2025)** [redhat-certification: chart-verifier: Rules based tool to certify Helm charts' 🌟](https://github.com/redhat-certification/chart-verifier) <span class='md-tag md-tag--info'>⭐ 61</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f4733b0c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 11 L 20 7 L 30 4 L 40 10 L 50 9" fill="none" stroke="url(#spark-grad-f4733b0c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's policy-enforcement checker built to certify Helm charts for enterprise deployment suitability on OpenShift platforms. It verifies that packaging templates align with platform standards, security models, and compliance benchmarks.
#### DevOps Pipelines

  - **(2025)** [Codecentric Jenkins 🌟](https://github.com/codecentric/helm-charts) <span class='md-tag md-tag--info'>⭐ 733</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-666f0a29" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 12 L 20 3 L 30 2 L 40 11 L 50 9" fill="none" stroke="url(#spark-grad-666f0a29)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active, community-maintained collection of high-quality Helm charts, featuring a robust configuration path for DevOps tooling like Jenkins. It provides clean, production-ready, security-hardened manifests optimized for enterprise use.
#### Helm Documentation

  - **(2025)** [**helm-docs**](https://github.com/norwoodj/helm-docs) <span class='md-tag md-tag--info'>⭐ 1745</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-18db4b03" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 13 L 20 13 L 30 5 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-18db4b03)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An automated utility designed to generate clear Markdown documentation from Helm chart metadata and schema structures. By analyzing values.yaml schema annotations, it produces clean, standardized configuration tables. This ensures chart configurations remain self-documenting and structurally valid within CI/CD pipelines.
#### Helm Plugins and Extensibility

  - **(2026)** [**Helm Diff Plugin 🌟**](https://github.com/databus23/helm-diff) <span class='md-tag md-tag--info'>⭐ 3447</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-38140098" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 7 L 20 6 L 30 4 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-38140098)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The essential Helm plugin that compares proposed templates with running cluster releases to output an exact color-coded unified diff. A foundational safety gate for continuous delivery, mitigating unexpected state drifts during upgrades.
  - **(2022)** [datree.io: How to build a Helm plugin in minutes](https://www.datree.io/resources/how-to-build-a-helm-plugin-in-minutes) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A developer-oriented guide outlining how to design, build, and distribute custom Helm plugins. The tutorial covers the CLI plugin contract, execution hook hooks, environment runtime variables, and best practices for extending Helm with customized subcommands.
#### Helm Templates

  - **(2025)** [HULL](https://github.com/vidispine/hull) <span class='md-tag md-tag--info'>⭐ 288</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-387b3077" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 8 L 20 5 L 30 11 L 40 6 L 50 11" fill="none" stroke="url(#spark-grad-387b3077)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The Helm Utility Library Layer (HULL) is an innovative templating library designed to drastically reduce boilerplate code. It allows platform engineers to define Kubernetes resources declaratively within JSON/YAML schemas, minimizing redundant YAML scripting.
#### Helm Visualization and UI

  - **(2025)** [**github.com/komodorio/helm-dashboard 🌟**](https://github.com/komodorio/helm-dashboard) <span class='md-tag md-tag--info'>⭐ 5716</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-78253049" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 3 L 20 7 L 30 5 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-78253049)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A real-time web UI dashboard tailored for managing, upgrading, and viewing Helm releases. It addresses the visibility gap for platform operators by facilitating live drift visualization, schema validation, and multi-version revision comparisons directly from a user-friendly browser interface.
#### Java Microservices

  - **(2022)** [openshift.com: Introducing the Quarkus Helm Chart](https://www.redhat.com/en/blog/introducing-the-quarkus-helm-chart) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction detailing the design of the Quarkus Helm Chart, optimized for cloud-native Java microservices. It highlights native compiling integrations, GraalVM deployment profiles, and how to harness OpenShift pipelines for highly efficient container bootstrapping.
#### Learning Hubs

  - **(2025)** [Red Hat Training & Certification Community](https://access.redhat.com/community/learn) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's official training ecosystem community. It offers platform operators, architects, and developers verified learning pathways, course materials, and labs covering OpenShift administration and cloud-native practices.
#### Legacy Charts

  - **(2020)** [==Jenkins==](https://github.com/helm/charts/tree/master/stable/jenkins) <span class='md-tag md-tag--info'>⭐ 15424</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0436d7b7" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 2 L 20 9 L 30 13 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-0436d7b7)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — The deprecated stable Helm chart repository for Jenkins. It is strongly recommended to avoid this legacy version, as active development and security patches have transitioned exclusively to the official Jenkins community repository on Artifact Hub.
#### Legacy Utilities

  - **(2021)** [github.com/mumoshu/helm-x: Helm X Plugin](https://github.com/mumoshu/helm-x) <span class='md-tag md-tag--info'>⭐ 178</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-5721e3c6" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 11 L 20 4 L 30 12 L 40 4 L 50 11" fill="none" stroke="url(#spark-grad-5721e3c6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — An experimental Helm plugin developed to extend standard chart templates with custom scripting functions and enhanced lifecycle control. This project is now unmaintained, serving purely as a design blueprint.
  - **(2021)** [maorfr/helm-backup: Helm Backup Plugin](https://github.com/maorfr/helm-backup) <span class='md-tag md-tag--info'>⭐ 83</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6ddc120b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 2 L 20 3 L 30 5 L 40 11 L 50 11" fill="none" stroke="url(#spark-grad-6ddc120b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early state backup plugin designed to preserve localized copies of active Helm releases. Modern declarative GitOps frameworks (such as Argo CD or Flux) have made manual stateful backups obsolete.
  - **(2021)** [Kubecrt](https://github.com/blendle/kubecrt) <span class='md-tag md-tag--info'>⭐ 113</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-89cf1f12" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 5 L 20 13 L 30 6 L 40 5 L 50 8" fill="none" stroke="url(#spark-grad-89cf1f12)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — An archived, early-stage conversion utility built to convert Helm charts into raw Kubernetes manifests. This project has been fully superseded by standard native capabilities like 'helm template' and is preserved solely as a historical reference of early declarative rendering strategies.
  - **(2019)** [github.com/jkosik: helm-decomposer](https://github.com/jkosik/helm-decomposer) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — An archived utility that parsed static Kubernetes manifests to automatically generate modular Helm charts. Unmaintained for several years, it serves as a legacy proof-of-concept for automated chart generation.
#### Multi-chart Orchestration

  - **(2026)** [==github.com/helmfile/helmfile==](https://github.com/helmfile/helmfile) <span class='md-tag md-tag--info'>⭐ 5136</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4af64d8c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 4 L 20 8 L 30 12 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-4af64d8c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier declarative orchestrator for multi-chart environments. Helmfile allows infrastructure-as-code developers to build multi-environment states, map release hierarchies, automate parameter layering, and enforce GitOps deployment sequences seamlessly.
  - **(2025)** [**Helmsman: Helm Charts as Code 🌟**](https://github.com/mkubaczyk/helmsman) <span class='md-tag md-tag--info'>⭐ 1498</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bfe13c2e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 3 L 20 5 L 30 2 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-bfe13c2e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An enterprise-grade, GitOps-friendly engine for declaring Helm charts as code. By monitoring desired state files, it automates lifecycle tasks including installations, cross-cluster upgrades, namespace setup, and purging deprecated releases.
  - **(2026)** [helmwave/helmwave](https://github.com/helmwave/helmwave) <span class='md-tag md-tag--info'>⭐ 886</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4ca013b4" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 8 L 20 13 L 30 8 L 40 4 L 50 6" fill="none" stroke="url(#spark-grad-4ca013b4)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> — An emerging orchestrator implementing a 'Docker Compose' deployment feel for Helm charts. Featuring parallel execution plans, strict dependency resolution, and declarative configs, it offers platform teams a robust multi-chart orchestration tool.
#### Orchestration Utilities

  - **(2021)** [github: Kubernetes Deployment Orchestrator](https://github.com/SAP-archive/kubernetes-deployment-orchestrator) <span class='md-tag md-tag--info'>⭐ 11</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f6c134e5" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 10 L 20 4 L 30 12 L 40 13 L 50 11" fill="none" stroke="url(#spark-grad-f6c134e5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An archived, experimental orchestrator developed by SAP to coordinate complex Helm releases and dependency chains across large multi-tenant landscapes. Kept strictly as a historic design blueprint for modular platform workflows.
#### Secrets Management

  - **(2024)** [tellerops/helm-teller](https://github.com/tellerops/helm-teller) <span class='md-tag md-tag--info'>⭐ 69</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bd39b76a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 10 L 20 5 L 30 5 L 40 7 L 50 8" fill="none" stroke="url(#spark-grad-bd39b76a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly specialized security plugin that interfaces with vault and KMS solutions to fetch secret values dynamically during deployment runtime. It eliminates the risk of committing sensitive configuration details to public code repositories.
#### Security and Auditing

  - **(2023)** [helm-scanner](https://github.com/bridgecrewio/helm-scanner) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight template vulnerability scanner that evaluates Helm manifests for potential security drift, secrets leaks, and misconfigurations prior to deployment. Often integrated early in pipeline testing stages.
## Security and Compliance

### Policy Enforcement

#### Datree Integration

  - **(2022)** [aws.amazon.com: Preventing Kubernetes misconfigurations using Datree](https://aws.amazon.com/blogs/containers/preventing-kubernetes-misconfigurations-using-datree) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS technical write-up detailing the configuration of Datree policies inside Amazon EKS clusters to catch security and configuration drift. It details automated testing strategies to block misconfigured resource manifests at pre-commit and pipeline execution gates.

---
💡 **Explore Related:** [AWS Pricing](./aws-pricing.md) | [Cloud Asset Inventory](./cloud-asset-inventory.md) | [Cloud Arch Diagrams](./cloud-arch-diagrams.md)

🔗 **See Also:** [Ansible](./ansible.md) | [AWS Storage](./aws-storage.md)

