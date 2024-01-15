# Client Libraries for Kubernetes

1. [Kubernetes Client Libraries](#kubernetes-client-libraries)
2. [Go Clients for Kubernetes](#go-clients-for-kubernetes)
3. [Python Client for Kubernetes](#python-client-for-kubernetes)
4. [Java Clients for Kubernetes](#java-clients-for-kubernetes)
    1. [Official Java client library for kubernetes](#official-java-client-library-for-kubernetes)
    2. [Fabric8 Java Client for Kubernetes](#fabric8-java-client-for-kubernetes)
5. [CDK8s](#cdk8s)
6. [Eclipse Jkube Java Client for Kubernetes (formerly known as Fabric8). Kubernetes \& OpenShift Maven Plugins](#eclipse-jkube-java-client-for-kubernetes-formerly-known-as-fabric8-kubernetes--openshift-maven-plugins)
7. [Java Operator SDK](#java-operator-sdk)

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
    - [pkg.go.dev/k8s.io/client-go](https://pkg.go.dev/k8s.io/client-go)
- [Rate Limiting in Controller-Runtime and Client-go](https://danielmangum.com/posts/controller-runtime-client-go-rate-limiting/)
- [kubernetes-client/go: OpenAPI based Generated Go client for Kubernetes](https://github.com/kubernetes-client/go)
- [kyaml2go (Pronounced as camel2go 🐫) 🌟](https://github.com/PrasadG193/kyaml2go) K8s Go client code generator from Kubernetes resource yamls.
- [itnext.io: Writing a Kubernetes CLI in Go](https://itnext.io/writing-a-kubernetes-cli-in-go-a3970ad58299)
- [blog.devgenius.io: Learn Kubernetes Programming — Part 1](https://blog.devgenius.io/learn-kubernetes-programming-part-1-7384e5f3c481) Learn to programmatically talk to the Kubernetes cluster using the Official Client Go Library. In this tutorial, you'll learn how to build a simple CLI that connects to the Kubernetes cluster and displays the server version. In the process, you will learn Go and the client-go package.
- [iximiuz.com: How To Develop Kubernetes CLIs Like a Pro](https://iximiuz.com/en/posts/kubernetes-api-go-cli/) Build You Own kubectl The Simple Way. Learn how to use the http://k8s.io/cli-runtime library to develop Kubernetes CLI tools that behave like and are as potent as the mighty kubectl.

## Python Client for Kubernetes

- [github.com/kubernetes-client/python](https://github.com/kubernetes-client/python)
- [github.com/kubernetes-client/python-base](https://github.com/kubernetes-client/python-base)
- [==medium.com/@dimitrijevskiv: Monitor Kubernetes pod status from a Jenkins pipeline==](https://medium.com/@dimitrijevskiv/monitor-kubernetes-pod-status-from-a-jenkins-pipeline-e25c744d944d)
- [blog.devgenius.io: Automate Kubernetes With Python 🌟](https://blog.devgenius.io/automate-kubernetes-with-python-2150c290afe7) The Kubernetes Python module is a very powerful client that allows you to easily automate interactions with a Kubernetes cluster.
- [martinheinz.dev/blog/73: Automate All the Boring Kubernetes Operations with Python 🌟](https://martinheinz.dev/blog/73) In this article, you will look at how you can leverage the Kubernetes Python Client library to automate any tasks. Examples:
    - Triggering a rollout
    - Scaling a deployment
    - Applying taints
    - Retrieving metrics
    - Backing up all resources in a namespace

## Java Clients for Kubernetes

- [==itnext.io: Difference between Fabric8 and Official Kubernetes Java Client== 🌟](https://itnext.io/difference-between-fabric8-and-official-kubernetes-java-client-3e0a994fd4af)

### Official Java client library for kubernetes

- [github.com/kubernetes-client/java: Kubernetes Java Client](https://github.com/kubernetes-client/java) Official Java client library for kubernetes

### Fabric8 Java Client for Kubernetes

- [Fabric8](https://fabric8.io/) has been available as a Java client for Kubernetes since 2015, and today is one of the most popular client libraries for Kubernetes (the most popular is [client-go](https://github.com/kubernetes/client-go), which is the client library for the Go programming language on Kubernetes). In recent years, **fabric8 has evolved from a Java client for the Kubernetes REST API to a full-fledged alternative to the kubectl command-line tool for Java-based development**.
- [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client/)
- [developers.redhat.com: How the fabric8 Maven plug-in deploys Java applications to OpenShift](https://developers.redhat.com/blog/2020/05/28/how-the-fabric8-maven-plug-in-deploys-java-applications-to-openshift/)
- [Fabric8.io Microservices Development Platform](https://fabric8.io/) It is an open source microservices platform based on Docker, Kubernetes and Jenkins. It is built by the Red Hat guys.The purpose of the project is to make it easy to create microservices, build, test and deploy them via Continuous Delivery pipelines then run and manage them with Continuous Improvement and ChatOps. Fabric8 installs and configures the following things for you automatically: Jenkins, Gogs, Fabric8 registry, Nexus, SonarQube.
- [developers.redhat.com: What’s new in Fabric8 Kubernetes Java client 4.12.0](https://developers.redhat.com/blog/2020/10/30/whats-new-in-fabric8-kubernetes-java-client-4-12-0/)
- [blog.marcnuri.com: Fabric8 Kubernetes Client for Java introduction](https://blog.marcnuri.com/kubernetes-client-java-fabric8-introduction)
- [blog.marcnuri.com: Build Kubernetes controllers with Fabric8 Kubernetes Client, Quarkus, and JKube](https://blog.marcnuri.com/fabric8-kubernetes-java-client-and-quarkus-and-graalvm)
- [developers.redhat.com: How to generate code using Fabric8 Kubernetes Client](https://developers.redhat.com/articles/2023/01/24/how-generate-code-using-fabric8-kubernetes-client)
- [==levelup.gitconnected.com: First Try on Java Operator SDK==](https://levelup.gitconnected.com/first-try-on-java-operator-sdk-5a07f30771de) Demo on java-operator-sdk and compare it with Kubebuilder
- [developers.redhat.com: How to use Fabric8 Java Client with Kubernetes](https://developers.redhat.com/articles/2023/01/04/how-use-fabric8-java-client-kubernetes) In this 5-part series, you'll learn how to use Fabric8 Kubernetes Client to interact with Kubernetes custom resources using its REST API

## CDK8s

- [cdk8s](https://github.com/cdk8s-team/cdk8s) Define Kubernetes native apps and abstractions using object-oriented programming
- [blog.twstewart.me: cdk8s-python - A Love and Hate Experience](https://blog.twstewart.me/posts/cdk8s-python) CDK8S is an alpha level library that allows you to write high level abstractions of Kubernetes objects like deployments, services, and more all in your favorite language ( TypeScript, Python, and others).
- [qdnqn.com: Kubernetes objects from Go to YAML using Cdk8s](https://qdnqn.com/create-kubernetes-yaml-definitions-using-go-and-cdk8s/) Cdk8s is an open-source software development framework for defining Kubernetes applications and reusable abstractions using familiar programming languages and rich object-oriented APIs. cdk8s apps synthesize into standard Kubernetes manifests which can be applied to any Kubernetes cluster.

## Eclipse Jkube Java Client for Kubernetes (formerly known as Fabric8). Kubernetes & OpenShift Maven Plugins

- [Eclipse JKube 🌟](https://www.eclipse.org/jkube/) Cloud-Native Java Applications without a hassle. Eclipse JKube is a collection of plugins and libraries that are used for building container images using Docker, JIB or S2I build strategies. Eclipse JKube generates and deploys Kubernetes/OpenShift manifests at compile time too. It brings your Java applications on to Kubernetes and OpenShift by leveraging the tasks required to make your application cloud-native. Eclipse JKube also provides a set of tools such as watch, debug, log, etc. to improve your developer experience.
- [Github: Eclipse Jkube](https://github.com/eclipse/jkube)
- [developers.redhat.com: Migrating from Fabric8 Maven Plugin to Eclipse JKube 1.0.0](https://developers.redhat.com/blog/2020/09/21/migrating-from-fabric8-maven-plugin-to-eclipse-jkube-1-0-0/)
- [developers.redhat.com: Cloud-native Java applications made easy: Eclipse JKube 1.0.0 now available](https://developers.redhat.com/blog/2020/09/09/cloud-native-java-applications-made-easy-eclipse-jkube-1-0-0-now-available/)
- [developers.redhat.com: Java development on top of Kubernetes using Eclipse JKube](https://developers.redhat.com/blog/2020/08/24/java-development-on-top-of-kubernetes-using-eclipse-jkube/)
- [eclipse.org: Migration Guide for projects using Fabric8 Maven Plugin to Eclipse JKube 🌟](https://www.eclipse.org/jkube/docs/migration-guide/)
- [youtube: Deploying a Quarkus application into Kubernetes using JKube | Cloud Tool Time | Marc Nuri 🌟](https://www.youtube.com/watch?v=HDDfdZqwM1E&ab_channel=EclipseFoundation)
- [blog.marcnuri.com](https://blog.marcnuri.com/)
    - [blog.marcnuri.com: Eclipse JKube 1.4.0 is now available!](https://blog.marcnuri.com/eclipse-jkube-1-4-0)
- [developers.redhat.com: How to manage microservices using OpenShift Dev Spaces and JKube](https://developers.redhat.com/developer-sandbox/activities/how-to-manage-microservices-using-openshift-dev-spaces-and-jkube)

## Java Operator SDK

- [javaoperatorsdk.io: Build Kubernetes Operators in Java without hassle](https://javaoperatorsdk.io/) Whether you want to build applications that operate themselves or provision infrastructure from Java code, Kubernetes Operators are the way to go. This SDK will make it easy for Java developers to embrace this new way of automation. The java-operator-sdk is based on the fabric8 Kubernetes client.
