# Caching Solutions 
- [Caching](#caching)
- [Java Caching](#java-caching)
- [Infinispan](#infinispan)
- [Red Hat Data Grid (commercial version of Infinispan)](#red-hat-data-grid-commercial-version-of-infinispan)
- [CDN Content Delivery Network](#cdn-content-delivery-network)
- [HAProxy](#haproxy)
- [Varnish](#varnish)
- [Memcached](#memcached)
- [Redis](#redis)
- [Nginx High-performance caching](#nginx-high-performance-caching)

## Caching
- [Wikipedia: Web cache](https://en.wikipedia.org/wiki/Web_cache)
- [Wikipedia: Dynamic site acceleration](https://en.wikipedia.org/wiki/Dynamic_site_acceleration)
- [Slideshare: Caching](http://www.slideshare.net/NasceniaIT/brown-bag-caching-rafi-faisal-48694442)
- [nixCraft: 9 Awesome Open Source Web Performance Software For Linux and Unix-like Systems](https://www.cyberciti.biz/open-source/http-web-performance-proxy-load-balancer-accelerator-software/)
- [Dzone: An Introduction to Caching: How and Why We Do It 🌟](https://dzone.com/articles/introducing-amp-assimilating-caching-quick-read-fo) When it comes to caching, what was once a nice-to-have it now a must-have. Check out this detailed article to learn everything you need to know about caching!

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

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/hkcICcrntApXsr" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/haproxytech/haproxy-best-practice" title="Haproxy best practice" target="_blank">Haproxy best practice</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/haproxytech">haproxytech</a></strong> </div>
</div>
</center>
<br/>

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

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/fQrbxcE741QjvX" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/kimlindholm/varnish-configuration-step-by-step" title="Varnish Configuration Step by Step" target="_blank">Varnish Configuration Step by Step</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/kimlindholm">Kim Stefan Lindholm</a></strong> </div>
</div>
</center>
<br/>

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/JlHlus2tBHDZVi" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ivanchepurnyi/advanced-varnishusage" title="Varnish Cache and its usage in the real world!" target="_blank">Varnish Cache and its usage in the real world!</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/ivanchepurnyi">Ivan Chepurnyi</a></strong> </div>
</div>
</center>
<br/>

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/crhLrhAgnlZmLv" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/samanthaquinonestembies/superchargin-varnish" title="Supercharging Content Delivery with Varnish" target="_blank">Supercharging Content Delivery with Varnish</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/samanthaquinonestembies">Samantha Quiñones</a></strong> </div>
</div>
</center>
<br/>

## Memcached
- [memcached.org](http://memcached.org)
- [Slideshare: Introduction to memcached](http://www.slideshare.net/oemebamo/introduction-to-memcached)
- [DZone - The Power of the Proxy: Request Routing Memcached](https://dzone.com/articles/the-power-of-the-proxy-request-routing-memcached)

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/rqpOlUNkU6NOvo" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/oemebamo/introduction-to-memcached" title="Introduction to memcached" target="_blank">Introduction to memcached</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/oemebamo">Jurriaan Persyn</a></strong> </div></div>
</center>
<br/>

## Redis
- [redis.io](http://redis.io)
- [Slideshare: Introduction to Redis](http://www.slideshare.net/dvirsky/introduction-to-redis)

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/3nvYR34GEVLEei" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/dvirsky/introduction-to-redis" title="Introduction to Redis" target="_blank">Introduction to Redis</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/dvirsky">Dvir Volk</a></strong> </div>
</div>
</center>
<br/>

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/42WDX39CPeO9e6" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NasceniaIT/brown-bag-caching-rafi-faisal-48694442" title="Caching" target="_blank">Caching</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/NasceniaIT">Nascenia IT</a></strong> </div></div>
</center>
<br/>

<center>
<div class="container">
<iframe src="https://www.youtube.com/embed/bjXNWBaIWjM?rel=0" frameborder="0" allowfullscreen class="video"></iframe>
</div> 
</center>
<br/>

## Nginx High-performance caching
- [Nginxconf 2014. When Dynamic Becomes Static:The Next Step in Web Caching Techniques: Wim Godden](https://www.youtube.com/watch?v=OssIuHbgzJY)
- [dzone: The Benefits of Microcaching with NGINX](https://dzone.com/articles/the-benefits-of-microcaching-with-nginx)
- [dzone: Scaling Web Applications with NGINX – Part II: Caching and Monitoring](https://dzone.com/articles/scaling-web-applications-with-nginx-part-ii-cachin)
- [Nginx: a caching, thumbnailing, reverse proxying image server? 🌟](http://charlesleifer.com/blog/nginx-a-caching-thumbnailing-reverse-proxying-image-server-/)
- [highscalability.com: Building nginx and Tarantool based services 🌟](http://highscalability.com/blog/2016/2/17/building-nginx-and-tarantool-based-services.html)

<center>
<div class="container">
<iframe src="https://www.youtube.com/embed/OssIuHbgzJY?rel=0" frameborder="0" allowfullscreen class="video"></iframe>
</div>
</center>
<br/>

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/wC5wngKnh2iydS" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/Nginx/nginx-highperformance-caching" title="NGINX High-performance Caching" target="_blank">NGINX High-performance Caching</a> </strong> from <strong><a href="//www.slideshare.net/Nginx" target="_blank">NGINX, Inc.</a></strong> </div></div>
</center>
<br/>
