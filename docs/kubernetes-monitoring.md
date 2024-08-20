# Kubernetes Monitoring and Logging

1. [Introduction](#introduction)
2. [Kubernetes Logging](#kubernetes-logging)
3. [SLOs in Kubernetes](#slos-in-kubernetes)
4. [ECK Elastic Cloud on Kubernetes](#eck-elastic-cloud-on-kubernetes)
5. [Telegraf Operator](#telegraf-operator)
6. [Monitoring Certificates Expiration](#monitoring-certificates-expiration)
7. [kubeshark](#kubeshark)
8. [k8spacket](#k8spacket)
9. [Kubelog](#kubelog)
10. [Microsoft Retina eBPF](#microsoft-retina-ebpf)
11. [Videos](#videos)

## Introduction

- [DZone: Kubernetes Monitoring Essentials](https://dzone.com/refcardz/monitoring-kubernetes)
- [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) Use Prometheus to monitor Kubernetes and applications running on Kubernetes. This repository collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.
    - [prometheus-community/kube-prometheus-stack 🌟🌟](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) **kube-prometheus-stack collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.**
    - [faun.pub: Becoming DevOps — Observability](https://faun.pub/becoming-devops-observability-152b292c05b9) Observability with Kube-Prometheus
    - [levelup.gitconnected.com: Installing & Exploring the Kube-Prometheus Project](https://levelup.gitconnected.com/installing-exploring-the-kube-prometheus-project-eef375d49f6b)
- [medium: Kubernetes Monitoring: Kube-State-Metrics](https://medium.com/@chrisedrego/kubernetes-monitoring-kube-state-metrics-df6546aea324)
- [Kubernetes Monitoring 101 — Core pipeline & Services Pipeline](https://levelup.gitconnected.com/kubernetes-monitoring-101-core-pipeline-services-pipeline-a34cd4cc9627)
- [medium: Utilizing and monitoring kubernetes cluster resources more effectively](https://medium.com/@martin.schneppenheim/utilizing-and-monitoring-kubernetes-cluster-resources-more-effectively-using-this-tool-df4c68ec2053)
- [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://sysdig.com/blog/kubernetes-monitoring-best-practices/)
- [magalix.com: Best Practices And Tools For Monitoring Your Kubernetes Cluster](https://www.magalix.com/blog/best-practices-and-tools-for-monitoring-your-kubernetes-cluster)
- [sysdig.com: Monitoring Kubernetes in Production](https://sysdig.com/blog/monitoring-kubernetes/)
- [sysdig.com: How to monitor Kubernetes control plane](https://sysdig.com/blog/monitor-kubernetes-control-plane/)
- [thenewstack.io: 12 Critical Kubernetes Health Conditions You Need to Monitor](https://thenewstack.io/12-critical-kubernetes-health-conditions-you-need-to-monitor/)
- [devopscurry.com: Best  Open-Source Monitoring Tools for Kubernetes in 2021](https://devopscurry.com/best-open-source-monitoring-tools-for-kubernetes-in-2021/)
- [circonus.com: 12 Critical Kubernetes Health Conditions You Need to Monitor and Why](https://www.circonus.com/2020/12/12-critical-kubernetes-health-conditions-you-need-to-monitor-and-why/)
- [circonus.com: Guide to Kubernetes Monitoring: Part 1](https://www.circonus.com/2020/09/guide-to-kubernetes-monitoring-part-1/)
    - [circonus.com: Guide to Monitoring Kubernetes, Part 2: Which Metrics and Health Conditions You Should be Monitoring](https://www.circonus.com/2021/01/guide-to-monitoring-kubernetes-part-2-which-metrics-and-health-conditions-you-should-be-monitoring/)
- [infracloud.io: Monitoring Kubernetes cert-manager Certificates with BotKube](https://www.infracloud.io/blogs/monitoring-kubernetes-cert-manager-certificates/) - [botkube.io](https://www.botkube.io/)
- [kube-state-metrics 🌟](https://github.com/kubernetes/kube-state-metrics) **Add-on agent to generate and expose cluster-level metrics. kube-state-metrics is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects. (See examples in the Metrics section below.) It is not focused on the health of the individual Kubernetes components, but rather on the health of the various objects inside, such as deployments, nodes and pods.**
- [itnext.io: Monitoring Kubernetes Jobs](https://itnext.io/monitoring-kubernetes-jobs-8adc241a7b60)
- [cncf.io: Avoiding Kubernetes cluster outages with synthetic monitoring](https://www.cncf.io/blog/2021/08/10/avoiding-kubernetes-cluster-outages-with-synthetic-monitoring/)
- [medium: Replication Controller & Replica sets in Kubernetes](https://medium.com/avmconsulting-blog/replication-controller-replica-sets-in-kubernetes-820f3cec7170)
- [kubermatic.com: The Complete Guide to Kubernetes Metrics](https://www.kubermatic.com/blog/the-complete-guide-to-kubernetes-metrics/)
- [arabitnetwork.com: K8S – Enabling Auditing Logs | Step-by-Step](https://arabitnetwork.com/2021/03/13/k8s-enabling-auditing-logs-step-by-step/)
- [youtube.com: Cloud Quick POCs - Kubernetes monitoring metrics using Grafana Cloud on AWS EKS | Observability | Grafana](https://www.youtube.com/watch?v=FVDHWPxK5nU&ab_channel=CloudQuickPOCs)
- [loft.sh: Kubernetes Cost Monitoring with Prometheus & Grafana](https://loft.sh/blog/kubernetes-cost-monitoring-with-prometheus-and-grafana/)
- [==anaisurl.com: Full Tutorial: Monitoring and Troubleshooting stack with Prometheus, Grafana, Loki and Komodor== 🌟](https://anaisurl.com/full-tutorial-monitoring/)
- [==blog.flant.com: Collecting system information from a bunch of Kubernetes clusters==](https://blog.flant.com/collect-system-information-stats-from-kubernetes-clusters/)
- [medium.com/is-it-observable: How to collect metrics in a Kubernetes cluster](https://medium.com/is-it-observable/how-to-collect-metrics-in-a-kubernetes-cluster-9ad4a69aafb0)
- [itnext.io: How to tackle Kubernetes observability challenges with Pixie](https://itnext.io/how-to-tackle-kubernetes-observability-challenges-with-pixie-4c6414ca913)
- [medium.com/@lucapompei91: Kubernetes observability](https://medium.com/@lucapompei91/kubernetes-observability-17a7875a38f6)
- [==dev.to: Monitoring Kubernetes cluster logs and metrics using Grafana, Prometheus and Loki==](https://dev.to/leroykayanda/kubernetes-monitoring-using-grafana-3dhc)
- [hitesh-pattanayak.medium.com: Observability in Kubernetes](https://hitesh-pattanayak.medium.com/observability-in-kubernetes-b53d6ea1b37d)
- [middlewareinventory.com: Get CPU and Memory Usage of NODES and PODS – Kubectl 🌟](https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s)
- [betterstack.com: 10 Best Kubernetes Monitoring Tools in 2022 🌟](https://betterstack.com/community/comparisons/kubernetes-monitoring-tools/)
- [medium.com/@kylekhunter: Kubernetes Monitoring with Prometheus](https://medium.com/@kylekhunter/kubernetes-monitoring-with-prometheus-a149c35694c4)
- [adamtheautomator.com: Utilizing Grafana & Prometheus Kubernetes Cluster Monitoring 🌟](https://adamtheautomator.com/prometheus-kubernetes/) In this guide, you'll learn how to monitor your Kubernetes cluster, viewing internal state metrics with a Prometheus and Grafana dashboard.
- [grafana.com: Introducing Kubernetes Monitoring in Grafana Cloud](https://grafana.com/blog/2022/07/13/introducing-kubernetes-monitoring-in-grafana-cloud/) Kubernetes Monitoring is available to all Grafana Cloud users, including on free tier. Container orchestration to deploy at scale, iterate quickly, and manage a large number of apps and services.
- [medium.com/@clymeneallen: Best Practices, Monitoring System for Multi-K8s Cluster Environments Using Open Source](https://medium.com/@clymeneallen/best-practices-monitoring-system-for-multi-k8s-cluster-environments-using-open-source-d85544052f37)
- [medium.com/@magstherdev: OpenTelemetry on Kubernetes 🌟](https://medium.com/@magstherdev/opentelemetry-on-kubernetes-c167f024b35f)
- [==betterprogramming.pub: 6 Metrics To Watch for on Your K8s Cluster== 🌟](https://betterprogramming.pub/6-metrics-to-watch-for-on-your-k8s-cluster-76d58f08397f) The most critical Kubernetes metrics to monitor. In this article, you will cover the 6 most critical metrics based on Kubernetes's metadata that form a good baseline for monitoring your workloads and ensuring they're in a healthy state.
- [figments.medium.com: Observable Kubernetes Cluster Using Grafana-Loki-Prometheus](https://figments.medium.com/observable-kubernetes-cluster-using-grafana-loki-prometheus-a661a31d7ad8)
- [medium.com/@isalapiyarisi: Getting Started on Kubernetes observability with eBPF](https://medium.com/@isalapiyarisi/getting-started-on-kubernetes-observability-with-ebpf-88139eb13fb2)
- [8 Best Kubernetes monitoring tools; Paid & open-source](https://middleware.io/blog/kubernetes-monitoring-tools/)
- [dev.to/mikeyglitz: Proactive Kubernetes Monitoring with Alerting](https://dev.to/mikeyglitz/proactive-kubernetes-monitoring-with-alerting-58en) In this tutorial, you'll learn how to combine Prometheus, Alertmanager, Grafana and Linkerd to deliver timely alerts when a problem occurs in a Kubernetes cluster.
- [isovalent.com: What are the 4 Golden Signals for Monitoring Kubernetes?](https://isovalent.com/blog/post/what-are-the-4-golden-signals-for-monitoring-kubernetes/)
- [grafana.com: How to manage high cardinality metrics in Prometheus and Kubernetes](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/)
- [==containiq.com: Leveraging Kubernetes Metrics | Tutorial & Tools To Use==](https://www.containiq.com/post/kubernetes-metrics) In Kubernetes, resource metrics, cluster state metrics, and control plane metrics are mission-critical. In this article, we explore these three types of metrics, explain how to use them, and introduce a number of tools to collect and monitor them.
- [medium.com/@HirenDhaduk1: Top Kubernetes Observability Tools and their Usage](https://medium.com/@HirenDhaduk1/top-kubernetes-observability-tools-and-their-usage-e4e8eef8aec3)
- [milindasenaka96.medium.com: Setup Prometheus and Grafana to Monitor the K8s Cluster](https://milindasenaka96.medium.com/setup-prometheus-and-grafana-to-monitor-the-k8s-cluster-e1d35343d7a9)
- [blog.fourninecloud.com: Kubernetes monitoring — How to monitor using prometheus?](https://blog.fourninecloud.com/kubernetes-monitoring-how-to-monitor-using-prometheus-f2eff767f6bb)
- [rcarrata.com: Network Observability Deep Dive in Kubernetes with NetObserv Operator](https://rcarrata.com/observability/netobserv-1/) How can we analyze our Network Flows in our Kubernetes clusters? How can we enable Network Observability for Kubernetes in a simple, searchable and visual way? How can we leverage cool technologies such as eBPF or IPFIX to enable Network Observability for our K8s Network Traffic?
- [kemilad.medium.com: Monitoring-Stack Deployment To A Kubernetes Cluster — Prometheus | Grafana | AlertManager | Loki + Exporters | Dashboards and etc 🌟](https://kemilad.medium.com/monitoring-stack-deployment-to-a-kubernetes-cluster-prometheus-grafana-alertmanager-loki-dcc7339d4f19)
- [newrelic.com: Pixie](https://newrelic.com/platform/kubernetes-pixie)
    - [xgrid.medium.com: Tackling Kubernetes Observability Challenges with Pixie](https://xgrid.medium.com/tackling-kubernetes-observability-challenges-with-pixie-a03cbad93148)
    - [newrelic.com: What Is eBPF and Why Does It Matter for Observability?](https://newrelic.com/blog/best-practices/what-is-ebpf)
- [awstip.com: Monitoring Your EKS Cluster with the Power of Prometheus and Grafana through Helm](https://awstip.com/monitoring-your-eks-cluster-with-the-power-of-prometheus-and-grafana-through-helm-%EF%B8%8F-1e8dc1ad5620)
- [grafana.com: A beginner's guide to Kubernetes application monitoring](https://grafana.com/blog/2023/01/31/a-beginners-guide-to-kubernetes-application-monitoring)
- [medium.com/@poseidon.os: Poseidon: A Kubernetes Cluster Visualization & Cost Analysis Tool](https://medium.com/@poseidon.os/poseidon-a-kubernetes-cluster-visualization-cost-analysis-tool-d0fb55c2858c)
- [==aws.amazon.com: Using Prometheus to Avoid Disasters with Kubernetes CPU Limits== 🌟](https://aws.amazon.com/blogs/containers/using-prometheus-to-avoid-disasters-with-kubernetes-cpu-limits/) **In this article, you'll discuss how CPU throttling can affect Kubernetes' node performance, and how to avoid this by setting the right values for limits. The author also suggests using Prometheus as a tool to help set reasonable limits**
- [umeey.medium.com: Four Golden Signals Of Monitoring: Site Reliability Engineering (SRE) Metrics](https://umeey.medium.com/four-golden-signals-of-monitoring-site-reliability-engineering-sre-metrics-64031dbe268) Golden Signal Monitoring using FastAPI on k8s
- [grafana.com: How to optimize resource utilization with Kubernetes Monitoring for Grafana Cloud 🌟](https://grafana.com/blog/2023/03/03/how-to-optimize-resource-utilization-with-kubernetes-monitoring-for-grafana-cloud/) **Overprovisioning or underprovisioning your Kubernetes resources can have significant consequences on both your budget and your app performance.**
- [medium.com/@lambdaEranga: Monitor Kubernets Services/Endpoints with Prometheus Blackbox Exporter 🌟](https://medium.com/@lambdaEranga/monitor-kubernets-services-endpoints-with-prometheus-blackbox-exporter-a64e062c05d5) In this article, you will discuss monitoring different endpoints/services in a Kubernetes cluster using Prometheus Blackbox Exporter
- [samiislam0306.medium.com: Insightful Monitoring of Kubernetes Clusters with Traces](https://samiislam0306.medium.com/insightful-monitoring-of-kubernetes-clusters-with-traces-c7c3b33ed07e) Gain valuable insights into the performance of your Kubernetes cluster with trace monitoring. A guide that helps you optimize your operations for maximum efficiency and productivity.
- [medium.com/@walissonscd: Monitoring Kubernetes Cluster Resources: Using Top Metrics Commands](https://medium.com/@walissonscd/monitoring-kubernetes-cluster-resources-using-top-metrics-commands-a60408765321)
- [==blog.devops.dev: Prometheus metrics within Kubernetes — an aerial view== | Joseph Esrig](https://blog.devops.dev/prometheus-metrics-within-kubernetes-an-ariel-view-d1d3b7d75418)
- [grafana.com: How to monitor Kubernetes clusters with the Prometheus Operator](https://grafana.com/blog/2023/01/19/how-to-monitor-kubernetes-clusters-with-the-prometheus-operator/) In this guide, you'll learn how to deploy and use the Prometheus Operator to configure and manage Prometheus instances in your Kubernetes cluster. You'll also discover how to deploy Grafana to help analyze and visualize the health of your clusters.
- [blog.palark.com: Service communication monitoring in Kubernetes with NetFlow](https://blog.palark.com/kubernetes-services-interaction-monitoring-with-netflow/)
- [betterprogramming.pub: Improve Cluster Monitoring With Network Mapping in Grafana](https://betterprogramming.pub/improve-cluster-monitoring-with-network-mapping-in-grafana-fa8bb479fd47) A deep dive into obtaining network maps and correlating IP with cluster workloads to speed up debugging
- [betterprogramming.pub: Kubernetes Observability Part 1: Events, Logs, and Integration With Slack, OpenAI, and Grafana](https://betterprogramming.pub/kubernetes-observability-part-1-events-logs-integration-with-slack-openai-and-grafana-62068cf43ec) Build a Kubernetes custom controller to watch Kubernetes Events and forward them to Grafana Loki using Promtail
- [itnext.io: Kubernetes: monitoring with Prometheus — exporters, a Service Discovery, and its roles](https://itnext.io/kubernetes-monitoring-with-prometheus-exporters-a-service-discovery-and-its-roles-ce63752e5a1)
- [opentelemetry.io: Creating a Kubernetes Cluster with Runtime Observability](https://opentelemetry.io/blog/2023/k8s-runtime-observability/)
- [medium.com/@onai.rotich: Understand container metrics and why they matter](https://medium.com/@onai.rotich/understand-container-metrics-and-why-they-matter-9e88434ca62a) In this 2-part article, you will explore the key metrics to scrape in your cluster
- [kkamalesh117.medium.com: Setting up Prometheus and Grafana Integration on Kubernetes with Helm](https://kkamalesh117.medium.com/setting-up-prometheus-and-grafana-integration-on-kubernetes-with-helm-dfc63823608c)
- [medium.com/@MetricFire: Monitoring Kubernetes tutorial: Using Grafana and Prometheus](https://medium.com/@MetricFire/monitoring-kubernetes-tutorial-using-grafana-and-prometheus-3239079b138f)
- [medium.com/globant: Monitoring a multi-cluster Kubernetes Deployment](https://medium.com/globant/monitoring-a-multi-cluster-kubernetes-deployment-9e7a418a06b7) Deploying a high resilience monitoring and observation platform for Kubernetes multi-cluster solutions
- [medium.com/@martin.hodges: Adding observability to a Kubernetes cluster using Prometheus](https://medium.com/@martin.hodges/adding-observability-to-a-kubernetes-cluster-using-prometheus-c2cba6c0fdaa) Monitoring your services is vital and should be considered as part of your underlying infrastructure for your services. You should put this in place ahead of creating and deploying your services. In this article I look at how to deploy Prometheus provide the observability you need to run your services.
- [addozhang.medium.com: Non-intrusive Inject OpenTelemetry Auto-Instrumentation in Kubernetes](https://addozhang.medium.com/non-intrusive-inject-opentelemetry-auto-instrumentation-in-kubernetes-a9dfd49fc714)
- [medium.com/@abhisman.sarkar: Kubernetes Monitoring: Effective Cluster Tracking with Prometheus](https://medium.com/@abhisman.sarkar/kubernetes-monitoring-effective-cluster-tracking-with-prometheus-b0ed5b3efb32)
- [==aws.plainenglish.io: Mastering Monitoring: The Complete Guide to Using Prometheus and Grafana with Kubernetes==](https://aws.plainenglish.io/mastering-monitoring-the-complete-guide-to-using-prometheus-and-grafana-with-kubernetes-e53d8306123d)
- [medium.com/@muppedaanvesh: A Hands-On Guide to Kubernetes Monitoring Using Prometheus & Grafana](https://medium.com/@muppedaanvesh/a-hands-on-guide-to-kubernetes-monitoring-using-prometheus-grafana-%EF%B8%8F-b0e00b1ae039) Understanding Prometheus & Grafana Setup in Kubernetes: A Comprehensive Guide
- [==signoz.io: Kubernetes Cluster Monitoring with OpenTelemetry | Complete Tutorial== 🌟](https://signoz.io/blog/opentelemetry-kubernetes-cluster-metrics-monitoring/)

## Kubernetes Logging

- [cncf.io: Logging in Kubernetes: EFK vs PLG Stack](https://www.cncf.io/blog/2020/07/27/logging-in-kubernetes-efk-vs-plg-stack/)
- [medium: How to Deploy an EFK stack to Kubernetes](https://medium.com/avmconsulting-blog/how-to-deploy-an-efk-stack-to-kubernetes-ebc1b539d063)
- [digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes)
- [portworx.com: How to backup and restore Elasticsearch on Kubernetes](https://portworx.com/how-to-backup-and-restore-elasticsearch-on-kubernetes/)
- [elastic.co: Elastic Stack Monitoring with Elastic Cloud on Kubernetes (ECK - official operator)](https://www.elastic.co/es/blog/elastic-stack-monitoring-with-elastic-cloud-on-kubernetes) In this blog post, we'll explore how the official **ElasticCloud** on **Kubernetes operator** can be used to easily deploy and manage **ElasticStack Monitoring** using the new **Beat CRD**.
- [papertrail.com: Quick and Easy Way to Implement Kubernetes Logging](https://www.papertrail.com/blog/quick-and-easy-way-to-implement-kubernetes-logging/) The SolarWinds® Papertrail™ team is excited to announce SolarWinds rKubeLog, an open-source project designed to streamline Kubernetes logging. rKubeLog allows you to forward logs to Papertrail from within a Kubernetes cluster without using a daemon or setting up application-level logging or a logging sidecar.
- [qlinh.com: Leveraging Kubernetes audit logs for threat detection](https://qlinh.com/infosec/2020/09/30/threat-detection-with-kubernetes-audit-logs.html) Kubernetes audit logs can provide great visibility into the operation and inner workings of your cluster. Learn how to leverage Kubernetes audit logs for threat detection
- [itnext.io: Kubernetes Logging in Production](https://itnext.io/kubernetes-logging-in-production-545ea88d9a4a)
- [opensource.com: What you need to know about cluster logging in Kubernetes 🌟](https://opensource.com/article/21/11/cluster-logging-kubernetes) Explore how different container logging patterns in Kubernetes work.
- [==devopscube.com: Kubernetes Logging Tutorial For Beginners== 🌟](https://devopscube.com/kubernetes-logging-tutorial)
- [aws.plainenglish.io: Kubernetes Deep Dive: Log Management](https://aws.plainenglish.io/kubernetes-deep-dive-log-management-a60b06e2d738) Part 28 of a series of articles about learning k8s!
- [medium.com/vmacwrites: Kubernetes Audit Logs: Who created or deleted a namespace?](https://medium.com/vmacwrites/kubernetes-audit-logs-who-created-or-deleted-a-namespace-7d55c20d2730) Learn how to set up log forwarding and collect audit logs that are passed through the Kubernetes API server to IBM Log Analysis to check who initiated a request and when they did so.
- [shivanshu1333.medium.com: Structured logging in Kubernetes](https://shivanshu1333.medium.com/structured-logging-in-kubernetes-58cf35e6d60d)
    - Logs are an essential aspect of observability and a critical tool for debugging. But Kubernetes logs have traditionally been unstructured strings, making any automated parsing difficult and any downstream processing, analysis, or querying challenging to do reliably.
    - In Kubernetes 1.19, we are adding support for structured logs, which natively support (key, value) pairs and object references. We have also updated many logging calls such that over 99% of logging volume in a typical deployment are now migrated to the structured format.
    - To maintain backwards compatibility, structured logs will still be outputted as a string where the string contains representations of those “key”=”value” pairs. Starting in alpha in 1.19, logs can also be outputted in JSON format using the --logging-format=json flag.
- [tealfeed.com: Kubernetes Audit Logs: Who created or deleted a namespace?](https://tealfeed.com/kubernetes-audit-logs-created-deleted-namespace-ho5o3) Learn how to set up log forwarding and collect audit logs that are passed through the Kubernetes API server to IBM Log Analysis to check who initiated a request and when they did so.
- [==containiq.com: Kubernetes Audit Logs | Use Cases & Best Practices==](https://www.containiq.com/post/kubernetes-audit-logs) Kubernetes audit logs are powerful, but only if enabled and correctly configured. This article will help you get started using audit logs, and show you how to get the most out of them.
- [blog.devops.dev: Importance of Logging In Kubernetes, Intro to Grafana Loki & deploying with helm-charts](https://blog.devops.dev/importance-of-logging-in-kubernetes-and-intro-to-grafana-loki-f8dc6f736e6)
- [faun.pub: Kubernetes Practice — Logging with Logstash and FluentD by Sidecar Container](https://faun.pub/kubernetes-practice-logging-with-logstash-and-fluentd-by-sidecar-container-86076da0812f) We are going to learn how to use the Sidecar Container pattern to install Logstash and FluentD on Kubernetes for log aggregation.
- [dev.to: Kubernetes Practice — Logging with Logstash and FluentD by Sidecar Container](https://dev.to/devopsvn/kubernetes-practice-logging-with-logstash-and-fluentd-by-sidecar-container-16oi)
- [signoz.io: Kubernetes Audit Logs - Best Practices And Configuration](https://signoz.io/blog/kubernetes-audit-logs)
- [blog.amhaish.com: Observing the K8 cluster using ELK stack](https://blog.amhaish.com/observing-the-k8-cluster-using-elk-stack-7d4264fdb0e3)
- [kube-logging/logging-operator](https://github.com/kube-logging/logging-operator) The Logging operator automates the deployment and configuration of a Kubernetes logging pipeline. The operator deploys and configures a Fluent Bit daemonset on every node to collect container and application logs from the node file system.
- [akyriako.medium.com: Kubernetes Logging with Grafana Loki & Promtail in under 10 minutes 🌟](https://akyriako.medium.com/kubernetes-logging-with-grafana-loki-promtail-in-under-10-minutes-d2847d526f9e) Consolidate all your Kubernetes logs in a intuitive Grafana dashboard.
- [yuminlee2.medium.com: Kubernetes: Container and Pod Logging](https://yuminlee2.medium.com/kubernetes-container-and-pod-logging-82ec5c057cb2)
- [medium.com/kubernetes-tutorials: Cluster-level Logging in Kubernetes with Fluentd](https://medium.com/kubernetes-tutorials/cluster-level-logging-in-kubernetes-with-fluentd-e59aa2b6093a)
- [shivanshu1333.medium.com: Contextual Logging in Kubernetes](https://shivanshu1333.medium.com/contextual-logging-in-kubernetes-41f4cc5fea69) The Structured Logging Working Group has added new capabilities to the logging infrastructure in Kubernetes. This post explains how developers can use those to make log output more useful.

## SLOs in Kubernetes

- [==thenewstack.io: Service Level Objectives in Kubernetes==](https://thenewstack.io/service-level-objectives-in-kubernetes/) an SLO is simply a metric, a goal for that metric, and a time period. For instance: “the success rate for service A must be at least 99.7% percent over the past 30 days.” The metric is known as the “service level indicator” (SLI) and the goal is the “objective.”
- [thenewstack.io: SLOs in Kubernetes, 1 Year Later](https://thenewstack.io/slos-in-kubernetes-1-year-later/)

## ECK Elastic Cloud on Kubernetes

- [elastic.co: How to configure Elastic Cloud on Kubernetes with SAML and hot-warm-cold architecture](https://www.elastic.co/es/blog/how-to-configure-elastic-cloud-on-kubernetes-with-saml-and-hot-warm-cold-architecture) Elastic Cloud on Kubernetes (ECK) is an easy way to get the Elastic Stack up and running on top of Kubernetes. That’s because ECK automates the deployment, provisioning, management, and setup of Elasticsearch, Kibana, Beats, and more.

## Telegraf Operator

- [influxdata.com: Expand Kubernetes Monitoring with Telegraf Operator](https://www.influxdata.com/blog/expand-kubernetes-monitoring-telegraf-operator)

## Monitoring Certificates Expiration

- [itnext.io: Monitoring Certificates Expiration in Kubernetes with X.509 Exporter](https://itnext.io/monitoring-certificates-expiration-in-kubernetes-with-x-509-exporter-8030b69f611d)

## kubeshark

- [==kubeshark.co==](https://kubeshark.co) The API Traffic Viewer for  kubernetes. Deep visibility and monitoring of all API traffic and payloads going in, out and across containers and pods inside a Kubernetes cluster.
- [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark) The API traffic viewer for Kubernetes providing deep visibility into all API traffic and payloads going in, out and across containers and pods inside a Kubernetes cluster. Think TCPDump and Wireshark re-invented for Kubernetes
- [medium.com/kernel-space: KubeShark: Wireshark for Kubernetes](https://medium.com/kernel-space/kubeshark-wireshark-for-kubernetes-4069a5f5aa3d)

## k8spacket

- [medium.com/@bareckidarek: TCP packets traffic visualization for kubernetes by k8spacket and Grafana](https://medium.com/@bareckidarek/tcp-packets-traffic-visualization-for-kubernetes-by-k8spacket-and-grafana-bb87cb106f30)
- [medium.com/geekculture: K8s Networking — k8spacket](https://medium.com/geekculture/k8s-networking-k8spacket-eb85f167d1d5) Use k8spacket and Grafana to visualize K8s cluster Traffic
- [pakdailytimes.com: TCP packets traffic visualization for kubernetes by k8spacket and Grafana](https://www.pakdailytimes.com/2022/12/tcp-packets-traffic-visualization-for.html)

## Kubelog

- [kubelog.de](https://kubelog.de) kubelog is a graphical log viewer for Kubernetes, which works with your existing Kubernetes logging infrastructure. Kubelog is a log viewer for kubernetes. Tail multiple pods in one view and use searches to highlight and show results in context.

## Microsoft Retina eBPF

- [==github.com/microsoft/retina==](https://github.com/microsoft/retina) - [retina.sh](https://retina.sh) **eBPF distributed networking observability tool for Kubernetes**
    - Retina is a cloud-agnostic, open-source Kubernetes network observability platform that provides a centralized hub for monitoring application health, network health, and security. It provides actionable insights to cluster network administrators, cluster security administrators, and DevOps engineers navigating DevOps, SecOps, and compliance use cases.
    - Retina collects customizable telemetry, which can be exported to multiple storage options (such as Prometheus, Azure Monitor, and other vendors) and visualized in a variety of ways (like Grafana, Azure Log Analytics, and other vendors).
- [blog.teknews.cloud/aks: A look at Retina on AKS](https://blog.teknews.cloud/aks/network/2024/06/29/A_look_at_Retina_on_AKS.html)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5ofsNyHZwWE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>
