# Kubernetes Bigdata

!!! info "Architectural Context"
    Detailed reference for Kubernetes Bigdata in the context of The Container Stack.

## Cloud Native AI

### Big Data Orchestration

#### Data Pipelines

  - **(2021)** [hevodata.com: Building Apache Spark Data Pipeline? Made Easy 101 🌟](https://hevodata.com/learn/spark-data-pipeline)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Fundamental guide detailing Apache Spark-based data pipeline creations.
Live Grounding: Explains basic architecture of Spark RDDs, DataFrames, and structural connections required to route data from transactional sources into modern cloud warehouses.
#### Market Surveys

  - **(2021)** [opensourceforu.com: Kubernetes Adoption Widespread for Big Data: Survey](https://www.opensourceforu.com/2021/12/kubernetes-adoption-widespread-for-big-data-survey/?amp)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Survey results discussing the widespread adoption of Kubernetes scheduling for big data workloads.
Live Grounding: Outlines historical transition metrics from static clusters to unified container environments, citing resource efficiency and deployment agility as top motivators.
#### Spark on Kubernetes

  - **(2020)** [itnext.io: Migrating Apache Spark workloads from AWS EMR to Kubernetes](https://itnext.io/migrating-apache-spark-workloads-from-aws-emr-to-kubernetes-463742b49fda) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Technical breakdown of migrating Apache Spark analytics engines from AWS EMR to Kubernetes clusters.
Live Grounding: Deep-dives into memory allocation, dynamic resource allocation, storage mounting, and cost optimizations compared to traditional VM-based EMR setups.
## Data Platforms

### Distributed Processing

#### Apache Spark on Kubernetes

  - **(2023)** [spot.io: Setting up, Managing & Monitoring Spark on Kubernetes](https://www.flexera.com/products/flexera-one/container-optimization)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines workflows for configuring, managing, and tracking Spark applications on Kubernetes. Live Grounding shows Spot's cloud cost-optimization strategies, illustrating how spot instances can be dynamically allocated for ephemeral Spark workers. This guide bridges infrastructure sizing with cost management.
  - **(2022)** [coderstan.com: Apache Spark on Kubernetes—Lessons Learned from Launching Millions of Spark Executors (Databricks Data+AI Summit 2022)](https://coderstan.com/2022/07/15/spark-on-kubernetes-launching-millions-of-spark-executors) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details lessons from Databricks' deployment of millions of Spark executors on Kubernetes. Live Grounding highlights Spark's core challenges in cluster autoscaling and executor lost events. This resource outlines precise architecture patterns to scale heavy data workloads under Kubernetes.
#### Databricks

  - **(2024)** [docs.databricks.com: Use scheduler pools for multiple streaming workloads](https://docs.databricks.com/aws/en/structured-streaming/production) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight explains how to configure fair scheduler pools to run concurrent streaming jobs. Live Grounding verifies that multi-tenant Databricks runtimes require resource isolated scheduler pools to mitigate thread starvation. This documentation provides actionable enterprise patterns for streaming production loads.
  - **(2022)** [aprenderbigdata.com: Databricks: Introducción a Spark en la nube](https://aprenderbigdata.com/databricks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight introduces the core components of the Databricks cloud platform and its managed Spark framework. Live Grounding indicates the rise in Spanish-speaking markets for distributed computing educational paths. This tutorial provides structural steps to deploy first-party data clusters. [SPANISH CONTENT]
#### Databricks Tools

  - **(2024)** [**github.com/databrickslabs/ucx: Databricks Labs UCX**](https://github.com/databrickslabs/ucx) <span class='md-tag md-tag--info'>⭐ 308</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight introduces UCX as a toolset to migrate legacy workspaces to Unity Catalog. Live Grounding validates that Databricks Labs continuously maintains UCX to safely upgrade metastores with metadata isolation. This repository is standard for enterprise migration pipelines.
## Hybrid Cloud and Enterprise

### OpenShift

#### Big Data Workloads

  - **(2020)** [cloud.redhat.com: Getting Started running Spark workloads on OpenShift](https://www.redhat.com/en/blog/getting-started-running-spark-workloads-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Practical guide detailing setup steps for hosting Spark data processors on OpenShift Platform.
Live Grounding: Demystifies user routing, security context constraints, and performance tuning when running containerized Spark clusters on enterprise Red Hat foundations.

---
💡 **Explore Related:** [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md) | [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md)

