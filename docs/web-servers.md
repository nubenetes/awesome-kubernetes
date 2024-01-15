# Web Servers & Reverse Proxies: Apache, Nginx, HAProxy, Traefik and more

1. [Introduction](#introduction)
2. [Apache](#apache)
    1. [Apache Configuration Samples](#apache-configuration-samples)
3. [Nginx](#nginx)
    1. [Nginx Unit](#nginx-unit)
    2. [Nginx playground](#nginx-playground)
4. [HAProxy (HTTP router and reverse proxy)](#haproxy-http-router-and-reverse-proxy)
5. [Traefik (HTTP router and reverse proxy)](#traefik-http-router-and-reverse-proxy)
6. [Skipper (HTTP router and reverse proxy)](#skipper-http-router-and-reverse-proxy)
7. [Videos](#videos)
8. [Tweets](#tweets)

## Introduction

- [Reverse Proxy: What, When, How](https://dzone.com/articles/reverse-proxy-what-when-how) Look at a tutorial that explains reverse proxies.
- [opensource.com: A beginner's guide to load balancing](https://opensource.com/article/21/4/load-balancing) Load balancing distributes resources to where they're needed most at that moment.

## Apache

- [Apache](https://httpd.apache.org/)
- [Dzone Refcard: Essential Apache HTTP Server](https://dzone.com/refcardz/essential-apache-http-server)
- [nixCraft: How to secure Apache with Let’s Encrypt Certificates on RHEL 8](https://www.cyberciti.biz/faq/how-to-secure-apache-with-lets-encrypt-certificates-on-rhel-8/)
- [Apache Reverse Proxy Guide](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html)

### Apache Configuration Samples

- [Apache Reverse Proxy for Jenkins](https://github.com/redhatspain/apache-reverse-proxy-jenkins) Reverse Proxy configuration with HTTPS for Jenkins, Sonarqube and Nexus. Based on RHEL 7 Apache config.

## Nginx

- [Nginx](https://www.nginx.com/)
- [Dzone: NGINX: Load Balancing Your Application Made Easy](https://dzone.com/articles/nginx-load-balancing-your-application-made-easy-1)
- [Dzone: Nginx Reverse Proxy Ubuntu 18.04](https://dzone.com/articles/nginx-reverse-proxy-ubuntu-1804) In this post, we will show you how to install Nginx Web Server and configure it as a reverse proxy on Ubuntu Server 18.04.
- [Dzone: DevOps 101: Set Up Nginx in Front of Your Spring Boot Application [Video]](https://dzone.com/articles/devops-101-setup-nginx-in-front-of-your-spring-boo)
- [NGINXConfig 🌟🌟](https://www.digitalocean.com/community/tools/nginx) The easiest way to configure a performant, secure, and stable NGINX server.
- [How To Use the Official NGINX Docker Image](https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/)
- [medium: Using Nginx-Ingress as a Static Cache for Assets Inside Kubernetes](https://medium.com/@vdboor/using-nginx-ingress-as-a-static-cache-91bc27be04a1) Optimizing Nginx on Kubernetes Without a Adding a Cloud CDN.
- [==freecodecamp.org: The NGINX Handbook== 🌟](https://www.freecodecamp.org/news/the-nginx-handbook/)
- [==nginx.com: The Complete NGINX Cookbook== 🌟](https://www.nginx.com/resources/library/complete-nginx-cookbook/) **Get sample NGINX configurations for load balancing, cloud deployment, automation, containers and microservices, service mesh, security, and more.**

### Nginx Unit

- [unit.nginx.org](https://unit.nginx.org) open source multi-language application server

### Nginx playground

- [jvns.ca: New tool: an nginx playground](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground/) It would be cool to have an nginx playground website where you can just paste in an nginx config and test it out. And then I realized it might actually be pretty easy to build, so got excited and started coding and I built it.
- [nginx-playground.wizardzines.com 🌟](https://nginx-playground.wizardzines.com/)

## HAProxy (HTTP router and reverse proxy)

- [Wikipedia: HAProxy](https://en.wikipedia.org/wiki/HAProxy)
- [haproxy.org](http://www.haproxy.org/)
- [dzone.com: How to Configure HAProxy as a Proxy and Load Balancer](https://dzone.com/articles/how-to-configure-ha-proxy-as-a-proxy-and-loadbalan)
- [tecmint.com: How to Setup High-Availability Load Balancer with ‘HAProxy’ to Control Web Server Traffic](https://www.tecmint.com/install-haproxy-load-balancer-in-linux/)
- [Tecmint.com: How to Setup HAProxy as Load Balancer for Nginx on CentOS 8](https://www.tecmint.com/setup-nginx-haproxy-load-balancer-in-centos-8/)
- [nixCraft: 9 Awesome Open Source Web Performance Software For Linux and Unix-like Systems](https://www.cyberciti.biz/open-source/http-web-performance-proxy-load-balancer-accelerator-software/)
- [High priority request queue with HAProxy](https://medium.com/swlh/high-priority-request-queue-with-haproxy-9efd639a8992)

## Traefik (HTTP router and reverse proxy)

- [Traefik](http://traefik.io/)
- [Dzone: How to Use the Open Source Tool Traefik to Direct Kubernetes Traffic](https://dzone.com/articles/how-to-use-the-open-source-tool-traefik-to-direct)
- [opensource.com: Directing Kubernetes traffic with Traefik](https://opensource.com/article/20/3/kubernetes-traefik)
- [blog.tomarrell.com - Kustomize: Traefik v2.2 as a Kubernetes Ingress Controller](https://blog.tomarrell.com/post/traefik_v2_on_kubernetes)
- [thenewstack.io: Using Traefik Ingress Controller with Istio Service Mesh](https://thenewstack.io/using-traefik-ingress-controller-with-istio-service-mesh/)
- [medium.com/beyn-technology: Is Nginx dead? Is Traefik v3 20% faster than Traefik v2?](https://medium.com/beyn-technology/is-nginx-dead-is-traefik-v3-20-faster-than-traefik-v2-f28ffb7eed3e)

## Skipper (HTTP router and reverse proxy)

- [opensource.com: Try this Kubernetes HTTP router and reverse proxy](https://opensource.com/article/20/4/http-kubernetes-skipper)

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/KZFkssRuBLE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>Nginx has a service mesh too. Is it any good?<br><br>Let&#39;s find out. <a href="https://t.co/890EIahXGq">pic.twitter.com/890EIahXGq</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1356935454206005249?ref_src=twsrc%5Etfw">February 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
