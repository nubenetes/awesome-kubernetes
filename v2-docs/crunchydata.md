---
description: "Top Crunchydata resources for 2026, AI-ranked: crunchy-pgadmin4, pgAdmin 4 and more — curated Cloud Native tools, guides and references."
---
# Crunchy Data PostgreSQL Operator

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/crunchydata/).

!!! info "Architectural Context"
    Detailed reference for Crunchy Data PostgreSQL Operator in the context of Data & Advanced Analytics.

## Application Development

### Python

#### Object-relational Mapping

  - **(2021)** [info.crunchydata.com: Composite Primary Keys, PostgreSQL and Django](https://www.crunchydata.com/blog/composite-primary-keys-postgresql-and-django) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses the implementation limits of compound primary keys within Django ORM integration when using PostgreSQL. Explains mapping workarounds, schema-migration patterns, and clean architecture solutions.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - **(None)** [](https://www.slideshare.net/slideshow/operating-postgresql-at-scale-with-kubernetes-137132067/137132067)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.slideshare.net in the Kubernetes Tools ecosystem.
  - [dzone: PostgreSQL HA and Kubernetes](https://dzone.com/articles/postgresql-ha-and-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: PostgreSQL HA and Kubernetes in the Kubernetes Tools ecosystem.
  - [ref3](https://dzone.com/articles/understanding-openshift-security-context-constrain)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ref3 in the Kubernetes Tools ecosystem.
## Cloud Native

### GKE

#### Postgresql Operator

  - **(2020)** [info.crunchydata.com: Deploying the PostgreSQL Operator on GKE](https://www.crunchydata.com/blog/install-postgres-operator-kubernetes-on-gke-ansible) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Teaches the deployment process of the Crunchy PostgreSQL Operator onto Google Kubernetes Engine (GKE) clusters using automated Ansible playbooks. Details storage class mappings and GKE-specific identity policies.
### Kubernetes Operators

#### Legacy Operators

  - **(2018)** [Youtube: Crunchy PostgreSQL Operator for Kubernetes 3.4 Overview (2018)](https://www.youtube.com/watch?v=gaXlrlz7GVc) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstration video analyzing Crunchy PostgreSQL Operator version 3.4 patterns. Focuses on dynamic scale-out configurations, primary-replica promotion mechanics, and native command-line interface (pgo CLI) structures.
  - **(2017)** [Youtube: Demo of Crunchy Data Postgres Operator v1.0.0 (2017)](https://www.youtube.com/watch?v=HX10WWTRiTY) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical video demonstration of the first public iteration (v1.0.0) of the Crunchy PostgreSQL Operator. Illustrates raw container deployments and early persistent volume claim configurations under primitive Kubernetes schemas.
#### Multi-tenancy

  - **(2020)** [thenewstack.io: Advanced Kubernetes Namespace Management with the PostgreSQL Operator 🌟](https://thenewstack.io/advanced-kubernetes-namespace-management-with-the-postgresql-operator) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyses advanced namespace orchestration patterns utilizing the Crunchy PostgreSQL Operator. Walks through configuring security boundaries and multi-tenant isolation policies across multiple database instances.
#### Postgresql Operator (1)

  - **(2020)** [info.crunchydata.com: Crunchy PostgreSQL for Kubernetes 4.3 Released](https://www.crunchydata.com/news/crunchy-postgresql-for-kuberenetes-4.3) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Release analysis profiling Crunchy PostgreSQL Operator v4.3. Highlights enhancements such as automated multi-namespace support, security context constraints, and integrated pgAdmin deployment patterns.
  - **(2020)** [postgresql.org: Crunchy PostgreSQL Operator 4.5: Enhanced Monitoring, Custom Annotations, PostgreSQL 13 🌟](https://www.postgresql.org/about/news/crunchy-postgresql-operator-45-enhanced-monitoring-custom-annotations-postgresql-13-2086) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Community release documentation of Crunchy PostgreSQL Operator v4.5. Focuses on support configurations for PostgreSQL 13, pod custom annotations, and major Prometheus exporter stack upgrades.
  - **(2019)** [crunchydata blog: What's New in Crunchy PostgreSQL Operator 4.0](https://www.crunchydata.com/blog/crunchy-postgres-kubernetes-operator-4.0) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Archival post announcing the release of Crunchy PostgreSQL Operator v4.0. Highlights early custom resource design paradigms, scaling improvements, and the transition of core tasks toward Patroni and pgBackRest systems.
#### Postgresql Scaling

  - **(2019)** [opensource.com: Scaling PostgreSQL with Kubernetes Operators 🌟](https://opensource.com/article/19/2/scaling-postgresql-kubernetes-operators) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the technical theory of the Kubernetes Operator pattern applied to database state management. Illustrates how operators capture advanced human tasks like database scaling, backups, and minor migrations.
### Kubernetes Storage

#### Rook Ceph

  - **(2021)** [info.crunchydata.com: Using the PostgreSQL Operator with Rook Ceph Storage](https://www.crunchydata.com/blog/crunchy-postgresql-operator-with-rook-ceph-storage) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural integration review detailing the implementation of Rook Ceph storage solutions to back Crunchy PostgreSQL Operator deployments. Analyzes performance characteristics, scale configurations, and replication safety parameters.
### Openshift

#### High Availability

  - **(2020)** [youtube: OCB: High Availability PostgreSQL and more on OpenShift - Jonathan Katz (Crunchy Data) 🌟](https://www.youtube.com/watch?v=9jbR9lZuSU0) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video presentation exploring the deployment of enterprise-grade, highly-available PostgreSQL patterns on OpenShift using Patroni. Analyzes storage profiles, automated routing, and backup schedules.
#### Operator Lifecycle Manager

  - **(2019)** [Youtube: OpenShift Meetup Tokyo #05 - Operator and Operator Lifecycle Manager on OpenShift (2019, openshift 4.1)](https://www.youtube.com/watch?v=X4vuktlK0Tg) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical deep dive from a Tokyo meetup illustrating deployment workflows with Operator Lifecycle Manager (OLM) on OpenShift 4.1. Describes package manifest curation and cross-namespace operator scheduling controls.
#### Postgresql Operator (2)

  - **(2020)** [info.crunchydata.com: Getting Started with PostgreSQL Operator 4.3 in OpenShift](https://www.crunchydata.com/blog/getting-started-with-postgresql-operator-4.3-in-openshift) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An identical operational reference detailing step-by-step procedures to provision PostgreSQL Operator 4.3 instances inside secure, multi-tenant OpenShift execution clusters.
### Postgresql

#### Backup and Recovery

  - **(2021)** [info.crunchydata.com: pgBackRest - Performing Backups on a Standby Cluster](https://www.crunchydata.com/blog/pgbackrest-performing-backups-on-a-standby-cluster) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An optimization manual guiding configuration patterns to run resource-heavy pgBackRest backup jobs directly from standby replicas, minimizing performance degradation on primary database targets.
  - **(2020)** [info.crunchydata.com: Scheduled PostgreSQL Backups and Retention Policies with Kubernetes](https://www.crunchydata.com/blog/schedule-postgresql-backups-and-retention-with-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details declarative backup execution schemas and Point-in-Time Recovery (PITR) configurations using pgBackRest within the operator framework. Highlights bucket retention controls and storage backup tier optimizations.
#### Container Images

  - **(2026)** [Documentation: Crunchy Data Container Suite 🌟](https://access.crunchydata.com/documentation/crunchy-postgres-containers/latest) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highly detailed documentation defining construction parameters for Crunchy Data's hardened database container images. Covers security boundaries, pgBackRest, Patroni integrations, and environment variable configuration sets.
#### High Availability (1)

  - **(2021)** [info.crunchydata.com: Deploy High-Availability PostgreSQL Clusters on Kubernetes by Example](https://www.crunchydata.com/blog/deploy-high-availability-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A complete operational blueprint detailing high-availability PostgreSQL configurations. Uses Patroni and distributed consensus backends to prevent split-brain issues, orchestrate automated failover scenarios, and manage virtual IPs.
#### Kubernetes Deployment

  - **(2018)** [slideshare.net: Deploying PostgreSQL on Kubernetes](https://www.slideshare.net/vyruss000/deploying-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical presentation reviewing early-generation deployment techniques of running stateful PostgreSQL relational databases within dynamic, ephemeral Kubernetes pods, noting historical volume storage limits and lifecycle challenges.
## Container Orchestration

### Docker Swarm

#### Postgresql Deployment

  - **(2019)** [info.crunchydata.com: An Easy Recipe for Creating a PostgreSQL Cluster with Docker Swarm](https://www.crunchydata.com/blog/an-easy-recipe-for-creating-a-postgresql-cluster-with-docker-swarm) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical tutorial outlining containerized high-availability PostgreSQL configurations using Docker Swarm. Covers Swarm Secrets, internal routing, and environment setup paradigms.
## Data Infrastructure

### Bare Metal Provisioning

#### Kubernetes Installation

  - **(2021)** [blog.crunchydata.com: Kubernetes + Postgres Cluster From Scratch on Rocky 8](https://www.crunchydata.com/blog/kube-cluster-from-scratch-on-rocky-8) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A duplicate guide mapping out Rocky Linux 8 operating system optimization, package registration, Kubeadm installation, and operator provisioning. It emphasizes disk partition strategies and container runtime configurations that ensure stable I/O performance (IOPS) required for heavy, production-grade stateful workloads.
### Database Operators

#### Postgresql (1)

##### Backup and Recovery (1)

  - **(2020)** [blog.crunchydata.com: Announcing Google Cloud Storage (GCS) Support for pgBackRest](https://www.crunchydata.com/blog/announcing-google-cloud-storage-gcs-support-for-pgbackrest) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the integration of Google Cloud Storage (GCS) as a native backup target for pgBackRest within the Postgres operator ecosystem. Extending storage targets beyond traditional AWS S3 endpoints enables resilient multi-cloud disaster recovery options. The architecture leverages high-throughput GCS API calls for reliable, low-overhead transaction log archiving.
  - **(2020)** [blog.crunchydata.com: pgBackRest Point-In-Time Recovery Using Crunchy PostgreSQL Operator](https://www.crunchydata.com/blog/pgbackrest-point-in-time-recovery-using-crunchy-postgresql-operator) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines point-in-time recovery (PITR) workflows using the integrated pgBackRest utility in Crunchy PostgreSQL Operator environments. Modern disaster recovery plans require precise WAL replay capabilities to minimize recovery point objectives (RPO). This guide explains how to define backup targets and restore parameters declaratively inside the operator CRD.
##### Connection Pooling

  - **(2021)** [blog.crunchydata.com: Your Guide to Connection Management in Postgres 🌟](https://www.crunchydata.com/blog/your-guide-to-connection-management-in-postgres) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep dive into connection management architectures, specifically focusing on PgBouncer configurations managed by PostgreSQL operators. Because microservice application scaling leads to volatile client connection counts, using an intermediate pooler prevents PostgreSQL server resource exhaustion. Incorporating poolers is a fundamental requirement to maintain query performance at scale.
##### Database Administration

  - **(2020)** [crunchy-pgadmin4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/container-specifications/crunchy-pgadmin4) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details container specification sheets for the crunchy-pgadmin4 image, including configuration variables and resource layouts. Historically, pgAdmin 4 was manually provisioned as a containerized sidecar or standalone service to provide database GUIs (Curator Insight). Current deployment strategies prefer integrated, operator-managed tooling and secure proxy pipelines.
  - **(2020)** [pgAdmin 4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/examples/administration/pgadmin4) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines early configuration models and environment mappings for pgAdmin 4 instances running in Kubernetes clusters. This resource demonstrates how to configure volume mounts and ingress rules for user sessions. For modern enterprise production, automated telemetry models (Prometheus/Grafana) are prioritized over graphical administrative consoles.
##### Developer Experience

  - **(2021)** [blog.crunchydata.com: Announcing Postgres Container Apps: Easy Deploy Postgres Apps](https://www.crunchydata.com/blog/announcing-postgres-container-apps-easy-deploy-postgres-apps) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Postgres Container Apps, a set of templated blueprints designed to simplify database-backed service deployments on Kubernetes. Standard database integrations often suffer from environmental schema synchronization and secret-mounting failures. These starter packs align service-to-database interfaces, improving local debugging and automated delivery pipelines.
##### Gitops Implementation

  - **(2021)** [info.crunchydata.com: Using GitOps to Self-Manage Postgres in Kubernetes 🌟](https://www.crunchydata.com/blog/gitops-postgres-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Integrates declarative GitOps workflows (e.g., ArgoCD/Flux) with the Crunchy Postgres Operator on Kubernetes. Contrasting early manual operator deployments (Curator Insight) with modern automated synchronization loops (Live Grounding), this architecture pattern establishes highly auditable, automated database provisioning. This ensures database configuration and storage states reconcile transparently with git-defined manifests.
##### High Availability (2)

  - **(2021)** [blog.crunchydata.com: Active-Active PostgreSQL Federation on Kubernetes](https://www.crunchydata.com/blog/active-active-postgres-federation-on-kubernetes) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Investigates architectural techniques for implementing active-active PostgreSQL database federation on top of Kubernetes. While active-passive replication is the standard for high availability (Curator Insight), active-active multi-region federation delivers massive read/write scalability at the cost of complex conflict resolution (Live Grounding). This represents an emerging frontier for global cloud-native systems.
##### Installation

  - **(2020)** [The PostgreSQL Operator Installer with kubectl](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/postgres-operator) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Documents installation paths for Crunchy PostgreSQL Operator v4.3.0, mapping Bash-based installations and Ansible playbooks. While highly detailed during early operator adoption (Curator Insight), these manual installation mechanisms and custom CLI commands have been deprecated in modern, helm-driven operator ecosystems (Live Grounding). It is retained only for historical system maintenance.
##### Multi-cluster

  - **(2021)** [blog.crunchydata.com: Multi-Kubernetes Cluster PostgreSQL Deployments](https://www.crunchydata.com/blog/multi-kubernetes-cluster-postgresql-deployments) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores deploying PostgreSQL clusters that span across multiple independent Kubernetes control planes. By configuring cross-cluster network routes, this design establishes highly resilient disaster recovery sites capable of handling total region outages. Live production systems frequently pair this multi-cluster layout with Service Meshes to guarantee secure cross-site database replication.
##### Packaging and CD

  - **(2021)** [blog.crunchydata.com: Helm, GitOps and the Postgres Operator](https://www.crunchydata.com/blog/gitops-postgres-kubernetes-helm) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to package the Crunchy Postgres Operator using Helm charts integrated directly within automated GitOps pipelines. By mapping Helm template parameters to GitOps controller environments, it overcomes traditional Helm hook limitations for stateful workloads. Modern production standards leverage this setup to seamlessly deploy database custom resource definitions (CRDs) across multi-tenant clusters.
##### Performance Tuning

  - **(2021)** [blog.crunchydata.com: Query Optimization in Postgres with pg_stat_statements](https://www.crunchydata.com/blog/tentative-smarter-query-optimization-in-postgres-starts-with-pg_stat_statements) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to optimize database execution patterns within Kubernetes using the `pg_stat_statements` extension. Modern PostgreSQL operators inject this utility by default, exposing run-time metrics directly to telemetry agents. This programmatic feedback loop provides platform engineers with the real-time query analysis required to automate index tuning and limit resource bottlenecks.
##### Platform Integration

  - **(2020)** [youtube: Install and use Crunchy PostgreSQLfor OpenShift operator for simple todo app on OpenShift 🌟](https://www.youtube.com/watch?v=9wuUXi6Qbis&ab_channel=MichaelBornholdtNielsen) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical video guide detailing the deployment of the Crunchy PostgreSQL Operator on Red Hat OpenShift to power a simple containerized web application. This walkthrough illustrates basic operator setup and pod status validation through the console interface. While useful for rapid developer prototyping, production installations bypass manual UI clicks in favor of declarative GitOps workflows.
  - **(2019)** [Crunchy PostgreSQL and Openshift](https://www.redhat.com/en/blog/leveraging-the-crunchy-postgresql) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates running Crunchy PostgreSQL Operator inside Red Hat OpenShift, highlighting platform compatibility and enterprise support options. OpenShift's default strict security contexts require deep operator integration to prevent privilege escalation. This study demonstrates the deployment of highly secure, resilient database clusters in enterprise PaaS environments.
##### Release Highlights

  - **(2021)** [blog.crunchydata.com: Crunchy Postgres Operator 4.6.0 🌟](https://www.crunchydata.com/blog/crunchy-postgres-operator-4.6.0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Documents the historical release of Crunchy PostgreSQL Operator v4.6, highlighting improved multi-namespace support and security configurations. Although v4.6 was once touted as the baseline for production readiness (Curator Insight), current cloud-native architecture standards have pivoted entirely to the declarative v5.x operator branch (Live Grounding). It serves primarily as a migration guide for legacy footprints.
  - **(2021)** [blog.crunchydata.com: Next Generation Crunchy Postgres for Kubernetes 5.0 Released](https://www.crunchydata.com/news/next-generation-crunchy-postgres-for-kubernetes-released) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Announces the major architecture redesign of Crunchy Postgres for Kubernetes v5.0, transitioning to a fully declarative reconciliation controller. Unlike legacy v4 versions that required external tools to drive state transitions (Curator Insight), v5 relies entirely on Kubernetes native API constructs to maintain database health (Live Grounding). It is currently the industry-standard version for production PostgreSQL operations.
  - **(2021)** [blog.crunchydata.com: PostgreSQL 14 on Kubernetes (with examples!)](https://www.crunchydata.com/blog/postgresql-14-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Showcases deployment patterns and performance improvements of running PostgreSQL 14 in containerized environments. It highlights scale optimizations, nested JSON enhancements, and parallel query executions. Leveraging modern operators enables painless, declarative major version migrations of active production instances.
##### Scheduling and Affinity

  - **(2020)** [blog.crunchydata.com: Kubernetes Pod Tolerations and Postgres Deployment Strategies 🌟](https://www.crunchydata.com/blog/kubernetes-pod-tolerations-and-postgresql-deployment-strategies) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes Kubernetes scheduling rules, focusing on taints, tolerations, and anti-affinity parameters optimized for PostgreSQL. Placing databases on dedicated hardware isolated from transient application pods is crucial for preserving storage I/O throughput. This redundant guide reiterates the absolute necessity of strict node assignment strategies in production.
##### Security

  - **(2021)** [blog.crunchydata.com: Deploy PostgreSQL With TLS in Kubernetes](https://www.crunchydata.com/blog/set-up-tls-for-postgresql-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates methods for implementing transport layer security (TLS) for PostgreSQL database streams in Kubernetes. Rather than relying on static, manually generated secrets (Curator Insight), live security standards mandate tight integration with Cert-Manager for dynamic, zero-downtime certificate rotation (Live Grounding). This pattern provides robust security compliance necessary for highly regulated microservice networks.
  - **(2021)** [blog.crunchydata.com: Using Cert Manager to Deploy TLS for Postgres on Kubernetes](https://www.crunchydata.com/blog/using-cert-manager-to-deploy-tls-for-postgres-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details how to interface the cert-manager operator with Crunchy PostgreSQL deployments to automate TLS certificate lifecycles. Standardizing certificate issuance and automatic renewal eliminates risks of unexpected database communication outages. It represents a foundational best-practice for zero-trust microservice communications.
##### Source Code

  - **(2026)** [==github.com/CrunchyData/postgres-operator==](https://github.com/CrunchyData/postgres-operator) <span class='md-tag md-tag--info'>⭐ 4421</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-902cdc92" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 11 L 20 3 L 30 3 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-902cdc92)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The main GitHub repository containing the source code for the Crunchy Postgres Operator. Written in Go, this industry-leading project automates the deployment, scaling, failover, backup, and security operations of PostgreSQL instances on Kubernetes. It is actively updated to support modern Kubernetes API standards and enterprise clustering patterns.
##### Storage Management

  - **(2021)** [blog.crunchydata.com: Can't Resize your Postgres Kubernetes Volume? No Problem!](https://www.crunchydata.com/blog/resize-postgres-kubernetes-volume-instance-sets) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Provides architectural workarounds for resizing PostgreSQL storage volumes when utilizing storage backends that do not support dynamic online volume expansion. The guide explains replica-seeding migration techniques that transition primary database roles to new, larger storage instances without downtime. It is a critical operational guide for bare-metal or legacy virtualization footprints.
### Developer Ecosystem

#### Reference Portals

  - **(2021)** [Announcing the Crunchy Data Developer Portal](https://www.crunchydata.com/blog/announcing-the-crunchy-data-developer-portal) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces the launch of Crunchy Data's Developer Portal, serving as an educational hub for running open-source relational databases in containerized ecosystems. It aggregates reference architectures, security practices, and deployment templates. This resource helps bridge the technical gap between software developers and database administrators.
  - **(2021)** [Crunchy Data Developer Portal](https://www.crunchydata.com/developers) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Landing page of the Crunchy Data Developer Portal, providing direct access to technical documentation, integration guides, and training labs. Key modules focus on database scaling, backup retention policies, and high-availability configuration. It acts as a primary hands-on resource for teams transitioning database layers to Kubernetes.
## Database Migration

### Oracle To Postgres

#### Data Architecture

  - **(2020)** [info.crunchydata.com: Migrating from Oracle to PostgreSQL: Tips and Tricks](https://www.crunchydata.com/blog/migrating-from-oracle-to-postgresql-questions-and-considerations) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores schema migration assessments and planning parameters when shifting corporate workloads from Oracle to PostgreSQL. Compares PL/SQL compatibility concerns and procedural data processing workarounds.
#### Migration Tools

  - **(2021)** [info.crunchydata.com: Setup ora2pg for Oracle to Postgres Migration](https://www.crunchydata.com/blog/setup-ora2pg-for-oracle-to-postgres-migration) <span class='md-tag md-tag--warning'>[PERL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep architectural setup guide for the open-source ora2pg utility. Teaches migration assessment score compilation, dynamic PL/SQL function translation, and automated data copy operations.
## Databases

### Postgresql (2)

#### Data Ingestion

  - **(2020)** [info.crunchydata.com: Fast CSV and JSON Ingestion in PostgreSQL with COPY](https://www.crunchydata.com/blog/fast-csv-and-json-ingestion-in-postgresql-with-copy) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines ingestion optimizations comparing multi-row INSERT patterns against the PostgreSQL COPY command for large CSV and JSON datasets. Includes WAL-bypass guidelines and indexing constraints.
#### Data Replication

  - **(2020)** [info.crunchydata.com: Guard Against Transaction Loss with PostgreSQL Synchronous Replication](https://www.crunchydata.com/blog/synchronous-replication-in-the-postgresql-operator-for-kubernetes-guarding-against-transactions-loss) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the technical trade-offs between asynchronous and synchronous replication profiles within PostgreSQL Kubernetes topologies. Analyzes WAL-level security limits, failover delays, and trade-offs regarding transaction write throughput.
#### Database Administration (1)

  - **(2020)** [info.crunchydata.com: Deploy pgAdmin4 with PostgreSQL on Kubernetes](https://www.crunchydata.com/blog/deploy-pgadmin4-with-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides the deployment of pgAdmin4 web client panels alongside database clusters inside Kubernetes. Reviews network ingress definitions, volume mounts, and credential injection mechanics.
  - **(2020)** [info.crunchydata.com: Quickly Document Your Postgres Database Using psql Meta-Commands](https://www.crunchydata.com/blog/d-meta) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Interactive tutorial on the utilization of native psql meta-commands to rapidly trace schema layouts, inspect index sizes, and generate database structure documentation directly via CLI commands.
#### Developer Tutorials

  - **(2026)** [learn.crunchydata.com 🌟](https://www.crunchydata.com/developers/tutorials) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Interactive educational portal offering structured developer exercises focused on core database engineering. Includes tasks on indexing optimizations, raw performance telemetry, and complex JSON data orchestration strategies in PostgreSQL.
#### Enterprise Solutions

  - **(2026)** [crunchydata.com](https://www.crunchydata.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Corporate entry point for Crunchy Data, a driving force behind enterprise-hardened, fully open-source PostgreSQL. Represents a suite of production support, compliance validation patterns, and cloud-native integration tools.
#### High Availability (3)

  - **(2021)** [info.crunchydata.com: Deploying Active-Active PostgreSQL on Kubernetes](https://www.crunchydata.com/blog/active-active-on-kubernetes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A duplicate evaluation of geographic replication solutions. Contrasts synchronous replication networks with active-active topologies to design low-latency, resilient multi-region database backends.
#### Open Source Repositories

  - **(2026)** [github.com/CrunchyData](https://github.com/CrunchyData) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Central organization repository host for Crunchy Data open-source projects, serving as the development hub for the highly utilized Crunchy PostgreSQL Operator, monitoring dashboards, and hardened container configurations.
#### Performance Tuning (1)

  - **(2021)** [info.crunchydata.com: PostgreSQL Monitoring for Application Developers: The DBA Fundamentals](https://www.crunchydata.com/blog/postgresql-monitoring-for-application-developers-dba-stats) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Bridges developer workflows with DBA database troubleshooting techniques. Teaches query bottlenecks analysis, lock tracing, and execution performance optimizations using pg_stat_activity and pg_stat_statements.
  - **(2021)** [info.crunchydata.com: Tuning Your Postgres Database for High Write Loads](https://www.crunchydata.com/blog/tuning-your-postgres-database-for-high-write-loads) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced tuning walkthrough optimizing engine parameters for write-intensive database profiles. Guides custom values configurations for shared_buffers, max_wal_size, and write-ahead log parameters.
## Observability

### Postgresql (3)

#### Database Monitoring

  - **(2020)** [info.crunchydata.com: Monitoring PostgreSQL clusters in kubernetes](https://www.crunchydata.com/blog/monitoring-postgresql-clusters-in-kubernetes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details structural metric collection architectures for Kubernetes-hosted PostgreSQL. Describes the integration of specialized postgres_exporter containers to feed telemetry into Prometheus targets with visualized dashboard outputs.
  - **(2020)** [info.crunchydata.com: How to Setup PostgreSQL Monitoring in Kubernetes](https://www.crunchydata.com/blog/setup-postgresql-monitoring-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hands-on implementation guide for deploying a scalable monitoring architecture for PostgreSQL. Instructs on integrating postgres_exporter configurations, configuring Prometheus scrape pools, and importing Grafana analytics interfaces.
#### Long-term Storage

  - **(2020)** [info.crunchydata.com: Introducing the Postgres Prometheus Adapter](https://www.crunchydata.com/blog/using-postgres-to-back-prometheus-for-your-postgresql-monitoring-1) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to using the Postgres Prometheus Adapter to store Prometheus time-series metrics. Covers performance metrics, schema structures, and remote-write configurations.
## Platform Security

### Access Control

#### Service Accounts

  - **(2019)** [ref1](https://www.redhat.com/en/blog/understanding-service-accounts-sccs) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains OpenShift Service Accounts, Role-Based Access Control (RBAC), and Security Context Constraints (SCC). Understanding SCCs is vital when deploying complex operators that need custom security postures, such as stateful databases. This reference outlines how to grant specific system permissions safely, protecting multi-tenant clusters from security compromise.

---
💡 **Explore Related:** [Databases](./databases.md) | [Yaml](./yaml.md) | [Message Queue](./message-queue.md)

🔗 **See Also:** [AWS Pricing](./aws-pricing.md) | [Ansible](./ansible.md)

