# Servicemesh

!!! info "Architectural Context"
    Detailed reference for Servicemesh in the context of Networking & Service Mesh.

## Table of Contents

---

  - [openshift.com: Introducing OpenShift Service Mesh 2.0 🌟](https://www.redhat.com/en/blog/introducing-openshift-service-mesh-2.0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerjournal.com: When Is Service Mesh Worth It?](https://cloudnativenow.com/features/when-is-service-mesh-worth-it)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medianova.com: Service Mesh vs. API Gateway](https://www.medianova.com/service-mesh-vs-api-gateway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [consul.io](https://developer.hashicorp.com/consul)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learn.hashicorp.com: Consul Service Mesh on Kubernetes Design Patterns](https://developer.hashicorp.com/consul/tutorials/archive/kubernetes-consul-design-patterns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [consul Connect](https://developer.hashicorp.com/consul/docs/connect)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Announcing Linkerd 2.8: simple, secure multi-cluster Kubernetes](https://linkerd.io/2020/06/09/announcing-linkerd-2.8/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkerd.io: Announcing Linkerd's Graduation](https://linkerd.io/2021/07/28/announcing-cncf-graduation/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerjournal.com: Linkerd’s CNCF Graduation Due to its Simplicity](https://cloudnativenow.com/features/linkerds-cncf-graduation-due-to-its-simplicity)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [buoyant.io: Go directly to namespace jail: Locking down network traffic between Kubernetes namespaces](https://www.buoyant.io/blog/locking-down-network-traffic-between-kubernetes-namespaces)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkerd.io: Announcing automated multi-cluster failover for Kubernetes](https://linkerd.io/2022/03/09/announcing-automated-multi-cluster-failover-for-kubernetes/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [buoyant.io: Upgrading to Linkerd 2.12: Zero-trust-ready route-based policy, Gateway API, access logging](https://www.buoyant.io/service-mesh-academy/upgrading-to-linkerd-2-12)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [buoyant.io: Multi-Cluster, Multi-Region Setup using Linkerd Service Mesh](https://www.buoyant.io/blog/multi-cluster-multi-region-setup-using-linkerd-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Maesh](https://traefik.io/traefik-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Traffic Director overview](https://docs.cloud.google.com/service-mesh/docs)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Traffic Director and gRPC—proxyless services for your service mesh](https://cloud.google.com/blog/products/networking/traffic-director-supports-proxyless-grpc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [L7 Internal HTTP(S) Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Service Mesh Ultimate Guide:](https://www.infoq.com/articles/service-mesh-ultimate-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Service Mesh Adds Security, Observability and Traffic Control to Kubernetes](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [lucperkins.dev: Service mesh use cases](https://lucperkins.dev/blog/service-mesh-use-cases)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Zero-Trust Security with Service Mesh](https://thenewstack.io/zero-trust-security-with-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Offloading Authentication and Authorization from Application Code to a Service Mesh](https://thenewstack.io/offloading-authentication-and-authorization-from-application-code-to-a-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: How a Service Mesh Can Help DevOps Achieve Business Goals](https://thenewstack.io/how-service-mesh-can-help-devops-achieve-business-goals)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Mutual TLS: Securing Microservices in Service Mesh](https://thenewstack.io/mutual-tls-microservices-encryption-for-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudops.com: Comparing Service Meshes: Istio, Linkerd, Consul Connect, and Citrix ADC](https://www.cloudops.com/blog/comparing-service-meshes-istio-linkerd-and-consul-connect-citrix-adc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Why you should care about service mesh](https://opensource.com/article/21/3/service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Service Meshes in the Cloud Native World](https://thenewstack.io/service-meshes-in-the-cloud-native-world)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [koyeb.com: Service Mesh and Microservices: Improving Network Management and Observability](https://www.koyeb.com/blog/service-mesh-and-microservices-improving-network-management-and-observability)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Accelerate Kubernetes Adoption with a Service Mesh](https://thenewstack.io/accelerate-kubernetes-adoption-with-a-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [layer5.io: The Service Mesh Landscape 🌟🌟](https://layer5.io/service-mesh-landscape)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Secure Your Service Mesh: A 13-Item Checklist](https://thenewstack.io/secure-your-service-mesh-a-13-item-checklist)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Adoption of Cloud Native Architecture, Part 3: Service Orchestration and Service Mesh](https://www.infoq.com/articles/cloud-native-architecture-adoption-part3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Stupid Simple Service Mesh — What, When, Why 🌟](https://itnext.io/stupid-simple-service-mesh-what-when-why-e9be9e5f4d41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Hidden Costs of Service Meshes](https://thenewstack.io/the-hidden-costs-of-service-meshes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnsteps.com: What is a service mesh? Is it born with Kubernetes?](https://www.learnsteps.com/what-is-a-service-mesh-is-it-born-with-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Deploying Service Mesh in Production](https://www.infoq.com/presentations/adopting-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devops.com: How Are API Management and Service Mesh Different?](https://devops.com/how-are-api-management-and-service-mesh-different)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devops.com: When to Use API Management and Service Mesh Together](https://devops.com/when-to-use-api-management-and-service-mesh-together)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: The Top-Five Challenges of Running a Service Mesh in an Enterprise 🌟](https://www.infoq.com/presentations/5-challenges-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Sidecars, eBPF and the Future of Service Mesh](https://www.infoq.com/presentations/service-mesh-ebpf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Meshery.io:](https://meshery.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Service Mesh Testing — Tools & Frameworks (Open Source)](https://itnext.io/service-mesh-testing-tools-frameworks-open-source-7904ee222298)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Fabio Load Balancer 🌟](https://fabiolb.net)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Linkerd](https://linkerd.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Linkerd 2.0: The Service Mesh for Service Owners, Platform Architects, SREs](https://thenewstack.io/linkerd-2-0-the-service-mesh-for-service-owners-platform-architects-sres)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkerd.io: Multi-cluster communication](https://linkerd.io/2.10/tasks/multicluster/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkerd.io: Benchmarking Linkerd and Istio](https://linkerd.io/2021/05/27/linkerd-vs-istio-benchmarks/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: A Practical Guide for Linkerd Authorization Policies](https://itnext.io/a-practical-guide-for-linkerd-authorization-policies-6cfdb50392e9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkerd.io: Benchmarking Linkerd and Istio: 2021 Redux](https://linkerd.io/2021/11/29/linkerd-vs-istio-benchmarks-2021/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Is Linkerd Winning the Service Mesh Race?](https://thenewstack.io/is-linkerd-winning-the-service-mesh-race)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Linkerd and GitOps](https://dev.to/thenjdevopsguy/linkerd-and-gitops-115a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [**Google Traffic Director** and the **L7 Internal Load Balancer** Intermingles **Cloud Native** and **Legacy Workloads**](https://thenewstack.io/google-traffic-director-and-the-l7-internal-load-balancer-intermingles-cloud-native-and-legacy-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Introducing Traffic Director: Google's Service Mesh Control Plane](https://www.infoq.com/news/2019/04/google-traffic-director)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Examining Load Balancing Algorithms with Envoy](https://blog.envoyproxy.io/examining-load-balancing-algorithms-with-envoy-1be643ea121c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [solo.io: Why the control plane matters. Control planes are different than data planes. Separating the control plane from data plane 🌟](https://www.solo.io/blog/why-the-control-plane-matters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [xDS REST and gRPC protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openservicemesh.io](https://openservicemesh.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kourier: A lightweight Knative Serving ingress](https://developers.redhat.com/blog/2020/06/30/kourier-a-lightweight-knative-serving-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
