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
- [redhat.com: Kubernetes operators - Embedding operational expertise side by side with containerized applications](https://www.redhat.com/sysadmin/kubernetes-operators)
- [hashicorp.com: Creating Workspaces with the HashiCorp Terraform Operator for Kubernetes](https://www.hashicorp.com/blog/creating-workspaces-with-the-hashicorp-terraform-operator-for-kubernetes/)
- [banzaicloud.com: Kafka rolling upgrade made easy with Supertubes](https://banzaicloud.com/blog/kafka-rolling-upgrade/)
- [devops.com: Day 2 for the Operator Ecosystem 🌟](https://devops.com/day-2-for-the-operator-ecosystem/)
    - [KUDO: The Kubernetes Universal Declarative Operator 🌟](https://kudo.dev/) KUDO is a toolkit that makes it easy to build Kubernetes Operators, in most cases just using YAML.
- [itnext.io: **Operator Lifecycle Manager (OLM)** 🌟](https://itnext.io/wth-is-a-operator-lifecycle-manager-873cf1661b04)
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
- [cncf.io: Kubernetes Operators 101](https://www.cncf.io/blog/2020/10/02/kubernetes-operators-101/)
- [container-solutions.com: Kubernetes Operators Explained](https://blog.container-solutions.com/kubernetes-operators-explained)
- [kubeload - load testing](https://github.com/Efrat19/kubeload) is a Kubernetes operator that lets you configure your load-test initial load, max load, interval and hatch-rate. You can use CRD to define all the parameters and repeat your load testing experiments.
- [contentful.com: Open-sourcing kube-secret-syncer: A Kubernetes operator to sync secrets from AWS Secrets Manager](https://www.contentful.com/blog/2020/10/20/open-source-kube-secret-syncer/)
    - [contentful-labs/kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer)
- [registry-creds](https://github.com/alexellis/registry-creds) is a Kubernetes operator that can be used to propagate a single ImagePullSecret to all namespaces within your cluster. The primary reason for creating this operator is to make it easier to consume images from Docker Hub.
- [gemini](https://github.com/FairwindsOps/gemini) is a Kubernetes CRD and operator for managing VolumeSnapshots. This allows you to back up your PersistentVolumes on a regular schedule, retire old backups, and restore backups with minimal downtime.
- [Kdo: deployless development on Kubernetes 🌟](https://kdo.dev/) Kdo is a command line tool that enables developers to run, develop and test code changes in a realistic deployed setting without having to deal with the complexity of Kubernetes deployment and configuration.
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
    - [medium.com: Getting Started With Kubernetes Operators (Ansible Based) — Part 2](https://medium.com/velotio-perspectives/getting-started-with-kubernetes-operators-ansible-based-part-2-472eb0d453b7)
    - [velotio.com: Getting Started With Kubernetes Operators (Golang Based) - Part 3](https://www.velotio.com/engineering-blog/getting-started-with-kubernetes-operators-golang-based-part-3)
- [IngressMonitorController (Deprecated)](https://github.com/stakater/IngressMonitorController) A Kubernetes controller to watch ingresses and create liveness alerts for your apps/microservices in UptimeRobot, StatusCake, Pingdom, etc.
- [==FairwindsOps/rbac-manager: RBAC Manager== 🌟](https://github.com/FairwindsOps/rbac-manager) A Kubernetes operator that simplifies the management of Role Bindings and Service Accounts. RBAC Manager is designed to simplify authorization in Kubernetes. This is an operator that supports declarative configuration for RBAC with new custom resources. Instead of managing role bindings or service accounts directly, you can specify a desired state and RBAC Manager will make the necessary changes to achieve that state.
- [KubePlus - Kubernetes Operator to deliver Helm charts as-a-service 🌟](https://github.com/cloud-ark/kubeplus)
- [kubernetes.io: Writing a Controller for Pod Labels](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/)
- [kubermatic.com: Why Implementing Kubernetes Operators Is a Good Idea! 🌟](https://www.kubermatic.com/blog/why-implementing-kubernetes-operators-is-a-good-idea/)
- [thenewstack.io: We Pushed Helm to the Limit, then Built a Kubernetes Operator 🌟](https://thenewstack.io/we-pushed-helm-to-the-limit-then-built-a-kubernetes-operator/)
- [cncf.io: CNCF Operator White Paper (PDF) 🌟](https://www.cncf.io/wp-content/uploads/2021/07/CNCF_Operator_WhitePaper.pdf) This white paper defines Operators in a wider context than Kubernetes. It describes their characteristics and components, gives an overview of common patterns currently in use and explains how they differ from Kubernetes controllers.
- [itnext.io: Kubexpose: A Kubernetes Operator, for fun and profit!](https://itnext.io/kubexpose-a-kubernetes-operator-for-fun-and-profit-f528586eee07) Access your Kubernetes Deployment over the Internet - [abhirockzz/kubexpose-operator](https://github.com/abhirockzz/kubexpose-operator) Access your Kubernetes Deployment over the Internet
- [redhat.com: Kubernetes Operators on Red Hat Marketplace](https://www.redhat.com/en/resources/kubernetes-operators-marketplace-datasheet)
- [itnext.io: Kubernetes Operators: Cruise Control for Managing Cloud-Native Apps](https://itnext.io/kubernetes-operators-cruise-control-for-managing-cloud-native-apps-db328ef8e345)
- [digitalis-io/vals-operator](https://github.com/digitalis-io/vals-operator) Kubernetes Operator to sync secrets between different secret backends and Kubernetes
- [banzaicloud/thanos-operator 🌟](https://github.com/banzaicloud/thanos-operator) Thanos Operator is a Kubernetes operator to manage Thanos stack deployment on Kubernetes.
- [cloud-bulldozer/benchmark-operator: The Chuck Norris of cloud benchmarks](https://github.com/cloud-bulldozer/benchmark-operator) The intent of this Operator is to deploy common workloads to establish a performance baseline of Kubernetes cluster on your provider.
- [pravega/pravega-operator](https://github.com/pravega/pravega-operator) Pravega Kubernetes Operator. Pravega is an open source distributed storage service implementing Streams. It offers Stream as the main primitive for the foundation of reliable storage systems: a high-performance, durable, elastic, and unlimited append-only byte stream with strict ordering and consistency. The Pravega Operator manages Pravega clusters deployed to Kubernetes and automates tasks related to operating a Pravega cluster.The operator itself is built with the Operator framework.
- [Quentin-M/etcd-cloud-operator](https://github.com/Quentin-M/etcd-cloud-operator) Deploying and managing production-grade etcd clusters on cloud providers: failure recovery, disaster recovery, backups and resizing.
- [==spring.io: Get to Know a Kubernetes Operator!==](https://spring.io/blog/2021/11/19/get-to-know-a-kubernetes-operator)
- [==levelup.gitconnected.com: Operators : Extending Kubernetes Capabilities==](https://levelup.gitconnected.com/operators-extending-kubernetes-capabilities-184df001b7e) Operators are software extensions to Kubernetes that make use of custom resources to manage applications and their components. So what it means is that there are some applications whose deployment and management might require manual intervention and operators is the solution to automate it. **Let’s say you need to deploy a database cluster for which each pod needs to be brought in sync after deployment, or say you need to perform a security scan whenever a new component is deployed, or maybe some configuration needs to be populated based on some event. Such a functionalities are not available in Kubernetes out of the box but can be implemented using operators.**
- [==developer.redis.com: Kubernetes Operator: What It Is and Why You Should Really Care About It==](https://developer.redis.com/create/kubernetes/kubernetes-operator/)
- [VictoriaMetrics/operator](https://github.com/VictoriaMetrics/operator) Kubernetes operator for Victoria Metrics
- [blog.px.dev/k8s-operator: 3 Reasons to Use Kubernetes Operators (and 2 Reasons Not To)](https://blog.px.dev/k8s-operator)
- [==dzone.com: What Is a Kubernetes Operator?==](https://dzone.com/articles/what-is-a-kubernetes-operator) A Kubernetes Operator fills in the gaps between the capabilities and automation provided by Kubernetes and how your software uses Kubernetes for task automation.
- [practicalkubernetes.blogspot.com: Making the case for Kubernetes Operators](https://practicalkubernetes.blogspot.com/2022/01/making-case-for-kubernetes-operators.html)
- [reactive-tech/kubegres](https://github.com/reactive-tech/kubegres) Kubegres is a Kubernetes operator allowing to deploy one or many **clusters of PostgreSql instances and manage databases replication, failover and backup.**
- [==Capsule Operator==](https://github.com/clastix/capsule) is a Kubernetes multi-tenant Operator. It aggregates multiple namespaces in a Tenant. Within each tenant, users are free to create their namespaces and share all the assigned resources between the namespaces of the tenant.
- [==redhat-cop/keepalived-operator: Keepalived operator==](https://github.com/redhat-cop/keepalived-operator) An operator to manage VIPs backed by keepalived. The objective of the keepalived operator is to allow for a way to create self-hosted load balancers in an automated way. From a user experience point of view the behavior is the same as of when creating LoadBalancer services with a cloud provider able to manage them.
- [medium.com/@samng1991216: Building Kubernetes Operator Application from Scratch (Part 1)](https://medium.com/@samng1991216/building-kubernetes-operator-application-from-scratch-part-1-211b6b2467df)
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
- [medium.com/@mjkool: Kubernetes Operator — Simplified!](https://medium.com/@mjkool/kubernetes-operator-simplified-96b8c8f7e627)
- [medium.com/@timebertt: Kubernetes Controllers at Scale: Clients, Caches, Conflicts, Patches Explained](https://medium.com/@timebertt/kubernetes-controllers-at-scale-clients-caches-conflicts-patches-explained-aa0f7a8b4332) A developer guideline to Kubernetes clients in go. As most development in the Kubernetes space is done in Go, available client libraries for interacting with the Kubernetes API have evolved over time to make controllers more scalable.
- [openshift/machine-api-operator](https://github.com/openshift/machine-api-operator) The Machine API Operator manages the lifecycle of specific purpose CRDs, controllers and RBAC objects that extend the Kubernetes API. This allows to convey desired state of machines in a cluster in a declarative fashion
- [rancher/system-upgrade-controller: System Upgrade Controller](https://github.com/rancher/system-upgrade-controller) This project aims to provide a general-purpose, Kubernetes-native upgrade controller (for nodes). It introduces a new CRD, the Plan, for defining any and all of your upgrade policies/requirements. A Plan is an outstanding intent to mutate nodes in your cluster.
- [alenkacz.medium.com: Kubernetes operator best practices: Implementing observedGeneration](https://alenkacz.medium.com/kubernetes-operator-best-practices-implementing-observedgeneration-250728868792) There's a lot of hidden knowledge in core controllers and api conventions doc that is not followed by many controllers in the wild. One of these patterns is observedGeneration. In this article, you will learn what problems it can help solve.
- [ckotzbauer/vulnerability-operator](https://github.com/ckotzbauer/vulnerability-operator) Scans SBOMs for vulnerabilities. This operator scans all SBOMs from a git-repository for vulnerabilities using Grype. The result-list can be emitted as JSON-file served via an endpoint and/or as Prometheus metrics. There may be more targets in the future. The scans are done periodically.
- [Michaelpalacce/SimpleSecrets](https://github.com/Michaelpalacce/SimpleSecrets) K8S Secrets Manager Operator. SimpleSecrets is a secure operator that allows you to create secrets on demand. You can commit the SimpleSecrets, which are references to a database secret, and the operator will create Kubernetes Secrets automatically for you.
- [learnsteps.com: Advance Kubernetes: What exactly are Kubernetes Operators?](https://www.learnsteps.com/advanced-kubernetes-what-exactly-are-kubernetes-operators/) Kubernetes has gained a lot of traction recently and is one of the standards followed across organizations when it comes to running and managing their containerized workloads. In this article, we are going to talk about Kubernetes operators.
- [betterprogramming.pub: Build a Kubernetes Operator in 10 Minutes 🌟](https://betterprogramming.pub/build-a-kubernetes-operator-in-10-minutes-11eec1492d30)
- [alain-airom.medium.com: Kubernetes Operators Patterns and Best Practices 🌟](https://alain-airom.medium.com/kubernetes-operators-patterns-and-best-practices-b7fbaa4cbd1) Using operators to manage the lifecycle of multi-cloud, Kubernetes-based applications.
- [theregister.com: IBM launches Db2 operator for Kubenetes on AWS](https://www.theregister.com/AMP/2022/07/20/ibm_db2_operator/) Azure soon to follow as Big Blue accomodates a world with many clouds
- [OT-CONTAINER-KIT/mongodb-operator: MongoDB Operator](https://github.com/OT-CONTAINER-KIT/mongodb-operator) MongoDB Operator is an operator created in Golang to create, update, and manage MongoDB standalone, replicated, and arbiter replicated setup on Kubernetes and Openshift clusters.
- [prosimcorp/reforma](https://github.com/prosimcorp/reforma) Reforma is a Kubernetes operator to patch resources with information from other resources. It is intended to use with GitOps and lets you do things such as creating annotation on a Service Account from metadata stored in a ConfigMap.
- [weaveworks/tf-controller: Weave GitOps Terraform Controller](https://github.com/weaveworks/tf-controller) A GitOps Terraform controller for Kubernetes. Weave TF-controller is a controller for Flux to reconcile Terraform resources in the GitOps way.
- [awstip.com: Manage AWS services directly from Kubernetes - AWS Controllers for Kubernetes (ACK)](https://awstip.com/manage-aws-services-directly-from-kubernetes-%EF%B8%8F-6c94e376febb) The AWS team released the ACK project, which allows users to create AWS services from within a Kubernetes cluster. In this tutorial, you will learn how to create an S3 bucket with a "Bucket" CRD.
- [vitobotta/velero-notifications](https://github.com/vitobotta/velero-notifications) Velero-notifications is a simple Kubernetes controller written in Ruby that sends email/Slack/webhook notifications when backups or restores are performed by Velero in a Kubernetes cluster.
- [NVIDIA/gpu-operator](https://github.com/NVIDIA/gpu-operator) NVIDIA GPU Operator creates/configures/manages GPUs atop Kubernetes. The NVIDIA GPU is a Kubernetes operator that automates the management of all NVIDIA software components needed to provision GPUs. These components include drivers, the Kubernetes device plugin, the NVIDIA Container Runtime, etc.
    - [NVIDIA/k8s-device-plugin: NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin) The NVIDIA device plugin for Kubernetes is a Daemonset that allows you to automatically:
        - Expose the number of GPUs on each node of your cluster
        - Keep track of the health of your GPUs
        - Run GPU enabled containers in your Kubernetes cluster
- [medium.com/@marom.itamar: Kubernetes Controllers, Custom Resources, and Operators Explained](https://medium.com/@marom.itamar/kubernetes-controllers-custom-resources-and-operators-explained-8e92f46829f6)
- [glebiller/dynamic-configuration-operator: Dynamic Configuration Operator](https://github.com/glebiller/dynamic-configuration-operator) Dynamic Configuration Operator is an operator that updates a deployment when a ConfigMap or Secret is updated. Useful for apps that:
    - Don't have a live-reload feature
    - Use `subPath` while mounting a ConfigMap or Secret
    - Use Projected Volumes
- [==faun.pub: A Definitive guide to Kubernetes Operator — The crawl!==](https://faun.pub/a-definitive-guide-to-kubernetes-operator-the-crawl-7647b278c28b)
- [github.com/furiko-io/furiko](https://github.com/furiko-io/furiko) Cloud-native, enterprise-level cron job platform for Kubernetes. Furiko is a Kubernetes-native operator for managing, scheduling and executing scheduled and ad-hoc jobs and workflows. It aims to be a general-purpose job platform that supports various use cases, including cron jobs, batch processing, etc.
- [paul-the-kelly.medium.com: Extending the Kubernetes API using Operators](https://paul-the-kelly.medium.com/extending-the-kubernetes-api-using-operators-9ffc8364ae5c) This article is aimed at developers already familiar with Kubernetes, and who are interested in extending the capabilities of a Kubernetes cluster. The extensible Kubernetes API enables administrators to add new facilities to a cluster, simplifying the deployment and management of complex applications. This article will give you a starting point to explore building your own operators.
- [github.com/DevOps-Nirvana: Kubernetes Volume / Disk Autoscaler (via Prometheus)](https://github.com/DevOps-Nirvana/Kubernetes-Volume-Autoscaler)
    - This repository contains a Kubernetes controller that automatically increases the size of a Persistent Volume Claim in Kubernetes when it is nearing full. Initially engineered based on AWS EKS, this should support any Kubernetes cluster or cloud provider which supports dynamically hot-resizing storage volumes in Kubernetes.
    - Keeping your volumes at a minimal size can help reduce cost, but having to manually scale them up can be painful and a waste of time for an DevOps / Systems Administrator. This is often used on storage volumes against things in Kubernetes such as Prometheus, MySQL, Redis, RabbitMQ, or any other stateful service.
- [borchero/switchboard: Switchboard](https://github.com/borchero/switchboard) Kubernetes Operator for Automatically Issuing DNS Records and TLS Certificates for Traefik Ingress Routes.
- [scylladb/scylla-operator](https://github.com/scylladb/scylla-operator) Scylla Operator is a Kubernetes Operator for managing and automating tasks related to managing Scylla clusters
- [==faun.pub: Kubernetes Controllers, Custom Resources, and Operators Explained==](https://faun.pub/kubernetes-controllers-custom-resources-and-operators-explained-8e92f46829f6)
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
- [medium.com/sda-se: Kubernetes Operator to the rescue. How our own MongoDB Operator improved our deployments](https://medium.com/sda-se/kubernetes-operator-to-the-rescue-how-our-own-mongodb-operator-improved-our-deployments-6d5ba3324abc) In this article you will learn about the challenges that the team at SDA SE faced when using a GitOps deployment and why they implemented their own Kubernetes Operator for MongoDB to speed up our deployments and reduce mistakes.
- [==blog.frankel.ch: Introduction to Kubernetes extensibility== 🌟](https://blog.frankel.ch/kubernetes-extensibility/) In this article, you'll learn several extension points in Kubernetes: the data model, admission controllers, and client-side.
    - At its most basic level, Kubernetes is just a platform able to run container images. It stores its configuration in a distributed storage engine, etcd. The most significant part of this configuration is dedicated to the desired state for objects. For example, you only update this state when you schedule a pod using the kubectl command line.
    - Other components, called controllers, watch configuration changes and read the desired state. Then, they try to reconcile the desired state with the actual state. It’s nothing revolutionary: Puppet is based on the same control-loop approach, and AFAIK, Chef. Generally, a controller manages a single type of object, e.g., the DeploymentController manages deployments.
- [superorbital.io: Testing Production Kubernetes Controllers](https://superorbital.io/blog/testing-production-controllers/) In this article, you will learn how to test Kubernetes controllers using a mix of unit tests, local integration tests, and more fully featured runtime integration tests.
- [github.com/lukaszraczylo/jobs-manager-operator 🌟](https://github.com/lukaszraczylo/jobs-manager-operator)
    - [itnext.io: Simplify Advanced Workflows in Kubernetes with Jobs Manager Operator](https://itnext.io/kubernetes-operator-to-manage-jobs-7ee96744c74a) A problem and idea led to the latest invention, which saved me hours of confusion and frustration and finally untangled the web of dependencies.
- [github.com/ricoberger/vault-secrets-operator](https://github.com/ricoberger/vault-secrets-operator) Create Kubernetes secrets from Vault for a secure GitOps based workflow.
- [github.com/ElementTech/kube-reqsizer](https://github.com/ElementTech/kube-reqsizer) kube-reqsizer is a kubernetes controller that measures the usage of pods over time and optimizes their requests based on the average usage. The controller calculates the requirements based on all the samples taken in the same deployment controller.
- [==kube-green.dev==](https://kube-green.dev) An operator to reduce CO2 footprint of your clusters. Suspend your pods when no-one's using them, scale down your cluster and save energy
- [betterprogramming.pub: How To Use Server-Side Apply in K8S Operators](https://betterprogramming.pub/how-to-use-server-side-apply-in-k8s-operators-5cbff023183c) Explore the benefits of SSA vs. CSA. Server-side apply (SSA) is an excellent mechanism to improve Kubernetes operators' performance and is becoming the default way to apply resources in a cluster.
- [github.com/sieve-project/sieve](https://github.com/sieve-project/sieve) Automated Reliability Testing for Kubernetes Controllers/Operators. Sieve is a tool to help developers test their Kubernetes controllers by deterministically injecting faults and detecting dormant bugs at development time.
- [betterprogramming.pub: Goldilocks vs. KRR](https://betterprogramming.pub/goldilocks-vs-krr-c986dfd7484d) The resources recommendation showdown!. Goldilocks is a Kubernetes operator written in Go, and it watches over a few custom resources to give out its Updates or Recommendations.
- [medium.com/lonto-digital-services-integrator: Why We Developed Own Kubernetes Controller to Copy Secrets](https://medium.com/lonto-digital-services-integrator/why-we-developed-own-kubernetes-controller-to-copy-secrets-e46368ae6db9) In this article, you will learn the thought process, design decision and code that led to writing a custom controller to copy secrets from Hashicorp Vault to Kubernetes
- [thenewstack.io: HashiCorp Vault Operator Manages Kubernetes Secrets](https://thenewstack.io/hashicorp-vault-operator-manages-kubernetes-secrets/) HashiCorp's new open source project, released alongside Vault 1.13 and now available in beta, makes it easier to use Vault with Kubernetes Secrets, automating tasks that were previously manual.
- [medium.com/@senjutide2000: Designing a Controller for Custom Resources from scratch for absolute beginners](https://medium.com/@senjutide2000/designing-a-controller-for-custom-resources-from-scratch-for-absolute-beginners-9cb84b7f906f) In this tutorial (and related repository and follow-up article), you will learn how to create your first Custom Resource Definition, Custom Resource and get a basic idea of the workflow of a controller
- [github.com/2-alchemists/krossboard-kubernetes-operator](https://github.com/2-alchemists/krossboard-kubernetes-operator) Kubernetes Operator to handle cross-site, cross-distribution & multi-Kubernetes usage tracking, analytics and accounting (vanilla Kubernetes, OpenShift, EKS, AKS, GKE and other distros).
    - Krossboard is a multi-cluster and cross-distribution Kubernetes usage accounting and analytics software
    - Each instance of Krossboard enables tracking the usage of a set of Kubernetes clusters listed in a kubeconfig secret
- [medium.com/@mikakrief: Using Azure Service Operator v2](https://medium.com/@mikakrief/using-azure-service-operator-v2-4a1fa1f5e3b8) Azure Service Operator v2 is a Kubernetes operator that enables you to manage Azure resources directly through Kubernetes tooling. It’s designed to simplify the deployment and management of Azure services, allowing developers to use familiar Kubernetes commands (like kubectl apply) to handle Azure resources.
- [github.com/gianlucam76/k8s-cleaner 🌟](https://github.com/gianlucam76/k8s-cleaner) **K8s cleaner is a controller that identifies, removes, or updates stale/orphaned or unhealthy resources to maintain a clean and efficient Kubernetes cluster**
- [dragondscv.medium.com: Controller runtime — handle resource deletion with predicate](https://dragondscv.medium.com/controller-runtime-handle-resource-deletion-with-predicate-f69d09dd5802)
- [github.com/NCCloud/mayfly: Ephemeral Kubernetes Resources 🌟](https://github.com/NCCloud/mayfly) An operator to manage ephemeral Kubernetes resources
- [==itnext.io: 5 Advanced Kubernetes Operators Every DevOps Engineer Should Know About== 🌟](https://itnext.io/5-advanced-kubernetes-operators-every-devops-engineer-should-know-about-ab46bdc1c7d5) **Simplify Infrastructure Management**

## OpenTelemetry Operator

- [github.com/open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator)
- [medium.com/@magstherdev: OpenTelemetry Operator](https://medium.com/@magstherdev/opentelemetry-operator-d3d407354cbf) This post aims to demonstrate how you can implement traces in your application without any code changes by using the OpenTelemetry Operator.

## Creating Kubernetes operator using Kubebuilder

- [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) Kubebuilder - SDK for building Kubernetes APIs using CRDs. Kubebuilder is a framework for building Kubernetes APIs using custom resource definitions (CRDs). Kubebuilder increases velocity and reduces the complexity managed by developers for rapidly building and publishing Kubernetes APIs in Go.
    - https://book.kubebuilder.io
- [medium.com/@adnn.selimovic: Creating Kubernetes operator using **Kubebuilder**](https://medium.com/@adnn.selimovic/creating-kubernetes-operator-using-kubebuilder-15db5f29ee50)
- [medium.com/geekculture: A New Pattern that Simplifies Operator Building](https://medium.com/geekculture/a-new-pattern-that-simplifies-operator-building-39df5d021cfa) Build Kubernetes Operator with **Kubebuilder** and declarative pattern. kubebuilder-declarative-pattern provides a set of tools for building cluster operators with kubebuilder. Declarative operators provide a fast path to orchestrating deployments instead of reinventing the wheel i.e. "how do I get/update this YAML?"
- [qdnqn.com: Creating Kubernetes operator using Kubebuilder](https://qdnqn.com/creating-kubernetes-operator-using-kubebuilder/)
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
- [itnext.io: Testing the Operator SDK and making a prefetch mechanism for Kubernetes](https://itnext.io/testing-the-operator-sdk-and-making-a-prefetch-mechanism-for-kubernetes-7508577efdd7)
- [magalix.com: Creating Custom Kubernetes Operators](https://www.magalix.com/blog/creating-custom-kubernetes-operators)
- [medium.com: Writing Your First Kubernetes Operator](https://medium.com/faun/writing-your-first-kubernetes-operator-8f3df4453234)
- [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)
- [Writing a Kubernetes Operator in Java Cheat Sheet](https://developers.redhat.com/cheat-sheets/writing-kubernetes-operator-java/)
- [linuxera.org: Writing Operators using the Operator Framework SDK](https://linuxera.org/writing-operators-using-operator-framework/)
- [openshift.com: 7 Best Practices for Writing Kubernetes Operators: An SRE Perspective](https://www.openshift.com/blog/7-best-practices-for-writing-kubernetes-operators-an-sre-perspective)
- [medium: From Zero to Kubernetes Operator](https://medium.com/@victorpaulo/from-zero-to-kubernetes-operator-dd06436b9d89) In this post you will learn how to build a simple Kubernetes Operator. The article starts with the main concepts and then continues with hands-on labs where you will create a Kubernetes Operator from the ground up.
- [openshift.com: Build Your Kubernetes Operator With the Right Tool 🌟](https://www.openshift.com/blog/build-your-kubernetes-operator-with-the-right-tool) **Go-based operators are by far the most popular. That is why Go is probably the first option to consider.** The other good choice is Helm, especially if you already have a Helm chart for your software or you want to build your operator quickly and you don't need any complex [capability levels](https://operatorframework.io/operator-capabilities/). I'd leave Operator Frameworks or Bare Programming Language implementations only for the cases when keeping a single programming language in your organization is a priority.
- [codilime.com: How to create a custom resource with Kubernetes Operator](https://codilime.com/how-to-create-a-custom-resource-with-kubernetes-operator/) Implementing DaemonJob from scratch learn how to create a custom resource with the Kubernetes Operator Framework.
- [rookout.com: Lessons Learned When Building A Kubernetes Operator](https://www.rookout.com/blog/lessons-learned-when-building-a-kubernetes-operator)
- [pavel.cool: Oxidizing the Kubernetes operator](https://www.pavel.cool/rust/rust-kubernetes-operators/)
- [brennerm.github.io: Kubernetes operators with Python #1: Creating CRDs](https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html)
- [vivilearns2code.github.io: Writing Controllers For Kubernetes Resources](https://vivilearns2code.github.io/k8s/2021/03/11/writing-controllers-for-kubernetes-custom-resources.html)
- [cloudark.medium.com: Writing Kubernetes Custom Controllers](https://cloudark.medium.com/kubernetes-custom-controllers-b6c7d0668fdf)
- [developers.redhat.com: Managing stateful applications with Kubernetes Operators in Golang 🌟](https://developers.redhat.com/articles/2021/08/04/managing-stateful-applications-kubernetes-operators-golang) Explore this pattern by creating a Kubernetes Operator in Golang to keep a WordPress site up to date.
- [medium: Kubernetes Dummy Operator in Java](https://medium.com/xgeeks/kubernetes-dummy-operator-in-java-6b2f26198a55) - [youtube: Creating a Kubernetes Operator in Java by Rudy De Busscher](https://www.youtube.com/watch?v=C0E93Uc4h5k&t=761s&ab_channel=xgeeks)
- [betterprogramming.pub: Build a Highly Available Kubernetes Operator Using Golang](https://betterprogramming.pub/building-a-highly-available-kubernetes-operator-using-golang-fe4a44c395c2) Develop a simple Kubernetes operator from scratch. In this article, you will build a "hello world” operator using the client-go library, make adaptations to it to achieve high availability, and deploy it to a Kubernetes cluster using Helm.
- [==kubernetes/sample-controller==](https://github.com/kubernetes/sample-controller) Repository for sample controller. Complements sample-apiserver
- [betterprogramming.pub: Writing Custom Kubernetes Controller and Webhooks](https://betterprogramming.pub/writing-custom-kubernetes-controller-and-webhooks-141230820e9) Create a Kubernetes API, controller, validate webhooks, and test.
- [betterprogramming.pub: How To Write Tests for Your Kubernetes Operator](https://betterprogramming.pub/write-tests-for-your-kubernetes-operator-d3d6a9530840)
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