# Kubernetes Operators and Controllers

1. [Introduction](#introduction)
2. [OpenTelemetry Operator](#opentelemetry-operator)
3. [Creating Kubernetes operator using Kubebuilder](#creating-kubernetes-operator-using-kubebuilder)
4. [operatorhub.io](#operatorhubio)
5. [Red Hat Container Community of Practice Operators](#red-hat-container-community-of-practice-operators)
6. [Operator Capability Levels](#operator-capability-levels)
7. [Cluster Addons](#cluster-addons)
8. [K8Spin Operator. Kubernetes multi-tenant operator](#k8spin-operator-kubernetes-multi-tenant-operator)
9. [K8s KPIs with Kuberhealthy Operator](#k8s-kpis-with-kuberhealthy-operator)
10. [Writing Kubernetes Operators and Controllers](#writing-kubernetes-operators-and-controllers)
11. [Tweets](#tweets)
12. [Videos](#videos)

## Introduction

- [kruschecompany.com: What is a Kubernetes Operator and Where it Can be Used?](https://kruschecompany.com/kubernetes-operator/)
- [kruschecompany.com: Prometheus Operator – Installing Prometheus Monitoring Within The Kubernetes Environment](https://kruschecompany.com/kubernetes-prometheus-operator/)
- [kube-fluentd-operator 🌟](https://github.com/vmware/kube-fluentd-operator) is a sane, no-brainer Kubernetes+Helm distribution of Fluentd with batteries included, config validation, no needs to restart, with sensible defaults and best practices built-in. You can use Kubernetes labels to filter/route logs!
- [Domain-harvester](https://github.com/shurshun/domain-harvester) is an operator that collects domains from all Ingress resources in a Kubernetes cluster and provides its expiry information
- [Cass Operator](https://github.com/datastax/cass-operator) The DataStax Kubernetes Operator for Apache Cassandra®
- [Kotal operator](https://github.com/kotalco/kotal) is cloud agnostic blockchain deployer that make it easy to deploy highly available, self-managing, self-healing blockchain infrastructure (networks, nodes, storage clusters ...) on any cloud.
- [Speculator: Redis Operator](https://github.com/OT-CONTAINER-KIT/redis-operator) A Golang based redis operator that will make/oversee Redis standalone/cluster mode setup on top of the Kubernetes. It can create a redis cluster setup with best practices on Cloud as well as the Bare metal environment. Also, it provides an in-built monitoring capability using redis-exporter.
- [github.com/carlosedp/lbconfig-operator: External Load Balancer Operator 🌟](https://github.com/carlosedp/lbconfig-operator) a Kubernetes/openshift Operator to dynamically configure external load-balancers distributing the traffic to the cluster nodes. It's not 100% (will it ever be?) but already configures the F5 BigIP. The idea is to have multiple LB backends soon.
- [Sentry Operator](https://github.com/jace-ys/sentry-operator) A Kubernetes operator for automating the provisioning and management of Sentry resources via Kubernetes CRDs.
- [thenewstack.io: When to Use, and When to Avoid, the Operator Pattern 🌟](https://thenewstack.io/kubernetes-when-to-use-and-when-to-avoid-the-operator-pattern/)
- [infoq.com: Kubernetes Operators in Depth](https://www.infoq.com/articles/kubernetes-operators-in-depth/)
- [DB Operator 🌟](https://github.com/kloeckner-i/db-operator) is a Kubernetes Operator for the management of cloud databases, primarily Google Cloud SQL(GCSQL). It is designed to support the on demand creation of test environments in CI/CD pipelines.
- [container-solutions.com: Kubernetes Operators Explained](https://blog.container-solutions.com/kubernetes-operators-explained)
- [kubeload - load testing](https://github.com/Efrat19/kubeload) is a Kubernetes operator that lets you configure your load-test initial load, max load, interval and hatch-rate. You can use CRD to define all the parameters and repeat your load testing experiments.
- [contentful.com: Open-sourcing kube-secret-syncer: A Kubernetes operator to sync secrets from AWS Secrets Manager](https://www.contentful.com/blog/2020/10/20/open-source-kube-secret-syncer/)
    - [contentful-labs/kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer)
- [registry-creds](https://github.com/alexellis/registry-creds) is a Kubernetes operator that can be used to propagate a single ImagePullSecret to all namespaces within your cluster. The primary reason for creating this operator is to make it easier to consume images from Docker Hub.
- [gemini](https://github.com/FairwindsOps/gemini) is a Kubernetes CRD and operator for managing VolumeSnapshots. This allows you to back up your PersistentVolumes on a regular schedule, retire old backups, and restore backups with minimal downtime.
- [HostPort Operator](https://github.com/rmb938/hostport-allocator) is a Kubernetes Operator to allocate host ports
- [iximiuz.com: Exploring Kubernetes Operator Pattern 🌟](https://iximiuz.com/en/posts/kubernetes-operator-pattern/)
- [isaaguilar/terraform-operator: Terraform Operator](https://github.com/isaaguilar/terraform-operator) A Kubernetes CRD and Controller to handle Terraform operations by generating k8s jobs catered to perform Terraform workflows
- [didil/autobucket-operator](https://github.com/didil/autobucket-operator) The autobucket operator is a Kubernetes operator that automatically creates and manages Cloud Buckets (Object Storage) for k8s Deployments.
- [openshift.com: Is your Operator Air-Gap Friendly?](https://www.openshift.com/blog/is-your-operator-air-gap-friendly)
- [kuberhealthy 🌟](https://github.com/Comcast/kuberhealthy) An operator for synthetic monitoring on Kubernetes. Write your own tests in your own container and Kuberhealthy will manage everything else. Automatically creates and sends metrics to Prometheus and InfluxDB. Included simple JSON status page. Supplements other solutions like Prometheus very nicely!
- [Bare Metal Operator](https://github.com/metal3-io/baremetal-operator) The Bare Metal Operator implements a Kubernetes API for managing bare metal hosts. It maintains an inventory of available hosts as Custom Resource Definitions.
- [Meerkat](https://github.com/borchero/meerkat) Meerkat is a Kubernetes Operator that facilitates the deployment of OpenVPN in a Kubernetes cluster. By leveraging Hashicorp Vault, Meerkat securely manages the underlying PKI.
- [Logging Operator](https://github.com/OT-CONTAINER-KIT/logging-operator) A golang based CRD operator to setup and manage logging stack (Elasticsearch, Fluentd, and Kibana) in the Kubernetes cluster. It helps to setup each component of the EFK stack separately.
- [gst-pipeline-operator: A Kubernetes operator for running audio/video processing pipelines](https://github.com/tinyzimmer/gst-pipeline-operator)
- [uptimerobot-operator](https://github.com/brennerm/uptimerobot-operator) A Kubernetes operator that creates UptimeRobot monitors for your ingresses
- [medium.com: Getting Started With Kubernetes Operators (Helm Based) - Part 1](https://www.velotio.com/engineering-blog/getting-started-with-kubernetes-operators-helm-based-part-1)
    - [velotio.com: Getting Started With Kubernetes Operators (Golang Based) - Part 3](https://www.velotio.com/engineering-blog/getting-started-with-kubernetes-operators-golang-based-part-3)
- [IngressMonitorController (Deprecated)](https://github.com/stakater/IngressMonitorController) A Kubernetes controller to watch ingresses and create liveness alerts for your apps/microservices in UptimeRobot, StatusCake, Pingdom, etc.
- [==FairwindsOps/rbac-manager: RBAC Manager== 🌟](https://github.com/FairwindsOps/rbac-manager) A Kubernetes operator that simplifies the management of Role Bindings and Service Accounts. RBAC Manager is designed to simplify authorization in Kubernetes. This is an operator that supports declarative configuration for RBAC with new custom resources. Instead of managing role bindings or service accounts directly, you can specify a desired state and RBAC Manager will make the necessary changes to achieve that state.
- [KubePlus - Kubernetes Operator to deliver Helm charts as-a-service 🌟](https://github.com/cloud-ark/kubeplus)
- [kubernetes.io: Writing a Controller for Pod Labels](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/)
- [kubermatic.com: Why Implementing Kubernetes Operators Is a Good Idea! 🌟](https://www.kubermatic.com/blog/why-implementing-kubernetes-operators-is-a-good-idea/)
- [thenewstack.io: We Pushed Helm to the Limit, then Built a Kubernetes Operator 🌟](https://thenewstack.io/we-pushed-helm-to-the-limit-then-built-a-kubernetes-operator/)
- [digitalis-io/vals-operator](https://github.com/digitalis-io/vals-operator) Kubernetes Operator to sync secrets between different secret backends and Kubernetes
- [banzaicloud/thanos-operator 🌟](https://github.com/banzaicloud/thanos-operator) Thanos Operator is a Kubernetes operator to manage Thanos stack deployment on Kubernetes.
- [cloud-bulldozer/benchmark-operator: The Chuck Norris of cloud benchmarks](https://github.com/cloud-bulldozer/benchmark-operator) The intent of this Operator is to deploy common workloads to establish a performance baseline of Kubernetes cluster on your provider.
- [pravega/pravega-operator](https://github.com/pravega/pravega-operator) Pravega Kubernetes Operator. Pravega is an open source distributed storage service implementing Streams. It offers Stream as the main primitive for the foundation of reliable storage systems: a high-performance, durable, elastic, and unlimited append-only byte stream with strict ordering and consistency. The Pravega Operator manages Pravega clusters deployed to Kubernetes and automates tasks related to operating a Pravega cluster.The operator itself is built with the Operator framework.
- [Quentin-M/etcd-cloud-operator](https://github.com/Quentin-M/etcd-cloud-operator) Deploying and managing production-grade etcd clusters on cloud providers: failure recovery, disaster recovery, backups and resizing.
- [==spring.io: Get to Know a Kubernetes Operator!==](https://spring.io/blog/2021/11/19/get-to-know-a-kubernetes-operator)
- [VictoriaMetrics/operator](https://github.com/VictoriaMetrics/operator) Kubernetes operator for Victoria Metrics
- [blog.px.dev/k8s-operator: 3 Reasons to Use Kubernetes Operators (and 2 Reasons Not To)](https://blog.px.dev/k8s-operator)
- [practicalkubernetes.blogspot.com: Making the case for Kubernetes Operators](https://practicalkubernetes.blogspot.com/2022/01/making-case-for-kubernetes-operators.html)
- [reactive-tech/kubegres](https://github.com/reactive-tech/kubegres) Kubegres is a Kubernetes operator allowing to deploy one or many **clusters of PostgreSql instances and manage databases replication, failover and backup.**
- [==Capsule Operator==](https://github.com/clastix/capsule) is a Kubernetes multi-tenant Operator. It aggregates multiple namespaces in a Tenant. Within each tenant, users are free to create their namespaces and share all the assigned resources between the namespaces of the tenant.
- [==redhat-cop/keepalived-operator: Keepalived operator==](https://github.com/redhat-cop/keepalived-operator) An operator to manage VIPs backed by keepalived. The objective of the keepalived operator is to allow for a way to create self-hosted load balancers in an automated way. From a user experience point of view the behavior is the same as of when creating LoadBalancer services with a cloud provider able to manage them.
- [redhat-cop/dynamic-rbac-operator: Dynamic RBAC Operator](https://github.com/redhat-cop/dynamic-rbac-operator) Flexible definitions of Kubernetes RBAC rules. Writing Kubernetes RBAC definitions by hand can be a pain. This operator allows you to define "Dynamic" RBAC rules that change based on the state of your cluster, so you can spend your time writing the RBAC patterns that you'd like to deploy, rather than traditional, fully enumerated RBAC rules.
- [spotify/flink-on-k8s-operator: Kubernetes Operator for Apache Flink](https://github.com/spotify/flink-on-k8s-operator) Kubernetes operator for that acts as control plane to manage the complete deployment lifecycle of Apache Flink applications. This is an open source fork of GoogleCloudPlatform/flink-on-k8s-operator with several new features and bug fixes.
- [kube-green](https://kube-green.dev) An operator to reduce CO2 footprint of your clusters.
    - Sleep your pods: Suspend your pods when no-one's using them, scale down your cluster and save energy
    - Reduce CO2 emissions: See how much you save in the Green Dashboard (coming soon)
- [krestomatio/keydb-operator](https://github.com/krestomatio/keydb-operator) A KeyDB (Drop-In Alternative to Redis) Operator for Kubernetes
- [==Keel== 🌟](https://github.com/keel-hq/keel) **Kubernetes Operator to automate Helm, DaemonSet, StatefulSet & Deployment updates:**
    - You can use policies to define when to update an application
    - Users can specify how many approvals do they need before a resource is updated.
    - https://keel.sh
- [openshift/machine-api-operator](https://github.com/openshift/machine-api-operator) The Machine API Operator manages the lifecycle of specific purpose CRDs, controllers and RBAC objects that extend the Kubernetes API. This allows to convey desired state of machines in a cluster in a declarative fashion
- [rancher/system-upgrade-controller: System Upgrade Controller](https://github.com/rancher/system-upgrade-controller) This project aims to provide a general-purpose, Kubernetes-native upgrade controller (for nodes). It introduces a new CRD, the Plan, for defining any and all of your upgrade policies/requirements. A Plan is an outstanding intent to mutate nodes in your cluster.
- [ckotzbauer/vulnerability-operator](https://github.com/ckotzbauer/vulnerability-operator) Scans SBOMs for vulnerabilities. This operator scans all SBOMs from a git-repository for vulnerabilities using Grype. The result-list can be emitted as JSON-file served via an endpoint and/or as Prometheus metrics. There may be more targets in the future. The scans are done periodically.
- [Michaelpalacce/SimpleSecrets](https://github.com/Michaelpalacce/SimpleSecrets) K8S Secrets Manager Operator. SimpleSecrets is a secure operator that allows you to create secrets on demand. You can commit the SimpleSecrets, which are references to a database secret, and the operator will create Kubernetes Secrets automatically for you.
- [learnsteps.com: Advance Kubernetes: What exactly are Kubernetes Operators?](https://www.learnsteps.com/advanced-kubernetes-what-exactly-are-kubernetes-operators/) Kubernetes has gained a lot of traction recently and is one of the standards followed across organizations when it comes to running and managing their containerized workloads. In this article, we are going to talk about Kubernetes operators.
- [theregister.com: IBM launches Db2 operator for Kubenetes on AWS](https://www.theregister.com/AMP/2022/07/20/ibm_db2_operator/) Azure soon to follow as Big Blue accomodates a world with many clouds
- [OT-CONTAINER-KIT/mongodb-operator: MongoDB Operator](https://github.com/OT-CONTAINER-KIT/mongodb-operator) MongoDB Operator is an operator created in Golang to create, update, and manage MongoDB standalone, replicated, and arbiter replicated setup on Kubernetes and Openshift clusters.
- [prosimcorp/reforma](https://github.com/prosimcorp/reforma) Reforma is a Kubernetes operator to patch resources with information from other resources. It is intended to use with GitOps and lets you do things such as creating annotation on a Service Account from metadata stored in a ConfigMap.
- [weaveworks/tf-controller: Weave GitOps Terraform Controller](https://github.com/weaveworks/tf-controller) A GitOps Terraform controller for Kubernetes. Weave TF-controller is a controller for Flux to reconcile Terraform resources in the GitOps way.
- [vitobotta/velero-notifications](https://github.com/vitobotta/velero-notifications) Velero-notifications is a simple Kubernetes controller written in Ruby that sends email/Slack/webhook notifications when backups or restores are performed by Velero in a Kubernetes cluster.
- [NVIDIA/gpu-operator](https://github.com/NVIDIA/gpu-operator) NVIDIA GPU Operator creates/configures/manages GPUs atop Kubernetes. The NVIDIA GPU is a Kubernetes operator that automates the management of all NVIDIA software components needed to provision GPUs. These components include drivers, the Kubernetes device plugin, the NVIDIA Container Runtime, etc.
    - [NVIDIA/k8s-device-plugin: NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin) The NVIDIA device plugin for Kubernetes is a Daemonset that allows you to automatically:
        - Expose the number of GPUs on each node of your cluster
        - Keep track of the health of your GPUs
        - Run GPU enabled containers in your Kubernetes cluster
- [glebiller/dynamic-configuration-operator: Dynamic Configuration Operator](https://github.com/glebiller/dynamic-configuration-operator) Dynamic Configuration Operator is an operator that updates a deployment when a ConfigMap or Secret is updated. Useful for apps that:
    - Don't have a live-reload feature
    - Use `subPath` while mounting a ConfigMap or Secret
    - Use Projected Volumes
- [github.com/furiko-io/furiko](https://github.com/furiko-io/furiko) Cloud-native, enterprise-level cron job platform for Kubernetes. Furiko is a Kubernetes-native operator for managing, scheduling and executing scheduled and ad-hoc jobs and workflows. It aims to be a general-purpose job platform that supports various use cases, including cron jobs, batch processing, etc.
- [github.com/DevOps-Nirvana: Kubernetes Volume / Disk Autoscaler (via Prometheus)](https://github.com/DevOps-Nirvana/Kubernetes-Volume-Autoscaler)
    - This repository contains a Kubernetes controller that automatically increases the size of a Persistent Volume Claim in Kubernetes when it is nearing full. Initially engineered based on AWS EKS, this should support any Kubernetes cluster or cloud provider which supports dynamically hot-resizing storage volumes in Kubernetes.
    - Keeping your volumes at a minimal size can help reduce cost, but having to manually scale them up can be painful and a waste of time for an DevOps / Systems Administrator. This is often used on storage volumes against things in Kubernetes such as Prometheus, MySQL, Redis, RabbitMQ, or any other stateful service.
- [borchero/switchboard: Switchboard](https://github.com/borchero/switchboard) Kubernetes Operator for Automatically Issuing DNS Records and TLS Certificates for Traefik Ingress Routes.
- [scylladb/scylla-operator](https://github.com/scylladb/scylla-operator) Scylla Operator is a Kubernetes Operator for managing and automating tasks related to managing Scylla clusters
    - This article will dive deep into one of Kubernetes’ core concepts — Controllers, Kubernetes API, CRDs, and Operators.
    - This 4-part series covers:
        - Kubernetes controllers, Custom Resources, and operators
        - Building Kubernetes operators
        - Testing Kubebuilder operators
        - Deploying Kubebuilder operators to Kubernetes
- [coderanger/migrations-operator: Migrations-Operator](https://github.com/coderanger/migrations-operator) A Kubernetes operator to manage database migrations or similar application setup tasks.
- [omerxx.com: 10 Things I wish I’d known before building a Kubernetes CRD controller](https://omerxx.com/k8s-controllers/) Controllers, operators, informers and other K8s mysteries. This article discusses a few of the gotchas of developing Kubernetes controllers:
    - CRDs don't create metadata by default
    - Interacting with CRDs outside the controller's context is not straightforward
    - "The DefaultUnstructuredConverter"
- [github.com/mittwald/kubernetes-secret-generator 🌟](https://github.com/mittwald/kubernetes-secret-generator) Kubernetes controller for automatically generating and updating secrets. This repository contains a custom Kubernetes controller that can automatically create random secret values. This may be used for auto-generating random credentials for applications running on Kubernetes
- [github.com/ContainerSolutions/delayed-jobs-operator](https://github.com/ContainerSolutions/delayed-jobs-operator) The Delayed Job Operator lets delay the start of a Kubernetes job until after a UNIX timestamp
- [github.com/actions/actions-runner-controller 🌟](https://github.com/actions/actions-runner-controller) Actions Runner Controller (ARC) is a Kubernetes controller for GitHub Actions self-hosted runners. With ARC, you can:
    - Deploy self-hosted runners on Kubernetes clusters with a simple set of commands
    - Auto scale runners based on demand
- [==blog.frankel.ch: Introduction to Kubernetes extensibility== 🌟](https://blog.frankel.ch/kubernetes-extensibility/) In this article, you'll learn several extension points in Kubernetes: the data model, admission controllers, and client-side.
    - At its most basic level, Kubernetes is just a platform able to run container images. It stores its configuration in a distributed storage engine, etcd. The most significant part of this configuration is dedicated to the desired state for objects. For example, you only update this state when you schedule a pod using the kubectl command line.
    - Other components, called controllers, watch configuration changes and read the desired state. Then, they try to reconcile the desired state with the actual state. It’s nothing revolutionary: Puppet is based on the same control-loop approach, and AFAIK, Chef. Generally, a controller manages a single type of object, e.g., the DeploymentController manages deployments.
- [superorbital.io: Testing Production Kubernetes Controllers](https://superorbital.io/blog/testing-production-controllers/) In this article, you will learn how to test Kubernetes controllers using a mix of unit tests, local integration tests, and more fully featured runtime integration tests.
- [github.com/lukaszraczylo/jobs-manager-operator 🌟](https://github.com/lukaszraczylo/jobs-manager-operator)
- [github.com/ricoberger/vault-secrets-operator](https://github.com/ricoberger/vault-secrets-operator) Create Kubernetes secrets from Vault for a secure GitOps based workflow.
- [github.com/ElementTech/kube-reqsizer](https://github.com/ElementTech/kube-reqsizer) kube-reqsizer is a kubernetes controller that measures the usage of pods over time and optimizes their requests based on the average usage. The controller calculates the requirements based on all the samples taken in the same deployment controller.
- [github.com/sieve-project/sieve](https://github.com/sieve-project/sieve) Automated Reliability Testing for Kubernetes Controllers/Operators. Sieve is a tool to help developers test their Kubernetes controllers by deterministically injecting faults and detecting dormant bugs at development time.
- [thenewstack.io: HashiCorp Vault Operator Manages Kubernetes Secrets](https://thenewstack.io/hashicorp-vault-operator-manages-kubernetes-secrets/) HashiCorp's new open source project, released alongside Vault 1.13 and now available in beta, makes it easier to use Vault with Kubernetes Secrets, automating tasks that were previously manual.
- [github.com/2-alchemists/krossboard-kubernetes-operator](https://github.com/2-alchemists/krossboard-kubernetes-operator) Kubernetes Operator to handle cross-site, cross-distribution & multi-Kubernetes usage tracking, analytics and accounting (vanilla Kubernetes, OpenShift, EKS, AKS, GKE and other distros).
    - Krossboard is a multi-cluster and cross-distribution Kubernetes usage accounting and analytics software
    - Each instance of Krossboard enables tracking the usage of a set of Kubernetes clusters listed in a kubeconfig secret
- [github.com/gianlucam76/k8s-cleaner 🌟](https://github.com/gianlucam76/k8s-cleaner) **K8s cleaner is a controller that identifies, removes, or updates stale/orphaned or unhealthy resources to maintain a clean and efficient Kubernetes cluster**
- [github.com/NCCloud/mayfly: Ephemeral Kubernetes Resources 🌟](https://github.com/NCCloud/mayfly) An operator to manage ephemeral Kubernetes resources

## OpenTelemetry Operator

- [github.com/open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator)

## Creating Kubernetes operator using Kubebuilder

- [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) Kubebuilder - SDK for building Kubernetes APIs using CRDs. Kubebuilder is a framework for building Kubernetes APIs using custom resource definitions (CRDs). Kubebuilder increases velocity and reduces the complexity managed by developers for rapidly building and publishing Kubernetes APIs in Go.
    - https://book.kubebuilder.io
    - Kubernetes is the current de facto standard for the deployment and running of applications that are suitable for modern cloud platforms. A declarative way of defining infrastructure state using YAML allows a super easy definition of the scheme for the deployment of the application. Deploying stateless applications is not a big deal. On the other hand — deploying distributed stateful applications, configuring, and operating them is a challenging task.

    - Kubernetes addressed this issue by allowing developers to extend it, using the Kubernetes operator. The operator reacts to the custom resource and reconciliate the state in the cluster with the state defined in the custom resource, by implementing logic embedded in the operator itself.

    - When designing/writing an application, intended to run on the Kubernetes, one should take into account capabilities provided by Kubernetes and take that information when designing software architecture. It can speed up implementation, make an application more reliable and the code can focus more on business logic itself.

    - There are multiple ways to create an operator. You could write one from scratch using Kubernetes  client-go. It’s a tedious task and the learning curve is steep. As an alternative, multiple tools provide boilerplate code and speed up the writing of operators. Popular ones are Operatorsdk and Kubebuilder. The focus of the article will be on creating an operator using Kubebuilder. Let’s create an operator which will create a pod running a simple HTTP API and bind some data to the HTTP API.
- [dev.to/thenjdevopsguy: What Is A Kubernetes Operator?](https://dev.to/thenjdevopsguy/what-is-a-kubernetes-operator-53kb)

## operatorhub.io

- [operatorhub.io](https://operatorhub.io/) OperatorHub.io is a new home for the Kubernetes community to share Operators. Find an existing Operator or list your own today.

## Red Hat Container Community of Practice Operators

- [==cloud.redhat.com: Red Hat Container Community of Practice Operators==](https://cloud.redhat.com/blog/red-hat-container-community-of-practice-operators) In this post, you will find a summary of the operators maintained by Red Hat and how they can be used to facilitate the adoption of OpenShift.

## Operator Capability Levels

- [Operator Capability Levels](https://operatorframework.io/operator-capabilities/) Operators come in different maturity levels in regards to their lifecycle management capabilities for the application or workload they deliver. The capability models aims to provide guidance in terminology to express what features users can expect from an Operator.

## Cluster Addons

- [Cluster Addons 🌟](https://github.com/kubernetes-sigs/cluster-addons) With cluster addon operators, we are exploring a kubernetes-native way of managing addons using CRDs(Custom Resource Definitions) and controllers where the controllers encode how best to manage the addon. Installing and managing an addon could be as simple as creating a custom resource.

## K8Spin Operator. Kubernetes multi-tenant operator

- [K8Spin Operator 🌟](https://github.com/k8spin/k8spin-operator) Kubernetes multi-tenant operator. Enables multi-tenant capabilities in your Kubernetes Cluster. [We defined some small features to implement](https://github.com/k8spin/k8spin-operator/projects/1). If you know python & Kubernetes and want to contribute to this project, ping us!
- [thenewstack.io: K8Spin Provides Multitenant Isolation for Kubernetes](https://thenewstack.io/k8spin-provides-multitenant-isolation-for-kubernetes/)
- [Discover K8Spin open source software](https://k8spin.cloud/oss-projects/)

## K8s KPIs with Kuberhealthy Operator

- [K8s KPIs with Kuberhealthy 🌟](https://kubernetes.io/blog/2020/05/29/k8s-kpis-with-kuberhealthy/) transforming Kuberhealthy into a Kubernetes operator for synthetic monitoring. This new ability granted developers the means to create their own Kuberhealthy check containers to synthetically monitor their applications and clusters. Additionally, we created a guide on how to easily install and use Kuberhealthy in order to capture some helpful synthetic [KPIs](https://kpi.org/KPI-Basics).

## Writing Kubernetes Operators and Controllers

- [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [opensource.com: Build a Kubernetes Operator in 10 minutes with Operator SDK](https://opensource.com/article/20/3/kubernetes-operator-sdk)
- [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)
- [linuxera.org: Writing Operators using the Operator Framework SDK](https://linuxera.org/writing-operators-using-operator-framework/)
- [openshift.com: 7 Best Practices for Writing Kubernetes Operators: An SRE Perspective](https://www.openshift.com/blog/7-best-practices-for-writing-kubernetes-operators-an-sre-perspective)
- [openshift.com: Build Your Kubernetes Operator With the Right Tool 🌟](https://www.openshift.com/blog/build-your-kubernetes-operator-with-the-right-tool) **Go-based operators are by far the most popular. That is why Go is probably the first option to consider.** The other good choice is Helm, especially if you already have a Helm chart for your software or you want to build your operator quickly and you don't need any complex [capability levels](https://operatorframework.io/operator-capabilities/). I'd leave Operator Frameworks or Bare Programming Language implementations only for the cases when keeping a single programming language in your organization is a priority.
- [rookout.com: Lessons Learned When Building A Kubernetes Operator](https://www.rookout.com/blog/lessons-learned-when-building-a-kubernetes-operator)
- [brennerm.github.io: Kubernetes operators with Python #1: Creating CRDs](https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html)
- [vivilearns2code.github.io: Writing Controllers For Kubernetes Resources](https://vivilearns2code.github.io/k8s/2021/03/11/writing-controllers-for-kubernetes-custom-resources.html)
- [==kubernetes/sample-controller==](https://github.com/kubernetes/sample-controller) Repository for sample controller. Complements sample-apiserver
- [metalbear.co: Writing a Kubernetes Operator](https://metalbear.co/blog/writing-a-kubernetes-operator/)
- [dev.to/hkhelil: Building a Kubernetes Operator with an NGINX CRD](https://dev.to/hkhelil/building-a-kubernetes-operator-with-an-nginx-crd-3lil)

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Generic automation tools like Helm are limited by the interfaces exposed to them, and often lack enough context to make the right state machine transitions.<br><br>Ideally, software evolves to expose better automation hooks, then custom tools, aka operators, can leverage them. <a href="https://t.co/v38aj4ukn4">https://t.co/v38aj4ukn4</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1435637052079427584?ref_src=twsrc%5Etfw">September 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ha3LjlD6g7g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>