# Service Mesh

1. [Introduction](#introduction)
2. [Service Mesh and API Gateways](#service-mesh-and-api-gateways)
3. [Tools For Evaluating Service Meshes](#tools-for-evaluating-service-meshes)
4. [Service Mesh Testing](#service-mesh-testing)
5. [Consul Service Mesh](#consul-service-mesh)
    1. [Consul Connect](#consul-connect)
6. [Linkerd Service Mesh](#linkerd-service-mesh)
7. [Maesh Service Mesh](#maesh-service-mesh)
8. [Traffic Director (Google's Service Mesh)](#traffic-director-googles-service-mesh)
    1. [Google L7 Internal Load Balancer](#google-l7-internal-load-balancer)
9. [Envoy Proxy Service Mesh](#envoy-proxy-service-mesh)
    1. [xDS protocol (Envoy's Discovery Service Protocol)](#xds-protocol-envoys-discovery-service-protocol)
10. [Istio Service Mesh](#istio-service-mesh)
11. [Open Service Mesh](#open-service-mesh)
12. [Kourier](#kourier)
13. [AWS App Mesh](#aws-app-mesh)
14. [NGINX Service mesh](#nginx-service-mesh)

## Introduction

- [infoq.com: Service Mesh Ultimate Guide:](https://www.infoq.com/articles/service-mesh-ultimate-guide/)  Managing Service-to-Service Communications in the Era of Microservices
- [deloitte.com: Service Mesh en arquitecturas de microservicios](https://www2.deloitte.com/es/es/pages/technology/articles/service-mesh-en-arquitecturas-de-microservicios.html)
- [==Service meshes to the rescue: Load balancing and scaling long-lived connections in Kubernetes==](https://learnk8s.io/kubernetes-long-lived-connections)
- [blog.christianposta.com: Do I Need an API Gateway if I Use a Service Mesh?](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
- [thenewstack.io: Service Mesh Adds Security, Observability and Traffic Control to Kubernetes](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes/)
- [lucperkins.dev: Service mesh use cases](https://lucperkins.dev/blog/service-mesh-use-cases/)
- [thenewstack.io: Zero-Trust Security with Service Mesh](https://thenewstack.io/zero-trust-security-with-service-mesh/)
- [solo.io: Identity Federation for Multi-Cluster Kubernetes and Service Mesh](https://www.solo.io/blog/identity-federation-for-multi-cluster-kubernetes-and-service-mesh/)
- [cncf.io: Service Mesh Is Still Hard](https://www.cncf.io/blog/2020/10/26/service-mesh-is-still-hard/)
- [medium: Part 1 — Why Red Hat Openshift Service Mesh? 🌟](https://medium.com/@maggarwa/part-1-why-red-hat-openshift-service-mesh-54b8b6ae1a8f)
- [openshift.com: Introducing OpenShift Service Mesh 2.0 🌟](https://www.openshift.com/blog/introducing-openshift-service-mesh-2.0)
- [weave.works: Introduction to Service Meshes on Kubernetes and Progressive Delivery 🌟](https://www.weave.works/blog/introduction-to-service-meshes-on-kubernetes-and-progressive-delivery)
- [rancher.com: Using Hybrid and Multi-Cloud Service Mesh Based Applications for Distributed Deployments](https://rancher.com/blog/2020/hybrid-multi-cloud-service-mesh-based-applications-distributed-deployments) Service Mesh addresses the communication requirements typical in a microservices-based application, including encrypted tunnels, health checks, circuit breakers, load balancing and traffic permission. Leaving the microservices to address these requirements leads to an expensive and time consuming development process. In this blog, we’ll provide an overview of the most common microservice communication requirements that the Service Mesh architecture pattern solves.
- [thenewstack.io: Offloading Authentication and Authorization from Application Code to a Service Mesh](https://thenewstack.io/offloading-authentication-and-authorization-from-application-code-to-a-service-mesh/)
- [thenewstack.io: How a Service Mesh Can Help DevOps Achieve Business Goals](https://thenewstack.io/how-service-mesh-can-help-devops-achieve-business-goals/)
- [thenewstack.io: Mutual TLS: Securing Microservices in Service Mesh](https://thenewstack.io/mutual-tls-microservices-encryption-for-service-mesh/)
- [medium: Service Mesh with Istio](https://medium.com/cloud-techies/service-mesh-with-istio-a0d045a28165)
- [rancher.com: Using Hybrid and Multi-Cloud Service Mesh Based Applications for Distributed Deployments. Get Hands-On with Rancher, Kong and Kong Mesh 🌟](https://rancher.com/blog/2020/hybrid-multi-cloud-service-mesh-based-applications-distributed-deployments)
    - Service Mesh is an emerging architecture pattern gaining traction today. Along with Kubernetes, Service Mesh can form a powerful platform which addresses the technical requirements that arise in a highly distributed environment typically found on a microservices cluster and/or service infrastructure. A Service Mesh is a dedicated infrastructure layer for facilitating service-to-service communications between microservices.
    - Service Mesh addresses the communication requirements typical in a microservices-based application, including encrypted tunnels, health checks, circuit breakers, load balancing and traffic permission. Leaving the microservices to address these requirements leads to an expensive and time consuming development process.
    - Kong provides an enterprise-class and comprehensive service connectivity platform that includes an API gateway, a Kubernetes ingress controller and a Service Mesh implementation. The platform allows customers to deploy on multiple environments such as on premises, hybrid, multi-­­­­­­region and multi-cloud.
- [cloudops.com: Comparing Service Meshes: Istio, Linkerd, Consul Connect, and Citrix ADC](https://www.cloudops.com/blog/comparing-service-meshes-istio-linkerd-and-consul-connect-citrix-adc/)
- [platform9.com: Kubernetes Service Mesh: A Comparison of Istio, Linkerd and Consul](https://platform9.com/blog/kubernetes-service-mesh-a-comparison-of-istio-linkerd-and-consul/)
- [opensource.com: Why you should care about service mesh](https://opensource.com/article/21/3/service-mesh) Service mesh provides benefits for development and operations in microservices environments.
- [==containerjournal.com: When Is Service Mesh Worth It?==](https://containerjournal.com/features/when-is-service-mesh-worth-it/)
- [thenewstack.io: Service Meshes in the Cloud Native World](https://thenewstack.io/service-meshes-in-the-cloud-native-world/)
- [koyeb.com: Service Mesh and Microservices: Improving Network Management and Observability](https://www.koyeb.com/blog/service-mesh-and-microservices-improving-network-management-and-observability)
- [thenewstack.io: Accelerate Kubernetes Adoption with a Service Mesh](https://thenewstack.io/accelerate-kubernetes-adoption-with-a-service-mesh/)
- [toptal.com: A Kubernetes Service Mesh Comparison 🌟](https://www.toptal.com/kubernetes/service-mesh-comparison)
- [nginx.com: How to Choose a Service Mesh 🌟](https://www.nginx.com/blog/how-to-choose-a-service-mesh/)
- [cncf.io: Networking with a service mesh: use cases, best practices, and comparison of top mesh options](https://www.cncf.io/blog/2021/07/15/networking-with-a-service-mesh-use-cases-best-practices-and-comparison-of-top-mesh-options/)
- [layer5.io: The Service Mesh Landscape 🌟🌟](https://layer5.io/service-mesh-landscape) Comparison of Service Mesh Strengths
- [blog.polymatic.systems: Service Mesh Wars, Goodbye Istio](https://blog.polymatic.systems/service-mesh-wars-goodbye-istio-b047d9e533c7) After using Istio in production for almost 2 years, we’re saying goodbye to it. Learn why, as well as the current state of the Service Mesh Wars.
- [thenewstack.io: Secure Your Service Mesh: A 13-Item Checklist](https://thenewstack.io/secure-your-service-mesh-a-13-item-checklist/)
- [infoq.com: Adoption of Cloud Native Architecture, Part 3: Service Orchestration and Service Mesh](https://www.infoq.com/articles/cloud-native-architecture-adoption-part3/)
- [infoq.com: Service Mesh Ultimate Guide - Second Edition: Next Generation Microservices Development](https://www.infoq.com/articles/service-mesh-ultimate-guide-2e/)
- [==itnext.io: Stupid Simple Service Mesh — What, When, Why== 🌟](https://itnext.io/stupid-simple-service-mesh-what-when-why-e9be9e5f4d41)
- [thenewstack.io: The Hidden Costs of Service Meshes](https://thenewstack.io/the-hidden-costs-of-service-meshes/)
- [learnsteps.com: What is a service mesh? Is it born with Kubernetes?](https://www.learnsteps.com/what-is-a-service-mesh-is-it-born-with-kubernetes/)
- [==medium: Microservices and the World with a Service Mesh== | Adarsh Prabhu](https://medium.com/@adarsh.prabhu/microservices-and-the-world-with-a-service-mesh-ec9a709dd4b5) We will look at how the unruly world of distributed microservices can be tamed by using a Service Mesh. Service Meshes form the backbone of some of the very complex applications out there. They solve critical issues of the microservices architecture and provide better Traffic Management, Security and Observability. In most cases these features are enabled without requiring any code changes.
- [digitalanarchist.com:  Service Mesh – Mark Chesire, Red Hat (video)](https://digitalanarchist.com/videos/featured-guests/service-mesh-red-hat) When should you look at using a ServiceMesh and/or APIManagement? Mark Chesire, director of product for application services at Red Hat, explains why IT organizations will need a service mesh to manage APIs.
- [infoq.com: Deploying Service Mesh in Production](https://www.infoq.com/presentations/adopting-service-mesh)
- [==devops.com: How Are API Management and Service Mesh Different?==](https://devops.com/how-are-api-management-and-service-mesh-different/)
- [devops.com: When to Use API Management and Service Mesh Together](https://devops.com/when-to-use-api-management-and-service-mesh-together/)
- [infoq.com: Deploying Service Mesh in Production](https://www.infoq.com/presentations/adopting-service-mesh/)
- [infoq.com: The Top-Five Challenges of Running a Service Mesh in an Enterprise 🌟](https://www.infoq.com/presentations/5-challenges-mesh/)
- [medium.com/elca-it: Service Mesh Performance Evaluation — Istio, Linkerd, Kuma and Consul](https://medium.com/elca-it/service-mesh-performance-evaluation-istio-linkerd-kuma-and-consul-d8a89390d630)
- [medium.com/@pauldotyu: Service Mesh Considerations](https://medium.com/@pauldotyu/service-mesh-considerations-117561f30295)
- [medium.com/4th-coffee: A Comprehensive Tutorial on Service Mesh, Istio, Envoy, Access Log, and Log Filtering](https://medium.com/4th-coffee/a-comprehensive-tutorial-on-service-mesh-istio-envoy-access-log-and-log-filtering-8f3d939c081d)
- [infoq.com: Sidecars, eBPF and the Future of Service Mesh](https://www.infoq.com/presentations/service-mesh-ebpf/)

## Service Mesh and API Gateways

- [medium: The Roles of Service Mesh and API Gateways in Microservice Architecture 🌟](https://medium.com/better-programming/the-roles-of-service-mesh-and-api-gateways-in-microservice-architecture-f6e7dfd61043)
- [medianova.com: Service Mesh vs. API Gateway](https://www.medianova.com/en-blog/service-mesh-vs-api-gateway/)

## Tools For Evaluating Service Meshes

- [Meshery.io:](https://meshery.io/) Open source tool for evaluating and contrasting service meshes

## Service Mesh Testing

- [itnext.io: Service Mesh Testing — Tools & Frameworks (Open Source)](https://itnext.io/service-mesh-testing-tools-frameworks-open-source-7904ee222298) There are quite a few open-source toolsets to test and measure performance impact of service meshes. In this article you will compare: Fortio, Nighthawk, Wrk2, Httpbin, Meshery, Isotope, Hyperfoil, Service-mesh-benchmark, Locust & more.

## Consul Service Mesh

- [consul.io](https://www.consul.io/)
- [medium: Consul in Kubernetes — Pushing to Production](https://medium.com/swlh/consul-in-kubernetes-pushing-to-production-223506bbe8db)
- [medium: HashiCorp Consul: Multi-Cloud and Multi-Platform Service Mesh](https://medium.com/hashicorp-engineering/hashicorp-consul-multi-cloud-and-multi-platform-service-mesh-372a82264e8e)
- [hashicorp.com: Get Started with Consul Service Mesh on Kubernetes 🌟](https://www.hashicorp.com/blog/get-started-with-consul-service-mesh-on-kubernetes/)
- [HashiCorp Consul Ingress Gateways and L7 Traffic Management in Kubernetes](https://www.hashicorp.com/blog/hashicorp-consul-ingress-gateways-and-l7-traffic-management-in-kubernetes) Learn about the advanced features of HashiCorp's Consul service mesh that are valuable to both infrastructure operators and developers.
- [hashicorp.com: HashiCorp Consul Ingress Gateways and L7 Traffic Management in Kubernetes 🌟](https://www.hashicorp.com/blog/hashicorp-consul-ingress-gateways-and-l7-traffic-management-in-kubernetes)
- [learn.hashicorp.com: Consul Service Mesh on Kubernetes Design Patterns](https://learn.hashicorp.com/tutorials/consul/kubernetes-consul-design-patterns)
- [hashicorp.com: Disaster Recovery for HashiCorp Consul on Kubernetes 🌟](https://www.hashicorp.com/blog/disaster-recovery-for-hashicorp-consul-on-kubernetes) See the recovery steps to protect your data and secrets during an extended outage using Kubernetes and HashiCorp Consul.
- [medium: A Practical Guide to HashiCorp Consul — Part 1 🌟](https://medium.com/velotio-perspectives/a-practical-guide-to-hashicorp-consul-part-1-5ee778a7fcf4)
    - [medium: A Practical Guide to HashiCorp Consul — Part 2 🌟](https://medium.com/velotio-perspectives/a-practical-guide-to-hashicorp-consul-part-2-3c0ebc0351e8)
- [Fabio Load Balancer 🌟](https://fabiolb.net/) fabio is a fast, modern, zero-conf load balancing HTTP(S) and TCP router for deploying applications managed by consul. Register your services in consul, provide a health check and fabio will start routing traffic to them. No configuration required. Deployment, upgrading and refactoring has never been easier.
- [hashicorp.com: Getting Started with HCP Consul: Frequently Asked Questions](https://www.hashicorp.com/blog/getting-started-with-hcp-consul-frequently-asked-questions)

### Consul Connect

- [consul Connect](https://www.consul.io/docs/connect/index.html)

## Linkerd Service Mesh

- [Linkerd](https://linkerd.io/)
- [Announcing Linkerd 2.8: simple, secure multi-cluster Kubernetes](https://linkerd.io/2020/06/09/announcing-linkerd-2.8/)
- [cncf.io: Kubernetes network policies with Cilium and Linkerd](https://www.cncf.io/blog/2021/02/25/kubernetes-network-policies-with-cilium-and-linkerd/)
- [cncf.io: Protocol detection and opaque ports in Linkerd](https://www.cncf.io/blog/2021/03/10/protocol-detection-and-opaque-ports-in-linkerd/)
- [thenewstack.io: Linkerd 2.0: The Service Mesh for Service Owners, Platform Architects, SREs](https://thenewstack.io/linkerd-2-0-the-service-mesh-for-service-owners-platform-architects-sres/)
- [cncf.io: Why Linkerd doesn’t use Envoy](https://www.cncf.io/blog/2020/12/11/why-linkerd-doesnt-use-envoy/)
- [linkerd.io: Multi-cluster communication](https://linkerd.io/2.10/tasks/multicluster/index.html) This guide will walk you through installing and configuring Linkerd so that two clusters can talk to services hosted on both.
- [linkerd.io: Benchmarking Linkerd and Istio](https://linkerd.io/2021/05/27/linkerd-vs-istio-benchmarks/index.html)
- [nais.io: Changing Service Mesh](https://nais.io/blog/posts/2021/05/changing-service-mesh.html) How we swapped Istio with Linkerd with hardly any downtime
- [linkerd.io: Announcing Linkerd's Graduation](https://linkerd.io/2021/07/28/announcing-cncf-graduation/)
- [containerjournal.com: Linkerd’s CNCF Graduation Due to its Simplicity](https://containerjournal.com/features/linkerds-cncf-graduation-due-to-its-simplicity/)
- [nais.io: Changing Service Mesh](https://nais.io/blog/posts/2021/05/changing-service-mesh.html) How we swapped Istio with Linkerd with hardly any downtime
- [itnext.io: A Practical Guide for Linkerd Authorization Policies](https://itnext.io/a-practical-guide-for-linkerd-authorization-policies-6cfdb50392e9)
- "Installed Linkerd in staging yesterday using Helm and Terraform. It was incredibly easy to setup and immediately helped me diagnose tricky latency issues between services. I have no idea why I didn’t do this sooner. Can’t wait to get this into production."
- [linkerd.io: Benchmarking Linkerd and Istio: 2021 Redux](https://linkerd.io/2021/11/29/linkerd-vs-istio-benchmarks-2021/index.html)
- [buoyant.io: Go directly to namespace jail: Locking down network traffic between Kubernetes namespaces](https://buoyant.io/2021/12/14/locking-down-network-traffic-between-kubernetes-namespaces)
- [linkerd.io: Announcing automated multi-cluster failover for Kubernetes](https://linkerd.io/2022/03/09/announcing-automated-multi-cluster-failover-for-kubernetes/)
- [thenewstack.io: Is Linkerd Winning the Service Mesh Race?](https://thenewstack.io/is-linkerd-winning-the-service-mesh-race/)
- [medium.com/attest-product-and-technology: Debugging mislabelled route metrics from Linkerd](https://medium.com/attest-product-and-technology/debugging-mislabelled-route-metrics-from-linkerd-dda47fdff04a)
- [buoyant.io: Upgrading to Linkerd 2.12: Zero-trust-ready route-based policy, Gateway API, access logging](https://buoyant.io/service-mesh-academy/upgrading-to-linkerd-2-12) In this webinar, you'll hear all about the Linkerd 2.12 release and what you need to know to upgrade. This massive release introduces route-based policy to Linkerd, allowing users to define and enforce authorization policies based on HTTP paths or gRPC methods in a fully zero-trust way. It also introduces support for iptables-nft and Apache-style access logging, authorizes all probes by default (even in default-deny clusters), and includes a host of other improvements and performance enhancements.
- [medium.com/@eshiett314: Mutual TLS with Emissary-Ingress and Linkerd](https://medium.com/@eshiett314/mutual-tls-with-emissary-ingress-and-linkerd-4aa3ffe0413f) In this article, you'll learn the meaning of Mutual TLS, why it is needed in Kubernetes and also implement it with Emissary-ingress
- [weeraman.com: Getting started with Linkerd](https://weeraman.com/getting-started-with-linkerd-415d6485227f)
- [dev.to: Linkerd and GitOps](https://dev.to/thenjdevopsguy/linkerd-and-gitops-115a)
- [buoyant.io: Multi-Cluster, Multi-Region Setup using Linkerd Service Mesh](https://buoyant.io/blog/multi-cluster-multi-region-setup-using-linkerd-service-mesh) This article teaches how to enhance Kubernetes with multi-cluster architecture for improved availability, fault tolerance, and performance with a Service Mesh such as Linkerd

## Maesh Service Mesh

- [Maesh](https://containo.us/maesh/)

## Traffic Director (Google's Service Mesh)

- [Traffic Director overview](https://cloud.google.com/traffic-director)
- [Google Cloud’s Traffic Director — What is it and how is it related to the Istio service-mesh?](https://medium.com/cloudzone/google-clouds-traffic-director-what-is-it-and-how-is-it-related-to-the-istio-service-mesh-c199acc64a6d)
- [**Google Traffic Director** and the **L7 Internal Load Balancer** Intermingles **Cloud Native** and **Legacy Workloads**](https://thenewstack.io/google-traffic-director-and-the-l7-internal-load-balancer-intermingles-cloud-native-and-legacy-workloads/)
- [infoq.com: Introducing Traffic Director: Google's Service Mesh Control Plane](https://www.infoq.com/news/2019/04/google-traffic-director/)
- [Traffic Director and gRPC—proxyless services for your service mesh](https://cloudblog.withgoogle.com/products/networking/traffic-director-supports-proxyless-grpc/amp/)

### Google L7 Internal Load Balancer

- [L7 Internal HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/l7-internal/)

## Envoy Proxy Service Mesh

- [Envoy](https://www.envoyproxy.io/)
- [Examining Load Balancing Algorithms with Envoy](https://blog.envoyproxy.io/examining-load-balancing-algorithms-with-envoy-1be643ea121c)
- [solo.io: Why the control plane matters. Control planes are different than data planes. Separating the control plane from data plane 🌟](https://www.solo.io/blog/why-the-control-plane-matters/)
- [ekglue - Envoy/Kubernetes glue](https://github.com/jrockway/ekglue) Glue the Kubernetes API to Envoy's xDS APIs
- [amalaruja.medium.com: Basic HTTP Routing Strategies with Envoy](https://amalaruja.medium.com/basic-http-routing-strategies-with-envoy-376be42559eb)

### xDS protocol (Envoy's Discovery Service Protocol)

- [xDS REST and gRPC protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)
- "The [gRPC project](https://grpc.io/faq/) is adding support for the **xDS protocol**, think Envoy Proxy as a library, which will provide a subset of functionality without an external proxy. 🤯 The best part, xDS based control planes such as Istio, Traffic Director, and Consul Connect should just work." Kelsey Hightower

## Istio Service Mesh

- [Istio](istio.md)

## Open Service Mesh

- [openservicemesh.io](https://openservicemesh.io/)

## Kourier

- [Kourier: A lightweight Knative Serving ingress](https://developers.redhat.com/blog/2020/06/30/kourier-a-lightweight-knative-serving-ingress/)
- https://github.com/knative/net-kourier : Kourier is an Ingress for Knative Serving. Kourier is a lightweight alternative for the Istio ingress as its deployment consists only of an Envoy proxy and a control plane for it.

## AWS App Mesh

- [AWS App Mesh with EKS and Canary deployment](https://medium.com/@anupam.s1602/aws-app-mesh-with-eks-and-canary-deployment-5503d9ba95d6)

## NGINX Service mesh

- [nginx.com: Introducing NGINX Service Mesh](https://www.nginx.com/blog/introducing-nginx-service-mesh/)
- [nginx.com: The mTLS Architecture in NGINX Service Mesh](https://www.nginx.com/blog/mtls-architecture-nginx-service-mesh/)