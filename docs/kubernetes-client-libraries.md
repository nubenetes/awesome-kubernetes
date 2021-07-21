# Client Libraries for Kubernetes
- [Kubernetes Client Libraries](#kubernetes-client-libraries)
- [Go Clients for Kubernetes](#go-clients-for-kubernetes)
- [Python Client for Kubernetes](#python-client-for-kubernetes)
- [Fabric8 Java Client for Kubernetes (deprecated)](#fabric8-java-client-for-kubernetes-deprecated)
- [Eclipse Jkube Java Client for Kubernetes (formerly known as Fabric8). Kubernetes & OpenShift Maven Plugins](#eclipse-jkube-java-client-for-kubernetes-formerly-known-as-fabric8-kubernetes--openshift-maven-plugins)
- [Java Operator SDK](#java-operator-sdk)
## Kubernetes Client Libraries
- [github.com/kubernetes-client 🌟](https://github.com/kubernetes-client)
- [medium: Building stuff with the Kubernetes API — TOC 🌟](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-toc-84d751876650)
    - [Part 1 — Exploring API objects](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-1-cc50a3642)
    - [Part 2 — Using the Java client framework](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-part-2-using-java-ceb8a5ff7920)
    - [Part 3 — Using the Python client framework](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-part-3-using-python-aea5ab16f627)
    - [Part 4 — Using the Go client framework](https://medium.com/programming-kubernetes/building-stuff-with-the-kubernetes-api-part-4-using-go-b1d0e3c1c899)
- [k8s-ruby: Kubernetes Ruby Client](https://github.com/k8s-ruby/k8s-ruby)
## Go Clients for Kubernetes
- [kubernetes/client-go: Go client for Kubernetes 🌟](https://github.com/kubernetes/client-go) Go clients for talking to a kubernetes cluster.
- [Rate Limiting in Controller-Runtime and Client-go](https://danielmangum.com/posts/controller-runtime-client-go-rate-limiting/)
- [kubernetes-client/go: OpenAPI based Generated Go client for Kubernetes](https://github.com/kubernetes-client/go)
- [kyaml2go (Pronounced as camel2go 🐫) 🌟](https://github.com/PrasadG193/kyaml2go) K8s Go client code generator from Kubernetes resource yamls.

## Python Client for Kubernetes
- [github.com/kubernetes-client/python](https://github.com/kubernetes-client/python)
- [github.com/kubernetes-client/python-base](https://github.com/kubernetes-client/python-base)
## Fabric8 Java Client for Kubernetes (deprecated)
- [Fabric8](https://fabric8.io/) has been available as a Java client for Kubernetes since 2015, and today is one of the most popular client libraries for Kubernetes (the most popular is [client-go](https://github.com/kubernetes/client-go), which is the client library for the Go programming language on Kubernetes). In recent years, **fabric8 has evolved from a Java client for the Kubernetes REST API to a full-fledged alternative to the kubectl command-line tool for Java-based development**.
- [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client/)
- [developers.redhat.com: How the fabric8 Maven plug-in deploys Java applications to OpenShift](https://developers.redhat.com/blog/2020/05/28/how-the-fabric8-maven-plug-in-deploys-java-applications-to-openshift/)
- [Fabric8.io Microservices Development Platform](https://fabric8.io/) It is an open source microservices platform based on Docker, Kubernetes and Jenkins. It is built by the Red Hat guys.The purpose of the project is to make it easy to create microservices, build, test and deploy them via Continuous Delivery pipelines then run and manage them with Continuous Improvement and ChatOps. Fabric8 installs and configures the following things for you automatically: Jenkins, Gogs, Fabric8 registry, Nexus, SonarQube.
- [developers.redhat.com: What’s new in Fabric8 Kubernetes Java client 4.12.0](https://developers.redhat.com/blog/2020/10/30/whats-new-in-fabric8-kubernetes-java-client-4-12-0/) 

## Eclipse Jkube Java Client for Kubernetes (formerly known as Fabric8). Kubernetes & OpenShift Maven Plugins
- [Eclipse JKube 🌟](https://www.eclipse.org/jkube/) Cloud-Native Java Applications without a hassle. Eclipse JKube is a collection of plugins and libraries that are used for building container images using Docker, JIB or S2I build strategies. Eclipse JKube generates and deploys Kubernetes/OpenShift manifests at compile time too. It brings your Java applications on to Kubernetes and OpenShift by leveraging the tasks required to make your application cloud-native. Eclipse JKube also provides a set of tools such as watch, debug, log, etc. to improve your developer experience.
- [Github: Eclipse Jkube](https://github.com/eclipse/jkube)
- [developers.redhat.com: Migrating from Fabric8 Maven Plugin to Eclipse JKube 1.0.0](https://developers.redhat.com/blog/2020/09/21/migrating-from-fabric8-maven-plugin-to-eclipse-jkube-1-0-0/)
- [developers.redhat.com: Cloud-native Java applications made easy: Eclipse JKube 1.0.0 now available](https://developers.redhat.com/blog/2020/09/09/cloud-native-java-applications-made-easy-eclipse-jkube-1-0-0-now-available/)
- [developers.redhat.com: Java development on top of Kubernetes using Eclipse JKube](https://developers.redhat.com/blog/2020/08/24/java-development-on-top-of-kubernetes-using-eclipse-jkube/)
- [eclipse.org: Migration Guide for projects using Fabric8 Maven Plugin to Eclipse JKube 🌟](https://www.eclipse.org/jkube/docs/migration-guide/)
- [youtube: Deploying a Quarkus application into Kubernetes using JKube | Cloud Tool Time | Marc Nuri 🌟](https://www.youtube.com/watch?v=HDDfdZqwM1E&ab_channel=EclipseFoundation)

## Java Operator SDK
- [javaoperatorsdk.io: Build Kubernetes Operators in Java without hassle](https://javaoperatorsdk.io/) Whether you want to build applications that operate themselves or provision infrastructure from Java code, Kubernetes Operators are the way to go. This SDK will make it easy for Java developers to embrace this new way of automation. The java-operator-sdk is based on the fabric8 Kubernetes client.