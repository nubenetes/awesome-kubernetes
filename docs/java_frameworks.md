# Java and Java Programming Models. Open Source Microservices Frameworks
- [Java](#java)
    - [Existing Java Implementations](#existing-java-implementations)
    - [Use Java 11](#use-java-11)
- [Java Programming Models (Java Frameworks)](#java-programming-models-java-frameworks)
- [Spring](#spring)
    - [SpringBoot](#springboot)
    - [SpringBoot with Docker](#springboot-with-docker)
    - [CI/CD for kubernetes with SpringBoot](#cicd-for-kubernetes-with-springboot)
- [Quarkus](#quarkus)
- [Eclipse MicroProfile](#eclipse-microprofile)
- [Spring Boot VS MicroProfile](#spring-boot-vs-microprofile)

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

## Java Programming Models (Java Frameworks)
- [Best Java Frameworks Solutions](https://www.itcentralstation.com/categories/java-frameworks) The best Java Frameworks vendors are **Apache Spark**, **Spring Boot**, **Oracle Application Development Framework (Oracle ADF)**, **Jakarta EE**, and **Open Liberty**. Apache is the top solution according to IT Central Station reviews and rankings. One reviewer writes: "Fast performance and has an easy initial setup", and another reviewer writes: "Easy to use and is capable of processing large amounts of data". The 2nd best product is Spring Boot. A user writes: "Very smooth implementation; excellent features for monitoring and tracking network calls ", and another reviewer writes: "Makes it difficult to support a specific functionality in a user-friendly manner, but simplifies application deployment".
- **Open Source Microservices Frameworks** (frameworks for microservices development): 
    - [Spring](https://spring.io/projects/spring-boot) 
    - [MicroProfile](https://microprofile.io) 

Java Programming Model|Technology|Cloud Native (microservices)|Platform
:----|:---|:---|:---
[Java EE](https://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition)<br/>[Java EE at a Glance](https://www.oracle.com/java/technologies/java-ee-glance.html)|Frontend + Backend <br/>Java EE Monoliths|No|Java EE Middleware Servers (WAS, WebLogic, JBoss EAP, etc)
[Jakarta EE (Java EE renamed)](https://jakarta.ee/)|Frontend + Backend|Yes|OpenShift, Kubernetes, etc 
[MicroProfile](https://microprofile.io/)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
[SpringBoot (Spring)](https://spring.io/projects/spring-boot)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
[Spring Cloud (Spring)](https://spring.io/projects/spring-cloud)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
[Quarkus](https://quarkus.io/)|Backend (RESTful)|Yes|OpenShift, Kubernetes, etc
etc|||

<br/>

## Spring 
- [Spring](https://spring.io/)
- [SpringBoot](https://spring.io/projects/spring-boot)
- [Spring Cloud](https://spring.io/projects/spring-cloud)
    - [Spring Cloud Kubernetes for hybrid microservices architecture](https://medium.com/javarevisited/spring-cloud-kubernetes-for-hybrid-microservices-architecture-f487d67328d0)

### SpringBoot
- [SpringBoot](https://spring.io/projects/spring-boot)
- [dzone: All About Spring Boot (Tutorials and Articles)](https://dzone.com/articles/spring-boot-framework-tutorials)
- [jaxenter.com: CI/CD for Spring Boot Microservices: Part 1](https://jaxenter.com/cicd-microservices-docker-162408.html)
- [jaxenter.com: CI/CD for Spring Boot Microservices: Part 2. Extending CI/CD: Kubernetes Continuous Deployment for Microservices](https://jaxenter.com/kubernetes-microservices-162690.html)
- [dzone: Deploying Spring Boot App to JBoss Wildfly](https://dzone.com/articles/deploying-spring-boot-app-to-jboss-wildfly)
- [Spring Boot: ¿war o jar? Ambos](https://www.adictosaltrabajo.com/2018/12/13/spring-boot-war-o-jar-ambos/)
- [javatutorial.net: Spring vs. Java EE](https://javatutorial.net/spring-vs-java-ee)
- [medium.com: Spring Cloud kubernetes for hybrid microservices architecture](https://medium.com/javarevisited/spring-cloud-kubernetes-for-hybrid-microservices-architecture-f487d67328d0)
- [10 Free Spring Boot Courses and Tutorials for Java Developers](https://medium.com/javarevisited/10-free-spring-boot-tutorials-and-courses-for-java-developers-53dfe084587e)

### SpringBoot with Docker
* [spring.io: spring boot with docker](https://spring.io/guides/gs/spring-boot-docker/)
* [spring.io: Creating Docker images with Spring Boot 2.3.0.M1](https://spring.io/blog/2020/01/27/creating-docker-images-with-spring-boot-2-3-0-m1) 
* [learnk8s.io: Developing and deploying Spring Boot microservices on Kubernetes](https://learnk8s.io/spring-boot-kubernetes-guide)
* [youtube: Creating Docker Images With Spring Boot](https://www.youtube.com/watch?v=1w1Jv9qssqg)

<center>
<iframe src="https://www.youtube.com/embed/1w1Jv9qssqg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### CI/CD for kubernetes with SpringBoot
* [CI/CD for Kubernetes through a Spring Boot example (Banzai Cloud CI/CD)](https://teletype.in/@sravancynixit/CcwqFANxY)

<center>
[![microservice arch](images/microservice_arch.png)](https://medium.com/javarevisited/10-free-spring-boot-tutorials-and-courses-for-java-developers-53dfe084587e)
</center>

## Quarkus
- [quarkus.io](https://quarkus.io/) Quarkus is a Kubernetes-native Java stack that is crafted from best-of-breed Java libraries and standards, and tailored for containers and cloud deployments
- [quarkus.io: Quarkus for Spring Developers](https://quarkus.io/blog/quarkus-for-spring-developers/)
- [redhat.com: Red Hat drives future of Java with cloud-native, container-first Quarkus](https://www.redhat.com/en/blog/red-hat-drives-future-java-cloud-native-container-first-quarkus)
- [developers.redhat.com: Quarkus: A quick-start guide to the Kubernetes-native Java stack](https://developers.redhat.com/articles/quarkus-quick-start-guide-kubernetes-native-java-stack/)
- [quarkus.io: Quarkus support in IDE's](https://quarkus.io/blog/march-of-ides/)
- [dzone: quarkus refcard](https://dzone.com/refcardz/quarkus-1)
- [dzone: Build a Java REST API With Quarkus](https://dzone.com/articles/build-a-java-rest-api-with-quarkus)
- [developers.redhat.com: Autowire MicroProfile into Spring with Quarkus](https://developers.redhat.com/blog/2019/10/02/autowire-microprofile-into-spring-with-quarkus/)
- [dmcommunity.org: Who will win? Spring Boot or Quarkus](https://dmcommunity.org/2020/01/12/who-will-win-spring-boot-or-quarkus/)
- [dzone.com: Microservices: Quarkus vs. Spring Boot](https://dzone.com/articles/microservices-quarkus-vs-spring-boot) In the era of containers (the "Docker Age") Java still keeps alive, being struggling for it or not. Who will win: Spring Boot or Quarkus.
- [developers.redhat.com: How Quarkus brings imperative and reactive programming together](https://developers.redhat.com/blog/2019/11/18/how-quarkus-brings-imperative-and-reactive-programming-together/)
- [developers.redhat.com: Migrating a Spring Boot microservices application to Quarkus](https://developers.redhat.com/blog/2020/04/10/migrating-a-spring-boot-microservices-application-to-quarkus/)
- [Quarkus, a Kubernetes-native Java runtime, now fully supported by Red Hat](https://developers.redhat.com/blog/2020/05/28/quarkus-a-kubernetes-native-java-runtime-now-fully-supported-by-red-hat/)

## Eclipse MicroProfile
- [Eclipse MicroProfile Project](https://projects.eclipse.org/projects/technology.microprofile) The Eclipse MicroProfile project is aimed at
optimizing Enterprise Java for the microservices architecture. 
    - Many innovative "microservice" Enterprise Java environments and frameworks already exist in the Java ecosystem. These projects are creating new features and capabilities to address microservice architectures -- leveraging both Java EE and non-Java EE technologies.
    - The goal of the Eclipse MicroProfile project is to iterate and innovate in short cycles to propose new common APIs and functionality, get community approval, release, and repeat.  Eventually, the outputs of this project could be submitted to the Eclipse Jakarta EE, JCP, OpenJDK or any relevant standards body.
- [MicroProfile.io](https://microprofile.io/) Optimizing Enterprise Java for a Microservices Architecture
- [developers.redhat.com: Eclipse MicroProfile for Spring Boot developers](https://developers.redhat.com/blog/2018/11/21/eclipse-microprofile-for-spring-boot-developers/)
- [Eclipse MicroProfile: 5 Things You Need to Know 🌟](https://medium.com/@alextheedom/eclipse-microprofile-5-things-you-need-to-know-e7a0bc9a3fb6)
- **Server Vendors providing MicroProfile runtimes**:
    - [WebSphere Liberty from IBM](https://developer.ibm.com/wasdev/websphere-liberty/)
    - [TomEE from Tomitribe](http://tomee.apache.org/)
    - [Payara](https://www.payara.fish/)
    - [RedHat’s WildFly Swarm](http://wildfly-swarm.io/)
    - [KumuluzEE](https://ee.kumuluz.com/)

## Spring Boot VS MicroProfile
- [Dzone: Programming Styles Compared: Spring Framework vis-a-vis Eclipse MicroProfile 🌟🌟](https://dzone.com/articles/programming-styles-spring-boot-vis-a-vis-with-ecli)
- [ibm.com: Java Microservices with MicroProfile – RESTful APIs and Dependency Injection. For microservices-based Java apps, knowing how to create REST APIs is an essential skill. Eclipse MicroProfile makes it easier](https://www.ibm.com/cloud/blog/migrate-java-microservices-from-spring-to-microprofile-p2) Spring Boot or MicroProfile for Java microservices apps? Choose the path of least resistance. The Spring Boot and MicroProfile frameworks have many of the same goals (i.e., you can do everything in MicroProfile that you can do in Spring Boot). Both of them are built on top of the same core APIs; even though there are differences in some of the APIs, the work they do is similar.