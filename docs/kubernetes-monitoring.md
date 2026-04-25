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

    - [prometheus-community/kube-prometheus-stack 🌟🌟](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) **kube-prometheus-stack collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.**
- [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://sysdig.com/blog/kubernetes-monitoring-best-practices/)
- [sysdig.com: Monitoring Kubernetes in Production](https://sysdig.com/blog/monitoring-kubernetes/)
- [sysdig.com: How to monitor Kubernetes control plane](https://sysdig.com/blog/monitor-kubernetes-control-plane/)
- [thenewstack.io: 12 Critical Kubernetes Health Conditions You Need to Monitor](https://thenewstack.io/12-critical-kubernetes-health-conditions-you-need-to-monitor/)
- [infracloud.io: Monitoring Kubernetes cert-manager Certificates with BotKube](https://www.infracloud.io/blogs/monitoring-kubernetes-cert-manager-certificates/) - [botkube.io](https://www.botkube.io/)
- [kube-state-metrics 🌟](https://github.com/kubernetes/kube-state-metrics) **Add-on agent to generate and expose cluster-level metrics. kube-state-metrics is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects. (See examples in the Metrics section below.) It is not focused on the health of the individual Kubernetes components, but rather on the health of the various objects inside, such as deployments, nodes and pods.**
- [kubermatic.com: The Complete Guide to Kubernetes Metrics](https://www.kubermatic.com/blog/the-complete-guide-to-kubernetes-metrics/)
- [youtube.com: Cloud Quick POCs - Kubernetes monitoring metrics using Grafana Cloud on AWS EKS | Observability | Grafana](https://www.youtube.com/watch?v=FVDHWPxK5nU&ab_channel=CloudQuickPOCs)
- [loft.sh: Kubernetes Cost Monitoring with Prometheus & Grafana](https://loft.sh/blog/kubernetes-cost-monitoring-with-prometheus-and-grafana/)
- [==anaisurl.com: Full Tutorial: Monitoring and Troubleshooting stack with Prometheus, Grafana, Loki and Komodor== 🌟](https://anaisurl.com/full-tutorial-monitoring/)
- [==dev.to: Monitoring Kubernetes cluster logs and metrics using Grafana, Prometheus and Loki==](https://dev.to/leroykayanda/kubernetes-monitoring-using-grafana-3dhc)
- [middlewareinventory.com: Get CPU and Memory Usage of NODES and PODS – Kubectl 🌟](https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s)
- [betterstack.com: 10 Best Kubernetes Monitoring Tools in 2022 🌟](https://betterstack.com/community/comparisons/kubernetes-monitoring-tools/)
- [adamtheautomator.com: Utilizing Grafana & Prometheus Kubernetes Cluster Monitoring 🌟](https://adamtheautomator.com/prometheus-kubernetes/) In this guide, you'll learn how to monitor your Kubernetes cluster, viewing internal state metrics with a Prometheus and Grafana dashboard.
- [grafana.com: Introducing Kubernetes Monitoring in Grafana Cloud](https://grafana.com/blog/2022/07/13/introducing-kubernetes-monitoring-in-grafana-cloud/) Kubernetes Monitoring is available to all Grafana Cloud users, including on free tier. Container orchestration to deploy at scale, iterate quickly, and manage a large number of apps and services.
- [8 Best Kubernetes monitoring tools; Paid & open-source](https://middleware.io/blog/kubernetes-monitoring-tools/)
- [dev.to/mikeyglitz: Proactive Kubernetes Monitoring with Alerting](https://dev.to/mikeyglitz/proactive-kubernetes-monitoring-with-alerting-58en) In this tutorial, you'll learn how to combine Prometheus, Alertmanager, Grafana and Linkerd to deliver timely alerts when a problem occurs in a Kubernetes cluster.
- [isovalent.com: What are the 4 Golden Signals for Monitoring Kubernetes?](https://isovalent.com/blog/post/what-are-the-4-golden-signals-for-monitoring-kubernetes/)
- [grafana.com: How to manage high cardinality metrics in Prometheus and Kubernetes](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/)
- [rcarrata.com: Network Observability Deep Dive in Kubernetes with NetObserv Operator](https://rcarrata.com/observability/netobserv-1/) How can we analyze our Network Flows in our Kubernetes clusters? How can we enable Network Observability for Kubernetes in a simple, searchable and visual way? How can we leverage cool technologies such as eBPF or IPFIX to enable Network Observability for our K8s Network Traffic?
- [newrelic.com: Pixie](https://newrelic.com/platform/kubernetes-pixie)
    - [newrelic.com: What Is eBPF and Why Does It Matter for Observability?](https://newrelic.com/blog/best-practices/what-is-ebpf)
- [grafana.com: A beginner's guide to Kubernetes application monitoring](https://grafana.com/blog/2023/01/31/a-beginners-guide-to-kubernetes-application-monitoring)
- [==aws.amazon.com: Using Prometheus to Avoid Disasters with Kubernetes CPU Limits== 🌟](https://aws.amazon.com/blogs/containers/using-prometheus-to-avoid-disasters-with-kubernetes-cpu-limits/) **In this article, you'll discuss how CPU throttling can affect Kubernetes' node performance, and how to avoid this by setting the right values for limits. The author also suggests using Prometheus as a tool to help set reasonable limits**
- [grafana.com: How to optimize resource utilization with Kubernetes Monitoring for Grafana Cloud 🌟](https://grafana.com/blog/2023/03/03/how-to-optimize-resource-utilization-with-kubernetes-monitoring-for-grafana-cloud/) **Overprovisioning or underprovisioning your Kubernetes resources can have significant consequences on both your budget and your app performance.**
- [grafana.com: How to monitor Kubernetes clusters with the Prometheus Operator](https://grafana.com/blog/2023/01/19/how-to-monitor-kubernetes-clusters-with-the-prometheus-operator/) In this guide, you'll learn how to deploy and use the Prometheus Operator to configure and manage Prometheus instances in your Kubernetes cluster. You'll also discover how to deploy Grafana to help analyze and visualize the health of your clusters.
- [blog.palark.com: Service communication monitoring in Kubernetes with NetFlow](https://blog.palark.com/kubernetes-services-interaction-monitoring-with-netflow/)
- [opentelemetry.io: Creating a Kubernetes Cluster with Runtime Observability](https://opentelemetry.io/blog/2023/k8s-runtime-observability/)
- [==signoz.io: Kubernetes Cluster Monitoring with OpenTelemetry | Complete Tutorial== 🌟](https://signoz.io/blog/opentelemetry-kubernetes-cluster-metrics-monitoring/)

## Kubernetes Logging

- [digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes)
- [papertrail.com: Quick and Easy Way to Implement Kubernetes Logging](https://www.papertrail.com/blog/quick-and-easy-way-to-implement-kubernetes-logging/) The SolarWinds® Papertrail™ team is excited to announce SolarWinds rKubeLog, an open-source project designed to streamline Kubernetes logging. rKubeLog allows you to forward logs to Papertrail from within a Kubernetes cluster without using a daemon or setting up application-level logging or a logging sidecar.
- [qlinh.com: Leveraging Kubernetes audit logs for threat detection](https://qlinh.com/infosec/2020/09/30/threat-detection-with-kubernetes-audit-logs.html) Kubernetes audit logs can provide great visibility into the operation and inner workings of your cluster. Learn how to leverage Kubernetes audit logs for threat detection
- [opensource.com: What you need to know about cluster logging in Kubernetes 🌟](https://opensource.com/article/21/11/cluster-logging-kubernetes) Explore how different container logging patterns in Kubernetes work.
- [==devopscube.com: Kubernetes Logging Tutorial For Beginners== 🌟](https://devopscube.com/kubernetes-logging-tutorial)
    - Logs are an essential aspect of observability and a critical tool for debugging. But Kubernetes logs have traditionally been unstructured strings, making any automated parsing difficult and any downstream processing, analysis, or querying challenging to do reliably.
    - In Kubernetes 1.19, we are adding support for structured logs, which natively support (key, value) pairs and object references. We have also updated many logging calls such that over 99% of logging volume in a typical deployment are now migrated to the structured format.
    - To maintain backwards compatibility, structured logs will still be outputted as a string where the string contains representations of those “key”=”value” pairs. Starting in alpha in 1.19, logs can also be outputted in JSON format using the --logging-format=json flag.
- [tealfeed.com: Kubernetes Audit Logs: Who created or deleted a namespace?](https://tealfeed.com/kubernetes-audit-logs-created-deleted-namespace-ho5o3) Learn how to set up log forwarding and collect audit logs that are passed through the Kubernetes API server to IBM Log Analysis to check who initiated a request and when they did so.
- [dev.to: Kubernetes Practice — Logging with Logstash and FluentD by Sidecar Container](https://dev.to/devopsvn/kubernetes-practice-logging-with-logstash-and-fluentd-by-sidecar-container-16oi)
- [signoz.io: Kubernetes Audit Logs - Best Practices And Configuration](https://signoz.io/blog/kubernetes-audit-logs)
- [kube-logging/logging-operator](https://github.com/kube-logging/logging-operator) The Logging operator automates the deployment and configuration of a Kubernetes logging pipeline. The operator deploys and configures a Fluent Bit daemonset on every node to collect container and application logs from the node file system.

## SLOs in Kubernetes

- [==thenewstack.io: Service Level Objectives in Kubernetes==](https://thenewstack.io/service-level-objectives-in-kubernetes/) an SLO is simply a metric, a goal for that metric, and a time period. For instance: “the success rate for service A must be at least 99.7% percent over the past 30 days.” The metric is known as the “service level indicator” (SLI) and the goal is the “objective.”
- [thenewstack.io: SLOs in Kubernetes, 1 Year Later](https://thenewstack.io/slos-in-kubernetes-1-year-later/)

## ECK Elastic Cloud on Kubernetes

- [elastic.co: How to configure Elastic Cloud on Kubernetes with SAML and hot-warm-cold architecture](https://www.elastic.co/es/blog/how-to-configure-elastic-cloud-on-kubernetes-with-saml-and-hot-warm-cold-architecture) Elastic Cloud on Kubernetes (ECK) is an easy way to get the Elastic Stack up and running on top of Kubernetes. That’s because ECK automates the deployment, provisioning, management, and setup of Elasticsearch, Kibana, Beats, and more.

## Telegraf Operator

- [influxdata.com: Expand Kubernetes Monitoring with Telegraf Operator](https://www.influxdata.com/blog/expand-kubernetes-monitoring-telegraf-operator)

## Monitoring Certificates Expiration


## kubeshark

- [==kubeshark.co==](https://kubeshark.co) The API Traffic Viewer for  kubernetes. Deep visibility and monitoring of all API traffic and payloads going in, out and across containers and pods inside a Kubernetes cluster.
- [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark) The API traffic viewer for Kubernetes providing deep visibility into all API traffic and payloads going in, out and across containers and pods inside a Kubernetes cluster. Think TCPDump and Wireshark re-invented for Kubernetes

## k8spacket


## Kubelog

- [kubelog.de](https://kubelog.de) kubelog is a graphical log viewer for Kubernetes, which works with your existing Kubernetes logging infrastructure. Kubelog is a log viewer for kubernetes. Tail multiple pods in one view and use searches to highlight and show results in context.

## Microsoft Retina eBPF

- [==github.com/microsoft/retina==](https://github.com/microsoft/retina) - [retina.sh](https://retina.sh) **eBPF distributed networking observability tool for Kubernetes**
    - Retina is a cloud-agnostic, open-source Kubernetes network observability platform that provides a centralized hub for monitoring application health, network health, and security. It provides actionable insights to cluster network administrators, cluster security administrators, and DevOps engineers navigating DevOps, SecOps, and compliance use cases.
    - Retina collects customizable telemetry, which can be exported to multiple storage options (such as Prometheus, Azure Monitor, and other vendors) and visualized in a variety of ways (like Grafana, Azure Log Analytics, and other vendors).

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5ofsNyHZwWE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>