# Kubernetes Monitoring

!!! info "Architectural Context"
    Detailed reference for Kubernetes Monitoring in the context of The Container Stack.

## Table of Contents

---

  - [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://www.sysdig.com/blog/kubernetes-monitoring-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Monitoring Kubernetes in Production](https://www.sysdig.com/blog/monitoring-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: How to monitor Kubernetes control plane](https://www.sysdig.com/blog/monitor-kubernetes-control-plane)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft.sh: Kubernetes Cost Monitoring with Prometheus & Grafana](https://www.vcluster.com/blog/kubernetes-cost-monitoring-with-prometheus-and-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [8 Best Kubernetes monitoring tools; Paid & open-source](https://middleware.io/blog/kubernetes-monitoring/tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rcarrata.com: Network Observability Deep Dive in Kubernetes with NetObserv Operator](https://rcarrata.github.io/observability/netobserv-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.palark.com: Service communication monitoring in Kubernetes with NetFlow](https://palark.com/blog/kubernetes-services-interaction-monitoring-with-netflow)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubeshark.co](https://www.immo-pop.com/login)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Monitoring Distributed Systems - Google SRE Book](https://sre.google/sre-book/monitoring-distributed-systems)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Prometheus and OpenTelemetry Compatibility Issues](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [prometheus-community/kube-prometheus-stack 🌟🌟](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: 12 Critical Kubernetes Health Conditions You Need to Monitor](https://thenewstack.io/12-critical-kubernetes-health-conditions-you-need-to-monitor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [circonus.com: 12 Critical Kubernetes Health Conditions You Need to Monitor and Why](https://www.circonus.com/2020/12/12-critical-kubernetes-health-conditions-you-need-to-monitor-and-why)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [circonus.com: Guide to Kubernetes Monitoring: Part 1](https://www.circonus.com/2020/09/guide-to-kubernetes-monitoring-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Monitoring Kubernetes cert-manager Certificates with BotKube](https://www.infracloud.io/blogs/monitoring-kubernetes-cert-manager-certificates)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube-state-metrics 🌟](https://github.com/kubernetes/kube-state-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Monitoring Kubernetes Jobs](https://itnext.io/monitoring-kubernetes-jobs-8adc241a7b60)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubermatic.com: The Complete Guide to Kubernetes Metrics](https://www.kubermatic.com/blog/the-complete-guide-to-kubernetes-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube.com: Cloud Quick POCs - Kubernetes monitoring metrics using Grafana Cloud on AWS EKS | Observability | Grafana](https://www.youtube.com/watch?v=FVDHWPxK5nU&ab_channel=CloudQuickPOCs)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [anaisurl.com: Full Tutorial: Monitoring and Troubleshooting stack with Prometheus, Grafana, Loki and Komodor 🌟](https://anaisurl.com/full-tutorial-monitoring)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: How to tackle Kubernetes observability challenges with Pixie](https://itnext.io/how-to-tackle-kubernetes-observability-challenges-with-pixie-4c6414ca913)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Monitoring Kubernetes cluster logs and metrics using Grafana, Prometheus and Loki](https://dev.to/leroykayanda/kubernetes-monitoring-using-grafana-3dhc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [middlewareinventory.com: Get CPU and Memory Usage of NODES and PODS – Kubectl 🌟](https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterstack.com: 10 Best Kubernetes Monitoring Tools in 2022 🌟](https://betterstack.com/community/comparisons/kubernetes-monitoring-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [adamtheautomator.com: Utilizing Grafana & Prometheus Kubernetes Cluster Monitoring 🌟](https://adamtheautomator.com/prometheus-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/mikeyglitz: Proactive Kubernetes Monitoring with Alerting](https://dev.to/mikeyglitz/proactive-kubernetes-monitoring-with-alerting-58en)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [isovalent.com: What are the 4 Golden Signals for Monitoring Kubernetes?](https://isovalent.com/blog/post/what-are-the-4-golden-signals-for-monitoring-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [grafana.com: How to manage high cardinality metrics in Prometheus and Kubernetes](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.fourninecloud.com: Kubernetes monitoring — How to monitor using prometheus?](https://blog.fourninecloud.com/kubernetes-monitoring-how-to-monitor-using-prometheus-f2eff767f6bb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [newrelic.com: Pixie](https://newrelic.com/platform/kubernetes-pixie)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [grafana.com: A beginner's guide to Kubernetes application monitoring](https://grafana.com/blog/2023/01/31/a-beginners-guide-to-kubernetes-application-monitoring)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.amazon.com: Using Prometheus to Avoid Disasters with Kubernetes CPU Limits 🌟](https://aws.amazon.com/blogs/containers/using-prometheus-to-avoid-disasters-with-kubernetes-cpu-limits)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes: monitoring with Prometheus — exporters, a Service Discovery, and its roles](https://itnext.io/kubernetes-monitoring-with-prometheus-exporters-a-service-discovery-and-its-roles-ce63752e5a1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opentelemetry.io: Creating a Kubernetes Cluster with Runtime Observability](https://opentelemetry.io/blog/2023/k8s-runtime-observability)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [signoz.io: Kubernetes Cluster Monitoring with OpenTelemetry | Complete Tutorial 🌟](https://signoz.io/blog/opentelemetry-kubernetes-cluster-metrics-monitoring)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bul: Interactive TUI for Exploring Kubernetes Container Logs](https://github.com/ynqa/bul)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [digitalocean.com: How To Set Up an Elasticsearch, Fluentd and Kibana (EFK) Logging Stack on Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [papertrail.com: Quick and Easy Way to Implement Kubernetes Logging](https://www.papertrail.com/blog/quick-and-easy-way-to-implement-kubernetes-logging)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [qlinh.com: Leveraging Kubernetes audit logs for threat detection](https://qlinh.com/infosec/2020/09/30/threat-detection-with-kubernetes-audit-logs.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Logging in Production](https://itnext.io/kubernetes-logging-in-production-545ea88d9a4a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: What you need to know about cluster logging in Kubernetes 🌟](https://opensource.com/article/21/11/cluster-logging-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: Kubernetes Logging Tutorial For Beginners 🌟](https://devopscube.com/kubernetes-logging-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tealfeed.com: Kubernetes Audit Logs: Who created or deleted a namespace?](https://tealfeed.com/kubernetes-audit-logs-created-deleted-namespace-ho5o3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Kubernetes Practice — Logging with Logstash and FluentD by Sidecar Container](https://dev.to/devopsvn/kubernetes-practice-logging-with-logstash-and-fluentd-by-sidecar-container-16oi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [signoz.io: Kubernetes Audit Logs - Best Practices And Configuration](https://signoz.io/blog/kubernetes-audit-logs)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube-logging/logging-operator](https://github.com/kube-logging/logging-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Service Level Objectives in Kubernetes](https://thenewstack.io/service-level-objectives-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: SLOs in Kubernetes, 1 Year Later](https://thenewstack.io/slos-in-kubernetes-1-year-later)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [elastic.co: How to configure Elastic Cloud on Kubernetes with SAML and hot-warm-cold architecture](https://www.elastic.co/es/blog/how-to-configure-elastic-cloud-on-kubernetes-with-saml-and-hot-warm-cold-architecture)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [influxdata.com: Expand Kubernetes Monitoring with Telegraf Operator](https://www.influxdata.com/blog/expand-kubernetes-monitoring-telegraf-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Monitoring Certificates Expiration in Kubernetes with X.509 Exporter](https://itnext.io/monitoring-certificates-expiration-in-kubernetes-with-x-509-exporter-8030b69f611d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Sharing a NVIDIA GPU Between Pods in Kubernetes](https://www.cloudnativedeepdive.com/sharing-a-nvidia-gpu-between-pods-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubelog.de](https://kubelog.de)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/microsoft/retina](https://github.com/microsoft/retina)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
