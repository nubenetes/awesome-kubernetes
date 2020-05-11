# OpenShift Monitoring and Performance. Prometheus, Grafana, APMs and more
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
    - [Collectors](#collectors)
        - [Prometheus Exporters. Plug-in architecture and extensibility with Prometheus Exporters (collectors)](#prometheus-exporters-plug-in-architecture-and-extensibility-with-prometheus-exporters-collectors)
        - [Prometheus Third Party Exporters](#prometheus-third-party-exporters)
        - [Prometheus Exporters Development. Node Exporter](#prometheus-exporters-development-node-exporter)
    - [Prometheus Alarms and Event Tracking](#prometheus-alarms-and-event-tracking)
    - [Prometheus and Cloud Monitoring](#prometheus-and-cloud-monitoring)
    - [Prometheus Installers](#prometheus-installers)
        - [Binaries, source code or Docker](#binaries-source-code-or-docker)
        - [Ansible Roles](#ansible-roles)
    - [Prometheus SaaS Solutions](#prometheus-saas-solutions)
- [Grafana](#grafana)
    - [Grafana Dashboards](#grafana-dashboards)
- [Kibana](#kibana)
- [Interactive Learning](#interactive-learning)
- [Performance](#performance)
- [Distributed Tracing. OpenTelemetry and Jaeger](#distributed-tracing-opentelemetry-and-jaeger)
- [Application Performance Management (APM)](#application-performance-management-apm)
    - [Dynatrace APM](#dynatrace-apm)
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
| :----------------------- | :-----------------: | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ElasticSearch            |          5          |                                                       [OpenShift 3.11 Metrics & Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging) |
| Fluentd                  |        0.12         |                                                       [OpenShift 3.11 Metrics & Logging](https://docs.openshift.com/container-platform/3.11/release_notes/ocp_3_11_release_notes.html#ocp-311-metrics-and-logging) |
| Kibana                   |       5.6.13        |                                                                                                                                      [kibana 5.6.13](https://www.elastic.co/guide/en/kibana/5.6/introduction.html) |
| Prometheus               |        2.3.2        |                                 [OpenShift 3.11 Prometheus Cluster Monitoring](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#prometheus-cluster-monitoring) |
| Prometheus Operator      |                     |                           [Prometheus Operator technical preview](https://www.redhat.com/en/blog/generally-available-today-red-hat-openshift-container-platform-311-ready-power-enterprise-kubernetes-deployments) |
| Prometheus Alert Manager |      0.15.1 1       | [OpenShift 3.11 Configuring Prometheus Alert Manager](https://docs.openshift.com/container-platform/3.11/install_config/prometheus_cluster_monitoring.html#configuring-alertmanager_prometheus-cluster-monitoring) |
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
| :----------------------- | :-----------------: | :------: | :-----: | :-----: | ------: |
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
* [https://github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)
* [Monitoring With Prometheus](https://dzone.com/articles/monitoring-with-prometheus)
* [Dzone Refcard: Scaling and Augmenting Prometheus](https://dzone.com/refcardz/scaling-and-augmenting-prometheus) Prometheus is an open-source infrastructure and services monitoring system popular for Kubernetes and cloud-native services and apps. It can help make metric collection easier, correlate events and alerts, provide security, and do troubleshooting and tracing at scale. This Refcard will teach you how to pave the path for Prometheus adoption, what observability looks like beyond Prometheus, and how Prometheus helps provide scalability, high availability, and long-term storage.
* [Monitoring Self-Destructing Apps Using Prometheus.](https://dzone.com/articles/prometheus-collectors) Learn how to configure Prometheus collectors and their use cases.
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
* [Synthetic Monitoring With Telegraf (white-box monitoring)](https://dzone.com/articles/synthetic-monitoring-with-telegraf) Monitoring based on metrics exposed by the internals of the system
*	[https://prometheus.io/docs/instrumenting/writing_exporters/](https://prometheus.io/docs/instrumenting/writing_exporters/)
*	[https://devconnected.com/complete-node-exporter-mastery-with-prometheus/](https://devconnected.com/complete-node-exporter-mastery-with-prometheus/)
*	[https://www.scalyr.com/blog/prometheus-metrics-by-example/](https://www.scalyr.com/blog/prometheus-metrics-by-example/)
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
* [**InfluxDB**:](https://www.influxdata.com/) An [open-source time series database (TSDB)](https://en.wikipedia.org/wiki/Time_series_database) developed by InfluxData. It is written in [Go](https://en.wikipedia.org/wiki/Go_(programming_language)) and optimized for fast, high-availability storage and retrieval of [time series](https://en.wikipedia.org/wiki/Time_series) data in fields such as operations monitoring, application metrics, [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things) sensor data, and real-time analytics. It also has support for processing data from [Graphite](https://en.wikipedia.org/wiki/Graphite_(software)).
    * [https://en.wikipedia.org/wiki/InfluxDB](https://en.wikipedia.org/wiki/MIT_License)
    * [https://en.wikipedia.org/wiki/MIT_License](https://en.wikipedia.org/wiki/MIT_License)
* [**M3**:](https://www.m3db.io/) An open source, large-scale metrics platform developed by Uber. It has its own time series database, M3DB. Like Thanos, M3 also uses a side-car container to push the metrics to the DB.
In addition, it supports metric deduplication and merging, and provides distributed query support.
Although it's exciting to see attempts to address the challenges of running Prometheus at scale, these are very young projects that are not widely used yet.

### Collectors
* [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector)
* [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)
* [Micrometer](http://micrometer.io/)

#### Prometheus Exporters. Plug-in architecture and extensibility with Prometheus Exporters (collectors)
* Prometheus proporciona un ecosistema de **"exporters"**, los cuales permiten que herramientas de terceros puedan exportar sus datos en Prometheus. Muchos componentes de software de código abierto son compatibles por defecto. 
* **Un "exporter" expone las métricas de uno ó varios "collectors".**
* [Prometheus Exporters](https://prometheus.io/docs/instrumenting/exporters/)
    * [https://prometheus.io/download/](https://prometheus.io/download/)
    * [https://github.com/prometheus](https://github.com/prometheus)
* [Prometheus JMX Exporter:](https://github.com/prometheus/jmx_exporter) A process for exposing JMX Beans via HTTP for Prometheus consumption.
* [Example: How to Use Prometheus Monitoring With Java to Gather Data. Gathering Java Metrics with Prometheus Monitoring (ActiveMQ)](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)
* [Maven Prometheus instrumentation library for JVM applications (client library)](https://mvnrepository.com/artifact/io.prometheus)
    * [github.com/prometheus/client_java](https://github.com/prometheus/client_java)
* [Example: JMX Exporter with ActiveMQ](https://www.openlogic.com/blog/prometheus-java-monitoring-and-gathering-data)

#### Prometheus Third Party Exporters
* [Prometheus Third Party Exporters](https://prometheus.io/docs/instrumenting/exporters/)
* [Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus](https://github.com/percona/grafana-dashboards)

#### Prometheus Exporters Development. Node Exporter
* Node exporter puede ser utilizado para exportar las métricas de nuestra aplicación ya que permite exportar un "text-file". Nuestra aplicación puede escribir datos en un fichero de texto con el formato de datos de Prometheus. Este fichero de texto con datos agregados sería exportado a Prometheus con Node Exporter. 
* [https://dzone.com/articles/prometheus-collectors](https://dzone.com/articles/prometheus-collectors)
* [https://prometheus.io/docs/instrumenting/writing_exporters/](https://prometheus.io/docs/instrumenting/writing_exporters/)
* [https://devconnected.com/complete-node-exporter-mastery-with-prometheus](https://devconnected.com/complete-node-exporter-mastery-with-prometheus)
* [https://www.scalyr.com/blog/prometheus-metrics-by-example/](https://www.scalyr.com/blog/prometheus-metrics-by-example/)

### Prometheus Alarms and Event Tracking
* Prometheus no soporta rastreo de eventos (event tracking), pero ofrece un soporte completo de alarmas y gestión de alarmas. El lenguaje de consultas (queries) de Prometheus permite en cambio implementar rastreo de eventos por cuenta propia.

### Prometheus and Cloud Monitoring
* AWS CloudWatch is supported by Prometheus.

### Prometheus Installers
#### Binaries, source code or Docker
* [https://prometheus.io/docs/prometheus/latest/installation/](https://prometheus.io/docs/prometheus/latest/installation/)
* [https://prometheus.io/docs/prometheus/latest/getting_started/](https://prometheus.io/docs/prometheus/latest/getting_started/) 
* [https://github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)

#### Ansible Roles
- **Cloud Alchemy**: Deploy prometheus node exporter using ansible.
    - [https://galaxy.ansible.com/cloudalchemy/node-exporter](https://galaxy.ansible.com/cloudalchemy/node-exporter)
    - [https://github.com/cloudalchemy/ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)
- [Idealista: This ansible role installs a Prometheus Node Exporter in a debian environment](https://github.com/idealista/prometheus_jmx_exporter-role)
- **Alexdzyoba**: This ansible role installs a Prometheus JMX exporter java agent in a debian nvironment. Inspired by [Idealista prometheus_jmx_exporter-role](https://github.com/dealista/prometheus_jmx_exporter-role).
    - [https://galaxy.ansible.com/alexdzyoba/jmx-exporter](https://galaxy.ansible.com/alexdzyoba/jmx-exporter) 
    - [https://github.com/alexdzyoba/ansible-jmx-exporter](https://github.com/alexdzyoba/ansible-jmx-exporter)
- **Mesaguy**: Installs and manages Prometheus and Prometheus exporters.
    - Installs and manages Prometheus server, Alertmanager, PushGateway, and numerous Prometheus exporters
    - This role was designed to allow adding new exporters with ease. Regular releases ensure it always provides the latest Prometheus software.
    - This role can register client exporters with the Prometheus server/s automatically (see tgroup management below).
    - This Ansible role will be migrated to an Ansible Collection.
    - [https://galaxy.ansible.com/mesaguy/prometheus](https://galaxy.ansible.com/mesaguy/prometheus)
    - [https://github.com/mesaguy/ansible-prometheus](https://github.com/mesaguy/ansible-prometheus)
- **William Yeh**: Prometheus for Ansible Galaxy. This role only installs 3 components: Prometheus server, Node exporter, and Alertmanager. 
    - [https://galaxy.ansible.com/William-Yeh/prometheus](https://galaxy.ansible.com/William-Yeh/prometheus) 
    - [https://github.com/William-Yeh/ansible-prometheus](https://github.com/William-Yeh/ansible-prometheus)
    - [https://awesomeopensource.com/project/William-Yeh/ansible-prometheus](https://awesomeopensource.com/project/William-Yeh/ansible-prometheus)
- **Undergreen**: An Ansible role that installs Prometheus Node Exporter on Ubuntu|Debian|redhat-based machines with systemd|Upstart|sysvinit.
    - [https://galaxy.ansible.com/UnderGreen/prometheus-node-exporter](https://galaxy.ansible.com/UnderGreen/prometheus-node-exporter) 
    - [https://github.com/UnderGreen/ansible-prometheus-node-exporter](https://github.com/UnderGreen/ansible-prometheus-node-exporter)
- **Mitesh Sharma**: Prometheus With Grafana Using Ansible
    - [https://itnext.io/prometheus-with-grafana-using-ansible-549e575c9dfa](https://itnext.io/prometheus-with-grafana-using-ansible-549e575c9dfa)
    - [https://github.com/MiteshSharma/PrometheusWithGrafana](https://github.com/MiteshSharma/PrometheusWithGrafana)

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
:------------------|:-------:|:---------------:|------------:
ActiveMQ 5.x "classic"|[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)|[10702](https://grafana.com/grafana/dashboards/10702)|[ActiveMQ Integration](https://docs.wavefront.com/activemq.html), [Config Example](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/activemq.yml)
ActiveMQ Artemis/Red Hat AMQ Broker|[JMX Exporter](https://github.com/prometheus/jmx_exporter)|[9087](https://grafana.com/grafana/dashboards/9087)|[Ref1](https://github.com/prometheus/jmx_exporter/blob/master/example_configs/artemis-2.yml), [Ref2](http://techiekhannotes.blogspot.com/2018/12/artemis-monitoring-with-grafana.html), [Ref 3](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin)
Message Streams like Kafka/Red Hat AMQ Streams|Other|[9777](https://grafana.com/grafana/dashboards/9777)|  

## Kibana
* [Kibana](https://www.elastic.co/kibana)
    * [Kibana Docs](https://www.elastic.co/guide/index.html)
* [dzone: Kibana Tutorial: Part 1 - Getting Started](https://dzone.com/articles/kibana-tutorial-getting-started-part-1)
    * [dzone: Kibana Tutorial: Part 2 - Creating Visualizations](https://logz.io/blog/kibana-tutorial-2/)
* [dzone: Getting Started With Kibana Advanced Searches](https://dzone.com/articles/getting-started-with-kibana-advanced-searches)
* [dzone: Kibana Hacks: 5 Tips and Tricks](https://dzone.com/articles/kibana-hacks-5-tips-and-tricks)

## Interactive Learning
* [katacoda.com: Getting Started with Prometheus](https://www.katacoda.com/courses/prometheus/getting-started)
* [katacoda.com: Creating Dashboards with Grafana](https://www.katacoda.com/courses/prometheus/creating-dashboards-with-grafana)

## Performance
* [dzone.com: The Keys to Performance Tuning and Testing](https://dzone.com/articles/the-keys-to-performance-tuning-and-testing)
* [dzone.com: How Performance Tuning and Testing are Changing](https://dzone.com/articles/how-performance-tuning-and-testing-are-changing)
* Java:
    * [developers.redhat.com: Troubleshooting java applications on openshift](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift/)
    * [dzone.com: how to take thread dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)
* [Performance Patterns in Microservices-Based Integrations 🌟](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1) Almost all applications that perform anything useful for a given business need to be integrated with one or more applications. With microservices-based architecture, where a number of services are broken down based on the services or functionality offered, the number of integration points or touch points increases massively.

## Distributed Tracing. OpenTelemetry and Jaeger
- [**opentelemetry.io** 🌟](https://opentelemetry.io/) (**OpenTracing.io + OpenCensus.io = OpenTelemetry.io**)
- [**Jaeger** 🌟](https://www.jaegertracing.io/)
     - [Jaeger Demo1](https://github.com/obitech/micro-obs)
     - [Jaeger Demo 2](https://github.com/open-telemetry/opentelemetry-collector/tree/master/examples/demo)
     - [medium.com: **Jaeger embraces OpenTelemetry collector** 🌟](https://medium.com/jaegertracing/jaeger-embraces-opentelemetry-collector-90a545cbc24)
- [**zipkin.io**](https://zipkin.io/)
- [**OpenTracing.io**](https://opentracing.io/)
     - [lightstep.com: Understand Distributed Tracing](https://docs.lightstep.com/docs/understand-distributed-tracing)
   
## Application Performance Management (APM)
* [en.wikipedia.org/wiki/Application_performance_management](https://en.wikipedia.org/wiki/Application_performance_management)
* [Awesome APM 🌟](https://github.com/antonarhipov/awesome-apm)
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
    * [AppDynamics 🌟](https://www.appdynamics.com/)
    * [New Relic 🌟](https://newrelic.com/)
    * [Dynatrace 🌟](https://www.dynatrace.com/)
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

