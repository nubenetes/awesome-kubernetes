# Chaos Engineering
- [Introduction](#introduction)
- [Chaos Engineering for kubernetes/Openshift](#chaos-engineering-for-kubernetesopenshift)
- [Chaos Engineering for serverless computing](#chaos-engineering-for-serverless-computing)
- [Other Chaos Engineering Tools](#other-chaos-engineering-tools)

## Introduction
- [thenewstack.io: Chaos Engineering Is Not Just for Ops](https://thenewstack.io/chaos-engineering-is-not-just-for-ops/)
- [==dzone: How to Pinpoint and Fix Distributed Problems Across Microservices==](https://dzone.com/articles/how-to-pinpoint-and-fix-distributed-problems-acros) While logical separation of APIs fosters parallel development of independent functions, complexity and interdependency becomes harder to manage.
## Chaos Engineering for kubernetes/Openshift
* [reddit: Help with Kube Monkey setup](https://www.reddit.com/r/openshift/comments/e1j5qzrbac_for_container_access_to_destroy_other/)
* [GitHub: kube-monkey](https://github.com/asobti/kube-monkey)
* [GitHub: monkey-ops, Openshift compliant, no cluster-admin required](https://github.comjoshmsmith/monkey-ops)
* [chaoskube periodically kills random pods in your Kubernetes cluster](https://github.com/linkichaoskube)
* [Chaos Mesh](https://github.com/pingcap/chaos-mesh)
* [Litmus Chaos is a toolset to do chaos engineering in a kubernetes native way. Litmus provides chaos CRDs for Cloud-Native developers and SREs to inject, orchestrate and monitor chaos to find weaknesses in Kubernetes deployments](https://github.com/litmuschaos/litmus)
    * [cloud.redhat.com: Chaos Engineering With LitmusChaos](https://cloud.redhat.com/blog/chaos-engineering-with-litmuschaos)
* [thenewstack.io: Using Chaos Engineering to Improve the Resilience of Stateful Applications on Kubernetes](https://thenewstack.io/using-chaos-engineering-to-improve-the-resilience-of-stateful-applications-on-kubernetes/)
* [infoq.com: Chaos Engineering on Kubernetes : Chaos Mesh Generally Available with v1.0](https://www.infoq.com/news/2020/10/kubernetes-chaos-mesh-ga/)
* [chaos-mesh.org: Chaos Mesh 1.0: Chaos Engineering on Kubernetes Made Easier](https://chaos-mesh.org/blog/chaos-mesh-1.0-chaos-engineering-on-kubernetes-made-easier/)
* [thenewstack.io: Develop a Daily Reporting System for Chaos Mesh to Improve System Resilience](https://thenewstack.io/develop-a-daily-reporting-system-for-chaos-mesh-to-improve-system-resilience/)
* [pingcap.com: chaos-mesh-action: Integrate Chaos Engineering into Your CI](https://pingcap.com/blog/chaos-mesh-action-integrate-chaos-engineering-into-your-ci)
* [openshift.com: Introduction to Kraken, a Chaos Tool for OpenShift/Kubernetes](https://www.openshift.com/blog/introduction-to-kraken-a-chaos-tool-for-openshift/kubernetes)
* [thenewstack.io: Chaos Engineering Progressively Moves to Production](https://thenewstack.io/chaos-engineering-progressively-moves-to-production/)
* [blog.flant.com: Open Source solutions for chaos engineering in Kubernetes](https://blog.flant.com/chaos-engineering-in-kubernetes-open-source-tools/)
    - kube-monkey
    - chaoskube
    - Chaos Mesh
    - Litmus Chaos
    - Chaos Toolkit
    - KubeInvaders
* [PowerfulSeal](https://github.com/powerfulseal/powerfulseal) injects failure into your Kubernetes clusters, so that you can detect problems as early as possible. It allows for writing scenarios describing complete chaos experiments.
* [devopscurry.com: How Chaos Engineering plays a vital role in devops success](https://devopscurry.com/how-chaos-engineering-plays-a-vital-role-in-devops-success)
* [BuggyApp: Simulate performance problems](https://buggyapp.ycrash.io/) BuggyApp can simulate various performance problems like Memory Leak, OutOfMemoryError, CPU spike, thread leak StackOverflowError, deadlock, unresponsiveness and so on. [youtube: BuggyApp Demo](https://www.youtube.com/watch?v=exsv-RUrUFY&t=2s&ab_channel=yCrash)
* [medium.com: Getting Started with Chaos Engineering](https://1829034.medium.com/getting-started-with-chaos-engineering-13e85a438d37)
* [Chaos Mesh 🌟](https://chaos-mesh.org/) A Powerful Chaos Engineering Platform for Kubernetes - [github ref](https://github.com/chaos-mesh/chaos-mesh)
* [opensource.com: 5 lessons I learned about chaos engineering for Kubernetes](https://opensource.com/article/21/10/chaos-engineering-kubernetes-ebook)
* [thenewstack.io: Chaos Engineering Made Simple](https://thenewstack.io/chaos-engineering-made-simple/)
* [thenewstack.io: Use Chaos Engineering to Strengthen Your Incident Response](https://thenewstack.io/use-chaos-engineering-to-strengthen-your-incident-response/)
* [thenewstack.io: Operationalizing Chaos Engineering with GitOps](https://thenewstack.io/operationalizing-chaos-engineering-with-gitops/)

## Chaos Engineering for serverless computing
* [thenewstack.io: Breaking Serverless on Purpose with Chaos Engineering](https://thenewstack.io/breaking-serverless-on-purpose-with-chaos-engineering/)

## Other Chaos Engineering Tools
- [chaosblade](https://github.com/chaosblade-io/chaosblade) An easy to use and powerful chaos engineering experiment toolkit. ChaosBlade is an Alibaba open source experimental injection tool that follows the principles of chaos engineering and chaos experimental models to help enterprises improve the fault tolerance of distributed systems and ensure business continuity during the process of enterprises going to cloud or moving to cloud native systems.
- [Azure Chaos Studio](https://azure.microsoft.com/services/chaos-studio/#overview)
    - [techcommunity.microsoft.com: Announcing the Public Preview of Azure Chaos Studio](https://techcommunity.microsoft.com/t5/azure-governance-and-management/announcing-the-public-preview-of-azure-chaos-studio/ba-p/2893050)