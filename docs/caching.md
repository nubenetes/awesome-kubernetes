# Caching Solutions

1. [Introduction to Caching](#introduction-to-caching)
2. [Java Caching](#java-caching)
3. [Infinispan](#infinispan)
4. [Red Hat Data Grid (commercial version of Infinispan)](#red-hat-data-grid-commercial-version-of-infinispan)
5. [CDN Content Delivery Network](#cdn-content-delivery-network)
6. [HAProxy](#haproxy)
7. [Varnish](#varnish)
8. [Memcached](#memcached)
9. [Redis](#redis)
10. [Nginx High-performance caching](#nginx-high-performance-caching)
11. [Tau Git-Native CDN PaaS](#tau-git-native-cdn-paas)
12. [Videos](#videos)
13. [Slides](#slides)

## Introduction to Caching

- [Wikipedia: Web cache](https://en.wikipedia.org/wiki/Web_cache)
- [Wikipedia: Dynamic site acceleration](https://en.wikipedia.org/wiki/Dynamic_site_acceleration)
- [Slideshare: Caching](http://www.slideshare.net/NasceniaIT/brown-bag-caching-rafi-faisal-48694442)
- [nixCraft: 9 Awesome Open Source Web Performance Software For Linux and Unix-like Systems](https://www.cyberciti.biz/open-source/http-web-performance-proxy-load-balancer-accelerator-software/)
- [Dzone: An Introduction to Caching: How and Why We Do It 🌟](https://dzone.com/articles/introducing-amp-assimilating-caching-quick-read-fo) When it comes to caching, what was once a nice-to-have it now a must-have. Check out this detailed article to learn everything you need to know about caching!
- [medium: Caching — System Design Concept 🌟](https://medium.com/enjoy-algorithm/caching-system-design-concept-500134cff300)
- [elastisys.com: Evaluation of Caching Methodologies for Microservice-Based Architectures in Kubernetes](https://elastisys.com/evaluation-of-caching-methodologies/)
- [medium: Microservices Distributed Caching](https://medium.com/design-microservices-architecture-with-patterns/microservices-distributed-caching-76828817e41b) In this article, we are going to talk about Microservices Distributed Caching for Microservices Architectures. As you know that we learned practices and patterns and add them into our design toolbox. And we will use these pattern and practices when designing e-commerce microservice architecture.
- [kothiyal-anuj.medium.com: Serverless Diary: The Ultimate Guide to Caching in the Cloud | Anuj Kothiyal](https://kothiyal-anuj.medium.com/serverless-diary-the-ultimate-guide-to-caching-in-the-cloud-249f6a06915f)
- [medium.com/rtkal: Distributed Cache Design](https://medium.com/rtkal/distributed-cache-design-348cbe334df1)
- [learncsdesign.medium.com: An Overview of Distributed Caching 🌟](https://learncsdesign.medium.com/an-overview-of-distributed-caching-e426781d1ff0)
- [surfingcomplexity.blog: Cache invalidation really is one of the hardest problems in computer science](https://surfingcomplexity.blog/2022/11/25/cache-invalidation-really-is-one-of-the-hardest-things-in-computer-science/)

## Java Caching

- [DZone refcard: Java Caching](https://dzone.com/refcardz/java-caching) Strategies and the JCache API. Explores the building blocks of JCache and other caching APIs, as well as multiple strategies for implementing temporary data storage in your application.

## Infinispan

- [Introduction to Infinispan](https://infinispan.org/about/) Distributed in-memory key/value data grid and cache
- [Dzone: Getting Started with Infinispan](https://dzone.com/refcardz/getting-started-infinispan) Enhance Performance With Scalable, Highly Available Data Stores. Infinispan is an open-source, ASL 2.0-licensed, in-memory data grid platform based on Java 8. This newly updated Refcard offers tips for implementing Infinispan, gives a practical example for using it in embedded mode, and lists key APIs and cache features. Learn more about running Infinispan in containers and how to integrate the platform with Hibernate ORM, Apache Hadoop, Apache Spark, and Apache Camel.

## Red Hat Data Grid (commercial version of Infinispan)

- In 2011, Red Hat began producing a commercial version of Infinispan, dubbed JBoss Enterprise Data Grid.
- [Red Hat Data Grid Overview](https://developers.redhat.com/products/datagrid/overview)
- [Red Hat Data Grid](https://www.redhat.com/en/technologies/jboss-middleware/data-grid)
- [Red Hat JBoss Data Grid is Not Just for Caching Java Objects Anymore 🌟](https://thenewstack.io/red-hat-jboss-data-grid-not-just-storing-java-objects-anymore/)
- [developers.redhat.com: Red Hat Data Grid 8.0 brings new server architecture, improved REST API, and more](https://developers.redhat.com/blog/2020/04/13/red-hat-data-grid-8-0-brings-new-server-architecture-improved-rest-api-and-more/)

## CDN Content Delivery Network

- [Wikipedia: CDN Content Delivery Network](https://en.wikipedia.org/wiki/Content_delivery_network)
    - [Traditional commercial CDNs 🌟](https://en.wikipedia.org/wiki/Content_delivery_network#Traditional_commercial_CDNs)
- [How content delivery networks (CDNs) work](https://humanwhocodes.com/blog/2011/11/29/how-content-delivery-networks-cdns-work/)
- [imperva.com: CDN Caching](https://www.imperva.com/learn/performance/cdn-caching/)
- [nczonline: How content delivery networks (CDNs) work - Nov 2011](https://www.nczonline.net/blog/2011/11/29/how-content-delivery-networks-cdns-work/)

## HAProxy

- [HAProxy](http://www.haproxy.org)
- [slideshare: Haproxy web performance](http://www.slideshare.net/haproxytech/haproxy-web-performance-55536394)
- [slideshare: Load Balancing MySQL with HAProxy](http://www.slideshare.net/Severalnines/load-balancing-mysql-with-haproxy-webinar-replay-english-44071270)
- [slideshare: Haproxy best practice](http://www.slideshare.net/haproxytech/haproxy-best-practice)
- [slideshare: How To Set Up SQL Load Balancing with HAProxy](http://www.slideshare.net/Severalnines/severalnines-ha-proxyjul20143)
- [slideshare: Performance Tuning of HAProxy for Database Load Balancing](http://www.slideshare.net/Severalnines/haproxy-mysql-slides)
- [haproxy.com: The HAProxy Enterprise WAF 🌟](https://www.haproxy.com/blog/the-haproxy-enterprise-waf/)

## Varnish

- [Varnish Cache](https://www.varnish-cache.org/)
- [varnish-software.com](https://www.varnish-software.com) Varnish Software is the company behind Varnish Cache, the open source HTTP accelerator.
    - [The Varnish Book](http://info.varnish-software.com/the-varnish-book) Download the Varnish Book to learn how you can optimize your Varnish instance.
- [fedoramagazine.org: Varnish: Your site faster and more stable](https://fedoramagazine.org/varnish-site-faster-stable/)
- [Red Hat Developer Blog. Tag: Varnish](https://developerblog.redhat.com/tag/varnish/)
- [Red Hat Enterprise Linux Blog. Tag: Varnish](http://rhelblog.redhat.com/tag/varnish/)
- [varnish-cache.org: Installation on RedHat](https://www.varnish-cache.org/installation/redhat)
- [Hitch - scalable TLS proxy. Hitch is a libev-based high performance SSL/TLS proxy by Varnish Software](https://hitch-tls.org/)
- [slideshare: Varnish - Tips & Tricks - 4Developers 2015](http://www.slideshare.net/piotrpasich/varnish-47199139)
- [digitalocean.com: How To Speed Up Static Web Pages with Varnish Cache Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-speed-up-static-web-pages-with-varnish-cache-server-on-ubuntu-20-04)
- [github.com/IBM/varnish-operator](https://github.com/IBM/varnish-operator) Run and manage Varnish clusters on Kubernetes. Varnish operator manages Varnish clusters using a CustomResourceDefinition that defines a new Kind called VarnishCluster. The operator manages the whole lifecycle of the cluster: creating, deleting and keeping the cluster configuration up to date
- [github.com/mittwald/kube-httpcache](https://github.com/mittwald/kube-httpcache) Varnish Reverse Proxy on Kubernetes

## Memcached

- [memcached.org](http://memcached.org)
- [Slideshare: Introduction to memcached](http://www.slideshare.net/oemebamo/introduction-to-memcached)
- [DZone - The Power of the Proxy: Request Routing Memcached](https://dzone.com/articles/the-power-of-the-proxy-request-routing-memcached)

## Redis

- [redis.io](http://redis.io)
- [Slideshare: Introduction to Redis](http://www.slideshare.net/dvirsky/introduction-to-redis)
- [medium: Scaling Millions of Geospatial Queries per minute using Redis](https://medium.com/groupon-eng/scaling-millions-of-geospatial-queries-per-minute-using-redis-7c05bcf6b4db)
- [==architecturenotes.co: Redis Explained== 🌟🌟](https://architecturenotes.co/redis/) A deep technical dive into all things Redis. Covering various Redis topologies, data persistence and process forking.
- [faun.pub: Redis High availability with Sentinel on Kubernetes(K8s)](https://faun.pub/redis-high-availability-with-sentinel-on-kubernetes-k8s-a1d67842e0ce) In this tutorial, you will learn how to deploy Redis with Sentinel in Kubernetes. You will also test the availability of the setup by simulating a master failure.
- [medium.com/lightricks-tech-blog: Step by Step Guide: How to create a Dynamic Service Endpoint via K8S API](https://medium.com/lightricks-tech-blog/step-by-step-guide-how-to-create-a-dynamic-service-endpoint-via-k8s-api-1024309cb226) This article explains how to deploy Redis HA in Kubernetes and create a Service that always points to the master Redis. It also demonstrates how to interact with Kubernetes API from inside a pod using a script to update the endpoint dynamically.

## Nginx High-performance caching

- [Nginxconf 2014. When Dynamic Becomes Static:The Next Step in Web Caching Techniques: Wim Godden](https://www.youtube.com/watch?v=OssIuHbgzJY)
- [dzone: The Benefits of Microcaching with NGINX](https://dzone.com/articles/the-benefits-of-microcaching-with-nginx)
- [dzone: Scaling Web Applications with NGINX – Part II: Caching and Monitoring](https://dzone.com/articles/scaling-web-applications-with-nginx-part-ii-cachin)
- [Nginx: a caching, thumbnailing, reverse proxying image server? 🌟](http://charlesleifer.com/blog/nginx-a-caching-thumbnailing-reverse-proxying-image-server-/)
- [highscalability.com: Building nginx and Tarantool based services 🌟](http://highscalability.com/blog/2016/2/17/building-nginx-and-tarantool-based-services.html)

## Tau Git-Native CDN PaaS

- [github.com/taubyte/tau: Tau](https://github.com/taubyte/tau) **Open Source Git-Native CDN PaaS.** An alternative to: Vercel, Netlify, Cloudflare, Amazon Lambda with CloudFront, S3, ElastiCache & SQS, Etc...

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/OssIuHbgzJY?rel=0" frameborder="0" allowfullscreen class="video"></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/bjXNWBaIWjM?rel=0" frameborder="0" allowfullscreen class="video"></iframe>
</center>
</details>

## Slides

<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/wC5wngKnh2iydS" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/Nginx/nginx-highperformance-caching" title="NGINX High-performance Caching" target="_blank">NGINX High-performance Caching</a> </strong> from <strong><a href="//www.slideshare.net/Nginx" target="_blank">NGINX, Inc.</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/3nvYR34GEVLEei" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/dvirsky/introduction-to-redis" title="Introduction to Redis" target="_blank">Introduction to Redis</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/dvirsky">Dvir Volk</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/42WDX39CPeO9e6" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NasceniaIT/brown-bag-caching-rafi-faisal-48694442" title="Caching" target="_blank">Caching</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/NasceniaIT">Nascenia IT</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/rqpOlUNkU6NOvo" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/oemebamo/introduction-to-memcached" title="Introduction to memcached" target="_blank">Introduction to memcached</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/oemebamo">Jurriaan Persyn</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/fQrbxcE741QjvX" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/kimlindholm/varnish-configuration-step-by-step" title="Varnish Configuration Step by Step" target="_blank">Varnish Configuration Step by Step</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/kimlindholm">Kim Stefan Lindholm</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/JlHlus2tBHDZVi" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ivanchepurnyi/advanced-varnishusage" title="Varnish Cache and its usage in the real world!" target="_blank">Varnish Cache and its usage in the real world!</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/ivanchepurnyi">Ivan Chepurnyi</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/crhLrhAgnlZmLv" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/samanthaquinonestembies/superchargin-varnish" title="Supercharging Content Delivery with Varnish" target="_blank">Supercharging Content Delivery with Varnish</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/samanthaquinonestembies">Samantha Quiñones</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/hkcICcrntApXsr" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/haproxytech/haproxy-best-practice" title="Haproxy best practice" target="_blank">Haproxy best practice</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/haproxytech">haproxytech</a></strong> </div>
</center>
</details>
