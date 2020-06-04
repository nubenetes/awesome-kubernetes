# Java and Memory Management
- [Java](#java)
    - [Existing Java Implementations](#existing-java-implementations)
    - [Use Java 11](#use-java-11)
    - [Java Programming Models (Java Frameworks)](#java-programming-models-java-frameworks)
        - [Spring and MicroProfile frameworks for microservices development (open source microservices frameworks)](#spring-and-microprofile-frameworks-for-microservices-development-open-source-microservices-frameworks)
            - [Spring](#spring)
            - [Eclipse MicroProfile Project](#eclipse-microprofile-project)
            - [Spring Boot VS MicroProfile](#spring-boot-vs-microprofile)
- [Java Performance Optimization](#java-performance-optimization)
    - [Relevant JVM Metrics](#relevant-jvm-metrics)
    - [Common JVM Errors](#common-jvm-errors)
    - [Tuning Jenkins GC](#tuning-jenkins-gc)
    - [Tuning Java Containers](#tuning-java-containers)
    - [Debugging java applications on OpenShift and Kubernetes](#debugging-java-applications-on-openshift-and-kubernetes)
- [List of Performance Analysis Tools](#list-of-performance-analysis-tools)
    - [Threadumps, Heapdumps and GC Analysis Tools](#threadumps-heapdumps-and-gc-analysis-tools)
        - [Capturing a Java Thread Dump](#capturing-a-java-thread-dump)
- [Garbage Collection and Heap Offloading](#garbage-collection-and-heap-offloading)
- [Cambios importantes en la gestión de memoria de Java 8 de Oracle (2014)](#cambios-importantes-en-la-gestión-de-memoria-de-java-8-de-oracle-2014)

## Java
* [reddit.com/r/java](https://www.reddit.com/r/java)
* [medium.com/@javachampions : Java is still free](https://medium.com/@javachampions/java-is-still-free-2-0-0-6b9aa8d6d244)
* [Oracle Java 11 and OpenJDK](https://blog.joda.org/2018/09/do-not-fall-into-oracles-java-11-trap.html)
* [developers.redhat.com: The future of Java and OpenJDK updates without Oracle support](https://developers.redhat.com/blog/2018/09/24/the-future-of-java-and-openjdk-updates-without-oracle-support/)
* [redhat.com: The history and future of OpenJDK](https://www.redhat.com/en/blog/history-and-future-openjdk)
* [javarevisited.blogspot.com: The 2020 Java Developer RoadMap 🌟](https://javarevisited.blogspot.com/2019/10/the-java-developer-roadmap.html)

### Existing Java Implementations
- [Oracle Java](https://www.oracle.com/technetwork/java/javase/overview/index.html)
- [Oracle OpenJDK](https://jdk.java.net/11/)
- [IBM JDK](https://developer.ibm.com/javasdk/) (based on [Eclipse OpenJ9](https://www.eclipse.org/openj9/))
- [Red Hat OpenJDK](https://developers.redhat.com/products/openjdk/download)
- [AdoptOpenJDk](https://adoptopenjdk.net/) (based on [Eclipse OpenJ9](https://www.eclipse.org/openj9/))

### Use Java 11
- [It’s time! Migrating to Java 11 🌟](https://medium.com/criciumadev/its-time-migrating-to-java-11-5eb3868354f9)
- [Oracle's Java 11 trap - Use OpenJDK instead! 🌟](https://blog.joda.org/2018/09/do-not-fall-into-oracles-java-11-trap.html)
- [**AdoptOpenJDK 11** Is the New Default 🌟](https://blog.adoptopenjdk.net/2020/06/adoptopenjdk-11-new-default/)
- [All You Need To Know For Migrating To Java 11](https://blog.codefx.org/java/java-11-migration-guide/)

### Java Programming Models (Java Frameworks)
- [Best Java Frameworks Solutions](https://www.itcentralstation.com/categories/java-frameworks) The best Java Frameworks vendors are **Apache Spark**, **Spring Boot**, **Oracle Application Development Framework (Oracle ADF)**, **Jakarta EE**, and **Open Liberty**. Apache is the top solution according to IT Central Station reviews and rankings. One reviewer writes: "Fast performance and has an easy initial setup", and another reviewer writes: "Easy to use and is capable of processing large amounts of data". The 2nd best product is Spring Boot. A user writes: "Very smooth implementation; excellent features for monitoring and tracking network calls ", and another reviewer writes: "Makes it difficult to support a specific functionality in a user-friendly manner, but simplifies application deployment".

Framework / Java Ecosystem|Technology|Cloud Native|Platform
:----|:---|:---|:---
[Java EE](https://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition)<br/>[Java EE at a Glance](https://www.oracle.com/java/technologies/java-ee-glance.html)|Frontend + Backend <br/>Java EE Monoliths|No|Java EE Middleware Servers (WAS, WebLogic, JBoss EAP, etc)
[Jakarta EE (Java EE renamed)](https://jakarta.ee/)|Frontend + Backend|Yes|OpenShift, Kubernetes, etc 
[MicroProfile](https://microprofile.io/)|Frontend+Backend|Yes|OpenShift, Kubernetes, etc
[SpringBoot (Spring)](https://spring.io/projects/spring-boot)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
[Spring Cloud (Spring)](https://spring.io/projects/spring-cloud)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
[Quarkus](https://quarkus.io/)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
etc|||

#### Spring and MicroProfile frameworks for microservices development (open source microservices frameworks)
##### Spring 
- [Spring](https://spring.io/)
- [SpringBoot](https://spring.io/projects/spring-boot)
- [Spring Cloud](https://spring.io/projects/spring-cloud)

##### Eclipse MicroProfile Project
- [Eclipse MicroProfile Project](https://projects.eclipse.org/projects/technology.microprofile) The Eclipse MicroProfile project is aimed at
optimizing Enterprise Java for the microservices architecture. 
    - Many innovative "microservice" Enterprise Java environments and frameworks already exist in the Java ecosystem. These projects are creating new features and capabilities to address microservice architectures -- leveraging both Java EE and non-Java EE technologies.
    - The goal of the Eclipse MicroProfile project is to iterate and innovate in short cycles to propose new common APIs and functionality, get community approval, release, and repeat.  Eventually, the outputs of this project could be submitted to the Eclipse Jakarta EE, JCP, OpenJDK or any relevant standards body.
- [MicroProfile.io](https://microprofile.io/) Optimizing Enterprise Java for a Microservices Architecture
- [developers.redhat.com: Eclipse MicroProfile for Spring Boot developers](https://developers.redhat.com/blog/2018/11/21/eclipse-microprofile-for-spring-boot-developers/)

##### Spring Boot VS MicroProfile
- [Dzone: Programming Styles Compared: Spring Framework vis-a-vis Eclipse MicroProfile 🌟🌟](https://dzone.com/articles/programming-styles-spring-boot-vis-a-vis-with-ecli)
- [ibm.com: Java Microservices with MicroProfile – RESTful APIs and Dependency Injection. For microservices-based Java apps, knowing how to create REST APIs is an essential skill. Eclipse MicroProfile makes it easier](https://www.ibm.com/cloud/blog/migrate-java-microservices-from-spring-to-microprofile-p2) Spring Boot or MicroProfile for Java microservices apps? Choose the path of least resistance. The Spring Boot and MicroProfile frameworks have many of the same goals (i.e., you can do everything in MicroProfile that you can do in Spring Boot). Both of them are built on top of the same core APIs; even though there are differences in some of the APIs, the work they do is similar.

## Java Performance Optimization
* [DZone refcard: java performance optimization 🌟](https://dzone.com/refcardz/java-performance-optimization) Tools and Techniques for Turbocharged Apps
- [DZone: String Concatenation's Effect on Performance](https://dzone.com/articles/string-concatentions-effect-on-performance) Don’t use the string concatenation operator to combine more than a few strings unless performance is irrelevant. Use StringBuilder’s append method instead. 
- [DZone: Performance Improvement in Java Applications: ORM/JPA 🌟](https://dzone.com/articles/performance-improvement-in-java-applications-orm-j)
- [DZone: The JVM Architecture Explained 🌟](https://dzone.com/articles/jvm-architecture-explained) An overview of the different components of the JVM, along with a very useful diagram
- [DZone: How to Troubleshoot Sudden CPU Spikes](https://dzone.com/articles/troubleshoot-sudden-cpu-spikes) Your Java application has been running fine, but all of a sudden CPU consumption starts to go higher and higher... sound familiar?
- [DZone refcard: Java Caching](https://dzone.com/refcardz/java-caching)
* [Dzone: 7 JVM Arguments of Highly Effective Applications 🌟🌟🌟](https://dzone.com/articles/7-jvm-arguments-of-highly-effective-applications-1) How to use 7 JVM arguments to help increase your application's performance and avoid common memory pitfalls.

### Relevant JVM Metrics
Metric|Details / Reference
:---|:---
GC Throughput|**Repeated Full GC happens way before OutOfMemoryError**<br/> [ref1](https://dzone.com/articles/7-jvm-arguments-of-highly-effective-applications-1)<br/>[ref2](https://blog.gceasy.io/2019/03/13/micrometrics-to-forecast-application-performance)
etc|

### Common JVM Errors
JVM Error|Details / Reference
:----|:----
OutOfMemoryError|**Repeated Full GC happens way before OutOfMemoryError** <br/> [ref1](https://dzone.com/articles/7-jvm-arguments-of-highly-effective-applications-1)<br/>[ref2](https://blog.gceasy.io/2019/03/13/micrometrics-to-forecast-application-performance)
StackOverflowError|[ref](https://blog.fastthread.io/2018/09/24/stackoverflowerror/)
etc|

### Tuning Jenkins GC
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [Running Jenkins on Java 11 🌟](https://www.jenkins.io/doc/administration/requirements/jenkins-on-java-11/#:~:text=The%20easiest%20way%20to%20run,images%2C%20use%20the%20jdk11%20tag.)

### Tuning Java Containers
* [blog.openshift.com: Scaling Java Containers 🌟](https://blog.openshift.com/scaling-java-containers/)
* [blog.openshift.com: Performance Metrics (APM) for Spring Boot Microservices on OpenShift](https://blog.openshift.com/performance-metrics-apm-spring-boot-microservices-openshift/)
* [dzone.com: Java RAM Usage in Containers: Top 5 Tips for Not Losing Your Memory](https://dzone.com/articles/java-ram-usage-in-containers-top-5-tips-not-to-los)
* [dzone.com: Running a JVM in a Container Without Getting Killed:](https://dzone.com/articles/running-a-jvm-in-a-container-without-getting-kille) Starting in JDK 9, and earlier if you use JDK 8u131, your JVM can detect how much memory is available when running inside a Docker container.
* [dzone.com: Java Inside Docker: What You Must Know to Not FAIL](https://dzone.com/articles/java-inside-docker-what-you-must-know-to-not-fail) If you've tried Java in containers, particularly Docker, you might have encountered some problems with the JVM and heap size. Here's how to fix it.

### Debugging java applications on OpenShift and Kubernetes
* [blog.openshift.com: Debugging Java Applications On OpenShift and Kubernetes](https://blog.openshift.com/debugging-java-applications-on-openshift-kubernetes/)

## List of Performance Analysis Tools
* [en.wikipedia.org/wiki/List_of_performance_analysis_tools](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)
* [InspectIT](https://en.wikipedia.org/wiki/InspectIT)
* [VisualVM](https://en.wikipedia.org/wiki/VisualVM)
* [OverOps](https://en.wikipedia.org/wiki/OverOps)
* [FusionReactor](https://en.wikipedia.org/wiki/FusionReactor)
* etc

### Threadumps, Heapdumps and GC Analysis Tools
* [tier1app.com](https://tier1app.com/)
* [fastthread.io](https://fastthread.io/)
* [gceasy.io](https://gceasy.io/)
* [heaphero.io](https://heaphero.io/)

#### Capturing a Java Thread Dump
* [baeldung.com: Capturing a Java Thread Dump](https://www.baeldung.com/java-thread-dump)

## Garbage Collection and Heap Offloading
- [Tecnologías de Heap-Offloading son EHcache, Memcached, Jillegal library, etc.](http://ehcache.org/)
- [Jillegal OffHeap Module](https://github.com/serkan-ozal/jillegal)
- [Free eGuide: JVM Troubleshooting Guide](http://freepromagazine.blogspot.de/2014/07/free-eguide-jvm-troubleshooting-guide.html)
- [Cambios importantes en la gestión de memoria de Java 8 de Oracle](http://karunsubramanian.com/websphere/one-important-change-in-memory-management-in-java-8/)
- [PermGen eliminado](http://www.infoq.com/articles/Java-PERMGEN-Removed)
- [On heap vs off heap memory usage](http://www.javacodegeeks.com/2014/12/on-heap-vs-off-heap-memory-usage.html)
- [How Garbage Collection differs in the three big JVMs](http://apmblog.dynatrace.com/2011/05/11/how-garbage-collection-differs-in-the-three-big-jvms/)
- [cubrid.org: How to Tune Java Garbage Collection](http://www.cubrid.org/blog/dev-platform/how-to-tune-java-garbage-collection)
- [DZone: Revisiting the Advanced Theories of ‘Java Garbage Collection’ 🌟](https://dzone.com/articles/revisiting-the-advanced-theories-of-java-garbage-c)
- [DZone: Understanding the Java Memory Model and Garbage Collection 🌟](https://dzone.com/articles/understanding-the-java-memory-model-and-the-garbag) In this article we will try to understand the Java memory model and how garbage collection works. In this article I have used JDK8 Oracle Hot Spot 64 bit JVM. First let me depict the different memory areas available for Java processes.
- [DZone: Memory Leaks and Java Code](https://dzone.com/articles/memory-leak-andjava-code) When you aren't using objects, but they aren't touched by GC, a memory leak happens. Here are six ways memory leaks happen to look for and avoid.

## Cambios importantes en la gestión de memoria de Java 8 de Oracle (2014)

PermGen no pertenece al heap y los objetos no son promocionados a esta sección de memoria gestionada durante un GC. Como bien dices es un espacio contiguo al heap, pero también se limpia cada vez que la tenured/old generation procede a un GC. No es una generación separada del mismo modo que es la young generation, y no hay un mecanismo específico para un GC separado de PermGen. La tenured/old generation y la permanent generation proceden a un GC cuando una de las dos se llena.

De todos modos no me queda claro si incorporaron PermGen dentro del heap en Java 7, aunque poco importa ya con los cambios en Java 8.

Mejor empiezo por introducir qué implementación de JVM es Java 8 de Oracle. Existen numerosas implementaciones de JVM y cada una utiliza diferentes soluciones para la gestión de memoria.

Dos de las soluciones más conocidas y populares de JVM han sido HotSpot de Sun (habitual en Tomcat) y JRockit de BEA (Weblogic). Ambas compañias fueron compradas por Oracle y Java 8 viene a ser la integración definitiva de ambas soluciones.

Históricamente se consideraba que HotSpot es el JVM con mejor rendimiento de las dos, si bien JRockit es valorada como la más escalable.

Originalmente en HotSpot no había generación permanente. Objetos y clases de JVM se almacenaban juntas. Las clases de ésta JVM eran estáticas y prácticamente no se utilizaban 'Class Loaders' (Load y Unload/Collection de Clases). PermGen surgió como una mejora de rendimiento. Por defecto los datos en la generación permanente no se eliminan nunca (son datos de JVM y no de aplicación, pudiendo variar según la pólítica de garbage collection). Esto podía llenar la generación permanente generando un OutOfMemoryErrors si se producía un elevado número de classloading. En muchos casos un problema con una generación permanente implica reiniciar regularmente la JVM y la aplicación Java.

Actualmente las clases de JVM son dinámicas y el espacio requerido para metadatos puede cambiar fácilmente.

A diferencia de HotSpot VM, JRockit carece de generación permanente y en cambio almacena los metadatos 'off the heap' en memoria nativa. Estos buffers de código son liberados constantemente cuando sus ClassLoaders no se utilizan. El problema de OutOfMemory en JRockit no es diferente a HotSpot, excepto por el hecho de ser memoria nativa en lugar de memoria heap. Hay dos diferencias significativas. Primero, en JRockit la limpieza de metadatos está habilitada siempre por defecto y segundo, no hay tamaño límite fijo para el espacio de metadatos. Uno de los principales problemas con HotSpot es su dificultad para seleccionar un tamaño adecuado para la generación permanente. ¿128MB, 256MB? Es muy difícil acertar para cada aplicación. JRockit es dinámico en la gestión de memoria reservada para metadatos y sin límites de tamaño (a excepción de la memoria del sistema). JRockit es también el único JVM con soporte de heaps no contiguos (uso de memoria por encima y por debajo del alojamiento del kernel y otras librerías), importante en el caso de Windows donde su kernel a menudo se ubica en mitad del espacio de direcciones.

Java 8 (HotRockit?) incorpora todas las herramientas de monitorización de HotSpot (Java VisualVM, jstat, jmap) y JRockit (Java Mission Control, Java Flight Recorder). Muy interesante.

Un inconveniente de Java 8 es la fragmentación de la memoria nativa para metadatos, pero probablemente incluya compactación en un futuro próximo.

En el 2016 saldrá Java 9 con la funcionalidad de auto-tuning y soporte de tamaños Heap multi-gigas.

En cualquier caso hay una tendencia al Heap-Offloading. El consumo de memoria en Java tiene un coste y las pausas/latencias causadas por los Full GC son proporcionales al tamaño del heap. Estas pausas son notables en tamaños de heap > 1Gb, con un considerable impacto en aplicaciones de tiempo real donde un proceso que no responde rápido puede ser descartado del cluster. Aún así, los servidores actuales hacen uso de frameworks muy pesados y fácilmente requieren heaps > 4Gb. Una solución a este problema es alojar fuera del heap los objetos poco utilizados mediante técnicas de serialización/deserialización (caché). El heap de memoria se mantiene pequeño y el Full GC se completa en milisegundos. Ejemplos:

1. caché de sesión de usuarios, donde un fichero mapeado en memoria almacena gigabytes de sesiones de usuarios inactivos. Una vez que el usuario hace log-in, la aplicación dispone de todos sus datos sin ser necesaria una consulta a la BBDD. 
2. caché de resultados computacionales como queries, páginas html, etc (donde el coste computacional es mayor a la deserialización)

<center>
<div class="container">
<iframe src="//www.slideshare.net/slideshow/embed_code/key/NpUYrnBQ59fyV6" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/feuteston/jvm-internals-2015corkdevio" title="JVM Internals (2015)" target="_blank">JVM Internals (2015)</a> </strong> from <strong><a href="//www.slideshare.net/feuteston" target="_blank">Luiz Fernando Teston</a></strong> </div>
</div>
</center>
<br/>



