# Web Servers

!!! info "Architectural Context"
    Detailed reference for Web Servers in the context of Networking & Service Mesh.

## Networking

### Fundamentals

#### Load Balancing

  - **(2021)** [opensource.com: A beginner's guide to load balancing](https://opensource.com/article/21/4/load-balancing) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-level introductory guide to load balancing strategies. It explains the differences between Layer 4 (TCP) and Layer 7 (HTTP) routing algorithms, making it a useful primer for developers designing multi-region architectures.
### Ingress

#### Skipper

##### HTTP Routing

  - **(2020)** [opensource.com: Try this Kubernetes HTTP router and reverse proxy](https://opensource.com/article/20/4/http-kubernetes-skipper) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to Skipper, an open-source HTTP router created by Zalando. Explores its use case as a highly customizable Kubernetes ingress controller with extensive routing filters tailored for large-scale production architectures.
#### Traefik

##### Istio Integration

  - **(2021)** [**thenewstack.io: Using Traefik Ingress Controller with Istio Service Mesh**](https://thenewstack.io/using-traefik-ingress-controller-with-istio-service-mesh) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A valuable integration guide demonstrating how to use Traefik as the external edge ingress router while leveraging Istio's internal service mesh to govern east-west traffic patterns and microservices telemetry.
##### Kubernetes Ingress

  - **(2020)** [opensource.com: Directing Kubernetes traffic with Traefik](https://opensource.com/article/20/3/kubernetes-traefik) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory article explaining how to set up Traefik as an Ingress Controller in Kubernetes. It focuses on setting up path-based routing rules and using labels to automate routing table updates.
  - **(2026)** [==Traefik==](http://traefik.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Traefik is a modern cloud-native HTTP reverse proxy and ingress controller designed to automatically discover backend services from platforms like Kubernetes, Docker, and Consul. Its auto-configuration feature and native support for Let's Encrypt certificates simplify cluster operations.
### Load Balancing (1)

#### HAProxy

##### Implementation

  - **(2021)** [tecmint.com: How to Setup High-Availability Load Balancer with ‘HAProxy’ to Control Web Server Traffic](https://www.tecmint.com/install-haproxy-load-balancer-in-linux) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed linux-level guide for implementing HAProxy from scratch. Guides the platform engineer through initial package deployment, configuration mapping, backend health checking, and metric page exposure.
##### Nginx Integration

  - **(2020)** [Tecmint.com: How to Setup HAProxy as Load Balancer for Nginx on CentOS 8](https://www.tecmint.com/setup-nginx-haproxy-load-balancer-in-centos-8) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A configuration-focused tutorial detailing how to chain HAProxy as a frontend load balancer in front of an Nginx web tier on CentOS 8. Note: CentOS 8 is end-of-life, meaning parts of this OS guide must be updated, but the routing concepts remain sound.
### Reverse Proxy

#### Apache HTTPD

##### Jenkins Integration

  - **(2021)** [Apache Reverse Proxy for Jenkins](https://github.com/nubenetes/apache-reverse-proxy-jenkins) <span class='md-tag md-tag--info'>⭐ 1</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical configuration repository demonstrating how to put Apache behind a Jenkins installation. Due to more than 4 years of inactivity and minimal community adoption, this project is deprioritized and kept primarily as a legacy configuration sample.
### Web Servers (1)

#### Apache HTTPD (1)

##### Reverse Proxy (1)

  - **(2025)** [**Apache Reverse Proxy Guide**](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official configuration guide for setting up Apache as a reverse proxy using `mod_proxy`. Delivers production-grade recommendations for managing connection pools, configuring SSL offloading, and tuning load-balancing headers.
  - **(2026)** [==Apache==](https://httpd.apache.org) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The home page for Apache HTTPD, the foundational open-source web server of the internet. While newer microservices architectures typically leverage Nginx or Envoy, Apache remains highly relevant for legacy proxy configurations and traditional web hosting setups.
#### Nginx

##### Guides

  - **(2021)** [**freecodecamp.org: The NGINX Handbook 🌟**](https://www.freecodecamp.org/news/the-nginx-handbook) <span class='md-tag md-tag--primary'>[GUIDE]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An extensive manual explaining the underlying mechanics of Nginx. Covers everything from server blocks and upstream definitions to proxy routing rules, security hardening, and cache configuration optimization.
##### Interactive Playgrounds

  - **(2025)** [**nginx-playground.wizardzines.com 🌟**](https://nginx-playground.wizardzines.com) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The web-based visual Nginx sandbox environment created by Wizard Zines. It provides immediate graphical feedback on how routing, header injections, and rewrite directives behave without requiring a local Nginx daemon installation.
  - **(2021)** [jvns.ca: New tool: an nginx playground](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory blog post by Julia Evans launching an interactive Nginx configuration playground. It explains the core configuration blocks and how the visual playground simplifies debugging path matches and header rewrites.
#### Nginx Unit

##### Application Server

  - **(2026)** [**unit.nginx.org**](https://unit.nginx.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Nginx Unit is a dynamic, polyglot application server engineered to run application code across multiple runtimes (Go, Python, Node.js, PHP) simultaneously. It is entirely controlled via a declarative JSON-based REST API, making it well-suited for container-centric microservices.

---
💡 **Explore Related:** [Caching](./caching.md) | [Servicemesh](./servicemesh.md) | [Kubernetes Networking](./kubernetes-networking.md)

