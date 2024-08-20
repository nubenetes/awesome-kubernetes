# Monitoring and Performance. Prometheus, Grafana, APMs and more

1. [Monitoring and Observability](#monitoring-and-observability)
    1. [Profiling](#profiling)
    2. [Key Performance Indicator (KPI)](#key-performance-indicator-kpi)
2. [OpenShift Cluster Monitoring Built-in solutions](#openshift-cluster-monitoring-built-in-solutions)
    1. [OpenShift 3.11 Metrics and Logging](#openshift-311-metrics-and-logging)
        1. [Prometheus and Grafana](#prometheus-and-grafana)
        2. [Custom Grafana Dashboard for OpenShift 3.11](#custom-grafana-dashboard-for-openshift-311)
        3. [Capacity Management Grafana Dashboard](#capacity-management-grafana-dashboard)
        4. [Software Delivery Metrics Grafana Dashboard](#software-delivery-metrics-grafana-dashboard)
        5. [Prometheus for OpenShift 3.11](#prometheus-for-openshift-311)
    2. [OpenShift 4](#openshift-4)
3. [Monitoring micro-front ends on kubernetes with NGINX](#monitoring-micro-front-ends-on-kubernetes-with-nginx)
4. [Prometheus vs OpenTelemetry](#prometheus-vs-opentelemetry)
5. [Prometheus](#prometheus)
6. [Grafana](#grafana)
7. [Kibana](#kibana)
8. [Prometheus and Grafana Interactive Learning](#prometheus-and-grafana-interactive-learning)
9. [Logging \& Centralized Log Management](#logging--centralized-log-management)
    1. [ElasticSearch](#elasticsearch)
        1. [Elastic Cloud on Kubernetes (ECK)](#elastic-cloud-on-kubernetes-eck)
    2. [OpenSearch](#opensearch)
    3. [EFK ElasticSearch Fluentd Kibana](#efk-elasticsearch-fluentd-kibana)
    4. [Logstash Grok for Log Parsing](#logstash-grok-for-log-parsing)
10. [Internet Performance Monitoring (IPM)](#internet-performance-monitoring-ipm)
11. [Performance](#performance)
12. [List of Performance Analysis Tools](#list-of-performance-analysis-tools)
     1. [Thread Dumps. Debugging Java Applications](#thread-dumps-debugging-java-applications)
13. [Debugging Java Applications on OpenShift and Kubernetes](#debugging-java-applications-on-openshift-and-kubernetes)
14. [Distributed Tracing. OpenTelemetry and Jaeger](#distributed-tracing-opentelemetry-and-jaeger)
     1. [Microservice Observability with Distributed Tracing. OpenTelemetry.io](#microservice-observability-with-distributed-tracing-opentelemetryio)
         1. [OpenTelemetry Operator](#opentelemetry-operator)
     2. [Jaeger VS OpenTelemetry. How Jaeger works with OpenTelemetry](#jaeger-vs-opentelemetry-how-jaeger-works-with-opentelemetry)
     3. [Jaeger vs Zipkin](#jaeger-vs-zipkin)
     4. [Grafana Tempo distributed tracing system](#grafana-tempo-distributed-tracing-system)
15. [Application Performance Management (APM)](#application-performance-management-apm)
     1. [Elastic APM](#elastic-apm)
     2. [Dynatrace APM](#dynatrace-apm)
16. [Message Queue Monitoring](#message-queue-monitoring)
     1. [Red Hat AMQ 7 Broker Monitoring solutions based on Prometheus and Grafana](#red-hat-amq-7-broker-monitoring-solutions-based-on-prometheus-and-grafana)
17. [Serverless Monitoring](#serverless-monitoring)
18. [Distributed Tracing in Apache Beam](#distributed-tracing-in-apache-beam)
19. [Krossboard Converged Kubernetes usage analytics](#krossboard-converged-kubernetes-usage-analytics)
20. [Instana APM](#instana-apm)
21. [Monitoring Etcd](#monitoring-etcd)
22. [Zabbix](#zabbix)
23. [VictoriaMetrics and VictoriaLogs](#victoriametrics-and-victorialogs)
24. [Other Tools](#other-tools)
25. [Other Awesome Lists](#other-awesome-lists)
26. [Slides](#slides)
27. [Tweets](#tweets)

## Monitoring and Observability

- [Wikipedia: Application Performance Index](https://en.wikipedia.org/wiki/Apdex)
- [thenewstack.io: The Challenges of Monitoring Kubernetes and OpenShift](https://thenewstack.io/the-challenges-of-monitoring-kubernetes-and-openshift/)
- [dzone.com: Kubernetes Monitoring: Best Practices, Methods, and Existing Solutions](https://dzone.com/articles/kubernetes-monitoring-best-practices-methods-and-e) Kubernetes handles containers in several computers, removing the complexity of handling distributed processing. But what's the best way to perform Kubernetes monitoring?
- [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb/)
- [Dzone: Comparison of Open Source API Analytics and Monitoring Tools 🌟](https://dzone.com/articles/comparison-of-open-source-api-analytics-and-monito) There are a variety of open-source projects you can leverage to build a complete API analytics platform. This articles compares them.
- [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://sysdig.com/blog/kubernetes-monitoring-best-practices/)
- [CNCF End User Technology Radar: Observability, September 2020 🌟](https://www.cncf.io/blog/2020/09/11/cncf-end-user-technology-radar-observability-september-2020/)
- [magalix.com: Monitoring Kubernetes Clusters Through Prometheus & Grafana 🌟](https://www.magalix.com/blog/monitoring-of-kubernetes-cluster-through-prometheus-and-grafana)
- [instana.com: The Hidden Cost of Observability: Data Volume](https://www.instana.com/blog/cf-the-hidden-cost-of-observability-data-volume/)
- [learnsteps.com: Monitoring Infrastructure System Design](https://www.learnsteps.com/monitoring-infrastructure-system-design/)
- [bravenewgeek.com: The Observability Pipeline](https://bravenewgeek.com/the-observability-pipeline/)
- [thenewstack.io: 3 Key Configuration Challenges for Kubernetes Monitoring with Prometheus](https://thenewstack.io/3-key-configuration-challenges-for-kubernetes-monitoring-with-prometheus/)
- [sysdig.com: Kubernetes Monitoring with Prometheus, the ultimate guide 🌟](https://sysdig.com/blog/kubernetes-monitoring-prometheus/)
- [sysdig.com: How to monitor kube-proxy 🌟](https://sysdig.com/blog/monitor-kube-proxy/) In this article, you will learn how to monitor kube-proxy to ensure the correct health of your cluster network.
- [thenewstack.io: Monitoring vs. Observability: What’s the Difference?](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/)
- [getenroute.io: TSDB, Prometheus, Grafana In Kubernetes: Tracing A Variable Across The OSS Monitoring Stack](https://getenroute.io/blog/leverage-open-source-oss-derive-insights-grafana-prometheus-tsdb-kubernetes-standalone-api-gateway/)
- [dashbird.io: Monitoring vs Observability: Can you tell the difference? 🌟](https://dashbird.io/blog/monitoring-vs-observability/)
- [thenewstack.io: Monitoring as Code: What It Is and Why You Need It 🌟](https://thenewstack.io/monitoring-as-code-what-it-is-and-why-you-need-it/)
- [thenewstack.io: Observability Won’t Replace Monitoring (Because It Shouldn’t) 🌟](https://thenewstack.io/observability-wont-replace-monitoring-because-it-shouldnt/)
- [devopscurry.com: Understanding Container Monitoring and popular Container Monitoring Tools in 2021](https://devopscurry.com/understaning-container-monitoring-and-popular-container-monitoring-tools-in-2021/)
- [matiasmct.medium.com: Observability at Scale](https://matiasmct.medium.com/observability-at-scale-52d0d9a5fb9b)
- [dynatrace.com: How to solve the challenges of multicloud AWS, Azure and GCP observability](https://www.dynatrace.com/news/blog/how-to-solve-the-challenges-of-multicloud-aws-azure-and-gcp-observability/)
- [logz.io: Top 11 Open Source Monitoring Tools for Kubernetes 🌟](https://logz.io/blog/open-source-monitoring-tools-for-kubernetes/)
    - [logz.io: Unified Observability: Announcing Kubernetes 360](https://logz.io/blog/unified-observability-kubernetes-360/) A single, unified platform combining a true log analytics solution, the best Prometheus metrics monitoring, and the value of distributed tracing powered by Jaeger that enables DevOps teams to monitor application SLOs in a simple, efficient and actionable manner.
- [thenewstack.io: Kubernetes Observability Challenges in Cloud Native Architecture 🌟](https://thenewstack.io/kubernetes-observability-challenges-in-cloud-native-architecture/)
- [opsdis.com: Building a custom monitoring solution with Grafana, Prometheus and Loki](https://opsdis.com/custom-monitoring-solution-with-grafana-prometheus-and-loki/)
- [harness.io: Metrics to Improve Continuous Integration Performance](https://harness.io/blog/continuous-integration/continuous-integration-performance-metrics/)
- [thenewstack.io: Best Practices to Optimize Infrastructure Monitoring within DevOps Teams](https://thenewstack.io/best-practices-to-optimize-infrastructure-monitoring-within-devops-teams/)
- [faun.pub: DevOps Meets Observability 🌟](https://faun.pub/devops-meets-observability-78775c021b0e)
- [skilledfield.com.au: Monitoring Kubernetes and Docker Container Logs](https://skilledfield.com.au/monitoring-kubernetes-and-docker-container-logs/)
- [thenewstack.io: Growing Adoption of Observability Powers Business Transformation](https://thenewstack.io/growing-adoption-of-observability-powers-business-transformation/)
- [blog.thundra.io: What CI Observability Means for DevOps 🌟](https://blog.thundra.io/what-ci-observability-means-for-devops)
- [thenewstack.io: Monitoring API Latencies After Releases: 4 Mistakes to Avoid](https://thenewstack.io/monitoring-api-latencies-after-releases-4-mistakes-to-avoid) Find 4 common mistakes engineers make when using histograms to monitor API latencies from release to release.
- [thenewstack.io: Monitoring API Latencies After Releases: 4 Mistakes to Avoid](https://thenewstack.io/monitoring-api-latencies-after-releases-4-mistakes-to-avoid/)
- [thenewstack.io: DevOps Observability from Code to Cloud](https://thenewstack.io/devops-observability-from-code-to-cloud/)
- [ortelius.io: Microservice Monitoring and Visualization with Ortelius open source project](https://ortelius.io/blog/2021/03/26/microservice-monitoring-and-visualization/)
- [thenewstack.io: CI Observability for Effective Change Management 🌟](https://thenewstack.io/ci-observability-for-effective-change-management/)
- [thenewstack.io: Monitor Your Containers with Sysdig](https://thenewstack.io/monitor-your-containers-with-sysdig/)
- [thenewstack.io: Applying Basic vs. Advanced Monitoring Techniques](https://thenewstack.io/applying-basic-vs-advanced-monitoring-techniques/)
- [cloudforecast.io: cAdvisor and Kubernetes Monitoring Guide 🌟](https://cloudforecast.io/blog/cadvisor-and-kubernetes-monitoring-guide/)
- [hmh.engineering: Musings on microservice observability!](https://hmh.engineering/musings-on-microservice-observability-f7052ac42f04)
- [stackoverflow.blog: Observability is key to the future of software (and your DevOps career)](https://stackoverflow.blog/2021/09/08/observability-is-key-to-the-future-of-software-and-your-devops-career/) Observability platforms enable you to easily figure out what’s happening with every request and to identify the cause of issues fast. Learning the principles of observability and OpenTelemetry will set you apart from the crowd and provide you with a skill set that will be in increasing demand as more companies perform cloud migrations.
- [forbes.com: Who Should Own The Job Of Observability In DevOps?](https://www.forbes.com/sites/forbestechcouncil/2021/09/03/who-should-own-the-job-of-observability-in-devops/)
- [dzone: Monitoring Web Servers Should Never Be Complex](https://dzone.com/articles/monitoring-web-servers-should-never-be-complex) Monitoring Web Services can become very very complex. But what really is needed to detect a failure? And how can setup and simplify your monitoring?
- [dynatrace.com: What is observability? Not just logs, metrics and traces](https://www.dynatrace.com/news/blog/what-is-observability-2/)
- [thenewstack.io: Observability Is the New Kubernetes 🌟](https://thenewstack.io/observability-is-the-new-kubernetes/)
- [learnsteps.com: Logging Infrastructure System Design](https://www.learnsteps.com/logging-infrastructure-system-design/) Logging infrastructure system design is very important for each and every infrastructure as you need to look into logs. When you have a huge number of applications talking to each other there is an enormous amount of logs that they produce. Handling this amount of logs can be very costly and a headache. Let’s look at this problem for handling your logs at scale and Logging infrastructure System Design.
- [medium.com: Monitoring Microservices - Part 1: Observability | Anderson Carvalho](https://medium.com/geekculture/monitoring-microservices-part-1-observability-b2b44fa3e67e) Achieving observability with probes, logs, metrics, and traces. **The Observability Pyramid comprises Probes, Logs, Metrics, and Traces:**
    - **Probes:** Probes are often exposed as endpoints and used by external agents like load balancers, container orchestrators, application servers, and sysadmins before deciding what to do next. The most common probes are starting, ready, and live. The startup probe is on during the component bootstrap phase. The liveness probe is on from the time the component starts until it stops running. The readiness probe is on during the period where the component is ready/open to receive requests or process workload.
    - **Logs:** Logs are messages produced during the component execution that capture a piece of relevant information. Usually, we classify log messages into all, debug, info, warn, error, and fatal. Logs can produce a huge amount of data and contain sensitive information. A good practice is to apply different log levels depending on the environment.
    - **Log Aggregation:** Each component generates one or more log files. Since distributed systems are composed of multiples components, it’s a daunting and miserable task to dig into a bunch of log files during troubleshooting. Thus, log aggregation is highly recommended for Microservices.
    - **Metrics:** Metrics give us the visibility of good and bad events that happen inside of an application. Metrics help us to distinguish between normal and abnormal application behavior. Usually, we collect, count, summarize and compare events related to rate, errors, duration, and saturation to produce metrics.
    - **Traces:** Traces record the flow of data between different components and execution details of each one along the way. By tracing we can discover the relationships, dependencies between components, identify bottlenecks, comprehend the data flow, and the time span on each component.
- [infoworld.com: The RED method: A new strategy for monitoring microservices](https://www.infoworld.com/article/3638693/the-red-method-a-new-strategy-for-monitoring-microservices.html) By using the RED metrics—rate, error, and duration—you can get a solid understanding of how your services are performing for end-users.
- [intellipaat.com: Top 10 DevOps Monitoring Tools](https://intellipaat.com/blog/devops-monitoring-tools) Are you a DevOps engineer? Are you confused about which DevOps monitoring tools to use for monitoring? If so, go through this comprehensive blog to know more about different types of DevOps monitoring tools, their purpose, and their importance.
- [==cncf.io: How to add observability to your application pipeline==](https://www.cncf.io/blog/2021/11/23/how-to-add-observability-to-your-application-pipeline/)
- [storiesfromtheherd.com: Unpacking Observability](https://storiesfromtheherd.com/unpacking-observability-a-beginners-guide-833258a0591f)
- [logz.io: A Monitoring Reality Check: More of the Same Won’t Work](https://logz.io/blog/monitoring-reality-check/)
- [medium.com/buildpiper: Observability for Monitoring Microservices — Top 5 Ways!](https://medium.com/buildpiper/observability-for-monitoring-microservices-top-5-ways-587871e726d0) Knowing what’s running inside the container, how the application and code are performing is critical for tackling important issues. Discussed here are some important Microservices monitoring tools and approaches. Take a look!
- [medium.com/@cbkwgl: Continuous Monitoring in DevOps 🌟](https://medium.com/@cbkwgl/continuous-monitoring-in-devops-8d4db48a0e24)
- [logz.io: The Open Source Observability Adoption and Migration Curve](https://logz.io/blog/open-source-observability-adoption-migration-curve/)
- [==devopscube.com: What Is Observability? Comprehensive Beginners Guide==](https://devopscube.com/what-is-observability/)
- [tiagodiasgeneroso.medium.com: Observability Concepts you should know](https://tiagodiasgeneroso.medium.com/observability-concepts-you-should-know-943fc057b208)
- [faun.pub: Getting started with Observability](https://faun.pub/getting-started-with-observability-657d57aab1c7) How to implement Observability
- [medium.com/@badawekoo: Monitoring in DevOps lifecycle](https://medium.com/@badawekoo/monitoring-in-devops-lifecycle-4d9a2f277eb0)
- [laduram.medium.com: The Future of Observability](https://laduram.medium.com/the-future-of-observability-c33cd7ff644a)
- [devops.com: Where Does Observability Stand Today, and Where is it Going Next?](https://devops.com/where-does-observability-stand-today-and-where-is-it-going-next/)
- [medium.com/kubeshop-i: Top 8 Open-Source Observability & Testing Tools](https://medium.com/kubeshop-i/top-8-open-source-observability-testing-tools-9341a361a634)
- [==dzone: 11 Observability Tools You Should Know== 🌟](https://dzone.com/articles/11-observability-tools-you-should-know-in-2023) This article looks at the features, limitations, and important selling points of eleven popular observability tools to help you select the best one for your project.
- [medium.com/devops-techable: Setup monitoring with Prometheus and Grafana in Kubernetes — Start monitoring your Kubernetes cluster resources](https://medium.com/devops-techable/setup-monitoring-with-prometheus-and-grafana-in-kubernetes-start-monitoring-your-kubernetes-a3071f083fa6)
- [thenewstack.io: What Is Container Monitoring?](https://thenewstack.io/what-is-container-monitoring/) Cloud native architectures don’t rely on dedicated hardware like virtualized infrastructure, which changes monitoring requirements and processes.
- [==devops.com: Why Monitoring-as-Code Will be a Must for DevOps Teams==](https://devops.com/why-monitoring-as-code-will-be-a-must-for-devops-teams/)
- [medium.com/cloud-native-daily: Why You Shouldn’t Fear to Adopt OpenTelemetry for Observability](https://medium.com/cloud-native-daily/why-you-shouldnt-fear-to-adopt-opentelemetry-for-observability-fcb6371ea8fe) An introduction to OpenTelemetry, an open-source project that’s taking observability to a new level.
- [medium.com/@bijit211987: Observability Driven Development (ODD)-Enhancing System Reliability](https://medium.com/@bijit211987/observability-driven-development-2bc2cdde8661)
- [==forbes.com: From Data Collection To Delivering KPIs: A Roadmap To A Mature Observability Strategy==](https://www.forbes.com/sites/forbestechcouncil/2024/03/08/from-data-collection-to-delivering-kpis-a-roadmap-to-a-mature-observability-strategy)
    - The observability space is a multi-billion-dollar market and for good reason—there are a lot of benefits when you implement a robust observability strategy. But extracting value is not as simple as adopting a tool, throwing your data into a black box and expecting it to spit out business-relevant, contextualized insights and helpful visualizations.
    - As they say, “Nothing good comes easy”—but when done right, a mature observability strategy will pay for itself over and over again.

### Profiling

- [==medium.com/performance-engineering-for-the-ordinary-barbie: Why profiling should be part of regular software development workflow== 🌟](https://medium.com/performance-engineering-for-the-ordinary-barbie/why-profiling-should-be-part-of-regular-software-development-workflow-8b19b7f52b38)

### Key Performance Indicator (KPI)

- [KPIs](https://kpi.org/KPI-Basics)

## OpenShift Cluster Monitoring Built-in solutions

### OpenShift 3.11 Metrics and Logging

OpenShift Container Platform Monitoring ships with a Prometheus instance for cluster monitoring and a central Alertmanager cluster. In addition to Prometheus and Alertmanager, OpenShift Container Platform Monitoring also includes a [Grafana](https://grafana.com/) instance as well as pre-built dashboards for cluster monitoring troubleshooting. **The Grafana instance that is provided with the monitoring stack, along with its dashboards, is read-only.**

| Monitoring Component     |       Release       |                                                                                                                                                                                                                URL |
| :----------------------- | :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ElasticSearch            |          5          |                                                       [OpenShift 3.11 Metrics & Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging) |
| Fluentd                  |        0.12         |                                                       [OpenShift 3.11 Metrics & Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging) |
| Kibana                   |       5.6.13        |                                                                                                                                      [kibana 5.6.13](https://www.elastic.co/guide/en/kibana/5.6/introduction.html) |
| Prometheus               |        2.3.2        |                                 [OpenShift 3.11 Prometheus Cluster Monitoring](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#prometheus-cluster-monitoring) |
| Prometheus Operator      |                     |                           [Prometheus Operator technical preview](https://www.redhat.com/en/blog/generally-available-today-red-hat-openshift-container-platform-311-ready-power-enterprise-kubernetes-deployments) |
| Prometheus Alert Manager |      0.15.1         | [OpenShift 3.11 Configuring Prometheus Alert Manager](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-alertmanager_prometheus-cluster-monitoring) |
| Grafana                  |        5.2.3        |                                 [OpenShift 3.11 Prometheus Cluster Monitoring](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#prometheus-cluster-monitoring) |

#### Prometheus and Grafana

- [github.com/prometheus-operator](https://github.com/prometheus-operator)
- [redhat.com: **How to gather and display metrics in Red Hat OpenShift** (Prometheus + Grafana)](https://www.redhat.com/en/blog/how-gather-and-display-metrics-red-hat-openshift)
- [Generally Available today: Red Hat OpenShift Container Platform 3.11 is ready to power enterprise Kubernetes deployments 🌟](https://www.redhat.com/en/blog/generally-available-today-red-hat-openshift-container-platform-311-ready-power-enterprise-kubernetes-deployments)
- [The Challenges of Monitoring Kubernetes and OpenShift 3.11 🌟](https://thenewstack.io/the-challenges-of-monitoring-kubernetes-and-openshift/)
- [OCP 3.11 Metrics and Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging)
- [Prometheus Cluster Monitoring 🌟](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html)
- [Prometheus Alert Manager](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-alertmanager_prometheus-cluster-monitoring)
- [Leveraging Kubernetes and OpenShift for automated performance tests (part 1)](https://developers.redhat.com/blog/2018/11/22/automated-performance-testing-kubernetes-openshift/)
- [Building an observability stack for automated performance tests on Kubernetes and OpenShift (part 2) 🌟](https://developers.redhat.com/blog/2019/01/03/leveraging-openshift-or-kubernetes-for-automated-performance-tests-part-2/)
- [Promster: Use Prometheus in huge deployments with dynamic clustering and scrape sharding capabilities based on ETCD service registration](http://github.com/flaviostutz/promster)
- [developers.redhat.com: Monitoring .NET Core applications on Kubernetes](https://developers.redhat.com/blog/2020/08/05/monitoring-net-core-applications-on-kubernetes/)
- [Systems Monitoring with Prometheus and Grafana](https://flightaware.engineering/systems-monitoring-with-prometheus-grafana/)

<center>
[![openshift3 Monitoring](images/ocp_monitoring.png)](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html)
</center>

#### Custom Grafana Dashboard for OpenShift 3.11

By default OpenShift 3.11 Grafana is a read-only instance. Many organizations may want to add new custom dashboards. This custom grafana will interact with existing Prometheus and will also add all out-of-the-box dashboards plus few more interesting dashboards which may require from day to day operation. Custom Grafana pod uses OpenShift oAuth to authenticate users and assigns "Admin" role to all users so that users can create their own dashboards for additional monitoring.

[Getting Started with Custom Dashboarding on OpenShift using Grafana](https://github.com/redhat-cop/openshift-toolkit/tree/master/custom-dashboards). This repository contains scaffolding and automation for developing a custom dashboarding strategy on OpenShift using the OpenShift Monitoring stac

#### Capacity Management Grafana Dashboard

[This repo](https://github.com/redhat-cop/openshift-toolkit/tree/master/capacity-dashboard) adds a capacity management Grafana dashboard. The intent of this dashboard is to answer a single question: Do I need a new node? . We believe this is the most important question when setting up a capacity management process. We are aware that this is not the only question a capacity management process may need to be able to answer. Thus, this should be considered as the starting point for organizations to build their capacity management process.

#### Software Delivery Metrics Grafana Dashboard

[This repo](https://github.com/redhat-cop/pelorus) contains tooling to help organizations measure Software Delivery and Value Stream metrics.

#### Prometheus for OpenShift 3.11

[This repo](https://github.com/openshift/origin/tree/release-3.11/examples/prometheus) contains example components for running either an operational Prometheus setup for your OpenShift cluster, or deploying a standalone secured Prometheus instance for configurating yourself.

### OpenShift 4

OpenShift Container Platform includes a pre-configured, pre-installed, and self-updating monitoring stack that is based on the Prometheus open source project and its wider eco-system. It provides monitoring of cluster components and includes a set of alerts to immediately notify the cluster administrator about any occurring problems and a set of Grafana dashboards. The cluster monitoring stack is only supported for monitoring OpenShift Container Platform clusters.

OpenShift Cluster Monitoring components cannot be extended since they are read only.

[Monitor your own services (technology preview)](https://docs.openshift.com/container-platform/4.3/release_notes/ocp-4-3-release-notes.html): The existing monitoring stack can be extended so you can configure monitoring for your own Services.

| Monitoring Component     | Deployed By Default | OCP 4.1  | OCP 4.2 | OCP 4.3 | OCP 4.4 |
| :----------------------- | :-----------------: | :------ | :----- | :----- | :----- |
| ElasticSearch            |         No          | 5.6.13.6 |         |         |         |
| Fluentd                  |         No          | 0.12.43  |         |         |         |
| Kibana                   |         No          |  5.6.13  |         |         |         |
| Prometheus               |         Yes         |  2.7.2   |         | 2.14.0  |  2.15.2 |
| Prometheus Operator      |         Yes         |          |         | 0.34.0  |  0.35.1 |
| Prometheus Alert Manager |         Yes         |  0.16.2  |         | 0.19.0  |  0.20.0 |
| kube-state-metrics       |         Yes         |          |         |  1.8.0  |   1.9.5 |
| Grafana                  |         Yes         |  5.4.3   |  6.2.4  |  6.4.3  |   6.5.3 |

## Monitoring micro-front ends on kubernetes with NGINX

- [==cncf.io: Monitoring micro-front ends on Kubernetes with NGINX== 🌟](https://www.cncf.io/blog/2023/02/01/monitoring-micro-front-ends-on-kubernetes-with-nginx/)

## Prometheus vs OpenTelemetry

- [timescale.com: Prometheus vs. OpenTelemetry Metrics: A Complete Guide](https://www.timescale.com/blog/prometheus-vs-opentelemetry-metrics-a-complete-guide/)

## Prometheus

- [Prometheus](prometheus.md)

## Grafana

- [Grafana](grafana.md)

## Kibana

- [Kibana](https://www.elastic.co/kibana)
    - [Kibana Docs](https://www.elastic.co/guide/index.html)
- [dzone: Kibana Tutorial: Part 1 - Getting Started](https://dzone.com/articles/kibana-tutorial-getting-started-part-1)
    - [dzone: Kibana Tutorial: Part 2 - Creating Visualizations](https://logz.io/blog/kibana-tutorial-2/)
- [dzone: Getting Started With Kibana Advanced Searches](https://dzone.com/articles/getting-started-with-kibana-advanced-searches)
- [dzone: Kibana Hacks: 5 Tips and Tricks](https://dzone.com/articles/kibana-hacks-5-tips-and-tricks)
- [juanonlab.com: Dashboards de Kibana](https://www.juanonlab.com/blog/es/dashboards-de-kibana)
- [skedler.com: Kibana Customization – The brilliant beginner’s guide to simplifying Kibana for non-technical users](https://www.skedler.com/blog/kibana-customization-brilliant-beginners-guide-simplifying-kibana-non-technical-users/)
- [dev.to: Beginner's guide to understanding the relevance of your search with Elasticsearch and Kibana](https://dev.to/lisahjung/beginner-s-guide-to-understanding-the-relevance-of-your-search-with-elasticsearch-and-kibana-29n6)

## Prometheus and Grafana Interactive Learning

- [katacoda.com: Getting Started with Prometheus](https://www.katacoda.com/courses/prometheus/getting-started)
- [katacoda.com: Creating Dashboards with Grafana](https://www.katacoda.com/courses/prometheus/creating-dashboards-with-grafana)

## Logging & Centralized Log Management

- [devops.com: How Centralized Log Management Can Save Your Company](https://devops.com/how-centralized-log-management-can-save-your-company/)
- [acloudguru.com: Getting started with the Elastic Stack](https://acloudguru.com/blog/engineering/getting-started-with-the-elastic-stack)
- [betterprogramming.pub: The Art of Logging](https://betterprogramming.pub/creating-a-human-and-machine-freindly-logging-format-bb6d4bb01dca) Creating a human- and machine-friendly logging format

### ElasticSearch

- [pythonsimplified.com: Elasticsearch Core Concepts Explained](https://pythonsimplified.com/elasticsearch-core-concepts-explained/)
- [zdnet.com: AWS, as predicted, is forking Elasticsearch](https://www.zdnet.com/article/aws-as-predicted-is-forking-elasticsearch/) Amazon Web Services, however, isn't the only one who dislikes Elastic's move to relicense Elasticsearch under the non-open-source Server Side Public License.
- [amazon.com: Stepping up for a truly open source Elasticsearch](https://aws.amazon.com/blogs/opensource/stepping-up-for-a-truly-open-source-elasticsearch/)
- [Store NGINX access logs in Elasticsearch with Logging operator 🌟](https://banzaicloud.com/docs/one-eye/logging-operator/quickstarts/es-nginx/) This guide describes how to collect application and container logs in Kubernetes using the Logging operator, and how to send them to Elasticsearch.
    - [Rancher Logging Operator 🌟](https://rancher.com/docs/rancher/v2.x/en/logging/v2.5/)
- [blog.streammonkey.com: How We Serverlessly Migrated 1.58 Billion Elasticsearch Documents](https://blog.streammonkey.com/how-we-serverlessly-migrated-1-58-billion-elasticsearch-documents-33ad3d0d7c4f)
- [youtube: ELK for beginners - by XavkiEn 🌟](https://www.youtube.com/playlist?list=PLWZKNB9waqIX00uj5q4nX_TOFiX3if1z3)
- [blog.bigdataboutique.com: Tuning Elasticsearch: The Ideal Java Heap Size](https://blog.bigdataboutique.com/2021/07/tuning-elasticsearch-the-ideal-java-heap-size-2toq2j)
- [javatechonline.com: How To Monitor Spring Boot Microservices Using ELK Stack?](https://javatechonline.com/how-to-monitor-spring-boot-microservices-using-elk-stack)
- [dzone: Running Elasticsearch on Kubernetes](https://dzone.com/articles/running-elasticsearch-on-kubernetes) A bit of a cross-over with the Cloud Zone, we explore the structures of both Elasticsearch and Kubernetes, and how to deploy Elasticsearch on K8s.
- [==medium: Which Elasticsearch Provider is Right For You?== 🌟](https://medium.com/gigasearch/which-elasticsearch-provider-is-right-for-you-3d596a65e704) In this post, we’ll explain the core differences between Elastic Cloud, AWS ESS, and self-hosted, so that you can make an informed decision.

    |  | __AWS ESS__ | __Elastic Cloud__ | __Self-hosted__ |
    | :--- | :--- | :--- | :--- |
    | __Operational Burden__ | __Medium__. Requires intimate knowledge of other AWS services to go beyond defaults. | __Low__. Backups, version upgrades, etc. are automated. | __High__. You need to provision, configure and maintain the cluster(s) yourself. |
    | __Cost__ | __Medium__. Over 50% premium on underlying infrastructure cost. | __High__. Up to 3x the cost of underlying infrastructure.| __Low__. Only pay for the underlying infrastructure. Optionally can purchase x-pack license for additional features and support. |
    | __Configurability__ | __Low__. No support for custom plugins. Several configuration parameters are not available. | __Medium__. Does support custom plugins and all parameters are available. Lack of direct node ssh access. | __High__. Full node-level acess. |
    | __Monitoring__ | __Mediocre__. Kibana monitoring is not available. Cloudwatch is often inadequate for Elasticsearch monitoring. | __Good__. Kibana monitoring available and pre-installed. | __Depends__. It is up to you to implement an adequate monitoring system, but you have access to kibana monitoring. |
    | __Future-proof__ | __Medium__. Oftern lags several minor versions behind the latest Elasticsearch version. Some features are not available at all. | __High__. Same day Elasticsearch version parity. All features are available. | __High__. Up to you to upgrade as needed, but in theory the same Elastic Cloud. |

- [jertel/elastalert2](https://github.com/jertel/elastalert2) ElastAlert 2 is a continuation of the original yelp/elastalert project. ElastAlert 2 is a standalone software tool for alerting on anomalies, spikes, or other patterns of interest from data in Elasticsearch and OpenSearch. ElastAlert 2 is backwards compatible with the original ElastAlert rules
- [medium.com/hepsiburadatech: Hepsiburada Search Engine on Kubernetes](https://medium.com/hepsiburadatech/hepsiburada-search-engine-on-kubernetes-1fe03a3e71a3) In this case study, you'll learn how Hepsiburada migrated from an on-premises active-active Elasticsearch cluster (manually scaled) deployed in two data centers to a multi-zone Google Cloud Kubernetes cluster that can scale automatically.
- [dev.to/sagary2j: ELK Stack Deployment using MiniKube single node architecture](https://dev.to/sagary2j/elk-stack-deployment-using-minikube-single-node-architecture-16cl) In this tutorial, you will learn how to deploy and expose Elastic Search, Logstash and Kibana on minikube.
- [search-guard.com/sgctl-elasticsearch: SGCTL - TAKE BACK CONTROL](https://search-guard.com/sgctl-elasticsearch/) In this article, we look at the new Search Guard Control command line tool that ships with Search Guard FLX and demonstrate how easy it has become to configure security for Elasticsearch.
- [==udemy.com: Elasticsearch 7 and the Elastic Stack: In Depth and Hands On==](https://www.udemy.com/course/elasticseach-7/?referralCode=83E57F5BF9B3557E51F8) **Complete Elastic search tutorial - search, analyze, and visualize big data with Elasticsearch, Kibana, Logstash, & Beats**

#### Elastic Cloud on Kubernetes (ECK)

- [medium: A detailed guide to deploying Elasticsearch on Elastic Cloud on Kubernetes (ECK)](https://medium.com/99dotco/a-detail-guide-to-deploying-elasticsearch-on-elastic-cloud-on-kubernetes-eck-31808ac60466) Running Elasticsearch on Kubernetes allows developers/admins to utilize container orchestration by Kubernetes and apply best practices on managing Elasticsearch clusters by the Elastic Operator

### OpenSearch

- [opensearch.org 🌟](https://opensearch.org/)
- [amazon.com: Introducing OpenSearch](https://aws.amazon.com/blogs/opensource/introducing-opensearch/)
- [logz.io: Logz.io Announces Support for OpenSearch; A Community-driven Open Source Fork of Elasticsearch and Kibana](https://logz.io/news-posts/logz-io-announces-support-for-opensearch-a-community-driven-open-source-fork-of-elasticsearch-and-kibana/)
- [techrepublic.com: OpenSearch: AWS rolls out its open source Elasticsearch fork](https://www.techrepublic.com/article/opensearch-aws-rolls-out-its-open-source-elasticsearch-fork/)
- [thenewstack.io: This Week in Programming: AWS Completes Elasticsearch Fork with OpenSearch](https://thenewstack.io/this-week-in-programming-aws-completes-elasticsearch-fork-with-opensearch/)
- [logz.io: OpenSearch Is Now Generally Available!](https://logz.io/blog/opensearch-1-0-ga-generally-available-elasticsearch-kibana-fork/)
- [thenewstack.io: This Week in Programming: The ElasticSearch Saga Continues](https://thenewstack.io/this-week-in-programming-the-elasticsearch-saga-continues/)
- [aws.amazon.com: Keeping clients of OpenSearch and Elasticsearch compatible with open source](https://aws.amazon.com/blogs/opensource/keeping-clients-of-opensearch-and-elasticsearch-compatible-with-open-source/)
- [aws.amazon.com: Amazon Elasticsearch Service Is Now Amazon OpenSearch Service and Supports OpenSearch 1.0](https://aws.amazon.com/es/blogs/aws/amazon-elasticsearch-service-is-now-amazon-opensearch-service-and-supports-opensearch-10)

### EFK ElasticSearch Fluentd Kibana

- [medium: Logging with EFK - Pratyush Mathur](https://medium.com/@pratyush.mathur/logging-with-efk-1c2e131496d)
- [medium.com/@CuriousLearner: Deploying EFK stack on Kubernetes](https://medium.com/@CuriousLearner/deploying-efk-stack-on-kubernetes-c25ba2682c99)
- [medium.com/@tech_18484: Simplifying Kubernetes Logging with EFK Stack](https://medium.com/@tech_18484/simplifying-kubernetes-logging-with-efk-stack-158da47ce982)

### Logstash Grok for Log Parsing

- [logz.io: A Beginner’s Guide to Logstash Grok](https://logz.io/blog/logstash-grok/)
- [logz.io: Grok Pattern Examples for Log Parsing](https://logz.io/blog/grok-pattern-examples-for-log-parsing/)

## Internet Performance Monitoring (IPM)

- [devops.com: The Fallacy of Continuous Integration, Delivery and Testing](https://devops.com/the-fallacy-of-continuous-integration-delivery-and-testing/) Whether your organization embraces CI/CD/CT already or is rethinking its approach to DevOps, this article should give you pause. Your job–perhaps as part of a larger team–is to catch performance issues and potential disruptions with your application before client impact is realized. Without IPM, only part of that job is being done.

## Performance

- [dzone.com: The Keys to Performance Tuning and Testing](https://dzone.com/articles/the-keys-to-performance-tuning-and-testing)
- [dzone.com: How Performance Tuning and Testing are Changing](https://dzone.com/articles/how-performance-tuning-and-testing-are-changing)
- [Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) Almost all applications that perform anything useful for a given business need to be integrated with one or more applications. With microservices-based architecture, where a number of services are broken down based on the services or functionality offered, the number of integration points or touch points increases massively.

## List of Performance Analysis Tools

- Threadumps + heapdumps + GC analysis tools
- [en.wikipedia.org/wiki/List_of_performance_analysis_tools](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)
- [InspectIT](https://en.wikipedia.org/wiki/InspectIT)
- [VisualVM 🌟](https://en.wikipedia.org/wiki/VisualVM)
- [OverOps](https://en.wikipedia.org/wiki/OverOps)
- [FusionReactor](https://en.wikipedia.org/wiki/FusionReactor)
- [tier1app.com](https://tier1app.com/)
- [fastthread.io 🌟](https://fastthread.io/)
- [gceasy.io 🌟](https://gceasy.io/)
- [heaphero.io](https://heaphero.io/)

### Thread Dumps. Debugging Java Applications

- [How to read a Thread Dump](https://dzone.com/articles/how-to-read-a-thread-dump)
- [Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) **A must read!**
- [Dzone: how to take thread dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)
- Thread Dump Analyzers: [fastThread](https://fastthread.io/), [Spotify TDA](https://spotify.github.io/threaddump-analyzer/), [IBM Thread and Monitor Dump Analyzer for Java](https://www.ibm.com/support/pages/ibm-thread-and-monitor-dump-analyzer-java-tmda), [TDA - Thread Dump Analyzer](https://github.com/irockel/tda)
- [blog.arkey.fr: Using JDK FlightRecorder and JDK Mission Control](https://blog.arkey.fr/2020/06/28/using-jdk-flight-recorder-and-jdk-mission-control/)
- [FastThread.io](https://fastthread.io/): Thread dumps can be uploaded via Web or API Call from within the POD (jstack must be available within the container):

```bash
#!/bin/sh
# Generate N thread dumps of the process PID with an INTERVAL between each dump.
if [ $# -ne 3 ]; then
   echo Generates Java thread dumps using the jstack command.
   echo
   echo usage: $0 process_id repetitions interval
   exit 1
fi 
PID=$1
N=$2
INTERVAL=$3 
for ((i=1;i<=$N;i++))
do
   d=$(date +%Y%m%d-%H%M%S)
   dump="threaddump-$PID-$d.txt"
   echo $i of $N: $dump
   jstack -l $PID > $dump
   curl -X POST --data-binary @./$dump https://fastthread.io/fastthread-api?apiKey=<APIKEY> --header "Content-Type:text"
   sleep $INTERVAL
done
```

- How to run this script from within the POD: ```./script_thread_dump.sh 1 15 3```, where:
    - “1”: PID of java process (“1” in containers running a single process, check with “ps ux” command).
    - “15”: 15 repetitions or thread dumps
    - “3”: interval of 3 seconds between each thread dump.
- According to some references only 3 thread dumps captured in a timeframe of 10 seconds is necessary (when we want to troubleshoot a Java issue during a service degradation).
- Sample thread dump analysis reports generated by fastThread:
    - [Transitive blocks](https://fastthread.io/ft-thread-report.jsp?dumpId=1&s=t)
    - [Unresponsive JVM](https://fastthread.io/ft-thread-report.jsp?dumpId=1&s=t)
    - [Sudden CPU spike](https://fastthread.io/ft-thread-report.jsp?dumpId=1&s=t)
    - [Thread Leaks](https://fastthread.io/ft-thread-report.jsp?dumpId=1&s=t)

## Debugging Java Applications on OpenShift and Kubernetes

- [developers.redhat.com: Troubleshooting java applications on openshift (Jolokia)](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift/)
- [Debugging Java Applications On OpenShift and Kubernetes](https://www.openshift.com/blog/debugging-java-applications-on-openshift-kubernetes)
- [Remote Debugging of Java Applications on OpenShift](https://servicesblog.redhat.com/2019/03/06/remote-debugging-of-java-applications-on-openshift/)
    - [Dzone: Remote Debugging of Java Applications on OpenShift (JMX + VisualVM)](https://dzone.com/articles/remote-debugging-of-java-applications-on-openshift)
- [VisualVM: JVisualVM to an Openshift pod](https://fedidat.com/250-jvisualvm-openshift-pod/)
- [redhat.com: How do I analyze a Java heap dump?](https://access.redhat.com/solutions/18301)

## Distributed Tracing. OpenTelemetry and Jaeger

- [Microservice Observability with Distributed Tracing: **OpenTelemetry.io** 🌟](https://opentelemetry.io/) (**OpenTracing.io + OpenCensus.io = OpenTelemetry.io**)
- [**Jaeger** 🌟](https://www.jaegertracing.io/)
    - [Jaeger Demo1](https://github.com/obitech/micro-obs)
    - [Jaeger Demo 2](https://github.com/open-telemetry/opentelemetry-collector/tree/master/examples/demo)
    - [medium.com: **Jaeger embraces OpenTelemetry collector** 🌟](https://medium.com/jaegertracing/jaeger-embraces-opentelemetry-collector-90a545cbc24)
    - [Best Practices for Deploying Jaeger on Kubernetes in Production](https://thenewstack.io/best-practices-for-deploying-jaeger-on-kubernetes-in-production/)
    - [faun.pub: How to deploy Jaeger on Kubernetes. A beginner’s guide to Jaeger (5 Part Series)](https://faun.pub/how-to-deploy-jaeger-on-kubernetes-69cf48447182)
- [**zipkin.io**](https://zipkin.io/)
    - [javatechonline.com: How To Implement Distributed Logging Tracing Using Sleuth Zipkin](https://javatechonline.com/how-to-implement-distributed-logging-tracing-using-sleuth-zipkin)
    - [thenewstack.io: Perform Distributed Tracing with Zipkin](https://thenewstack.io/perform-distributed-tracing-with-zipkin/) Open source Zipkin offers a robust set of features that make it easier for developers to understand and optimize complex distributed systems.
- [**OpenTracing.io**](https://opentracing.io/)
    - [lightstep.com: Understand Distributed Tracing](https://docs.lightstep.com/docs/understand-distributed-tracing)
- [grafana.com: A beginner's guide to distributed tracing and how it can increase an application's performance 🌟](https://grafana.com/blog/2021/01/25/a-beginners-guide-to-distributed-tracing-and-how-it-can-increase-an-applications-performance/)
- [awkwardferny.medium.com: Setting up Distributed Tracing in Kubernetes with OpenTracing, Jaeger, and Ingress-NGINX](https://awkwardferny.medium.com/setting-up-distributed-tracing-with-opentelemetry-jaeger-in-kubernetes-ingress-nginx-cfdda7d9441d)
- [ploffay.medium.com: Five years evolution of open-source distributed tracing 🌟](https://ploffay.medium.com/five-years-evolution-of-open-source-distributed-tracing-ec1c5a5dd1ac)

### Microservice Observability with Distributed Tracing. OpenTelemetry.io

- Used for monitoring and troubleshooting microservices-based distributed systems.
- [OpenTelemetry.io](https://opentelemetry.io/):
    - **Unified standard** (open, vendor-neutral API), **merge of [OpenCensus.io](https://opencensus.io/) and [OpenTracing.io](https://opentracing.io/)**.
    - “A single set of system components and language-specific telemetry libraries” to standardize how the industry uses metrics, traces, and eventually logs to enable observability.
    - [signadot.com: Sandboxes in Kubernetes using OpenTelemetry](https://www.signadot.com/blog/sandboxes-in-kubernetes-using-opentelemetry)
    - [dynatrace.com: What is  OpenTelemetry? An open-source standard for logs, metrics, and traces](https://www.dynatrace.com/news/blog/what-is-opentelemetry-2/)
    - [betterprogramming.pub: Distributed Tracing With OpenTelemetry, Spring Cloud Sleuth, Kafka, and Jaeger](https://betterprogramming.pub/distributed-tracing-with-opentelemetry-spring-cloud-sleuth-kafka-and-jaeger-939e35f45821) A step-by-step guide for Distributed Tracing Implementation in Microservices
    - [==logz.io: Beginner’s Guide to OpenTelemetry== 🌟](https://logz.io/learn/opentelemetry-guide/)
    - [timescale.com: Kubernetes Observability in One Command: How to Generate and Store OpenTelemetry Traces Automatically](https://www.timescale.com/blog/generate-and-store-opentelemetry-traces-automatically/) If your microservices are written in languages currently supported by the OpenTelemetry Operator, you can start collecting and storing traces with minimal manual work. Learn how to do so with the tobs stack in Kubernetes.
    - [trstringer.com: Observability with OpenTelemetry Part 1 - Introduction](https://trstringer.com/otel-part1-intro/)
    - [medium.com/apache-apisix: End-to-end tracing with OpenTelemetry](https://medium.com/apache-apisix/end-to-end-tracing-opentelemetry-a50fceafed74)
- A major component of the [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification) is **distributed tracing**.
- **Tracing** is about analyzing, recording, and describing transactions.
- **Distributed Tracing:** Troubleshooting requests between interconnected cloud-based microservices can’t always be done with logs and metrics alone. This is where distributed tracing comes into play: It provides developers with a  detailed view of individual requests as they “hop” through a system of microservices. With **distributed tracing** you can:
    - Trace the path of a request as it travels across a complex system.
    - Discover the latency of the components along that path.
    - Know which component in the path is creating a bottleneck or failure.
- **Performance:** Latency is a very important metric in microservices. Latency problems in one service will impact the overall request latency when chaining calls to different microservices. Every call to a microservice should record a trace, which is basically a record of how much time it took to respond. It's possible to add more details to the function level, including the action, the result, and the pass to the next service. The hard part is triaging all traces in a request from a client. Usually, a trace ID header has to be sent in every request. If there isn't one, the logging library creates it and it will represent the first trace in a request. **Adding traces with [OpenCensus](https://opencensus.io/) is simply a matter of including the libraries and registering an exporter.**
- **Monitoring in a Microservices/Kubernetes World:** In distributed system architectures like microservices, having visibility from different perspectives will be critical at troubleshooting time. Many things could happen in a request when there are many parts constantly interacting at the same time. The most common method is to write logs to the stdout and stderr streams.
    - For example, a latency problem in the system could exist because a microservice is not responding correctly. Maybe Kubernetes is restarting the pod too frequently, or perhaps the cluster is out of capacity and can't schedule any more pods. But for this reason, tools like [Istio](https://istio.io/) exist; by injecting a container in every pod, you can get a pretty good baseline of telemetry. Additionally, when you add instrumentation with libraries like [OpenCensus](https://opencensus.io/), you can deeply understand what's happening with and within each service.
    - All this information will need a storage location, and as a good practice, you might want to have it a centralized location to provide access to anyone in the team — not just for the operations team.
- **Older Distributed Tracing Solutions:**
    - [Dapper](https://research.google/pubs/pub36356/) (Google)
    - [Zipkin](https://zipkin.io/) (A.K.A. OpenZipkin, created by Twitter, inspired by Dapper)
    - [Jaeger](https://www.jaegertracing.io/) (Uber Technologies, inspired by Dapper & Zipkin)
    - etc.
- [Medium: Distributed Tracing and Monitoring using OpenCensus](https://medium.com/@rghetia/distributed-tracing-and-monitoring-using-opencensus-fe5f6e9479fb)
- [Dzone: Zipkin vs. Jaeger: Getting Started With Tracing](https://dzone.com/articles/zipkin-vs-jaeger-getting-started-with-tracing) Learn about Zipkin and Jaeger, how they work to add request tracing to your logging routine, and how to choose which one is the right fit for you.
- [opensource.com: Distributed tracing in a microservices world](https://opensource.com/article/18/9/distributed-tracing-microservices-world) What is distributed tracing and why is it so important in a microservices environment?
- [opensource.com: 3 open source distributed tracing tools](https://opensource.com/article/18/9/distributed-tracing-tools) Find performance issues quickly with these tools, which provide a graphical view of what's happening across complex software systems.
- [newrelic.com: OpenTracing, OpenCensus, OpenTelemetry, and New Relic (Best overview of OpenTelemetry)](https://blog.newrelic.com/engineering/opentelemetry-opentracing-opencensus/)
- There’s no OpenTelemetry UI, instead Jaeger UI (or any APM like Dynatrace or New Relic) can be used as “Tracing backend + Visualization frontend + Data mining platform” of OpenTelemetry API/SDK.
- [thenewstack.io: Tracing: Why Logs Aren’t Enough to Debug Your Microservices 🌟](https://thenewstack.io/tracing-why-logs-arent-enough-to-debug-your-microservices/)

#### OpenTelemetry Operator

- [github.com/open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator)
- [medium.com/@magstherdev: OpenTelemetry Operator](https://medium.com/@magstherdev/opentelemetry-operator-d3d407354cbf) This post aims to demonstrate how you can implement traces in your application without any code changes by using the OpenTelemetry Operator.
- [thenewstack.io: OpenTelemetry Gaining Traction from Companies and Vendors](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) Elastic and OpenTelemetry will merge standards as more companies embrace OpenTelemetry to improve user experience and cut costs.
- [thenewstack.io: How OpenTelemetry Works with Kubernetes](https://thenewstack.io/how-opentelemetry-works-with-kubernetes/)
- [medium.com/@bijit211987: Grafana with OpenTelemetry, Vendor-neutral and open-source approach](https://medium.com/@bijit211987/grafana-with-opentelemetry-vendor-neutral-and-open-source-approach-ab4bc08f67e9)

<center>
[![Jaeger UI](images/jaeger_ui.png)](https://www.jaegertracing.io/)

[![Zipking UI](images/zipkin_ui.png)](https://zipkin.io/)
</center>

### Jaeger VS OpenTelemetry. How Jaeger works with OpenTelemetry

- [medium: Jaeger VS OpenTracing VS OpenTelemetry](https://medium.com/jaegertracing/jaeger-and-opentelemetry-1846f701d9f2)
- [medium: Using Jaeger and OpenTelemetry SDKs in a mixed environment with W3C Trace-Context](https://medium.com/jaegertracing/jaeger-clients-and-w3c-trace-context-c2ce1b9dc390)

<center>
![Jaeger Vs OpenTelemetry](images/jaeger_vs_opentelemetry.png)
</center>

### Jaeger vs Zipkin

- [thenewstack.io: Jaeger vs. Zipkin: Battle of the Open Source Tracing Tools](https://thenewstack.io/jaeger-vs-zipkin-battle-of-the-open-source-tracing-tools/)

### Grafana Tempo distributed tracing system

- [Grafana Tempo](https://github.com/grafana/tempo) Grafana Tempo is an open source, easy-to-use and high-scale distributed tracing backend. Tempo requires only object storage to operate and is deeply integrated with Grafana, Prometheus, and Loki.
- [grafana.com: Announcing Grafana Tempo, a massively scalable distributed tracing system 🌟](https://grafana.com/blog/2020/10/27/announcing-grafana-tempo-a-massively-scalable-distributed-tracing-system/)
- [opensource.com: Get started with distributed tracing using Grafana Tempo](https://opensource.com/article/21/2/tempo-distributed-tracing) Grafana Tempo is a new open source, high-volume distributed tracing backend.

## Application Performance Management (APM)

- [APM in wikipedia](https://en.wikipedia.org/wiki/Application_performance_management): The monitoring and management of performance and availability of software applications. APM strives to detect and diagnose complex application performance problems to maintain an expected level of service. APM is "the translation of IT metrics into business meaning.”
- Tip: [Download APM report from IT Central Station](https://www.itcentralstation.com/categories/application-performance-management-apm)
- [Awesome APM 🌟](https://github.com/antonarhipov/awesome-apm)
- [dzone.com: APM Tools Comparison](https://dzone.com/articles/apm-tools-comparison-which-one-should-you-choose)
- [dzone.com: Java Performance Monitoring: 5 Open Source Tools You Should Know](https://dzone.com/articles/java-performance-monitoring-5-open-source-tools-you-should-know)
- [dzone.com: 14 best performance testing tools and APM solutions](https://dzone.com/articles/14-best-performance-testing-tools-and-apm-solution)
- Exception Tracking:
    - [sentry.io](https://sentry.io/)
        - [blog.sentry.io: Development Environment Observability with Sentry](https://blog.sentry.io/2021/11/18/monitoring-our-local-development-environment-with-sentry)
    - APMs like Dynatrace, etc.
- APM Tools:
    - [datadoghq.com](https://www.datadoghq.com/)
        - [blog.porter.run: Datadog on Kubernetes: Avoiding Common Pitfalls](https://blog.porter.run/datadog-and-kubernetes/) Install Datadog on Kubernetes and configure additional features like DogStatsD and APM while avoiding common pitfalls.
        - [dev.to/thenjdevopsguy: Implementing Datadog For Kubernetes](https://dev.to/thenjdevopsguy/implementing-datadog-for-kubernetes-586e)
    - [honeycomb.io](https://www.honeycomb.io)
    - [lightstep.com](https://lightstep.com)
    - [skywalking.apache.org 🌟](https://skywalking.apache.org/)
        - [tetrate.io: SkyWalking 8.4 provides infrastucture monitoring for VMs](https://www.tetrate.io/blog/27835-revision-v1/)
        - [thenewstack.io: End-User Tracing in a SkyWalking-Observed Browser](https://thenewstack.io/end-user-tracing-in-a-skywalking-observed-browser/)
    - [AppDynamics 🌟](https://www.appdynamics.com/)
    - [New Relic 🌟](https://newrelic.com/)
        - [newrelic.com: Creating dashboards with Terraform and JSON templates](https://newrelic.com/blog/how-to-relic/create-nr-dashboards-with-terraform-part-1) Learn how to quickly update New Relic dashboards with Terraform by using JSON templates—no HCL required.
    - [Dynatrace 🌟](https://www.dynatrace.com/)
    - [==SigNoz: Open source Application Performance Monitoring (APM) & Observability tool== 🌟](https://github.com/SigNoz/signoz) SigNoz helps developers monitor their applications & troubleshoot problems, an open-source alternative to DataDog, NewRelic, etc.
        - [golang.ch: A Golang-based open-source alternative to DataDog, New Relic, etc](https://golang.ch/a-golang-based-open-source-alternative-to-datadog-new-relic-etc/)
    - [savecost/datav 🌟](https://github.com/savecost/datav) A modern APM for metrics,traces and logs, also datav is a lightweight alternative to Grafana. It has fully native support for open-telemetry, is an open-source alternative to DataDog, NewRelic.

### Elastic APM

- [Elastic APM](https://www.elastic.co/products/apm)
- [Elastic APM Server](https://www.elastic.co/guide/en/apm/get-started/current/components.html):
- [Mininimum elasticsearch requirement is 6.2.x or higher](https://www.elastic.co/support/matrix#matrix_compatibility)
- Built-in elasticsearch 5.6 in Openshift 3 & Openshift 4 cannot be integrated with Elastic APM Server.
- Solutions: Deploy a higher version of [Elasticsearch + Kibana](https://hub.docker.com/_/elasticsearch) on a new Project dedicated to Elastic APM; or setup an Elastic Cloud account.
- [Elastic APM Server Docker image](https://github.com/sls-dev1/openshift-elastic-apm-server) (“oss” & openshift compliant).
- [elastic.co: Using the Elastic APM Java Agent on Kubernetes](https://www.elastic.co/blog/using-elastic-apm-java-agent-on-kubernetes-k8s)
- [Monitoring Java applications with Elastic: Getting started with the Elastic APM Java Agent](https://www.elastic.co/blog/monitoring-java-applications-and-getting-started-with-the-elastic-apm-java-agent)
- [Jenkins pipeline shared library for the project Elastic APM 🌟](https://github.com/elastic/apm-pipeline-library)
- [bqstack.com: Monitoring Application using Elastic APM](https://bqstack.com/b/detail/109)

<center>
![Elastic APM](images/elasticapm.png)
</center>

### Dynatrace APM

- [adictosaltrabajo.com: Monitorización y análisis de rendimiento de aplicaciones con Dynatrace APM](https://www.adictosaltrabajo.com/tutoriales/monitorizacion-y-analisis-de-rendimiento-de-aplicaciones-con-dynatrace/)
- [dynatrace.com: openshift monitoring](https://www.dynatrace.com/technologies/openshift-monitoring/)
- [dynatrace.com: Dynatrace monitoring for Kubernetes and OpenShift](https://www.dynatrace.com/news/blog/dynatrace-monitoring-for-kubernetes-and-openshift/)
- [dynatrace.com: Deploy OneAgent on OpenShift Container Platform](https://www.dynatrace.com/support/help/cloud-platforms/openshift/full-stack/deploy-oneagent-on-openshift-container-platform/)
- [Successful Kubernetes Monitoring – Three Pitfalls to Avoid](https://www.dynatrace.com/news/blog/successful-kubernetes-monitoring-3-pitfalls-to-avoid/)
- [My Dynatrace proof of concept 🌟](https://github.com/redhatspain/awesome-kubernetes/blob/master/pdf/dynatrace_demo.pdf)
- [Tutorial: Guide to automated SRE-driven performance engineering 🌟](https://www.dynatrace.com/news/blog/guide-to-automated-sre-driven-performance-engineering-analysis/)
- [dynatrace.com: 4 steps to modernize your IT service operations with Dynatrace](https://www.dynatrace.com/news/blog/4-steps-to-modernize-your-it-service-operations-with-dynatrace/)
- [dynatrace.com: Monitoring of Kubernetes Infrastructure for day 2 operations](https://www.dynatrace.com/news/blog/monitoring-of-kubernetes-infrastructure-for-day-2-operations/)
- [dynatrace.com: The Power of OpenShift, The Visibility of Dynatrace](https://www.dynatrace.com/news/blog/the-power-of-openshift-the-visibility-of-dynatrace/)
- [dynatrace.com: Why conventional observability fails in Kubernetes environments—A real-world use case 🌟](https://www.dynatrace.com/news/blog/why-conventional-observability-fails-in-kubernetes-environments-a-real-world-use-case)
- [dynatrace.com: A look behind the scenes of AWS Lambda and our new Lambda monitoring extension](https://www.dynatrace.com/news/blog/a-look-behind-the-scenes-of-aws-lambda-and-our-new-lambda-monitoring-extension/)
- [dynatrace.com: Analyze all AWS data in minutes with Amazon CloudWatch Metric Streams available in Dynatrace](https://www.dynatrace.com/news/blog/amazon-cloudwatch-metric-streams-launch-partnership/)
- [dynatrace.com: New Dynatrace Operator elevates cloud-native observability for Kubernetes](https://www.dynatrace.com/news/blog/new-dynatrace-operator-elevates-cloud-native-observability-for-kubernetes/)
- [dynatrace.com: How to collect Prometheus metrics in Dynatrace](https://www.dynatrace.com/news/blog/how-to-collect-prometheus-metrics-in-dynatrace)
- [dynatrace.com: Automatic connection of logs and traces accelerates AI-driven cloud analytics](https://www.dynatrace.com/news/blog/automatic-connection-of-logs-and-traces-accelerates-ai-driven-cloud-analytics/)
- [==devops.com: Dynatrace Advances Application Environments as Code==](https://devops.com/dynatrace-advances-application-environments-as-code/)

## Message Queue Monitoring

Messaging Solution|Monitoring Solution|URL
:-------|:-------|:-----
ActiveMQ 5.8.0+|[Dynatrace](https://www.dynatrace.com)|[ref](https://www.dynatrace.com/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/activemq/)
ActiveMQ Artemis|[Micrometer Collector](https://micrometer.io/) + Prometheus|[ref1](http://activemq.apache.org/components/artemis/documentation/latest/metrics.html), [ref2](https://micrometer.io/docs/registry/prometheus)
IBM MQ|[IBM MQ](https://github.com/ibm-messaging) Exporter for Prometheus|[ref](https://github.com/ibm-messaging/mq-metric-samples/tree/master/cmd/mq_prometheus)
Kafka|[Dynatrace](https://www.dynatrace.com)|[ref1](https://www.dynatrace.com/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/kafka/), [ref2](https://www.dynatrace.com/news/blog/introducing-kafka-process-monitoring-beta/), [ref3](https://answers.dynatrace.com/spaces/482/dynatrace-open-qa/questions/232421/dynatrace-distributed-tracing-with-kafka.html)
Kafka|[Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter)|[ref1](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/zookeeper.yaml), [ref2](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/kafka-2_0_0.yml), [ref3](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/kafka-connect.yml), [ref4](https://strimzi.io/blog/2019/10/14/improving-prometheus-metrics/), [ref5](https://medium.com/activewizards-machine-learning-company/kafka-monitoring-with-prometheus-telegraf-and-grafana-6228fed736f1), [ref6](https://medium.com/@nblaye/exporting-kafka-jmx-metrics-to-grafana-1b9d32fe900a), [ref7](https://blog.knoldus.com/monitoring-kafka-with-prometheus-and-grafana/)
Kafka|Kafka Exporter<br/> Use [JMX Exporter](https://github.com/prometheus/jmx_exporter) to export other Kafka's metrics|[ref](https://github.com/danielqsj/kafka_exporter)
Kafka|Kafdrop – Kafka Web UI|[ref](https://github.com/obsidiandynamics/kafdrop)
Kafka|ZooNavigator: Web-based ZooKeeper UI|[ref](https://zoonavigator.elkozmon.com/)
Kafka|CMAK (Cluster Manager for Apache Kafka, previously known as Kafka Manager)|[ref](https://github.com/patelh/kafka-manager)
Kafka|Xinfra Monitor (renamed from Kafka Monitor, created by Linkedin)|[ref](https://github.com/linkedin/kafka-monitor)
Kafka|Telegraf + InfluxDB|[ref](https://www.influxdata.com/integration/kafka-telegraf-integration/)
Red Hat AMQ Broker (ActiveMQ Artemis)|Prometheus plugin for AMQ Broker<br/>To monitor the health and performance of your broker instances, you can use the **Prometheus plugin for AMQ Broker** to monitor and store broker runtime metrics. Prometheus is software built for monitoring large, scalable systems and storing historical runtime data over an extended time period. The **AMQ Broker Prometheus plugin exports the broker runtime metrics to Prometheus format**, enabling you to use Prometheus itself to visualize and run queries on the data.<br/>You can also use a graphical tool, such as **Grafana, to configure more advanced visualizations and dashboards** for the metrics that the Prometheus plugin collects.<br/>The metrics that the plugin exports to Prometheus format are listed below. A description of each metric is exported along with the metric itself.|[ref1](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/managing_amq_broker/prometheus-plugin-managing), [ref2](https://github.com/lbroudoux/openshift-cases/tree/master/jboss-amq7-custom), [ref3](https://www.openshift.com/blog/enhanced-openshift-jboss-amq-container-image-for-production)
Red Hat AMQ Streams (Kafka)|[JMX](https://www.oracle.com/java/technologies/javase/javamanagement.html), OpenTracing+Jaeger <br/>ZooKeeper, the Kafka broker, Kafka Connect, and the Kafka clients all expose management information using [Java Management Extensions (JMX)](https://www.oracle.com/java/technologies/javase/javamanagement.html). Most management information is in the form of metrics that are useful for monitoring the condition and performance of your Kafka cluster. Like other Java applications, Kafka provides this management information through managed beans or MBeans.<br/> **JMX** works at the level of the JVM (Java Virtual Machine). To obtain management information, **external tools can connect to the JVM that is running ZooKeeper, the Kafka broker, and so on.** By default, only tools on the same machine and running as the same user as the JVM are able to connect.<br/>**Distributed Tracing with Jaeger:**<br/> - Kafka Producers, Kafka Consumers, and Kafka Streams applications (referred to as Kafka clients)<br/> - MirrorMaker and Kafka Connect <br/> - Kafka Bridge|[ref1](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_rhel/index),[ref2](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_rhel/assembly-distributed-tracing-str)
Red Hat AMQ Streams Operator|AMQ Streams Operator (Prometheus & Jaeger), strimzi, jmxtrans<br/>How to monitor AMQ Streams Kafka, Zookeeper and Kafka Connect clusters using Prometheus to provide monitoring data for example Grafana dashboards.<br/>Support for distributed tracing in AMQ Streams, using **Jaeger**:<br/> - You instrument Kafka Producer, Consumer, and Streams API applications for distributed tracing using an OpenTracing client library. This involves adding instrumentation code to these clients, which monitors the execution of individual transactions in order to generate trace data.<br/>  - Distributed tracing support is built in to the Kafka Connect, MirrorMaker, and Kafka Bridge components of AMQ Streams. To configure these components for distributed tracing, you configure and update the relevant custom resources.|[ref1](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_openshift/assembly-metrics-setup-str), [ref2](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_openshift/assembly-distributed-tracing-str), [ref3 strimzi](https://operatorhub.io/operator/strimzi-kafka-operator), [ref4: **jmxtrans**](https://github.com/jmxtrans/jmxtrans), [ref5: banzai operator](https://operatorhub.io/operator/banzaicloud-kafka-operator)
Red Hat AMQ Broker Operator|Prometheus (recommended) or Jolokia REST to JMX <br/>To monitor runtime data for brokers in your deployment, use one of these approaches:<br/> - [Section 9.1, “Monitoring broker runtime data using Prometheus”](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#assembly_br-monitoring-broker-runtime-data-using-prometheus_broker-ocp)<br/> - [Section 9.2, “Monitoring broker runtime data using JMX”](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#proc_br-monitoring-broker_broker-ocp) <br/>In general, using Prometheus is the recommended approach. However, you might choose to use the Jolokia REST interface to JMX if a metric that you need to monitor is not exported by the Prometheus plugin. For more information about the broker runtime metrics that the Prometheus plugin exports, [see Section 9.1.1, “Overview of Prometheus metrics”](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#con-br-overview-of-prometheus-metrics_broker-ocp)|[ref1](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/deploying-broker-on-ocp-using-operator_broker-ocp), [ref2](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp), [ref3](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#assembly_br-monitoring-broker-runtime-data-using-prometheus_broker-ocp), [ref4](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#proc_br-monitoring-broker_broker-ocp), [ref5](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp#con-br-overview-of-prometheus-metrics_broker-ocp)

### Red Hat AMQ 7 Broker Monitoring solutions based on Prometheus and Grafana

This is a selection of monitoring solutions suitable for RH AMQ 7 Broker based on Prometheus and Grafana:

Environment|Collector/Exporter|Details/URL
:----------|:----------------:|:--------------
RHEL|Prometheus Plugin for AMQ Broker|[ref](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/managing_amq_broker/prometheus-plugin-managing)
RHEL|Prometheus JMX Exporter|Same solution applied to ActiveMQ Artemis
OpenShift 3|Prometheus Plugin for AMQ Broker|**Grafana Dashboard not available**, [ref1](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/deploying-broker-on-ocp-using-operator_broker-ocp), [ref2](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/deploying_amq_broker_on_openshift/assembly_br-broker-monitoring_broker-ocp)
OpenShift 4|Prometheus Plugin for AMQ Broker|Check if Grafana Dashboard is automatically setup by Red Hat AMQ Operator
OpenShift 3|Prometheus JMX Exporter|**Grafana Dashboard not available**, [ref1](https://www.openshift.com/blog/enhanced-openshift-jboss-amq-container-image-for-production), [ref2](https://github.com/lbroudoux/openshift-cases/tree/master/jboss-amq7-custom)

## Serverless Monitoring

- [thenewstack.io: Serverless Needs More Observability Tools](https://thenewstack.io/serverless-needs-more-observability-tools/)

## Distributed Tracing in Apache Beam

- [Apache Beam](https://beam.apache.org/)
- [A Distributed Tracing Adventure in Apache Beam](http://rion.io/2020/07/04/a-distributed-tracing-adventure-in-apache-beam/)

## Krossboard Converged Kubernetes usage analytics

- [Krossboard](https://krossboard.app/) All in one single place, Krossboard tracks the usage of all your clusters over time, it helps forecast capacity scale up/down, thereby enabling you to easily anticipate and master operations costs.
- [Krossboard: A centralized usage analytics approach for multiple Kubernetes](https://itnext.io/in-search-of-converged-usage-analytics-for-multiple-managed-kubernetes-c5108cb7f0e1)

## Instana APM

- [cloudbees.com: Automated Build and Deploy Feedback Using Jenkins and Instana 🌟](https://www.cloudbees.com/blog/automated-build-deploy-feedback-using-instana)

## Monitoring Etcd

- [rancher.com: Monitor Etcd with Prometheus and Grafana using Rancher](https://rancher.com/blog/2020/monitor-etcd-prometheus-grafana-rancher)

## Zabbix

- [openshift.com: Monitoring Infrastructure Openshift 4.x Using Zabbix Operator](https://www.openshift.com/blog/monitoring-infrastructure-openshift-4.x-using-zabbix-operator)
- [openshift.com: How to Monitor Openshift 4.x with Zabbix using Prometheus - Part 2](https://www.openshift.com/blog/how-to-monitoring-openshift-4.x-with-zabbix-using-prometheus-part-2)
- [cloud.redhat.com: Monitoring Infrastructure Openshift 4.x Using Zabbix Operator](https://cloud.redhat.com/blog/monitoring-infrastructure-openshift-4.x-using-zabbix-operator)

## VictoriaMetrics and VictoriaLogs

- [victoriametrics.com](https://victoriametrics.com)
- [victoriametrics.com: Q2 2024 Round Up: VictoriaMetrics & VictoriaLogs Updates](https://victoriametrics.com/blog/q2-2024-round-up-victoriametrics-and-victorialogs-updates/) VictoriaLogs is an open source database for logs that uses up to 30x less RAM and up to 15x disk space than Elasticsearch has just relased several new features to celebrate their one year anniversary

## Other Tools

- [Netdata](https://github.com/netdata/netdata) Netdata's distributed, real-time monitoring Agent collects thousands of metrics from systems, hardware, containers, and applications with zero configuration.
- [PM2](https://github.com/Unitech/pm2) is a production process manager for Node.js applications with a built-in load balancer. It allows you to keep applications alive forever, to reload them without downtime and to facilitate common system admin tasks.
- [Huginn](https://github.com/huginn/huginn) Create agents that monitor and act on your behalf. Your agents are standing by!
- [OS Query](https://github.com/osquery/osquery) SQL powered operating system instrumentation, monitoring, and analytics.
- [Glances](https://github.com/nicolargo/glances) Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, Mac OS and Windows operating systems. It is written in Python and uses libraries to grab information from your system. It is based on an open architecture where developers can add new plugins or exports modules.
- [TDengine](https://github.com/taosdata/TDengine) is an open-sourced big data platform under GNU AGPL v3.0, designed and optimized for the Internet of Things (IoT), Connected Cars, Industrial IoT, and IT Infrastructure and Application Monitoring.
- [stackpulse.com: Automated Kubernetes Pod Restarting Analysis with StackPulse](https://stackpulse.com/blog/automated-kubernetes-pod-restarting-analysis-with-stackpulse/)
- [Checkly](https://www.checklyhq.com/) is the API & E2E monitoring platform for the modern stack: programmable, flexible and loving JavaScript.
    - [hashicorp.com: Monitoring as Code with Terraform Cloud and Checkly](https://www.hashicorp.com/blog/monitoring-as-code-with-terraform-cloud-and-checkly)
- [network-king.net: IoT use in healthcare grows but has some pitfalls](https://network-king.net/iot-use-in-healthcare-grows-but-has-its-pitfalls/)
- [Zebrium](https://www.zebrium.com/) Monitoring detects problems, Zebrium finds root cause
Resolve your software incidents 10x faster
- [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) A fancy self-hosted monitoring tool. Uptime Kuma is an open source monitoring tool that can be used to monitor the service uptime along with few other stats like Ping Status, Avg. Response time, uptime etc.

## Other Awesome Lists

- [Awesome APM](https://github.com/antonarhipov/awesome-apm)

## Slides

<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/J1S3NyN9ZeLjh9" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/challenges-in-a-microservices-age-monitoring-logging-and-tracing-on-red-hat-openshift" title="Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift" target="_blank">Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift</a> </strong> from <strong><a href="//www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/lr07J585Y86D7i" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/monitoring-microservices-at-scale-on-openshift-67500621" title="Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)" target="_blank">Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)</a> </strong> from <strong><a href="//www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/CDyLLoStp2omzE" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/PurnimaKurella/dynatrace-70789377" title="Dynatrace" target="_blank">Dynatrace</a> </strong> from <strong><a href="//www.slideshare.net/PurnimaKurella" target="_blank">Purnima Kurella</a></strong> </div>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The ecosystem of CI / CD tools that integrates in <a href="https://twitter.com/hashtag/OpenTelemetry?src=hash&amp;ref_src=twsrc%5Etfw">#OpenTelemetry</a> traces is growing rapidly with already <a href="https://twitter.com/hashtag/Jenkins?src=hash&amp;ref_src=twsrc%5Etfw">#Jenkins</a>, <a href="https://twitter.com/hashtag/Maven?src=hash&amp;ref_src=twsrc%5Etfw">#Maven</a>, <a href="https://twitter.com/hashtag/Ansible?src=hash&amp;ref_src=twsrc%5Etfw">#Ansible</a>, and the generic otel-cli<a href="https://t.co/GeKUMd5zl4">https://t.co/GeKUMd5zl4</a><a href="https://t.co/KrMIGZ3vkp">https://t.co/KrMIGZ3vkp</a><a href="https://t.co/UiJ0Dk78Pd">https://t.co/UiJ0Dk78Pd</a><a href="https://t.co/UdwnxXOUa4">https://t.co/UdwnxXOUa4</a> <a href="https://t.co/MsYViY6jwf">pic.twitter.com/MsYViY6jwf</a></p>&mdash; Cyrille Le Clerc (@cyrilleleclerc) <a href="https://twitter.com/cyrilleleclerc/status/1430070961366257693?ref_src=twsrc%5Etfw">August 24, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Distributed tracing is like IPv6. The entire premise reveals itself when critical usage is achieved. Hence, there are few organizations that has resources to do the hard work of retrofitting it into their existing systems. For “green field” companies, it’s different.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1434980799716102144?ref_src=twsrc%5Etfw">September 6, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">One of the biggest frictions of the container ecosystem to me is the fact that I still have to deal with the node. Either directly or indirectly, managed or unmanaged, visible to me or not. And it sucks.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1435849792542830594?ref_src=twsrc%5Etfw">September 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">We want a stack debuggable all the way down to the bare metal and we want a stack that encapsulates all the complexity. We don&#39;t know what we want and all compute ended up being leaky abstractions.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1435859851851165704?ref_src=twsrc%5Etfw">September 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">As someone who is working on monitoring and performance, my job is about leaking into abstractions. Whatever abstraction layer I am targeting, I often engage with all to cover everything down to bare metal.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1438780504690466817?ref_src=twsrc%5Etfw">September 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If your observability strategy only relies on your service mesh, you are in the early stages of putting together a strategy. And you must have a very reliable service mesh.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1443652442063704065?ref_src=twsrc%5Etfw">September 30, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This. I work with tens of companies &amp; they sometimes want to hire me to &quot;fix their observability&quot;. You can&#39;t throw some tools or a single person to this problem. Observability is like security, it&#39;s a vertical. You have to embed it to your eng culture. <a href="https://t.co/poFsLhsxq9">https://t.co/poFsLhsxq9</a></p>&mdash; Jaana Dogan at KubeCon ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1448373809631817734?ref_src=twsrc%5Etfw">October 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Does anyone want to try out the <a href="https://twitter.com/hashtag/k8s?src=hash&amp;ref_src=twsrc%5Etfw">#k8s</a> <a href="https://twitter.com/hashtag/slack?src=hash&amp;ref_src=twsrc%5Etfw">#slack</a> bot? It helps with browsing clusters directly from Slack and notifies you about important changes to your clusters. Your feedback would be super helpful! Please DM for details. <a href="https://t.co/SpRFz2wgtZ">pic.twitter.com/SpRFz2wgtZ</a></p>&mdash; Kubevious (@kubevious) <a href="https://twitter.com/kubevious/status/1471208374196850693?ref_src=twsrc%5Etfw">December 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>