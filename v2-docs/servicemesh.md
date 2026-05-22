# Servicemesh

!!! info "Architectural Context"
    Detailed reference for Servicemesh in the context of Networking & Service Mesh.

## Cloud Infrastructure

### Kubernetes

#### Service Mesh

  - **(2021)** [**Service meshes to the rescue: Load balancing and scaling long-lived connections in Kubernetes 🌟**](https://learnkube.com/kubernetes-long-lived-connections) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A deep dive into the engineering challenge of load balancing long-lived connections (gRPC, HTTP/2, WebSockets) within Kubernetes. It explains how standard L4 kube-proxy load balancing fails to distribute traffic evenly and presents L7 proxies and service meshes (like Linkerd or Istio) as the definitive architectural solution.
## Cloud Native Infrastructure

### Data Plane

#### Envoy Proxy

##### Official Docs

  - **(2026)** [==Envoy==](https://www.envoyproxy.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The home portal of Envoy, the industry-standard L7 proxy designed specifically for cloud-native services. Acts as the data plane engine for most modern service meshes (including Istio), delivering outstanding network performance, advanced routing, and rich observability.
### Service Mesh (1)

#### Istio

##### Operations

  - **(2021)** [solo.io: Navigating __Istio Config__: a look into Istio’s toolkit](https://www.solo.io/blog) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A guide detailing useful debugging utilities and CLI tools for validating and diagnosing Istio configuration sets. Explains how to leverage 'istioctl' diagnostics, debug configuration states, and inspect direct Envoy configuration mappings to maintain healthy cluster states.
## Networking

### Service Mesh (2)

#### Istio (1)

##### Implementation

  - **(2023)** [Implementing Istio From Start To Finish](https://www.cloudnativedeepdive.com/implementing-istio-from-start-to-finish) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An implementation guide mapping out the lifecycle steps required to deploy, secure, and operate an Istio service mesh in enterprise environments. It provides structured insights on handling namespace injection, ambient mesh considerations, and mutual TLS enforcement.
## Observability

### Telemetry Standards

#### OpenTelemetry vs Prometheus

  - **(2022)** [Prometheus and OpenTelemetry Compatibility Issues](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An informative look at the historical data model incompatibilities between Prometheus and OpenTelemetry (OTel). It details the industry efforts to reconcile standard Prometheus structures with the broader OTel landscape.

---
💡 **Explore Related:** [Caching](./caching.md) | [Kubernetes Networking](./kubernetes-networking.md) | [Networking](./networking.md)

