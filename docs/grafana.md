# Grafana

1. [Introduction](#introduction)
2. [Grafana Agent](#grafana-agent)
3. [Grafana Faro](#grafana-faro)
4. [Grafana Mimir](#grafana-mimir)
5. [Grafana Dashboards](#grafana-dashboards)
6. [Grafana Releases](#grafana-releases)
7. [Grafana Loki](#grafana-loki)
8. [Grafana Beyla](#grafana-beyla)
9. [Grafana as Code](#grafana-as-code)

## Introduction

- [Grafana](https://grafana.com/)
- Prometheus utiliza plantillas de consola para los dashboards, si bien su curva de aprendizaje de sus múltiples funcionalidades es alta, con una interfaz de usuario insuficiente. Por este motivo es muy habitual utilizar **Grafana** como interfaz de usuario.
- [grafana.com: Provisioning Grafana 🌟](https://grafana.com/docs/grafana/latest/administration/provisioning/) Las últimas versiones de Grafana permiten la creación de "datasources" y "dashboards" con Ansible, mediante las opciones de provisión de Grafana. Funciona con cualquier "datasource" (Prometheus, InfluxDB, etc), incluyendo la configuración de Grafana correspondiente y dejando poco margen para el error humano.
    - [Grafana provisioning Ansible Role](https://github.com/cloudalchemy/ansible-grafana)
- [grafana.com: Introducing the new and improved New Relic plugin for Grafana](https://grafana.com/blog/2020/07/22/introducing-the-new-and-improved-new-relic-plugin-for-grafana/)
- [Log Monitoring and Alerting with Grafana Loki](https://www.infracloud.io/blogs/grafana-loki-log-monitoring-alerting)
- [magalix.com: Monitoring Kubernetes Clusters Through Prometheus & Grafana 🌟](https://www.magalix.com/blog/monitoring-of-kubernetes-cluster-through-prometheus-and-grafana)
- [itnext.io: Monitoring Kubernetes workloads with Prometheus and Thanos](https://itnext.io/monitoring-kubernetes-workloads-with-prometheus-and-thanos-4ddb394b32c)
- [medium: Why Grafana: Part II](https://medium.com/lightspeed-venture-partners/why-grafana-part-ii-2e7e42e0f7bb)
- [scylladb.com: Building a Grafana Backend Plugin](https://www.scylladb.com/2020/10/01/building-a-grafana-backend-plugin/)
- [thenewstack.io: Grafana Adds Logging to Its Enterprise Observability Stack 🌟](https://thenewstack.io/grafana-adds-logging-to-its-enterprise-observability-stack/)
- [openshift.com: Metrics-Driven Pod Constraints](https://www.openshift.com/blog/metrics-driven-pod-constraints)
- [thenewstack.io: Grafana 7.5: Controversial Pie Charts and Loki Alerts](https://thenewstack.io/grafana-7-5-controversial-pie-charts-and-loki-alerts/)
- [zdnet.com: Grafana 8.0 integrates with Prometheus alerting](https://www.zdnet.com/article/grafana-8-0-integrates-with-prometheus-alerting/) Alerting is finally unified in the latest update of the Grafana open source stack.
- [thenewstack.io: Grafana 8.0 Rethinks Alerts and Visualizations](https://thenewstack.io/grafana-8-0-rethinks-alerts-and-visualizations/)
- [youtube.com: Grafana Loki Promtail | Grafana Loki Setup And Configuration On CentOs](https://www.youtube.com/watch?v=iqpLXUdJ0Ro&ab_channel=Thetips4you)
- [grafana.com: What's new in Grafana Cloud for July 2021: Traces, live streaming, Kubernetes and Docker integrations, and more](https://grafana.com/blog/2021/07/06/whats-new-in-grafana-cloud-for-july-2021-traces-live-streaming-kubernetes-and-docker-integrations-and-more/)
- [thenewstack.io: Grafana Is Not Worried About AWS Commercialization](https://thenewstack.io/grafana-is-not-worried-about-aws-commercialization/)
- [grafana.com: Introducing the AWS CloudWatch integration, Grafana Cloud's first fully managed integration](https://grafana.com/blog/2021/11/17/2021/11/17/grafana-aws-cloudwatch-integration/) Latest integration available in Grafana Cloud: the AWS CloudWatch metrics integration, the first of our fully managed integrations that makes it simple to connect and visualize your data in Grafana.
- [grafana.com: Testing shift left observability with the Grafana Stack, OpenTelemetry, and k6](https://grafana.com/blog/2021/12/06/testing-shift-left-observability-with-the-grafana-stack-opentelemetry-and-k6/)
- [thenewstack.io: Will Grafana Become Easier to Use in 2022?](https://thenewstack.io/will-grafana-become-easier-to-use-in-2022)
- [grafana.com: Top 5 user-requested synthetic monitoring alerts in Grafana Cloud](https://grafana.com/blog/2022/01/11/top-5-user-requested-synthetic-monitoring-alerts-in-grafana-cloud/)
- [==grafana.com: A beginner's guide to network monitoring with Grafana and Prometheus==](https://grafana.com/blog/2022/01/19/a-beginners-guide-to-network-monitoring-with-grafana-and-prometheus/)
    - https://github.com/prometheus/snmp_exporter/tree/main/snmp-mixin
- [==grafana.com: A 3-step guide to troubleshooting and visualizing Kubernetes with Grafana Cloud==](https://grafana.com/blog/2021/11/19/a-3-step-guide-to-troubleshooting-and-visualizing-kubernetes-with-grafana-cloud/)
- [grafana.com: Video: How to build a Prometheus query in Grafana](https://grafana.com/blog/2022/01/27/video-how-to-build-a-prometheus-query-in-grafana/)
- [grafana.com: An advanced guide to network monitoring with Grafana and Prometheus](https://grafana.com/blog/2022/02/01/an-advanced-guide-to-network-monitoring-with-grafana-and-prometheus/)
- [==devopscube.com: How To Setup Grafana On Kubernetes==](https://devopscube.com/setup-grafana-kubernetes/)
- [infoq.com: Grafana Cloud Adds Incident and On-Call Management Solutions](https://www.infoq.com/news/2022/02/grafana-incident-oncall/)
- [alexandrev.medium.com: Grafana Alerting vs AlertManager: A Comparison of Two Leading Monitoring Tools | Alex Vazquez](https://alexandrev.medium.com/grafana-alerting-vs-alertmanager-a-comparison-of-two-leading-monitoring-tools-5e262446a5f9)
- [linkedin.com/pulse: Automatización de procesos con Prometheus, Grafana y WebHook: resolución autónoma de incidentes](https://www.linkedin.com/pulse/automatizaci%C3%B3n-de-procesos-con-prometheus-grafana-y-v%C3%ADctor-vela-l%C3%B3pez-1e/)
- [devops.com: Grafana Labs Acquires Asserts.ai to Bring AI to Observability](https://devops.com/grafana-labs-acquires-assert-ai-to-bring-ai-to-observability/)
- [grafana.com: Why companies choose Grafana Cloud over self-managed OSS stacks](https://grafana.com/blog/2023/10/16/why-companies-choose-grafana-cloud-over-self-managed-oss-stacks/)

## Grafana Agent

- [grafana/agent: Grafana Agent](https://github.com/grafana/agent) Prometheus Metrics, Loki Logs, and Tempo Traces, optimized for Grafana Cloud.
- [sid-infinity-yadav.medium.com: Grafana Agent Kubernetes Operator](https://sid-infinity-yadav.medium.com/grafana-agent-kubernetes-operator-f89b744487f5)
- [levelup.gitconnected.com: Grafana Agent Flow: Simplifying Monitoring and Telemetry Collection for Kubernetes Clusters](https://levelup.gitconnected.com/exploring-grafana-agent-flow-simplifying-monitoring-for-kubernetes-2a06a92614)

## Grafana Faro

- [Grafana Faro 🌟](https://grafana.com/oss/faro/) A project for frontend application observability, Grafana Faro includes a highly configurable web SDK for real user monitoring (RUM) that instruments browser frontend applications to capture observability signals. The frontend telemetry can then be correlated with backend and infrastructure data for seamless, full-stack observability.
- [grafana.com: Introducing Grafana Faro, an open source project for frontend application observability](https://grafana.com/blog/2022/11/02/introducing-grafana-faro-oss-application-observability/)

## Grafana Mimir

- [github.com/grafana/mimir](https://github.com/grafana/mimir) Grafana Mimir provides horizontally scalable, highly available, multi-tenant, long-term storage for Prometheus.

## Grafana Dashboards

- [Grafana Dashboards](https://grafana.com/grafana/dashboards)
- [github.com/DevOps-Nirvana/Grafana-Dashboards](https://github.com/DevOps-Nirvana/Grafana-Dashboards) In this repository, you will find a variety of open-source Grafana dashboards, typically for AWS and Kubernetes
- [github.com/mlabouardy: Grafana Dashboards](https://github.com/mlabouardy/grafana-dashboards)
- [openlogic.com: How to develop Grafana Dashboards 🌟](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana)
- [Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus 🌟](https://github.com/percona/grafana-dashboards)
- [Prometheus Monitoring With Grafana. Prometheus Stats Dashboard and Prometheus Benchmark Dashboard](https://dzone.com/articles/prometheus-monitoring-with-grafana). How you construct your Prometheus monitoring dashboard involves trial and error. Grafana makes this exploration very easy and Prometheus has good built-in functionality.
- [Popular community plugins that can improve your Grafana dashboards 🌟](https://grafana.com/blog/2020/08/26/popular-community-plugins-that-can-improve-your-grafana-dashboards/)
- [CISCO DNA Center with Grafana Dashboard](https://hawar.no/2020/09/cisco-dna-center-with-grafana-dashboard/)
- [prskavec.net: Grafana dashboards and Jsonnet](https://www.prskavec.net/post/grafana-jsonnet/) Simple way how to make your dashboard easy to maintain.
- [percona.com: Tips for Designing Grafana Dashboards](https://www.percona.com/blog/2019/11/22/designing-grafana-dashboards/)
- [devblogs.microsoft.com:Monitoring Azure by using Grafana dashboards 🌟](https://devblogs.microsoft.com/devops/monitoring-azure-by-using-grafana-dashboards/)
- [github.com/kubevirt/monitoring](https://github.com/kubevirt/monitoring) KubeVirt monitoring dashboards. This repository collects Grafana dashboards for KubeVirt and Prometheus runbooks for alerts shipped with the KubeVirt stack.
- [medium.com/@dotdc: A set of modern Grafana dashboards for Kubernetes 🌟](https://medium.com/@dotdc/a-set-of-modern-grafana-dashboards-for-kubernetes-4b989c72a4b2) In this article, I will present a set of modern Grafana dashboards I made for Kubernetes, explain why I decided to create them and how they work.
- [grafana.com: Grafana dashboards: A complete guide to all the different types you can build](https://grafana.com/blog/2022/06/06/grafana-dashboards-a-complete-guide-to-all-the-different-types-you-can-build/)
- [blog.bespinian.io: Creating Grafana Dashboards for Node.js Apps on Kubernetes](https://blog.bespinian.io/posts/creating-grafana-dashboards-for-nodejs-on-kubernetes/) While Grafana and Prometheus are relatively easy to understand, creating useful dashboards requires familiarity with PromQL and Prometheus’ data model. In this article, you'll learn how to create a dashboard for a Node.js app deployed on Kubernetes.
- [medium.com/how-tos: How To Provisioning Dashboards In Grafana via Kubernetes](https://medium.com/how-tos/how-to-provisioning-dashboards-in-grafana-via-kubernetes-5d261508658d) Create a nice Dashboard that matches your needs
- [==github.com/dotdc/grafana-dashboards-kubernetes== 🌟](https://github.com/dotdc/grafana-dashboards-kubernetes)
- [github.com/onzack/grafana-dashboards](https://github.com/onzack/grafana-dashboards) Grafana Dashboards for Kubernetes, OpenShift and other systems

Monitored Component|Collector|Dashboard Number|URL
:------------------|:-------|:---------------|------------
ActiveMQ 5.x "classic"|[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)|[10702](https://grafana.com/grafana/dashboards/10702)|[Ref1](https://docs.wavefront.com/activemq.html), [Ref2](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/activemq), [Ref3](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/activemq.yml), [Ref4](https://stackoverflow.com/questions/57107282/prometheus-and-activemq-integration)
ActiveMQ Artemis/Red Hat AMQ Broker|[JMX Exporter](https://github.com/prometheus/jmx_exporter)|[9087](https://grafana.com/grafana/dashboards/9087)|[Ref1](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/artemis-2.yml), [Ref2](http://techiekhannotes.blogspot.com/2018/12/artemis-monitoring-with-grafana.html), [Ref3](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin)
Message Streams like Kafka/Red Hat AMQ Streams|Other|[9777](https://grafana.com/grafana/dashboards/9777)|

## Grafana Releases

- [Open source observability, meet data transformation: Grafana 7.0 promises to connect, unify, and visualize all your data](https://www.zdnet.com/article/open-source-observability-meet-data-transformation-grafana-7-0-promises-to-connect-unify-and-visualize-all-your-data/) Grafana Labs sets the bar for open source observability with Grafana 7.0: more developer friendly, more data sources, data transformation, and growth in the cloud and on premise
- [Grafana 7.0: “We’ve built one of the best visualisation tools and it’s not tied to any one database”](https://jaxenter.com/grafana-7-0-interview-tom-wilkie-172261.html)
- [grafana.com: Grafana 8.1 released: New Geomap and Annotations panels, updated plugin management, and more](https://grafana.com/blog/2021/08/05/grafana-8.1-released-new-geomap-and-annotations-panels-updated-plugin-management-and-more/)
- [thenewstack.io: Grafana 8.2 Wants to ‘Democratize’ Cloud Native Metrics](https://thenewstack.io/grafana-wants-to-democratize-cloud-native-metrics/)
- [grafana.com: Grafana Labs and Microsoft partner to deliver new first party Microsoft Azure service](https://grafana.com/about/press/2021/11/10/grafana-labs-and-microsoft-partner-to-deliver-new-first-party-microsoft-azure-service) Today we announced a partnership with Microsoft that lets customers run Grafana natively within their Azure cloud platform.
- [grafana.com: Grafana 9.3 feature: Grafana OAuth token improvements](https://grafana.com/blog/2022/12/08/grafana-9.3-feature-grafana-oauth-token-improvements/?mdm=social)

## Grafana Loki

- [Grafana Loki](https://grafana.com/oss/loki/)
- [itnext.io: Logging in Kubernetes with Loki and the PLG Stack](https://itnext.io/logging-in-kubernetes-with-loki-and-the-plg-stack-93b27c90ec34) Loki is a new log aggregation system from Grafana Labs. It is designed to be cost-effective and easy to operate. In this article, you learn more about Loki and how to use the PLG Stack (Promtail, Loki, Grafana) for logging in Kubernetes.
- [medium.com/devopsturkiye: Deploy Grafana Loki and Promtail using ArgoCD](https://medium.com/devopsturkiye/deploy-grafana-loki-and-promtail-using-argocd-416b2fd4539f)
- [faun.pub: Manage Grafana Loki alerting and recording rules using GitOps](https://faun.pub/manage-grafana-lokis-alerting-and-recording-rules-using-gitops-c26d06d772c6)
- [cleancloud-k8s.com: Handling Multiline Logs with Loki and Fluent Bit on Kubernetes](https://cleancloud-k8s.com/2022/01/19/handling-multiline-logging-with-loki-and-fluent-bit-on-kubernetes/) In this blog post, you will learn how to handle multiline logs such as Java stack traces with Loki and Fluent Bit on Kubernetes.
- [faun.pub: Grafana, Prometheus, and Loki: Exploring Metrics and Logs](https://faun.pub/grafana-prometheus-and-loki-exploring-metrics-and-logs-f198637784fc)

## Grafana Beyla

- [grafana.com: Grafana Beyla 1.0 release: zero-code instrumentation for application telemetry using eBPF](https://grafana.com/blog/2023/11/14/grafana-beyla-1.0-release-zero-code-instrumentation-for-application-telemetry-using-ebpf/)

## Grafana as Code

- [grafana.com: A complete guide to managing Grafana as code: tools, tips, and tricks](https://grafana.com/blog/2022/12/06/a-complete-guide-to-managing-grafana-as-code-tools-tips-and-tricks/)