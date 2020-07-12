# Service Mesh
* [infoq.com: Service Mesh Ultimate Guide:](https://www.infoq.com/articles/service-mesh-ultimate-guide/)  Managing Service-to-Service Communications in the Era of Microservices
* [deloitte.com: Service Mesh en arquitecturas de microservicios](https://www2.deloitte.com/es/es/pages/technology/articles/service-mesh-en-arquitecturas-de-microservicios.html)
* [Service meshes to the rescue: Load balancing and scaling long-lived connections in Kubernetes](https://learnk8s.io/kubernetes-long-lived-connections)
* [blog.christianposta.com: Do I Need an API Gateway if I Use a Service Mesh?](https://blog.christianposta.com/microservices/do-i-need-an-api-gateway-if-i-have-a-service-mesh/)
* [thenewstack.io: Service Mesh Adds Security, Observability and Traffic Control to Kubernetes](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes/)

## Tools For Evaluating Service Meshes
* [Meshery.io:](https://meshery.io/) Open source tool for evaluating and contrasting service meshes

## Consul Service Mesh
- [consul.io](https://www.consul.io/)
- [medium: Consul in Kubernetes — Pushing to Production](https://medium.com/swlh/consul-in-kubernetes-pushing-to-production-223506bbe8db)
- [medium: HashiCorp Consul: Multi-Cloud and Multi-Platform Service Mesh](https://medium.com/hashicorp-engineering/hashicorp-consul-multi-cloud-and-multi-platform-service-mesh-372a82264e8e)
- [hashicorp.com: Get Started with Consul Service Mesh on Kubernetes 🌟](https://www.hashicorp.com/blog/get-started-with-consul-service-mesh-on-kubernetes/)

### Consul Connect
- [consul Connect](https://www.consul.io/docs/connect/index.html)

## Linkerd Service Mesh
- [Linkerd](https://linkerd.io/)
- [Announcing Linkerd 2.8: simple, secure multi-cluster Kubernetes](https://linkerd.io/2020/06/09/announcing-linkerd-2.8/)

```
[Installed @Linkerd in staging yesterday using Helm and Terraform](https://twitter.com/DanielJamesPost). It was incredibly easy to setup and immediately helped me diagnose tricky latency issues between services. I have no idea why I didn’t do this sooner. Can’t wait to get this into production.
 ```

## Maesh Service Mesh
- [Maesh](https://containo.us/maesh/)

## Traffic Director (Google's Service Mesh)
- [Traffic Director overview](https://cloud.google.com/traffic-director)
- [Google Cloud’s Traffic Director — What is it and how is it related to the Istio service-mesh?](https://medium.com/cloudzone/google-clouds-traffic-director-what-is-it-and-how-is-it-related-to-the-istio-service-mesh-c199acc64a6d)
- [**Google Traffic Director** and the **L7 Internal Load Balancer** Intermingles **Cloud Native** and **Legacy Workloads**](https://thenewstack.io/google-traffic-director-and-the-l7-internal-load-balancer-intermingles-cloud-native-and-legacy-workloads/) 
- [infoq.com: Introducing Traffic Director: Google's Service Mesh Control Plane](https://www.infoq.com/news/2019/04/google-traffic-director/)

### Google L7 Internal Load Balancer
- [L7 Internal HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/l7-internal/)

## Envoy Proxy Service Mesh 
- [Envoy](https://www.envoyproxy.io/)
- [Examining Load Balancing Algorithms with Envoy](https://blog.envoyproxy.io/examining-load-balancing-algorithms-with-envoy-1be643ea121c)
- [solo.io: Why the control plane matters. Control planes are different than data planes. Separating the control plane from data plane 🌟](https://www.solo.io/blog/why-the-control-plane-matters/)

### xDS protocol (Envoy's Discovery Service Protocol)
- [xDS REST and gRPC protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)
- "The [gRPC project](https://grpc.io/faq/) is adding support for the **xDS protocol**, think Envoy Proxy as a library, which will provide a subset of functionality without an external proxy. 🤯 The best part, xDS based control planes such as Istio, Traffic Director, and Consul Connect should just work." Kelsey Hightower

## Istio - Service Mesh
- [Istio](istio.md)

## Kourier
- [Kourier: A lightweight Knative Serving ingress](https://developers.redhat.com/blog/2020/06/30/kourier-a-lightweight-knative-serving-ingress/)
- https://github.com/knative/net-kourier : Kourier is an Ingress for Knative Serving. Kourier is a lightweight alternative for the Istio ingress as its deployment consists only of an Envoy proxy and a control plane for it.