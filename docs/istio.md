# Istio - Service Mesh

1. [Docs](#docs)
2. [API Access Control](#api-access-control)
3. [Maistra Istio](#maistra-istio)
4. [Admiral](#admiral)
5. [Ambient Mesh - Istio Data Plane](#ambient-mesh---istio-data-plane)
6. [Kiali project, observability for the Istio service mesh](#kiali-project-observability-for-the-istio-service-mesh)
7. [Jaeger tracing. Open source, end-to-end distributed tracing](#jaeger-tracing-open-source-end-to-end-distributed-tracing)
8. [Envoy micro proxy](#envoy-micro-proxy)
    1. [Envoy Gateway](#envoy-gateway)
9. [Kibana](#kibana)
10. [AWS App Mesh](#aws-app-mesh)
11. [Istio and AWS EKS](#istio-and-aws-eks)
12. [Istio Tools](#istio-tools)
13. [Videos](#videos)
14. [Tweets](#tweets)

## Docs

- [Istio.io](https://istio.io/)
- [github.com: Istio](https://github.com/istio/istio)
- [karlstoney.com: Istio 503's with UC's and TCP Fun Times](https://karlstoney.com/2019/05/31/istio-503s-ucs-and-tcp-fun-times/)
- [blog.christianposta.com: Istio as an Example of When Not to Do Microservices](https://blog.christianposta.com/microservices/istio-as-an-example-of-when-not-to-do-microservices/)
- [istiobyexample.dev 🌟](https://istiobyexample.dev/)
    - [istiobyexample.dev: Fault Injection](https://istiobyexample.dev/fault-injection/)
- [blog.openshift.com: Red Hat OpenShift Service Mesh is now available: What you should know 🌟](https://blog.openshift.com/red-hat-openshift-service-mesh-is-now-available-what-you-should-know/)
- [The Istio project just consolidated its control plane services: Pilot, Citadel, Galley, and the sidecar injector, into a single binary, __Istiod__](https://istio.io/blog/2020/tradewinds-2020/#fewer-moving-parts)
- [github.com/askmeegs/learn-istio 🌟](https://github.com/askmeegs/learn-istio)
- [Riding the Tiger: Lessons Learned Implementing Istio 🌟](https://zwischenzugs.com/2020/05/05/riding-the-tiger-lessons-learned-implementing-istio/)
- [dev.to/aurelievache: Understanding Istio: part 1 – Istio Components](https://dev.to/aurelievache/understanding-istio-part-1-istio-components-4ik5)
    - [dev.to/aurelievache: Understanding Istio: part 9 – DestinationRule](https://dev.to/aurelievache/understanding-istio-part-9-destinationrule-1g7e)
    - [dev.to/aurelievache: Understanding Istio: part 16 – Observability / Metrics](https://dev.to/aurelievache/understanding-istio-part-16-observability-metrics-2m8p)
- [openshift.com: Monitoring Services like an SRE in OpenShift ServiceMesh Part 2: Collecting Standard Metrics 🌟](https://www.openshift.com/blog/monitoring-services-like-an-sre-in-openshift-servicemesh-part-2-collecting-standard-metrics-3)
- [istio.io: Learn Microservices using Kubernetes and Istio 🌟](https://istio.io/latest/docs/examples/microservices-istio/) step-by-step tutorial
- [thenewstack.io - Service Mesh: The Gateway to Cloud Migration](https://thenewstack.io/when-you-need-or-dont-need-service-mesh/)
- [thenewstack.io: Kubernetes, Microservices, and Istio  — A Great Fit!](https://thenewstack.io/kubernetes-microservices-istio%E2%80%8A-%E2%80%8Aa-great-fit/)
- [solo.io: Learn how to rate limit requests in Istio 🌟](https://www.solo.io/blog/tutorial-rate-limiting-of-service-requests-in-istio-service-mesh)
- [solo.io: Identity Federation for Multi-Cluster Kubernetes and Service Mesh](https://www.solo.io/blog/identity-federation-for-multi-cluster-kubernetes-and-service-mesh/)
- [sysdig.com: How to monitor Istio, the Kubernetes service mesh](https://sysdig.com/blog/monitor-istio/)
- [tetrate.io: VM to container communications 101](https://www.tetrate.io/blog/vm-to-container-communications-101/) How can I use Istio Service Mesh to make VMs and containers talk to each other?
- [redhat-scholars: istio-tutorial 🌟](https://github.com/redhat-scholars/istio-tutorial) Polyglot microservices (Java, Node, .NET) + Istio on Kubernetes/OpenShift
- [blog.jetstack.io: Istio OIDC Authentication](https://blog.jetstack.io/blog/istio-oidc/) A service mesh is an architectural pattern that provides common network services as a feature of the infrastructure. This typically includes features such as service discovery and policy enforcement to control how services within the mesh can communicate with each other.
- [solo.io: The evolution of VM support in Istio 1.8 (with video)](https://www.solo.io/blog/the-evolution-of-vm-support-in-istio-1-8-with-video/)
- [jetstack.io: Securing Istio workloads with mTLS using cert-manager](https://www.jetstack.io/blog/cert-manager-istio-integration/)
- [thenewstack.io: Why Do You Need Istio When You Already Have Kubernetes? 🌟](https://thenewstack.io/why-do-you-need-istio-when-you-already-have-kubernetes)
- [thenewstack.io: Solo.io: Istio Is Winning the Service Mesh War](https://thenewstack.io/solo-io-istio-is-winning-the-service-mesh-war/)
- [tetrate.io: Why do you need Istio when you already have Kubernetes?](https://www.tetrate.io/blog/why-do-you-need-istio-when-you-already-have-kubernetes/)
- [learncloudnative.com: Attach multiple VirtualServices to Istio Gateway](https://learncloudnative.com/blog/2020-11-23-multiple-vs-gateway)
- [thenewstack.io: What Is Istio and Why Does Kubernetes Need it? 🌟](https://thenewstack.io/what-is-istio-and-why-does-kubernetes-need-it/)
- [youtube: Istio & Service Mesh - simply explained in 15 mins 🌟](https://www.youtube.com/watch?v=16fgzklcF7Y&ab_channel=TechWorldwithNana)
- [dev.to: A GitOps recipe for Progressive Delivery with Istio 🌟](https://dev.to/stefanprodan/a-gitops-recipe-for-progressive-delivery-2pa3) GitOps and Progressive Delivery featuring
IstioMesh, PrometheusIO, Flux v2 & Flagger.
- [samos-it.com: Securing Redis with Istio TLS origination](https://samos-it.com/posts/securing-redis-istio-tls-origniation-termination.html) Istio is daunting and not all use cases are well documented. The public docs focus mostly on using the egress gateway for TLS orignation. The use case of using the sidecar for TLS origination with a database isn't documented well. This blog post hopes to solve that.
- [solo.io: Istio multi-cluster on Red Hat OpenShift with Gloo Mesh](https://www.solo.io/blog/istio-multi-cluster-on-red-hat-openshift-with-gloo-mesh/)
- [solo.io: Ode to Istio 🌟](https://www.solo.io/blog/ode-to-istio/)
- [thenewstack.io: Istio 1.10 Improves Scalability and Revision Control](https://thenewstack.io/istio-1-10-improves-scalability-and-revision-control/)
- [istio.io: Configuring failover for external services](https://istio.io/latest/blog/2021/external-locality-failover/) Learn how to configure locality load balancing and failover for endpoints that are outside of your mesh.
- [thenewstack.io: Multicluster Management with Kubernetes and Istio](https://thenewstack.io/multicluster-management-with-kubernetes-and-istio/)
- [piotrminkowski.com: Multicluster Traffic Mirroring with Istio and Kind](https://piotrminkowski.com/2021/07/12/multicluster-traffic-mirroring-with-istio-and-kind)
- [thenewstack.io: Securing Istio Workloads with Auth0](https://thenewstack.io/securing-istio-workloads-with-auth0/)
- [tetrate.io: Multicluster Management with Kubernetes and Istio 🌟](https://www.tetrate.io/blog/multicluster-management-with-kubernetes-and-istio/)
- [solo.io: Upgrading Istio without Downtime](https://www.solo.io/blog/upgrading-istio-without-downtime/)
- [tetrate.io: Using Istio Service Mesh as API Gateway 🌟](https://www.tetrate.io/blog/istio-servicemesh-api-gateway/)
- [mirantis.com: Your App Deserves More than Kubernetes Ingress: Kubernetes Ingress vs. Istio Gateway [webinar]](https://www.mirantis.com/blog/your-app-deserves-more-than-kubernetes-ingress-kubernetes-ingress-vs-istio-gateway-webinar)
- [solo.io: Configuration as Data, GitOps, and Controllers: it’s not simple for multi-cluster](https://www.solo.io/blog/configuration-as-data-gitops-and-controllers-its-not-simple-for-multi-cluster/)
- [solo.io: Istio’s networking: An in-depth look at traffic and architecture 🌟](https://www.solo.io/blog/istios-networking-in-depth) Istio’s networking in a demo environment
- [solo.io: Navigating __Istio Config__: a look into Istio’s toolkit](https://www.solo.io/blog/navigating-istio-config-toolkit/)
- [istio.io: Merbridge - Accelerate your mesh with eBPF](https://istio.io/latest/blog/2022/merbridge/) Replacing iptables rules with eBPF allows transporting data directly from inbound sockets to outbound sockets, shortening the datapath between sidecars and services.
- [==freecodecamp.org: Learn Istio – How to Manage, Monitor, and Secure Microservices== 🌟](https://www.freecodecamp.org/news/learn-istio-manage-microservices)
- [useanvil.com: Load balancing gRPC in Kubernetes with Istio](https://www.useanvil.com/blog/engineering/load-balancing-grpc-in-kubernetes-with-istio/)
- [jimmysong.io: Understanding the Sidecar Injection, Traffic Intercepting & Routing Process in Istio](https://jimmysong.io/en/blog/sidecar-injection-iptables-and-traffic-routing/) This article will cover Istio and:
    - What is the sidecar pattern and what advantages does it have?
    - How are the sidecar injections done in Istio?
    - How does the sidecar proxy do transparent traffic hijacking?
    - How is the traffic routed upstream?
- [blog.getambassador.io: Kubernetes Canary Testing and Release with Istio](https://blog.getambassador.io/kubernetes-canary-testing-and-release-with-istio-4cbdedcc9914?gi=816ffb457b0d) In this article, you'll learn about Canary testing in Kubernetes and how Istio can help perform seamless Canary upgrades
    - What is a JWT, and why should you care?
    - Dissecting Istio's JWT edge authentication & authorization
    - How to build an external authz service for Istio
    - What is Zero Trust Architecture
    - Istio Architecture
    - How to enable mTLS
    - How to enable access control and authorization between your microservices

## API Access Control


## Maistra Istio

- [Maistra.io](https://maistra.io)
- [github.com: Maistra Istio](https://github.com/maistra/istio)

## Admiral

- [istio-ecosystem/admiral](https://github.com/istio-ecosystem/admiral) Admiral provides automatic configuration and service discovery for multicluster Istio service mesh. Istio has a very robust set of multi-cluster capabilities. Managing this configuration across multiple clusters at scale is challenging. Admiral takes an opinionated view on this configuration and provides automatic provisioning and syncing across clusters. This removes the complexity for developers and mesh operators.

## Ambient Mesh - Istio Data Plane

- [istio.io: Introducing Ambient Mesh](https://istio.io/latest/blog/2022/introducing-ambient-mesh/) A new dataplane mode for Istio without sidecars.

## Kiali project, observability for the Istio service mesh

- [kiali.io](https://www.kiali.io/)
- [github.com: kiali](https://github.com/kiali/kiali)

## Jaeger tracing. Open source, end-to-end distributed tracing

- Monitor and troubleshoot transactions in complex distributed systems
- [jaegertracing.io](https://www.jaegertracing.io/)
- [hackernoon.com: A Guide to Deploying Jaeger on Kubernetes in Production](https://hackernoon.com/a-guide-to-deploying-jaeger-on-kubernetes-in-production-0p2n3tub)
- [hackernoon.com: How To Use OpenTelemetry And Jaeger To Implement Distributed Tracing And APM](https://hackernoon.com/how-to-use-opentelemetry-and-jaeger-to-implement-distributed-tracing-and-apm-jcx34fi)
- [infracloud.io: Linking Traces with Continuous Profiling using Pyroscope](https://www.infracloud.io/blogs/linking-traces-continuous-profiling-pyroscope/) The future of observability lies in distributed tracing with continuous profiling. In this article, you will learn how you can link traces with continuous profiling using Pyroscope and Jaeger.

## Envoy micro proxy

- [envoyproxy.io](https://www.envoyproxy.io/)
- [getenvoy.io](https://www.getenvoy.io/)
- [Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes)

### Envoy Gateway

- [Envoy Gateway](https://github.com/envoyproxy/gateway) Envoy Gateway is an open source project for managing Envoy Proxy as a standalone or Kubernetes-based application gateway.

## Kibana

- [kibana](https://www.elastic.co/products/kibana)
- [The Best Tools for Exporting Elasticsearch Data from Kibana](https://www.skedler.com/blog/the-best-tools-for-exporting-elasticsearch-data-from-kibana/)

## AWS App Mesh

- [aws.amazon.com/app-mesh](https://aws.amazon.com/app-mesh/)
- [allthingsdistributed.com: Redefining application communications with AWS App Mesh](https://www.allthingsdistributed.com/2019/03/redefining-application-communications-with-aws-app-mesh.html)

## Istio and AWS EKS


## Istio Tools

- [Istio Performance/Stability Testing](https://github.com/istio/tools/blob/master/perf/README.md)

## Videos

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/voAyroDb6xk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/E0h1rS2D86k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">💎 Hidden gem feature<br><br>Did you know that Kiali can automatically generate all the Authorization Policies of a namespace?<br><br>Via telemetry, Kiali can define one Authz Policy per each service in the mesh.<a href="https://twitter.com/IstioMesh?ref_src=twsrc%5Etfw">@IstioMesh</a> <a href="https://twitter.com/hashtag/servicemesh?src=hash&amp;ref_src=twsrc%5Etfw">#servicemesh</a> <a href="https://twitter.com/hashtag/authorization?src=hash&amp;ref_src=twsrc%5Etfw">#authorization</a> <a href="https://twitter.com/hashtag/security?src=hash&amp;ref_src=twsrc%5Etfw">#security</a> <a href="https://twitter.com/hashtag/k8s?src=hash&amp;ref_src=twsrc%5Etfw">#k8s</a> <a href="https://t.co/YlEKRq6nq0">pic.twitter.com/YlEKRq6nq0</a></p>&mdash; Kiali (@KialiProject) <a href="https://twitter.com/KialiProject/status/1393940551637127168?ref_src=twsrc%5Etfw">May 16, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How can you roll out an app only to a subset of your users in Kubernetes?<br><br>Let&#39;s explore Canary Releases with Istio, Kiali and the Gateway API! <a href="https://t.co/Ao4LkBRRu3">pic.twitter.com/Ao4LkBRRu3</a></p>&mdash; Daniele Polencic — @danielepolencic@hachyderm.io (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1658087679333109762?ref_src=twsrc%5Etfw">May 15, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>