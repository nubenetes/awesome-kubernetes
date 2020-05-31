# Monitoring and Performance. Prometheus, Grafana, APMs and more
- [Monitoring](#monitoring)
- [OpenShift Cluster Monitoring Built-in solutions](#openshift-cluster-monitoring-built-in-solutions)
    - [OpenShift 3.11 Metrics and Logging](#openshift-311-metrics-and-logging)
        - [Prometheus and Grafana](#prometheus-and-grafana)
        - [Custom Grafana Dashboard for OpenShift 3.11](#custom-grafana-dashboard-for-openshift-311)
        - [Capacity Management Grafana Dashboard](#capacity-management-grafana-dashboard)
        - [Software Delivery Metrics Grafana Dashboard](#software-delivery-metrics-grafana-dashboard)
        - [Prometheus for OpenShift 3.11](#prometheus-for-openshift-311)
    - [OpenShift 4](#openshift-4)
- [Prometheus](#prometheus)
    - [Prometheus Storage](#prometheus-storage)
        - [Scalability, High Availability (HA) and Long-Term Storage](#scalability-high-availability-ha-and-long-term-storage)
        - [Storage Solutions for Prometheus](#storage-solutions-for-prometheus)
    - [Collectors. Software exposing Prometheus metrics](#collectors-software-exposing-prometheus-metrics)
        - [Prometheus Exporters. Plug-in architecture and extensibility with Prometheus Exporters (collectors)](#prometheus-exporters-plug-in-architecture-and-extensibility-with-prometheus-exporters-collectors)
        - [Prometheus Exporters Development. Node Exporter](#prometheus-exporters-development-node-exporter)
        - [Prometheus Third-party Collectors/Exporters](#prometheus-third-party-collectorsexporters)
            - [OpenTelemetry Collector](#opentelemetry-collector)
            - [Telegraf Collector](#telegraf-collector)
            - [Micrometer Collector](#micrometer-collector)
    - [Prometheus Alarms and Event Tracking](#prometheus-alarms-and-event-tracking)
    - [Prometheus and Cloud Monitoring](#prometheus-and-cloud-monitoring)
    - [Prometheus Installers](#prometheus-installers)
        - [Binaries, source code or Docker](#binaries-source-code-or-docker)
        - [Ansible Roles](#ansible-roles)
    - [Prometheus Operator](#prometheus-operator)
        - [kube Prometheus](#kube-prometheus)
        - [Prometheus Operator with Helm3](#prometheus-operator-with-helm3)
        - [Kubernetes Cluster Monitoring Stack based on Prometheus Operator](#kubernetes-cluster-monitoring-stack-based-on-prometheus-operator)
    - [Prometheus SaaS Solutions](#prometheus-saas-solutions)
- [Grafana](#grafana)
    - [Grafana Dashboards](#grafana-dashboards)
    - [Grafana 7](#grafana-7)
- [Proof of Concept: ActiveMQ Monitoring with Prometheus](#proof-of-concept-activemq-monitoring-with-prometheus)
    - [PoC: ActiveMQ 5.x Monitoring with Telegraf Collector, Prometheus and Grafana Dashboard 10702](#poc-activemq-5x-monitoring-with-telegraf-collector-prometheus-and-grafana-dashboard-10702)
        - [Deployment and Configuration](#deployment-and-configuration)
    - [PoC: ActiveMQ Artemis Monitoring with Prometheus Metrics Plugin (Micrometer Collector) and Prometheus. Grafana Dashboard not available](#poc-activemq-artemis-monitoring-with-prometheus-metrics-plugin-micrometer-collector-and-prometheus-grafana-dashboard-not-available)
        - [Deployment and Configuration](#deployment-and-configuration-1)
    - [Validation of Artemis Broker Monitoring with JMeter](#validation-of-artemis-broker-monitoring-with-jmeter)
        - [JMeter Example Test Plans](#jmeter-example-test-plans)
- [Kibana](#kibana)
- [Prometheus and Grafana Interactive Learning](#prometheus-and-grafana-interactive-learning)
- [Performance](#performance)
- [List of Performance Analysis Tools](#list-of-performance-analysis-tools)
    - [Thread Dumps. Debugging Java Applications](#thread-dumps-debugging-java-applications)
- [Debugging Java Applications on OpenShift and Kubernetes](#debugging-java-applications-on-openshift-and-kubernetes)
- [Distributed Tracing. OpenTelemetry and Jaeger](#distributed-tracing-opentelemetry-and-jaeger)
    - [Microservice Observability with Distributed Tracing. OpenTelemetry.io](#microservice-observability-with-distributed-tracing-opentelemetryio)
    - [Jaeger VS OpenTelemetry. How Jaeger works with OpenTelemetry](#jaeger-vs-opentelemetry-how-jaeger-works-with-opentelemetry)
- [Application Performance Management (APM)](#application-performance-management-apm)
    - [Elastic APM](#elastic-apm)
    - [Dynatrace APM](#dynatrace-apm)
- [Message Queue Monitoring](#message-queue-monitoring)
    - [Red Hat AMQ 7 Broker Monitoring solutions based on Prometheus and Grafana](#red-hat-amq-7-broker-monitoring-solutions-based-on-prometheus-and-grafana)
- [Other Awesome Lists](#other-awesome-lists)

## Monitoring
* [Wikipedia: Application Performance Index](https://en.wikipedia.org/wiki/Apdex)
* [thenewstack.io: The Challenges of Monitoring Kubernetes and OpenShift](https://thenewstack.io/the-challenges-of-monitoring-kubernetes-and-openshift/)
* [dzone.com: Kubernetes Monitoring: Best Practices, Methods, and Existing Solutions](https://dzone.com/articles/kubernetes-monitoring-best-practices-methods-and-e) Kubernetes handles containers in several computers, removing the complexity of handling distributed processing. But what's the best way to perform Kubernetes monitoring?
* [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb/)

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
* [redhat.com: **How to gather and display metrics in Red Hat OpenShift** (Prometheus + Grafana)](https://www.redhat.com/en/blog/how-gather-and-display-metrics-red-hat-openshift)
* [Generally Available today: Red Hat OpenShift Container Platform 3.11 is ready to power enterprise Kubernetes deployments 🌟](https://www.redhat.com/en/blog/generally-available-today-red-hat-openshift-container-platform-311-ready-power-enterprise-kubernetes-deployments)
* [The Challenges of Monitoring Kubernetes and OpenShift 3.11 🌟](https://thenewstack.io/the-challenges-of-monitoring-kubernetes-and-openshift/)
* [OCP 3.11 Metrics and Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging)
* [Prometheus Cluster Monitoring 🌟](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html)
* [Prometheus Alert Manager](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-alertmanager_prometheus-cluster-monitoring)
* [Leveraging Kubernetes and OpenShift for automated performance tests (part 1)](https://developers.redhat.com/blog/2018/11/22/automated-performance-testing-kubernetes-openshift/)
* [Building an observability stack for automated performance tests on Kubernetes and OpenShift (part 2) 🌟](https://developers.redhat.com/blog/2019/01/03/leveraging-openshift-or-kubernetes-for-automated-performance-tests-part-2/)

[![openshift3 Monitoring](images/ocp_monitoring.png)](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html)

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

## Prometheus
* [**prometheus.io**](https://prometheus.io/)
* [dzone.com: Monitoring with **Prometheus**](https://dzone.com/articles/monitoring-with-prometheus) Learn how to set up a basic instance of Prometheus along with Grafana and the Node Exporter to monitor a simple Linux server.
* [github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)
* [Monitoring With Prometheus](https://dzone.com/articles/monitoring-with-prometheus)
* [Dzone Refcard: Scaling and Augmenting Prometheus](https://dzone.com/refcardz/scaling-and-augmenting-prometheus) Prometheus is an open-source infrastructure and services monitoring system popular for Kubernetes and cloud-native services and apps. It can help make metric collection easier, correlate events and alerts, provide security, and do troubleshooting and tracing at scale. This Refcard will teach you how to pave the path for Prometheus adoption, what observability looks like beyond Prometheus, and how Prometheus helps provide scalability, high availability, and long-term storage.
* [Monitoring Self-Destructing Apps Using Prometheus](https://dzone.com/articles/prometheus-collectors) Learn how to configure Prometheus collectors and their use cases.
* [Monitoring kubernetes with Prometheus](https://opensource.com/article/19/11/introduction-monitoring-prometheus)
* [Focus on Detection: Prometheus and the Case for Time Series Analysis](https://dzone.com/articles/focus-on-detectionprometheus-and-the-case-for-time)
* [Ensure High Availability and Uptime With Kubernetes Horizontal Pod Autoscaler (HPA) and Prometheus](https://dzone.com/articles/ensure-high-availability-and-uptime-with-kubernete)
* [Prometheus 2 Times Series Storage Performance Analyses](https://dzone.com/articles/prometheus-2-times-series-storage-performance-anal)
* [Set Up and Integrate Prometheus With Grafana for Monitoring.](https://dzone.com/articles/monitoring-using-spring-boot-20-prometheus-and-gra) How to set up and configure Prometheus and Grafana to enable application performance monitoring for REST applications.
* [Discover Applications Running on Kubernetes With Prometheus](https://dzone.com/articles/discover-applications-running-on-kubernetes-with-p)
* [Prometheus vs. Graphite: Which Should You Choose for Time Series or Monitoring?](https://dzone.com/articles/prometheus-vs-graphite-which-should-you-choose-for)
* [PromQL Tutorial](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085)
* [How to use Ansible to set up system monitoring with Prometheus](https://opensource.com/article/18/3/how-use-ansible-set-system-monitoring-prometheus)
* [Initial experiences with the Prometheus monitoring system](https://medium.com/@griggheo/initial-experiences-with-the-prometheus-monitoring-system-167054ac439c)
* [prometheus.io/docs/instrumenting/writing_exporters/](https://prometheus.io/docs/instrumenting/writing_exporters/)
* [devconnected.com/complete-node-exporter-mastery-with-prometheus/](https://devconnected.com/complete-node-exporter-mastery-with-prometheus/)
* [www.scalyr.com/blog/prometheus-metrics-by-example/](https://www.scalyr.com/blog/prometheus-metrics-by-example/)
* Prometheus es un "time series DBMS" y sistema de monitorización completo, que incluye recogida de datos, almacenamiento, visualización y exportación. 
* La **arquitectura de Prometheus** se basa en **"pull metrics" (extracción de métricas)**. En lugar de empujar las métricas ("pushing metrics") hacia la herramienta de monitorización, **extrae ("pull") las métricas de los servicios (por defecto un "/metrics" HTTP endpoint)** en texto plano (parseable por humanos y de fácil diagnóstico). Prometheus también tiene un "push gateway", de modo que también soporta "push" para métricas específicas cuando el modelo de "pull" no funciona (si bien este método no es recomendable).
* Prometheus se puede conectar a **series de tiempo (time series)** con un nombre de métrica y pares clave-valor, simplificando la monitorización en complejos entornos cloud multi-nodo.
* La herramienta también proporciona [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/), para el procesado de datos "time-series". Permite realizar consultas (queries) para la manipulación de datos y generar nueva información relevante. Con [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) se pueden generar gráficos, visualizar conjuntos de datos, crear tablas, y generar alertas basadas en parámetros específicos. 
* La consola web de Prometheus permite gestionar todas las características y herramientas disponibles en Prometheus. Se pueden utilizar expresiones regulares y consultas avanzadas de [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) para la creación de conjuntos de datos (datasets) y alertas.
* Prometheus activamente "scrapea" datos, los almacena, y soporta "queries", "gráficos" y "alertas", así como proporciona "endpoints" a otros consumidores API como Grafana. Todo esto lo realiza con los siguientes componentes:
    * [Librerías cliente](https://prometheus.io/docs/instrumenting/clientlibs/): instrumentación del código de aplicación (para generar eventos).
    * [Servidor Prometheus](https://github.com/prometheus/prometheus): "scrapeando" y almacenando estos eventos, cuando se generan, como "time series data". Este es el **modelo "pull"** más común para la recogida general de métricas en Prometheus.
    * [Pushgateway](https://github.com/prometheus/pushgateway): **Modelo "Push"**, soportando trabajos efímeros de importación de datos. **Sólo recomendable en aplicaciones "serverless"**, donde las aplicaciones son lanzadas y destruidas bajo demanda, así como las aplicaciones que manejan "batch jobs". 
    * [Exportadores de Datos](https://prometheus.io/docs/instrumenting/exporters/): exportando servicios como HAProxy, StatsD, Graphite, etc.
* Prometheus se diferencia de otros sistemas de monitorización con las siguientes funcionalidades:
    *	Modelo de datos multi-dimensional, donde los "time-series data" se definen por el nombre de la métrica y dimensiones clave/valor.
    *	Nodos únicos de servidor y autónomos, sin dependencia de almacenamiento distribuido.
    *	Recogida de datos via un modelo "pull" sobre HTTP.
    *	"Time Series Data" empujado ("pushed") a otros destinos de datos vía un gateway intermediario.
    *	"Targets" descubiertos via "service discovery" ó configuración estática.
    *	Soporte de federación horizontal y vertical.
* [magalix.com: Monitoring of Kubernetes Clusters To Manage Large Scale Projects](https://www.magalix.com/blog/monitor-kuberentes-cluster-to-manage-large-scale-projects)

[![prometheus architecture](images/prometheus-architecture.png)](https://github.com/prometheus/prometheus)

### Prometheus Storage
* Proporciona etiquetado clave-valor y "time-series".  La propia documentación de Prometheus explica cómo se gestiona el [almacenamiento en disco](https://prometheus.io/docs/prometheus/latest/storage/) (**Prometheus Time-Series DB**). La ingestión de datos se agrupa en bloques de dos horas, donde cada bloque es un directorio conteniendo uno o más "chunk files" (los datos), además de un fichero de metadatos y un fichero index:
* Almacenamiento de datos en disco (Prometheus Time-Series DB):
```
./data/01BKGV7JBM69T2G1BGBGM6KB12
./data/01BKGV7JBM69T2G1BGBGM6KB12/meta.json
./data/01BKGV7JBM69T2G1BGBGM6KB12/wal
./data/01BKGV7JBM69T2G1BGBGM6KB12/wal/000002
./data/01BKGV7JBM69T2G1BGBGM6KB12/wal/000001
```
* Un proceso en segundo plano compacta los bloques de dos horas en otros más grandes.
* Es posible almacenar los datos en otras soluciones de "Time-Series Database" como **InfluxDB**.

#### Scalability, High Availability (HA) and Long-Term Storage
* Prometheus fue diseñado para ser fácil de desplegar. Es extremadamente fácil ponerlo en marcha, recoger algunas métricas, y empezar a construir nuestra propia herramienta de monitorización. Las cosas se complican cuando se intenta operar a un nivel de escalado considerable.
* Para entender si esto va a ser un problema, conviene plantearse las siguiente preguntas:
    -	¿Cuántas métricas puede ingerir el sistema de monitorización y cuántas son necesarias?
    -	¿Cuál es la cardinalidad de las métricas? La cardinalidad es el número de etiquetas que cada métrica puede tener. Es una cuestión muy frecuente en las métricas pertenecientes a entornos dinámicos donde a los contenedores se les asignan un ID ó nombre diferente cada vez que son lanzados, reiniciados o movidos entre nodos (caso de kubernetes).
    -	¿Es necesaria la Alta Disponibilidad (HA)?
    -	¿Durante cuánto tiempo es necesario mantener las métricas y con qué resolución? 
* La implementación de HA es laboriosa porque la funcionalidad de cluster requiere añadir plugins de terceros al servidor Prometheus. Es necesario tratar con "backups" y "restores", y el almacenamiento de métricas por un periodo de tiempo extendido hará que la base de datos crezca exponencialmente. Los servidores Prometheus proporcionan almacenamiento persistente, pero Prometheus no fue creado para el almacenamiento distribuido de métricas a lo largo de múltiples nodos de un cluster con replicación y capacidad curativa (como es el caso de Kubernetes).  Esto es conocido como **"almacenamiento a largo-plazo" (Long-Term)** y actualmente es un requisito en unos pocos casos de uso, por ejemplo en la planificación de la capacidad para monitorizar cómo la infraestructura necesita evolucionar, contracargos para facturar diferentes equipos ó departamentos para un caso específico que han hecho de la infraestructura, análisis de tendencias de uso, o adherirse a regulaciones para verticales específicos como banca, seguros, etc. 

#### Storage Solutions for Prometheus
* [**Prometheus TSDB**](https://prometheus.io/docs/prometheus/latest/storage/)
* [**Cortex**:](https://cortexmetrics.io/) Provides horizontally scalable, highly available, multi-tenant, long term storage for Prometheus. Cortex allows for storing time series data in a key-value store like Cassandra, AWS DynamoDB, or Google BigTable. It offers a Prometheus compatible query API, and you can push metrics into a write endpoint. This makes it best suited for cloud environments and multi-tenant scenarios like service providers building hosted and managed platforms.
    * [Weave Cortex SaaS (Hosted Prometheus - Public Cloud)](https://www.weave.works/features/prometheus-monitoring/)
* [**Thanos**:](https://thanos.io/) Open source, **highly available Prometheus setup with long term storage capabilities**. 
    * Thanos stores time series data in an object store like AWS S3, Google Cloud Storage, etc. Thanos pushes metrics through a side-car container from each Prometheus server through the gRPC store API to the query service in order to provide a global query view.
    * [github.com/ruanbekker: Thanos Cluster Setup](https://github.com/ruanbekker/thanos-cluster-setup) How to deploy a HA Prometheus setup with Unlimited Data Retention Capabilities on aws cloud S3 with Thanos Metrics.
    * [Highly Available Prometheus Metrics for Distributed SQL with Thanos on GKE](https://blog.yugabyte.com/highly-available-prometheus-metrics-for-distributed-sql-with-thanos-on-gke/)
* [**InfluxDB**:](https://www.influxdata.com/) An [open-source time series database (TSDB)](https://en.wikipedia.org/wiki/Time_series_database) developed by InfluxData. It is written in [Go](https://en.wikipedia.org/wiki/Go_(programming_language)) and optimized for fast, high-availability storage and retrieval of [time series](https://en.wikipedia.org/wiki/Time_series) data in fields such as operations monitoring, application metrics, [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things) sensor data, and real-time analytics. It also has support for processing data from [Graphite](https://en.wikipedia.org/wiki/Graphite_(software)).
    * [en.wikipedia.org/wiki/InfluxDB](https://en.wikipedia.org/wiki/MIT_License)
    * [en.wikipedia.org/wiki/MIT_License](https://en.wikipedia.org/wiki/MIT_License)
    * [dzone: Flux queries](https://dzone.com/articles/flux-windowing-and-aggregation) New language being developed at InfluxData.
* [**M3**:](https://www.m3db.io/) An open source, large-scale metrics platform developed by Uber. It has its own time series database, M3DB. Like Thanos, M3 also uses a side-car container to push the metrics to the DB.
In addition, it supports metric deduplication and merging, and provides distributed query support.
Although it's exciting to see attempts to address the challenges of running Prometheus at scale, these are very young projects that are not widely used yet.

### Collectors. Software exposing Prometheus metrics

#### Prometheus Exporters. Plug-in architecture and extensibility with Prometheus Exporters (collectors)
* Prometheus proporciona un ecosistema de **"exporters"**, los cuales permiten que herramientas de terceros puedan exportar sus datos en Prometheus. Muchos componentes de software de código abierto son compatibles por defecto. 
* **Un "exporter" expone las métricas de uno ó varios "collectors".**
* [Prometheus Exporters](https://prometheus.io/docs/instrumenting/exporters/)
    * [prometheus.io/download/](https://prometheus.io/download/)
    * [github.com/prometheus](https://github.com/prometheus)
* [Prometheus JMX Exporter:](https://github.com/prometheus/jmx_exporter) A process for exposing JMX Beans via HTTP for Prometheus consumption.
* [Example: How to Use Prometheus Monitoring With Java to Gather Data. Gathering Java Metrics with Prometheus Monitoring (ActiveMQ)](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)
* [Maven Prometheus instrumentation library for JVM applications (client library)](https://mvnrepository.com/artifact/io.prometheus)
    * [github.com/prometheus/client_java](https://github.com/prometheus/client_java)
* [Example: JMX Exporter with ActiveMQ](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)

#### Prometheus Exporters Development. Node Exporter
* Node exporter puede ser utilizado para exportar las métricas de nuestra aplicación ya que permite exportar un "text-file". Nuestra aplicación puede escribir datos en un fichero de texto con el formato de datos de Prometheus. Este fichero de texto con datos agregados sería exportado a Prometheus con Node Exporter. 
* [dzone.com: Monitoring Self-Destructing Apps Using Prometheus](https://dzone.com/articles/prometheus-collectors) Learn how to configure Prometheus collectors and their use cases.
* [prometheus.io: Writing Exporters](https://prometheus.io/docs/instrumenting/writing_exporters/)
* [devconnected.com: Complete Node Exporter Mastery with Prometheus](https://devconnected.com/complete-node-exporter-mastery-with-prometheus)
* [scalyr.com: Prometheus metrics by example: 5 things you can learn](https://www.scalyr.com/blog/prometheus-metrics-by-example/)

#### Prometheus Third-party Collectors/Exporters
* Some third-party software exposes metrics in the Prometheus format, so no separate exporters are needed.
* [Prometheus Third Party Exporters](https://prometheus.io/docs/instrumenting/exporters/)
  
##### OpenTelemetry Collector
* [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

##### Telegraf Collector
* [Telegraf Collector](https://www.influxdata.com/time-series-platform/telegraf/)
* [Telegraf Prometheus Output Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/prometheus_client)
* [Telegraf Ansible Role](https://github.com/rossmcdonald/telegraf)
* [Grafana Dashboards with Telegraf Collectors](https://grafana.com/grafana/dashboards?collector=Telegraf)
* [dzone: Synthetic Monitoring With Telegraf (white-box monitoring)](https://dzone.com/articles/synthetic-monitoring-with-telegraf) Monitoring based on metrics exposed by the internals of the system

##### Micrometer Collector
* [**Micrometer** Collector](http://micrometer.io/)
* [Micrometer Prometheus](https://micrometer.io/docs/registry/prometheus)

### Prometheus Alarms and Event Tracking
* Prometheus no soporta rastreo de eventos (event tracking), pero ofrece un soporte completo de alarmas y gestión de alarmas. El lenguaje de consultas (queries) de Prometheus permite en cambio implementar rastreo de eventos por cuenta propia.

### Prometheus and Cloud Monitoring
* AWS CloudWatch is supported by Prometheus.

### Prometheus Installers
#### Binaries, source code or Docker
* [prometheus.io: Installarion](https://prometheus.io/docs/prometheus/latest/installation/)
* [prometheus.io: Getting Started](https://prometheus.io/docs/prometheus/latest/getting_started/) 
* [github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)

#### Ansible Roles
- **Cloud Alchemy**: Deploy prometheus node exporter using ansible.
    - [galaxy.ansible.com/cloudalchemy/node-exporter](https://galaxy.ansible.com/cloudalchemy/node-exporter)
    - [github.com/cloudalchemy/ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)
- [Idealista: This ansible role installs a Prometheus Node Exporter in a debian environment](https://github.com/idealista/prometheus_jmx_exporter-role)
- **Alexdzyoba**: This ansible role installs a Prometheus JMX exporter java agent in a debian nvironment. Inspired by [Idealista prometheus_jmx_exporter-role](https://github.com/dealista/prometheus_jmx_exporter-role).
    - [galaxy.ansible.com/alexdzyoba/jmx-exporter](https://galaxy.ansible.com/alexdzyoba/jmx-exporter) 
    - [github.com/alexdzyoba/ansible-jmx-exporter](https://github.com/alexdzyoba/ansible-jmx-exporter)
- **Mesaguy**: Installs and manages Prometheus and Prometheus exporters.
    - Installs and manages Prometheus server, Alertmanager, PushGateway, and numerous Prometheus exporters
    - This role was designed to allow adding new exporters with ease. Regular releases ensure it always provides the latest Prometheus software.
    - This role can register client exporters with the Prometheus server/s automatically (see tgroup management below).
    - This Ansible role will be migrated to an Ansible Collection.
    - [galaxy.ansible.com/mesaguy/prometheus](https://galaxy.ansible.com/mesaguy/prometheus)
    - [github.com/mesaguy/ansible-prometheus](https://github.com/mesaguy/ansible-prometheus)
- **William Yeh**: Prometheus for Ansible Galaxy. This role only installs 3 components: Prometheus server, Node exporter, and Alertmanager. 
    - [galaxy.ansible.com/William-Yeh/prometheus](https://galaxy.ansible.com/William-Yeh/prometheus) 
    - [github.com/William-Yeh/ansible-prometheus](https://github.com/William-Yeh/ansible-prometheus)
    - [awesomeopensource.com/project/William-Yeh/ansible-prometheus](https://awesomeopensource.com/project/William-Yeh/ansible-prometheus)
- **Undergreen**: An Ansible role that installs Prometheus Node Exporter on Ubuntu|Debian|redhat-based machines with systemd|Upstart|sysvinit.
    - [galaxy.ansible.com/UnderGreen/prometheus-node-exporter](https://galaxy.ansible.com/UnderGreen/prometheus-node-exporter) 
    - [github.com/UnderGreen/ansible-prometheus-node-exporter](https://github.com/UnderGreen/ansible-prometheus-node-exporter)
- **Mitesh Sharma**: Prometheus With Grafana Using Ansible
    - [itnext.io/prometheus-with-grafana-using-ansible-549e575c9dfa](https://itnext.io/prometheus-with-grafana-using-ansible-549e575c9dfa)
    - [github.com/MiteshSharma/PrometheusWithGrafana](https://github.com/MiteshSharma/PrometheusWithGrafana)

### Prometheus Operator 
#### kube Prometheus
* [kube-prometheus](https://github.com/coreos/kube-prometheus) Use Prometheus to monitor Kubernetes and applications running on Kubernetes.

#### Prometheus Operator with Helm3
* [devstack.in: Deploy Prometheus Operator with Helm3 and Private Registry 🌟](https://devstack.in/2020/05/25/deploy-prometheus-operator-with-helm3-and-private-registry/)

#### Kubernetes Cluster Monitoring Stack based on Prometheus Operator
- [Cluster Monitoring stack for ARM / X86-64 platforms](https://github.com/carlosedp/cluster-monitoring) Updated the cluster-monitoring stack for kubernetes to latest versions. Fresh Grafana 7, Prometheus Operator and more. This repository collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.

### Prometheus SaaS Solutions
* [Weave Cortex SaaS (Hosted Prometheus - Public Cloud)](https://www.weave.works/features/prometheus-monitoring/)

## Grafana
* [Grafana](https://grafana.com/) 
* Prometheus utiliza plantillas de consola para los dashboards, si bien su curva de aprendizaje de sus múltiples funcionalidades es alta, con una interfaz de usuario insuficiente. Por este motivo es muy habitual utilizar **Grafana** como interfaz de usuario.
* [grafana.com: Provisioning Grafana 🌟](https://grafana.com/docs/grafana/latest/administration/provisioning/) Las últimas versiones de Grafana permiten la creación de "datasources" y "dashboards" con Ansible, mediante las opciones de provisión de Grafana. Funciona con cualquier "datasource" (Prometheus, InfluxDB, etc), incluyendo la configuración de Grafana correspondiente y dejando poco margen para el error humano.
    * [Grafana provisioning Ansible Role](https://github.com/cloudalchemy/ansible-grafana)
 
### Grafana Dashboards
* [Grafana Dashboards](https://grafana.com/grafana/dashboards)
* [github.com/mlabouardy: Grafana Dashboards](https://github.com/mlabouardy/grafana-dashboards)
* [openlogic.com: How to develop Grafana Dashboards 🌟](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana)
* [Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus 🌟](https://github.com/percona/grafana-dashboards)
* [Prometheus Monitoring With Grafana. Prometheus Stats Dashboard and Prometheus Benchmark Dashboard](https://dzone.com/articles/prometheus-monitoring-with-grafana). How you construct your Prometheus monitoring dashboard involves trial and error. Grafana makes this exploration very easy and Prometheus has good built-in functionality.

Monitored Component|Collector|Dashboard Number|URL
:------------------|:-------|:---------------|------------
ActiveMQ 5.x "classic"|[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)|[10702](https://grafana.com/grafana/dashboards/10702)|[Ref1](https://docs.wavefront.com/activemq.html), [Ref2](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/activemq), [Ref3](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/activemq.yml), [Ref4](https://stackoverflow.com/questions/57107282/prometheus-and-activemq-integration)
ActiveMQ Artemis/Red Hat AMQ Broker|[JMX Exporter](https://github.com/prometheus/jmx_exporter)|[9087](https://grafana.com/grafana/dashboards/9087)|[Ref1](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/artemis-2.yml), [Ref2](http://techiekhannotes.blogspot.com/2018/12/artemis-monitoring-with-grafana.html), [Ref3](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin)
Message Streams like Kafka/Red Hat AMQ Streams|Other|[9777](https://grafana.com/grafana/dashboards/9777)|  

### Grafana 7
- [Open source observability, meet data transformation: Grafana 7.0 promises to connect, unify, and visualize all your data](https://www.zdnet.com/article/open-source-observability-meet-data-transformation-grafana-7-0-promises-to-connect-unify-and-visualize-all-your-data/) Grafana Labs sets the bar for open source observability with Grafana 7.0: more developer friendly, more data sources, data transformation, and growth in the cloud and on premise
- [Grafana 7.0: “We’ve built one of the best visualisation tools and it’s not tied to any one database”](https://jaxenter.com/grafana-7-0-interview-tom-wilkie-172261.html)

## Proof of Concept: ActiveMQ Monitoring with Prometheus 
The aim of this Proof of Concept is to learn Prometheus by example being [Red Hat AMQ 7 (broker)](https://developers.redhat.com/products/amq/overview) on RHEL the application to be monitored. Red Hat AMQ Broker is based on ActiveMQ Artemis, being this the reason why one of the following proof of concepts is done with Artemis (the other one was run in order to learn telegraf, prometheus and grafana). The same solution tested with Artemis on RHEL is valid for Red Hat AMQ 7 Broker on RHEL. 

Red Hat AMQ 7 Broker is OpenShift 3.11 compliant as Technical Preview and deployed as Operator.

Red Hat AMQ 7 Operator is fully supported in OpenShift 4.x, initially with Prometheus and Grafana monitoring already setup and maintained by AMQ Operator. It is recommended to check the metrics collected and displayed by AMQ Operator with another Proof of Concept in OpenShift 4.x. 

### PoC: ActiveMQ 5.x Monitoring with Telegraf Collector, Prometheus and Grafana Dashboard 10702
* Latest releases of Telegraf and Prometheus have been used in this Proof of Concept:
    * [telegraf-1.14.0-1 (rpm)](https://www.influxdata.com/time-series-platform/telegraf/)
    * [grafana-6.3.2-1.x86_64 (rpm)](https://grafana.com/) This is the release specified as requirement for this grafana dashboard. Newer releases of grafana are probably compliant.
    * [prometheus-2.17.1.linux-amd64 (.tar.gz)](https://prometheus.io/)
    * [apache-activemq-5.15.12 (.tar.g)](https://activemq.apache.org/components/classic/)
* References:
    * [activemq.apache.org/components/classic/documentation](https://activemq.apache.org/components/classic/documentation)
    * [grafana.com/grafana/dashboards/10702](https://grafana.com/grafana/dashboards/10702) 
    * [github.com/influxdata/telegraf/tree/master/plugins/inputs/activemq](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/activemq) 
    * [docs.wavefront.com/activemq.html](https://docs.wavefront.com/activemq.html)

#### Deployment and Configuration
* Systemd 

```
/etc/systemd/system/prometheus.service
/etc/systemd/system/activemq.service
/usr/lib/systemd/system/telegraf.service
/usr/lib/systemd/system/grafana-server.service
```

* Systemctl

```bash
systemctl daemon-reload
for service in activemq telegraf prometheus grafana-server; do systemctl status $service; done
for service in activemq telegraf prometheus grafana-server; do systemctl restart $service; done
for service in activemq telegraf prometheus grafana-server; do systemctl stop $service; done
for service in activemq telegraf prometheus grafana-server; do systemctl start $service; done
```

*  Jolokia Permissions already integrated in ActiveMQ by default. Jolokia permissions have been disabled by renaming "jolokia-access.xml" to "jolokia-access.xmlORIG" (this is a Proof of Concept):

```bash
mv /opt/activemq/webapps/api/WEB-INF/classes/jolokia-access.xml /opt/activemq/webapps/api/WEB-INF/classes/jolokia-access.xmlORIG
```

* Telegraf Jolokia Input Plugin /etc/telegraf/telegraf.d/activemq.conf 

```
[[inputs.jolokia2_agent]]
urls = ["http://localhost:8161/api/jolokia"]
name_prefix = "activemq."
username = "admin"
password = "admin"
### JVM Generic
[[inputs.jolokia2_agent.metric]]
name  = "OperatingSystem"
mbean = "java.lang:type=OperatingSystem"
paths = ["ProcessCpuLoad","SystemLoadAverage","SystemCpuLoad"]
[[inputs.jolokia2_agent.metric]]
name  = "jvm_runtime"
mbean = "java.lang:type=Runtime"
paths = ["Uptime"]
[[inputs.jolokia2_agent.metric]]
name  = "jvm_memory"
mbean = "java.lang:type=Memory"
paths = ["HeapMemoryUsage", "NonHeapMemoryUsage", "ObjectPendingFinalizationCount"]
[[inputs.jolokia2_agent.metric]]
name     = "jvm_garbage_collector"
mbean    = "java.lang:name=*,type=GarbageCollector"
paths    = ["CollectionTime", "CollectionCount"]
tag_keys = ["name"]
[[inputs.jolokia2_agent.metric]]
name       = "jvm_memory_pool"
mbean      = "java.lang:name=*,type=MemoryPool"
paths      = ["Usage", "PeakUsage", "CollectionUsage"]
tag_keys   = ["name"]
tag_prefix = "pool_"
### ACTIVEMQ
[[inputs.jolokia2_agent.metric]]
name     = "queue"
mbean    = "org.apache.activemq:brokerName=*,destinationName=*,destinationType=Queue,type=Broker"
paths    = ["QueueSize","EnqueueCount","ConsumerCount","DispatchCount","DequeueCount","ProducerCount","InFlightCount"]
tag_keys = ["brokerName","destinationName"]
[[inputs.jolokia2_agent.metric]]
name     = "topic"
mbean    = "org.apache.activemq:brokerName=*,destinationName=*,destinationType=Topic,type=Broker"
paths    = ["ProducerCount","DequeueCount","ConsumerCount","QueueSize","EnqueueCount"]
tag_keys = ["brokerName","destinationName"]
[[inputs.jolokia2_agent.metric]]
name     = "broker"
mbean    = "org.apache.activemq:brokerName=*,type=Broker"
paths    = ["TotalConsumerCount","TotalMessageCount","TotalEnqueueCount","TotalDequeueCount","MemoryLimit","MemoryPercentUsage","StoreLimi
t","StorePercentUsage","TempPercentUsage","TempLimit"]
tag_keys = ["brokerName"]
```

*  InfluxDB: Not required.
* Defautl /etc/telegraf/telegraf.conf file is modified to allow Prometheus to collect ActiveMQ metrics by pulling Telegraf metrics:

```
  # # Configuration for the Prometheus client to spawn
  [[outputs.prometheus_client]]
  #   ## Address to listen on
      listen = ":9273"
      ## Path to publish the metrics on.
      path = "/metrics"
  ...
  ...
  # # Gather ActiveMQ metrics
  [[inputs.activemq]]
  #   ## ActiveMQ WebConsole URL
  url = "http://127.0.0.1:8161"
  #   ## Credentials for basic HTTP authentication
  username = "admin"
  password = "admin"
  ...
  ...
```

* scrape_configs in /opt/prometheus/prometheus.yml 

```
  scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
      # metrics_path defaults to '/metrics'
      # scheme defaults to 'http'.
      static_configs:
      - targets: ['localhost:9090']
  - job_name: 'broker'
      static_configs:
      - targets: ['localhost:9273']
```

* Grafana Dashboard [10702](https://grafana.com/grafana/dashboards/10702) is imported from Grafana UI -> "import dashboard". Prometheus data source is connected manually with Grafana via Grafana UI.

### PoC: ActiveMQ Artemis Monitoring with Prometheus Metrics Plugin (Micrometer Collector) and Prometheus. Grafana Dashboard not available
* Latest releases of ActiveMQ Artemis and Prometheus have been used in this Proof of Concept:
    * [grafana-6.7.2-1.x86_64.rpm](https://grafana.com/)
    * [prometheus-2.17.1.linux-amd64](https://prometheus.io)
    * [apache-artemis-2.11.0](https://activemq.apache.org/components/artemis/) 
    * [apache-maven-3.6.3](https://maven.apache.org/)
* ActiveMQ Artemis can export metrics to several monitoring systems via [Artemis Prometheus Metrics Plugin](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin), which uses [Micrometer Collector](https://micrometer.io/). Check [this link](http://activemq.apache.org/components/artemis/documentation/latest/metrics.html).
* Unfortunately, there's no Grafana Dashboard available for this plugin. In consequence [a new Grafana Dashboard has to be developed from scratch](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana).
* [Artemis Prometheus Metrics Plugin](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin) is the recommended approach. Use [JMX Exporter](https://github.com/prometheus/jmx_exporter) to export other metrics.
* References:
    * [Apache ActiveMQ Artemis Using the Server](https://activemq.apache.org/components/artemis/documentation/latest/using-server.html)
    * [Apache ActiveMQ Artemis Management Console](https://activemq.apache.org/components/artemis/documentation/latest/management-console.html)
    * [Apache ActiveMQ Artemis Metrics](http://activemq.apache.org/components/artemis/documentation/latest/metrics.html)

#### Deployment and Configuration
* systemd

```
/etc/systemd/system/prometheus.service
/etc/systemd/system/artemis.service
/usr/lib/systemd/system/grafana-server.service
```

* systemctl

```bash
# systemctl enable artemis
# systemctl daemon-reload

 for service in artemis prometheus grafana-server; do systemctl status $service; done
 for service in artemis prometheus grafana-server; do systemctl restart $service; done
 for service in artemis prometheus grafana-server; do systemctl stop $service; done
 for service in artemis prometheus grafana-server; do systemctl start $service; done
```

* Creation of Artemis Broker

```bash
cd /var/lib
/opt/artemis/bin/artemis create --addresses 192.168.1.38 --allow-anonymous --home /opt/artemis --host <my_servername.my_domain> --http-host <my_servername.my_domain> --name <my_servername.my_domain> --queues queue1,queue2 --user artemisuser --password artemispassword artemisbroker

Creating ActiveMQ Artemis instance at: /var/lib/artemisbroker

Auto tuning journal ...
done! Your system can make 13.89 writes per millisecond, your journal-buffer-timeout will be 72000

You can now start the broker by executing:

   "/var/lib/artemisbroker/bin/artemis" run

Or you can run the broker in the background using:

   "/var/lib/artemisbroker/bin/artemis-service" start
```

* Permissions change in broker directory

```bash
# chown -R activemq. /var/lib/artemisbroker/
```

* Running artemis broker

```bash
# su - activemq
$ cd /var/lib/artemisbroker/
$ /var/lib/artemisbroker/bin/artemis run
```

* Artemis Prometehus Console Access. We can now access to Artemis Console via http://my_servername.my_domain:8161/console using the credentials specified during the CLI deployment (artemisuser / artemispassword)

* [Artemis Prometheus Plugin](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin)

```bash
activemq@my_servername ~]$ pwd
/home/activemq
[activemq@my_servername ~]$ cd artemis-prometheus-metrics-plugin/
[activemq@my_servername artemis-prometheus-metrics-plugin]$ mvn install
...
[INFO] Replacing /home/activemq/artemis-prometheus-metrics-plugin/artemis-prometheus-metrics-plugin/target/artemis-prometheus-metrics-plug
in-1.0.0.CR1.jar with /home/activemq/artemis-prometheus-metrics-plugin/artemis-prometheus-metrics-plugin/target/artemis-prometheus-metrics
-plugin-1.0.0.CR1-shaded.jar
[INFO] Dependency-reduced POM written at: /home/activemq/artemis-prometheus-metrics-plugin/artemis-prometheus-metrics-plugin/dependency-re
duced-pom.xml
[INFO]
[INFO] --- maven-install-plugin:2.4:install (default-install) @ artemis-prometheus-metrics-plugin ---
[INFO] Installing /home/activemq/artemis-prometheus-metrics-plugin/artemis-prometheus-metrics-plugin/target/artemis-prometheus-metrics-plu
gin-1.0.0.CR1.jar to /home/activemq/.m2/repository/org/apache/activemq/artemis-prometheus-metrics-plugin/1.0.0.CR1/artemis-prometheus-metr
ics-plugin-1.0.0.CR1.jar
[INFO] Installing /home/activemq/artemis-prometheus-metrics-plugin/artemis-prometheus-metrics-plugin/dependency-reduced-pom.xml to /home/a
ctivemq/.m2/repository/org/apache/activemq/artemis-prometheus-metrics-plugin/1.0.0.CR1/artemis-prometheus-metrics-plugin-1.0.0.CR1.pom
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary for artemis-prometheus-metrics-pom 1.0.0.CR1:
[INFO]
[INFO] artemis-prometheus-metrics-pom ..................... SUCCESS [  0.328 s]
[INFO] ActiveMQ Artemis Prometheus Metrics Plugin Servlet . SUCCESS [  7.964 s]
[INFO] ActiveMQ Artemis Prometheus Metrics Plugin ......... SUCCESS [ 34.596 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  43.030 s
[INFO] Finished at: 2020-04-10T13:36:27+02:00
[INFO] ------------------------------------------------------------------------
```

* New artifact is copied to artemis broker. Artefact artemis-prometheus-metrics-plugin/target/artemis-prometheus-metrics-plugin-VERSION.jar is copied to our broker:  

```bash
[activemq@my_servername artemis-prometheus-metrics-plugin]$ cp artemis-prometheus-metrics-plugin/target/artemis-prometheus-metrics-plugin-
1.0.0.CR1.jar /var/lib/artemisbroker/lib/
```

* Edition of file /var/lib/artemisbroker/etc/broker.xml

```
<metrics-plugin class-name="org.apache.activemq.artemis.core.server.metrics.plugins.ArtemisPrometheusMetricsPlugin"/>
``` 

* Creation of <artemis_instance>/web

```
[activemq@my_servername artemisbroker]$ mkdir /var/lib/artemisbroker/web
```

* Artifact artemis-prometheus-metrics-plugin-servlet/target/metrics.war is copied to <ARTEMIS_INSTANCE>/web :

```bash
[activemq@my_servername artemis-prometheus-metrics-plugin]$ cp artemis-prometheus-metrics-plugin-servlet/target/metrics.war /var/lib/artem
isbroker/web/
```

* Below web component added to <ARTEMIS_INSTANCE>/etc/bootstrap.xml :

```
[activemq@my_servername artemis-prometheus-metrics-plugin]$ vim /var/lib/artemisbroker/etc/bootstrap.xml
...
<app url="metrics" war="metrics.war"/>
...

```

* Restart of Artemis Broker
* Prometheus configuration, scrape_configs in /opt/prometheus/prometheus.yml :

```
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']
  - job_name: 'broker'
    static_configs:
    - targets: ['localhost:8161']
```

* Last step: Apparently there's not Grafana Dashboard available for this use case. It is required to [develop a new Grafana Dashboard](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana).

### Validation of Artemis Broker Monitoring with JMeter
* In order to validate our Artemis Broker Monitoring solution we need to "inject traffic/data/metrics" with for example Pub/Sub messages. 
* We can achieve this with a little of java code or by sending messages via Artemis Web Console -> **"Operations"** tab. 
* Another option is running the jmeter test plans available on [Artemis' github repo](https://github.com/apache/activemq-artemis/tree/master/examples/perf/jmeter). The procedure is described below. Remember to create the queues and addresses (topics) defined in jmeter example test plans.

#### JMeter Example Test Plans 
* Latest release of [Apache JMeter](https://jmeter.apache.org/) deployed in /opt
* Library artemis-jms-client-all-2.11.0.jar is copied to $JMETER_HOME/lib :

```bash
$ cp /opt/artemis/lib/client/artemis-jms-client-all-2.11.0.jar /opt/apache-jmeter-5.2.1/lib/
```

* jndi.properties file is modified with Artemis' IP address (it is not listening on localhost):

```
$ vim /opt/artemis/examples/perf/jmeter/jndi.properties
$ cat /opt/artemis/examples/perf/jmeter/jndi.properties
connectionFactory.ConnectionFactory=tcp://192.168.1.38:61616
```

* jndi.properties is packaged in a jar file and moved to $JMETER_HOME/lib :

```
[activemq@my_servername ~]$ cd /opt/artemis/examples/perf/jmeter/
[activemq@my_servername jmeter]$ ls -l
total 28
-rw-rw-r-- 1 activemq activemq 11887 Jan 10 16:22 1.jms_p2p_test.jmx
-rw-rw-r-- 1 activemq activemq  8442 Jan 10 16:22 2.pub_sub_test.jmx
-rw-rw-r-- 1 activemq activemq   833 Jan 10 16:22 jndi.properties
[activemq@my_servername jmeter]$ jar -cf artemis-jndi.jar jndi.properties
[activemq@my_servername jmeter]$ ls -l
total 32
-rw-rw-r-- 1 activemq activemq 11887 Jan 10 16:22 1.jms_p2p_test.jmx
-rw-rw-r-- 1 activemq activemq  8442 Jan 10 16:22 2.pub_sub_test.jmx
-rw-rw-r-- 1 activemq activemq   946 May 15 08:46 artemis-jndi.jar
-rw-rw-r-- 1 activemq activemq   833 Jan 10 16:22 jndi.properties
[activemq@my_servername jmeter]$ cp artemis-jndi.jar /opt/apache-jmeter-5.2.1/lib/
```

* Example Test Plans available at Artemis GitHub Repo are run by JMeter (from within the GUI or the CLI):

```
[activemq@my_servername ~]$ cd /opt/artemis/examples/perf/jmeter/
[activemq@my_servername jmeter]$ ls -la
total 32
drwxrwxr-x 2 activemq activemq   101 May 15 08:46 .
drwxrwxr-x 3 activemq activemq    19 Jan 10 16:22 ..
-rw-rw-r-- 1 activemq activemq 11887 Jan 10 16:22 1.jms_p2p_test.jmx
-rw-rw-r-- 1 activemq activemq  8442 Jan 10 16:22 2.pub_sub_test.jmx
-rw-rw-r-- 1 activemq activemq   946 May 15 08:46 artemis-jndi.jar
-rw-rw-r-- 1 activemq activemq   833 Jan 10 16:22 jndi.properties
[activemq@my_servername jmeter]$
[activemq@my_servername bin]$ cd
[activemq@my_servername ~]$ pwd
/home/activemq
[activemq@my_servername ~]$ /opt/apache-jmeter-5.2.1/bin/jmeter.sh -n -t /opt/artemis/examples/perf/jmeter/1.jms_p2p_test.jmx -l results-file-1.txt -j 1.log
[activemq@my_servername ~]$ /opt/apache-jmeter-5.2.1/bin/jmeter.sh -n -t /opt/artemis/examples/perf/jmeter/2.pub_sub_test.jmx -l results-file-2.txt -j 2.log

```

* We can now see metrics displayed on Grafana and Artemis Dashboard:

JMeter|Artemis Grafana|Artemis Dashboard
:-------:|:---------:|:-------:
![jmeter artemis](images/jmeter_artemis.png)|![artemis grafana](images/artemis_grafana.png)|![artemis dashboard monitoring](images/artemis_dashboard_mon.png)

## Kibana
* [Kibana](https://www.elastic.co/kibana)
    * [Kibana Docs](https://www.elastic.co/guide/index.html)
* [dzone: Kibana Tutorial: Part 1 - Getting Started](https://dzone.com/articles/kibana-tutorial-getting-started-part-1)
    * [dzone: Kibana Tutorial: Part 2 - Creating Visualizations](https://logz.io/blog/kibana-tutorial-2/)
* [dzone: Getting Started With Kibana Advanced Searches](https://dzone.com/articles/getting-started-with-kibana-advanced-searches)
* [dzone: Kibana Hacks: 5 Tips and Tricks](https://dzone.com/articles/kibana-hacks-5-tips-and-tricks)

## Prometheus and Grafana Interactive Learning
* [katacoda.com: Getting Started with Prometheus](https://www.katacoda.com/courses/prometheus/getting-started)
* [katacoda.com: Creating Dashboards with Grafana](https://www.katacoda.com/courses/prometheus/creating-dashboards-with-grafana)

## Performance
* [dzone.com: The Keys to Performance Tuning and Testing](https://dzone.com/articles/the-keys-to-performance-tuning-and-testing)
* [dzone.com: How Performance Tuning and Testing are Changing](https://dzone.com/articles/how-performance-tuning-and-testing-are-changing)
* [Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) Almost all applications that perform anything useful for a given business need to be integrated with one or more applications. With microservices-based architecture, where a number of services are broken down based on the services or functionality offered, the number of integration points or touch points increases massively.

## List of Performance Analysis Tools
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

### Thread Dumps. Debugging Java Applications
- [How to read a Thread Dump](https://dzone.com/articles/how-to-read-a-thread-dump)
- [Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) **A must read!**
- [Dzone: how to take thread dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)
- Thread Dump Analyzers: [fastThread](https://fastthread.io/), [Spotify TDA](https://spotify.github.io/threaddump-analyzer/), [IBM Thread and Monitor Dump Analyzer for Java](https://www.ibm.com/support/pages/ibm-thread-and-monitor-dump-analyzer-java-tmda), [TDA - Thread Dump Analyzer](https://github.com/irockel/tda)
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
- [**zipkin.io**](https://zipkin.io/)
- [**OpenTracing.io**](https://opentracing.io/)
     - [lightstep.com: Understand Distributed Tracing](https://docs.lightstep.com/docs/understand-distributed-tracing)

### Microservice Observability with Distributed Tracing. OpenTelemetry.io
- Used for monitoring and troubleshooting microservices-based distributed systems.
- [OpenTelemetry.io](https://opentelemetry.io/): 
    - **Unified standard** (open, vendor-neutral API), **merge of [OpenCensus.io](https://opencensus.io/) and [OpenTracing.io](https://opentracing.io/)**. 
    - “A single set of system components and language-specific telemetry libraries” to standardize how the industry uses metrics, traces, and eventually logs to enable observability. 
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

<center>
[![Jaeger UI](images/jaeger_ui.png)](https://www.jaegertracing.io/)

[![Zipking UI](images/zipkin_ui.png)](https://zipkin.io/)
</center>
<br/>

### Jaeger VS OpenTelemetry. How Jaeger works with OpenTelemetry
- [medium: Jaeger VS OpenTracing VS OpenTelemetry](https://medium.com/jaegertracing/jaeger-and-opentelemetry-1846f701d9f2)
- [medium: Using Jaeger and OpenTelemetry SDKs in a mixed environment with W3C Trace-Context](https://medium.com/jaegertracing/jaeger-clients-and-w3c-trace-context-c2ce1b9dc390)

![Jaeger Vs OpenTelemetry](images/jaeger_vs_opentelemetry.png)

## Application Performance Management (APM)
- [APM in wikipedia](https://en.wikipedia.org/wiki/Application_performance_management): The monitoring and management of performance and availability of software applications. APM strives to detect and diagnose complex application performance problems to maintain an expected level of service. APM is "the translation of IT metrics into business meaning.” 
- Tip: [Download APM report from IT Central Station](https://www.itcentralstation.com/categories/application-performance-management-apm)
* [Awesome APM 🌟](https://github.com/antonarhipov/awesome-apm)
* [dzone.com: APM Tools Comparison](https://dzone.com/articles/apm-tools-comparison-which-one-should-you-choose)
* [dzone.com: Java Performance Monitoring: 5 Open Source Tools You Should Know](https://dzone.com/articles/java-performance-monitoring-5-open-source-tools-you-should-know)
* [dzone.com: 14 best performance testing tools and APM solutions](https://dzone.com/articles/14-best-performance-testing-tools-and-apm-solution)
* Exception Tracking:
    * [sentry.io](https://sentry.io/)
    * APMs like Dynatrace, etc.
* APM Tools:
    * [datadoghq.com](https://www.datadoghq.com/)
    * [honeycomb.io](https://www.honeycomb.io)
    * [lightstep.com](https://lightstep.com)
    * [skywalking.apache.org](https://skywalking.apache.org/)   
    * [AppDynamics 🌟](https://www.appdynamics.com/)
    * [New Relic 🌟](https://newrelic.com/)
    * [Dynatrace 🌟](https://www.dynatrace.com/)

### Elastic APM
- [Elastic APM](https://www.elastic.co/products/apm)
- [Elastic APM Server](https://www.elastic.co/guide/en/apm/get-started/current/components.html): 
- [Mininimum elasticsearch requirement is 6.2.x or higher](https://www.elastic.co/support/matrix#matrix_compatibility)
- Built-in elasticsearch 5.6 in Openshift 3 & Openshift 4 cannot be integrated with Elastic APM Server.
- Solutions: Deploy a higher version of [Elasticsearch + Kibana](https://hub.docker.com/_/elasticsearch) on a new Project dedicated to Elastic APM; or setup an Elastic Cloud account.
- [Elastic APM Server Docker image](https://github.com/sls-dev1/openshift-elastic-apm-server) (“oss” & openshift compliant). 
- [elastic.co: Using the Elastic APM Java Agent on Kubernetes](https://www.elastic.co/blog/using-elastic-apm-java-agent-on-kubernetes-k8s)

![Elastic APM](images/elasticapm.png)

### Dynatrace APM
* [adictosaltrabajo.com: Monitorización y análisis de rendimiento de aplicaciones con Dynatrace APM](https://www.adictosaltrabajo.com/tutoriales/monitorizacion-y-analisis-de-rendimiento-de-aplicaciones-con-dynatrace/)
* [dynatrace.com: openshift monitoring](https://www.dynatrace.com/technologies/openshift-monitoring/)
* [dynatrace.com: Dynatrace monitoring for Kubernetes and OpenShift](https://www.dynatrace.com/news/blog/dynatrace-monitoring-for-kubernetes-and-openshift/)
* [dynatrace.com: Deploy OneAgent on OpenShift Container Platform](https://www.dynatrace.com/support/help/cloud-platforms/openshift/full-stack/deploy-oneagent-on-openshift-container-platform/)
* [Successful Kubernetes Monitoring – Three Pitfalls to Avoid](https://www.dynatrace.com/news/blog/successful-kubernetes-monitoring-3-pitfalls-to-avoid/)
* [My Dynatrace proof of concept 🌟](https://github.com/redhatspain/awesome-kubernetes/blob/master/pdf/dynatrace_demo.pdf)
* [Tutorial: Guide to automated SRE-driven performance engineering 🌟](https://www.dynatrace.com/news/blog/guide-to-automated-sre-driven-performance-engineering-analysis/)

## Message Queue Monitoring

Messaging Solution|Monitoring Solution|URL
:-------|:-------|:-----
ActiveMQ 5.8.0+|[Dynatrace](https://www.dynatrace.com)|[ref](https://www.dynatrace.com/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/activemq/)
ActiveMQ Artemis|[Micrometer Collector](https://micrometer.io/) + Prometheus|[ref1](http://activemq.apache.org/components/artemis/documentation/latest/metrics.html), [ref2](https://micrometer.io/docs/registry/prometheus)
IBM MQ|[IBM MQ](https://github.com/ibm-messaging) Exporter for Prometheus|[ref](https://github.com/ibm-messaging/mq-metric-samples/tree/master/cmd/mq_prometheus)
Kakfa|[Dynatrace](https://www.dynatrace.com)|[ref1](https://www.dynatrace.com/support/help/technology-support/application-software/other-technologies/supported-out-of-the-box/kafka/), [ref2](https://www.dynatrace.com/news/blog/introducing-kafka-process-monitoring-beta/), [ref3](https://answers.dynatrace.com/spaces/482/dynatrace-open-qa/questions/232421/dynatrace-distributed-tracing-with-kafka.html)
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

## Other Awesome Lists
- [Awesome APM](https://github.com/antonarhipov/awesome-apm)

<center>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/J1S3NyN9ZeLjh9" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/challenges-in-a-microservices-age-monitoring-logging-and-tracing-on-red-hat-openshift" title="Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift" target="_blank">Challenges in a Microservices Age: Monitoring, Logging and Tracing on Red Hat OpenShift</a> </strong> from <strong><a href="https://www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/lr07J585Y86D7i" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MartinEtmajer/monitoring-microservices-at-scale-on-openshift-67500621" title="Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)" target="_blank">Monitoring Microservices at Scale on OpenShift (OpenShift Commons Briefing #52)</a> </strong> from <strong><a href="//www.slideshare.net/MartinEtmajer" target="_blank">Martin Etmajer</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/CDyLLoStp2omzE" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/PurnimaKurella/dynatrace-70789377" title="Dynatrace" target="_blank">Dynatrace</a> </strong> from <strong><a href="https://www.slideshare.net/PurnimaKurella" target="_blank">Purnima Kurella</a></strong> </div>
</center>
