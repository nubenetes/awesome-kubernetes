# Message Queue

!!! info "Architectural Context"
    Detailed reference for Message Queue in the context of Data & Advanced Analytics.

## Application Integration

### Cloud Managed Services

#### Pub-Sub Pattern

  - **(2026)** [==Google Cloud Platform Pub/Sub==](https://docs.cloud.google.com/pubsub/docs/overview) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Comprehensive documentation for GCP Pub/Sub, an enterprise-grade, globally distributed, fully-managed asynchronous messaging service. It provides consistent sub-second latencies at arbitrary scale. It features seamless integrations with Google Cloud's data analytics stacks.
### Enterprise Integration Patterns

#### Cloud Managed Services (1)

  - **(2024)** [ibm.com: iPaaS (Integration-Platform-as-a-Service)](https://www.ibm.com/think/topics/ipaas) 🌟🌟🌟 <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A strategic and architectural overview of Integration Platform as a Service (iPaaS). It reviews how cloud-native middleware bridges legacy on-premise systems and modern SaaS ecosystems. Highly useful for enterprise digital integration roadmaps.
#### Event-Driven Systems

  - **(2021)** [developers.redhat.com: Design event-driven integrations with Kamelets and Camel K](https://developers.redhat.com/blog/2021/04/02/design-event-driven-integrations-with-kamelets-and-camel-k) 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Introduces "Kamelets" (Camel Route Snippets), which act as reusable cloud-native integration building blocks. It explains how non-developers or low-code frameworks can plug Kamelets into serverless topologies for immediate data flow orchestration on Kubernetes.
#### Middleware

  - **(2025)** [****Red Hat Fuse****](https://www.redhat.com/en/products/application-foundations) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Red Hat's enterprise-grade, distributed integration platform, heavily utilizing Apache Camel, ActiveMQ, and CXF. It provides a highly stable middleware environment designed to bind heterogeneous enterprise workloads and APIs under unified orchestration rules.
#### Serverless Integration

  - **(2021)** [developers.redhat.com: Integrating systems with Apache Camel and Quarkus on Red Hat OpenShift](https://developers.redhat.com/articles/2021/05/17/integrating-systems-apache-camel-and-quarkus-red-hat-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Practical walk-through highlighting the integration of legacy enterprise environments using Apache Camel Quarkus extensions (Camel K) on OpenShift. It demonstrates how Quarkus' sub-second startup times enable serverless, cloud-native integration routes.
### Event Streaming

#### Enterprise Integration Patterns (1)

  - **(2022)** [**kai-waehner.de: When to use Apache Camel vs. Apache Kafka? 🌟**](https://www.kai-waehner.de/blog/2022/01/28/when-to-use-apache-camel-vs-apache-kafka-for-etl-application-integration-event-streaming) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines the complementarity and core differences between Apache Camel (an integration framework implementing Enterprise Integration Patterns) and Apache Kafka (a distributed streaming platform). It outlines architectures where Camel acts as a producer/consumer or edge connector for Kafka pipelines.
#### Kafka Connectors

  - **(2020)** [**developers.redhat.com: Extending Kafka connectivity with Apache Camel Kafka connectors**](https://developers.redhat.com/blog/2020/05/19/extending-kafka-connectivity-with-apache-camel-kafka-connectors) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Outlines how the Camel Kafka Connector framework allows developers to utilize Camel's extensive component suite as standard Kafka Connect sources or sinks. This simplifies ingestion and delivery to hundreds of external enterprise systems without custom code.
### Local Development

#### Containerization

  - **(2021)** [geshan.com.np: How to use RabbitMQ and Node.js with Docker and Docker-compose](https://geshan.com.np/blog/2021/07/rabbitmq-docker-nodejs) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A hands-on tutorial outlining the setup of a localized asynchronous worker pipeline using Node.js, RabbitMQ, and Docker Compose. It serves as an accessible entry point to grasp queue-based application decoupling. Includes configuration templates ready for development workflows.
### Low-Code Integration

#### Enterprise Integration Patterns (2)

  - **(2022)** [**Syndesis** open source integration platform](https://syndesis.io) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Syndesis is an open-source, cloud-native low-code integration platform designed to run natively on Kubernetes and OpenShift. It enables drag-and-drop connections between diverse business APIs and internal databases, utilizing Apache Camel under the hood. Note: The project has recently transitioned to legacy status.
#### Microservices

  - **(2020)** [developers.redhat.com: Low-code microservices orchestration with Syndesis](https://developers.redhat.com/blog/2020/03/25/low-code-microservices-orchestration-with-syndesis) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed demonstration of leveraging Syndesis for visual, low-code orchestration of enterprise microservices. It highlights quick deployment cycles, declarative configuration models, and integration with Red Hat OpenShift resources.
### Message Brokers

#### Clustering

  - **(2021)** [developers.redhat.com: Implementing Apache ActiveMQ-style broker meshes with Apache Artemis](https://developers.redhat.com/articles/2021/06/30/implementing-apache-activemq-style-broker-meshes-apache-artemis) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Focuses on establishing distributed, multi-broker network configurations (broker meshes) using Apache Artemis. It highlights migration techniques from classic ActiveMQ network-of-brokers architectures. It explains target configuration profiles to optimize reliability across complex enterprise regions.
#### Evaluation Frameworks

  - **(2022)** [**kai-waehner.de: Comparison: JMS Message Queue vs. Apache Kafka**](https://www.kai-waehner.de/blog/2022/05/12/comparison-jms-api-message-broker-mq-vs-apache-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details the technical tradeoffs, design limitations, and complementary features of JMS broker specifications versus Apache Kafka. It assists system engineers in distinguishing transaction-heavy classic queuing requirements from massive event streaming workloads.
  - **(2020)** [**developers.redhat.com: Choosing the right asynchronous-messaging infrastructure for the job**](https://developers.redhat.com/blog/2020/07/31/choosing-the-right-asynchronous-messaging-infrastructure-for-the-job) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Lays out a decision framework for choosing between broker-based messaging (e.g., AMQP, ActiveMQ), event-streaming (e.g., Apache Kafka), and cloud-native serverless event routing. It evaluates criteria like throughput, ordering guarantees, consumer groups, and message preservation. This is an essential architectural comparative reference.
  - **(2023)** [kubemq.io: Kafka VS KubeMQ 🌟](https://kubemq.io/kafka-vs-kubemq) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides a detailed comparison between Apache Kafka and KubeMQ, focusing on memory footprint, container resource demands, and operational complexity. It presents KubeMQ as a highly localized, easy-to-manage container broker, contrasting it with Kafka's robust, distributed cluster topology.
#### Event Streaming (1)

  - **(2021)** [**blog.rabbitmq.com: First Application With RabbitMQ Streams**](https://www.rabbitmq.com/blog/2021/07/19/rabbitmq-streams-first-application) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Introduces RabbitMQ Streams, a high-throughput, log-append-only streaming protocol introduced in RabbitMQ 3.9. It compares RabbitMQ Streams' sub-millisecond latencies and message retention directly with traditional AMQP queues and Apache Kafka. The walkthrough showcases a complete consumer-producer application setup.
#### High-Performance Messaging

  - **(2026)** [==Apache Artemis JMeter==](https://github.com/apache/artemis) <span class='md-tag md-tag--info'>⭐ 1017</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official GitHub mirror of Apache ActiveMQ Artemis, housing the high-performance non-blocking asynchronous message broker. It provides native support for AMQP, MQTT, STOMP, and OpenWire. It delivers ultra-low latency and scalable message distribution under extreme workloads.
#### JMS

  - **(2024)** [**ActiveMQ 5.x "classic"**](https://activemq.apache.org/components/classic) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The classic implementation of Apache ActiveMQ, continuing to power millions of production enterprise nodes. It offers rich support for JMS client specifications alongside robust clustering and persistence. Ideal for traditional integration architecture, though increasingly superseded by Artemis.
  - **(1999)** [**Apache ActiveMQ**](https://activemq.apache.org) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — An iconic, mature open-source multi-protocol message broker supporting JMS 1.1 and 2.0, AMQP, MQTT, and STOMP. Known for enterprise-grade reliability and complex message routing patterns. It remains a foundational asset in legacy integration environments globally.
#### Kubernetes Native

  - **(2026)** [**KubeMQ.io: Kubernetes Native Message Queue Broker**](https://kubemq.io) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — KubeMQ is an enterprise-grade, ultra-lightweight message broker engineered specifically for Kubernetes container ecosystems. Delivered in a minimal footprint, it supports pub/sub, queues, and streams with native GRPC and REST support. It avoids external operational dependencies.
  - **(2024)** [**github.com/kubemq-io/kubemq-community 🌟**](https://github.com/kubemq-io/kubemq-community) <span class='md-tag md-tag--info'>⭐ 668</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The community-driven core repository for KubeMQ. It offers a lightweight, high-performance messaging interface for microservices on Kubernetes. Supports standard asynchronous protocols and integrates natively with Kubernetes patterns.
  - **(2019)** [devops.com: Best of 2019: Implementing Message Queue in Kubernetes](https://devops.com/implementing-message-queue-in-kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Evaluates the operational paradigms, stateful challenges, and strategies when setting up distributed message brokers natively inside Kubernetes environments. Discusses dynamic volume allocations, stateful sets, and persistent cloud networking protocols.
#### Pub-Sub Pattern (1)

  - **(2026)** [**Redis Pub/sub**](https://redis.io/docs/latest/develop) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official developer documentation detailing Redis' built-in Pub/Sub and Streams features. It provides technical blueprints for lightweight, fire-and-forget message passing and log-append streaming. This allows developers to construct fast messaging queues without setting up heavy broker architectures.
### Orchestration

#### Kubernetes Operators

  - **(2024)** [**Apache Camel K**](https://camel.apache.org/camel-k/2.10.x) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Core documentation for Apache Camel K, a lightweight cloud-native integration platform built on Kubernetes. It utilizes the Operator Pattern to run integration DSL routes serverlessly. It drastically simplifies deploying complex integration patterns across cloud-native domains.
  - **(2021)** [thenewstack.io: Camel K Brings Apache Camel to Kubernetes for Event-Driven Architectures](https://thenewstack.io/camel-k-brings-apache-camel-to-kubernetes-for-event-driven-architectures) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive review of Camel K's architecture, analyzing its integration with Knative and Kubernetes-native messaging patterns. It describes how Camel K reduces traditional ESB resource consumption to support high-density container layouts.
#### Reference Architecture

  - **(2022)** [github.com/osa-ora/camel-k-samples](https://github.com/osa-ora/camel-k-samples) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated collection of practical code templates and sample deployment topologies demonstrating Camel K in action. Covers integrations with relational databases, message queues, and cloud endpoints. This repository is a valuable tool for accelerated prototyping.
#### Serverless Integration (1)

  - **(2020)** [developers.redhat.com: Six reasons to love Camel K](https://developers.redhat.com/blog/2020/05/12/six-reasons-to-love-camel-k) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Outlines six key architectural advantages of Camel K, including fast deployment loops, native Quarkus optimization, low memory footprints, and serverless scale-to-zero capabilities via Knative. Highly useful for architects modernizing traditional ESBs.
## Cloud Native Architecture

### Domain-Driven Design

#### Messaging Architectures

  - **(2019)** [**verraes.net: DDD and Messaging Architectures 🌟**](https://verraes.net/2019/05/ddd-msg-arch) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Synthesizes core concepts of Domain-Driven Design (DDD) with message-oriented middleware patterns. It examines bounded contexts, aggregate boundaries, and the strategic distribution of domain events. It provides deep conceptual clarity on decoupling enterprise service boundaries using asynchronous message paths.
### Event-Driven Systems (1)

#### Foundations

  - **(2021)** [thenewstack.io: The Rise of Event-Driven Architecture](https://thenewstack.io/the-rise-of-event-driven-architecture) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Traces the industry shift from request-response synchronous APIs to asynchronous event-driven models. It outlines the architectural advantages regarding system resilience, temporal decoupling, and scalability. The analysis evaluates standard broker technologies that enable reactive cloud-native systems.
#### Patterns

  - **(2021)** [**codeopinion.com: Event Sourcing vs Event Driven Architecture**](https://codeopinion.com/event-sourcing-vs-event-driven-architecture) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Clarifies the critical distinctions and synergies between Event Sourcing (capturing state transitions as events) and Event-Driven Architecture (broadcasting state changes). It uses architectural examples to prevent common integration anti-patterns. This assists architects in deciding when to combine or isolate these patterns.
#### Standards

  - **(2022)** [**salaboy.com: Event-Driven applications with CloudEvents on Kubernetes**](https://www.salaboy.com/2022/01/29/event-driven-applications-with-cloudevents-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains how the CNCF CloudEvents specification standardizes event metadata format across distinct systems. It integrates CloudEvents within Kubernetes architectures using tools like Knative Eventing. This provides an excellent overview of building vendor-neutral, highly reactive event mesh fabrics.
### Foundations (1)

#### Introductory Patterns

  - **(2024)** [ibm.com: Event-driven cloud-native applications (microservices)](https://www.ibm.com/think/topics/cloud-native) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains core principles of cloud-native architecture, including containerization, microservices, and reactive behaviors. It outlines the foundational tenets necessary to design robust applications optimized for public and private clouds. It serves as a high-level conceptual reference for infrastructure modernization.
### Inter-Service Communication

#### Performance

  - **(2020)** [particular.net: RPC vs. Messaging – which is faster?](https://particular.net/blog/rpc-vs-messaging-which-is-faster) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides a detailed comparative benchmark of Remote Procedure Call (RPC) protocols versus messaging-based asynchronous protocols. It highlights how latency, queue depths, network overhead, and decoupling impact application performance under high load. It concludes that throughput gains in asynchronous messaging often outweigh synchronous RPC latency benefits.
### Microservices (1)

#### Change Data Capture CDC

  - **(2020)** [**developers.redhat.com: Change data capture for microservices without writing any code**](https://developers.redhat.com/blog/2020/05/15/change-data-capture-for-microservices-without-writing-any-code) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walkthrough detailing how to set up out-of-the-box Change Data Capture architectures using Debezium without custom application-level code. It demonstrates immediate real-time synchronization from database transactions straight to Kafka-enabled microservices.
  - **(2019)** [**developers.redhat.com: Decoupling microservices with Apache Camel and Debezium**](https://developers.redhat.com/blog/2019/11/19/decoupling-microservices-with-apache-camel-and-debezium) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains how to decouple distributed database structures in microservices by employing a combination of Debezium (for Change Data Capture) and Apache Camel (for integration and transformation pipelines). It ensures low latency, resilient state updates.
#### Distributed Transactions

  - **(2021)** [**developers.redhat.com: Distributed transaction patterns for microservices compared**](https://developers.redhat.com/articles/2021/09/21/distributed-transaction-patterns-microservices-compared) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes and contrasts critical transactional strategies for microservice boundaries, including 2PC (Two-Phase Commit), Sagas, and Outbox patterns. It highlights how asynchronous message-passing mitigates the failure modes of distributed transactions. Practical implementation guidelines focus on maintaining eventual consistency without tight coupling.
#### Event Sourcing

  - **(2021)** [blog.bitsrc.io: Why Microservices Should use Event Sourcing 🌟](https://blog.bitsrc.io/why-microservices-should-use-event-sourcing-9755a54ebfb4) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Argues the case for event sourcing as a primary mechanism to store state in distributed microservice topologies. It highlights capabilities such as complete audit trails, high-performance writes, and historical state reconstruction. The post warns of common pitfalls including schema evolution complexity and read projection overhead.
## Cloud Native Infrastructure

### High Availability

#### Kafka on Kubernetes

  - **(2022)** [==learnk8s.io/kafka-ha-kubernetes: Designing and testing a highly available Kafka cluster on Kubernetes 🌟==](https://learnkube.com/kafka-ha-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Outstanding reference tutorial for validating HA setups in production. Live Grounding: Outlines designing multi-AZ deployments, tuning pod disruption budgets (PDBs), and performing simulated chaos engineering tests (network partitions, node restarts) to prove zero-data-loss capabilities.
### Kafka on Kubernetes (1)

#### Application Integration (1)

  - **(2021)** [itnext.io: Sending Messages to Kafka in Kubernetes](https://itnext.io/sending-messages-to-kafka-cfb5a246f5eb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Practical post on establishing low-latency, secure client connections to Kafka brokers inside a Kubernetes network boundary. Live Grounding: Reviews internal DNS routing, ingress endpoints, and SASL authentication configs to safely bridge containerized publishers and consumer workloads.
#### Deployments

  - **(2023)** [thelinuxnotes.com: How to deploy Kafka in Kubernetes with Helm chart + kafdrop](https://thelinuxnotes.com/how-to-deploy-kafka-in-kubernetes-with-helm-chart-kafdrop-commander)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Deployment tutorial utilizing established community Helm packages. Live Grounding: Guides deployment of a functional Kafka test cluster integrated directly with Kafdrop as a companion visual administration interface.
#### Guides

  - **(2022)** [**linkedin.com: Kafka Cluster Setup on Kubernetes**](https://www.linkedin.com/pulse/kaka-cluster-setup-kubernetes-avinash-kumar-chandran) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Step-by-step technical guide for provisioning Kafka on Kubernetes using direct manifests. Live Grounding: Covers statefulsets, headless service definitions, volume claim templates, and environment variables targeting manual multi-broker cluster creation.
#### Local Development (1)

  - **(2021)** [dev.to: Running Kafka on kubernetes for local development](https://dev.to/thegroo/running-kafka-on-kubernetes-for-local-development-2a54)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Practical setup workflow for running local Kafka configurations under Minikube or Docker Desktop. Live Grounding: Explains minimal YAML profiles using Helm or lightweight operators to quickly spin up development broker instances for sandboxed microservices validation.
### Kubernetes Strategy

#### Infrastructure Decisions

  - **(2023)** [**thenewstack.io: Kafka on Kubernetes: Should You Adopt a Managed Solution?**](https://thenewstack.io/kafka-on-kubernetes-should-you-adopt-a-managed-solution) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Strategic evaluation of managed SaaS Kafka setups versus DIY operator approaches on Kubernetes. Live Grounding: Compares total cost of ownership (TCO), maintenance scaling, day-2 operations complexity, and custom flexibility demands.
### Security

#### Amazon EKS

  - **(2021)** [itnext.io: Securely Decoupling Kubernetes-based Applications on Amazon EKS using Kafka with SASL/SCRAM](https://itnext.io/securely-decoupling-applications-on-amazon-eks-using-kafka-with-sasl-scram-48c340e1ffe9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Hardening guide detailing connection security between AWS EKS-based consumers and Kafka clusters. Live Grounding: Demonstrates configuring Kafka users with SASL/SCRAM credentials, managing secrets within Kubernetes natively, and establishing encrypted TLS connectivity over VPC boundaries.
### Serverless Data Platforms

#### Elastic Kafka

  - **(2021)** [confluent.io: Making Apache Kafka Serverless: Lessons From Confluent Cloud](https://www.confluent.io/blog/designing-an-elastic-apache-kafka-for-the-cloud) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Architectural retrospective on how Confluent engineered a multi-tenant, elastic serverless Kafka platform. Live Grounding: Explores storage-compute decoupling, automated partition rebalancing, and custom multi-tenant billing-aware resource allocators.
### Stateful Workloads

#### Kafka on Kubernetes (2)

  - **(2021)** [**phoenixnap.com: How to Set Up and Run Kafka on Kubernetes 🌟**](https://phoenixnap.com/kb/kafka-on-kubernetes) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Comprehensive guide to running stateful Kafka clusters on Kubernetes platforms. Live Grounding: Outlines deploying Kafka utilizing statefulsets, configuring persistent volumes, and handling network routing. Explores the advantages of operator-managed setups versus standard manual deployments.
#### Strimzi Operator

  - [==strimzi.io==](https://strimzi.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: The leading open-source CNCF sandbox operator platform for running Kafka on Kubernetes. Live Grounding: Orchestrates secure topologies, cluster expansion, user management, and seamless rolling upgrades using fully declarative Kubernetes Custom Resources (CRDs).
  - **(2020)** [**developers.redhat.com: Introduction to Strimzi: Apache Kafka on Kubernetes (KubeCon Europe 2020) 🌟**](https://developers.redhat.com/blog/2020/08/14/introduction-to-strimzi-apache-kafka-on-kubernetes-kubecon-europe-2020) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Detailed breakdown of the Strimzi operator architectural internals from KubeCon. Live Grounding: Evaluates how the operator automates bootstrap, health monitoring, protocol configurations, TLS generation, and storage management for Kafka on Kubernetes.
  - **(2021)** [strimzi.io: Kafka upgrade improvements](https://strimzi.io/blog/2021/07/05/upgrade-improvements) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Direct technical update from the Strimzi maintainers regarding Kafka upgrade orchestration. Live Grounding: Details the architectural improvements in Strimzi's reconciliation loops, enabling automated, zero-downtime rolling upgrades of stateful Kafka pods with strict schema protection.
#### Tooling and UI

  - **(2024)** [pepy.tech/project/strimzi-kafka-cli 🌟](https://pepy.tech/projects/strimzi-kafka-cli) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Download analytics and overview of the Strimzi Kafka CLI. Live Grounding: Provides python-based CLI tools to interactively administer Strimzi-managed custom resources, simplifying manual deployment, topic configuration, and user creation operations.
## Cloud-Native Infrastructure

### Event Streaming (2)

#### GitOps Practices

  - **(2021)** [**confluent.io: DevOps for Apache Kafka with Kubernetes and GitOps 🌟**](https://www.confluent.io/blog/devops-for-apache-kafka-with-kubernetes-and-gitops) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Examines GitOps models for coordinating declarative configurations of schemas, partitions, ACLs, and topics across multiple Kubernetes-hosted Kafka environments using automated pipelines.
#### Infrastructure Operations

  - **(2018)** [tecmint: How to Install Apache Kafka in CentOS/RHEL 7](https://www.tecmint.com/install-apache-kafka-in-centos-rhel) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A technical operational guide detailing the installation and configuration of Zookeeper and Apache Kafka services directly on bare-metal or VM instances running CentOS and RHEL 7.
#### Kafka Connect Operators

  - **(2021)** [developers.redhat.com: Improve your Kafka Connect builds of Debezium.](https://developers.redhat.com/articles/2021/12/06/improve-your-kafka-connect-builds-debezium#build_a_debezium_kafka_connect_image_with_a_custom_resource) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical walk-through of the Strimzi Operator build processes for deploying optimized Kafka Connect container environments on Kubernetes. Illustrates declarative custom resource setups to bundle custom Debezium connector packages safely.
#### Kubernetes Operators (1)

  - **(2021)** [openshift.com: How to Orchestrate Data Pipelines with Applications Deployed on OpenShift](https://www.redhat.com/en/blog/how-to-orchestrate-data-pipelines-with-applications-deployed-on-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates deployment patterns for co-locating high-throughput data processing pipelines (Argo, Apache Spark, Strimzi) directly alongside backend application microservices inside Red Hat OpenShift clusters.
  - **(2021)** [thenewstack.io: Beyond the Quickstart: Running Apache Kafka as a Service on Kubernetes](https://thenewstack.io/beyond-the-quickstart-running-apache-kafka-as-a-service-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides architectural guidelines on hosting stable, production-grade Apache Kafka clusters on Kubernetes. Explores state persistence requirements, advanced container network setups, and operational recovery pipelines.
  - **(2020)** [containerjournal.com: Red Hat Platform Brings Kafka Closer to Kubernetes](https://cloudnativenow.com/topics/cloudnativeplatforms/red-hat-platform-brings-kafka-closer-to-kubernetes) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses Strimzi operators on Red Hat OpenShift, evaluating how declaratively defined operators streamline stateful deployments and coordinate safe, automated rolling updates of Kafka nodes on Kubernetes.
### Hybrid Cloud Platforms

#### Anthos Deployments

  - **(2020)** [confluent.fr: Infrastructure Modernization with Google Anthos and Apache Kafka](https://www.confluent.io/fr-fr/blog/modernize-apps-and-infrastructure-with-anthos-confluent-kafka) <span class='md-tag md-tag--warning'>[FRENCH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span> 🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides architectural guidelines for deploying federated Confluent Kafka setups across local datacenters and public Google Cloud regions using Google Anthos configuration models [FRENCH CONTENT].
#### Modernization Strategy

  - **(2021)** [kai-waehner.de: App Modernization and Hybrid Cloud Architectures with Apache Kafka](https://www.kai-waehner.de/blog/2021/03/10/apache-kafka-app-modernization-legacy-hybrid-cloud-native-architecture) 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Examines legacy migration models utilizing Apache Kafka as an integration buffer. Discusses streaming events between on-prem mainframe systems and agile cloud-native microservices with zero downtime.
### Infrastructure as Code IaC

#### Event-Driven Provisioning

  - **(2021)** [daily.dev: Building a fault-tolerant event-driven architecture with Google Cloud, Pulumi and Debezium](https://daily.dev/blog/building-a-fault-tolerant-event-driven-architecture-with-google-cloud-pulumi-and-debezium) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An infrastructure guide detailing the automated configuration of a fault-tolerant event-driven backend. Demonstrates the step-by-step deployment of Google Cloud resources and Debezium instances using Pulumi for stateful, declarative management.
### Serverless Computing

#### Knative Eventing

  - **(2021)** [**piotrminkowski.com: Knative Eventing with Kafka and Quarkus**](https://piotrminkowski.com/2021/03/31/knative-eventing-with-kafka-and-quarkus) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Illustrates the deployment of Knative serverless application endpoints coordinated with Apache Kafka event feeds. Utilizes Quarkus microservices to demonstrate scale-to-zero configurations that adapt automatically to stream ingestion.
## Data Architecture

### Data Lakehouse

#### Iceberg Integration

  - **(2021)** [**debezium.io: Using Debezium to Create a Data Lake with Apache Iceberg**](https://debezium.io/blog/2021/10/20/using-debezium-create-data-lake-with-apache-iceberg) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explains how to feed streaming transaction logs directly into Apache Iceberg storage using Debezium CDC and Kafka Connect. Outlines strategies for supporting dynamic schema evolution and ensuring transactional ACID-level safety on cheap cloud object stores.
### Data Mesh

#### Cloud-Native Platforms

  - **(2021)** [mrpaulandrew.com: BUILDING A DATA MESH ARCHITECTURE IN AZURE – PART 2](https://mrpaulandrew.com/2021/12/22/building-a-data-mesh-architecture-in-azure-part-2) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A platform implementation guide focusing on assembling a production-ready Data Mesh within Microsoft Azure. Explores multi-workspace configurations utilizing Azure Synapse, Azure Purview, and Data Factory within enterprise environments.
#### Domain-Driven Design (1)

  - **(2021)** [towardsdatascience.com: Data Domains and Data Products](https://towardsdatascience.com/data-domains-and-data-products-64cc9d28283e) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on building discrete, discoverable, and governed domain-centric data products. Reviews core responsibilities for product engineering teams and logical boundaries required to achieve seamless interoperability within a Data Mesh.
#### Foundational Principles

  - **(2020)** [==martinfowler.com: Data Mesh Principles and Logical Architecture==](https://martinfowler.com/articles/data-mesh-principles.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The seminal architectural blueprint by Zhamak Dehghani introducing Data Mesh principles. Focuses on the core four pillars: domain-driven decentralized data ownership, data-as-a-product, self-serve data infrastructure platforms, and federated computational governance.
#### Migration Strategies

  - **(2019)** [==martinfowler.com: How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh==](https://martinfowler.com/articles/data-monolith-to-mesh.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The pioneering analysis introducing the Data Mesh framework. Outlines failure modes of traditional centralized databases and enterprise data lakes, presenting a distributed, domain-driven data topology as a scalable alternative.
#### Strategic Overview

  - **(2020)** [infoq.com: Data Mesh Principles and Logical Architecture Defined](https://www.infoq.com/news/2020/12/data-mesh-architecture) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An executive summary analyzing Zhamak Dehghani's foundational Data Mesh concepts. Contemplates the operational and architectural pivot from centralized monolithic data pools to distributed, domain-centric, and governed team landscapes.
### Data Science Platform

#### Real-Time Machine Learning

  - **(2018)** [confluent.io: How to Build and Deploy Scalable Machine Learning in Production with Apache Kafka](https://www.confluent.io/blog/build-deploy-scalable-machine-learning-production-apache-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews the architecture designs required for deploying, evaluating, and monitoring analytical machine learning models against fast event-streams. Utilizes Apache Kafka as the backbone for scalable ingestion.
### Event Streaming (3)

#### Architectural Patterns

  - **(2021)** [davidxiang.com: Kafka As A Database? Yes Or No](https://davidxiang.com/2021/01/10/kafka-as-a-database) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the controversial 'Kafka as a database' design model. Analyzes the trade-offs of using Kafka for data persistence, explaining limits on random queries and index lookups relative to typical relational/NoSQL setups.
#### Audio Curation

  - **(2020)** [**softwareengineeringdaily.com: Kafka Applications with Tim Berglund (podcast) 🌟**](https://softwareengineeringdaily.com/2020/12/16/kafka-applications-with-tim-berglund-repeat) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A podcast conversation detailing real-world patterns for building highly decoupled event-driven systems. Explores streaming architecture choices, data evolution, and microservice communication patterns with Tim Berglund.
#### Cluster Management

  - **(2026)** [==AKHQ (previously known as KafkaHQ) 🌟==](https://github.com/tchiotludo/akhq) <span class='md-tag md-tag--info'>⭐ 3808</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A powerful, feature-rich web console for administering Kafka cluster resources. Supports direct topic data browsing, consumer group rebalancing monitoring, schema registry integrations, and multi-tenant ACL audits.
  - **(2021)** [confluent.io: Simplifying Apache Kafka Multi-Cluster Management Using Control Center and Cluster Registry](https://www.confluent.io/blog/simplify-multiple-kafka-cluster-management-monitoring-using-confluent) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains methods for operating federated or geographically-dispersed Kafka clusters. Details patterns for maintaining centralized visibility and configuring multi-cluster pipelines using Confluent Control Center.
#### Consumer Coordination

  - **(2021)** [blog.cloudera.com: Scalability of Kafka Messaging using Consumer Groups](https://www.cloudera.com/blog.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the scaling behaviors of consumer groups in Apache Kafka. Outlines dynamic partition rebalancing algorithms, protocol designs, and strategies to minimize processing lag in active networks.
#### Data Pipelines

  - **(2019)** [**Single Message Transformations - The Swiss Army Knife of Kafka Connect**](https://www.morling.dev/blog/single-message-transforms-swiss-army-knife-of-kafka-connect) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An deep-dive breakdown of Single Message Transformations (SMTs) within Kafka Connect. Shows how to filter, modify, anonymize, and restructure record payloads on-the-fly without requiring customized stream computing logic.
#### Development Tutorials

  - **(2021)** [==kafka-tutorials.confluent.io 🌟==](https://developer.confluent.io/tutorials) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — The premier tutorial index hosted by Confluent. Provides a rich set of runnable recipes demonstrating microservice streaming actions, temporal joins, window operations, and message transformations using ksqlDB and Kafka Streams.
  - **(2021)** [kafka-tutorials.confluent.io: How to count messages in a Kafka topic](https://developer.confluent.io/confluent-tutorials/count-messages/ksql) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A precise development recipe outlining how to count incoming records inside Apache Kafka topics using ksqlDB. Details the construction of stateful materialized views for monitoring live volumes.
#### Foundational Principles (1)

  - **(2021)** [**Confluent.io: Intro to Apache Kafka: How Kafka Works 🌟**](https://developer.confluent.io/what-is-apache-kafka) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A foundational, highly descriptive reference for Kafka basics. Explains structural layouts of partitions, records, offsets, log retention, and replication, ensuring developers master core broker fundamentals.
#### IoT Telemetry Integration

  - **(2021)** [**kai-waehner.de: Apache Kafka and MQTT (Part 1 of 5) – Overview and Comparison**](https://www.kai-waehner.de/blog/2021/03/15/apache-kafka-mqtt-sparkplug-iot-blog-series-part-1-of-5-overview-comparison) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A systematic deep dive comparing MQTT brokers to Kafka. Reviews how to build end-to-end telemetry systems, deploying MQTT at the edge for lightweight transport and Kafka at the core for analytical streaming.
#### Message Brokers (1)

  - **(2026)** [==Apache Kafka==](https://kafka.apache.org) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The main portal for Apache Kafka, the industry de facto standard distributed event streaming engine. It outlines critical capabilities including partition clustering, transactional controls, offset management, and high-performance ingestion designs.
#### Metadata Management KRaft

  - **(2021)** [devclass.com: Apache Kafka 2.8.0 previews life without ZooKeeper](https://www.devclass.com/databases/2021/04/20/apache-kafka-280-previews-life-without-zookeeper/1627009) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the operational and administrative benefits of ZooKeeper removal. Reviews how KRaft architecture improves cluster limits, simplifies administrator overhead, and accelerates recovery speeds during node failures.
#### Resource Indexes

  - **(2026)** [**Awesome Streaming**](https://github.com/manuzhang/awesome-streaming) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly curated meta-resource listing frameworks, engine architectures, academic publications, and database connectors within the streaming data ecosystem. Covers key analytical and event-driven technologies.
  - **(2026)** [Awesome Kafka](https://github.com/monksy/awesome-kafka/blob/master/tools.md) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A rich community collection of operational utilities, libraries, and GUI packages optimized for developers and administrators deploying and scaling Apache Kafka systems.
#### Video Tutorials

  - **(2020)** [**youtube playlist: Kafka Connect Tutorials | Kafka Connect 101: REST API 🌟**](https://www.youtube.com/watch?v=9wu-j9gIlBY&list=PLa7VYi0yPIH1MB2n2w8pMZguffCDu2L4Y&index=8&ab_channel=Confluent) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An educational video series illustrating the programmatic administration of Kafka Connect connectors. Details the layout of the Connect REST API for creating, validating, scaling, and debugging stateful data integrations.
### Event-Driven Data

#### Change Data Capture CDC (1)

  - **(2021)** [**shopify.engineering: Capturing Every Change From Shopify’s Sharded Monolith**](https://shopify.engineering/capturing-every-change-shopify-sharded-monolith) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — This architectural case study highlights Shopify's high-throughput solution for real-time mutation extraction from sharded MySQL clusters. By combining Debezium with customized Apache Kafka configurations, the system secures sub-second delivery while safely preserving transaction-order invariants at massive scale.
  - **(2020)** [**vladmihalcea.com: A beginner’s guide to CDC (Change Data Capture)**](https://vladmihalcea.com/a-beginners-guide-to-cdc-change-data-capture) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A comprehensive structural overview of Change Data Capture (CDC) design patterns. It details transaction log parsing, dual-writes mitigation, and the key architectural differences between query-based and log-based CDC solutions. This acts as an essential primer for development groups transitioning from monolith DB schemas to real-time event streaming systems.
  - **(2020)** [developers.redhat.com: Capture database changes with Debezium Apache Kafka connectors](https://developers.redhat.com/blog/2020/04/14/capture-database-changes-with-debezium-apache-kafka-connectors) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on manual detailing the implementation of Debezium to safely convert relational database modifications into real-time Kafka event feeds. Outlines event formatting, partition strategy, and recovery procedures.
  - **(2020)** [Build a simple cloud-native change data capture pipeline](https://developers.redhat.com/blog/2020/07/02/build-a-simple-cloud-native-change-data-capture-pipeline) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates how to engineer a low-latency, cloud-native CDC pipeline utilizing Debezium connectors alongside open database architectures. Explores data serialization optimizations and horizontal scale metrics.
#### Compliance Systems

  - **(2018)** [infoq.com: Building a SQL Database Audit System using Kafka, MongoDB and Maxwell's Daemon](https://www.infoq.com/articles/database-audit-system-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines a robust architectural design for database auditing. Uses Maxwell's Daemon to ingest database binlogs, routing changes through Kafka into MongoDB to form a tamper-resistant historical record.
#### Data Federation

  - **(2020)** [Event streaming and data federation: A citizen integrator’s story](https://developers.redhat.com/blog/2020/06/12/event-streaming-and-data-federation-a-citizen-integrators-story) 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Examines low-code patterns for connecting real-time streaming architectures with legacy enterprise databases. Explains how federation tools bridge information gaps between non-technical users and distributed message networks.
#### Debezium Connectors

  - **(2021)** [developers.redhat.com: Db2 and Oracle connectors coming to Debezium 1.4 GA](https://developers.redhat.com/blog/2021/03/25/db2-and-oracle-connectors-coming-to-debezium-1-4-ga) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical release breakdown detailing the production-grade integration of IBM Db2 and Oracle connectors within the Debezium 1.4 ecosystem. It reviews performance benchmarks, log-mining mechanisms, and setup procedures critical for cloud-native enterprise migrations.
### Schema Governance

#### Event-Driven Governance

  - **(2021)** [developers.redhat.com: Event-driven APIs and schema governance for Apache Kafka: Get ready for Kafka Summit Europe 2021](https://developers.redhat.com/blog/2021/05/04/event-driven-apis-and-schema-governance-for-apache-kafka-get-ready-for-kafka-summit-europe-2021) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes key themes of Kafka Summit Europe 2021, detailing patterns in distributed schema governance, central API catalogs, and microservice integration design protocols.
#### Microservices Design Patterns

  - **(2021)** [redhat.com: Using a schema registry to ensure data consistency between microservices](https://www.redhat.com/en/blog/schema-registry) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the operational role of schema registries in maintaining system stability. Highlights how decoupled producers and consumers leverage registries for backward and forward schema compatibility, protecting distributed microservices from payload parsing errors.
#### Service Registry

  - **(2026)** [****Apicurio** Registry**](https://github.com/apicurio/apicurio-registry) <span class='md-tag md-tag--info'>⭐ 806</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Apicurio Registry is a high-performance, open-source centralized schema registry. It enables teams to maintain and store OpenAPI, AsyncAPI, Avro, Protobuf, and JSON schemas, supporting real-time validation layers in high-throughput microservice pipelines.
  - **(2019)** [Red Hat Integration service registry](https://developers.redhat.com/blog/2019/12/16/getting-started-with-red-hat-integration-service-registry) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory architecture guide describing the capabilities of the Red Hat Integration Service Registry. Reviews standard patterns for managing API schemas (Avro, JSON Schema, Protobuf) to guarantee strong message-contract enforcement in decoupled broker networks.
### Stream Processing

#### Evolutionary Topologies

  - **(2020)** [thenewstack.io: Part 1: The Evolution of Data Pipeline Architecture](https://thenewstack.io/part-1-the-evolution-of-data-pipeline-architecture) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Traces the structural progress of big data analytics pipelines. Focuses on the architectural evolution from high-latency batch map-reduce jobs to real-time Kappa and Lambda messaging topologies.
#### Managed Pipelines

  - **(2021)** [cloudblog.withgoogle.com: Turn any Dataflow pipeline into a reusable template](https://cloud.google.com/blog/products/data-analytics/create-templates-from-any-dataflow-pipeline) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical look at creating and managing GCP Dataflow templates. Details packaging patterns that permit modular, parameter-driven run execution of streaming data pipelines across multi-tenant infrastructures.
#### Microservices Frameworks

  - **(2020)** [Build a data streaming pipeline using Kafka Streams and Quarkus](https://developers.redhat.com/blog/2020/09/28/build-a-data-streaming-pipeline-using-kafka-streams-and-quarkus) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates the construction of microsecond-responsive streams using the Kafka Streams API paired with Quarkus. Explores native execution compilation patterns to reduce JVM memory overhead and launch latency.
## Data Engineering

### Change Data Capture CDC (2)

#### Cloud Managed Services (2)

  - **(2020)** [**debezium.io: Lessons Learned from Running Debezium with PostgreSQL on Amazon RDS**](https://debezium.io/blog/2020/02/25/lessons-learned-running-debezium-with-postgresql-on-rds) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly valuable technical case study sharing performance profiles, optimization constraints, and gotchas when operating Debezium alongside Amazon RDS PostgreSQL. It details replication slot configurations, WAL storage management, and handling heavy transaction volumes under AWS limitations.
#### PostgreSQL

  - **(2021)** [**info.crunchydata.com: PostgreSQL Change Data Capture With Debezium**](https://www.crunchydata.com/blog/postgresql-change-data-capture-with-debezium) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive operational manual focused on establishing Debezium CDC connectors specifically for enterprise-grade PostgreSQL deployments. It details WAL level adjustments, logical replication slot configuration, and the extraction of mutation events for consumer engines.
#### Real-Time Data Streaming

  - **(2026)** [==**Debezium**:==](https://debezium.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The industry-leading, open-source distributed platform for Change Data Capture (CDC). Built on top of Apache Kafka, it taps database transaction logs in real-time, streaming row-level mutations downstream without querying databases. Essential for low-latency event-driven microservices.
#### Stream Processing (1)

  - **(2021)** [**noti.st: Change Data Capture with Flink SQL and Debezium 🌟**](https://noti.st/morsapaes/liQzgs/change-data-capture-with-flink-sql-and-debezium) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A visual presentation sharing architectural strategies to integrate Debezium with Apache Flink SQL for high-speed continuous stream processing. Explains patterns for building real-time materialized views, continuous aggregations, and live analytics directly from database mutation logs.
### Data Culture

#### Real-Time Data Streaming (1)

  - **(2021)** [linkedin.com: How to Move From a “Wait for it...” Batch-Processing Culture to a “Get It Now” Real-Time Data Culture](https://www.linkedin.com/pulse/how-move-from-wait-batch-processing-culture-get-now-tomsen-bukovec) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Discusses the cultural and systemic paradigm shift required for enterprises moving from batch scheduling to real-time event-driven insights. It touches on organizational friction, architectural changes, and immediate business advantages. It serves as a non-technical strategic guide for data transformation.
### Data Pipelines (1)

#### Cloud Native Architectures

  - **(2020)** [towardsdatascience.com: Architecture for High-Throughput Low-Latency Big Data Pipeline on Cloud 🌟](https://towardsdatascience.com/scalable-efficient-big-data-analytics-machine-learning-pipeline-architecture-on-cloud-4d59efc092b5) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Evaluates design principles for high-throughput, low-latency cloud-native big data architectures. The guide details how to integrate ingestion layers with stream processing engines and distributed analytical databases. It presents structured architectural templates for unified analytical and machine learning workloads.
### Data on Kubernetes

#### Orchestration (1)

  - **(2021)** [thenewstack.io: The Path to Getting the Full Data Stack on Kubernetes](https://thenewstack.io/the-path-to-getting-the-full-data-stack-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explores the evolutionary path of running complex, stateful database and data streaming systems natively on Kubernetes. It addresses the maturity of operators, storage classes, and orchestrators that facilitate the deployment of the complete data pipeline. The article details challenges regarding resource management and high availability.
### Real-Time Data Streaming (2)

#### Data Stack

  - **(2022)** [thenewstack.io: Streaming Data and the Modern Real-Time Data Stack](https://thenewstack.io/streaming-data-and-the-modern-real-time-data-stack) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Discusses the components constituting the modern real-time data stack, emphasizing continuous streaming over traditional batch ETL. It explores the roles of message logs, stream processors, and real-time OLAP databases. This provides a blueprint for engineering low-latency analytics systems.
#### Foundations (2)

  - **(2022)** [thenewstack.io: How to Get Started with Data Streaming](https://thenewstack.io/how-to-get-started-with-data-streaming) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A beginner-to-intermediate guide outlining initial workflows for setting up real-time stream ingestion and processing pipelines. It reviews primary tooling such as Apache Kafka and Apache Flink. It offers guidance on mapping traditional batch datasets into real-time pipelines.
## Data Infrastructure

### Data Architecture (1)

#### Data as a Service

##### Integrations

  - **(2020)** [**mongodb.com: DaaS with MongoDB and Confluent**](https://www.mongodb.com/company/blog/technical/daa-s-with-mongo-db-and-confluent) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An architecture case study exploring how to design a modern Data-as-a-Service (DaaS) paradigm using MongoDB and Confluent. Focuses on real-time CDC synchronization mechanisms and state persistence across high-throughput microservices.
### Event Streaming (4)

#### Apache Kafka

##### Enterprise Distribution

  - **(2026)** [==confluent.io==](https://www.confluent.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The enterprise cloud-native streaming data platform built on top of Apache Kafka. Confluent provides fully managed SaaS offerings, enterprise schema management, cloud-to-local replication, and declarative connectors for data warehouses.
##### Integrations (1)

  - **(2021)** [strimzi.io: Using HTTP Bridge as a Kubernetes sidecar](https://strimzi.io/blog/2021/08/18/using-http-bridge-as-a-kubernetes-sidecar) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exploration of deploy-time design patterns using the Strimzi HTTP Bridge as a Kubernetes sidecar container. This integration simplifies microservices communications by providing standard HTTP REST endpoints to interact with underlying Kafka event-driven pipelines.
##### Management Tools

  - **(2026)** [==conduktor.io 🌟==](https://www.conduktor.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An enterprise-grade desktop and cloud management platform for Apache Kafka that simplifies queue monitoring, schema registry auditing, and multi-cluster testing. It features advanced user security, performance monitoring, and message generation tools.
##### Monitoring

  - **(2021)** [strimzi/strimzi-canary](https://github.com/strimzi/strimzi-canary) <span class='md-tag md-tag--info'>⭐ 42</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deployment-ready diagnostic tool that acts as a canary monitor within Kafka clusters. It helps ops teams measure round-trip message latency, validation success, and consumer group responsiveness under realistic workloads.
  - **(2020)** [confluent.io: Monitoring Your Event Streams: Integrating Confluent with Prometheus and Grafana](https://www.confluent.io/blog/monitor-kafka-clusters-with-prometheus-grafana-and-confluent) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A guide showing how to set up robust monitoring patterns for Apache Kafka cluster metrics using Prometheus and Grafana. Details exact exporter configurations and provides ready-to-use visualizations of critical performance telemetry.
##### Operators

  - **(2024)** [**Banzai Kafka Operator**](https://github.com/banzaicloud/koperator) <span class='md-tag md-tag--info'>⭐ 792</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The Banzai Cloud Koperator simplifies Apache Kafka operations on top of Kubernetes clusters. It implements granular auto-scaling, Cruise Control-assisted broker load rebalancing, and self-healing systems directly within the cluster scheduler.
##### Security (1)

  - **(2020)** [**strimzi.io: Using Open Policy Agent with Strimzi and Apache Kafka**](https://strimzi.io/blog/2020/08/05/using-open-policy-agent-with-strimzi-and-apache-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A detailed security-focused guide illustrating the integration of Open Policy Agent (OPA) with Strimzi and Apache Kafka. Explains how to enforce centralized, declarative, and fine-grained access control policies across streaming clusters.
##### Strimzi Operators

  - **(2022)** [strimzi/kafka-kubernetes-config-provider: Kubernetes Configuration Provider for Apache Kafka](https://github.com/strimzi/kafka-kubernetes-config-provider) <span class='md-tag md-tag--info'>⭐ 30</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized Kubernetes configuration provider for Apache Kafka that enables Kafka applications to read configuration data dynamically from Kubernetes Secrets and ConfigMaps. It simplifies the secure mounting of TLS certificates and broker credentials directly in client workloads.
  - **(2020)** [blog.jromanmartin.io: How to upgrade Strimzi Operator using the CLI](https://blog.jromanmartin.io/2020/09/25/how-upgrade-strimzi-operator.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a practical, command-line step-by-step procedure to upgrade Strimzi Operator versions on live Kubernetes/OpenShift clusters while avoiding message pipeline downtime.
  - **(2021)** [strimzi.io: Using Kubernetes Configuration Provider to load data from Secrets and Config Maps](https://strimzi.io/blog/2021/07/22/using-kubernetes-config-provider-to-load-data-from-secrets-and-config-maps) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This blog post details the implementation of the Strimzi Kubernetes Config Provider. It demonstrates how to decouple configurations from code by directly mapping Kafka properties to Kubernetes-managed infrastructure configurations.
#### Architectural Patterns (1)

##### Comparisons

  - **(2021)** [softkraft.co: WS Kinesis vs Kafka comparison: Which is right for you? 🌟](https://www.softkraft.co/aws-kinesis-vs-kafka-comparison) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An objective comparative analysis contrasting Amazon Kinesis and Apache Kafka across parameters like performance, architecture, pricing, and infrastructure overhead. Helps architects select the ideal event engine for specific scaling targets.
  - **(2020)** [Pulsar vs Kafka – Comparison and Myths Explored](https://www.kai-waehner.de/blog/2020/06/09/apache-kafka-versus-apache-pulsar-event-streaming-comparison-features-myths-explored) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed technical breakdown comparing Apache Kafka and Apache Pulsar. Evaluates performance benchmarks, architecture complexities, replication topologies, and real-world deployment challenges.
#### Business Ecosystem

##### Partnerships

  - **(2021)** [confluent.io: Confluent and Microsoft Announce Strategic Alliance](https://www.confluent.io/blog/latest-partner-ecosystem) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of the strategic alignment between Microsoft and Confluent. Describes integrations for native resource provisioning, unified billing portals, and security optimizations within the Azure cloud environment.
#### Cloud-Native Streaming

##### AWS

  - **(2026)** [==AWS Kinesis==](https://docs.aws.amazon.com/kinesis) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official AWS documentation for Kinesis Data Streams. Highly resilient, fully managed cloud service for real-time data streaming at scale, designed for seamless integrations within the AWS ecosystem and serverless application designs.
#### Modern Alternatives

##### Apache Pulsar

  - **(2026)** [==Apache Pulsar==](https://pulsar.apache.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A highly scalable cloud-native event streaming model that separates compute (Apache Pulsar brokers) from state/storage (Apache BookKeeper). Ideal for multi-tenant, geographically distributed messaging workloads that require decoupled horizontal scaling.
##### Interviews

  - **(2021)** [**softwareengineeringdaily.com: Redpanda: Kafka Alternative with Alexander Gallego 🌟**](https://softwareengineeringdaily.com/2021/01/22/redpanda-kafka-alternative-with-alexander-gallego) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An analytical podcast interview featuring Redpanda founder Alexander Gallego. Delves into the C++ implementation details, thread-per-core architectures, and the structural decisions that differentiate Redpanda from JVM-based event processors.
##### Licensing

  - **(2021)** [Redpanda is now Free & Source Available](https://www.redpanda.com/blog/bsl-source-available-license) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official blog post detailing Redpanda's pivot to the Business Source License (BSL). It provides a high-level corporate and architectural perspective regarding license changes and global open-source resource sustainability.
##### Redpanda

  - **(2026)** [==Redpanda 🌟==](https://www.redpanda.com) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An ultra-fast, C++ based, Seastar engine implementation of Kafka API protocols. Redpanda acts as a direct, lightweight replacement for Apache Kafka that removes heavy JVM tuning and ZooKeeper/KRaft runtimes, significantly lowering hardware footprints.
#### Red Hat AMQ Streams

##### Components

  - **(2019)** [Understanding Red Hat AMQ Streams components for OpenShift and Kubernetes 🌟](https://developers.redhat.com/blog/2019/12/04/understanding-red-hat-amq-streams-components-for-openshift-and-kubernetes-part-1) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part 1 of an analytical breakdown detailing the components of Red Hat AMQ Streams (built on Strimzi). Explains operators, ZooKeeper configurations, and Kafka broker deployment patterns within enterprise Kubernetes clusters.
##### Security (2)

  - **(2020)** [Set up **Red Hat AMQ Streams** custom certificates on OpenShift](https://developers.redhat.com/blog/2020/04/01/set-up-red-hat-amq-streams-custom-certificates-on-openshift-update) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates replacing auto-generated certificates with custom enterprise CA certs to implement secured TLS and mTLS configurations inside Strimzi-managed AMQ Streams.
##### Slides

  - **(2020)** [speakerdeck.com: Apache Kafka with Red Hat AMQ Streams 🌟](https://speakerdeck.com/mabulgu/apache-kafka-with-red-hat-amq-streams) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An informative slide presentation charting Apache Kafka deployments on OpenShift via Red Hat AMQ Streams. Visualizes operator behaviors and declarative infrastructure patterns.
### In-Memory Computing

#### Distributed Compute

##### Hazelcast

  - **(2021)** [devops.com: Hazelcast Simplifies Streaming for Extremely Fast Event Processing in IoT, Edge and Cloud Environments](https://devops.com/hazelcast-simplifies-streaming-for-extremely-fast-event-processing-in-iot-edge-and-cloud-environments) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This article highlights Hazelcast's integration of stream processing and in-memory data store capabilities. Focuses on low-latency streaming applications for edge environments, high-throughput IoT networks, and real-time analytical portals.
### IoT Messaging

#### Mosquitto

##### OpenShift

  - **(2021)** [developers.redhat.com: Deploying the Mosquitto MQTT message broker on Red Hat OpenShift, Part 1](https://developers.redhat.com/blog/2021/04/16/deploying-the-mosquitto-mqtt-message-broker-on-red-hat-openshift-part-1) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A developer-focused walkthrough on deploying Eclipse Mosquitto, an open-source MQTT message broker, onto Red Hat OpenShift. Ideal for scaling lightweight telemetry components adjacent to containerized enterprise layers.
#### Protocols

##### MQTT

  - **(2026)** [==mqtt.org==](https://mqtt.org) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The main specification portal for MQTT, an ISO standard lightweight publish-subscribe network protocol. Widely adopted for edge environments, remote telemetry, and machine-to-machine integrations requiring minimal memory footprint and network load.
### Message Brokers (2)

#### ActiveMQ

##### Artemis

  - **(2026)** [==Apache ActiveMQ Artemis broker==](https://artemis.apache.org/components/artemis) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Apache ActiveMQ Artemis provides a non-blocking, multi-protocol, highly performant asynchronous message broker designed for enterprise messaging. It supports advanced queue architectures, JMS/AMQP protocols, and cloud cluster deployments.
##### High Availability (1)

  - **(2017)** [developers.redhat.com: JDBC Master-Slave Persistence setup with Activemq using Postgresql database](https://developers.redhat.com/blog/2017/10/05/jdbc-master-slave-persistence-setup-activemq-using-postgresql-database) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides system administrators through building a JDBC Master-Slave active/passive high-availability messaging layer in ActiveMQ backed by a PostgreSQL cluster.
#### Enterprise Middleware

##### Red Hat AMQ

  - **(2026)** [**Red Hat AMQ**](https://www.redhat.com/en/technologies/jboss-middleware/amq) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official product home of Red Hat AMQ, an enterprise-grade messaging suite. Delivers highly-available JMS, AMQP, and MQTT engines along with robust Strimzi Kafka integration for complex enterprise data layers.
#### Red Hat AMQ (1)

##### OpenShift Routing

  - **(2020)** [developers.redhat.com: Connecting external clients to Red Hat AMQ Broker on Red Hat OpenShift](https://developers.redhat.com/blog/2020/08/26/connecting-external-clients-to-red-hat-amq-broker-on-red-hat-openshift) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A walkthrough explaining how to securely configure ingress and network protocols to route client applications external to OpenShift directly into containerized AMQ brokers.
### Message Queues

#### Alternative Architectures

##### PostgreSQL (1)

  - **(2021)** [dagster.io: Postgres: a better message queue than Kafka?](https://dagster.io/blog/skip-kafka-use-postgres-message-queue) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural exploration evaluating the use of PostgreSQL as a highly concurrent transactional queue using `FOR UPDATE SKIP LOCKED`. Suggests a lightweight operational alternative to Apache Kafka for low-to-medium scale applications.
### Stream Processing (2)

#### Architectural Patterns (2)

##### Comparisons (1)

  - **(2025)** [**Kafka Streams and ksqlDB Compared – How to Choose**](https://docs.confluent.io/platform/current/streams/overview.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An extensive comparison guide from Confluent mapping out when to use the lightweight Kafka Streams Java client library versus ksqlDB database abstraction layers. Analyzes development environments, deployment scales, and infrastructure constraints.
#### Distributed Processing

##### Apache Flink

  - **(2026)** [==Apache Flink==](https://flink.apache.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A highly performant distributed processing framework designed for stateful stream processing over bounded and unbounded data structures. Features sub-millisecond execution latencies and robust exactly-once transaction guarantees.
##### Kubernetes Native (1)

  - **(2021)** [**flink.apache.org: How to natively deploy Flink on Kubernetes with High-Availability (HA)**](https://flink.apache.org/2021/02/10/native-k8s-with-ha.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides architectural guidelines on natively deploying Apache Flink on Kubernetes clusters with robust High Availability (HA) configurations. Covers resource scheduling, Zookeeper integrations, and Kubernetes-native active scaling strategies.
#### SQL Engines

##### ksqlDB

  - **(2026)** [**ksqlDB**](https://www.confluent.io/product/ksqldb) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official product home of ksqlDB, an event-streaming database tailored to construct stream-processing platforms on top of Apache Kafka. Translates complex Java/Scala stream pipelines into standard SQL definitions.
## Data Platform

### Customer Data

#### iPaaS

  - **(2026)** [**rudderstack.com iPaaS**](https://www.rudderstack.com) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An enterprise-grade Customer Data Platform (CDP) designed specifically for developers, serving as a specialized iPaaS for telemetry and event streaming.

*   Built to run securely on top of existing cloud data warehouses (Snowflake, BigQuery).
*   Enables real-time event routing, transformation, and identity resolution with strict privacy controls.
### Data Engineering (1)

#### Event Streaming (5)

  - **(2018)** [==O'Really: Streaming data==](http://streamingsystems.net) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The definitive conceptual companion to the Apache Beam and Google Cloud Dataflow models of stream processing.

*   Details critical patterns of out-of-order data handling.
*   Explains event-time vs. processing-time, windowing, and triggering paradigms crucial for building resilient stream processing pipelines.
## Data and Databases

### Stream Processing (3)

#### Streaming Databases

  - **(2020)** [thenewstack.io: The Rise of the Event Streaming Database 🌟](https://thenewstack.io/the-rise-of-the-event-streaming-database) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical piece exploring the convergence of databases and stream processing systems to create unified event-streaming databases. It addresses how modern architectures require real-time log computation. Grounding tracks its evolution toward modern systems like ksqlDB and Materialize.
## Event-Driven Architecture

### API Management

#### Schema Governance (1)

  - **(2021)** [**developers.redhat.com: Managing the API life cycle in an event-driven architecture: A practical approach 🌟**](https://developers.redhat.com/articles/2021/07/07/managing-api-life-cycle-event-driven-architecture-practical-approach) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Best practices on governing async APIs and schema definitions inside microservice ecosystems. Live Grounding: Focuses on AsyncAPI specifications, Schema Registry integration, and decoupling publisher/consumer evolution paths to ensure backward compatibility and operational maturity.
### Apache Kafka (1)

#### Architecture Evolution

  - **(2021)** [confluent.io: Apache Kafka Made Simple: A First Glimpse of a Kafka Without ZooKeeper](https://www.confluent.io/blog/latest-apache-kafka-release) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Announcement and architectural breakdown of Kafka's transition away from ZooKeeper in favor of KRaft (Kafka Raft metadata mode). Live Grounding: Discusses the architectural simplification, metadata scalability improvements, and decreased operational footprint of removing the external ZooKeeper dependency.
#### Fundamentals

  - **(2022)** [**freecodecamp.org: The Apache Kafka Handbook – How to Get Started Using Kafka 🌟**](https://www.freecodecamp.org/news/apache-kafka-handbook) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Comprehensive handbook targeting developers getting started with event streams. Live Grounding: Explains underlying storage patterns, consumers, producers, and practical command-line exercises, making it an excellent onboarding guide.
  - **(2021)** [gentlydownthe.stream](https://www.gentlydownthe.stream)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A highly acclaimed visual, interactive introduction to Apache Kafka and stream processing. Live Grounding: Leverages hand-drawn diagrams and narrative storytelling to explain complex streaming concepts such as replication, consumer offsets, and transaction semantics in an exceptionally digestible manner.
#### Learning Resources

  - [==developer.confluent.io 🌟🌟==](https://developer.confluent.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Confluent's central education portal containing exhaustive learning paths for Apache Kafka. Live Grounding: Houses premium-grade technical videos, tutorials, sample applications, and comprehensive courses covering stream processing, Kafka streams, and event-driven architecture patterns.
  - [==conduktor.io/kafka: Learn Apache Kafka like never before==](https://docs.conduktor.io/learn) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Conduktor's comprehensive learning catalog targeting advanced Kafka operations. Live Grounding: Step-by-step guides covering schema evolution, security architectures (SASL/mTLS), custom interceptors, and stream processing with Kafka Streams and ksqlDB.
#### Local Development (2)

  - **(2024)** [**github.com/lensesio/fast-data-dev (Lenses Box)**](https://github.com/lensesio/fast-data-dev) <span class='md-tag md-tag--info'>⭐ 2079</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Highly popular, all-in-one Docker image comprising Kafka, ZooKeeper, Schema Registry, and REST Proxy. Live Grounding: Excellent for local developer validation and integration pipelines needing a pre-wired, enterprise-ready playground instance.
#### Performance Optimization

  - **(2021)** [**newrelic.com: Effective Strategies for Kafka Topic Partitioning 🌟**](https://newrelic.com/blog/observability/effective-strategies-kafka-topic-partitioning) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Deep-dive tutorial on optimizing Kafka throughput via smart partitioning schemes. Live Grounding: Analyzes consumer group balancing, message ordering requirements, and custom partitioning algorithms. Provides architectural guidelines for sizing partition counts to balance throughput and rebalance overhead.
#### Performance Testing

  - **(2023)** [KLoadGen - Kafka + (Avro/Json Schema) Load Generator 🌟](https://github.com/sngular/kloadgen) <span class='md-tag md-tag--info'>⭐ 218</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Purpose-built CLI and tool to simulate heavy load scenarios utilizing Schemas. Live Grounding: Streamlines load testing of schema-validated topics by generating synthetic Avro or JSON messages at target event rates.
#### Tooling and UI (1)

  - **(2026)** [==Kafdrop – Kafka Web UI 🌟==](https://github.com/obsidiandynamics/kafdrop) <span class='md-tag md-tag--info'>⭐ 6135</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Highly popular, lightweight web UI for monitoring and managing Apache Kafka. Live Grounding: Renders cluster info, brokers, topics, partition offsets, consumer group lag, and allows active JSON/protobuf message payload inspection.
  - **(2026)** [==redpanda-data/kowl==](https://github.com/redpanda-data/console) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Excellent web UI (now Redpanda Console) designed for debugging and exploring event streams. Live Grounding: Outstanding user experience presenting topology, schema registry mapping, consumer tracking, and high-performance message search.
  - **(2024)** [**github.com/sauljabin/kaskade**](https://github.com/sauljabin/kaskade) <span class='md-tag md-tag--info'>⭐ 1013</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Modern Terminal User Interface (TUI) client for Apache Kafka. Live Grounding: Employs an elegant console layout allowing engineering teams to navigate topics, inspect raw schema properties, and watch streaming events dynamically right from the terminal.
  - **(2021)** [**dev.to: Learn how to use Kafkacat – the most versatile Kafka CLI client 🌟**](https://dev.to/de_maric/learn-how-to-use-kafkacat-the-most-versatile-kafka-cli-client-1kb4) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Guide to Kafkacat (now rebranded as kcat), the developer's favorite Swiss Army knife CLI. Live Grounding: Walks through real-world piping, consuming from dynamic offsets, producing raw file contents, and query configurations using the command line.
  - **(2021)** [towardsdatascience.com: Overview of UI Tools for Monitoring and Management of Apache Kafka Clusters](https://towardsdatascience.com/overview-of-ui-tools-for-monitoring-and-management-of-apache-kafka-clusters-8c383f897e80)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Comparative review of leading open-source and commercial administration portals for Kafka. Live Grounding: Compares visual management capabilities, schema registration support, and partition offset visualization across tools like AKHQ, Kafdrop, and Lenses.
### Application Integration (2)

#### Java Spring Boot

  - **(2023)** [piotrminkowski.com: Concurrency with Kafka and Spring Boot](https://piotrminkowski.com/2023/04/30/concurrency-with-kafka-and-spring-boot)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Optimization guide for Spring Boot engineers processing high-throughput event logs. Live Grounding: Examines concurrent message listener configurations, partition distribution strategies, and thread-safe processing to fully maximize JVM resources.
### Architectural Evaluation

#### Anti-Patterns

  - **(2022)** [==kai-waehner.de: When NOT to use Apache Kafka?==](https://www.kai-waehner.de/blog/2022/01/04/when-not-to-use-apache-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Essential architectural review pointing out Kafka anti-patterns. Live Grounding: Evaluates hard constraints of Kafka, comparing it against traditional message queues (RabbitMQ), data warehouses, and API gateways. Ideal for teams auditing if Kafka is the appropriate fit.
### Architectural Patterns (3)

#### Resiliency

  - **(2021)** [developers.redhat.com: Building resilient event-driven architectures with Apache Kafka](https://developers.redhat.com/blog/2021/05/05/building-resilient-event-driven-architectures-with-apache-kafka)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: A practical guide from Red Hat engineers on building resilient EDA systems using Kafka. Live Grounding: Explains foundational patterns such as retries, dead-letter queues (DLQ), and stateful stream processing to prevent message loss and maintain system availability during downstream failures.
### Disaster Recovery

#### High Availability (2)

  - **(2021)** [tech.ebayinc.com: Resiliency and Disaster Recovery with Kafka](https://innovation.ebayinc.com/stories/resiliency-and-disaster-recovery-with-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Real-world operational strategies for disaster recovery from eBay's engineering team. Live Grounding: Focuses on multi-region active-passive and active-active Kafka setups, addressing replication lag, mirror maker configurations, and failover automation challenges at extreme scale.
### Integration Patterns

#### Transactional Outbox

  - **(2021)** [**developers.redhat.com: The outbox pattern with Apache Kafka and Debezium 🌟**](https://developers.redhat.com/articles/2021/09/01/outbox-pattern-apache-kafka-and-debezium) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Deep technical analysis of resolving dual-write problems using CDC and the Outbox Pattern. Live Grounding: Uses Debezium and Apache Kafka to stream database transaction events reliably, ensuring strict eventual consistency across decoupled microservices without 2PC overhead.
### Multi-Cluster Strategy

#### Governance

  - **(2022)** [developers.redhat.com: Which is better: A single Kafka cluster to rule them all, or many?](https://developers.redhat.com/articles/2022/03/10/which-better-single-kafka-cluster-rule-them-all-or-many#) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Comparative design analysis evaluating consolidated vs. decentralized cluster strategies. Live Grounding: Evaluates multi-tenancy, risk blast radius, organizational boundaries, billing allocation, and schema maintenance overhead across both topological models.
### Performance Optimization (1)

#### Architectural Patterns (4)

  - **(2022)** [**redhat.com: How we use Apache Kafka to improve event-driven architecture performance**](https://www.redhat.com/en/blog/apache-kafka-EDA-performance) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: Analysis of leveraging Kafka's performance characteristics within complex corporate environments. Live Grounding: Covers tuning throughput and reducing processing latency in microservices by optimization of batch sizes, compression parameters, and consumer allocation.
#### Broker Operations

  - **(2021)** [**strimzi.io: Optimizing Kafka consumers 🌟**](https://strimzi.io/blog/2021/01/07/consumer-tuning) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight: In-depth study on maximizing consumer ingestion performance. Live Grounding: Analyzes consumer fetch sizes, commit mechanisms, partition assignments, and session timeout options to prevent unneeded offset rebalancing in enterprise settings.
  - **(2020)** [strimzi.io: Optimizing Kafka producers](https://strimzi.io/blog/2020/10/15/producer-tuning)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Diagnostic guide to fine-tuning publisher performance. Live Grounding: Explains structural impacts of compression types (lz4, zstd), batch.size configurations, linger.ms, and broker request limits on latency and message pipeline delivery.
### Scale Operations

#### Automation

  - **(2021)** [slack.engineering: Building Self-driving Kafka clusters using open source components](https://slack.engineering/building-self-driving-kafka-clusters-using-open-source-components) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Insightful deep dive from Slack engineers on automating cluster maintenance. Live Grounding: Analyzes their usage of LinkedIn's Cruise Control to automate cluster balancing, partition reassignment, and self-healing under heavy operational scaling pressures.
#### Case Studies

  - **(2022)** [thenewstack.io: LinkedIn Layered Architecture Minimizes Kafka Scaling Issues](https://thenewstack.io/linkedin-layered-architecture-minimizes-kafka-scaling-issues) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Case study detailing how LinkedIn redesigned their backend streaming pipeline layers. Live Grounding: Explains how a layered model decouples the client APIs from physical clusters, mitigating client-induced connection bloat and simplifying routing management.
  - **(2021)** [analyticsindiamag.com: How Uber is Leveraging Apache Kafka For More Than 300 Micro Services](https://analyticsindiamag.com/how-uber-is-leveraging-apache-kafka-for-more-than-300-micro-services) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: High-level overview of Uber's multi-cluster global event bus setup. Live Grounding: Discusses operating trillions of daily messages over 300+ microservices, highlighting custom proxying layers, dead-letter routing structures, and regional backpressure mitigation strategies.
### Schema Governance (2)

#### Security (3)

  - **(2021)** [developers.redhat.com: How to secure Apache Kafka schemas with Red Hat Integration Service Registry 2.0](https://developers.redhat.com/articles/2021/07/16/how-secure-apache-kafka-schemas-red-hat-integration-service-registry-20) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Security-focused guide for configuring and shielding the API schema registry. Live Grounding: Details RBAC integration, TLS communication, and schema evolution restrictions using Red Hat Integration Service Registry 2.0 (based on Apicurio Registry) to protect message payloads.
### Security (4)

#### Data Compliance

  - **(2022)** [developers.redhat.com: End-to-end field-level encryption for Apache Kafka Connect](https://developers.redhat.com/articles/2022/09/27/end-end-field-level-encryption-apache-kafka-connect) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Security implementation guide on field-level crypto for data pipelines. Live Grounding: Addresses PCI/GDPR requirements by demonstrating Cryptographic SMTs (Simple Message Transforms) within Kafka Connect, ensuring data is encrypted before hitting log segments.
#### Kafka Connect

  - **(2020)** [developers.redhat.com: Using secrets in Kafka Connect configuration](https://developers.redhat.com/blog/2020/02/14/using-secrets-in-apache-kafka-connect-configuration)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Security patterns for avoiding plain-text secrets inside Kafka Connect configurations. Live Grounding: Outlines setting up native SecretProviders (such as directory or file-based providers) inside properties files to map dynamic environment secrets securely.
#### Zero Trust

  - **(2022)** [engineering.grab.com: Zero trust with Kafka](https://engineering.grab.com/zero-trust-with-kafka) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Production study from Grab's engineering team on implementing zero-trust network boundaries for messaging. Live Grounding: Covers mutual TLS (mTLS) for broker-client transport, fine-grained ACL authorization, and automating credential lifecycle rotation.
## Observability

### Monitoring (1)

#### Grafana Integration

  - **(2021)** [grafana.com: Get comprehensive monitoring for your Apache Kafka ecosystem instances quickly with Grafana Cloud](https://grafana.com/blog/2021/07/26/get-comprehensive-monitoring-for-your-apache-kafka-ecosystem-instances-quickly-with-grafana-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Overview of cloud-managed observability templates for Kafka. Live Grounding: Details the installation of preconfigured Grafana dashboards targeting JVM metrics, consumer group lag, broker performance, and broker/under-replicated partition alerts.
#### Performance Metrics

  - **(2021)** [datadoghq.com: Monitoring Kafka performance metrics](https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: The gold-standard diagnostic reference for key Kafka metrics. Live Grounding: Breaks down critical under-replicated partition counts, active controller counts, consumer lag, and I/O network thread usage, offering concrete troubleshooting actions for operational stability.
## Orchestration and Workflow

### BPMN Orchestration

#### Architectural Patterns (5)

##### Comparisons (2)

  - **(2019)** [infoq.com: Event Streams and Workflow Engines – Kafka and Zeebe 🌟](https://www.infoq.com/news/2019/05/kafka-zeebe-streams-workflows) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses integrating Apache Kafka's distributed streaming logs with Zeebe's stateful workflow management. Analyzes patterns to maintain reliable, long-running saga transactions across microservices.
#### Zeebe

##### Camunda

  - **(2026)** [**Zeebe workflow engine**](https://camunda.com/platform/zeebe) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Camunda's cloud-native workflow engine, Zeebe. Built specifically to orchestrate distributed microservices, Zeebe parses BPMN 2.0 structures and implements high-throughput, horizontally scalable state machines directly on top of Kubernetes.
### Data Pipelines (2)

#### Apache Airflow

##### Advanced Patterns

  - **(2025)** [**docs.astronomer.io: Dynamically generating DAGs in Airflow**](https://www.astronomer.io/docs/learn/dynamically-generating-dags) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Technical documentation illustrating design patterns to construct dynamically generated DAG pipelines in Apache Airflow. Covers generation templates, dynamic parameters, and runtime optimization.
##### Architecture

  - **(2020)** [towardsdatascience.com: Apache Airflow Architecture 🌟](https://towardsdatascience.com/apache-airflow-architecture-496b9cb28288) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured architectural deep dive explaining how Apache Airflow schedules and executes pipelines. Outlines relationships between scheduler loops, state synchronization databases, and executors.
##### Basics

  - **(2021)** [dev.to: Get started with Apache Airflow](https://dev.to/arunkc/get-started-with-apache-airflow-1218) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step introduction to Apache Airflow design patterns. Covers the core orchestration concepts including DAG definitions, basic Python operators, scheduler parameters, and task execution workflows.
##### Configuration

  - **(2024)** [airflow.apache.org: Add Owner Links to DAG](https://airflow.apache.org/docs/apache-airflow/stable/howto/add-owner-links.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide showing how to map ownership contacts, support channels, and documentation links to pipeline owners within Airflow dashboards for rapid operations management.
##### Deployments (1)

  - **(2026)** [==Apache Airflow official helm chart 🌟==](https://airflow.apache.org/docs/helm-chart) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Apache Airflow community Helm Chart. Provides pre-configured, modular, and enterprise-hardened templates for deploying schedulers, webservers, worker nodes, and scalable Celery or Kubernetes executors.
  - **(2021)** [youtube: Airflow Helm Chart : Quick Start For Beginners in 10mins](https://www.youtube.com/watch?v=GDOw8ByzMyY&ab_channel=MarcLamberti) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A concise introductory video training illustrating how to deploy Apache Airflow quickly using standard Helm commands. Walks through default configurations, worker provisioning, and web interface verification.
##### Kubernetes Native (2)

  - **(2026)** [==airflow.apache.org: KubernetesPodOperator 🌟🌟🌟==](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official engineering reference for the KubernetesPodOperator. Explains how to spin up isolated, dedicated pods within a target Kubernetes namespace dynamically for each individual Airflow DAG task execution.
  - **(2020)** [towardsdatascience.com: Apache Airflow for containerized data-pipelines](https://towardsdatascience.com/apache-airflow-for-containerized-data-pipelines-4d7a3c385bd) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores patterns to deploy containerized data processing networks via Apache Airflow. Focuses on orchestrating individual pipeline stages inside isolated runtime structures on top of cloud infrastructure.
##### Monitoring (2)

  - **(2021)** [redhat.com: Monitoring Apache Airflow using Prometheus](https://www.redhat.com/en/blog/monitoring-apache-airflow-using-prometheus) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical tutorial on integrating Apache Airflow orchestration endpoints with Prometheus. Illustrates how to pull scheduler workloads, active runner pools, and pipeline errors into centralized monitoring systems.
### Machine Learning Orchestration

#### Data Platforms

##### Open Data Hub

  - **(2026)** [**Open Data Hub**](https://opendatahub.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The main portal for Open Data Hub, an AI/ML platform reference architecture on Red Hat OpenShift. Orchestrates tools like Kubeflow, Spark, and Kafka into a standardized workspace for ML operations.
##### Releases

  - **(2020)** [Open Data Hub 0.6 brings component updates and Kubeflow architecture](https://developers.redhat.com/blog/2020/05/07/open-data-hub-0-6-brings-component-updates-and-kubeflow-architecture) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights components within Open Data Hub v0.6 release, evaluating the integrated Kubeflow-aligned architectural updates for containerized machine learning pipelines.
##### Roadmaps

  - **(2020)** [A development roadmap for Open Data Hub](https://developers.redhat.com/blog/2020/06/22/a-development-roadmap-for-open-data-hub) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A development roadmap overview outlining core development visions and tooling tracks designed for the Open Data Hub analytics platform.
#### Python SDKs

##### Couler

  - **(2023)** [Couler](https://github.com/couler-proj/couler) <span class='md-tag md-tag--info'>⭐ 944</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source Python SDK focused on orchestrating workloads on Kubernetes. Simplifies constructing declarative workflows across native schedulers like Argo or Tekton using programmatic expressions.
## Serverless

### Knative

#### Declarative Configuration

  - **(2021)** [itnext.io: Configuring Kafka Sources and Sinks declaratively in Kubernetes using Knative](https://itnext.io/configuring-kafka-sources-and-sinks-in-kubernetes-271e3757b208)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Hands-on exploration of declarative serverless ingestion pipelines on Kubernetes. Live Grounding: Focuses on setting up Knative Eventing Kafka sources and sinks, showcasing how to abstract underlying broker complexities into native Kubernetes custom resource definitions (CRDs).
#### Event-Driven Integration

  - **(2021)** [piotrminkowski.com: Knative Eventing with Quarkus, Kafka and Camel](https://piotrminkowski.com/2021/06/14/knative-eventing-with-quarkus-kafka-and-camel) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A step-by-step implementation guide showing serverless integration patterns using Knative, Quarkus, Kafka, and Apache Camel. Live Grounding: Demonstrates how to build efficient, fast-booting containerized JVM microservices that react dynamically to Kafka events routed via Knative's eventing framework.
#### Python Microservices

  - **(2023)** [**rogulski.it: Consume Kafka events with Knative service and FastAPI on kubernetes 🌟**](https://rogulski.it/blog/kafka-consumer-knative-fastapi) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Practical reference implementation for python-based serverless consumers. Live Grounding: Illustrates setting up Knative Eventing with a KafkaSource trigger to dynamically scale a FastAPI container from zero to process inbound streaming records.
## Software Architecture

### Case Studies (1)

#### Event Delivery

  - **(2016)** [**engineering.atspotify.com: Spotify’s Event Delivery – The Road to the Cloud (Part I)**](https://engineering.atspotify.com/2016/2/spotifys-event-delivery-the-road-to-the-cloud-part-i) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Part one of Spotify's highly detailed case study documenting their massive shift from on-premise infrastructure to Google Cloud Platform event infrastructure. It details scaling to deliver billions of events daily without data loss. Grounding validates this as an classic, essential read for distributed systems architects.
### Event-Driven Architecture (1)

#### Application Design

  - **(2020)** [stackoverflow.blog: How event-driven architecture solves modern web app problems 🌟](https://stackoverflow.blog/2020/03/16/how-event-driven-architecture-solves-modern-web-app-problems) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly clear explanation of how event-driven patterns resolve high concurrency and cross-system latency challenges. Grounding demonstrates its continued popularity as a primary training introduction to decoupled publishing and subscribing paradigms.
#### Infrastructure Design

  - **(2021)** [redhat.com: Event-driven architecture: Understanding the essential benefits 🌟](https://www.redhat.com/en/blog/event-driven-architecture-essentials) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive by Red Hat explaining how event-driven designs foster agility, decoupling, and high horizontal scalability. It discusses integration paths with Kubernetes, Apache Kafka, and Knative. Grounding shows its essential role for platform engineers planning enterprise application modernized routes.
### Integration Patterns (1)

#### iPaaS (1)

  - **(2026)** [==Mulesoft==](https://www.mulesoft.com) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The industry-standard enterprise integration platform (Anypoint Platform) providing high-density API management, ESB capabilities, and iPaaS routing. Mulesoft is highly suited for large-scale legacy modernization and hybrid-cloud orchestration, though it introduces significant runtime complexity and enterprise licensing costs.
  - **(2023)** [**quandarycg.com: Everything You Need To Know About System Integration (And IPaaS) 🌟**](https://www.quandarycg.com/everything-you-need-to-know-about-integrations) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A comprehensive architectural primer outlining the foundational concepts of Enterprise Application Integration (EAI) and Integration Platform as a Service (iPaaS).

*   Details the transition from legacy point-to-point connections to modern hub-and-spoke models.
*   Provides evaluation frameworks for cloud-native middleware alternatives.
  - **(2024)** [blog.hubspot.com: The 22 Best iPaaS Vendors for Any Budget](https://blog.hubspot.com/marketing/ipaas-vendors)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A commercial and technical overview of the top 22 Integration Platform as a Service (iPaaS) vendor solutions. Useful for architectural selection phases to compare enterprise offerings like MuleSoft, Workato, and Zapier across cloud compatibility, throughput limits, and ease of orchestration.
### Java Ecosystem

#### Microservices (2)

  - **(2020)** [adambien.blog - 75th **airhacks.tv** Questions and Answers: Kafka, JAX-RS, MicroProfile, JSON-B, GSON, JWT, VSC, NetBeans, Java Fullstack](https://adambien.blog/roller/abien/entry/kafka_jax_rs_microprofile_json)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical Q&A session highlighting architectural strategies using Kafka, JAX-RS, MicroProfile, and JSON-B. This resource offers pragmatic patterns for decoupling enterprise Java applications and migrating monolithic structures to cloud-native, microservice-based runtimes.
### Microservices (3)

#### Event-Driven Architecture (2)

  - **(2022)** [**confluent.io: Event-Driven Microservices Architecture (white paper) 🌟**](https://www.confluent.io/resources/white-paper/event-driven-microservices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Confluent's authoritative white paper on designing and scaling event-driven microservices around Apache Kafka log segments. It addresses CQRS, Event Sourcing, and transactional schemas. Grounding solidifies this as a core reference for large-scale enterprise data mesh topologies.
### Monolith Migration

#### Event-Driven Architecture (3)

  - **(2021)** [**infoq.com: From Monolith to Event-Driven: Finding Seams in Your Future Architecture**](https://www.infoq.com/articles/event-driven-finding-seams) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An InfoQ guide detailing how to use Domain-Driven Design (DDD) to isolate domain boundaries and discover 'seams' within large-scale monoliths. Grounding confirms its position as a primary methodology for refactoring to decoupled, event-driven pipelines.

---
💡 **Explore Related:** [Yaml](./yaml.md) | [Databases](./databases.md) | [Newsql](./newsql.md)

