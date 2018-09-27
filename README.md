# awesome-2018
A curated list of awesome references collected in 2018

# Table of Contents
<!-- TOC -->

- [awesome-2018](#awesome-2018)
- [Table of Contents](#table-of-contents)
- [CI/CD](#cicd)
- [Jenkins](#jenkins)
    - [Performance Testing with Jenkins and JMeter](#performance-testing-with-jenkins-and-jmeter)
    - [Jenkins and Openshift](#jenkins-and-openshift)
- [Kubernetes](#kubernetes)
    - [Docker](#docker)
    - [Openshift Kubernetes](#openshift-kubernetes)
    - [Java Performance Optimization](#java-performance-optimization)
    - [Debugging java applications on openshift and kubernetes](#debugging-java-applications-on-openshift-and-kubernetes)
    - [Troubleshooting openshift network performance](#troubleshooting-openshift-network-performance)
- [SonarQube](#sonarqube)
- [Nexus](#nexus)
- [Maven](#maven)
- [Git](#git)
- [Visual Studio](#visual-studio)
- [Terraform](#terraform)
- [Ansible](#ansible)

<!-- /TOC -->

# CI/CD
* [opensource.com: What is CI/CD?](https://opensource.com/article/18/8/what-cicd)
* [Awesome Continuous Integration and Continuous Delivery](https://github.com/ciandcd/awesome-ciandcd)

# Jenkins
* https://jenkins.io/
* [dzone.com: Jenkins Configuration as Code: Need for Speed! 🌟🌟🌟🌟](https://dzone.com/articles/jenkins-configuration-as-code-need-for-speed)
    * https://github.com/jenkinsci/configuration-as-code-plugin
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [dzone.com: How to Set Up Scalable Jenkins on Top of a Kubernetes Cluster 🌟🌟🌟](https://dzone.com/articles/how-to-setup-scalable-jenkins-on-top-of-a-kubernet)
* [devops.com: Kubernetes Jenkins Master-Slave: Scaling the Scalability Issue](https://devops.com/kubernetes-jenkins-master-slave-scaling-the-scalability-issue/)
* [udemy.com: Master Jenkins CI For DevOps and Developers](https://www.udemy.com/the-complete-jenkins-course-for-developers-and-devops/)
* [Jenkins Docker Image for Openshift v3](https://github.com/openshift/jenkins)
* [Official Jenkins Docker image](https://github.com/michaelneale/jenkins-ci.org-docker)
* https://github.com/jenkinsci
* https://github.com/jenkinsci/performance-plugin
* https://github.com/geerlingguy/ansible-role-jenkins
* https://github.com/sahilsk/awesome-jenkins
* https://www.reddit.com/r/jenkinsci 🌟🌟
* https://jenkins.io/doc/book/pipeline/jenkinsfile/ 🌟
* [DZone refcard: declarative pipeline with jenkins 🌟🌟](https://dzone.com/refcardz/declarative-pipeline-with-jenkins)
* [Dzone refcard: Continuous Delivery with Jenkins Workflow](https://dzone.com/refcardz/continuous-delivery-with-jenkins-workflow)
* [Dzone refcard: Jenkins on PaaS. Continuous Integration with Jenkins for Java Projects. Includes a review of the most useful plugins, best practices, security, integration to an enterprise environment, and more.](https://dzone.com/asset/download/230)
* [7 Ways to Optimize Jenkins](https://www.sitepoint.com/7-ways-optimize-jenkins/)
* [opensource.com: Running Jenkins builds in Openshift containers](https://opensource.com/article/18/4/running-jenkins-builds-containers)

## Performance Testing with Jenkins and JMeter
* https://github.com/jenkinsci/performance-plugin
* https://github.com/jenkinsci/performance-plugin
* https://www.blazemeter.com/blog/continuous-integration-101-how-run-jmeter-jenkins 🌟
* https://www.baeldung.com/jenkins-and-jmeter
* https://dzone.com/articles/2-ways-to-integrate-jmeter-tests-into-jenkins
* https://www.guru99.com/jenkins-jmeter-blazemeter.html

## Jenkins and Openshift
* [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟🌟](https://blog.openshift.com/building-declarative-pipelines-openshift-dsl-plugin/)
* [slideshare.net: CI/CD with Openshift and Jenkins 🌟🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)
* [slideshare.net: OPENSHIFT CONTAINER PLATFORM CI/CD Build & Deploy  🌟🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)

# Kubernetes
* [youtube: Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [Awesome kubernetes 🌟🌟🌟🌟](https://github.com/ramitsurana/awesome-kubernetes)
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟🌟🌟](https://stackify.com/kubernetes-docker-deployments/)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)

## Docker
* [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
* [Dzone refcard: Getting Started with Docker](https://dzone.com/refcardz/getting-started-with-docker-1)
* [Dzone refcard: Java Containerization 🌟](https://dzone.com/refcardz/java-containerization)

## Openshift Kubernetes
* [Openshift Awesome 🌟](https://github.com/dudash/openshift-is-awesome)
* [Openshift Awesome List 2](https://github.com/oscp/awesome-openshift3)
* [Dzone: OpenShift Quick Start 🌟🌟](https://dzone.com/articles/openshift-quick-start)
* [blog.openshift.com: Installing OKD 3.10 on a Single Host 🌟🌟🌟🌟](https://blog.openshift.com/installing-okd-3-10-on-a-single-host/)
    * [youtube.com: OpenShift Origin is now OKD. Installation of OKD 3.10 from start to finish](https://www.youtube.com/watch?v=ZkFIozGY0IA)
    * [Install RedHat OKD 3.10 on your development box:](https://github.com/gshipley/installcentos) This repository is a set of scripts that will allow you easily install the latest version (3.10) of OKD in a single node fashion. What that means is that all of the services required for OKD to function (master, node, etcd, etc.) will all be installed on a single host. The script supports a custom hostname which you can provide using the interactive mode.]
    * A few other options to use OKD locally include [oc cluster up](https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md) and [minishift](https://www.okd.io/minishift/). These may be a better fit for your use case if you only need a quick throwaway environment.
* [developers.redhat.com: **Red Hat Container Development Kit** 🌟🌟🌟](https://developers.redhat.com/products/cdk/overview/)
* [udemy.com: Red Hat OpenShift With Jenkins: DevOps For Beginners 🌟🌟🌟🌟](https://www.udemy.com/red-hat-openshift)
* [blog.openshift.com: Introducing Red Hat Quay 🌟](https://blog.openshift.com/introducing-red-hat-quay/)
* [redhat.com: **How to gather and display metrics in Red Hat OpenShift** (Prometheus + Grafana)](https://www.redhat.com/en/blog/how-gather-and-display-metrics-red-hat-openshift)
* [claydesk.com: Google Cloud App Engine Vs Red Hat OpenShift](https://www.claydesk.com/ecampus/google-cloud-app-engine-vs-red-hat/)
* https://github.com/fabric8io/fabric8-pipeline-library
* https://fabric8.io/
* https://twitter.com/openshift 🌟

## Java Performance Optimization
* [Dzone refcard: Java Peformance Optimization](https://dzone.com/refcardz/java-performance-optimization)
* [Monitorización y análisis de rendimiento de aplicaciones con Dynatrace APM](https://www.adictosaltrabajo.com/tutoriales/monitorizacion-y-analisis-de-rendimiento-de-aplicaciones-con-dynatrace/)
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [blog.openshift.com: Scaling Java Containers 🌟🌟🌟🌟](https://blog.openshift.com/scaling-java-containers/)
* [blog.openshift.com: Performance Metrics (APM) for Spring Boot Microservices on OpenShift](https://blog.openshift.com/performance-metrics-apm-spring-boot-microservices-openshift/)
* [dzone.com: Java RAM Usage in Containers: Top 5 Tips for Not Losing Your Memory](https://dzone.com/articles/java-ram-usage-in-containers-top-5-tips-not-to-los)
* [dzone.com: Running a JVM in a Container Without Getting Killed:](https://dzone.com/articles/running-a-jvm-in-a-container-without-getting-kille) Starting in JDK 9, and earlier if you use JDK 8u131, your JVM can detect how much memory is available when running inside a Docker container.
* [dzone.com: Java Inside Docker: What You Must Know to Not FAIL](https://dzone.com/articles/java-inside-docker-what-you-must-know-to-not-fail) If you've tried Java in containers, particularly Docker, you might have encountered some problems with the JVM and heap size. Here's how to fix it.
* [medium.com/@javachampions : Java is still free](https://itnext.io/java-is-still-free-c02aef8c9e04)
* [Oracle Java 11 and OpenJDK](https://blog.joda.org/2018/09/do-not-fall-into-oracles-java-11-trap.html)

## Debugging java applications on openshift and kubernetes
* [blog.openshift.com: Debugging Java Applications On OpenShift and Kubernetes](https://blog.openshift.com/debugging-java-applications-on-openshift-kubernetes/)

## Troubleshooting openshift network performance
* [blog.openshift.com: Troubleshooting OpenShift network performance with a netperf DaemonSet](https://blog.openshift.com/troubleshooting-openshift-network-performance-with-a-netperf-daemonset/)

# SonarQube
* https://www.sonarqube.org/
* https://dzone.com/articles/code-analysis-part-2-analyzing-code-with-sonarqube

# Nexus
* https://www.sonarqube.org/
* https://dzone.com/articles/code-analysis-part-2-analyzing-code-with-sonarqube

# Maven
* https://maven.apache.org/
* https://dzone.com/articles/starting-with-apache-maven
* https://dzone.com/articles/solving-dependency-conflicts-in-maven

# Git
* [The awesome git cheat sheet](https://the-awesome-git-cheat-sheet.com/)
* [9 awesome git tricks](https://tychoish.com/post/9-awesome-git-tricks/)
* [Awesome Git 🌟](https://github.com/dictcp/awesome-git)
* [dzone.com: intro git 🌟](https://dzone.com/articles/intro-git)
* [dzone.com: refcard - getting started with git](https://dzone.com/refcardz/getting-started-git)
* [dzone.com: Top 20 git commands with examples 🌟](https://dzone.com/articles/top-20-git-commands-with-examples)
* [dzone.com: 8 Useful But Not Well-Known Git Concepts. These lesser-known Git tricks can help you solve problems that are not handled well by the GitHub and BitBucket GUIs](https://dzone.com/articles/8-useful-but-not-well-known-git-concepts)
* [dzone.com: Git Commands Tutorial - Part 1](https://dzone.com/articles/git-commands-tutorial-part-1)
* [dzone.com: Git Commands Tutorial - Part 2](https://dzone.com/articles/git-commands-tutorial-part-2)
* [Dzone refcard: Getting started with Git](https://dzone.com/refcardz/getting-started-git)
* [Oh shit, git!](https://ohshitgit.com/)

# Visual Studio
* [Awesome Visual Studio Code](https://github.com/viatsko/awesome-vscode)

# Terraform
* https://www.terraform.io/
* https://github.com/shuaibiyy/awesome-terraform
* https://github.com/Azure/awesome-terraform
* https://github.com/ozbillwang/terraform-best-practices

# Ansible
* https://github.com/jdauphant/awesome-ansible
* https://github.com/awesome-devops/awesome-ansible