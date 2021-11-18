# Grafana
- [Introduction](#introduction)
- [Grafana Dashboards](#grafana-dashboards)
- [Grafana Releases](#grafana-releases)
- [Grafana Loki](#grafana-loki)

## Introduction
* [Grafana](https://grafana.com/) 
* Prometheus utiliza plantillas de consola para los dashboards, si bien su curva de aprendizaje de sus múltiples funcionalidades es alta, con una interfaz de usuario insuficiente. Por este motivo es muy habitual utilizar **Grafana** como interfaz de usuario.
* [grafana.com: Provisioning Grafana 🌟](https://grafana.com/docs/grafana/latest/administration/provisioning/) Las últimas versiones de Grafana permiten la creación de "datasources" y "dashboards" con Ansible, mediante las opciones de provisión de Grafana. Funciona con cualquier "datasource" (Prometheus, InfluxDB, etc), incluyendo la configuración de Grafana correspondiente y dejando poco margen para el error humano.
    * [Grafana provisioning Ansible Role](https://github.com/cloudalchemy/ansible-grafana)
* [grafana.com: Introducing the new and improved New Relic plugin for Grafana](https://grafana.com/blog/2020/07/22/introducing-the-new-and-improved-new-relic-plugin-for-grafana/)
* [Log Monitoring and Alerting with Grafana Loki](https://www.infracloud.io/blogs/grafana-loki-log-monitoring-alerting)
* [magalix.com: Monitoring Kubernetes Clusters Through Prometheus & Grafana 🌟](https://www.magalix.com/blog/monitoring-of-kubernetes-cluster-through-prometheus-and-grafana)
* [itnext.io: Monitoring Kubernetes workloads with Prometheus and Thanos](https://itnext.io/monitoring-kubernetes-workloads-with-prometheus-and-thanos-4ddb394b32c)
* [medium: Why Grafana: Part II](https://medium.com/lightspeed-venture-partners/why-grafana-part-ii-2e7e42e0f7bb)
* [scylladb.com: Building a Grafana Backend Plugin](https://www.scylladb.com/2020/10/01/building-a-grafana-backend-plugin/)
* [thenewstack.io: Grafana Adds Logging to Its Enterprise Observability Stack 🌟](https://thenewstack.io/grafana-adds-logging-to-its-enterprise-observability-stack/)
* [openshift.com: Metrics-Driven Pod Constraints](https://www.openshift.com/blog/metrics-driven-pod-constraints)
* [thenewstack.io: Grafana 7.5: Controversial Pie Charts and Loki Alerts](https://thenewstack.io/grafana-7-5-controversial-pie-charts-and-loki-alerts/)
* [zdnet.com: Grafana 8.0 integrates with Prometheus alerting](https://www.zdnet.com/article/grafana-8-0-integrates-with-prometheus-alerting/) Alerting is finally unified in the latest update of the Grafana open source stack.
* [thenewstack.io: Grafana 8.0 Rethinks Alerts and Visualizations](https://thenewstack.io/grafana-8-0-rethinks-alerts-and-visualizations/)
* [youtube.com: Grafana Loki Promtail | Grafana Loki Setup And Configuration On CentOs](https://www.youtube.com/watch?v=iqpLXUdJ0Ro&ab_channel=Thetips4you)
* [grafana.com: What's new in Grafana Cloud for July 2021: Traces, live streaming, Kubernetes and Docker integrations, and more](https://grafana.com/blog/2021/07/06/whats-new-in-grafana-cloud-for-july-2021-traces-live-streaming-kubernetes-and-docker-integrations-and-more/)
* [thenewstack.io: Grafana Is Not Worried About AWS Commercialization](https://thenewstack.io/grafana-is-not-worried-about-aws-commercialization/)
* [grafana.com: Introducing the AWS CloudWatch integration, Grafana Cloud's first fully managed integration](https://grafana.com/blog/2021/11/17/2021/11/17/grafana-aws-cloudwatch-integration/) Latest integration available in Grafana Cloud: the AWS CloudWatch metrics integration, the first of our fully managed integrations that makes it simple to connect and visualize your data in Grafana.

## Grafana Dashboards
* [Grafana Dashboards](https://grafana.com/grafana/dashboards)
* [github.com/mlabouardy: Grafana Dashboards](https://github.com/mlabouardy/grafana-dashboards)
* [openlogic.com: How to develop Grafana Dashboards 🌟](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana)
* [Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus 🌟](https://github.com/percona/grafana-dashboards)
* [Prometheus Monitoring With Grafana. Prometheus Stats Dashboard and Prometheus Benchmark Dashboard](https://dzone.com/articles/prometheus-monitoring-with-grafana). How you construct your Prometheus monitoring dashboard involves trial and error. Grafana makes this exploration very easy and Prometheus has good built-in functionality.
* [Popular community plugins that can improve your Grafana dashboards 🌟](https://grafana.com/blog/2020/08/26/popular-community-plugins-that-can-improve-your-grafana-dashboards/)
* [CISCO DNA Center with Grafana Dashboard](https://hawar.no/2020/09/cisco-dna-center-with-grafana-dashboard/)
* [prskavec.net: Grafana dashboards and Jsonnet](https://www.prskavec.net/post/grafana-jsonnet/) Simple way how to make your dashboard easy to maintain.
* [percona.com: Tips for Designing Grafana Dashboards](https://www.percona.com/blog/2019/11/22/designing-grafana-dashboards/)
* [devblogs.microsoft.com:Monitoring Azure by using Grafana dashboards 🌟](https://devblogs.microsoft.com/devops/monitoring-azure-by-using-grafana-dashboards/)
* [github.com/kubevirt/monitoring](https://github.com/kubevirt/monitoring) KubeVirt monitoring dashboards. This repository collects Grafana dashboards for KubeVirt and Prometheus runbooks for alerts shipped with the KubeVirt stack.

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

## Grafana Loki
- [Grafana Loki](https://grafana.com/oss/loki/)
- [itnext.io: Logging in Kubernetes with Loki and the PLG Stack](https://itnext.io/logging-in-kubernetes-with-loki-and-the-plg-stack-93b27c90ec34) Loki is a new log aggregation system from Grafana Labs. It is designed to be cost-effective and easy to operate. In this article, you learn more about Loki and how to use the PLG Stack (Promtail, Loki, Grafana) for logging in Kubernetes.