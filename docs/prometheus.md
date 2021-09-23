# Prometheus
- [Introduction](#introduction)
- [Promgen](#promgen)
- [Promcat Resource Catalog](#promcat-resource-catalog)
- [Prometheus Demo](#prometheus-demo)
- [Prometheus Storage](#prometheus-storage)
- [Prometheus SLO Service Level Objectives](#prometheus-slo-service-level-objectives)
    - [Scalability, High Availability (HA) and Long-Term Storage](#scalability-high-availability-ha-and-long-term-storage)
    - [Storage Solutions for Prometheus](#storage-solutions-for-prometheus)
        - [InfluxDB and InfluxDB Templates](#influxdb-and-influxdb-templates)
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
- [Proof of Concept: ActiveMQ Monitoring with Prometheus](#proof-of-concept-activemq-monitoring-with-prometheus)
    - [PoC: ActiveMQ 5.x Monitoring with Telegraf Collector, Prometheus and Grafana Dashboard 10702](#poc-activemq-5x-monitoring-with-telegraf-collector-prometheus-and-grafana-dashboard-10702)
        - [Deployment and Configuration](#deployment-and-configuration)
    - [PoC: ActiveMQ Artemis Monitoring with Prometheus Metrics Plugin (Micrometer Collector) and Prometheus. Grafana Dashboard not available](#poc-activemq-artemis-monitoring-with-prometheus-metrics-plugin-micrometer-collector-and-prometheus-grafana-dashboard-not-available)
        - [Deployment and Configuration](#deployment-and-configuration-1)
    - [Validation of Artemis Broker Monitoring with JMeter](#validation-of-artemis-broker-monitoring-with-jmeter)
        - [JMeter Example Test Plans](#jmeter-example-test-plans)
- [Videos](#videos)

## Introduction
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
* [Cloud Native Monitoring with Prometheus 🌟](https://samirbehara.com/2019/05/30/cloud-native-monitoring-with-prometheus/)
* [itnext.io - Prometheus: yet-another-cloudwatch-exporter — collecting AWS CloudWatch metrics](https://itnext.io/prometheus-yet-another-cloudwatch-exporter-collecting-aws-cloudwatch-metrics-806bd34818a8)
* [medium: Kubernetes Lessons in Alerting](https://medium.com/better-programming/kubernetes-lessons-in-alerting-a0b7a455e89d) Live issues are a great opportunity to learn and improve. Here’s what happened to us
* [Prometheus Monitoring Ecosystem Begins to Mature](https://containerjournal-com.cdn.ampproject.org/c/s/containerjournal.com/topics/container-ecosystems/prometheus-monitoring-ecosystem-begins-to-mature/amp/)
* [learnsteps.com: Monitoring Infrastructure System Design](https://www.learnsteps.com/monitoring-infrastructure-system-design/)
* [ganeshvernekar.com: Prometheus TSDB (Part 1): The Head Block](https://ganeshvernekar.com/blog/prometheus-tsdb-the-head-block/)
* [ganeshvernekar.com: Prometheus TSDB (Part 2): WAL and Checkpoint](https://ganeshvernekar.com/blog/prometheus-tsdb-wal-and-checkpoint/)
* [ganeshvernekar.com: Prometheus TSDB (Part 3): Memory Mapping of Head Chunks from Disk](https://ganeshvernekar.com/blog/prometheus-tsdb-mmapping-head-chunks-from-disk/)
* [ganeshvernekar.com: Prometheus TSDB (Part 4): Persistent Block and its Index](https://ganeshvernekar.com/blog/prometheus-tsdb-persistent-block-and-its-index/)
* [youtube playlist: How to setup Prometheus 🌟](https://www.youtube.com/playlist?list=PLVx1qovxj-anCTn6um3BDsoHnIr0O2tz3)
* [learndevops.substack.com: Hitting prometheus API with curl and jq 🌟](https://learndevops.substack.com/p/hitting-prometheus-api-with-curl) **Determine offending pods that use more RAM than requested, causing OOM.**
* [devclass.com: Safety…first? Prometheus 2.24 finally features TLS on HTTP serving endpoints](https://devclass.com/2021/01/07/prometheus-2_24/)
* [sysadminxpert.com: Steps to Monitor Linux Server using Prometheus](https://sysadminxpert.com/steps-to-monitor-linux-server-using-prometheus/)
* [medium.com: Prometheus-Grafana : Node Monitoring on Kubernetes](https://medium.com/@akshitverma8191/prometheus-grafana-node-monitoring-on-kubernetes-79fd8311b56d)
* [zerodha.tech: Infrastructure monitoring with Prometheus at Zerodha](https://zerodha.tech/blog/infra-monitoring-at-zerodha/)
* [devopscube.com: How to Setup Prometheus Monitoring On Kubernetes Cluster 🌟](https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/)
* [prometheus-operator.dev 🌟](https://prometheus-operator.dev) 
* [gabrieltanner.org: Golang Application monitoring using Prometheus](https://gabrieltanner.org/blog/collecting-prometheus-metrics-in-golang)
* [promlens.com 🌟](https://promlens.com/) The power tool for querying Prometheus. Build, understand, and fix your queries much more effectively with the ultimate query builder for PromQL
* [timber.io: PromQL For Humans 🌟](https://timber.io/blog/promql-for-humans)
* [medium: Prometheus monitoring with Elastic Stack in Kubernetes 🌟](https://medium.com/avmconsulting-blog/prometheus-monitoring-with-elastic-stack-in-kubernetes-5cf0aaa7ce04) Monitoring is one of the key components for managing large clusters. For this, we have several tools.
* [grafana.com: How we use metamonitoring Prometheus servers to monitor all other Prometheus servers at Grafana Labs](https://grafana.com/blog/2021/04/08/how-we-use-metamonitoring-prometheus-servers-to-monitor-all-other-prometheus-servers-at-grafana-labs/) If you rely on Prometheus for your monitoring, and your monitoring fails, how will you know? Learn how to set up Prometheus servers to monitor all other Prometheus servers
* [portworx.com: Monitoring Kubernetes Backup with Prometheus and Grafana](https://portworx.com/kubernetes-backup-monitoring/)
* [sysdig.com: Top 10 metrics in PostgreSQL monitoring with Prometheus 🌟](https://sysdig.com/blog/postgresql-monitoring/)
* [itnext.io: Observability at Scale](https://itnext.io/observability-at-scale-52d0d9a5fb9b)
* [jonbc.medium.com: Hacking your way to Observability — Part 1 : Metrics](https://jonbc.medium.com/hacking-your-way-to-observability-part-1-cf4cd42fb4dc) Starting your journey in observability by gathering metrics with Prometheus
* [innoq.com: Scraping a Docker swarm service with Prometheus](https://www.innoq.com/en/blog/scraping-docker-swarm-service-instances-with-prometheus/)
* [opensource.com: Run Prometheus at home in a container](https://opensource.com/article/21/7/run-prometheus-home-container)
* [faun.pub: Production grade Kubernetes Monitoring using Prometheus 🌟](https://faun.pub/production-grade-kubernetes-monitoring-using-prometheus-78144b835b60)
* [howtoforge.com: How to Install Prometheus System Monitoring Tool on Ubuntu 20.04](https://www.howtoforge.com/how-to-install-prometheus-on-ubuntu-20-04/)
* [cribl.io: Using Prometheus for Agentless Monitoring](https://cribl.io/blog/using-prometheus-for-agentless-monitoring/)
* [logz.io:  Guide to Monitoring AWS Lambda Metrics with Prometheus & Logz.io 🌟](https://logz.io/blog/aws-lambda-metrics-monitoring-guide/)
* [aprenderbigdata.com: Prometheus: Introducción a la Monitorización de Métricas](https://aprenderbigdata.com/prometheus/)
* [tech.marksblogg.com: Monitor ClickHouse column oriented database with Prometheus & Grafana](https://tech.marksblogg.com/clickhouse-prometheus-grafana.html)
* [karma 🌟](https://github.com/prymitive/karma) Alert dashboard for Prometheus Alertmanager
* [Alertmanager 0.23.0-rc.0 with awscloud SNS support is available for testing. There are also bugfixes and features for amtool](https://github.com/prometheus/alertmanager/releases/tag/v0.23.0-rc.0)
* [youtube: Monitoring your k6 load test: how to install Grafana and Prometheus on a Kubernetes cluster](https://www.youtube.com/watch?v=GL2v81xYuAQ&ab_channel=k6)
* [blog.couchbase.com: How to Build Observability Dashboards with Prometheus, Grafana & Couchbase](https://blog.couchbase.com/how-to-build-observability-dashboards-prometheus-grafana-couchbase/)

[![prometheus architecture](images/prometheus-architecture.png)](https://github.com/prometheus/prometheus)

## Promgen
- [Promgen 🌟](https://github.com/line/promgen) Promgen is a configuration file generator for Prometheus

## Promcat Resource Catalog
- [Promcat: A resource catalog for enterprise-class Prometheus monitoring 🌟](https://promcat.io/)

## Prometheus Demo
- [Prometheus Demo: prometheus.demo.do.prometheus.io 🌟](https://prometheus.demo.do.prometheus.io)

## Prometheus Storage
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

## Prometheus SLO Service Level Objectives
- [Sloth 🌟](https://github.com/slok/sloth) Easy and simple Prometheus SLO (service level objectives) generator
    - [itnext.io: SLOs should be easy, say hi to Sloth 🌟](https://itnext.io/slos-should-be-easy-say-hi-to-sloth-9c8a225df0d4)
- [PromTools: SLOs with Prometheus 🌟](https://promtools.dev/) Multiple Burn Rate Alerts. This page will generate, with the data you provide in the form, the necessary Prometheus alerting and recording rules for Multiple Burn Rate which you might know from The Site Reliability Workbook. These rules will evaluate based on the available metrics in the last 30 days. 
    - [slo-libsonnet](https://github.com/metalmatze/slo-libsonnet) Generate Prometheus alerting & recording rules and Grafana dashboards for your SLOs.
- [opensource.google: Prometheus SLO example](https://opensource.google/projects/prometheus-slo-burn-example) An end to end example of implementing SLOs with Prometheus, Grafana and Go
- [SLO Generator](https://github.com/google/slo-generator) SLO Generator is a tool to compute SLIs, SLOs, Error Budgets and Burn rate and export an SLO report to supported exporters.

### Scalability, High Availability (HA) and Long-Term Storage
* Prometheus fue diseñado para ser fácil de desplegar. Es extremadamente fácil ponerlo en marcha, recoger algunas métricas, y empezar a construir nuestra propia herramienta de monitorización. Las cosas se complican cuando se intenta operar a un nivel de escalado considerable.
* Para entender si esto va a ser un problema, conviene plantearse las siguiente preguntas:
    -	¿Cuántas métricas puede ingerir el sistema de monitorización y cuántas son necesarias?
    -	¿Cuál es la cardinalidad de las métricas? La cardinalidad es el número de etiquetas que cada métrica puede tener. Es una cuestión muy frecuente en las métricas pertenecientes a entornos dinámicos donde a los contenedores se les asignan un ID ó nombre diferente cada vez que son lanzados, reiniciados o movidos entre nodos (caso de kubernetes).
    -	¿Es necesaria la Alta Disponibilidad (HA)?
    -	¿Durante cuánto tiempo es necesario mantener las métricas y con qué resolución? 
* La implementación de HA es laboriosa porque la funcionalidad de cluster requiere añadir plugins de terceros al servidor Prometheus. Es necesario tratar con "backups" y "restores", y el almacenamiento de métricas por un periodo de tiempo extendido hará que la base de datos crezca exponencialmente. Los servidores Prometheus proporcionan almacenamiento persistente, pero Prometheus no fue creado para el almacenamiento distribuido de métricas a lo largo de múltiples nodos de un cluster con replicación y capacidad curativa (como es el caso de Kubernetes).  Esto es conocido como **"almacenamiento a largo-plazo" (Long-Term)** y actualmente es un requisito en unos pocos casos de uso, por ejemplo en la planificación de la capacidad para monitorizar cómo la infraestructura necesita evolucionar, contracargos para facturar diferentes equipos ó departamentos para un caso específico que han hecho de la infraestructura, análisis de tendencias de uso, o adherirse a regulaciones para verticales específicos como banca, seguros, etc. 

### Storage Solutions for Prometheus
* [monitoring2.substack.com: Big Prometheus. Thanos, Cortex, M3DB and VictoriaMetrics at scale 🌟](https://monitoring2.substack.com/p/big-prometheus)
* [**Prometheus TSDB**](https://prometheus.io/docs/prometheus/latest/storage/)
* [**Cortex**:](https://cortexmetrics.io/) Provides horizontally scalable, highly available, multi-tenant, long term storage for Prometheus. Cortex allows for storing time series data in a key-value store like Cassandra, AWS DynamoDB, or Google BigTable. It offers a Prometheus compatible query API, and you can push metrics into a write endpoint. This makes it best suited for cloud environments and multi-tenant scenarios like service providers building hosted and managed platforms.
    * [github.com/cortexproject/cortex](https://github.com/cortexproject/cortex)
    * [Weave Cortex SaaS (Hosted Prometheus - Public Cloud)](https://www.weave.works/features/prometheus-monitoring/)
* [**Thanos**:](https://thanos.io/) Open source, **highly available Prometheus setup with long term storage capabilities**. 
    * Thanos stores time series data in an object store like AWS S3, Google Cloud Storage, etc. Thanos pushes metrics through a side-car container from each Prometheus server through the gRPC store API to the query service in order to provide a global query view.
    * [github.com/ruanbekker: Thanos Cluster Setup](https://github.com/ruanbekker/thanos-cluster-setup) How to deploy a HA Prometheus setup with Unlimited Data Retention Capabilities on aws cloud S3 with Thanos Metrics.
    * [Highly Available Prometheus Metrics for Distributed SQL with Thanos on GKE](https://blog.yugabyte.com/highly-available-prometheus-metrics-for-distributed-sql-with-thanos-on-gke/)
    * [infracloud.io: Achieving multi-tenancy in monitoring with Prometheus & the mighty Thanos Receiver](https://www.infracloud.io/blogs/multi-tenancy-monitoring-thanos-receiver/)
    * [particule.io: Multi-Cluster Monitoring with Thanos](https://particule.io/en/blog/thanos-monitoring)
    * [prometheus-operator.dev: Thanos and the Prometheus Operator 🌟](https://prometheus-operator.dev/docs/operator/thanos/)
    * [Thanos Architecture Overview 🌟](https://github.com/thanos-io/thanos#architecture-overview)
    * [enmilocalfunciona.io: Aprende a configurar Thanos usando docker-compose](https://enmilocalfunciona.io/aprende-a-configurar-thanos-usando-docker-compose/)
* [**M3**:](https://www.m3db.io/) An open source, large-scale metrics platform developed by Uber. It has its own time series database, M3DB. Like Thanos, M3 also uses a side-car container to push the metrics to the DB. In addition, it supports metric deduplication and merging, and provides distributed query support.
Although it's exciting to see attempts to address the challenges of running Prometheus at scale, these are very young projects that are not widely used yet.
* [VictoriaMetrics](https://victoriametrics.com/)

#### InfluxDB and InfluxDB Templates
* [**InfluxDB**:](https://www.influxdata.com/) An [open-source time series database (TSDB)](https://en.wikipedia.org/wiki/Time_series_database) developed by InfluxData. It is written in [Go](https://en.wikipedia.org/wiki/Go_(programming_language)) and optimized for fast, high-availability storage and retrieval of [time series](https://en.wikipedia.org/wiki/Time_series) data in fields such as operations monitoring, application metrics, [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things) sensor data, and real-time analytics. It also has support for processing data from [Graphite](https://en.wikipedia.org/wiki/Graphite_(software)).
* [en.wikipedia.org/wiki/InfluxDB](https://en.wikipedia.org/wiki/MIT_License)
* [influxdata.com: Building a Metrics & Alerts as a Service (MaaS) Monitoring Solution Using the InfluxDB Stack](https://www.influxdata.com/blog/building-a-metrics-alerts-as-a-service-maas-monitoring-solution-using-the-influxdb-stack/)
* [en.wikipedia.org/wiki/MIT_License](https://en.wikipedia.org/wiki/MIT_License)
* [dzone: Flux queries](https://dzone.com/articles/flux-windowing-and-aggregation) New language being developed at InfluxData.
* [influxdb-templates](https://www.influxdata.com/products/influxdb-templates/) Build and share InfluxDB templates for monitoring solutions that deliver faster time to awesome.
    * [thenewstack.io: Make a GitOps Workflow Using InfluxDB Templates](https://thenewstack.io/make-a-gitops-workflow-using-influxdb-templates/)
* [influxdata.com: Running InfluxDB 2.0 and Telegraf Using Docker](https://www.influxdata.com/blog/running-influxdb-2-0-and-telegraf-using-docker/)

## Collectors. Software exposing Prometheus metrics
- http://localhost:9090/targets : you should see a list of targets that you Prometheus server is scraping. 

### Prometheus Exporters. Plug-in architecture and extensibility with Prometheus Exporters (collectors)
* Prometheus proporciona un ecosistema de **"exporters"**, los cuales permiten que herramientas de terceros puedan exportar sus datos en Prometheus. Muchos componentes de software de código abierto son compatibles por defecto. 
* [exporterhub.io 🌟](https://exporterhub.io/) Exporterhub is a curated List of Prometheus Exporters
* **Un "exporter" expone las métricas de uno ó varios "collectors".**
* [Prometheus Exporters](https://prometheus.io/docs/instrumenting/exporters/) 
    * [prometheus.io/download/](https://prometheus.io/download/)
    * [github.com/prometheus](https://github.com/prometheus)
* [Prometheus JMX Exporter 🌟](https://github.com/prometheus/jmx_exporter) A process for exposing JMX Beans via HTTP for Prometheus consumption.
* [blackbox_exporter 🌟](https://github.com/prometheus/blackbox_exporter) The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
* [Example: How to Use Prometheus Monitoring With Java to Gather Data. Gathering Java Metrics with Prometheus Monitoring (ActiveMQ)](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)
* [Maven Prometheus instrumentation library for JVM applications (client library)](https://mvnrepository.com/artifact/io.prometheus)
    * [github.com/prometheus/client_java](https://github.com/prometheus/client_java)
* [Example: JMX Exporter with ActiveMQ](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)
* [k8s-image-availability-exporter](https://github.com/flant/k8s-image-availability-exporter) is a Prometheus exporter that warns you proactively about images that are defined in Kubernetes objects (e.g., an image field in the Deployment) but are not available in the container registry (such as Docker Registry, etc.).
* [engineeringblog.yelp.com: Improving the performance of the Prometheus JMX Exporter](https://engineeringblog.yelp.com/2020/10/improving-the-performance-of-the-prometheus-jmx-exporter.html)
* [sysdig.com: How to monitor an Oracle database with Prometheus. The OracleDB Prometheus exporter](https://sysdig.com/blog/monitor-oracle-database-prometheus/)
* [YACE - yet another cloudwatch exporter 🌟](https://github.com/ivx/yet-another-cloudwatch-exporter) AWS cloudwatch to prometheus exporter - Discovers services through AWS tags, gets cloudwatch data and provides them as prometheus metrics with AWS tags as labels
* [prometheus-community/elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter) Prometheus exporter for various metrics about ElasticSearch, written in Go.

### Prometheus Exporters Development. Node Exporter
* Node exporter puede ser utilizado para exportar las métricas de nuestra aplicación ya que permite exportar un "text-file". Nuestra aplicación puede escribir datos en un fichero de texto con el formato de datos de Prometheus. Este fichero de texto con datos agregados sería exportado a Prometheus con Node Exporter. 
* [dzone.com: Monitoring Self-Destructing Apps Using Prometheus](https://dzone.com/articles/prometheus-collectors) Learn how to configure Prometheus collectors and their use cases.
* [prometheus.io: Writing Exporters](https://prometheus.io/docs/instrumenting/writing_exporters/)
* [devconnected.com: Complete Node Exporter Mastery with Prometheus](https://devconnected.com/complete-node-exporter-mastery-with-prometheus)
* [scalyr.com: Prometheus metrics by example: 5 things you can learn](https://www.scalyr.com/blog/prometheus-metrics-by-example/)
* [aws.amazon.com: Building a Prometheus remote write exporter for the OpenTelemetry Go SDK](https://aws.amazon.com/blogs/opensource/building-a-prometheus-remote-write-exporter-for-the-opentelemetry-go-sdk/)

### Prometheus Third-party Collectors/Exporters
* Some third-party software exposes metrics in the Prometheus format, so no separate exporters are needed.
* [Prometheus Third Party Exporters](https://prometheus.io/docs/instrumenting/exporters/)
  
#### OpenTelemetry Collector
* [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)
* [thenewstack.io: Lightstep’s OpenTelemetry Launchers Simplify Integration to Line of Code](https://thenewstack.io/lightsteps-opentelemetry-launchers-simplify-integration-to-line-of-code/) 
* [OpenTelemetry Launchers 🌟](https://github.com/search?q=org%3Alightstep+launcher)
* [thenewstack.io: Demystifying Distributed Traces in OpenTelemetry](https://thenewstack.io/demystifying-distributed-traces-in-opentelemetry/)
* [medium: OpenTelemetry Specification v1.0.0, Tracing Edition](https://medium.com/opentelemetry/opentelemetry-specification-v1-0-0-tracing-edition-72dd08936978)
* [cncf.io: From distributed tracing to APM: Taking OpenTelemetry and Jaeger up a level](https://www.cncf.io/blog/2021/04/29/from-distributed-tracing-to-apm-taking-opentelemetry-and-jaeger-up-a-level/?utm_source=thenewstack&utm_medium=twitter&utm_campaign=platform)
* [medium: Tracing in eDreams ODIGEO Lodging with Open Telemetry and Grafana Tempo](https://medium.com/edreams-odigeo-tech/tracing-in-edreams-odigeo-lodging-with-open-telemetry-and-grafana-tempo-bd1f20ddf49d)
* [newrelic.com: Understand OpenTelemetry Part 4: Instrument a Java App with OpenTelemetry](https://newrelic.com/blog/best-practices/java-opentelemetry)
* https://github.com/jenkinsci/opentelemetry-plugin Publish Jenkins performances metrics to an OpenTelemetry endpoint, including distributed traces of job executions and health metrics of the controller.
* https://github.com/cyrille-leclerc/opentelemetry-maven-extension Maven extension to observe Maven builds as distributed traces using OpenTelemetry
* https://github.com/equinix-labs/otel-cli OpenTelemetry command-line tool for sending events from shell scripts & similar environments
* https://github.com/ansible-collections/community.general/pull/3091 Send distributed traces for the ansible runs with OpenTelemetry

#### Telegraf Collector
* [Telegraf Collector](https://www.influxdata.com/time-series-platform/telegraf/)
* [Telegraf Prometheus Output Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/prometheus_client)
* [Telegraf Ansible Role](https://github.com/rossmcdonald/telegraf)
* [Grafana Dashboards with Telegraf Collectors](https://grafana.com/grafana/dashboards?collector=Telegraf)
* [dzone: Synthetic Monitoring With Telegraf (white-box monitoring)](https://dzone.com/articles/synthetic-monitoring-with-telegraf) Monitoring based on metrics exposed by the internals of the system
* [grafana.com: Using Telegraf plugins to visualize industrial IoT data with the Grafana Cloud Hosted Prometheus service](https://grafana.com/blog/2021/04/05/using-telegraf-plugins-to-visualize-industrial-iot-data-with-the-grafana-cloud-hosted-prometheus-service/)
* [sysadminxpert.com: How to Monitor Linux System with Grafana and Telegraf](https://sysadminxpert.com/monitor-linux-system-with-grafana-and-telegraf/)
* [influxdata.com: Three Ways to Keep Cardinality Under Control When Using Telegraf](https://www.influxdata.com/blog/three-ways-to-keep-cardinality-under-control-when-using-telegraf/)

#### Micrometer Collector
* [**Micrometer** Collector](http://micrometer.io/)
* [Micrometer Prometheus](https://micrometer.io/docs/registry/prometheus)

## Prometheus Alarms and Event Tracking
* Prometheus no soporta rastreo de eventos (event tracking), pero ofrece un soporte completo de alarmas y gestión de alarmas. El lenguaje de consultas (queries) de Prometheus permite en cambio implementar rastreo de eventos por cuenta propia.

## Prometheus and Cloud Monitoring
* AWS CloudWatch is supported by Prometheus.

## Prometheus Installers
### Binaries, source code or Docker
* [prometheus.io: Installarion](https://prometheus.io/docs/prometheus/latest/installation/)
* [prometheus.io: Getting Started](https://prometheus.io/docs/prometheus/latest/getting_started/) 
* [github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)

### Ansible Roles
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

## Prometheus Operator 
### kube Prometheus
* [kube-prometheus](https://github.com/coreos/kube-prometheus) Use Prometheus to monitor Kubernetes and applications running on Kubernetes.

### Prometheus Operator with Helm3
* [devstack.in: Deploy Prometheus Operator with Helm3 and Private Registry 🌟](https://devstack.in/2020/05/25/deploy-prometheus-operator-with-helm3-and-private-registry/)

### Kubernetes Cluster Monitoring Stack based on Prometheus Operator
- [Cluster Monitoring stack for ARM / X86-64 platforms](https://github.com/carlosedp/cluster-monitoring) Updated the cluster-monitoring stack for kubernetes to latest versions. Fresh Grafana 7, Prometheus Operator and more. This repository collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.

## Prometheus SaaS Solutions
* [Weave Cortex SaaS (Hosted Prometheus - Public Cloud)](https://www.weave.works/features/prometheus-monitoring/)
* [logz.io](https://logz.io)
    * [logz.io: Logz.io’s Prometheus-as-a-Service is Generally Available 🌟](https://logz.io/blog/prometheus-as-a-service-launch/)
* [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)

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


## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="https://www.youtube.com/embed/r8UvWSX3KA8" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>