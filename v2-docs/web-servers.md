# Web Servers

!!! info "Architectural Context"
    Detailed reference for Web Servers in the context of Networking & Service Mesh.

## Networking

### Fundamentals

#### Load Balancing

  - [opensource.com: A beginner's guide to load balancing](https://opensource.com/article/21/4/load-balancing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-level introductory guide to load balancing strategies. It explains the differences between Layer 4 (TCP) and Layer 7 (HTTP) routing algorithms, making it a useful primer for developers designing multi-region architectures.
### Ingress

#### Skipper

##### HTTP Routing

  - [opensource.com: Try this Kubernetes HTTP router and reverse proxy](https://opensource.com/article/20/4/http-kubernetes-skipper) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to Skipper, an open-source HTTP router created by Zalando. Explores its use case as a highly customizable Kubernetes ingress controller with extensive routing filters tailored for large-scale production architectures.
#### Traefik

##### Istio Integration

  - [thenewstack.io: Using Traefik Ingress Controller with Istio Service Mesh](https://thenewstack.io/using-traefik-ingress-controller-with-istio-service-mesh) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A valuable integration guide demonstrating how to use Traefik as the external edge ingress router while leveraging Istio's internal service mesh to govern east-west traffic patterns and microservices telemetry.
##### Kubernetes Ingress

  - [opensource.com: Directing Kubernetes traffic with Traefik](https://opensource.com/article/20/3/kubernetes-traefik)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory article explaining how to set up Traefik as an Ingress Controller in Kubernetes. It focuses on setting up path-based routing rules and using labels to automate routing table updates.
##### Kustomize Deployments

  - [blog.tomarrell.com: Kustomize: Traefik v2.2 as a Kubernetes Ingress Controller](https://blog.tomarrell.com/post/traefik_v2_on_kubernetes)  <span class='md-tag md-tag--info'>[LEGACY]</span> — An operations blog outlining Traefik v2.2 deployment using Kustomize overlays. Although the specific Traefik CRD API versions are legacy, the architectural structure of managing ingress with Kustomize remains highly educational.
  - **(2026)** [==Traefik==](http://traefik.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Traefik is a modern cloud-native HTTP reverse proxy and ingress controller designed to automatically discover backend services from platforms like Kubernetes, Docker, and Consul. Its auto-configuration feature and native support for Let's Encrypt certificates simplify cluster operations.
### Load Balancing (1)

#### HAProxy

##### Implementation

  - [tecmint.com: How to Setup High-Availability Load Balancer with ‘HAProxy’' to Control Web Server Traffic](https://www.tecmint.com/install-haproxy-load-balancer-in-linux)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed linux-level guide for implementing HAProxy from scratch. Guides the platform engineer through initial package deployment, configuration mapping, backend health checking, and metric page exposure.
##### Nginx Integration

  - [Tecmint.com: How to Setup HAProxy as Load Balancer for Nginx on CentOS 8](https://www.tecmint.com/setup-nginx-haproxy-load-balancer-in-centos-8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A configuration-focused tutorial detailing how to chain HAProxy as a frontend load balancer in front of an Nginx web tier on CentOS 8. Note: CentOS 8 is end-of-life, meaning parts of this OS guide must be updated, but the routing concepts remain sound.
  - **(2026)** [==haproxy.org==](http://www.haproxy.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official site for HAProxy, the high-performance TCP/HTTP load balancer. Renowned for its extreme efficiency and microsecond-level latency control, HAProxy is an industry standard for routing massive amounts of concurrent web traffic.
### Reverse Proxy

#### Apache HTTPD

##### Jenkins Integration

  - **(2021)** [Apache Reverse Proxy for Jenkins](https://github.com/nubenetes/apache-reverse-proxy-jenkins) <span class='md-tag md-tag--info'>⭐ 1</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical configuration repository demonstrating how to put Apache behind a Jenkins installation. Due to more than 4 years of inactivity and minimal community adoption, this project is deprioritized and kept primarily as a legacy configuration sample.
### Web Servers (1)

#### Apache HTTPD (1)

##### Reverse Proxy (1)

  - [Apache Reverse Proxy Guide](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official configuration guide for setting up Apache as a reverse proxy using `mod_proxy`. Delivers production-grade recommendations for managing connection pools, configuring SSL offloading, and tuning load-balancing headers.
  - [Apache](https://httpd.apache.org)  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The home page for Apache HTTPD, the foundational open-source web server of the internet. While newer microservices architectures typically leverage Nginx or Envoy, Apache remains highly relevant for legacy proxy configurations and traditional web hosting setups.
#### Nginx

##### Configuration Generators

  - [NGINXConfig](https://www.digitalocean.com/community/tools/nginx)  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — DigitalOcean's visual configuration tool for Nginx. It generates highly secure, production-tested server blocks tailored for modern features like HTTP/2, custom security headers, SSL/TLS optimizations via Let's Encrypt, and Gzip compression.
##### Guides

  - [freecodecamp.org: The NGINX Handbook 🌟](https://www.freecodecamp.org/news/the-nginx-handbook) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An extensive manual explaining the underlying mechanics of Nginx. Covers everything from server blocks and upstream definitions to proxy routing rules, security hardening, and cache configuration optimization.
##### Interactive Playgrounds

  - [jvns.ca: New tool: an nginx playground](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory blog post by Julia Evans launching an interactive Nginx configuration playground. It explains the core configuration blocks and how the visual playground simplifies debugging path matches and header rewrites.
  - [nginx-playground.wizardzines.com 🌟](https://nginx-playground.wizardzines.com)  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The web-based visual Nginx sandbox environment created by Wizard Zines. It provides immediate graphical feedback on how routing, header injections, and rewrite directives behave without requiring a local Nginx daemon installation.
#### Nginx Unit

##### Application Server

  - [unit.nginx.org](https://unit.nginx.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Nginx Unit is a dynamic, polyglot application server engineered to run application code across multiple runtimes (Go, Python, Node.js, PHP) simultaneously. It is entirely controlled via a declarative JSON-based REST API, making it well-suited for container-centric microservices.

---
💡 **Explore Related:** [Istio](./istio.md) | [Caching](./caching.md) | [Kubernetes Networking](./kubernetes-networking.md)

