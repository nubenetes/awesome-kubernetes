# Chaos Engineering

1. [Introduction](#introduction)
2. [Chaos Engineering for kubernetes/Openshift](#chaos-engineering-for-kubernetesopenshift)
3. [Chaos Engineering for serverless computing](#chaos-engineering-for-serverless-computing)
4. [Other Chaos Engineering Tools](#other-chaos-engineering-tools)
5. [Videos](#videos)

## Introduction

- [thenewstack.io: Chaos Engineering Is Not Just for Ops](https://thenewstack.io/chaos-engineering-is-not-just-for-ops/)
- [==dzone: How to Pinpoint and Fix Distributed Problems Across Microservices==](https://dzone.com/articles/how-to-pinpoint-and-fix-distributed-problems-acros) While logical separation of APIs fosters parallel development of independent functions, complexity and interdependency becomes harder to manage.
- [thenewstack.io: Why Chaos Engineering Isn’t Just for Operations](https://thenewstack.io/why-chaos-engineering-isnt-just-for-operations/)
- [medium.com/adidoescode: Chaos Engineering: How simulating adversity can help build eCommerce Resilience](https://medium.com/adidoescode/chaos-engineering-how-simulating-adversity-can-help-build-ecommerce-resilience-4a799c8912dc)
- [opsmx.com: What is Chaos Engineering?](https://www.opsmx.com/blog/what-is-chaos-engineering/)
- [aws.amazon.com: Verify the resilience of your workloads using Chaos Engineering](https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering/)
- [faun.pub: What is Chaos Engineering?](https://faun.pub/what-is-chaos-engineering-a89b64db9af0) Chaos Engineering is the discipline of experimenting on a system in order to build confidence in the system’s capability to withstand turbulent conditions in production.

## Chaos Engineering for kubernetes/Openshift

- [reddit: Help with Kube Monkey setup](https://www.reddit.com/r/openshift/comments/e1j5qzrbac_for_container_access_to_destroy_other/)
- [GitHub: kube-monkey](https://github.com/asobti/kube-monkey) An implementation of Netflix's Chaos Monkey for Kubernetes clusters
- [GitHub: monkey-ops, Openshift compliant, no cluster-admin required](https://github.comjoshmsmith/monkey-ops)
- [chaoskube periodically kills random pods in your Kubernetes cluster](https://github.com/linkichaoskube)
- [Chaos Mesh](https://github.com/pingcap/chaos-mesh)
- [Litmus Chaos is a toolset to do chaos engineering in a kubernetes native way. Litmus provides chaos CRDs for Cloud-Native developers and SREs to inject, orchestrate and monitor chaos to find weaknesses in Kubernetes deployments](https://github.com/litmuschaos/litmus)
    - [cloud.redhat.com: Chaos Engineering With LitmusChaos](https://cloud.redhat.com/blog/chaos-engineering-with-litmuschaos)
- [thenewstack.io: Using Chaos Engineering to Improve the Resilience of Stateful Applications on Kubernetes](https://thenewstack.io/using-chaos-engineering-to-improve-the-resilience-of-stateful-applications-on-kubernetes/)
- [infoq.com: Chaos Engineering on Kubernetes : Chaos Mesh Generally Available with v1.0](https://www.infoq.com/news/2020/10/kubernetes-chaos-mesh-ga/)
- [chaos-mesh.org: Chaos Mesh 1.0: Chaos Engineering on Kubernetes Made Easier](https://chaos-mesh.org/blog/chaos-mesh-1.0-chaos-engineering-on-kubernetes-made-easier/)
- [thenewstack.io: Develop a Daily Reporting System for Chaos Mesh to Improve System Resilience](https://thenewstack.io/develop-a-daily-reporting-system-for-chaos-mesh-to-improve-system-resilience/)
- [pingcap.com: chaos-mesh-action: Integrate Chaos Engineering into Your CI](https://pingcap.com/blog/chaos-mesh-action-integrate-chaos-engineering-into-your-ci)
- [openshift.com: Introduction to Kraken, a Chaos Tool for OpenShift/Kubernetes](https://www.openshift.com/blog/introduction-to-kraken-a-chaos-tool-for-openshift/kubernetes)
- [thenewstack.io: Chaos Engineering Progressively Moves to Production](https://thenewstack.io/chaos-engineering-progressively-moves-to-production/)
- [blog.flant.com: Open Source solutions for chaos engineering in Kubernetes](https://blog.flant.com/chaos-engineering-in-kubernetes-open-source-tools/)
    - kube-monkey
    - chaoskube
    - Chaos Mesh
    - Litmus Chaos
    - Chaos Toolkit
    - KubeInvaders
- [PowerfulSeal](https://github.com/powerfulseal/powerfulseal) injects failure into your Kubernetes clusters, so that you can detect problems as early as possible. It allows for writing scenarios describing complete chaos experiments.
- [devopscurry.com: How Chaos Engineering plays a vital role in devops success](https://devopscurry.com/how-chaos-engineering-plays-a-vital-role-in-devops-success)
- [BuggyApp: Simulate performance problems](https://buggyapp.ycrash.io/) BuggyApp can simulate various performance problems like Memory Leak, OutOfMemoryError, CPU spike, thread leak StackOverflowError, deadlock, unresponsiveness and so on. [youtube: BuggyApp Demo](https://www.youtube.com/watch?v=exsv-RUrUFY&t=2s&ab_channel=yCrash)
- [medium.com: Getting Started with Chaos Engineering](https://1829034.medium.com/getting-started-with-chaos-engineering-13e85a438d37)
- [Chaos Mesh 🌟](https://chaos-mesh.org/) A Powerful Chaos Engineering Platform for Kubernetes - [github ref](https://github.com/chaos-mesh/chaos-mesh)
- [opensource.com: 5 lessons I learned about chaos engineering for Kubernetes](https://opensource.com/article/21/10/chaos-engineering-kubernetes-ebook)
- [thenewstack.io: Chaos Engineering Made Simple](https://thenewstack.io/chaos-engineering-made-simple/)
- [thenewstack.io: Use Chaos Engineering to Strengthen Your Incident Response](https://thenewstack.io/use-chaos-engineering-to-strengthen-your-incident-response/)
- [thenewstack.io: Operationalizing Chaos Engineering with GitOps](https://thenewstack.io/operationalizing-chaos-engineering-with-gitops/)
- [medium.com/better-practices: Learn how your Kubernetes clusters respond to failure using Gremlin and Grafana](https://medium.com/better-practices/chaos-d3ef238ec328) Building resilient APIs with chaos engineering
- [Chaos engineering on Amazon EKS using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator/)
- [aws.amazon.com: Chaos Engineering with LitmusChaos on Amazon EKS](https://aws.amazon.com/blogs/containers/chaos-engineering-with-litmuschaos-on-amazon-eks/) In this tutorial, you will create an Amazon EKS cluster, install LitmusChaos and deploy a demo application. Then, you will define chaos experiments to be run on it and observe the behaviour
- [blog.container-solutions.com: Comparing Chaos Engineering Tools for Kubernetes Workloads](https://blog.container-solutions.com/comparing-chaos-engineering-tools) How do Chaos Toolkit, Pumba, Litmus, and Chaos Mesh stack up against each other as chaos engineering tools for Kubernetes workloads? In this article, you will compare strengths and weaknesses.
- [blog.palark.com: Attaining harmony of chaos in Kubernetes with Chaos Mesh](https://blog.palark.com/chaos-mesh-in-kubernetes/) This article discusses chaos engineering solutions for Kubernetes using the Chaos Mesh operator. It covers tests on:
    - Failing nodes
    - Failing infrastructure dependencies
    - Network problems

- [awstip.com: Kubernetes Chaos Monkey: A Scheduled Random Pod Deletion Python Script for Testing Cluster Resilience](https://awstip.com/kubernetes-chaos-monkey-a-scheduled-random-pod-deletion-python-script-for-testing-cluster-6eac429554b2)
- [medium.com/@alex.ivenin: Chaos engineering in kubernetes](https://medium.com/@alex.ivenin/chaos-engineering-in-kubernetes-4de425132ba1)

## Chaos Engineering for serverless computing

- [thenewstack.io: Breaking Serverless on Purpose with Chaos Engineering](https://thenewstack.io/breaking-serverless-on-purpose-with-chaos-engineering/)

## Other Chaos Engineering Tools

- [chaosblade](https://github.com/chaosblade-io/chaosblade) An easy to use and powerful chaos engineering experiment toolkit. ChaosBlade is an Alibaba open source experimental injection tool that follows the principles of chaos engineering and chaos experimental models to help enterprises improve the fault tolerance of distributed systems and ensure business continuity during the process of enterprises going to cloud or moving to cloud native systems.
- [Azure Chaos Studio](https://azure.microsoft.com/services/chaos-studio/#overview)
    - [techcommunity.microsoft.com: Announcing the Public Preview of Azure Chaos Studio](https://techcommunity.microsoft.com/t5/azure-governance-and-management/announcing-the-public-preview-of-azure-chaos-studio/ba-p/2893050)
    - [docs.microsoft.com: What is Azure Chaos Studio?](https://docs.microsoft.com/en-us/azure/chaos-studio/chaos-studio-overview)
    - [sqlservercentral.com: Chaos Engineering in Azure](https://www.sqlservercentral.com/articles/chaos-engineering-in-azure)
- [aws.amazon.com: Automating and Scaling Chaos Engineering using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/industries/automating-and-scaling-chaos-engineering-using-aws-fault-injection-simulator/)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/GmErjHyHcUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/B8DfYnDh2F4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>