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
- [==Service meshes to the rescue: Load balancing and scaling long-lived connections in Kubernetes==](https://learnk8s.io/kubernetes-long-lived-connections)
- [blog.christianposta.com: Do I Need an API Gateway if I Use a Service Mesh?](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
- [thenewstack.io: Service Mesh Adds Security, Observability and Traffic Control to Kubernetes](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes/)
- [lucperkins.dev: Service mesh use cases](https://lucperkins.dev/blog/service-mesh-use-cases/)
- [thenewstack.io: Zero-Trust Security with Service Mesh](https://thenewstack.io/zero-trust-security-with-service-mesh/)
- [solo.io: Identity Federation for Multi-Cluster Kubernetes and Service Mesh](https://www.solo.io/blog/identity-federation-for-multi-cluster-kubernetes-and-service-mesh/)
- [openshift.com: Introducing OpenShift Service Mesh 2.0 🌟](https://www.openshift.com/blog/introducing-openshift-service-mesh-2.0)
- [weave.works: Introduction to Service Meshes on Kubernetes and Progressive Delivery 🌟](https://www.weave.works/blog/introduction-to-service-meshes-on-kubernetes-and-progressive-delivery)
- [rancher.com: Using Hybrid and Multi-Cloud Service Mesh Based Applications for Distributed Deployments](https://rancher.com/blog/2020/hybrid-multi-cloud-service-mesh-based-applications-distributed-deployments) Service Mesh addresses the communication requirements typical in a microservices-based application, including encrypted tunnels, health checks, circuit breakers, load balancing and traffic permission. Leaving the microservices to address these requirements leads to an expensive and time consuming development process. In this blog, we’ll provide an overview of the most common microservice communication requirements that the Service Mesh architecture pattern solves.
- [thenewstack.io: Offloading Authentication and Authorization from Application Code to a Service Mesh](https://thenewstack.io/offloading-authentication-and-authorization-from-application-code-to-a-service-mesh/)
- [thenewstack.io: How a Service Mesh Can Help DevOps Achieve Business Goals](https://thenewstack.io/how-service-mesh-can-help-devops-achieve-business-goals/)
- [thenewstack.io: Mutual TLS: Securing Microservices in Service Mesh](https://thenewstack.io/mutual-tls-microservices-encryption-for-service-mesh/)
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
- [nginx.com: How to Choose a Service Mesh 🌟](https://www.nginx.com/blog/how-to-choose-a-service-mesh/)
- [layer5.io: The Service Mesh Landscape 🌟🌟](https://layer5.io/service-mesh-landscape) Comparison of Service Mesh Strengths
- [thenewstack.io: Secure Your Service Mesh: A 13-Item Checklist](https://thenewstack.io/secure-your-service-mesh-a-13-item-checklist/)
- [infoq.com: Adoption of Cloud Native Architecture, Part 3: Service Orchestration and Service Mesh](https://www.infoq.com/articles/cloud-native-architecture-adoption-part3/)
- [infoq.com: Service Mesh Ultimate Guide - Second Edition: Next Generation Microservices Development](https://www.infoq.com/articles/service-mesh-ultimate-guide-2e/)
- [thenewstack.io: The Hidden Costs of Service Meshes](https://thenewstack.io/the-hidden-costs-of-service-meshes/)
- [learnsteps.com: What is a service mesh? Is it born with Kubernetes?](https://www.learnsteps.com/what-is-a-service-mesh-is-it-born-with-kubernetes/)
- [infoq.com: Deploying Service Mesh in Production](https://www.infoq.com/presentations/adopting-service-mesh)
- [infoq.com: The Top-Five Challenges of Running a Service Mesh in an Enterprise 🌟](https://www.infoq.com/presentations/5-challenges-mesh/)
- [infoq.com: Sidecars, eBPF and the Future of Service Mesh](https://www.infoq.com/presentations/service-mesh-ebpf/)

## Service Mesh and API Gateways

- [medianova.com: Service Mesh vs. API Gateway](https://www.medianova.com/en-blog/service-mesh-vs-api-gateway/)

## Tools For Evaluating Service Meshes

- [Meshery.io:](https://meshery.io/) Open source tool for evaluating and contrasting service meshes

## Service Mesh Testing


## Consul Service Mesh

- [consul.io](https://www.consul.io/)
- [learn.hashicorp.com: Consul Service Mesh on Kubernetes Design Patterns](https://learn.hashicorp.com/tutorials/consul/kubernetes-consul-design-patterns)
- [Fabio Load Balancer 🌟](https://fabiolb.net/) fabio is a fast, modern, zero-conf load balancing HTTP(S) and TCP router for deploying applications managed by consul. Register your services in consul, provide a health check and fabio will start routing traffic to them. No configuration required. Deployment, upgrading and refactoring has never been easier.

### Consul Connect

- [consul Connect](https://www.consul.io/docs/connect/index.html)

## Linkerd Service Mesh

- [Linkerd](https://linkerd.io/)
- [Announcing Linkerd 2.8: simple, secure multi-cluster Kubernetes](https://linkerd.io/2020/06/09/announcing-linkerd-2.8/)
- [thenewstack.io: Linkerd 2.0: The Service Mesh for Service Owners, Platform Architects, SREs](https://thenewstack.io/linkerd-2-0-the-service-mesh-for-service-owners-platform-architects-sres/)
- [linkerd.io: Multi-cluster communication](https://linkerd.io/2.10/tasks/multicluster/index.html) This guide will walk you through installing and configuring Linkerd so that two clusters can talk to services hosted on both.
- [linkerd.io: Benchmarking Linkerd and Istio](https://linkerd.io/2021/05/27/linkerd-vs-istio-benchmarks/index.html)
- [linkerd.io: Announcing Linkerd's Graduation](https://linkerd.io/2021/07/28/announcing-cncf-graduation/)
- [containerjournal.com: Linkerd’s CNCF Graduation Due to its Simplicity](https://containerjournal.com/features/linkerds-cncf-graduation-due-to-its-simplicity/)
- "Installed Linkerd in staging yesterday using Helm and Terraform. It was incredibly easy to setup and immediately helped me diagnose tricky latency issues between services. I have no idea why I didn’t do this sooner. Can’t wait to get this into production."
- [linkerd.io: Benchmarking Linkerd and Istio: 2021 Redux](https://linkerd.io/2021/11/29/linkerd-vs-istio-benchmarks-2021/index.html)
- [buoyant.io: Go directly to namespace jail: Locking down network traffic between Kubernetes namespaces](https://buoyant.io/2021/12/14/locking-down-network-traffic-between-kubernetes-namespaces)
- [linkerd.io: Announcing automated multi-cluster failover for Kubernetes](https://linkerd.io/2022/03/09/announcing-automated-multi-cluster-failover-for-kubernetes/)
- [thenewstack.io: Is Linkerd Winning the Service Mesh Race?](https://thenewstack.io/is-linkerd-winning-the-service-mesh-race/)
- [buoyant.io: Upgrading to Linkerd 2.12: Zero-trust-ready route-based policy, Gateway API, access logging](https://buoyant.io/service-mesh-academy/upgrading-to-linkerd-2-12) In this webinar, you'll hear all about the Linkerd 2.12 release and what you need to know to upgrade. This massive release introduces route-based policy to Linkerd, allowing users to define and enforce authorization policies based on HTTP paths or gRPC methods in a fully zero-trust way. It also introduces support for iptables-nft and Apache-style access logging, authorizes all probes by default (even in default-deny clusters), and includes a host of other improvements and performance enhancements.
- [dev.to: Linkerd and GitOps](https://dev.to/thenjdevopsguy/linkerd-and-gitops-115a)
- [buoyant.io: Multi-Cluster, Multi-Region Setup using Linkerd Service Mesh](https://buoyant.io/blog/multi-cluster-multi-region-setup-using-linkerd-service-mesh) This article teaches how to enhance Kubernetes with multi-cluster architecture for improved availability, fault tolerance, and performance with a Service Mesh such as Linkerd

## Maesh Service Mesh

- [Maesh](https://containo.us/maesh/)

## Traffic Director (Google's Service Mesh)

- [Traffic Director overview](https://cloud.google.com/traffic-director)
- [**Google Traffic Director** and the **L7 Internal Load Balancer** Intermingles **Cloud Native** and **Legacy Workloads**](https://thenewstack.io/google-traffic-director-and-the-l7-internal-load-balancer-intermingles-cloud-native-and-legacy-workloads/)
- [infoq.com: Introducing Traffic Director: Google's Service Mesh Control Plane](https://www.infoq.com/news/2019/04/google-traffic-director/)
- [Traffic Director and gRPC—proxyless services for your service mesh](https://cloudblog.withgoogle.com/products/networking/traffic-director-supports-proxyless-grpc/amp/)

### Google L7 Internal Load Balancer

- [L7 Internal HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/l7-internal/)

## Envoy Proxy Service Mesh

- [Envoy](https://www.envoyproxy.io/)
- [solo.io: Why the control plane matters. Control planes are different than data planes. Separating the control plane from data plane 🌟](https://www.solo.io/blog/why-the-control-plane-matters/)
- [ekglue - Envoy/Kubernetes glue](https://github.com/jrockway/ekglue) Glue the Kubernetes API to Envoy's xDS APIs

### xDS protocol (Envoy's Discovery Service Protocol)

- [xDS REST and gRPC protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)
- "The [gRPC project](https://grpc.io/faq/) is adding support for the **xDS protocol**, think Envoy Proxy as a library, which will provide a subset of functionality without an external proxy. 🤯 The best part, xDS based control planes such as Istio, Traffic Director, and Consul Connect should just work." Kelsey Hightower

## Istio Service Mesh

- [Istio](istio.md)

## Open Service Mesh

- [openservicemesh.io](https://openservicemesh.io/)

## Kourier

- https://github.com/knative/net-kourier : Kourier is an Ingress for Knative Serving. Kourier is a lightweight alternative for the Istio ingress as its deployment consists only of an Envoy proxy and a control plane for it.

## AWS App Mesh


## NGINX Service mesh

- [nginx.com: Introducing NGINX Service Mesh](https://www.nginx.com/blog/introducing-nginx-service-mesh/)
- [nginx.com: The mTLS Architecture in NGINX Service Mesh](https://www.nginx.com/blog/mtls-architecture-nginx-service-mesh/)