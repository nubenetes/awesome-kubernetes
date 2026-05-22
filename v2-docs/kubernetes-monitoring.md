# Kubernetes Monitoring

!!! info "Architectural Context"
    Detailed reference for Kubernetes Monitoring in the context of The Container Stack.

## Observability

### ChatOps

#### Cert-Manager Monitoring

  - **(2022)** [infracloud.io: Monitoring Kubernetes cert-manager Certificates with BotKube](https://www.infracloud.io/blogs/monitoring-kubernetes-cert-manager-certificates) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide for integrating cert-manager with BotKube. Shows how to set up active Slack or Teams alerts that notify platform engineers when TLS certificates are nearing expiration or failing ACME challenges.
### Command Line Tools

#### Kubectl Usage

  - **(2023)** [middlewareinventory.com: Get CPU and Memory Usage of NODES and PODS – Kubectl 🌟](https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A clear, task-focused tutorial demonstrating how to query cluster performance metrics directly using the `kubectl top` command. Explains metrics-server requirements and how to target resource utilization trends across namespaces.
### FinOps

#### Cost Monitoring

##### Prometheus and Grafana

  - **(2023)** [**loft.sh: Kubernetes Cost Monitoring with Prometheus & Grafana**](https://www.vcluster.com/blog/kubernetes-cost-monitoring-with-prometheus-and-grafana) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A FinOps tutorial detailing how to set up cost monitoring dashboards in Kubernetes. Using Prometheus and Grafana, it links CPU and memory metrics to cloud instance pricing sheets to identify underutilized resources.
### Grafana Cloud

#### SaaS Monitoring

##### AWS EKS

  - **(2023)** [youtube.com: Cloud Quick POCs - Kubernetes monitoring metrics using Grafana Cloud on AWS EKS | Observability | Grafana](https://www.youtube.com/watch?v=FVDHWPxK5nU&ab_channel=CloudQuickPOCs) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video guide illustrating the quick setup of AWS EKS cluster metrics tracking using Grafana Cloud. Ideal for engineers seeking a fast SaaS onboarding experience without hosting their own telemetry storage backends.
### Logging

#### Command Line Tools (1)

  - **(2021)** [kubelog.de](https://kubelog.de) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized logging utility designed to simplify container log fetching. Grounding reveals it as a community-driven project that acts as an easy alternative to standard kubectl logs with colorized output.
  - **(2021)** [bul: Interactive TUI for Exploring Kubernetes Container Logs](https://github.com/ynqa/bul) <span class='md-tag md-tag--info'>⭐ 16</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interactive Terminal User Interface (TUI) written in Go for streaming and searching Kubernetes container logs. Grounding suggests that development has stalled (inactive for over 4 years), so while technically functional for local dev, tools like Stern or K9s are preferred in enterprise environments.
#### Concepts

  - **(2022)** [==devopscube.com: Kubernetes Logging Tutorial For Beginners 🌟==](https://devopscube.com/kubernetes-logging-tutorial) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An elite, entry-level tutorial introducing Kubernetes logging paradigms, covering container stdout extraction, cluster-level log architectures, and daemonset collection. Curators praise its lucid diagrams and step-by-step practical commands.
  - **(2021)** [**opensource.com: What you need to know about cluster logging in Kubernetes 🌟**](https://opensource.com/article/21/11/cluster-logging-kubernetes) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides an essential primer on the core Kubernetes logging architecture, explaining stdout/stderr streams, node-level log rotation, and log collector agents. Highly valued for explaining foundational mechanisms before diving into specific tooling.
#### EFK

  - **(2020)** [**digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes**](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A structured, hands-on deployment guide for the classic EFK (Elasticsearch, Fluentd, Kibana) logging stack on Kubernetes. Despite newer logging alternatives, the EFK architecture remains a highly stable and widely documented enterprise standard.
#### Elasticsearch

  - **(2021)** [**elastic.co: How to configure Elastic Cloud on Kubernetes with SAML and hot-warm-cold architecture**](https://www.elastic.co/es/blog/how-to-configure-elastic-cloud-on-kubernetes-with-saml-and-hot-warm-cold-architecture) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A detailed guide on configuring Elastic Cloud on Kubernetes (ECK) featuring single sign-on via SAML and cost-efficient hot-warm-cold storage architectures. Essential for multi-tenant, enterprise security requirements.
#### Operators

  - **(2024)** [**kube-logging/logging-operator**](https://github.com/kube-logging/logging-operator) <span class='md-tag md-tag--info'>⭐ 1696</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A Kubernetes operator designed to manage logging pipelines using Fluentd and Fluent Bit. Provides automated scaling, multi-tenant log isolation, and declarative routing rules, drastically reducing log management complexity.
#### Patterns

  - **(2021)** [dev.to: Kubernetes Practice — Logging with Logstash and FluentD by Sidecar Container](https://dev.to/devopsvn/kubernetes-practice-logging-with-logstash-and-fluentd-by-sidecar-container-16oi) 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A practical walkthrough deploying a sidecar container pattern for log extraction using Logstash and Fluentd. Demonstrates how to ship multi-line log streams from legacy apps that cannot write standard stdout/stderr.
#### Production Architecture

  - **(2021)** [**itnext.io: Kubernetes Logging in Production**](https://itnext.io/kubernetes-logging-in-production-545ea88d9a4a) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Discusses architectural patterns for scale-resilient Kubernetes logging. Compares node-agent logging (DaemonSet) with sidecar injectors, outlining CPU/memory overhead trade-offs for high-volume enterprise traffic.
#### SaaS Logging

  - **(2020)** [papertrail.com: Quick and Easy Way to Implement Kubernetes Logging](https://www.papertrail.com/blog/quick-and-easy-way-to-implement-kubernetes-logging) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides an entry-level walkthrough on configuring Kubernetes container logging to stream directly to SolarWinds Papertrail. Ideal for small-scale projects needing instant search and log aggregation without hosting Elasticsearch.
### Metrics

#### Grafana

  - **(2023)** [grafana.com: A beginner's guide to Kubernetes application monitoring](https://grafana.com/blog/2023/01/31/a-beginners-guide-to-kubernetes-application-monitoring) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Introduces foundational concepts of monitoring applications running inside Kubernetes. It walks through metrics generation, collection using Prometheus, and dashboarding via Grafana. Perfect for engineers getting started with basic application telemetry.
#### Prometheus

  - **(2022)** [==aws.amazon.com: Using Prometheus to Avoid Disasters with Kubernetes CPU Limits 🌟==](https://aws.amazon.com/blogs/containers/using-prometheus-to-avoid-disasters-with-kubernetes-cpu-limits) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A critical engineering guide addressing the dreaded CPU throttling issue in Kubernetes caused by hard CFS limits. Combines Prometheus query analysis with kernel-level metrics to showcase how to balance application latency and resource utilization. Highly recommended for production platform engineers.
  - **(2022)** [**grafana.com: How to manage high cardinality metrics in Prometheus and Kubernetes**](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides an in-depth operational guide on mitigating Prometheus cardinality spikes within Kubernetes clusters. Curator insight emphasizes structural optimization of metric labels, while live grounding confirms Grafana's continuing dominance in visualization platforms handling high-churn timeseries data. Key strategies include using metric relabel configurations and dropping redundant metrics prior to ingestion.
  - **(2021)** [itnext.io: Kubernetes: monitoring with Prometheus — exporters, a Service Discovery, and its roles](https://itnext.io/kubernetes-monitoring-with-prometheus-exporters-a-service-discovery-and-its-roles-ce63752e5a1) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs Prometheus service discovery mechanics inside Kubernetes, highlighting the difference between Pod, Service, and Endpoint discovery roles. Demonstrates how exporters expose node and application-level metrics for scrape targets.
  - **(2020)** [blog.fourninecloud.com: Kubernetes monitoring — How to monitor using prometheus?](https://blog.fourninecloud.com/kubernetes-monitoring-how-to-monitor-using-prometheus-f2eff767f6bb) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational tutorial detail step-by-step deployment of Prometheus on Kubernetes. It covers target discovery, metrics collection, and node exporter setup. While helpful for beginners, modern architectures typically favor Operator-based deployments.
#### SLOs

  - **(2021)** [**thenewstack.io: Service Level Objectives in Kubernetes**](https://thenewstack.io/service-level-objectives-in-kubernetes) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explains Service Level Objectives (SLOs) in cloud-native systems, detailing how to establish SLIs and error budgets inside Kubernetes clusters. Introduces standard math and metrics pipelines needed to track app health reliably.
  - **(2022)** [thenewstack.io: SLOs in Kubernetes, 1 Year Later](https://thenewstack.io/slos-in-kubernetes-1-year-later) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Follow-up retrospective on implementing and maintaining SLO programs. Evaluates failures, cultural barriers, and technical evolution (like OpenSLO), offering architectural lessons from long-term metric monitoring.
#### Telegraf

  - **(2020)** [influxdata.com: Expand Kubernetes Monitoring with Telegraf Operator](https://www.influxdata.com/blog/expand-kubernetes-monitoring-telegraf-operator) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details using the Telegraf Operator to automatically inject sidecar containers for comprehensive metric harvesting. Grounding shows how it simplifies complex time-series data streams directly into InfluxDB.
### Monitoring Practices

#### Alerting Policies

  - **(2020)** [thenewstack.io: 12 Critical Kubernetes Health Conditions You Need to Monitor](https://thenewstack.io/12-critical-kubernetes-health-conditions-you-need-to-monitor) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compiles 12 critical cluster health indicators that platform engineers should monitor. Covers specific warning metrics like CrashLoopBackOff, disk pressure thresholds, and API server request latency bounds.
  - **(2020)** [circonus.com: 12 Critical Kubernetes Health Conditions You Need to Monitor and Why](https://www.circonus.com/2020/12/12-critical-kubernetes-health-conditions-you-need-to-monitor-and-why) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An alternative perspective highlighting twelve crucial Kubernetes metrics. Explains why etcd leader election loss, system OOMs, and PVC storage saturation require high-priority automated alerts.
#### Introduction

  - **(2020)** [circonus.com: Guide to Kubernetes Monitoring: Part 1](https://www.circonus.com/2020/09/guide-to-kubernetes-monitoring-part-1) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of a introductory series detailing the evolution of Kubernetes observability. Outlines how pull-based metrics scrape architectures operate and explains why traditional host-centric monitoring fails in containerized runtime environments.
#### Job Telemetry

  - **(2021)** [itnext.io: Monitoring Kubernetes Jobs](https://itnext.io/monitoring-kubernetes-jobs-8adc241a7b60) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses the specific challenge of monitoring ephemeral Kubernetes CronJobs and Jobs. Focuses on setting up Alertmanager rules that isolate transient run errors from long-running service alerts.
#### Production Readiness

  - **(2021)** [sysdig.com: Monitoring Kubernetes in Production](https://www.sysdig.com/blog/monitoring-kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An operational guide covering the complexities of monitoring Kubernetes clusters in live production. It focuses on scaling metrics infrastructure, scraping limits, and setting up centralized dashboards for multi-cluster operations.
### Monitoring Stack

#### Alerting Policies (1)

  - **(2022)** [dev.to/mikeyglitz: Proactive Kubernetes Monitoring with Alerting](https://dev.to/mikeyglitz/proactive-kubernetes-monitoring-with-alerting-58en) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains how to set up proactive alerts inside Kubernetes using Prometheus rules paired with Slack webhooks. Walks through alert configurations for pending pods, node pressure events, and high namespace limit utilization.
#### Kube-State-Metrics

  - **(2026)** [==kube-state-metrics 🌟==](https://github.com/kubernetes/kube-state-metrics) <span class='md-tag md-tag--info'>⭐ 6125</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official repository for kube-state-metrics. This system service listens to the Kubernetes API server and generates Prometheus-compatible metrics representing the state of objects (such as deployments, pods, and nodes) rather than raw resource usage.
#### Kubernetes Control Plane

  - **(2023)** [**sysdig.com: How to monitor Kubernetes control plane**](https://www.sysdig.com/blog/monitor-kubernetes-control-plane) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A deep dive tutorial explaining how to parse metrics from core control plane components like the API Server, etcd, controller manager, and scheduler. Essential reading for platform teams building enterprise SLAs around cluster health.
#### Loki Configuration

  - **(2022)** [dev.to: Monitoring Kubernetes cluster logs and metrics using Grafana, Prometheus and Loki](https://dev.to/leroykayanda/kubernetes-monitoring-using-grafana-3dhc) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A deployment guide detailing how to build a unified log and metrics tracking pipeline using Prometheus, Grafana, and Loki (the PLG stack). Focuses on optimal Promtail configurations for efficient pod log ingestion.
#### Market Comparisons

  - **(2024)** [8 Best Kubernetes monitoring tools; Paid & open-source](https://middleware.io/blog/kubernetes-monitoring/tools) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An updated evaluation comparing top-tier commercial and open-source observability tooling. Helps architects evaluate software packages on their capacity to unify metrics, traces, and application logs into single pane dashboards.
  - **(2022)** [betterstack.com: 10 Best Kubernetes Monitoring Tools in 2022 🌟](https://betterstack.com/community/comparisons/kubernetes-monitoring-tools) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comparative overview analyzing ten leading Kubernetes monitoring solutions. Contrasts self-hosted open-source deployments with managed APM SaaS platforms, evaluating features, maintenance costs, and ingestion limits.
#### Prometheus Integration

  - **(2021)** [adamtheautomator.com: Utilizing Grafana & Prometheus Kubernetes Cluster Monitoring 🌟](https://adamtheautomator.com/prometheus-kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed configuration manual showcasing how to deploy the kube-prometheus telemetry stack on Kubernetes via Helm. Includes steps for building custom dashboard interfaces and setting up routing rules in Alertmanager.
#### Prometheus Operator

##### Kube-Prometheus

  - **(2026)** [==kube-prometheus==](https://github.com/prometheus-operator/kube-prometheus) <span class='md-tag md-tag--info'>⭐ 7651</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official codebase for kube-prometheus. This repository offers a pre-configured telemetry stack that deploys the Prometheus Operator, Grafana dashboards, Alertmanager rules, and node collectors optimized for monitoring Kubernetes master components.
#### Troubleshooting Platforms

  - **(2022)** [**anaisurl.com: Full Tutorial: Monitoring and Troubleshooting stack with Prometheus, Grafana, Loki and Komodor 🌟**](https://anaisurl.com/full-tutorial-monitoring) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An extensive tutorial demonstrating the installation and routing setup of a modern troubleshooting stack. Combines Prometheus metrics, Grafana dashboards, Loki log aggregators, and Komodor for tracking configuration change impacts in Kubernetes.
### Network Observability

#### NetFlow

  - **(2021)** [blog.palark.com: Service communication monitoring in Kubernetes with NetFlow](https://palark.com/blog/kubernetes-services-interaction-monitoring-with-netflow) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to monitor inter-service communication within Kubernetes by exporting NetFlow data from the underlying Linux network namespace. Curator insight notes its lightweight footprint, while grounding reminds that eBPF has largely superseded pure NetFlow approaches in 2026.
#### Wireshark

  - [kubeshark.co](https://www.immo-pop.com/login)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Note: This link appears redirected to an unrelated domain (immo-pop.com), signaling a precision failure under Mandate 32. It is flagged for review, while users are redirected to the official open-source Kubeshark repository.
#### eBPF

  - **(2024)** [==kubeshark/kubeshark==](https://github.com/kubeshark/kubeshark) <span class='md-tag md-tag--info'>⭐ 11905</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kubeshark provides deep API traffic inspection and network analysis for Kubernetes. Operating via eBPF, it captures and decodes L7 protocols (HTTP/2, gRPC, Redis) in real-time, functioning as 'Wireshark for Kubernetes'.
  - **(2024)** [**github.com/microsoft/retina**](https://github.com/microsoft/retina) <span class='md-tag md-tag--info'>⭐ 3143</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Microsoft Retina is a highly advanced, eBPF-powered network observability platform for Kubernetes. It aggregates deep network metrics, handles connection tracking, and performs distributed packet captures transparently.
  - **(2022)** [**rcarrata.com: Network Observability Deep Dive in Kubernetes with NetObserv Operator**](https://rcarrata.github.io/observability/netobserv-1) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Deep dive into Red Hat's NetObserv Operator, showcasing how eBPF is leveraged to gather network flow telemetry without sidecars. Live grounding confirms NetObserv's evolution into a robust tool for analyzing Kubernetes internal traffic patterns and diagnosing network bottlenecks.
### Reliability Engineering

#### Cilium

##### Four Golden Signals

  - **(2023)** [**isovalent.com: What are the 4 Golden Signals for Monitoring Kubernetes?**](https://isovalent.com/blog/post/what-are-the-4-golden-signals-for-monitoring-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An advanced technical blog demonstrating how to monitor Google's 4 Golden Signals using Cilium's eBPF architecture and Prometheus. This method allows teams to gather application performance metrics without sidecar injection overhead.
### Runtime Observability

#### eBPF (1)

  - **(2021)** [newrelic.com: Pixie](https://newrelic.com/platform/kubernetes-pixie) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the integration of Pixie, an eBPF-driven Kubernetes observability tool, with New Relic. It highlights instant telemetry collection without code instrumentation, capturing metrics, traces, and logs. Live grounding highlights its CNCF Sandbox hosting and widespread adoption for real-time debugging.
### Telemetry Standards

#### Core Metrics Guide

  - **(2021)** [kubermatic.com: The Complete Guide to Kubernetes Metrics](https://www.kubermatic.com/blog/the-complete-guide-to-kubernetes-metrics) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A complete manual detailing metrics collection pathways in Kubernetes. Explores how the metrics pipeline aggregates metrics from cAdvisor, Kubelet, and API sources, explaining the roles of both metrics-server and custom prometheus adapters.
#### OpenTelemetry

  - **(2023)** [==signoz.io: Kubernetes Cluster Monitoring with OpenTelemetry | Complete Tutorial 🌟==](https://signoz.io/blog/opentelemetry-kubernetes-cluster-metrics-monitoring) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive masterclass on configuring the OpenTelemetry Collector daemonset to monitor Kubernetes system components. It contrasts traditional Prometheus agent scraping with OTel's unified ingestion pipeline. Demonstrates clear performance benefits and architectural modernization.
  - **(2023)** [**opentelemetry.io: Creating a Kubernetes Cluster with Runtime Observability**](https://opentelemetry.io/blog/2023/k8s-runtime-observability) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides step-by-step guidance on provisioning a Kubernetes cluster with built-in runtime observability using OpenTelemetry. It details standardizing telemetry signals (metrics, traces, logs) straight from the container runtime interface. Grounding confirms its status as the default open-standard approach.
### eBPF Monitoring

#### Pixie Integration

  - **(2021)** [**itnext.io: How to tackle Kubernetes observability challenges with Pixie**](https://itnext.io/how-to-tackle-kubernetes-observability-challenges-with-pixie-4c6414ca913) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explains how to use Pixie, an eBPF-driven platform, to achieve instant observability on Kubernetes clusters. Demonstrates capturing system-wide HTTP traffic, db queries, and CPU profiles with zero code instrumenting overhead.
## Security

### Certificates

#### Monitoring

  - **(2021)** [itnext.io: Monitoring Certificates Expiration in Kubernetes with X.509 Exporter](https://itnext.io/monitoring-certificates-expiration-in-kubernetes-with-x-509-exporter-8030b69f611d) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores configuring the Prometheus X.509 Certificate Exporter to continuously scan Kubernetes secret spaces. Prevents outages by alerting on expiring internal and ingress SSL/TLS certificates.
### Threat Detection

#### Audit Logs

  - **(2022)** [**signoz.io: Kubernetes Audit Logs - Best Practices And Configuration**](https://signoz.io/blog/kubernetes-audit-logs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Outlines advanced configuration policies for the Kubernetes API audit logging engine. Deeply covers audit profiles, performance tuning, secure log transport, and compliance-driven retention metrics.
  - **(2020)** [**qlinh.com: Leveraging Kubernetes audit logs for threat detection**](https://qlinh.com/infosec/2020/09/30/threat-detection-with-kubernetes-audit-logs.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A security-oriented analysis showing how to leverage Kubernetes API audit logs to capture malicious actions and abnormal cluster behavior. Grounding confirms its high value in implementing Falco-based SIEM ingestion architectures.
  - **(2022)** [tealfeed.com: Kubernetes Audit Logs: Who created or deleted a namespace?](https://tealfeed.com/kubernetes-audit-logs-created-deleted-namespace-ho5o3) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A targeted troubleshooting guide focused on analyzing the Kube-APIServer audit log payload. Explains how to parse JSON audit trails to track exact identity, timestamp, and API verbs executing namespace lifecycle events.

---
💡 **Explore Related:** [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md) | [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md)

