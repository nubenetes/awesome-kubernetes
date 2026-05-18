# Istio

!!! info "Architectural Context"
    Detailed reference for Istio in the context of Networking & Service Mesh.

## Table of Contents

---

  - [karlstoney.com: Istio 503's with UC's and TCP Fun Times](https://karlstoney.com/istio-503s-ucs-and-tcp-fun-times)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Red Hat OpenShift Service Mesh is now available: What you should know 🌟](https://www.redhat.com/en/blog/red-hat-openshift-service-mesh-is-now-available-what-you-should-know)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [The Istio project just consolidated its control plane services: Pilot, Citadel, Galley, and the sidecar injector, into a single binary, __Istiod__](https://istio.io/latest/blog/2020/tradewinds-2020/#fewer-moving-parts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Monitoring Services like an SRE in OpenShift ServiceMesh Part 2: Collecting Standard Metrics 🌟](https://www.redhat.com/en/blog/monitoring-services-like-an-sre-in-openshift-servicemesh-part-2-collecting-standard-metrics-3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [solo.io: Identity Federation for Multi-Cluster Kubernetes and Service Mesh](https://www.solo.io/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: How to monitor Istio, the Kubernetes service mesh](https://www.sysdig.com/blog/monitor-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tetrate.io: VM to container communications 101](https://tetrate.io/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tetrate.io: Why do you need Istio when you already have Kubernetes?](https://tetrate.io/blog/what-is-istio-and-why-does-kubernetes-need-it)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tetrate.io: Using Istio Service Mesh as API Gateway 🌟](https://tetrate.io/blog/istio-service-mesh-api-gateway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jimmysong.io: Understanding the Sidecar Injection, Traffic Intercepting & Routing Process in Istio](https://jimmysong.io/blog/sidecar-injection-iptables-and-traffic-routing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.getambassador.io: Kubernetes Canary Testing and Release with Istio](https://blog.getambassador.io/kubernetes-canary-testing-and-release-with-istio-4cbdedcc9914?gi=a8be5865b1c9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kiali.io](https://kiali.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [getenvoy.io](https://www.envoyproxy.io/docs/envoy/latest/start/install)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Istio.io](https://istio.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com: Istio](https://github.com/istio/istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat Developer: Istio Service Mesh](https://developers.redhat.com/topics/service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.christianposta.com: Istio as an Example of When Not to Do Microservices](https://blog.christianposta.com/microservices/istio-as-an-example-of-when-not-to-do-microservices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/askmeegs/learn-istio 🌟](https://github.com/askmeegs/learn-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Riding the Tiger: Lessons Learned Implementing Istio 🌟](https://zwischenzugs.com/2020/05/05/riding-the-tiger-lessons-learned-implementing-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/aurelievache: Understanding Istio: part 1 – Istio Components](https://dev.to/aurelievache/understanding-istio-part-1-istio-components-4ik5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [istio.io: Learn Microservices using Kubernetes and Istio 🌟](https://istio.io/latest/docs/examples/microservices-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io - Service Mesh: The Gateway to Cloud Migration](https://thenewstack.io/when-you-need-or-dont-need-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kubernetes, Microservices, and Istio  — A Great Fit!](https://thenewstack.io/kubernetes-microservices-istio%E2%80%8A-%E2%80%8Aa-great-fit)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [solo.io: Learn how to rate limit requests in Istio 🌟](https://www.solo.io/blog/tutorial-rate-limiting-of-service-requests-in-istio-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redhat-scholars: istio-tutorial 🌟](https://github.com/redhat-scholars/istio-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Why Do You Need Istio When You Already Have Kubernetes? 🌟](https://thenewstack.io/why-do-you-need-istio-when-you-already-have-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Solo.io: Istio Is Winning the Service Mesh War](https://thenewstack.io/solo-io-istio-is-winning-the-service-mesh-war)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learncloudnative.com: Attach multiple VirtualServices to Istio Gateway](https://learncloudnative.com/blog/2020-11-23-multiple-vs-gateway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: What Is Istio and Why Does Kubernetes Need it? 🌟](https://thenewstack.io/what-is-istio-and-why-does-kubernetes-need-it)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Istio & Service Mesh - simply explained in 15 mins 🌟](https://www.youtube.com/watch?v=16fgzklcF7Y&ab_channel=TechWorldwithNana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: A GitOps recipe for Progressive Delivery with Istio 🌟](https://dev.to/stefanprodan/a-gitops-recipe-for-progressive-delivery-2pa3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [samos-it.com: Securing Redis with Istio TLS origination](https://samos-it.com/posts/securing-redis-istio-tls-origniation-termination.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Istio 1.10 Improves Scalability and Revision Control](https://thenewstack.io/istio-1-10-improves-scalability-and-revision-control)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [istio.io: Configuring failover for external services](https://istio.io/latest/blog/2021/external-locality-failover)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Multicluster Management with Kubernetes and Istio](https://thenewstack.io/multicluster-management-with-kubernetes-and-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [piotrminkowski.com: Multicluster Traffic Mirroring with Istio and Kind](https://piotrminkowski.com/2021/07/12/multicluster-traffic-mirroring-with-istio-and-kind)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Securing Istio Workloads with Auth0](https://thenewstack.io/securing-istio-workloads-with-auth0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [solo.io: Upgrading Istio without Downtime](https://www.solo.io/blog/upgrading-istio-without-downtime)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [istio.io: Merbridge - Accelerate your mesh with eBPF](https://istio.io/latest/blog/2022/merbridge)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [freecodecamp.org: Learn Istio – How to Manage, Monitor, and Secure Microservices 🌟](https://www.freecodecamp.org/news/learn-istio-manage-microservices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [useanvil.com: Load balancing gRPC in Kubernetes with Istio](https://www.useanvil.com/blog/engineering/load-balancing-grpc-in-kubernetes-with-istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Taffic Shaping - Kubernetes & Istio | Daniele Polencic](https://itnext.io/traffic-shaping-with-kubernetes-and-istio-7e44fbfca200)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Maistra.io](https://maistra.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com: Maistra Istio](https://github.com/maistra/istio)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [istio-ecosystem/admiral](https://github.com/istio-ecosystem/admiral)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [istio.io: Introducing Ambient Mesh](https://istio.io/latest/blog/2022/introducing-ambient-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com: kiali](https://github.com/kiali/kiali)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Find issues in your Istio mesh with Kiali](https://itnext.io/find-issues-in-your-istio-mesh-with-kiali-89d37d5e1fb1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jaegertracing.io](https://www.jaegertracing.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [hackernoon.com: A Guide to Deploying Jaeger on Kubernetes in Production](https://hackernoon.com/a-guide-to-deploying-jaeger-on-kubernetes-in-production-0p2n3tub)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [hackernoon.com: How To Use OpenTelemetry And Jaeger To Implement Distributed Tracing And APM](https://hackernoon.com/how-to-use-opentelemetry-and-jaeger-to-implement-distributed-tracing-and-apm-jcx34fi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Linking Traces with Continuous Profiling using Pyroscope](https://www.infracloud.io/blogs/linking-traces-continuous-profiling-pyroscope)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Envoy](https://www.envoyproxy.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Envoy Gateway](https://github.com/envoyproxy/gateway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kibana](https://www.elastic.co/kibana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.amazon.com/app-mesh](https://aws.amazon.com/app-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [allthingsdistributed.com: Redefining application communications with AWS App Mesh](https://www.allthingsdistributed.com/2019/03/redefining-application-communications-with-aws-app-mesh.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [AKS Labs - Introduction](https://azure-samples.github.io/aks-labs/docs/intro)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Observing gRPC-based Microservices on Amazon EKS running Istio](https://itnext.io/observing-grpc-based-microservices-on-amazon-eks-running-istio-77ba90dd8cc0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Application Gateway for Containers: Istio Integration](https://blog.cloudtrooper.net/2025/11/21/application-gateway-for-containers-istio-integration)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Implementing Istio From Start To Finish](https://www.cloudnativedeepdive.com/implementing-istio-from-start-to-finish)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Istio Performance/Stability Testing](https://github.com/istio/tools/blob/master/perf/README.md)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
