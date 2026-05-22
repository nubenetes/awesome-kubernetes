# Helm

!!! info "Architectural Context"
    Detailed reference for Helm in the context of Architectural Foundations.

## Application Delivery

### Helm (1)

#### Alternative Engines

  - **(2025)** [**Nelm: A Helm Alternative for Kubernetes Deployments**](https://github.com/werf/nelm) <span class='md-tag md-tag--info'>⭐ 1072</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An innovative deployment engine integrated within the Werf workflow that functions as an alternative to native Helm release tracking. It resolves Helm's tracking limitations by ensuring strict live cluster validation and resource health monitoring.
#### Developer Experience

  - **(2021)** [opensource.com: What Kubernetes taught me about development](https://opensource.com/article/21/12/kubernetes-developer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A retrospective engineering article summarizing lessons learned from building and deploying microservices on Kubernetes. It highlights the paradigm shift of treating infrastructure-as-code and configuration as vital parts of the software lifecycle.
#### Documentation

  - **(2025)** [==helm-docs==](https://github.com/norwoodj/helm-docs) <span class='md-tag md-tag--info'>⭐ 1740</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry standard utility that auto-generates Markdown documentation from Helm chart metadata and variables files. It reads 'values.yaml' schema annotations to generate detailed configuration tables, ensuring precise, up-to-date documentation.
  - **(2021)** [chart-doc-gen: Helm Chart Documentation Generator](https://github.com/kubepack/chart-doc-gen) <span class='md-tag md-tag--info'>⭐ 122</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated CLI utility for generating Markdown documentation automatically from Helm 'values.yaml' files. It streamlines package maintenance by keeping user-facing parameter catalogs perfectly aligned with template configurations.
  - **(2023)** [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog) <span class='md-tag md-tag--info'>⭐ 43</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A CLI utility designed to automatically assemble neat changelogs for Helm charts by parsing git repository commit history. It simplifies publishing notes by keeping track of charts updates over multiple releases.
#### Governance

  - **(2025)** [**github: Nova 🌟**](https://github.com/fairwindsops/nova) <span class='md-tag md-tag--info'>⭐ 860</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A valuable auditing tool that scans running Kubernetes clusters for outdated Helm releases. It cross-references deployed charts with upstream versions to ensure administrators maintain robust patch levels and security updates.
  - **(2024)** [redhat-certification: chart-verifier: Rules based tool to certify Helm charts 🌟](https://github.com/redhat-certification/chart-verifier) <span class='md-tag md-tag--info'>⭐ 61</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's automated verification tool built to certify that third-party Helm charts align with platform standards on OpenShift. It performs automated checks against strict deployment policies and security guidelines.
#### Learning Paths

  - **(2023)** [**mattias.engineer/courses/kubernetes/helm: Kubernetes-101: Helm 🌟**](https://mattias.engineer/courses/kubernetes/helm) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational course module mapping out Helm architecture, release lifecycles, and template syntax. It serves as an optimal starting point for operators transitioning from static manifests to dynamic Kubernetes packaging.
#### Legacy Charts

  - **(2020)** [==Jenkins==](https://github.com/helm/charts/tree/master/stable/jenkins) <span class='md-tag md-tag--info'>⭐ 15415</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The historic Helm chart repository location for Jenkins under the official Helm org. This template configuration has since been migrated to the Jenkins community repository and should be avoided in favor of modern forks.
#### Legacy Integration

  - **(2018)** [Kubecrt](https://github.com/blendle/kubecrt) <span class='md-tag md-tag--info'>⭐ 113</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — An early-stage, archived utility developed to convert Helm charts into raw Kubernetes manifests. While superseded by standard native features like 'helm template', it remains a historic reference for early manifest-rendering strategies.
#### Lifecycle

  - **(2023)** [rafay.co: Helm Chart Hooks Tutorial](https://rafay.co/ai-and-cloud-native-blog/helm-chart-hooks-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical tutorial detailing the execution phases of Helm chart hooks (such as pre-install, post-upgrade, and test actions). It demonstrates how to cleanly orchestrate database migrations and validation routines within application lifecycles.
  - **(2020)** [itnext.io: Database migrations on Kubernetes using Helm hooks](https://itnext.io/database-migrations-on-kubernetes-using-helm-hooks-fb80c0d97805)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An actionable production playbook detailing how to coordinate database schema upgrades prior to application deployment using Helm release hooks. It discusses failure rollbacks and job design patterns for modern pipelines.
#### Observability

  - **(2024)** [sstarcher/helm-exporter](https://github.com/sstarcher/helm-exporter) <span class='md-tag md-tag--info'>⭐ 298</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Prometheus exporter designed to surface real-time metrics for deployed Helm releases. It monitors charts metadata, tracking status, revisions, and health states across namespaces to empower advanced alert rules.
  - **(2022)** [blog.knell.it: Making your Helm Chart observable for Prometheus](https://christianhuth.de/making-your-helm-chart-observable-for-prometheus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical engineering guide detailing how to expose Prometheus metrics from custom Helm charts. It explores configuring PodMonitors and ServiceMonitors directly within Chart templates to guarantee day-2 observability out of the box.
#### Orchestration

  - **(2026)** [==github.com/helmfile/helmfile==](https://github.com/helmfile/helmfile) <span class='md-tag md-tag--info'>⭐ 5107</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A critical declarative wrapper that allows operators to deploy multi-chart environments as a unified, version-controlled system. Helmfile handles dependencies, value layering, and state synchronization across multiple environments with ease.
  - **(2024)** [**Helmsman: Helm Charts as Code 🌟**](https://github.com/mkubaczyk/helmsman) <span class='md-tag md-tag--info'>⭐ 1495</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An advanced tool designed to manage Helm releases declaratively as code. Supporting GitOps principles, Helmsman processes desired state files to automatically update, clean, or track installations across dynamic clusters.
  - **(2021)** [github: Kubernetes Deployment Orchestrator](https://github.com/SAP-archive/kubernetes-deployment-orchestrator) <span class='md-tag md-tag--info'>⭐ 11</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — An early experimental orchestrator from SAP for coordinating complex Kubernetes and Helm release sequences. The repository has been archived and is kept solely for historic exploration of modular cluster orchestration.
#### Plugins and Extensions

  - **(2025)** [==Helm Diff Plugin 🌟==](https://github.com/databus23/helm-diff) <span class='md-tag md-tag--info'>⭐ 3429</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A high-utility Helm extension to render exact resource differences between operational releases. Highly recommended for avoiding deployment accidents and executing reliable continuous deliveries.
  - **(2024)** [**Helm mapkubeapis Plugin**](https://github.com/helm/helm-mapkubeapis) <span class='md-tag md-tag--info'>⭐ 1034</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A crucial maintenance tool that maps deprecated or removed Kubernetes API versions to supported equivalents in Helm release metadata. This plugin avoids release lockups during major cluster upgrades where APIs are retired.
  - **(2021)** [JovianX/helm-release-plugin](https://github.com/JovianX/helm-release-plugin) <span class='md-tag md-tag--info'>⭐ 109</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight plugin to facilitate Helm release management, providing extra commands to inspect, export, and manipulate releases. It simplifies operations for cluster administrators dealing with multi-release drift.
  - **(2021)** [datree.io: How to build a Helm plugin in minutes](https://www.datree.io/resources/how-to-build-a-helm-plugin-in-minutes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured developer guide that walks through the anatomy of Helm's plugin architecture. It provides an actionable walkthrough on packaging custom scripts as first-class CLI extensions, enhancing operational customizability.
#### Registries


??? abstract "Architect's Technical Comparison Table"
    | Solution | Maturity | Primary Focus | Language | Stars |
    | :--- | :--- | :--- | :--- | :--- |
    | [Bitnami Helm Charts](https://bitnami.com/stacks?stack=helm) |  | Registries | English | 🌟🌟🌟🌟🌟 |
    | [Artifact Hub 🌟](https://artifacthub.io) |  | Registries | English | 🌟🌟🌟🌟🌟 |
    | [prometheus-community.github.io: Prometheus Community Kubernetes Helm Charts 🌟](https://prometheus-community.github.io/helm-charts) |  | Registries | English | 🌟🌟🌟🌟🌟 |
    | [Codecentric Jenkins 🌟](https://github.com/codecentric/helm-charts) |  | Registries | English | 🌟🌟🌟🌟 |
    | [artifacthub.io: Official Helm charts for HAProxy and the HAProxy Kubernetes Ingress Controller on Artifact Hub 🌟](https://artifacthub.io/packages/search?repo=haproxytech) |  | Registries | English | 🌟🌟🌟🌟 |
    | [Choerodon Nexus3 🌟](https://artifacthub.io/packages/helm/choerodon/nexus3) |  | Registries | English | 🌟🌟🌟 |

  - **(2026)** [==Bitnami Helm Charts==](https://bitnami.com/stacks?stack=helm) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier source for hardened, production-ready application and database Helm charts. Kept strictly up-to-date, Bitnami's repository provides secure, multi-architecture-supported templates for enterprise stack deployment.
  - **(2026)** [==Artifact Hub 🌟==](https://artifacthub.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The CNCF-backed global registry for finding, installing, and publishing Kubernetes packages. It features integrated vulnerability scanning, deprecation warnings, and multi-repository searching, cementing its role as the industry's default search directory.
  - **(2026)** [==prometheus-community.github.io: Prometheus Community Kubernetes Helm Charts 🌟==](https://prometheus-community.github.io/helm-charts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The absolute source of truth for deploying Prometheus, Grafana, and Alertmanager inside Kubernetes clusters. This community-maintained hub provides standard Helm configurations for complete cloud-native observability.
  - **(2025)** [**Codecentric Jenkins 🌟**](https://github.com/codecentric/helm-charts) <span class='md-tag md-tag--info'>⭐ 728</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly maintained community Helm chart collection containing reliable configurations for DevOps tools like Jenkins. It is widely recommended for active cluster operations, offering secure, production-hardened manifests.
  - **(2025)** [**artifacthub.io: Official Helm charts for HAProxy and the HAProxy Kubernetes Ingress Controller on Artifact Hub 🌟**](https://artifacthub.io/packages/search?repo=haproxytech) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The authoritative collection of Helm charts for deploying the HAProxy Load Balancer and Kubernetes Ingress Controller. These enterprise-stable manifests offer optimal performance-tuning settings out of the box.
  - **(2024)** [Choerodon Nexus3 🌟](https://artifacthub.io/packages/helm/choerodon/nexus3) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active Helm package designed to configure and orchestrate Sonatype Nexus3 instances. It handles data persistence, ingress routing, and performance tuning configurations optimized for enterprise container workloads.
  - **(2020)** [hub.helm.sh 🌟](http://hub.helm.sh) 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — The historic original central repository for discovering Helm charts, now deprecated and redirected to Artifact Hub. It served as the initial hub for the community-led standardization of cloud-native package publishing.
  - **(2022)** [JFrog ChartCenter](https://chartcenter.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — JFrog's central repository designed to offer security-vetted and rich-metadata indexing for public Helm charts. Although largely integrated into newer Artifactory offerings, it serves as an early reference for enterprise security proxying.
  - **(2022)** [openshift.com: Introducing the Quarkus Helm Chart](https://www.redhat.com/en/blog/introducing-the-quarkus-helm-chart)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Red Hat announcement showcasing the specialized Helm chart for Quarkus Java microservices. It explores how this chart streamlines the build-to-deploy pipeline, highlighting native compilation support for Kubernetes targets.
  - **(2021)** [harness.io: Tutorial: Turning a GitHub Repo Into a Helm Chart Repo](https://www.harness.io/blog/helm-chart-repo)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step CI/CD tutorial showing how to host a lightweight private Helm chart repository using GitHub Pages and Chart Releaser. It is ideal for teams wanting internal chart distribution without standing up heavy artifactory services.
  - **(2020)** [codeengineered.com: 4 Places To Find Helm Charts](https://codeengineered.com/blog/2020/helm-find-charts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A reference article identifying leading public and private directories for sourcing Helm charts. It helps developers locate stable, community-vetted charts, bridging the gap before major consolidation initiatives like Artifact Hub.
  - **(2020)** [New Location For Stable and Incubator Charts](https://helm.sh/blog/new-location-stable-incubator-charts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official blog announcement detailing the deprecation timeline of the old stable/incubator chart repositories. It describes the migration path toward distributed hosting on GitHub Pages and private charts registries.
#### Security

  - **(2022)** [**thenewstack.io: Applying Kubernetes Security Best Practices to Helm Charts 🌟**](https://thenewstack.io/applying-kubernetes-security-best-practices-to-helm-charts) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly recommended security framework guide highlighting practices such as enforcing non-root execution, defining CPU/Memory limits, and utilizing RBAC minimal privileges within Helm manifests. It bridges the gap between raw templating and hardened production standards.
  - **(2023)** [tellerops/helm-teller](https://github.com/tellerops/helm-teller) <span class='md-tag md-tag--info'>⭐ 69</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized plugin built to secure sensitive parameters inside charts by pulling secrets directly from cloud secret managers (such as HashiCorp Vault or AWS Secrets Manager) during deployment execution.
  - **(2022)** [helm-scanner](https://github.com/bridgecrewio/helm-scanner) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A template security scanning utility that parses Helm charts to detect security misconfigurations, vulnerability signatures, and compliance policy violations. It acts as an early gate tool in CI/CD developer pipelines.
  - **(2022)** [aws.amazon.com: Preventing Kubernetes misconfigurations using Datree](https://aws.amazon.com/blogs/containers/preventing-kubernetes-misconfigurations-using-datree)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An authoritative AWS guide introducing Datree integrations for preventing misconfigurations within Helm deployment cycles. It details how to set up policy validation within EKS pipelines to block non-compliant resources before deployment.
#### Templating

  - **(2024)** [HULL](https://github.com/vidispine/hull) <span class='md-tag md-tag--info'>⭐ 288</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A unique template library extension designed to drastically reduce boilerplate in Helm development. HULL enables declarative, object-oriented configuration structures, letting developers generate entire charts with minimal template overhead.
  - **(2022)** [boxunix.com: Developer’s Guide to Writing a Good Helm Chart](https://boxunix.com/2022/02/05/developers-guide-to-writing-a-good-helm-chart)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive guide outline covering best practices in writing high-quality Helm charts. It addresses templates organization, variable naming conventions, semantic schema formatting, and validation practices.
  - **(2020)** [itnext.io: Helm: reusable chart — named templates, and a generic chart for multiple applications](https://itnext.io/helm-reusable-chart-named-templates-and-a-generic-chart-for-multiple-applications-13d9b26e9244) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive article addressing advanced Go template techniques in Helm, specifically targeting the creation of reusable library charts. It offers a blueprint for building a single, highly flexible parent chart that can deploy diverse microservice patterns.
#### Visualization

  - **(2024)** [==github.com/komodorio/helm-dashboard 🌟==](https://github.com/komodorio/helm-dashboard) <span class='md-tag md-tag--info'>⭐ 5695</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A robust, user-friendly web UI for viewing, installing, and managing Helm releases in real-time. It enables operators to easily track installed packages, compare release revisions, and visualize values drift without relying on the command line.
  - **(2024)** [Helm Kanvas Snapshot](https://github.com/meshery-extensions/helm-kanvas-snapshot) <span class='md-tag md-tag--info'>⭐ 35</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extension designed to capture visual topology snapshots of Helm releases within Meshery. It allows operators to visually audit and document the runtime architecture generated by complex multi-tier Helm installations.
## Application Delivery and GitOps

### Package Management

#### Advanced Helm Patterns

  - **(2022)** [**dev.to: Helm Release Time-To-Live(TTL)⏳💀 for Temporary Environments**](https://dev.to/rtpro/helm-release-time-to-livettl-for-temporary-environments-1239) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical implementation patterns for enforcing a Time-To-Live (TTL) on Helm releases. Crucial technique for cleaning up dynamic, ephemeral preview environments automatically.
  - **(2021)** [**blog.flant.com: Making the most out of Helm templates 🌟**](https://palark.com/blog/advanced-helm-templating) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep architectural guide focused on unlocking Go template capabilities in Helm. Teaches loop logic, conditional scopes, and standard library variables for highly dynamic charts.
  - **(2020)** [**itnext.io: Helm 3 Umbrella Charts & Standalone Chart Image Tags — An Alternative Approach**](https://itnext.io/helm-3-umbrella-charts-standalone-chart-image-tags-an-alternative-approach-78a218d74e2d) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Architectural deep-dive illustrating the 'Umbrella Charts' pattern. Solves image-tag syncing issues in large microservice landscapes by overriding nested parameters from a root deployment chart.
  - **(2020)** [**itnext.io: Reference Other Values in Helm Chart Values File**](https://itnext.io/reference-other-values-in-helm-chart-values-file-19d44d9276c7) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide showing how to reference values dynamically within the same `values.yaml` file, minimizing data duplication across multi-environment Helm releases.
#### Case Studies

  - **(2022)** [**dev.to/francoislp: Post-mortem: 1h30 downtime on a Saturday morning**](https://dev.to/francoislp/post-mortem-1h30-downtime-on-a-saturday-morning-5af0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A detailed post-mortem documenting a 1.5-hour system outage caused by conflicting Helm upgrades and state locks, with valuable architectural takeaways on configuring proper timeouts.
#### Educational Videos


??? abstract "Architect's Technical Comparison Table"
    | Solution | Maturity | Primary Focus | Language | Stars |
    | :--- | :--- | :--- | :--- | :--- |
    | [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng) |  | Educational Videos | English | 🌟🌟🌟🌟 |
    | [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8) |  | Educational Videos | English | 🌟🌟🌟🌟 |
    | [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4) |  | Educational Videos | English | 🌟🌟🌟 |
    | [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w) |  | Educational Videos | English | 🌟🌟🌟 |
    | [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o) |  | Educational Videos | English | 🌟🌟🌟 |
    | [youtube.com: Demystifying Helm 🌟](https://www.youtube.com/watch?v=2HPsPOwHOlY&ab_channel=DonovanBrown) |  | Educational Videos | English | 🌟🌟🌟 |

  - **(2021)** [**Delve into Helm: Advanced DevOps**](https://www.youtube.com/watch?v=cZ1S2Gp47ng) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Advanced video deep-dive exploring Helm's Go-templating mechanisms, advanced parameter isolation, and complex dependency structures in enterprise pipeline environments.
  - **(2020)** [**Continuously delivering apps to Kubernetes using Helm**](https://www.youtube.com/watch?v=CmPK93hg5w8) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Webinar showing best practices for continuous delivery of multi-tier workloads to Kubernetes using Helm. Explains how to integrate Helm lifecycle hooks into CI/CD loops.
  - **(2020)** [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Introductory video tutorial explaining Helm's packaging abstractions including charts, templates, releases, and repositories. Great entry point for beginners learning declarative deployments.
  - **(2019)** [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Screencast guiding developers through setting up a declarative Jenkins pipeline that automatically packages and deploys microservices to Kubernetes using Helm.
  - **(2018)** [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — DevOps video showcasing integration between Azure Pipelines, Azure Kubernetes Service (AKS), and Helm. Shows how to structure multi-environment releases smoothly.
  - **(2018)** [youtube.com: Demystifying Helm 🌟](https://www.youtube.com/watch?v=2HPsPOwHOlY&ab_channel=DonovanBrown) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical video breakdown demystifying how Helm operates. Explains basic mechanics of building templates and decoupling dynamic configurations from application specifications.
#### GitOps and Helm

  - **(2021)** [**youtube: GitOps Guide to the Galaxy: Working with Helm**](https://www.youtube.com/watch?v=1FzOlSed5ts&ab_channel=OpenShift) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — OpenShift GitOps instructional video exploring Helm usage inside GitOps systems like Argo CD. Discusses reconciliation pipelines, helm templates, and automated cluster sync mechanics.
  - **(2020)** [**codefresh.io: Using Helm with GitOps 🌟**](https://octopus.com/blog/using-helm-with-gitops) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analysis of integrating Helm templates with GitOps deployments, showing how to balance templated application metadata packaging with strict, declarative environment state tracking.
#### Helm (2)


??? abstract "Architect's Technical Comparison Table"
    | Solution | Maturity | Primary Focus | Language | Stars |
    | :--- | :--- | :--- | :--- | :--- |
    | [helm.sh](https://helm.sh) |  | Helm | English | 🌟🌟🌟🌟🌟 |
    | [GitHub: Helm, the Kubernetes Package Manager](https://github.com/helm/helm) |  | Helm | English | 🌟🌟🌟🌟🌟 |
    | [thoughtworks.com: Helm](https://www.thoughtworks.com/radar/tools/helm) |  | Helm | English | 🌟🌟🌟🌟🌟 |
    | [freecodecamp.org: What is a Helm Chart? A Tutorial for Kubernetes Beginners](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners) |  | Helm | English | 🌟🌟🌟 |
    | [thedeveloperstory.com: Helm 101: Brief introduction to kubernetes package manager](https://thedeveloperstory.com/2021/07/12/helm-101-brief-introduction-to-kubernetes-package-manager) |  | Helm | English | 🌟🌟🌟 |
    | [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2) |  | Helm | English | 🌟🌟🌟 |
    | [dev.to: Introduction to Helm 🌟](https://dev.to/leading-edje/introduction-to-helm-50jl) |  | Helm | English | 🌟🌟🌟 |

  - **(2026)** [==helm.sh==](https://helm.sh) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The main landing site for Helm, containing foundational documentation, API schemas, and architecture overviews. The ultimate hub for engineers developing or consuming Kubernetes chart templates.
  - **(2026)** [==GitHub: Helm, the Kubernetes Package Manager==](https://github.com/helm/helm) <span class='md-tag md-tag--info'>⭐ 29830</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Authoritative GitHub repository for Helm. With over 29k stars and massive community backing, it is the primary source of truth for the project's codebase, releases, and development.
  - **(2020)** [==thoughtworks.com: Helm==](https://www.thoughtworks.com/radar/tools/helm) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Thoughtworks Technology Radar page validating Helm's position as the primary package manager for Kubernetes. Underlines how the server-side removal (Tiller) in Helm v3 fundamentally resolved security risks.
  - **(2021)** [freecodecamp.org: What is a Helm Chart? A Tutorial for Kubernetes Beginners](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comprehensive beginner's tutorial detailing the directory structures and YAML formats of Helm. Offers hands-on exercises for authoring and deploying custom application templates.
  - **(2021)** [thedeveloperstory.com: Helm 101: Brief introduction to kubernetes package manager](https://thedeveloperstory.com/2021/07/12/helm-101-brief-introduction-to-kubernetes-package-manager) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An ultra-focused 101 guide explaining the core structures of Helm charts. Highlights essential commands and structure conventions to quickly onboard teams.
  - **(2020)** [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — High-level overview illustrating the synergies between Kubernetes architectures and Helm's package abstractions, demonstrating how Helm reduces manual configuration drift.
  - **(2020)** [dev.to: Introduction to Helm 🌟](https://dev.to/leading-edje/introduction-to-helm-50jl) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Accessible and clear introduction detailing core Helm entities (charts, repositories, releases). Excellent read for cloud engineers looking to grasp basic Helm vocabulary quickly.
#### Helm Best Practices

  - **(2020)** [**jfrog.com: Steering Straight with Helm Charts Best Practices 🌟**](https://jfrog.com/blog/helm-charts-best-practices) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — JFrog's blueprint on production Helm chart development. Recommends strategies for structured defaults, semantic versioning rules, and secure enterprise registry publishing.
  - **(2020)** [**codersociety.com: 13 Best Practices for using Helm**](https://codersociety.com/blog/articles/helm-best-practices) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curation of 13 battle-tested engineering guidelines for authoring Helm Charts. Covers formatting patterns, values mapping, naming rules, and GitOps integration schemas.
#### Helm Migration

  - **(2019)** [**helm.sh: How to migrate from Helm v2 to Helm v3**](https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Official migration blueprint from Helm's core team detailing the path from v2 to v3. Shows how to securely convert in-cluster release metadata and fully decommission the Tiller component.
#### Helm Security

  - **(2022)** [**apiiro.com: Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments**](https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Vulnerability report showcasing how malicious Helm charts could be engineered to exfiltrate secret resources from Argo CD controller pods. Important reading for platform hardening.
  - **(2022)** [**sysdig.com: Helm security and best practices**](https://www.sysdig.com/blog/how-to-secure-helm) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Sysdig engineering guide for securing Helm charts. Teaches vulnerability scanning of templates, access control limits for chart operations, and runtime monitoring of helm releases.
  - **(2021)** [**thenewstack.io: Upgrade Helm if You Don’t Want to Share Your Username and Password (Helm’s CVE-2021-32690) 🌟**](https://thenewstack.io/upgrade-helm-if-you-dont-want-to-share-your-username-and-password) 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Security breakdown analyzing CVE-2021-32690, where Helm leaked sensitive credential headers during remote chart requests. Critical warning illustrating why regular client patching is necessary.
  - **(2020)** [**rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts**](https://www.suse.com/c/rancher_blog/create-reproducible-security-in-kubernetes-with-helm-3-and-helm-charts) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical security overview emphasizing reproducible chart security patterns using validation schemas, signed values, and limited-scope Service Accounts.
#### Helm Testing

  - **(2020)** [**blog.heyal.co.uk: How to unit-test your helm charts with Golang 🌟**](https://blog.heyal.co.uk/unit-testing-helm-charts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Advanced engineering guide showing how to unit-test Helm templates using Golang. Demonstrates programmatically generating manifests and asserting correct outputs before deploying.
  - **(2022)** [dev.to: HULL Tutorial 01: Introducing HULL, the Helm Universal Layer Library](https://dev.to/gre9ory/hull-tutorial-01-introducing-hull-the-helm-universal-layer-library-4njb) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduction to HULL (Helm Universal Layer Library), showing how it abstracts boilerplate Helm templates via standard JSON/YAML schema specifications, facilitating dynamic chart generation.
#### Helm Validation

  - **(2020)** [**Helm 3: Validating Helm Chart Values with JSON Schemas 🌟**](https://www.arthurkoziel.com/validate-helm-chart-values-with-json-schemas) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Excellent technical guide showing how to write and use JSON Schema (`values.schema.json`) to programmatically validate Helm Chart variables and eliminate formatting errors prior to deploy.
#### Helm vs Operators

  - **(2020)** [**cloud.redhat.com: Application Management in Kubernetes Environments with Helm Charts and Kubernetes Operators**](https://www.redhat.com/en/blog/application-management-in-kubernetes-environments-with-helm-charts-and-kubernetes-operators) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Architectural discussion comparing Helm package templates with Kubernetes Operators. Outlines when to use Helm for Day 1 installs versus Operators for stateful Day 2 operations.
#### OpenShift Integration

  - **(2021)** [**developers.redhat.com: Deploy Node.js applications to Red Hat OpenShift with Helm**](https://developers.redhat.com/articles/2021/07/20/deploy-nodejs-applications-red-hat-openshift-helm) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Developer-centric walkthrough for wrapping Node.js applications into compliant Helm charts for OpenShift deployment, showing the end-to-end development-to-production lifecycle.
  - **(2020)** [**redhat.com: Red Hat OpenShift Certification extends support for Kubernetes-native technologies with Helm 🌟**](https://www.redhat.com/en/blog/red-hat-openshift-certification-extends-support-kubernetes-native-technologies-helm) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Red Hat blog announcing extended, first-class Helm integration in OpenShift. Discusses Console-level management of Helm charts, ensuring enterprise-compliant application lifecycles.
#### Waypoint

  - **(2022)** [**learn.hashicorp.com: Deploy a Helm-based application automatically with GitOps**](https://github.com/hashicorp/waypoint/tree/main/website/content/docs) <span class='md-tag md-tag--info'>⭐ 4730</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — HashiCorp walkthrough presenting continuous, declarative deployment of Helm-based apps using Waypoint pipelines, highlighting structural GitOps workflows.
## Edge Computing

### IoT and Smart Home

#### Surveillance

  - **(2024)** [Frigate](https://frigate.readthedocs.io/en/latest) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highly specialized NVR software focusing on local real-time object detection using AI accelerators. Its reference Helm and Kubernetes guides allow developers to scale home automation and security workloads on private clusters.
## Infrastructure as Code

### Kubernetes Package Management

#### Deconstruction

  - **(2018)** [github.com/jkosik: helm-decomposer](https://github.com/jkosik/helm-decomposer) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — An early utility designed to deconstruct static Kubernetes manifests into modular Helm templates. The project has had no active maintenance for years, serving purely as a conceptual legacy archive.
#### Helm GitOps

  - **(2025)** [**helmwave/helmwave**](https://github.com/helmwave/helmwave) <span class='md-tag md-tag--info'>⭐ 885</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Helmwave acts as a docker-compose-like manager for Helm charts. It offers structured multi-chart deployments, parallel releases, and strict dependency trees, representing a strong emerging pattern for platform team orchestration.
#### Helm Plugins

  - **(2020)** [github.com/mumoshu/helm-x: Helm X Plugin](https://github.com/mumoshu/helm-x) <span class='md-tag md-tag--info'>⭐ 178</span> 🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Helm X is an experimental plugin extending Helm capabilities with enhanced templating features. While originally useful, modern Helm development has rendered this tool obsolete, and lack of active commits makes it a legacy reference.
  - **(2019)** [maorfr/helm-backup: Helm Backup Plugin](https://github.com/maorfr/helm-backup) <span class='md-tag md-tag--info'>⭐ 83</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A legacy Helm backup plugin designed to preserve state. Modern GitOps workflows with declarative tools like Argo CD and Flux have deprecated the need for manual, stateful Helm backups.
## Multi-Cluster Management

### Cluster Governance

#### Sveltos

  - **(2025)** [github.com/projectsveltos: sveltosctl](https://github.com/projectsveltos/sveltosctl#display-outcome-of-clusterprofiles-in-dryrun-mode) <span class='md-tag md-tag--info'>⭐ 36</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — sveltosctl provides command-line control over Project Sveltos. It excels at dry-run validations of ClusterProfiles, ensuring declarative configurations are verified prior to production propagation.

---
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Cheatsheets](./cheatsheets.md) | [Linux](./linux.md)

