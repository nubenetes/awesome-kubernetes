# Kubernetes Operators and Controllers
- [Introduction](#introduction)
- [operatorhub.io](#operatorhubio)
- [Operator Capability Levels](#operator-capability-levels)
- [Cluster Addons](#cluster-addons)
- [K8Spin Operator. Kubernetes multi-tenant operator](#k8spin-operator-kubernetes-multi-tenant-operator)
- [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
- [K8s KPIs with Kuberhealthy Operator](#k8s-kpis-with-kuberhealthy-operator)
- [Writing Kubernetes Operators and Controllers](#writing-kubernetes-operators-and-controllers)
- [Tweets](#tweets)
- [Videos](#videos)

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
- [hashicorp/terraform-k8s: Terraform Cloud Operator for Kubernetes](https://github.com/hashicorp/terraform-k8s) The Terraform Cloud Operator for Kubernetes provides first-class integration between Kubernetes and Terraform Cloud by extending the Kubernetes control plane to enable lifecycle management of cloud and on-prem infrastructure.
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
- [RBAC Manager 🌟](https://github.com/FairwindsOps/rbac-manager) A Kubernetes operator that simplifies the management of Role Bindings and Service Accounts. RBAC Manager is designed to simplify authorization in Kubernetes. This is an operator that supports declarative configuration for RBAC with new custom resources. Instead of managing role bindings or service accounts directly, you can specify a desired state and RBAC Manager will make the necessary changes to achieve that state.
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
- [medium.com/@adnn.selimovic: Creating Kubernetes operator using **Kubebuilder**](https://medium.com/@adnn.selimovic/creating-kubernetes-operator-using-kubebuilder-15db5f29ee50)
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
- [Keel 🌟](https://github.com/keel-hq/keel) Kubernetes Operator to automate Helm, DaemonSet, StatefulSet & Deployment updates.

## operatorhub.io
* [operatorhub.io](https://operatorhub.io/) OperatorHub.io is a new home for the Kubernetes community to share Operators. Find an existing Operator or list your own today.

## Operator Capability Levels
- [Operator Capability Levels](https://operatorframework.io/operator-capabilities/) Operators come in different maturity levels in regards to their lifecycle management capabilities for the application or workload they deliver. The capability models aims to provide guidance in terminology to express what features users can expect from an Operator.

## Cluster Addons
- [Cluster Addons 🌟](https://github.com/kubernetes-sigs/cluster-addons) With cluster addon operators, we are exploring a kubernetes-native way of managing addons using CRDs(Custom Resource Definitions) and controllers where the controllers encode how best to manage the addon. Installing and managing an addon could be as simple as creating a custom resource.

## K8Spin Operator. Kubernetes multi-tenant operator
- [K8Spin Operator 🌟](https://github.com/k8spin/k8spin-operator) Kubernetes multi-tenant operator. Enables multi-tenant capabilities in your Kubernetes Cluster. [We defined some small features to implement](https://github.com/k8spin/k8spin-operator/projects/1). If you know python & Kubernetes and want to contribute to this project, ping us!
- [thenewstack.io: K8Spin Provides Multitenant Isolation for Kubernetes](https://thenewstack.io/k8spin-provides-multitenant-isolation-for-kubernetes/) 
- [Discover K8Spin open source software](https://k8spin.cloud/oss-projects/)

## Flux. The GitOps Operator for Kubernetes
* [Flux 🌟](https://fluxcd.io/) The GitOps operator for Kubernetes
* [docs.fluxcd.io](https://docs.fluxcd.io/)
* [github: Flux CD](https://github.com/fluxcd/flux)
* [dzone: Developing Applications on Multi-tenant Clusters With Flux and Kustomize](https://dzone.com/articles/developing-applications-on-multitenant-clusters-wi) Take a look at how multiple teams can use the resources of a single cluster to develop an application.
* [alicegg.tech: Managing a Kubernetes cluster with Helm and FluxCD](https://alicegg.tech/2020/11/09/helm.html)

## K8s KPIs with Kuberhealthy Operator
- [K8s KPIs with Kuberhealthy 🌟](https://kubernetes.io/blog/2020/05/29/k8s-kpis-with-kuberhealthy/) transforming Kuberhealthy into a Kubernetes operator for synthetic monitoring. This new ability granted developers the means to create their own Kuberhealthy check containers to synthetically monitor their applications and clusters. Additionally, we created a guide on how to easily install and use Kuberhealthy in order to capture some helpful synthetic [KPIs](https://kpi.org/KPI-Basics).

## Writing Kubernetes Operators and Controllers
* [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* [opensource.com: Build a Kubernetes Operator in 10 minutes with Operator SDK](https://opensource.com/article/20/3/kubernetes-operator-sdk)
* [itnext.io: Testing the Operator SDK and making a prefetch mechanism for Kubernetes](https://itnext.io/testing-the-operator-sdk-and-making-a-prefetch-mechanism-for-kubernetes-7508577efdd7)
* [magalix.com: Creating Custom Kubernetes Operators](https://www.magalix.com/blog/creating-custom-kubernetes-operators)
* [medium.com: Writing Your First Kubernetes Operator](https://medium.com/faun/writing-your-first-kubernetes-operator-8f3df4453234)
* [bmc.com: What Is a Kubernetes Operator?](https://www.bmc.com/blogs/kubernetes-operator/)
* [Writing a Kubernetes Operator in Java Cheat Sheet](https://developers.redhat.com/cheat-sheets/writing-kubernetes-operator-java/)
* [linuxera.org: Writing Operators using the Operator Framework SDK](https://linuxera.org/writing-operators-using-operator-framework/)
* [openshift.com: 7 Best Practices for Writing Kubernetes Operators: An SRE Perspective](https://www.openshift.com/blog/7-best-practices-for-writing-kubernetes-operators-an-sre-perspective)
* [medium: From Zero to Kubernetes Operator](https://medium.com/@victorpaulo/from-zero-to-kubernetes-operator-dd06436b9d89) In this post you will learn how to build a simple Kubernetes Operator. The article starts with the main concepts and then continues with hands-on labs where you will create a Kubernetes Operator from the ground up.
* [openshift.com: Build Your Kubernetes Operator With the Right Tool 🌟](https://www.openshift.com/blog/build-your-kubernetes-operator-with-the-right-tool) **Go-based operators are by far the most popular. That is why Go is probably the first option to consider.** The other good choice is Helm, especially if you already have a Helm chart for your software or you want to build your operator quickly and you don't need any complex [capability levels](https://operatorframework.io/operator-capabilities/). I'd leave Operator Frameworks or Bare Programming Language implementations only for the cases when keeping a single programming language in your organization is a priority.
* [codilime.com: How to create a custom resource with Kubernetes Operator](https://codilime.com/how-to-create-a-custom-resource-with-kubernetes-operator/) Implementing DaemonJob from scratch learn how to create a custom resource with the Kubernetes Operator Framework.
* [rookout.com: Lessons Learned When Building A Kubernetes Operator](https://www.rookout.com/blog/lessons-learned-when-building-a-kubernetes-operator)
* [pavel.cool: Oxidizing the Kubernetes operator](https://www.pavel.cool/rust/rust-kubernetes-operators/)
* [brennerm.github.io: Kubernetes operators with Python #1: Creating CRDs](https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html)
* [vivilearns2code.github.io: Writing Controllers For Kubernetes Resources](https://vivilearns2code.github.io/k8s/2021/03/11/writing-controllers-for-kubernetes-custom-resources.html)
* [cloudark.medium.com: Writing Kubernetes Custom Controllers](https://cloudark.medium.com/kubernetes-custom-controllers-b6c7d0668fdf)
* [developers.redhat.com: Managing stateful applications with Kubernetes Operators in Golang 🌟](https://developers.redhat.com/articles/2021/08/04/managing-stateful-applications-kubernetes-operators-golang) Explore this pattern by creating a Kubernetes Operator in Golang to keep a WordPress site up to date.
* [medium: Kubernetes Dummy Operator in Java](https://medium.com/xgeeks/kubernetes-dummy-operator-in-java-6b2f26198a55) - [youtube: Creating a Kubernetes Operator in Java by Rudy De Busscher](https://www.youtube.com/watch?v=C0E93Uc4h5k&t=761s&ab_channel=xgeeks)
* [betterprogramming.pub: Build a Highly Available Kubernetes Operator Using Golang](https://betterprogramming.pub/building-a-highly-available-kubernetes-operator-using-golang-fe4a44c395c2) Develop a simple Kubernetes operator from scratch. In this article, you will build a "hello world” operator using the client-go library, make adaptations to it to achieve high availability, and deploy it to a Kubernetes cluster using Helm.

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