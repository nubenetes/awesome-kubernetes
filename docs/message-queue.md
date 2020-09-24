# Cloud Based Integration & Messaging. Data Processing & Streaming (aka Data Pipeline). Open Data Hub
- [Message Queue in Kubernetes. Event-driven Messaging. Real-Time Data Streaming](#message-queue-in-kubernetes-event-driven-messaging-real-time-data-streaming)
- [Message Brokers](#message-brokers)
    - [ActiveMQ message broker](#activemq-message-broker)
    - [RabbitMQ message broker](#rabbitmq-message-broker)
    - [Redis message broker](#redis-message-broker)
    - [Apache Camel message broker](#apache-camel-message-broker)
        - [Apache Camel K](#apache-camel-k)
    - [KubeMQ message broker](#kubemq-message-broker)
    - [Google Cloud Platform Pub/Sub](#google-cloud-platform-pubsub)
- [Cloud Based Integration. Integration Platform-as-a-Service (iPaaS) solutions](#cloud-based-integration-integration-platform-as-a-service-ipaas-solutions)
    - [Red Hat Fuse and Red Hat Fuse Online](#red-hat-fuse-and-red-hat-fuse-online)
    - [Syndesis open source integration platform](#syndesis-open-source-integration-platform)
- [Debezium open source distributed platform for Change Data Capture (CDC) software design pattern](#debezium-open-source-distributed-platform-for-change-data-capture-cdc-software-design-pattern)
- [Red Hat Integration service registry and Apicurio](#red-hat-integration-service-registry-and-apicurio)
- [Data Processing (aka Streaming Data, Data Pipeline or Big Data Pipeline)](#data-processing-aka-streaming-data-data-pipeline-or-big-data-pipeline)
    - [Apache Airflow](#apache-airflow)
    - [Apache Kafka](#apache-kafka)
    - [Banzai Cloud Supertubes (Cloud Native Kafka implementation)](#banzai-cloud-supertubes-cloud-native-kafka-implementation)
    - [Confluent Cloud (Apache Kafka Re-engineered for the Cloud)](#confluent-cloud-apache-kafka-re-engineered-for-the-cloud)
        - [KsqlDB](#ksqldb)
    - [Apache Pulsar](#apache-pulsar)
    - [Apache Flink](#apache-flink)
    - [Hazelcast JET](#hazelcast-jet)
- [Red Hat AMQ (ActiveMQ Artemis broker and Apache Kafka)](#red-hat-amq-activemq-artemis-broker-and-apache-kafka)
    - [Red Hat AMQ Broker (ActiveMQ Artemis)](#red-hat-amq-broker-activemq-artemis)
    - [Red Hat AMQ Streams](#red-hat-amq-streams)
- [Open Data Hub AI-as-a-Service (AIaaS) platform](#open-data-hub-ai-as-a-service-aiaas-platform)
- [eBooks](#ebooks)
- [Related](#related)
- [Questions and Answers](#questions-and-answers)

## Message Queue in Kubernetes. Event-driven Messaging. Real-Time Data Streaming
- [Wikipedia: Message Broker](https://en.wikipedia.org/wiki/Message_broker)
- [Wikipedia: Event-driven messaging](https://en.wikipedia.org/wiki/Event-driven_messaging)
- [Wikipedia: Streaming Data](https://en.wikipedia.org/wiki/Streaming_data)
- [nginx.com: Event-Driven Data Management for Microservices 🌟](https://www.nginx.com/blog/event-driven-data-management-microservices/)
- [dzone: Event-Driven Architecture as a Strategy](https://dzone.com/articles/event-driven-architecture-as-a-strategy) Event-driven architecture provides five key benefits to modern application architecture: scalability, resilience, agility, data sharing, and cloud enabling.

## Message Brokers
- [Apache ActiveMQ](https://activemq.apache.org/)
- [Dzone: Introduction to Message Brokers. Part 1: Apache Kafka vs. RabbitMQ](https://dzone.com/articles/introduction-to-message-brokers-part-1-apache-kafk)
- [Dzone: Introduction to Message Brokers. Part 2: ActiveMQ vs. Redis Pub/Sub](https://dzone.com/articles/introduction-to-message-brokers-part-2-activemq-vs)
- [developers.redhat.com: Choosing the right asynchronous-messaging infrastructure for the job](https://developers.redhat.com/blog/2020/07/31/choosing-the-right-asynchronous-messaging-infrastructure-for-the-job/)

### ActiveMQ message broker
- [ActiveMQ 5.x "classic"](https://activemq.apache.org/components/classic/)
- [ActiveMQ Artemis](https://activemq.apache.org/components/artemis/) Apache ActiveMQ is a subproject of Apache ActiveMQ. It has been donated to the Apache Software Foundation in 2015. There were lots of changes in project names in the past. The Artemis project first started as JBoss Messaging and got renamed to HornetQ in August 2009.
- [Apache Artemis JMeter](https://github.com/apache/activemq-artemis/tree/master/examples/perf/jmeter) Running the ActiveMQ Artemis JMeter Performance Testing Examples.

### RabbitMQ message broker
- [K8s prevent queue worker Pod from being killed during deployment](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) How to prevent a Kubernetes (like RabbitMQ) queue worker Pod from being killed during deployment while handling a message?
- [medium.com: **RabbitMQ vs. Kafka**](https://medium.com/better-programming/rabbitmq-vs-kafka-1ef22a041793) An architect’s dilemma

### Redis message broker
- [Redis](https://redis.io/)
- [Redis Pub/sub](https://redis.io/topics/pubsub)

### Apache Camel message broker
- [Apache Camel](https://camel.apache.org/)
- [Quora.com: What's the difference between Apache Camel and Kafka?](https://www.quora.com/Whats-the-difference-between-Apache-Camel-and-Kafka)

#### Apache Camel K
- [Apache Camel K](https://camel.apache.org/camel-k/latest/) is a lightweight cloud-integration platform that runs natively on Kubernetes. Based on the famous Apache Camel, Camel K is designed and optimized for serverless and microservices architectures.
- [developers.redhat.com: Six reasons to love Camel K](https://developers.redhat.com/blog/2020/05/12/six-reasons-to-love-camel-k/)
- [developers.redhat.com: Extending Kafka connectivity with Apache Camel Kafka connectors](https://developers.redhat.com/blog/2020/05/19/extending-kafka-connectivity-with-apache-camel-kafka-connectors/)

### KubeMQ message broker
- [KubeMQ.io: Kubernetes Native Message Queue Broker](https://kubemq.io/)
- [devops.com: Best of 2019: Implementing Message Queue in Kubernetes](https://devops.com/implementing-message-queue-in-kubernetes/)
- [kubemq.io: Kafka VS KubeMQ 🌟](https://kubemq.io/kafka-vs-kubemq/)

### Google Cloud Platform Pub/Sub
- [Google Cloud Platform Pub/Sub](https://cloud.google.com/pubsub/docs/overview)
- [A generic framework of concurrent consumers for Google Cloud Platform Pub/Sub 🌟](https://towardsdatascience.com/a-python-implementation-of-concurrent-consumers-for-google-cloud-platform-pub-sub-991ae8b9841d) An example shows how to publish messages to Pub/Sub and build a service to consume the messages concurrently using the Python multiprocessing module

## Cloud Based Integration. Integration Platform-as-a-Service (iPaaS) solutions 
- [Wikipedia: Cloud Based Integration (iPaaS)](https://en.wikipedia.org/wiki/Cloud-based_integration)
- Integration Platform as a Service (iPaaS) is a suite of cloud services enabling development, execution and governance of integration flows connecting any combination of on premises and cloud-based processes, services, applications and data within individual or across multiple organizations.
- Integration platform as a service (iPaaS) is a set of automated tools for connecting software applications that are deployed in different environments. iPaaS is often used by large business-to-business (B2B) enterprises that need to integrate on-premises applications and data with cloud applications and data.
- [blog.axway.com: What is iPaaS?](https://blog.axway.com/hybrid-integration/whats-ipaas)
- [ibm.com: iPaaS (Integration-Platform-as-a-Service)](https://www.ibm.com/cloud/learn/ipaas): iPaaS is a cloud-based solution that simplifies application integration across on-premises and cloud environments, to help you accelerate innovation and lower your integration and operations costs.

### Red Hat Fuse and Red Hat Fuse Online
- [**Red Hat Fuse**](https://www.redhat.com/en/technologies/jboss-middleware/fuse)
- [**Red Hat Fuse Online**](https://www.redhat.com/en/technologies/jboss-middleware/fuse-online)
    
### Syndesis open source integration platform 
- [**Syndesis** open source integration platform](https://syndesis.io/) (OpenSource Project for **Red Hat Fuse Online**)
- [developers.redhat.com: Low-code microservices orchestration with Syndesis](https://developers.redhat.com/blog/2020/03/25/low-code-microservices-orchestration-with-syndesis/)

## Debezium open source distributed platform for Change Data Capture (CDC) software design pattern
- **Change Data Capture**, or **CDC**, is a well-established **software design pattern** for a system that monitors and captures the changes in data so that other software can respond to those changes. CDC captures row-level changes to database tables and passes corresponding change events to a data streaming bus. Applications can read these change event streams and access these change events in the order in which they occurred.
- [**Debezium**:](https://debezium.io/) Stream changes from your database
- [developers.redhat.com: Decoupling microservices with Apache Camel and Debezium](https://developers.redhat.com/blog/2019/11/19/decoupling-microservices-with-apache-camel-and-debezium/)
- [A good explanation of how to avoid distributed transactions using outbox pattern: Transaction Log Tailing With Debezium](https://medium.com/trendyol-tech/transaction-log-tailing-with-debezium-part-1-aeb968d72220)
- [developers.redhat.com: Capture database changes with Debezium Apache Kafka connectors](https://developers.redhat.com/blog/2020/04/14/capture-database-changes-with-debezium-apache-kafka-connectors/)
- [developers.redhat.com: Change data capture for microservices without writing any code](https://developers.redhat.com/blog/2020/05/15/change-data-capture-for-microservices-without-writing-any-code/)
- [debezium.io: Lessons Learned from Running Debezium with PostgreSQL on Amazon RDS](https://debezium.io/blog/2020/02/25/lessons-learned-running-debezium-with-postgresql-on-rds/)
- [info.crunchydata.com: PostgreSQL Change Data Capture With Debezium](https://info.crunchydata.com/blog/postgresql-change-data-capture-with-debezium)
- [medium.com: Stream Your Database into Kafka with Debezium](https://medium.com/comsystoreply/stream-your-database-into-kafka-with-debezium-a94b2f649664) An Introduction and Experience Report. Insightful post by David Hettler of 
comsysto about their usage of Debezium, touching on many details like outbox pattern, Avro schemas, Postgres on RDS etc.

## Red Hat Integration service registry and Apicurio
- [Red Hat Integration service registry](https://developers.redhat.com/blog/2019/12/16/getting-started-with-red-hat-integration-service-registry/)
- [**Apicurio** Registry](https://github.com/apicurio/apicurio-registry) An API/Schema registry - stores APIs and Schemas.
- [Event streaming and data federation: A citizen integrator’s story](https://developers.redhat.com/blog/2020/06/12/event-streaming-and-data-federation-a-citizen-integrators-story/)

## Data Processing (aka Streaming Data, Data Pipeline or Big Data Pipeline)
- [Awesome Streaming](https://github.com/manuzhang/awesome-streaming) A curated list of awesome [streaming (stream processing)](https://www.oreilly.com/radar/the-world-beyond-batch-streaming-101/) frameworks, applications, readings and other resources.

### Apache Airflow
- [towardsdatascience.com: A journey to Airflow on Kubernetes](https://towardsdatascience.com/a-journey-to-airflow-on-kubernetes-472df467f556)

### Apache Kafka
- [Apache Kafka](https://kafka.apache.org/)
- [developers.redhat.com: how easy to deploy and configure a Kafka Connect on Kubernetes through strimziio operator and use secrets](https://developers.redhat.com/blog/2020/02/14/using-secrets-in-apache-kafka-connect-configuration/)
- [developers.redhat.com: Using secrets in Kafka Connect configuration](https://developers.redhat.com/blog/2020/02/14/using-secrets-in-apache-kafka-connect-configuration/)
- [developers.redhat.com: Capture database changes with Debezium Apache Kafka connectors](https://developers.redhat.com/blog/2020/04/14/capture-database-changes-with-debezium-apache-kafka-connectors/)
- [Awesome Kafka](https://github.com/monksy/awesome-kafka/blob/master/tools.md)
- [Single Message Transformations - The Swiss Army Knife of Kafka Connect](https://www.morling.dev/blog/single-message-transforms-swiss-army-knife-of-kafka-connect/)
- [medium: Logs & Offsets: (Near) Real Time ELT with Apache Kafka + Snowflake](https://medium.com/convoy-tech/logs-offsets-near-real-time-elt-with-apache-kafka-snowflake-473da1e4d776) Replacing Apache Airflow with Debezium. 
- [medium: Apache Kafka Startup Guide: System Design Architectures: Notification System, Web Activity Tracker, ELT Pipeline, Storage System 🌟](https://medium.com/swlh/apache-kafka-startup-guide-system-design-architectures-notification-system-web-activity-tracker-6dcaf0cf8a7)
- [medium: Getting Started With Kafka on OpenShift](https://medium.com/swlh/getting-started-with-kafka-on-openshift-c44c0fdec384)
- [containerjournal.com: Red Hat Platform Brings Kafka Closer to Kubernetes](https://containerjournal.com/topics/container-management/red-hat-platform-brings-kafka-closer-to-kubernetes/)
- [lightbend.com: Monitor Kafka Consumer Group Latency with Kafka Lag Exporter](https://www.lightbend.com/blog/monitor-kafka-consumer-group-latency-with-kafka-lag-exporter)
- [AKHQ (previously known as KafkaHQ) 🌟](https://github.com/tchiotludo/akhq) Kafka GUI for Apache Kafka to manage topics, topics data, consumers group, schema registry, connect and more...
- [banzaicloud.com: Kafka Schema Registry on Kubernetes the declarative way](https://banzaicloud.com/blog/kafka-schemareg/)
- [Build a simple cloud-native change data capture pipeline](https://developers.redhat.com/blog/2020/07/02/build-a-simple-cloud-native-change-data-capture-pipeline/)

<center>
[![airflow vs kafka debezium](images/airflow_vs_debezium.jpg)](https://medium.com/convoy-tech/logs-offsets-near-real-time-elt-with-apache-kafka-snowflake-473da1e4d776)
</center>

### Banzai Cloud Supertubes (Cloud Native Kafka implementation)
- [Banzai Cloud](https://banzaicloud.com/)
- [Banzai Kafka Operator](https://github.com/banzaicloud/kafka-operator)
- [The benefits of integrating Apache Kafka with Istio](https://banzaicloud.com/blog/kafka-on-istio-benefits/)

### Confluent Cloud (Apache Kafka Re-engineered for the Cloud)
- [confluent.io](https://www.confluent.io/) The Complete Event Streaming Platform for Apache Kafka. 
- Focus on building apps and not managing clusters with a scalable, resilient and secure event streaming platform. Event streaming with Kafka made simple on AWS, Azure and GCP clouds.

#### KsqlDB
- [ksqlDB](https://ksqldb.io/) The event streaming database purpose-built for stream processing applications.
- [Kafka Streams and ksqlDB Compared – How to Choose](https://www.confluent.io/blog/kafka-streams-vs-ksqldb-compared/)

### Apache Pulsar
- [Apache Pulsar](https://pulsar.apache.org/) is an open-source distributed pub-sub messaging system originally created at Yahoo and now part of the Apache Software Foundation
- [Pulsar vs Kafka – Comparison and Myths Explored](https://www.kai-waehner.de/blog/2020/06/09/apache-kafka-versus-apache-pulsar-event-streaming-comparison-features-myths-explored/)

### Apache Flink
- [Apache Flink](https://flink.apache.org/) Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.
- [How to set up Apache Flink on Kubernetes for real time data processing](https://ci.apache.org/projects/flink/flink-docs-stable/ops/deployment/kubernetes.html)

### Hazelcast JET
- [Hazelcast JET](https://jet-start.sh/) Open-Source Distributed Stream Processing
- [devops.com: Hazelcast Simplifies Streaming for Extremely Fast Event Processing in IoT, Edge and Cloud Environments](https://devops.com/hazelcast-simplifies-streaming-for-extremely-fast-event-processing-in-iot-edge-and-cloud-environments/)

## Red Hat AMQ (ActiveMQ Artemis broker and Apache Kafka)
- [**Red Hat AMQ overview**](https://developers.redhat.com/products/amq/overview)
- [Red Hat AMQ](https://www.redhat.com/en/technologies/jboss-middleware/amq) = AMQ Broker (Apache ActiveMQ Artemis) + AMQ Streams (Apache Kafka)

### Red Hat AMQ Broker (ActiveMQ Artemis)
- [Apache ActiveMQ Artemis broker](https://activemq.apache.org/components/artemis/)
- [developers.redhat.com: JDBC Master-Slave Persistence setup with Activemq using Postgresql database](https://developers.redhat.com/blog/2017/10/05/jdbc-master-slave-persistence-setup-activemq-using-postgresql-database)
- [developers.redhat.com: Connecting external clients to Red Hat AMQ Broker on Red Hat OpenShift](https://developers.redhat.com/blog/2020/08/26/connecting-external-clients-to-red-hat-amq-broker-on-red-hat-openshift)

### Red Hat AMQ Streams
- [Understanding Red Hat AMQ Streams components for OpenShift and Kubernetes 🌟](https://developers.redhat.com/blog/2019/12/04/understanding-red-hat-amq-streams-components-for-openshift-and-kubernetes-part-1/)
- [Red Hat **AMQ streams** (kafka): Simplify Apache Kafka on Red Hat OpenShift](https://www.redhat.com/en/resources/amq-streams-datasheet)
- [Set up **Red Hat AMQ Streams** custom certificates on OpenShift](https://developers.redhat.com/blog/2020/04/01/set-up-red-hat-amq-streams-custom-certificates-on-openshift-update/)
- [speakerdeck.com: Apache Kafka with Red Hat AMQ Streams 🌟](https://speakerdeck.com/mabulgu/apache-kafka-with-red-hat-amq-streams)
- [HTTP-based Kafka messaging with Red Hat AMQ Streams](https://developers.redhat.com/blog/2020/08/04/http-based-kafka-messaging-with-red-hat-amq-streams/#more-720187)

<center>
[![AMQ in a nutshell](images/AMQ.png)](https://developers.redhat.com/products/amq/overview)
</center>

Product|Also Known As|Components|URL
:------|:----|:--------|:----
Red Hat AMQ 6|JBoss AMQ 6|Apache ActiveMQ|[Ref](https://access.redhat.com/documentation/en-us/red_hat_amq/6.3/)
Red Hat AMQ 7|JBoss AMQ 7 (Broker) or Red Hat AMQ 7 Suite|AMQ Broker + AMQ Streams|[Ref](https://access.redhat.com/documentation/en-us/red_hat_amq/6.3/)
Red Hat AMQ 7|JBoss AMQ 7 (Broker) or Red Hat AMQ 7 Suite|JBoss AMQ 7 (Broker) + Apache Kafka|[Ref](https://access.redhat.com/documentation/en-us/red_hat_amq/6.3/)
Red Hat AMQ 7|JBoss AMQ 7 (Broker) or Red Hat AMQ 7 Suite|Apache ActiveMQ Artemis + Apache Kafka|[Ref](https://access.redhat.com/documentation/en-us/red_hat_amq/6.3/)

<center>
<script async class="speakerdeck-embed" data-id="54c1ce6ee6e44d68a0c311c31ddc8225" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>

## Open Data Hub AI-as-a-Service (AIaaS) platform
- [Open Data Hub](https://opendatahub.io/)
- [Open Data Hub 0.6 brings component updates and Kubeflow architecture](https://developers.redhat.com/blog/2020/05/07/open-data-hub-0-6-brings-component-updates-and-kubeflow-architecture/)
- [A development roadmap for Open Data Hub](https://developers.redhat.com/blog/2020/06/22/a-development-roadmap-for-open-data-hub/)

## eBooks
- [O'Really: Streaming data](http://streamingsystems.net/)

## Related
- [Service meshes to the rescue: Load balancing and scaling long-lived connections in Kubernetes](https://learnk8s.io/kubernetes-long-lived-connections)

## Questions and Answers
- [adambien.blog - 75th **airhacks.tv** Questions and Answers: Kafka, JAX-RS, MicroProfile, JSON-B, GSON, JWT, VSC, NetBeans, Java Fullstack](https://adambien.blog/roller/abien/entry/kafka_jax_rs_microprofile_json) "Kafka vs. JAX-RS / RPC, thoughts about APIs, JSON-B vs. GSON, Path.of over Paths.get, Java Records, MicroProfile JWT, beginners vs. expert content, best Java fullstack, code coverage, NetBeans in 2020, Visual Studio Setup for Java, screencast configuration, ReactJS / Angular over JSF?, JSON-P vs. JSON-B, security code scanning"

---

<center>
<iframe src="https://www.youtube.com/embed/LieT75Zb_OY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Pub-Sub ≠ Partitioning ≠ Multiplexing <a href="https://t.co/0ZVaH9Mxvr">pic.twitter.com/0ZVaH9Mxvr</a></p>&mdash; Clemens Vasters 🇪🇺☁📨 (@clemensv) <a href="https://twitter.com/clemensv/status/1288152399211909120?ref_src=twsrc%5Etfw">July 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>