# Monitoring and Performance
1. [Monitoring](#monitoring)
2. [Prometheus](#prometheus)
    1. [Prometheus Exporters (collectors)](#prometheus-exporters-collectors)
    2. [Prometheus Exporters (third party)](#prometheus-exporters-third-party)
3. [Grafana](#grafana)
4. [Collectors](#collectors)
5. [Prometheus Storage](#prometheus-storage)
6. [Performance](#performance)
7. [Distributed Tracing](#distributed-tracing)
8. [Application Performance Management](#application-performance-management)
    1. [Dynatrace APM](#dynatrace-apm)
9. [Other Awesome Lists](#other-awesome-lists)

## Monitoring
* [Wikipedia: Application Performance Index](https://en.wikipedia.org/wiki/Apdex)
* [thenewstack.io: The Challenges of Monitoring Kubernetes and OpenShift](https://thenewstack.io/the-challenges-of-monitoring-kubernetes-and-openshift/)
* [dzone.com: Kubernetes Monitoring: Best Practices, Methods, and Existing Solutions](https://dzone.com/articles/kubernetes-monitoring-best-practices-methods-and-e) Kubernetes handles containers in several computers, removing the complexity of handling distributed processing. But what's the best way to perform Kubernetes monitoring?
* [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb/)

## Prometheus
* [**prometheus.io**](https://prometheus.io/)
* [dzone.com: Monitoring with **Prometheus**](https://dzone.com/articles/monitoring-with-prometheus) Learn how to set up a basic instance of Prometheus along with Grafana and the Node Exporter to monitor a simple Linux server.

### Prometheus Exporters (collectors)
* [**Prometheus exporters** (collectors)](https://prometheus.io/docs/instrumenting/exporters/)
* [**JMX Exporter**](https://github.com/prometheus/jmx_exporter) A process for exposing JMX Beans via HTTP for Prometheus consumption.
* [Maven Prometheus instrumentation library for JVM applications (client library)](https://mvnrepository.com/artifact/io.prometheus)
    * [github.com/prometheus/client_java](https://github.com/prometheus/client_java)

### Prometheus Exporters (third party)
* [Third Party Exporters](https://prometheus.io/docs/instrumenting/exporters/)

## Grafana
* [Grafana](https://grafana.com/)
* [Grafana Dashboards](https://grafana.com/grafana/dashboards)
* [github.com/mlabouardy: Grafana Dashboards](https://github.com/mlabouardy/grafana-dashboards)
* [grafana.com: Provisioning Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/)
    * [Grafana provisioning Ansible Role](https://github.com/cloudalchemy/ansible-grafana)
* [openlogic.com: How to develop Grafana Dashboards](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana)
* [Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus](https://github.com/percona/grafana-dashboards)

## Collectors
* [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector)
* [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)
* [Micrometer](http://micrometer.io/)
* [Prometheus Exporters](https://prometheus.io/docs/instrumenting/exporters/)
* [Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter)

## Prometheus Storage
* [Prometheus TSDB](https://prometheus.io/docs/prometheus/latest/storage/)
* [Cortex](https://cortexmetrics.io/) provides horizontally scalable, highly available, multi-tenant, long term storage for Prometheus. Cortex allows for storing time series data in a key-value store like Cassandra, AWS DynamoDB, or Google BigTable. It offers a Prometheus compatible query API, and you can push metrics into a write endpoint. This makes it best suited for cloud environments and multi-tenant scenarios like service providers building hosted and managed platforms.
* [**Thanos**:](https://thanos.io/) Open source, **highly available Prometheus setup with long term storage capabilities**. Thanos stores time series data in an object store like AWS S3, Google Cloud Storage, etc. Thanos pushes metrics through a side-car container from each Prometheus server through the gRPC store API to the query service in order to provide a global query view.
    * [github.com/ruanbekker: Thanos Cluster Setup](https://github.com/ruanbekker/thanos-cluster-setup) How to deploy a HA 
Prometheus setup with Unlimited Data Retention Capabilities on aws cloud S3 with Thanos Metrics.
* [**InfluxDB**:](https://www.influxdata.com/) open-source time series database (TSDB) developed by InfluxData. It is written in Go and optimized for fast, high-availability storage and retrieval of time series data in fields such as operations monitoring, application metrics, Internet of Things sensor data, and real-time analytics. It also has support for processing data from Graphite.
* [**M3**](https://www.m3db.io/) is an open source, large-scale metrics platform developed by Uber. It has its own time series database, M3DB. Like Thanos, M3 also uses a side-car container to push the metrics to the DB.
In addition, it supports metric deduplication and merging, and provides distributed query support.
Although it's exciting to see attempts to address the challenges of running Prometheus at scale, these are very young projects that are not widely used yet.


## Performance
* [dzone.com: The Keys to Performance Tuning and Testing](https://dzone.com/articles/the-keys-to-performance-tuning-and-testing)
* [dzone.com: How Performance Tuning and Testing are Changing](https://dzone.com/articles/how-performance-tuning-and-testing-are-changing)
* Java:
    * [developers.redhat.com: Troubleshooting java applications on openshift](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift/)
    * [dzone.com: how to take thread dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)
* [Performance Patterns in Microservices-Based Integrations 🌟🌟🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) Almost all applications that perform anything useful for a given business need to be integrated with one or more applications. With microservices-based architecture, where a number of services are broken down based on the services or functionality offered, the number of integration points or touch points increases massively.

## Distributed Tracing
- [**opentelemetry.io** 🌟🌟🌟](https://opentelemetry.io/) (**OpenTracing.io + OpenCensus.io = OpenTelemetry.io**)
- [**Jaeger** 🌟](https://www.jaegertracing.io/)
     - [Jaeger Demo1](https://github.com/obitech/micro-obs)
     - [Jaeger Demo 2](https://github.com/open-telemetry/opentelemetry-collector/tree/master/examples/demo)
     - [medium.com: **Jaeger embraces OpenTelemetry collector** 🌟🌟🌟](https://medium.com/jaegertracing/jaeger-embraces-opentelemetry-collector-90a545cbc24)
- [**zipkin.io**](https://zipkin.io/)
- [**OpenTracing.io**](https://opentracing.io/)
     - [lightstep.com: Understand Distributed Tracing](https://docs.lightstep.com/docs/understand-distributed-tracing)
   
## Application Performance Management
* [en.wikipedia.org/wiki/Application_performance_management](https://en.wikipedia.org/wiki/Application_performance_management)
* [dzone.com: APM Tools Comparison](https://dzone.com/articles/apm-tools-comparison-which-one-should-you-choose)
* [dzone.com: Java Performance Monitoring: 5 Open Source Tools You Should Know](https://dzone.com/articles/java-performance-monitoring-5-open-source-tools-you-should-know)
* [dzone.com: 14 best performance testing tools and APM solutions](https://dzone.com/articles/14-best-performance-testing-tools-and-apm-solution)
* [elastic.co: Using the Elastic APM Java Agent on Kubernetes](https://www.elastic.co/blog/using-elastic-apm-java-agent-on-kubernetes-k8s)
* Exception Tracking:
    * [sentry.io](https://sentry.io/)
    * APMs like Dynatrace, etc.
* APM Tools:
    * [datadoghq.com](https://www.datadoghq.com/)
    * [honeycomb.io](https://www.honeycomb.io)
    * [lightstep.com](https://lightstep.com)
    * [skywalking.apache.org](https://skywalking.apache.org/)
    * [Elastic APM](https://www.elastic.co/products/apm)
    * [AppDynamics 🌟🌟](https://www.appdynamics.com/)
    * [New Relic 🌟🌟](https://newrelic.com/)
    * [Dynatrace 🌟🌟🌟](https://www.dynatrace.com/)
* List of Performance Analysis Tools:
    * Threadumps + heapdumps + GC analysis tools
    * [en.wikipedia.org/wiki/List_of_performance_analysis_tools](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)
    * [InspectIT](https://en.wikipedia.org/wiki/InspectIT)
    * [VisualVM 🌟](https://en.wikipedia.org/wiki/VisualVM)
    * [OverOps](https://en.wikipedia.org/wiki/OverOps)
    * [FusionReactor](https://en.wikipedia.org/wiki/FusionReactor)
    * [tier1app.com](https://tier1app.com/)
    * [fastthread.io 🌟](https://fastthread.io/)
    * [gceasy.io 🌟](https://gceasy.io/)
    * [heaphero.io](https://heaphero.io/)

### Dynatrace APM
* [adictosaltrabajo.com: Monitorización y análisis de rendimiento de aplicaciones con Dynatrace APM](https://www.adictosaltrabajo.com/tutoriales/monitorizacion-y-analisis-de-rendimiento-de-aplicaciones-con-dynatrace/)
* [dynatrace.com: openshift monitoring](https://www.dynatrace.com/technologies/openshift-monitoring/)
* [dynatrace.com: Dynatrace monitoring for Kubernetes and OpenShift](https://www.dynatrace.com/news/blog/dynatrace-monitoring-for-kubernetes-and-openshift/)
* [dynatrace.com: Deploy OneAgent on OpenShift Container Platform](https://www.dynatrace.com/support/help/cloud-platforms/openshift/full-stack/deploy-oneagent-on-openshift-container-platform/)
* [Successful Kubernetes Monitoring – Three Pitfalls to Avoid](https://www.dynatrace.com/news/blog/successful-kubernetes-monitoring-3-pitfalls-to-avoid/)
* [My Dynatrace proof of concept 🌟](https://github.com/inafev/awesome-kubernetes/blob/master/pdf/dynatrace_demo.pdf)

## Other Awesome Lists
- [Awesome APM](https://github.com/antonarhipov/awesome-apm)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/J1S3NyN9ZeLjh9" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/challenges-in-a-microservices-age-monitoring-logging-and-tracing-on-red-hat-openshift" title="Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift" target="_blank">Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift</a> </strong> from <strong><a href="https://www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/lr07J585Y86D7i" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/monitoring-microservices-at-scale-on-openshift-67500621" title="Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)" target="_blank">Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)</a> </strong> from <strong><a href="//www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/CDyLLoStp2omzE" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/PurnimaKurella/dynatrace-70789377" title="Dynatrace" target="_blank">Dynatrace</a> </strong> from <strong><a href="https://www.slideshare.net/PurnimaKurella" target="_blank">Purnima Kurella</a></strong> </div>

