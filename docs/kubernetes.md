# Kubernetes

{=="Kubernetes is not for application development but for platform development. Its magic is in enterprise standardization, not app portability" (Kelsey Hightower)==}

- [Introduction](#introduction)
    - [Kubernetes Jobs Market](#kubernetes-jobs-market)
    - [Certified Kubernetes Offerings](#certified-kubernetes-offerings)
    - [The State of Cloud-Native Development](#the-state-of-cloud-native-development)
    - [Kubernetes Failure Stories](#kubernetes-failure-stories)
    - [Kubernetes Maturity Model](#kubernetes-maturity-model)
    - [Cloud Native Learn by doing platforms](#cloud-native-learn-by-doing-platforms)
    - [Kubernetes Installation Methods](#kubernetes-installation-methods)
    - [Kubernetes Knowledge Hubs](#kubernetes-knowledge-hubs)
        - [Kubernetes Podcasts](#kubernetes-podcasts)
        - [Kubernetes Blogs](#kubernetes-blogs)
        - [Spanish Kubernetes Blogs](#spanish-kubernetes-blogs)
- [Kubernetes Open Source Container Orchestation](#kubernetes-open-source-container-orchestation)
    - [kubeconfig](#kubeconfig)
    - [Docker and Kubernetes](#docker-and-kubernetes)
        - [Kubernetes vs Docker](#kubernetes-vs-docker)
        - [Kubernetes vs Docker Swarm](#kubernetes-vs-docker-swarm)
    - [Kubernetes Admission Controllers](#kubernetes-admission-controllers)
    - [Kubernetes Mutating Webhooks](#kubernetes-mutating-webhooks)
    - [Kubernetes Cloud Controller Manager](#kubernetes-cloud-controller-manager)
    - [Kubernetes Resources](#kubernetes-resources)
        - [Kubernetes Pods](#kubernetes-pods)
        - [Kubernetes ConfigMaps](#kubernetes-configmaps)
        - [Kubernetes Secrets](#kubernetes-secrets)
        - [Kubernetes Volumes](#kubernetes-volumes)
        - [Kubernetes Namespaces and Multi Tenancy. Self Service Namespaces](#kubernetes-namespaces-and-multi-tenancy-self-service-namespaces)
            - [Creating Users](#creating-users)
        - [Kubernetes Labels and Selectors](#kubernetes-labels-and-selectors)
        - [Kubernetes Taints and Tolerations](#kubernetes-taints-and-tolerations)
        - [Kubernetes Deployment, Rollling Updates and Rollbacks](#kubernetes-deployment-rollling-updates-and-rollbacks)
        - [Kubernetes StatefulSet](#kubernetes-statefulset)
        - [Kubernetes Jobs and Cron Jobs](#kubernetes-jobs-and-cron-jobs)
    - [Kubernetes Deployment Strategies](#kubernetes-deployment-strategies)
    - [Kubernetes API](#kubernetes-api)
        - [Multi-Cluster Services API](#multi-cluster-services-api)
    - [Kubernetes Health Checks/Probes. Startup, Liveness, Readiness](#kubernetes-health-checksprobes-startup-liveness-readiness)
    - [Kubernetes Limits and Requests](#kubernetes-limits-and-requests)
    - [Kube Scheduler](#kube-scheduler)
    - [Kubernetes etcd](#kubernetes-etcd)
    - [Kubernetes Sidecars](#kubernetes-sidecars)
    - [Kubernetes Annotations](#kubernetes-annotations)
    - [Kubernetes Best Practices and Tips](#kubernetes-best-practices-and-tips)
    - [Disruptions](#disruptions)
    - [Cost Estimation Strategies](#cost-estimation-strategies)
        - [kubecost](#kubecost)
    - [Kubernetes Resource and Capacity Management. Capacity Planning](#kubernetes-resource-and-capacity-management-capacity-planning)
    - [Architecting Kubernetes clusters. Node Size. Multi Clusters and Hybrid Cloud](#architecting-kubernetes-clusters-node-size-multi-clusters-and-hybrid-cloud)
        - [Wide Cluster instead of Multi-Cluster](#wide-cluster-instead-of-multi-cluster)
- [Client Libraries for Kubernetes](#client-libraries-for-kubernetes)
- [Helm Kubernetes Tool](#helm-kubernetes-tool)
- [Templating YAML in Kubernetes with real code. YQ YAML processor](#templating-yaml-in-kubernetes-with-real-code-yq-yaml-processor)
- [Extending Kubernetes](#extending-kubernetes)
    - [Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API](#adding-custom-resources-extending-kubernetes-api-with-kubernetes-resource-definitions-crd-vs-aggregated-api)
    - [Krew, a plugin manager for kubectl plugins](#krew-a-plugin-manager-for-kubectl-plugins)
    - [OpenKruise/Kruise](#openkruisekruise)
    - [Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions](#crossplane-a-universal-control-plane-api-for-cloud-computing-crossplane-workloads-definitions)
- [Kubernetes Community](#kubernetes-community)
    - [Community Forums](#community-forums)
    - [Kubernetes Special Interest Groups (SIGs)](#kubernetes-special-interest-groups-sigs)
        - [Kubernetes SIG's Repos](#kubernetes-sigs-repos)
        - [Kubectl Plugins](#kubectl-plugins)
- [Enforcing Policies and governance for kubernetes workloads with Conftest](#enforcing-policies-and-governance-for-kubernetes-workloads-with-conftest)
- [Kubernetes Troubleshooting](#kubernetes-troubleshooting)
    - [Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes](#provisioning-cloud-resources-aws-gcp-azure-in-kubernetes)
    - [Debugging Techniques and Strategies. Debugging with ephemeral containers](#debugging-techniques-and-strategies-debugging-with-ephemeral-containers)
- [Kubernetes Tutorials](#kubernetes-tutorials)
    - [Online Training](#online-training)
    - [K8s Diagrams](#k8s-diagrams)
- [Kubernetes Patterns and Antipatterns. Service Discovery](#kubernetes-patterns-and-antipatterns-service-discovery)
- [Kubernetes Scheduling and Scheduling Profiles](#kubernetes-scheduling-and-scheduling-profiles)
    - [Assigning Pods to Nodes. Pod Affinity and Anti-Affinity](#assigning-pods-to-nodes-pod-affinity-and-anti-affinity)
    - [Pod Topology Spread Constraints and PodTopologySpread Scheduling Plugin](#pod-topology-spread-constraints-and-podtopologyspread-scheduling-plugin)
- [Cloud Development Kit (CDK) for Kubernetes](#cloud-development-kit-cdk-for-kubernetes)
    - [AWS Cloud Development Kit (AWS CDK)](#aws-cloud-development-kit-aws-cdk)
- [Serverless with OpenFaas and Knative](#serverless-with-openfaas-and-knative)
- [Multi-Cluster Federation. Hybrid Cloud Setup Tools](#multi-cluster-federation-hybrid-cloud-setup-tools)
    - [KubeFed](#kubefed)
    - [KubeCarrier](#kubecarrier)
    - [Red Hat Operator Lifecycle Manager (OLM)](#red-hat-operator-lifecycle-manager-olm)
    - [Istio Service Mesh](#istio-service-mesh)
- [Multi-Regional Architecture](#multi-regional-architecture)
- [Kubernetes Scripts](#kubernetes-scripts)
    - [Kubernetes and Ansible](#kubernetes-and-ansible)
- [Spot instances in Kubernetes](#spot-instances-in-kubernetes)
- [Kubernetes on Windows](#kubernetes-on-windows)
- [Kubernetes Incident Report Plan IRP](#kubernetes-incident-report-plan-irp)
- [Kubernetes interview questions](#kubernetes-interview-questions)
- [Kubernetes Certifications. CKA, CKAD and CKS](#kubernetes-certifications-cka-ckad-and-cks)
- [Books and eBooks](#books-and-ebooks)
    - [Kubernetes Patterns eBooks](#kubernetes-patterns-ebooks)
    - [Famous Kubernetes ebooks of 2019](#famous-kubernetes-ebooks-of-2019)
- [Famous Kubernetes resources of 2019](#famous-kubernetes-resources-of-2019)
- [Famous Kubernetes resources of 2020](#famous-kubernetes-resources-of-2020)
- [Kubernetes Slack Channel](#kubernetes-slack-channel)
- [Slides](#slides)
- [Bunch of images](#bunch-of-images)
- [Videos](#videos)
- [Spanish Videos](#spanish-videos)
- [Tweets](#tweets)

## Introduction
* [Wikipedia.org: Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [cloud.google.com: What is Kubernetes? 🌟](https://cloud.google.com/learn/what-is-kubernetes)
* [Kubernetes Glossary 🌟](https://www.bluematador.com/learn/kubernetes-glossary)
* [=="Kubernetes magic is in enterprise standardization, not app portability"== (Kelsey Hightower) 🌟](https://www.techrepublic.com/article/kubernetes-magic-is-in-enterprise-standardization-not-app-portability/)
* [twitter.com/kubernetesio](https://twitter.com/kubernetesio)
* [techbeacon.com: 25 Kubernetes experts you should follow on Twitter](https://techbeacon.com/enterprise-it/25-kubernetes-experts-you-should-follow-twitter)
* [enterprisersproject.com: Kubernetes: Everything you need to know (2020) 🌟](https://enterprisersproject.com/article/2020/4/kubernetes-everything-you-need-know)
* [padok.fr: Kubernetes’ Architecture: Understanding the components and structure of clusters 🌟](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)
* [opensource.com: Explaining Kubernetes in 10 minutes using an analogy](https://opensource.com/article/20/7/kubernetes-analogy)
* [medium: A Practical Step-by-Step Guide to Understanding Kubernetes](https://medium.com/better-programming/a-practical-step-by-step-guide-to-understanding-kubernetes-d8be7f82e533) Deploy a distributed application and understand key underlying concepts.
* [medium: Kubernetes, a practical introduction](https://medium.com/nexton/kubernetes-a-practical-introduction-18a5b69e7763)
* [itnext.io: Kubernetes is Hard! 🌟](https://itnext.io/kubernetes-is-hard-190f1d0c6d36) But, where there’s Kubernetes, there’s a way!
* [medium: Starting with kubernetes](https://medium.com/@thomaspoignant/starting-with-kubernetes-db121b09fd4)
* [thenewstack.io: Kubernetes Is the New Standard for Computing, Including the Edge](https://thenewstack.io/kubernetes-is-the-new-standard-for-computing-including-the-edge/)
* [thenewstack.io: How does kubernetes work?](https://thenewstack.io/how-does-kubernetes-work/)
* [cloudsavvyit.com: How Does Kubernetes Work?](https://www.cloudsavvyit.com/10110/how-does-kubernetes-work/)
* [elmanytas.es: Kubernetes para impostores III](http://elmanytas.es/?q=node/358)
* [enterprisersproject.com: How to explain Kubernetes in plain English](https://enterprisersproject.com/article/2017/10/how-explain-kubernetes-plain-english) How do you explain Kubernetes and orchestration to non-technical people? Listen to the experts
* [maximilianmichels.com: Kubernetes in a Nutshell: 10 Things You Need to Know](https://maximilianmichels.com/2021/kubernetes-what-you-need-to-know/)
* [brennerm.github.io: Kubernetes Overview Diagrams 🌟](https://brennerm.github.io/posts/kubernetes-overview-diagrams.html#architecture)
* [thenewstack.io: Kubernetes Lifecycle Management! So Important! (Day 0, Day 1, Day 2) 🌟](https://thenewstack.io/kubernetes-lifecycle-management-so-important-what-does-it-mean)
* [lemoncode.net: Hola Kubernetes: Definiciones 🌟](https://lemoncode.net/lemoncode-blog/2021/3/17/hola-kubernetes-definiciones)
* [opensource.com: A beginner's guide to Kubernetes container orchestration](https://opensource.com/article/20/6/container-orchestration) Understanding the building blocks of container orchestration makes it easier to get started with Kubernetes.  
* [luminousmen.com: Kubernetes 101](https://luminousmen.com/post/kubernetes-101)
* [css-tricks.com: Kubernetes Explained Simply: Containers, Pods and Images](https://css-tricks.com/kubernetes-explained-simply-containers-pods-and-images/)
* [auth0.com: Kubernetes Tutorial - Step by Step Introduction to Basic Concepts](https://auth0.com/blog/kubernetes-tutorial-step-by-step-introduction-to-basic-concepts/) Learn about the basic Kubernetes concepts while deploying a sample application on a real cluster.
* [thenewstack.io: Why developers should learn kubernetes](https://thenewstack.io/why-developers-should-learn-kubernetes/)
* [thenewstack.io: This Week in Programming: Kubernetes from Day One? 🌟](https://thenewstack.io/this-week-in-programming-kubernetes-from-day-one/)
* [==nextplatform.com: KUBERNETES EXPANDS FROM CONTAINERS TO INFRASTRUCTURE MANAGEMENT== 🌟](https://www.nextplatform.com/2021/08/02/kubernetes-expands-from-containers-to-infrastructure-management) **More and more in the middleware layer, not in the hardware**
* [thenewstack.io: Monolithic Development Practices Kill Powerful Kubernetes Benefits 🌟🌟](https://thenewstack.io/monolithic-development-practices-kill-powerful-kubernetes-benefits/) **"It’s not about the economy of data, it’s about speed and nimbleness of data. The benefits of using Kubernetes and microservices is incredible — just make sure you know how to fully wield its power!"**
* [dev.to: Getting Started Tutorial for Learning Kubernetes 🌟](https://dev.to/chefgs/getting-started-tutorial-for-learning-kubernetes-455e)
* [tech.showmax.com: Developers' basic guide to kubernetes](https://tech.showmax.com/2021/08/developers-101-kubernetes/)
* [dev.to: How to start with Kubernetes for begginer](https://dev.to/dhirajpatra/how-to-start-with-kubernetes-for-begginer-309e)
* [opensource.com: How the Kubernetes scheduler works](https://opensource.com/article/20/11/kubernetes-scheduler) Understand how the Kubernetes scheduler discovers new pods and assigns them to nodes.
* [medium.com: The Kubernetes Scheduler: this series aims to advance the understanding of Kubernetes and its underlying concepts](https://medium.com/@dominik.tornow/the-kubernetes-scheduler-cd429abac02f)
* [blogs.mulesoft.com - K8s: 8 questions about Kubernetes](https://blogs.mulesoft.com/dev/resources-dev/k8s-kubernetes/)
* [devcentral.f5.com: What is Kubernetes?](https://devcentral.f5.com/s/articles/What-is-Kubernetes)
* [docs.google.com: Kubernetes For Everyone 🌟🌟](https://docs.google.com/document/d/1p4ZYQYM2VrMCR8K3T68JOMzWHlV-C8Jogrl9Ces77OA)  A consolidated document on Kubernetes by: Pavan Belagatti
* [hackernoon.com: The Ultimate Beginners Guide To Kubernetes and Container Orchestration](https://hackernoon.com/the-ultimate-beginners-guide-to-kubernetes-and-container-orchestration-5d83354y)
* [k21academy.com: Kubernetes Architecture. An Introduction to Kubernetes Components](https://k21academy.com/docker-kubernetes/kubernetes-architecture-components-overview-for-beginners/)
* [dzone: Introduction To Kubernetes 🌟](https://dzone.com/articles/introduction-to-kubernetes-part-1) An orchestration tool takes care of provisioning and deployment, allocation of resources, load balancing, and many other important aspects of any system.
* [weave.works: Kubernetes components that make up its architecture 🌟](https://www.weave.works/blog/kubernetes-components-that-makeup-its-architecture) Great intro
* [dzone refcard: Advanced kubernetes 🌟](https://dzone.com/refcardz/advanced-kubernetes)
* [loginradius.com: Understanding Basics of Kubernetes](https://www.loginradius.com/engineering/blog/understanding-kubernetes/)
* [redhat.com: Kubernetes basics for sysadmins](https://www.redhat.com/sysadmin/kubernetes-basics-sysadmins) Learn when Kubernetes can be effectively used and how the containers it manages might be better than virtual machines.
* [redhat.com: Kubernetes Components - A sysadmin's guide to basic Kubernetes components 🌟](https://www.redhat.com/sysadmin/kubernetes-components) Kubernetes control plane nodes and worker nodes, their features, and how they interact.
* [learnsteps.com: How Kubernetes works on reconciler pattern 🌟](https://www.learnsteps.com/how-kubernetes-works-on-a-reconciler-pattern/)
* [devopsunlocked.com: Kubernetes: Learning Material](https://devopsunlocked.com/kubernetes-learning-material/)
* [cncf.io: Kubernetes 101: An Introduction 🌟](https://www.cncf.io/blog/2020/12/14/kubernetes-101-an-introduction/)
* [millionvisit.blogspot.com: Kubernetes for Developers #1: Kubernetes Architecture and Features 🌟](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-1-kubernetes-architecture.html)
* [redhat.com: Start learning Kubernetes from your local machine](https://www.redhat.com/sysadmin/start-learning-kubernetes)
* [medium: Pratyush Mathur - Kubernetes Architecture](https://medium.com/@pratyush.mathur/kubernetes-architecture-82e9bc8324f1)
* [medium: Kubernetes Fundamentals For Absolute Beginners: Architecture & Components](https://medium.com/the-programmer/kubernetes-fundamentals-for-absolute-beginners-architecture-components-1f7cda8ea536)
* [learnsteps.com: What is a control plane? Basics on Kubernetes](https://www.learnsteps.com/what-is-a-control-plane-what-do-people-mean-by-this-basics-on-kubernetes/)
* [infoworld.com: No one wants to manage Kubernetes anymore 🌟](https://www.infoworld.com/article/3614850/no-one-wants-to-manage-kubernetes-anymore.html) **The availability of solid and varied managed kubernetes options has seen more and more companies shy away from managing their own clusters.** 
* [eximiaco.tech: when to choose Kubernetes? 🌟](https://www.eximiaco.tech/en/2020/06/03/3-facts-to-consider-before-adopting-kubernetes/)
* [thenewstack.io: Living with Kubernetes: Cluster Upgrades 🌟](https://thenewstack.io/living-with-kubernetes-cluster-upgrades/)
* [thenewstack.io: 5 Things Developers Need to Know About Kubernetes Management](https://thenewstack.io/5-things-developers-need-to-know-about-kubernetes-management/)
* [How to handle environment variables with Kubernetes? 🌟](https://humanitec.com/blog/handling-environment-variables-with-kubernetes)
* [weave.works: The Definitive Guide to Kubernetes in Production 🌟🌟](https://www.weave.works/blog/the-definitive-guide-to-kubernetes-in-production)
* [vmblog.com: The Rise of Modern Day Kubernetes Operations](https://vmblog.com/archive/2021/10/07/the-rise-of-modern-day-kubernetes-operations.aspx)
* [elastisys.com: Evaluation of Caching Methodologies for Microservice-Based Architectures in Kubernetes](https://elastisys.com/evaluation-of-caching-methodologies/)
* [thenewstack.io: What Workloads Do Businesses Run on Kubernetes?](https://thenewstack.io/what-workloads-do-businesses-run-on-kubernetes/)
* [dzone: Getting Started With Kubernetes In 2 Days](https://dzone.com/articles/getting-started-with-kubernetes-in-2-days) Check out these tools to help you deploy and manage your K8s clusters from the ground up...
* [itnext.io: The subtleties of ensuring zero downtime during pod lifecycle events in Kubernetes](https://itnext.io/the-subtleties-of-ensuring-zero-downtime-during-pod-lifecycle-events-in-kubernetes-6461c12f7736)
* [tutorialworks.com: The differences between Docker, containerd, CRI-O and runc](https://www.tutorialworks.com/difference-docker-containerd-runc-crio-oci/) Since Docker kicked off this explosion in containers, there’s been a growing family of tools and standards to help govern how to use this technology.
* [searchitoperations.techtarget.com: Ensure Kubernetes high availability with master node planning](https://searchitoperations.techtarget.com/tip/Ensure-Kubernetes-high-availability-with-master-node-planning) Kubernetes ensures high availability in its worker nodes, but for a mission-critical workload, IT teams should take these extra steps for redundancy in the master node components.
* [thenewstack.io: The New Stack’s Top Kubernetes Stories of 2021](https://thenewstack.io/the-new-stacks-top-kubernetes-stories-of-2021/)
* [ostechnix.com: Kubernetes Features Explained In Detail](https://ostechnix.com/kubernetes-features/)
* [==kodekloud.com: Kubernetes Features Every Beginner Must Know==](https://kodekloud.com/kubernetes-features-every-beginner-must-know/)
* [learnsteps.com: Kubernetes: What to learn from a long term perspective](https://www.learnsteps.com/kubernetes-what-to-learn-from-a-long-term-perspective/) 
* [==joshgav.github.io: Kubernetes isn't about containers==](https://joshgav.github.io/2021/12/16/kubernetes-isnt-about-containers.html) **Kubernetes offers a standard interface for managing software-defined infrastructure - cloud, in other words. Kubernetes is a standard API framework for cloud services.**
* [medium: Do I need to learn Kubernetes?](https://medium.com/devops-dudes/do-i-need-to-learn-kubernetes-a3dd9a7f9e9b)
* [medium.com/@david.alvares.62: Kubernetes Control Plane for newbies](https://medium.com/@david.alvares.62/kubernetes-control-plane-for-newbies-75d77f5c8456) Kubernetes has a reputation for being a very complex system, difficult to master in terms of administration and security. Today I suggest you better understand an essential component of Kubernetes: the control plane.
* [divya-mohan0209.medium.com: Getting started with K8s in 2022](https://divya-mohan0209.medium.com/getting-started-with-k8s-in-2022-1dfeb4bdc112) And a list of resources structured to help you learn!
* [==docs.google.com: Kubernetes For Everyone==](https://docs.google.com/document/d/1p4ZYQYM2VrMCR8K3T68JOMzWHlV-C8Jogrl9Ces77OA/edit)
* [medium.com/paypal-tech: Scaling Kubernetes to Over 4k Nodes and 200k Pods](https://medium.com/paypal-tech/scaling-kubernetes-to-over-4k-nodes-and-200k-pods-29988fad6ed)

### Kubernetes Jobs Market
* [kube.careers: Kubernetes jobs market (Q2 2021)](https://kube.careers/report-2021-q2) We analyzed all the 113 Kubernetes jobs posted in the past 3 months (Apr-May-Jun 2021) and extracted metrics for:
    - Kubernetes salary ranges
    - Remote vs office offers
    - Popular cloud providers
- [==kube.careers: Kubernetes jobs market trends for 2021 (Q4)==](https://kube.careers/report-2021-q4) What's the average salary for a Kubernetes engineer? Do you need a Kubernetes certification to apply for a job? What technologies and cloud providers are often used with Kubernetes? We analyzed 276 Kubernetes jobs from 2021 and found that:
    - If you know AWS and Python, the world is your oyster.
    - CKA is the top Kubernetes certification. But only a few employers require one.
    - Jenkins is more alive than ever.
    - Prometheus is synonymous with monitoring. No one comes close.
    - Terraform and Ansible lead IaC.

### Certified Kubernetes Offerings
* [Certified Kubernetes offerings](https://www.cncf.io/certification/software-conformance/)

### The State of Cloud-Native Development
* [Cloud-Native Development Survey Details Kubernetes, Serverless Data](https://virtualizationreview.com/articles/2020/05/08/cloud-native-dev-survey.aspx) Detailed data on the use of Kubernetes, serverless computing and more.

### Kubernetes Failure Stories
- [k8s.af 🌟](https://k8s.af/)
- [thenewstack.io: Kubernetes Horror Stories](https://thenewstack.io/kubernetes-horror-stories/)
- [techbeacon.com: Why teams fail with Kubernetes—and what to do about it](https://techbeacon.com/enterprise-it/why-teams-fail-kubernetes-what-do-about-it)
- [kodekloud.com: Kubernetes Features Every Beginner Must Know](https://kodekloud.com/blog/200628/kubernetes-features-every-beginner-must-know)

### Kubernetes Maturity Model
- [fairwinds.medium.com: Kubernetes Maturity Model](https://www.fairwinds.com/kubernetes-maturity-model)
- [fairwinds.medium.com: An Introduction to the Kubernetes Maturity Model — How to Use It](https://fairwinds.medium.com/an-introduction-to-the-kubernetes-maturity-model-how-to-use-it-54ebfc21e413)
    - The Fairwinds team developed the Kubernetes Maturity Model over a year ago, and they continue to update and refine it to reflect the five stages you go through in your journey to Kubernetes maturity. 
    - If the Kubernetes Maturity Model is new to you, this is a helpful introduction and guide on how to use it.
    - Before you do anything, consider what a cloud-native journey means to you and your organization. Kubernetes isn’t right for everyone, so make sure you understand where to start and how to prove value by embracing Kubernetes.
    - Any maturity model is a process, and you’re likely to move back and forth between phases, and some will take longer than others. Even once you’ve reached phase five, you’ll always be working on ongoing optimization, removing human error and effort, and improving reliability and efficiency.

### Cloud Native Learn by doing platforms
- [openshift sandbox](https://developers.redhat.com/developer-sandbox/get-started)
- [Kubebyexample.com - kubernetesbyexample.com 🌟🌟](https://kubebyexample.com) A free learning platform covering the fundamentals of how to develop, deploy, manage, and automate containers in cloud-native environments. 
- https://killer.sh CKS CKA CKAD Simulator
- https://acloudguru.com
- https://cloudacademy.com
- https://cloudyuga.guru
- https://instruqt.com
- https://katacoda.com
- https://kodekloud.com
- https://learning.oreilly.com
- https://play-with-docker.com
- https://play-with-k8s.com

### Kubernetes Installation Methods
- [itnext.io: Kubernetes Installation Methods The Complete Guide](https://itnext.io/kubernetes-installation-methods-the-complete-guide-1036c860a2b3)

{==

### Kubernetes Knowledge Hubs
- [kubernetes.io](https://kubernetes.io/)
- [reddit.com/r/kubernetes](https://www.reddit.com/r/kubernetes) 
- [Kubernetes README: kubernetesreadme.com](https://kubernetesreadme.com/) What to Read to Learn More About Kubernetes
- [dev-k8sref-io.web.app](https://dev-k8sref-io.web.app/) Kubernetes Reference - [k8sref.io](https://www.k8sref.io/)
- [learnk8s.io: Kubernetes Research. Research documents on node instance types, managed services, ingress controllers, CNIs, etc.](https://learnk8s.io/research) A research hub to collect all knowledge around Kubernetes. Those are in-depth reports and comparisons designed to drive your decisions. Should you use GKE, AKS, EKS? How many nodes? What instance type?
- [jamiehannaford/what-happens-when-k8s](https://github.com/jamiehannaford/what-happens-when-k8s) 🤔 What happens when I type kubectl run?

#### Kubernetes Podcasts
- [kubernetespodcast.com](https://kubernetespodcast.com/)
- [==weave.works: Podcast: Kubernetes has won the enterprise==](https://www.weave.works/blog/kubernetes-in-the-enterprise)

#### Kubernetes Blogs
- [nativecloud.dev](https://nativecloud.dev)
- [learnk8s.io/blog](https://learnk8s.io/blog)
- [kubermatic.com](https://www.kubermatic.com/categories/kubernetes/)
- [containerjournal.com](https://containerjournal.com)
- [cloudowski.com](https://cloudowski.com/)
- [dev.to/t/kubernetes](https://dev.to/t/kubernetes)
- [kubernetes-on-aws.readthedocs.io](https://kubernetes-on-aws.readthedocs.io/)
- [opensource.com/tags/kubernetes](https://opensource.com/tags/kubernetes)
- [itnext.io/tagged/kubernetes](https://itnext.io/tagged/kubernetes)
- [thenewstack.io/category/kubernetes](https://thenewstack.io/category/kubernetes)
- [k21academy.com/category/docker-kubernetes](https://k21academy.com/category/docker-kubernetes)
- [weave.works/blog/category/kubernetes](https://www.weave.works/blog/category/kubernetes)
- [learnsteps.com/tag/basics-on-kubernetes](https://www.learnsteps.com/tag/basics-on-kubernetes)
- [devopscube.com](https://devopscube.com)
- [rcarrata.com](https://rcarrata.com)

#### Spanish Kubernetes Blogs 
- [returngis.net](https://www.returngis.net/)

==}

## Kubernetes Open Source Container Orchestation
* [kubedex.com](https://kubedex.com/) Discover, Compare and Share Kubernetes Applications
* [medium.com: A Year Of Running Kubernetes at MYOB, And The Importance Of Empathy](https://medium.com/@jpcontad/a-year-of-running-kubernetes-as-a-product-7eed1204eecd)
* [labs.mwrinfosecurity.com: Attacking Kubernetes through Kubelet](https://labs.mwrinfosecurity.com/blog/attacking-kubernetes-through-kubelet/)
* [itnext.io: Successful & Short Kubernetes Stories For DevOps Architects](https://itnext.io/successful-short-kubernetes-stories-for-devops-architects-677f8bfed803)
* [platform9.com: Kubernetes CI/CD Pipelines at Scale](https://platform9.com/blog/kubernetes-ci-cd-pipelines-at-scale/)
* [4 trends for Kubernetes cloud-native teams to watch in 2020](https://searchapparchitecture.techtarget.com/tip/4-trends-for-Kubernetes-cloud-native-teams-to-watch-in-2020)
* [5 open source projects that make Kubernetes even better: Prometheus, Operator framework, Knative, Tekton, Kubeflow 🌟](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve) Open source projects bring many additional capabilities to Kubernetes, such as performance monitoring, developer tools, serverless capabilities, and CI/CD workflows. Check out these five widely used options
* [4 trends for Kubernetes cloud-native teams to watch in 2020 ](https://searchapparchitecture.techtarget.com/tip/4-trends-for-Kubernetes-cloud-native-teams-to-watch-in-2020) Today's software architectural landscape seems to change like the weather. Stay ahead of the curve with these cloud-related trends, including GitOps and service meshes.
* [Creating a Kubernetes cloud provider, doesn't required boiling the ocean ](https://thebsdbox.co.uk/2020/03/18/Creating-a-Kubernetes-cloud-doesn-t-required-boiling-the-ocean/)
* [opensource.com: 5 ways to boost your Kubernetes knowledge](https://opensource.com/article/20/6/kubernetes-anniversary)
* [blog.container-solutions.com: 7 Cloud Native Trends to Watch in 2020 ](https://blog.container-solutions.com/7-cloud-native-trends-to-watch-in-2020)
* [snyk.io: Shipping Kubernetes-native applications with confidence](https://snyk.io/blog/shipping-kubernetes-native-applications-with-confidence/)
* [medium: Delivering value on Kubernetes](https://medium.com/@dius_au/delivering-value-on-kubernetes-8d5c5655c1b4)
* [blocksandfiles.com: Kubernetes is in a bit of state about state](https://blocksandfiles.com/2020/07/21/kubernetes-stateful-status/) Kubernetes is “four to five years away” from being a stable distribution capable of running stateful apps, according to Redis Labs chief product officer Alvin Richards.
* [medium: Then he asked me “Is Kubernetes right for us?”](https://medium.com/@alexellisuk/then-he-asked-me-is-kubernetes-right-for-us-78695ee35289)
* [loft.sh: Kubernetes: Virtual Clusters For CI/CD & Testing](https://loft.sh/blog/kubernetes-virtual-clusters-for-ci-cd-testing/)
* [jfrog.com: Kubernetes in Production with Jessica Deen at swampUP 2020](https://jfrog.com/blog/kubernetes-in-production-with-jessica-deen-at-swampup-2020/)
* [lambda.grofers.com: Learnings From Two Years of Kubernetes in Production ](https://lambda.grofers.com/learnings-from-two-years-of-kubernetes-in-production-b0ec21aa2814)
* [medium: 3 Years of Kubernetes in Production–Here’s What We Learned](https://medium.com/better-programming/3-years-of-kubernetes-in-production-heres-what-we-learned-44e77e1749c8)
* [revistacloudcomputing.com: Los mejores proveedores de Kubernetes](https://www.revistacloudcomputing.com/2020/09/los-mejores-proveedores-de-kubernetes/)
* [Virtual Clusters for Kubernetes — Benefits and Use Cases](https://medium.com/better-programming/virtual-clusters-for-kubernetes-benefits-use-cases-a4eee1c5c5a5) Virtual Kubernetes clusters could be the next driver for Kubernetes adoption.
* [Getting a shell on each node](https://gist.github.com/xandout/8d24558c75c53f3cb8bf0a97ec25fcfc) Learn how you can use a **DaemonSet to expose an SSH shell on each node** of your cluster (even if you don't have SSH installed)
* [medium: Virtual Clusters for Kubernetes — Benefits and Use Cases](https://medium.com/better-programming/virtual-clusters-for-kubernetes-benefits-use-cases-a4eee1c5c5a5) Virtual Kubernetes clusters could be the next driver for Kubernetes adoption
* [containerjournal.com: Overcoming Kubernetes Infrastructure Challenges](https://containerjournal.com/topics/container-management/overcoming-kubernetes-infrastructure-challenges/)
* [medium: Installing cf-for-k8s on a Kubernetes Cluster Running on Digital Ocean](https://medium.com/cloud-foundry-foundation/installing-cf-for-k8s-on-a-kubernetes-cluster-running-on-digitalocean-acffdc652dcf) If you want to install Cloud Foundry on Kubernetes on Digital Ocean, you might find this article relevant.
* [itnext.io: Lessons learned from managing a Kubernetes cluster for side projects (GKE) ](https://itnext.io/lessons-learned-from-managing-a-kubernetes-cluster-for-side-projects-780fbbacf36c)
* [projectcalico.org: Using Kubernetes to orchestrate VMs ](https://www.projectcalico.org/using-kubernetes-to-orchestrate-vms/)
* [lastweekinaws.com: Is ECS deprecated? Has Kubernetes won?](https://www.lastweekinaws.com/blog/reader-mailbag-is-ecs-deprecated/)
* [opensource.com: 8 Kubernetes insights for 2021 ](https://opensource.com/article/21/1/kubernetes) Review the top five Kubernetes articles of 2020, then preview three tools you should learn about in 2021.
* [srcco.de: Zalando - Many Kubernetes Clusters instead of 1 huge cluster ](https://srcco.de/posts/many-kubernetes-clusters.html) Running 80+ Kubernetes clusters in production? Yes, Zalando runs 100+ Kubernetes clusters on AWS.
    - Each cluster runs in its own AWS account.
    - They always create a pair of prod/non-prod clusters per "product community", i.e. only half of their clusters (50+) are marked as "production" and have full 24x7 on-call support.
    - They decided to go with "many" (that's relative) clusters for various reasons:
        - Kubernetes has no strong story for multi-tenancy, having "smaller" clusters mitigates part of this problem
        - Some infrastructure is shared per cluster, e.g. Prometheus and the Ingress proxy (Skipper) --- this requires appropriate (vertical) scaling of these components, smaller clusters make this easier to handle
        - The blast radius is limited --- anything going wrong in one cluster (outage, security incident, ..) does not necessarily affect the whole organization
        - Cost attribution is easier (every cluster belongs to a cost center)
        - The cluster (and its AWS account) serves as a natural trust boundary for access control (you can either deploy via CI/CD to a cluster or not)
* [platform9.com: The Gorilla Guide to Kubernetes in the Enterprise ](https://platform9.com/lp/ultimate-guide-enterprise-kubernetes/) Discover key capabilities for Kubernetes at scale. 
    * A complete Enterprise Kubernetes infrastructure needs proper DNS, load balancing, Ingress, stateful services, K8’s role-based access control (RBAC), integration with LDAP and authentication systems, and more. Once Kubernetes is deployed, day-2 operational challenges and life-cycle management comes into play: monitoring, alerting, troubleshooting, upgrades, security patching, compliance checking and much more.
    * The Gorilla guide to Kubernetes in the Enterprise is your resource to ensure the success of your Enterprise Kubernetes projects by thinking through critical decisions around deployment options, day-2 operational considerations, use cases, and choosing your Kubernetes implementation solutions.
* [magalix.com: Influencing Kubernetes Scheduler Decisions](https://www.magalix.com/blog/influencing-kubernetes-scheduler-decisions) To ensure maximum possible performance and availability given the infrastructure at hand, the scheduler uses complex algorithms to ensure the most efficient Pod placement. In this article, we discuss how the scheduler selects the best node to host the Pod and how we can influence its decision.
* [medium: Making Sense of Taints and Tolerations in Kubernetes](https://medium.com/kubernetes-tutorials/making-sense-of-taints-and-tolerations-in-kubernetes-446e75010f4e)
* [devopscube.com: 10 Key Considerations for Kubernetes Cluster Design & Setup 🌟](https://devopscube.com/key-considerations-kubernetes-cluster-design-setup/)
* [blog.pixielabs.ai: Building Kubernetes Native SaaS applications: iterating quickly by deploying in-cluster data planes](https://blog.pixielabs.ai/hybrid-architecture/hybrid-architecture/)
* [itnext.io: CKS Exam Series #9 RBAC v2](https://itnext.io/cks-exam-series-9-rbac-v2-23ee24dd77cd) Kubernetes CKS Example Exam Question Series
* [dzone: Scale to Zero With Kubernetes with KEDA and/or Knative ](https://dzone.com/articles/scale-to-zero-with-kubernetes) This article reviews how Kubernetes provides the platform capabilities for dynamic deployment, scaling, and management in Cloud-native applications.
* [infoq.com: Experts Discuss Top Kubernetes Trends and Production Challenges](https://www.infoq.com/articles/kubernetes-trends-and-challenges/)
* [blog.appstack.one: How to run Ghost blog inside Kubernetes](https://blog.appstack.one/how-to-run-ghost-blog-inside-kubernetes/)
* [learnk8s.io: Scaling Celery workers with RabbitMQ on Kubernetes ](https://learnk8s.io/scaling-celery-rabbitmq-kubernetes) In this article, you will explore how to use Kubernetes and KEDA to scale Celery workers based on the number of messages in a RabbitMQ queue.
    1. Learn how to set up a metrics pipeline
    2. How you can drive autoscaling based on metrics from RabbitMQ.
    3. Why KEDA might be an alternative to prometheus+adapters
* [superuser.openstack.org: Run Your Kubernetes Cluster on OpenStack in Production](https://superuser.openstack.org/articles/run-your-kubernetes-cluster-on-openstack-in-production/)
* [andrewlock.net: Series: Deploying ASP.NET Core applications to Kubernetes](https://andrewlock.net/series/deploying-asp-net-core-applications-to-kubernetes/)
    * [andrewlock.net: Deploying ASP.NET Core applications to Kubernetes - Part 6 - Adding health checks with Liveness, Readiness, and Startup probes](https://andrewlock.net/deploying-asp-net-core-applications-to-kubernetes-part-6-adding-health-checks-with-liveness-readiness-and-startup-probes/)
* [infoq.com: The Evolution of Distributed Systems on Kubernetes](https://www.infoq.com/articles/distributed-systems-kubernetes) What Comes After Microservices:
    * Yet Microservices gives us the guiding principles on how to split a monolithic application into separate business domains.
    * After that came serverless and Function-as-a-Service (FaaS), where we said we could split those further by operations, giving us extreme scaling - because we can scale each operation individually.
    * The author argues that maybe FaaS is not the best model - as functions are not the best model for implementing reasonably complex services where you want multiple operations to reside together when they have to interact with the same dataset.
    * Probably, multi-runtime as the author calls it Mecha architecture, where you have your business logic in one container, and you have all the infrastructure-related concerns as a separate container.
    * They jointly represent a multi-runtime microservice. Maybe that's a more suitable model because it has better properties.
    * You get all the benefits of microservice. You still have all your domain, all the bounded contexts in one place.
    * You have all the infrastructure and distributed application needs in a separate container, and you combine them at runtime.
    * Probably, the closest thing that's getting to that right now is [Dapr](https://dapr.io/).
* [medium: Graceful shutdown of fpm and nginx in Kubernetes](https://medium.com/inside-personio/graceful-shutdown-of-fpm-and-nginx-in-kubernetes-f362369dff22)
* [fairwinds.com: Over-Provisioned and Over-Permissioned Containers & Kubernetes](https://www.fairwinds.com/blog/over-provisioned-and-over-permissioned-containers-kubernetes)
* [betterprogramming.pub: How to Implement Your Distributed Filesystem With GlusterFS And Kubernetes](https://betterprogramming.pub/how-to-implement-your-distributed-filesystem-with-glusterfs-and-kubernetes-83ee7f5f834f) Learn the advantages of using GlusterFS and how can it help in achieving a highly-scalable, distributed filesystem.
* [compliantkubernetes.io: Compliant Kubernetes is a Certified Kubernetes distribution, that complies with: HIPAA, GDPR, PCI DSS, FFFS 2014:7, ISO 27001, etc. 🌟](https://compliantkubernetes.io)
* [medium: Scaling Kubernetes with Assurance at Pinterest](https://medium.com/pinterest-engineering/scaling-kubernetes-with-assurance-at-pinterest-a23f821168da)
* [blog.flant.com: How we enjoyed upgrading a bunch of Kubernetes clusters from v1.16 to v1.19](https://blog.flant.com/how-we-enjoyed-upgrading-kubernetes-clusters-from-v1-16-to-v1-19/)
* [openshift.com: Topology Aware Scheduling in Kubernetes Part 1: The High Level Business Case](https://www.openshift.com/blog/topology-aware-scheduling-in-kubernetes-part-1-the-high-level-business-case)
    * [openshift.com: Topology Awareness in Kubernetes Part 2: Don’t we already have a Topology Manager?](https://www.openshift.com/blog/topology-awareness-in-kubernetes-part-2-dont-we-already-have-a-topology-manager)
* [Kubernetes setup with CRI-O Runtime](https://github.com/msfidelis/kubernetes-with-cri-o) Example to build Kubernetes Clusters using CRI-O runtime instead of Docker
* [blog.min.io: Kubernetes, Consistency and Commoditization - The Way of the Cloud](https://blog.min.io/the_way_of_the_cloud/)
* [hjrocha.medium.com: Add a Custom Host to Kubernetes](https://hjrocha.medium.com/add-a-custom-host-to-kubernetes-a06472cedccb)
* [rancher.com: The Three Pillars of Kubernetes Container Orchestration 🌟](https://rancher.com/three-pillars-kubernetes-container-orchestration)
* [qwinix.io: What Is Kubernetes? K8s Uses, Benefits, & More](https://www.qwinix.io/blog-what-is-kubernetes/)
* [thenewstack.io: Governance, Risk and Compliance with Kubernetes](https://thenewstack.io/governance-risk-and-compliance-with-kubernetes/)
* [zhimin-wen.medium.com: Custom Notifications with Alert Manager’s Webhook Receiver in Kubernetes](https://zhimin-wen.medium.com/custom-notifications-with-alert-managers-webhook-receiver-in-kubernetes-8e1152ba2c31)
* [harness.io: Introducing Recommendations API: Find Potential Cost Savings Programmatically](https://harness.io/blog/product-updates/recommendations-api/)
* [blog.harbur.io: Demystifying stateful apps on Kubernetes by deploying an etcd cluster](https://blog.harbur.io/demystifying-stateful-apps-on-kubernetes-by-deploying-an-etcd-cluster-b85bf8c16fea) In this tutorial you will learn how to deploy an etcd cluster in Kubernetes
* [blog.kintone.io: Rebooting a LOT of Kubernetes nodes in a declarative way](https://blog.kintone.io/entry/2021/01/14/160935)
* [infoworld.com: How Kubernetes works](https://www.infoworld.com/article/3617008/how-kubernetes-works.html) If you want to understand containers, microservices architecture, modern application development, and cloud native computing, you need to understand Kubernetes.
* [infoq.com: Cloud Native and Kubernetes Observability: Expert Panel](https://www.infoq.com/articles/cloud-native-observability/)
* [kubernetes.io: Don't Panic: Kubernetes and Docker](https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/)
* [thenewstack.io: Exploring the New Kubernetes Maturity Model](https://thenewstack.io/exploring-the-new-kubernetes-maturity-model/)
* [blog.bandowski.eu: Tools that should be used in every Kubernetes cluster 🌟](https://blog.bandowski.eu/tools-that-should-be-used-in-every-kubernetes-cluster-38969ed3e603) 
    * [ArgoCD](https://argoproj.github.io/) for deploying your resources the GitOps way
    * [MetalLB](https://metallb.universe.tf/) in case you need a load balancer when running Kubernetes on-prem and not in a cloud
    * [external-secrets](https://github.com/external-secrets/kubernetes-external-secrets) to easily sync the secrets of your external secret manager with your Kubernetes cluster
    * [cert-manager 🌟](https://cert-manager.io/) to easily retrieve and/or generate new certificates on the fly
        * [github.com/cert-manager](https://github.com/cert-manager)
        * [github.com/cert-manager: Policy Approver](https://github.com/cert-manager/policy-approver) Policy Approver is a cert-manager approver that is responsible for Approving or Denying CertificateRequests.
        * [jetstack.io: Getting started using cert-manager with the sig-network Gateway API](https://www.jetstack.io/blog/cert-manager-gateway-api-traefik-guide/)
    * [external-dns](https://github.com/kubernetes-sigs/external-dns) to manage your DNS entries automatically
* [redhat.com: Building containers by hand: The PID namespace](https://www.redhat.com/sysadmin/pid-namespace) The PID namespace is an important one when it comes to building isolated environments. Find out why and how to use it.
* [infoq.com: The Kubernetes Effect](https://www.infoq.com/articles/kubernetes-effect/)
* [dustinspecker.com: iptables: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/iptables-how-kubernetes-services-direct-traffic-to-pods/)
* [dustinspecker.com: Scaling Kubernetes Pods using Prometheus Metrics 🌟](https://dustinspecker.com/posts/scaling-kubernetes-pods-prometheus-metrics/) one of Kubernetes many features is auto-scaling workloads. Typically, Horizontal Pod Autoscalers scale pods based on CPU or memory usage. During other times we could better scale by using custom metrics that Prometheus is already scraping. Fortunately, Horizontal Pod Autoscalers can support using custom metrics. I’m a fan of the [kube-prometheus 🌟](https://github.com/prometheus-operator/kube-prometheus) project, but it wasn’t apparent how to set up a Horizontal Pod Autoscaler using custom metrics. This post walks through:
    * Deploying kube-prometheus (Prometheus operator, Prometheus adapter, Grafana, and more)
    * Creating a custom metrics APIService
    * Configuring Prometheus adapter to support our custom metrics
    * Deploying a Horizontal Pod Autoscaler for Grafana using a custom metric
* [dev.to: How to switch container runtime in a Kubernetes cluster](https://dev.to/stack-labs/how-to-switch-container-runtime-in-a-kubernetes-cluster-1628)
* [digizoo.com.au: How to Master Admission Webhooks In Kubernetes (GKE) (Part One)](https://digizoo.com.au/1376/mastering-admission-webhooks-in-kubernetes-gke-part-1/) Admission webhooks are HTTP callbacks that receive admission requests (for resources in a K8s cluster) and do something with them. You can define two types of admission webhooks, validating admission webhook and mutating admission webhook. 
* [itnext.io: Breaking down and fixing etcd cluster](https://itnext.io/breaking-down-and-fixing-etcd-cluster-d81e35b9260d)
* [itnext.io: Kubernetes: what are Endpoints](https://itnext.io/kubernetes-what-are-endpoints-3cc9e769b614)
* [medium.com: Using kubernetes custom resources to manage our ephemeral environments](https://medium.com/beamdental/using-kubernetes-custom-resources-to-manage-our-ephemeral-environments-f298610893e1) Building a Kubernetes operator with **kubebuilder** to manage ephemeral environments.
* [medium: Running Apache Flink on Kubernetes](https://medium.com/empathyco/running-apache-flink-on-kubernetes-10815a26559e)
* [learnsteps.com: How exactly kube-proxy works: Basics on Kubernetes](https://www.learnsteps.com/how-exactly-kube-proxy-works-basics-on-kubernetes/)
* [medium.com: Connect services across Kubernetes clusters using Teleproxy](https://medium.com/flare-systems/connect-services-across-kubernetes-clusters-using-teleproxy-3f317cfd8da) [Teleproxy](https://github.com/flared/teleproxy) is a shell script that lets you quickly replace a Kubernetes deployment by a single pod that forwards incoming traffic to another pod running in a destination Kubernetes cluster.
* [medium: Kubernetes DNS for Services and Pods](https://medium.com/kubernetes-tutorials/kubernetes-dns-for-services-and-pods-664804211501)
* [edgehog.blog: Getting Started with K8s: Core Concepts](https://edgehog.blog/getting-started-with-k8s-core-concepts-135fb570462e)
* [talos-systems.com: Is Vanilla Kubernetes Really Too Heavy For The Raspberry Pi?]()
* [infoq.com: Kubernetes Workloads in the Serverless Era: Architecture, Platforms, and Trends](https://www.infoq.com/articles/kubernetes-workloads-serverless-era/)
* [blog.kintone.io: Tolerating failures in container image registries](https://blog.kintone.io/entry/neco-registry) This article will show you several ways to ensure your Kubernetes clusters can always pull images even while an upstream registry is failing.
* [blog.px.dev: How etcd works and 6 tips to keep in mind](https://blog.px.dev/etcd-6-tips/)
* [containerjournal.com: Kubernetes’ True Superpower is its Control Plane](https://containerjournal.com/kubeconcnc/kubernetes-true-superpower-is-its-control-plane/)
* [dev.to: A Deep Dive Into Kubernetes Schema Validation](https://dev.to/datreeio/a-deep-dive-into-kubernetes-schema-validation-39ll)
* [tremolosecurity.com: Pipelines and Kubernetes Authentication](https://www.tremolosecurity.com/post/pipelines-and-kubernetes-authentication) The Right Way To Authenticate to Your Clusters From Your CI/CD Pipelines:
    * Don't use ServiceAccount tokens outside of your cluster
    * Create service accounts inside of your authentication identity provider, assign RBAC privileges
    * Easy with Okta and OpenUnison
* [usepine.com: Improving cert-manager HTTP01 self-check speed](https://www.usepine.com/blog/en/improving-cert-manager-self-check-speed-when-issuing-certificates/) This post describes how to improve cert-manager self-check speed, by pointing the cluster to Google nameservers, and disabling DNS caching
* [datree.io: A Deep Dive Into Kubernetes Schema Validation 🌟](https://www.datree.io/resources/kubernetes-schema-validation) Great overview of different schema validation tools, incl. server-side ,dry-run“. But I think with tools like kind in CI it’s actually less of a burden to spin up K8s and do proper server-side validation (which catches all issues as mentioned in the post).
* [community.suse.com: Stupid Simple Kubernetes — Deployments, Services and Ingresses Explained](https://community.suse.com/posts/stupid-simple-kubernetes-deployments-services-and-ingresses-explained)
* [elastisys.com: PCI DSS compliance in Kubernetes-based platforms](https://elastisys.com/pci-dss-compliance-in-kubernetes-based-platforms/)
* [infracloud.io: Avoiding Kubernetes Cluster Outages with Synthetic Monitoring](https://www.infracloud.io/blogs/avoiding-kubernetes-cluster-outages-synthetic-monitoring/) Synthetic monitoring consists of pre-defined checks to proactively monitor the critical elements in your infrastructure. These checks simulate the functionality of the elements. We can also simulate the communication between the elements to ensure end-to-end connectivity. Continuous monitoring of these checks also helps to measure overall performance in terms of availability and response times.
* [talos-systems.com: Is Vanilla Kubernetes Really Too Heavy For The Raspberry Pi?](https://www.talos-systems.com/blog/is-vanilla-kubernetes-really-too-heavy-for-the-raspberry-pi/)
* [towardsdatascience.com: Kubernetes 101: Cluster Architecture](https://towardsdatascience.com/kubernetes-101-cluster-architecture-d79995785563) They say a picture is worth a thousand (or a million) words
* [blog.kintone.io: Tolerating failures in container image registries 🌟](https://blog.kintone.io/entry/neco-registry)
* [thenucleargeeks.com: Taints and Tolerations in Kubernetes](https://thenucleargeeks.com/2021/06/26/taints-and-tolerations-in-kubernetes-edit/)
* [humanitec.com: Benchmark your Kubernetes setup against 500+ other teams and find out how well (or not) you are doing](https://humanitec.com/kubernetes-team-setup-test)
* [devopshubproject/cka-lab](https://github.com/devopshubproject/cka-lab) This repo contains set of practice questions which will help you to get ready for the cka exam.
* [medium: Run Kubernetes Production Environment on EC2 Spot Instances With Zero Downtime: A Complete Guide](https://medium.com/riskified-technology/run-kubernetes-on-aws-ec2-spot-instances-with-zero-downtime-f7327a95dea)
* [shayn-71079.medium.com: Scaling Kubernetes Clusters](https://shayn-71079.medium.com/scaling-kubernetes-clusters-8a061321de93) The below figure presents a schematic diagram of how cluster auto-scaling is done in AWS EKS clusters.
* [itnext.io: Kubernetes Essential Tools: 2021](https://itnext.io/kubernetes-essential-tools-2021-def12e84c572)
* [thenewstack.io: Living with Kubernetes: Multicluster Management](https://thenewstack.io/living-with-kubernetes-multicluster-management/)
* [tigera.io: Comparing kube-proxy modes: iptables or IPVS?](https://www.tigera.io/blog/comparing-kube-proxy-modes-iptables-or-ipvs/)
* [fairwinds.com: K8s Clinic: How to Run Kubernetes Securely and Efficiently 🌟](https://www.fairwinds.com/blog/k8s-clinic-how-to-run-kubernetes-securely-and-efficiently) 
    * With the adoption of containers, software packaging is increasingly shifting left, which means (depending on your organization) that developers are taking on responsibility for the containerization of applications. Developers may also be responsible for some parts of Kubernetes configuration. As that process shifts left, developers need support to make the right decisions for the organization in order to run Kubernetes securely and efficiently. 
    * Many companies are adopting cloud native technologies to deliver speed to market. For businesses seeking to compete in today's marketplace, it’s important to ship new features and meet customer needs where they are — and increasingly those needs are being met through software.
* [weave.works: Production Ready Checklists for Kubernetes 🌟](https://go.weave.works/production-ready-kubernetes-checklist.html) 
* [containerjournal.com: The Rise of the KubeMaster 🌟](https://containerjournal.com/features/the-rise-of-the-kubemaster/) 
    * It wasn’t obvious while it was happening, probably because everyone was focused on dealing with a global pandemic, but your IT environment became more complex. Cloud technology continued to evolve, and while that was happening, cloud use grew. Hybrid cloud use, already growing before the pandemic, became much more established with a year-over-year annual growth rate of 17.8%, according to Quince Market Insights. And with more distinct technology advances from each of the major cloud service providers, multi-cloud use also became more established.
    * This more complex environment encouraged the use of containers, and Kubernetes became the preferred means of managing them. Unfortunately, the great irony of Kubernetes is that the technology created to make the management of modern cloud applications easier is, itself, incredibly difficult to manage. Just to deploy and manage a single application in your own data center requires working familiarity with a Kubernetes distribution and working integrations with a number of supporting systems and enterprise software including code registries, CI/CD, secrets management, storage management, networking, logging and monitoring, service mesh, backup and disaster recovery (DR). That’s just for one environment. In a hybrid infrastructure, perhaps using one of the leading cloud service providers such as AWS, Azure or GCP, you could double this overhead.
    * This rapid growth combined with immense complexity means not every Kubernetes implementation has been successful, and in the worst cases, misconfigurations have led to security breaches and significant application downtime. Overwhelmed teams with insufficient training only make the problem worse, putting these implementations farther behind as Kubernetes management becomes increasingly difficult. As such, I believe **the time is now for a new role to emerge in the enterprise—Kubernetes Manager**. This is a job function that more and more companies will need to hire as operating and managing Kubernetes becomes a significantly larger part of the engineering operation than ever before. Let me explain.
* [okteto.com: Run your Pull Request Preview Environments on Kubernetes](https://okteto.com/blog/preview-environments-for-kubernetes/)
* [allanjohn909.medium.com: Kubernetes Ingress with Traefik, CertManager, LetsEncrypt and HAProxy](https://allanjohn909.medium.com/kubernetes-ingress-traefik-cert-manager-letsencrypt-3cb5ea4ee071)
* [asishmm.medium.com: Discussion on Horizontal Pod Autoscaler with a demo on local k8s cluster](https://asishmm.medium.com/discussion-on-horizontal-pod-autoscaler-with-a-demo-on-local-k8s-cluster-81694c09f818)
* [piotrminkowski.com: Kubernetes Multicluster with Kind and Submariner](https://piotrminkowski.com/2021/07/08/kubernetes-multicluster-with-kind-and-submariner/)
* [civo.com: Get up and running with Kubeflow on Civo Kubernetes](https://www.civo.com/learn/get-up-and-running-with-kubeflow-on-civo-kubernetes)
* [blog.nillsf.com: How to run your own admission controller on Kubernetes](https://blog.nillsf.com/index.php/2020/12/03/how-to-run-your-own-admission-controller-on-kubernetes/)
* [blog.flant.com: Failure stories #2. How to destroy Elasticsearch while migrating it within Kubernetes](https://blog.flant.com/failure-stories-elasticsearch-migration-within-kubernetes/)
* [dbafromthecold.com: Adjusting pod eviction time in Kubernetes](https://dbafromthecold.com/2020/04/08/adjusting-pod-eviction-time-in-kubernetes/)
* [doordash.engineering: Gradual Code Releases Using an In-House Kubernetes Canary Controller](https://doordash.engineering/2021/04/14/gradual-code-releases-using-an-in-house-kubernetes-canary-controller/) Gradual code releases with canary deployments and a custom Kubernetes controller
* [itnext.io: How to deploy a cross-cloud Kubernetes cluster with built-in disaster recovery 🌟](https://itnext.io/how-to-deploy-a-cross-cloud-kubernetes-cluster-with-built-in-disaster-recovery-bbce27fcc9d7)
* [getambassador.io: Getting Started with Kubernetes for JavaScript Developers](https://www.getambassador.io/resources/getting-started-with-kubernetes-for-javascript-developers/)
* [blog.cloudflare.com: Automatic Remediation of Kubernetes Nodes](https://blog.cloudflare.com/automatic-remediation-of-kubernetes-nodes/)
* [pulumi.com: Kubernetes Fundamentals Part One - Python instead of YAML 🌟](https://www.pulumi.com/blog/kubernetes-fundamentals-part-one/)
* [ubuntu.com: How to test the latest Kubernetes 1.22 release candidate with MicroK8s](https://ubuntu.com/blog/how-to-test-the-latest-kubernetes-with-microk8s)
* [thenewstack.io: 10 Steps to a Successful Kubernetes Technical Transformation 🌟](https://thenewstack.io/10-steps-to-a-successful-kubernetes-technical-transformation/)
* [medium: Kubernetes Scaling & Replicas 🌟](https://medium.com/brainyydude/kubernetes-scaling-replicas-69fcd44b0630) Whenever we talk about “Scaling”, we need to discuss the states of the application. There are two types: Stateful and Stateless Applications.
    *  Stateful: A stateful application can remember at least some of the things(from the past) about its state when it runs each time. For example: It stores our preferences, keeps track of window size and location, and remembers what files they have opened recently. Their Attributes are:
        * persistence Storage
        * gracefully deployment and scaling
        * gracefully deletion and termination
        * Automated rolling updates
    *  Stateless: A stateless application requests are self-contained, i.e. everything is contained within the request, and handled in two distinct phases - a “request” and a “response.” Their Attributes are:
        *  Scaling can be done independently
        * Mortal (Kubernetes Pods are mortal. They are born and when they die, they are not resurrected)
        *  No persistence Storage
        * Client Cookies can be used to make service stateless
* [cncf.io: Advanced Kubernetes pod to node scheduling](https://www.cncf.io/blog/2021/07/27/advanced-kubernetes-pod-to-node-scheduling/) In this article, you'll review some of the use cases for advanced pod scheduling in Kubernetes as well as best practices for implementing it in real-world situations.
* [medium: Create A Pod In Kubernetes Cluster](https://medium.com/codex/create-a-pod-in-kubernetes-cluster-b9e0c33bb904) Learn what is Pod and how to create a Pod in the Kubernetes cluster.
* [cloudsavvyit.com: How to Scale Docker Containers Across Servers Using Kubernetes](https://www.cloudsavvyit.com/13039/how-to-scale-docker-containers-across-servers-using-kubernetes/)
* [Kubernetes. Label and Selector. Important Topic. Identify object in cluster. CKA Exam Tips](https://www.youtube.com/watch?app=desktop&v=Vh3piGAxcf8&ab_channel=AlokKumar)
* [thenewstack.io: Cloud Foundry Summit: Kubernetes Must Do Better by Developers](https://thenewstack.io/cloud-foundry-summit-kubernetes-must-do-better-by-developers/)
* [itnext.io: How to create Kubernetes home lab on an old laptop with K3s](https://itnext.io/how-to-create-kubernetes-home-lab-on-an-old-laptop-1de6cc12c13e)
* [itnext.io: How to deploy a single Kubernetes cluster across multiple clouds using k3s and WireGuard](https://itnext.io/how-to-deploy-a-single-kubernetes-cluster-across-multiple-clouds-using-k3s-and-wireguard-a5ae176a6e81)
* [itnext.io: How to Add MySql & MongoDB to a Kubernetes .Net Core Microservice Architecture](https://itnext.io/databases-in-a-kubernetes-angular-net-core-microservice-arch-a0c0ae23dca9) How to add a MySQL DB and a MongoDB replica set in K8S on Docker desktop using persistent volumes and access the databases from ASP.NET Core, C# and Angular
* [itnext.io: Expose Open Policy Agent/Gatekeeper Constraint Violations for Kubernetes Applications with Prometheus and Grafana](https://itnext.io/expose-open-policy-agent-gatekeeper-constraint-violations-with-prometheus-and-grafana-6b7ac92ea07f)
* [thenewstack.io: How Airbnb and Twitter Cut Back on Microservice Complexities](https://thenewstack.io/how-airbnb-and-twitter-cut-back-on-microservice-complexities/)
* Some useful and promising Kubernetes projects to follow: 
    - [submarinerio](https://twitter.com/submarinerio) multicluster direct networking
    - [shipwrightio](https://twitter.com/shipwrightio) building container images
    - [microcksio](https://twitter.com/microcksio) testing API and messaging
    - [telepresenceio](https://twitter.com/telepresenceio) development tool
    - [k0sproject](https://twitter.com/k0sproject) new Kubernetes distro
* [redkubes.com: DIY Kubernetes-based platform building – part 3](https://redkubes.com/diy-kubernetes-based-platform-building-part-3/)
* [hobby-kube/guide 🌟](https://github.com/hobby-kube/guide) Kubernetes clusters for the hobbyist. This guide answers the question of how to setup and operate a fully functional, secure Kubernetes cluster on a cloud provider such as Hetzner Cloud, DigitalOcean or Scaleway. It explains how to overcome the lack of external ingress controllers, fully isolated secure private networking and persistent distributed block storage.
* [wecloudpro.com: Watchers in Kubernetes](https://www.wecloudpro.com/2021/08/21/Watchers-in-Kubernetes.html)
* [learnk8s.io: Kubernetes wallpapers](https://learnk8s.io/kubernetes-wallpapers) A collection of free Kubernetes wallpapers for your computer.
* [youtube: Tinder's Move to Kubernetes - Chris O'Brien & Chris Thomas, Tinder](https://www.youtube.com/watch?app=desktop&v=o3WXPXDuCSU)
* [medium: How to enable Kubernetes container RuntimeDefault seccomp profile for all workloads](https://medium.com/@LachlanEvenson/how-to-enable-kubernetes-container-runtimedefault-seccomp-profile-for-all-workloads-6795624fcbcc)
* [doordash.engineering: Gradual Code Releases Using an In-House Kubernetes Canary Controller](https://doordash.engineering/2021/04/14/gradual-code-releases-using-an-in-house-kubernetes-canary-controller/)
* [infoq.com: Six Tips for Running Scalable Workloads on Kubernetes](https://www.infoq.com/articles/tips-running-scalable-workloads-kubernetes/)
* [Assess managed Kubernetes services for your workloads.](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services) Managed services from cloud providers can simplify Kubernetes deployment but create some snags in a multi-cloud model. Follow three steps to see if these services can benefit you.
* [itnext.io: Evolution of PaaSes to Platform-as-Code in Kubernetes world](https://itnext.io/evolution-of-paases-to-platform-as-code-in-kubernetes-world-74464b0013ca)
* [medium: Wordpress High Availability on Kubernetes](https://medium.com/@icheko/wordpress-high-availability-on-kubernetes-f6c0bcc2f28d) Wordpress is configured to support two separate ingress paths — a private for edits and a public for read-only traffic. By “read-only”, mean that Wordpress is only able to execute SELECTs on the DB. The HA MySQL cluster is accomplished using oracle’s mysql-operator. This makes it extremely easy to handle the master-slave replication for the DB side of things.
* [cloudfoundry.org: Deploy A Laravel Application To Kubernetes Using Cloud Foundry](https://www.cloudfoundry.org/blog/deploy-laravel-app-to-k8s-with-cf/) This tutorial uses the Google Kubernetes Engine (GKE). However, the steps followed in this guide can be applied to Kubernetes clusters running on any cloud provider, as long as Cloud Foundry (cf-for-k8s) has been installed on it. Also, the series of install steps outlined here can function for any “composer” based PHP application such as Drupal, Symfony, etc.
* [thenewstack.io: The State of Kubernetes: Key Challenges and the Role of AI](https://thenewstack.io/the-state-of-kubernetes-key-challenges-and-the-role-of-ai/)
* [learnsteps.com: Basics on Kubernetes: What exactly is a ReplicaSet](https://www.learnsteps.com/basics-on-kubernetes-what-exactly-is-a-replicaset/)
* [ithands-on.com: Kubernetes 101 : Switching namespaces](https://www.ithands-on.com/2021/10/kubernetes-101-switching-namespaces.html)
* [juju.is: Kubernetes and cloud native operations report 2021](https://juju.is/cloud-native-kubernetes-usage-report-2021) Data from 1200 respondents on hybrid and multi-cloud operations, Kubernetes, VMs, bare metal, goals, benefits, challenges, operators, advanced usage, edge, and more.
* [medium.com: Tinder’s move to Kubernetes](https://medium.com/tinder-engineering/tinders-move-to-kubernetes-cda2a6372f44)
* [==blog.flant.com: Best practices for deploying highly available apps in Kubernetes. Part 1==](https://blog.flant.com/best-practices-for-deploying-highly-available-apps-in-kubernetes-part-1/)
    * [blog.flant.com: Best practices for deploying highly available apps in Kubernetes. Part 2](https://blog.flant.com/best-practices-for-deploying-highly-available-apps-in-kubernetes-part-2/)
* [danielmangum.com: How Kubernetes validates custom resources](https://danielmangum.com/posts/how-kubernetes-validates-custom-resources/)
* [ronaknathani.com: How a Kubernetes Pod Gets an IP Address](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address/)
* [opensource.com: How the Kubernetes ReplicationController works](https://opensource.com/article/21/11/kubernetes-replicationcontroller) A ReplicationController is responsible for managing the pod lifecycle and ensuring that the specified number of pods required are running at any given time.
* [containerjournal.com: When is Kubernetes Service Ownership the Right Fit?](https://containerjournal.com/features/when-is-kubernetes-service-ownership-the-right-fit/)
    * Why is Kubernetes service ownership emerging as the way for software delivery and operations teams to establish full “ownership” of the services they support? Because ownership covers the lifespan of software from development to deployment to the sunsetting process. And this shift to full-spectrum accountability brings about dramatic improvements in the overall speed, reliability, security and cost of applications. 
    * Of course, it’s not always easy to determine which organizations need this level of ownership. When businesses grow, they typically discover that pushing the delivery of applications and services through a gate of operations is challenging at best, impossible at worst. Even so, the DevSecOps mindset is on the rise, which means teams are now seeking ways to make this type of shift into more meaningful and effective ownership. It is the shift that enables a deep fundamental change to occur within an organization. 
* [itnext.io: Kubernetes — Running Multiple Container Runtimes](https://itnext.io/kubernetes-running-multiple-container-runtimes-65220b4f9ef4) In this post, you'll learn how to run multiple OCI container runtimes on Kubernetes. You will see how to configure containerd to run both runC and Kata Containers
* [iximiuz.com: Why and How to Use containerd from the Command Line](https://iximiuz.com/en/posts/containerd-command-line-clients/)
* [medium: Kubernetes for dummies: introduction. Part 1](https://medium.com/@mfsilv/kubernetes-a-gentle-introduction-9d23de7f00e0)
    * [medium: Kubernetes for dummies: the cluster. Part 2](https://medium.com/@mfsilv/kubernetes-for-dummies-the-cluster-7cf6a7b5532)
    * [itnext.io: Kubernetes for dummies: Life of a Pod. Part 3](https://itnext.io/kubernetes-for-dummies-life-of-a-pod-fc8158e27aa)
* [==iximiuz.com: Containers vs. Pods - Taking a Deeper Look==](https://iximiuz.com/en/posts/containers-vs-pods/)
* [kubermatic.com: The Ultimate Checklist for Running Kubernetes in Production](https://www.kubermatic.com/resources/the-ultimate-checklist-for-running-kubernetes-in-production)
* [==vadosware.io: So you need to wait for some Kubernetes resources?==](https://vadosware.io/post/so-you-need-to-wait-for-some-kubernetes-resources/) __There are at least two ways to wait for Kubernetes resources you probably care about: kubectl wait for Pods, initContainers for everything else__
* [vxav.fr: Interacting with containerd runtime for kubernetes](https://www.vxav.fr/2021-09-13-interacting-with-containerd-runtime-for-kubernetes/)
* [medium: Exploring Kubernetes Node Architecture](https://medium.com/nerd-for-tech/exploring-kubernetes-node-architecture-3a36df6ae034)
* [mayankshah.dev: Demystifying kube-proxy](https://mayankshah.dev/blog/demystifying-kube-proxy/)
* [arthurchiao.art: Cracking kubernetes node proxy (aka kube-proxy)](https://arthurchiao.art/blog/cracking-k8s-node-proxy/) This post analyzes the Kubernetes node proxy model, and provides 5 demo implementations (within couples of lines of code) of the model, each based on different tech-stacks (userspace/iptables/ipvs/tc-ebpf/sock-ebpf).
* [blog.brujordet.no: Using custom hardware in kubernetes](https://blog.brujordet.no/post/homelab/using_custom_hardware_in_kubernetes/)
* [==technos.medium.com: Kubernetes Workflow for Absolute Beginners==](https://technos.medium.com/kubernetes-workflow-bad346c54962)
* [==cloud.google.com: The past, present, and future of Kubernetes with Eric Brewer==](https://cloud.google.com/blog/products/containers-kubernetes/the-rise-and-future-of-kubernetes-and-open-source-at-google)
* [kmitevski.com: Writing a Kubernetes Validating Webhook using Python](https://kmitevski.com/writing-a-kubernetes-validating-webhook-using-python/)
* [medium.com/@hinsulak: Multi-node lightweight Kubernetes setup](https://medium.com/@hinsulak/multi-node-lightweight-kubernetes-setup-using-k3s-454e87fdc933)
* [kubernetes.io: Kubernetes is Moving on From Dockershim: Commitments and Next Steps](https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/)
* [blog.px.dev: Where are my container's files? Inspecting container filesystems](https://blog.px.dev/container-filesystems/)
* [medium.com/codex: How to Deploy WordPress On Kubernetes — Part 2](https://medium.com/codex/how-to-deploy-wordpress-on-kubernetes-part-2-df1cc9cbaa2e) Learn how to deploy the WordPress on Kubernetes and connect with MySQL Pod.
* [freecodecamp.org: Learn Kubernetes and Start Containerizing Your Applications](https://www.freecodecamp.org/news/learn-kubernetes-and-start-containerizing-your-applications/)
* [==komodor.com: Kubernetes Nodes – The Complete Guide==](https://komodor.com/learn/kubernetes-nodes-complete-guide/)
* [medium.com/techbeatly: Chain of events behind a running Pod](https://medium.com/techbeatly/chain-of-events-behind-a-running-pod-149ebaafbfbc) What exactly happens behind the scenes when you create a pod/deployment?

### kubeconfig
* [medium: Mastering the KUBECONFIG file](https://medium.com/@ahmetb/mastering-kubeconfig-4e447aa32c75)
* [rcarrata.github.io: Regenerating Kubeconfig for system:admin user in OpenShift clusters](https://rcarrata.github.io/openshift/regenerate-kubeconfig/) You missed your kubeconfig file of your OpenShift cluster? Your dog ate your kubeconfig file? No worries! Let’s regenerate it in a easy and automated way!

### Docker and Kubernetes
* [kruyt.org: Migrate from Docker to Containerd in Kubernetes](https://kruyt.org/migrate-docker-containerd-kubernetes)
* [opensourcerers.org: How to go from Docker to Kubernetes the right way 🌟](https://www.opensourcerers.org/2021/02/01/how-to-go-from-docker-to-kubernetes-the-right-way/)
* [loft.sh: Docker Compose to Kubernetes: Step-by-Step Migration 🌟](https://loft.sh/blog/docker-compose-to-kubernetes-step-by-step-migration)
* [linuxtechi.com: How to Setup Private Docker Registry in Kubernetes (k8s)](https://www.linuxtechi.com/setup-private-docker-registry-kubernetes/)
* [itnexst.io: Docker and Kubernetes — root vs. privileged](https://itnext.io/docker-and-kubernetes-root-vs-privileged-9d2a37453dec)
* [containerjournal.com: Best of 2020: How Docker and Kubernetes Work Together](https://containerjournal.com/topics/container-ecosystems/how-docker-and-kubernetes-work-together/)
* [blog.sighup.io: How to run Kubernetes without Docker](https://blog.sighup.io/how-to-run-kubernetes-without-docker/) Sooner or later this moment had to come, and it finally has: Kubernetes is deprecating Docker as a Container Runtime Interface in favor of the other supported runtimes. Let's try to explain why Docker seems really replaceable.

#### Kubernetes vs Docker
* [cloudify.co: Docker Vs. Kubernetes](https://cloudify.co/blog/docker-vs-kubernetes-comparison/)
#### Kubernetes vs Docker Swarm
* [dynatrace.com: Kubernetes vs Docker: What’s the difference?](https://www.dynatrace.com/news/blog/kubernetes-vs-docker/)
* [imaginarycloud.com: Docker VS Kubernetes? It should be Docker + Kubernetes](https://www.imaginarycloud.com/blog/docker-vs-kubernetes/)

### Kubernetes Admission Controllers
* [sysdig.com: Kubernetes admission controllers in 5 minutes](https://sysdig.com/blog/kubernetes-admission-controllers/)
* [blog.rewanthtammana.com: Creating Malicious Admission Controllers](https://blog.rewanthtammana.com/creating-malicious-admission-controllers)
* [loft.sh: Kubernetes Admission Controllers: What They Are and Why They Matter](https://loft.sh/blog/kubernetes-admission-controllers-what-they-are-and-why-they-matter)
* [kubernetes.io: Using Admission Controllers to Detect Container Drift at Runtime](https://kubernetes.io/blog/2021/12/21/admission-controllers-for-container-drift/)
* [slack.engineering: A Simple Kubernetes Admission Webhook](https://slack.engineering/simple-kubernetes-webhook/)

### Kubernetes Mutating Webhooks
- [medium.com/@pflooky: Intro to Kubernetes Mutating Webhooks (get more out of Kubernetes)](https://medium.com/@pflooky/intro-to-kubernetes-mutating-webhooks-even-if-you-dont-know-kubernetes-172c30232488) 
    - In its simplest terms, a **MutatingWebhookConfiguration** defines a webhook application to alter a Kubernetes resource when a particular action is taken on it. For example, if I wanted to add particular labels to all the pods that are created, it could be done by a mutating webhook which watches for all CREATE POD events and adds the labels to that pod before it gets deployed.
    - **Why:** As the development teams put larger workloads into Kubernetes, managing all of the resources becomes quite difficult as there may be different deployment patterns and life cycles. Mutating webhooks give you the ability to target changes to any Kubernetes resource regardless of their deployment mechanisms and alter them before or after any point within the life cycle.
    - Some use cases where it could be used include:
        - Metadata management: include useful metadata about team, environment or type of workload to each Kubernetes resource
        - Attaching sidecar processes: add a log listener to particular pods
        - Secret management: apply consistent secret retrieval across all resources
        - Deployment configuration: could add environment variables or configmaps on the fly to pods

### Kubernetes Cloud Controller Manager
* [medium: The Kubernetes Cloud Controller Manager](https://medium.com/@m.json/the-kubernetes-cloud-controller-manager-d440af0d2be5)
### Kubernetes Resources
* [medium: Kubernetes Resources 🌟](https://medium.com/@pratyush.mathur/kubernetes-resources-c09d172dbdc5)
* [enterprisersproject.com: Managing Kubernetes resources: 5 things to remember](https://enterprisersproject.com/article/2020/8/managing-kubernetes-resources-5-things-remember) Kubernetes automates much of the work of managing containers at scale. But containerized applications commonly share pooled resources, so you need to allocate and manage them properly
* [stackify.com: The Advantages of Using Kubernetes and Docker Together](https://stackify.com/kubernetes-docker-deployments/)
* [linuxadvise.com: Kubernetes Node Affinity](https://www.linuxadvise.com/post/kubernetes-node-affinity)
* [linuxadvise.com: Kubernetes Daemon Sets](https://www.linuxadvise.com/post/kubernetes-daemon-sets)
* [magalix.com: **Team Productivity: Resource Management** 🌟](https://www.magalix.com/blog/team-productivity-1) Resource Requests, Limits and Quota

#### Kubernetes Pods
* [medium.com: kubernetes Pod Priority and Preemption](https://medium.com/@mohaamer5/kubernetes-pod-priority-and-preemption-943c58aee07d)
* [itnext.io: K8s prevent queue worker Pod from being killed during deployment](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) How to prevent a Kubernetes (like RabbitMQ) queue worker Pod from being killed during deployment while handling a message?
* [medium: How to configure and manage Pod in Kubernetes Cluster (K8s)](https://medium.com/faun/pod-in-kubernetes-cluster-k8s-adeb5b901153) There are two types of Pods: Single container pod & Multi container pod. 
* [howtoforge.com: How to create Multi-Container Pods in Kubernetes](https://www.howtoforge.com/multi-container-pods-in-kubernetes/)
* [Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) When retrieving all service’s connected pods is desired
* [Kubernetes Tip: What Happens To Pods Running On Node That Become Unreachable?](https://medium.com/tailwinds-navigator/kubernetes-tip-what-happens-to-pods-running-on-node-that-become-unreachable-3d409f734e5d)
* [medium: Kubernetes Pod Redundancy Strategies](https://medium.com/better-programming/kubernetes-pod-redundancy-strategies-a6d9b560749a)
* [medium: Discovering Running Pods By Using DNS and Headless Services in Kubernetes 🌟](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4) When retrieving all service’s connected pods is desired.
* [iximiuz.com: Service proxy, pod, sidecar, oh my!](https://iximiuz.com/en/posts/service-proxy-pod-sidecar-oh-my/)
* [linuxadvise.com: Kubernetes Static Pods](https://www.linuxadvise.com/post/kubernetes-static-pods)
* [linuxadvise.com: Kubernetes Pod Security Policy](https://www.linuxadvise.com/post/kubernetes-pod-security-policy)
* [medium: Discovering Running Pods By Using DNS and Headless Services in Kubernetes](https://medium.com/swlh/discovering-running-pods-by-using-dns-and-headless-services-in-kubernetes-7002a50747f4)
* [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods/) Why are Pod not fully restartable in Kubernetes? Why is Kubernetes not restarting the Pod in **CrashLoopBackOff**?
* [medium: Notes on Graceful Shutdown in Kubernetes 🌟](https://medium.com/@pleasingsmoke/graceful-shutdown-of-pods-in-kubernetes-6da5588b5356)
* [didil.medium.com: Building a Kubernetes Mutating Admission Webhook](https://didil.medium.com/building-a-kubernetes-mutating-admission-webhook-7e48729523ed) A “magic” way to inject a file into Pod Containers
* [thenucleargeeks.com: Introduction to Kubernetes Pods](https://thenucleargeeks.com/2021/03/22/introduction-to-pods-in-kubernetes/)
* [speakerdeck.com: Kubernetes Pod internals with the fundamentals of Containers](https://speakerdeck.com/devinjeon/kubernetes-pod-internals-with-the-fundamentals-of-containers)
* [kubernetes.io: PodSecurityPolicy Deprecation: Past, Present, and Future 🌟](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
* [dustinspecker.com: IPVS: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/ipvs-how-kubernetes-services-direct-traffic-to-pods/)
* [returngis.net: Organizar los pods en Kubernetes usando taints y tolerations](https://www.returngis.net/2020/06/organizar-los-pods-en-kubernetes-usando-taints-y-tolerations/)
* [==medium: How to Schedule Pods on Nodes in Kubernetes==](https://medium.com/@knoldus/how-to-schedule-pods-on-nodes-in-kubernetes-af321d8ea5d)
* [==medium: Kubernetes: Evenly Distribution of Pods Across Cluster Nodes== |Puru Tuladhar](https://medium.com/geekculture/kubernetes-distributing-pods-evenly-across-cluster-c6bdc9b49699)
* [medium: Understanding PodSecurity in Kubernetes](https://medium.com/@orangecola3/understanding-podsecurity-in-kubernetes-e58a65102056)
* [blog.searce.com: Single Pod Access Mode for Persistent Volumes on Kubernetes](https://blog.searce.com/single-pod-access-mode-for-persistent-volumes-on-kubernetes-4cf79200aa9a) This article will explore a new feature introduced by Kubernetes v1.22, a fourth access mode used for CSI volumes.

#### Kubernetes ConfigMaps
* [medium: ConfigMaps in Kubernetes: how they work and what you should remember 🌟](https://medium.com/flant-com/configmaps-in-kubernetes-f9f6d0081dcb)
* [medium: ConfigMaps in Kubernetes (K8s)](https://medium.com/faun/configmaps-in-kubernetes-k8s-2f2ce79d7e66)
* [itnext.io: Working with kubernetes configmaps, part 1: volume mounts](https://itnext.io/working-with-kubernetes-configmaps-part-1-volume-mounts-f0ace283f5aa)
    * [itnext.io: Working with kubernetes configmaps, part 2: Watchers](https://itnext.io/working-with-kubernetes-configmaps-part-2-watchers-b6dd0e583d71)
* [blog.gopaddle.io: Strange things you never knew about Kubernetes ConfigMaps on day one 🌟🌟](https://blog.gopaddle.io/2021/04/01/strange-things-you-never-knew-about-kubernetes-configmaps-on-day-one/)
* [k21academy.com: Kubernetes ConfigMaps and Secrets: Guide to Create and Update 🌟](https://k21academy.com/docker-kubernetes/configmaps-secrets/)  
* [kubermatic.com: Keeping the State of Apps Part 3: Introduction to ConfigMaps 🌟](https://www.kubermatic.com/blog/keeping-the-state-of-apps-part-3-introduction-to-configmaps)
* [medium: Kubernetes ConfigMaps Explained](https://medium.com/codex/kubernetes-configmaps-explained-961cdd23f232)
* [linuxadvise.com: Kubernetes Config Maps](https://www.linuxadvise.com/post/kubernetes-config-maps)
#### Kubernetes Secrets
* [linuxadvise.com: Kubernetes Secrets](https://www.linuxadvise.com/post/kubernetes-secrets)
* https://blog.newrelic.com/engineering/how-to-use-kubernetes-secrets/

#### Kubernetes Volumes
* [linkedin.com/pulse: What are Kubernetes Persistent Volumes?](https://www.linkedin.com/pulse/what-kubernetes-persistent-volumes-gyan-prakash-1f/)
* [blog.newrelic.com: Kubernetes Fundamentals, Part 5: Working with Kubernetes Volumes](https://blog.newrelic.com/engineering/how-to-use-kubernetes-volumes/)
* [medium: Kubernetes Persistent Volume Explained](https://medium.com/codex/kubernetes-persistent-volume-explained-fb27df29c393)
* [giffgaff.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://www.giffgaff.io/tech/resizing-statefulset-persistent-volumes-with-zero-downtime)
* [kubermatic.com: Keeping the State of Apps 1: Introduction to Volume and volumeMounts](https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts) In this blog post, you will get a hands-on practice and learn how to provide persistent storage in the form of different volumes to the Pods.
#### Kubernetes Namespaces and Multi Tenancy. Self Service Namespaces
- [Self-Service Kubernetes Namespaces Are A Game-Changer 🌟](https://loft.sh/blog/self-service-kubernetes-namespaces-are-a-game-changer/)
- [qvault.io: How to Restart All Pods in a Kubernetes Namespace](https://qvault.io/2020/10/26/how-to-restart-all-pods-in-a-kubernetes-namespace/)
- [medium: How to create Namespaces in Kubernetes? 🌟](https://medium.com/faun/namespaces-in-kubernetes-4bac49414770)
- [starwindsoftware.com: Remove a Kubernetes namespace blocked with Terminating status](https://www.starwindsoftware.com/blog/remove-a-kubernetes-namespace-blocked-with-terminating-status) 
- [opensource.com: Configure multi-tenancy with Kubernetes namespaces 🌟](https://opensource.com/article/21/2/kubernetes-namespaces) Namespaces provide basic building blocks of access control for applications, users, or groups of users.
- [Kubernetes Hierarchical Namespace Controller (slides from Kubernetes Multitenancy Working Group) 🌟](https://static.sched.com/hosted_files/kccncna19/f7/kubecon-us-2019-mt-wg-deep-dive.pdf)
- [kubernetes.io: Introducing Hierarchical Namespaces](https://kubernetes.io/blog/2020/08/14/introducing-hierarchical-namespaces/)
- [Hierarchical namespaces](https://github.com/kubernetes-sigs/multi-tenancy/tree/master/incubator/hnc) make it easier to share your Kubernetes cluster. For example, you can create additional namespaces under your team's namespace, even if you don't have cluster-level permission to create namespaces
- [medium: Kubernetes Multi-Tenancy — A Best Practices Guide 🌟](https://medium.com/faun/kubernetes-multi-tenancy-a-best-practices-guide-88e37ef2b709)
- [vamsitalkstech.com: Kubernetes Multi-tenancy Best Practices & Architecture Model..(2/2)](https://www.vamsitalkstech.com/architecture/kubernetes-multitenancy-best-practices-architecture-models-2-2/)
- [loft.sh: Kubernetes Multi-Tenancy: Why Virtual Clusters Are The Best Solution](https://loft.sh/blog/kubernetes-multi-tenancy-why-virtual-clusters-are-the-best-solution/)
- [kubesphere.io: Kubernetes Multi-tenancy in KubeSphere](https://kubesphere.io/docs/access-control-and-account-management/multi-tenancy-in-kubesphere/)
- [kubernetes.io: Three Tenancy Models For Kubernetes](https://kubernetes.io/blog/2021/04/15/three-tenancy-models-for-kubernetes/) What are your tenancy options with Kubernetes? This post calls out three: by namespace, by cluster, by control plane.
- [thenewstack.io: Avoiding the Pitfalls of Multitenancy in Kubernetes](https://thenewstack.io/avoiding-the-pitfalls-of-multitenancy-in-kubernetes/)
- [blog.sighup.io: Hierarchical Namespace Controller (HNC): a look into the future of Kubernetes Multitenancy](https://blog.sighup.io/an-introduction-to-hierarchical-namespace-controller-hnc/) Hierarchical Namespace Controller (HNC) is bringing a better multi-tenancy model to Kubernetes. In this article we are exploring the current state of the project and useful use-cases.
- [vamsitalkstech.com: Introduction to Kubernetes Multi-tenancy..(1/2)](https://www.vamsitalkstech.com/architecture/a-deepdive-into-kubernetes-multitenancy-1-2/)
- [asonisg.medium.com: Multi-tenancy with Kubernetes (Part-1)](https://asonisg.medium.com/multi-tenancy-with-kubernetes-part-1-8ac4e5083e31)
- [openshift.com: The Hidden Dangers of Terminating Namespaces 🌟](https://www.openshift.com/blog/the-hidden-dangers-of-terminating-namespaces)
- [medium: Kubernetes Namespaces vs. Virtual Clusters](https://medium.com/geekculture/kubernetes-namespaces-vs-virtual-clusters-cc8731752972)
- [engineering.salesforce.com: Project Agumbe: Share Objects Across Namespaces in Kubernetes 🌟](https://engineering.salesforce.com/project-agumbe-share-objects-across-namespaces-in-kubernetes-1fc2e1ddb3eb)
- [p3r.one: Delete namespace stuck in Terminating State](https://www.p3r.one/delete-terminating-namespace/)
- [loft.sh: Multi-Tenant Kubernetes Clusters: Challenges and Useful Tooling](https://loft.sh/blog/multi-tenant-kubernetes-clusters-challenges-and-useful-tooling)
- [infracloud.io: Introduction to Multi-Tenancy in Kubernetes](https://www.infracloud.io/blogs/multi-tenancy-kubernetes/)

##### Creating Users
* [cloudhero.io](https://cloudhero.io/creating-users-for-your-kubernetes-cluster) Creating Users for your Kubernetes Cluster. Learn how to use x509 certificates to authenticate users in your cluster.

#### Kubernetes Labels and Selectors
* [sandeepbaldawa.medium.com: K8s Labels & Selectors](https://sandeepbaldawa.medium.com/k8s-labels-selectors-9ad2fcf78a4e) In this post, we will look at What Kubernetes(K8s) Labels and Selectors are, Why do we need them, How to use them.
* [blog.kubecost.com: The Guide to Kubernetes Labels](https://blog.kubecost.com/blog/kubernetes-labels/)
* [millionvisit.blogspot.com: Kubernetes for Developers #8: Kubernetes Object Name, Labels, Selectors and Namespace](http://millionvisit.blogspot.com/2021/02/kubernetes-for-developers-8-Object%20Name-Labels-Selectors-Namespace.html)
* [millionvisit.blogspot.com: Kubernetes for Developers #11: Pod Organization using Labels](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-11-pod-organization-using-labels.html)
* [linuxadvise.com: Kubernetes Node Selectors](https://www.linuxadvise.com/post/kubernetes-node-selectors)
* [ithands-on.com: Kubernetes 101 : Changing a Pod's label on the fly](https://www.ithands-on.com/2021/04/kubernetes-101-changing-pods-label-on.html)
* [blog.newrelic.com: Kubernetes Fundamentals, Part 4: How to Organize Clusters](https://blog.newrelic.com/engineering/how-to-organize-kubernetes-clusters/)

#### Kubernetes Taints and Tolerations
* [thenucleargeeks.com: Taints and Tolerations in Kubernetes](https://thenucleargeeks.com/2021/03/28/taints-and-tolerations-in-kubernetes/)
* [faun.pub: Taints And Toleration Basics In Kubernetes](https://faun.pub/taints-and-toleration-basics-in-kubernetes-c0538c3f6deb)
* [blog.learncodeonline.in: Kubernetes Scheduling - Taints and Tolerations](https://blog.learncodeonline.in/kubernetes-scheduling-taints-and-tolerations)
#### Kubernetes Deployment, Rollling Updates and Rollbacks
* [medium: How to Deploy a Web Application with Kubernetes](https://medium.com/swlh/how-to-deploy-an-asp-net-application-with-kubernetes-3c00c5fa1c6e) Learn how to create a Kubernetes cluster from scratch and deploy a web application (SPA+API) in two hours.
* [itnext.io: Kubernetes rolling updates, rollbacks and multi-environments](https://itnext.io/kubernetes-rolling-updates-rollbacks-and-multi-environments-4ff9912df5)
* [linuxadvise.com: Kubernetes Rolling Updates and Rollbacks](https://www.linuxadvise.com/post/kubernetes-rolling-updates-and-rollbacks)
* [medium: How Rolling and Rollback Deployments work in Kubernetes](https://medium.com/@yankee.exe/how-rolling-and-rollback-deployments-work-in-kubernetes-8db4c4dce599)
* [medium: Kubernetes Deployment — Rolling Updates and Rollbacks Explained](https://medium.com/codex/kubernetes-deployment-rolling-updates-and-rollbacks-explained-e3efa6557368) Learn how to update the application once created a Deployment in the Kubernetes cluster and how to rollback. 
* [thenewstack.io: How do applications run on kubernetes?](https://thenewstack.io/how-do-applications-run-on-kubernetes/)
* [deepsource.io: Breaking down zero downtime deployments in Kubernetes](https://deepsource.io/blog/zero-downtime-deployment/) An in-depth analysis of deployments in Kubernetes
* [k21academy.com: Kubernetes Deployment and Step-by-Step Guide to Deployment: Update, Rollback, Scale & Delete](https://k21academy.com/docker-kubernetes/kubernetes-deployment/)
* [medium: Kubernetes Deployment: Connect Your Front End to Your Back End With Nginx](https://medium.com/better-programming/kubernetes-deployment-connect-your-front-end-to-your-back-end-with-nginx-7e4e7cfef177)
* [sbg.technology: Zero-Downtime Kubernetes Deployments](https://sbg.technology/2020/08/21/zero-downtime-kubernetes-deployments/)
* [Zero-Downtime Kubernetes Deployments](https://sbg.technology/2020/08/21/zero-downtime-kubernetes-deployments)
* [mirantis.com: Introduction to YAML: Creating a Kubernetes deployment](https://www.mirantis.com/blog/introduction-to-yaml-creating-a-kubernetes-deployment)
* [medium: Kubernetes Deployment Explained](https://medium.com/geekculture/kubernetes-deployment-explained-9b2b89dd3977) Learn what is Deployment in the Kubernetes cluster and learn the advantages of the Deployment object.
* [redhat.com: 10 considerations for Kubernetes deployments - Checklist](https://www.redhat.com/en/engage/considerations-kubernetes-deployments-s-202001101221)
* [learnk8s.io: Graceful shutdown and zero downtime deployments in Kubernetes](https://learnk8s.io/graceful-shutdown)
* [thoughtbot.com: Zero Downtime Rails Deployments with Kubernetes](https://thoughtbot.com/blog/zero-downtime-rails-deployments-with-kubernetes)
* [medium: Deployment types in Kubernetes](https://medium.com/avmconsulting-blog/deployment-types-in-kubernetes-14b70ca7ef93)
* [hackernoon.com: How To Deploy Code Faster Using Kubernetes](https://hackernoon.com/how-to-deploy-code-faster-using-kubernetes-jh1y3ul0)
* [fosstechnix.com: Rolling out and Rolling back updates with Zero Downtime on Kubernetes Cluster](https://www.fosstechnix.com/rolling-out-and-rolling-back-updates-with-zero-downtime-on-kubernetes-cluster/)
* [medium: 5 Things We Overlooked When Deploying Our First App on Kubernetes](https://medium.com/gumgum-tech/5-things-we-overlooked-when-putting-our-first-app-on-kubernetes-58583c1783e4)
* [Our Journey to Zero Downtime Rolling Updates with Ambassador](https://eng.lifion.com/journey-to-zero-downtime-rolling-updates-with-ambassador-badda6a7d450) In this article you will cover: How Kubernetes lifecycle hooks can be used to shutdown applications gracefully. How pods are removed from the system and why it is necessary to understand and carefully handle the shutdown sequence appropriately.
* [medium: Kubernetes Tip: How Statefulsets Behave Differently Than Deployments When Node Fails?](https://medium.com/tailwinds-navigator/kubernetes-tip-how-statefulsets-behave-differently-than-deployments-when-node-fails-d29e36bca7d5) What happens to the Pods when a node fails in Kubernetes?
* [learnsteps.com: Basics on Kubernetes: What exactly is a deployment?](https://www.learnsteps.com/basics-on-kubernetes-what-exactly-is-a-deployment/)
* [polarsquad.com: Check your Kubernetes deployments!](https://polarsquad.com/blog/check-your-kubernetes-deployments)
* [yankeexe.medium.com: How Rolling and Rollback Deployments work in Kubernetes](https://yankeexe.medium.com/how-rolling-and-rollback-deployments-work-in-kubernetes-8db4c4dce599)

#### Kubernetes StatefulSet
* [medium: Kubernetes — Difference between Deployment and StatefulSet in K8s](https://medium.com/devops-mojo/kubernetes-difference-between-deployment-and-statefulset-in-k8s-deployments-vs-statefulsets-855f9e897091)
* [kubermatic.com: Keeping the State of Apps 6: Introduction to StatefulSets](https://www.kubermatic.com/blog/keeping-the-state-of-apps-5/)
* [loft.sh: Kubernetes StatefulSet - Examples & Best Practices](https://loft.sh/blog/kubernetes-statefulset-examples-and-best-practices/)
    * [loft-sh.medium.com: Kubernetes StatefulSet — Examples & Best Practices](https://loft-sh.medium.com/kubernetes-statefulset-examples-best-practices-902cd50f7fff)

#### Kubernetes Jobs and Cron Jobs
* [ithands-on.com: Kubernetes 101 : Performing tasks in kubernetes - Jobs](https://www.ithands-on.com/2021/05/kubernetes-101-performing-tasks-in.html)
* [How we learned to improve Kubernetes CronJobs at Scale (Part 1 of 2)](https://eng.lyft.com/improving-kubernetes-cronjobs-at-scale-part-1-cf1479df98d4)
    * [How we learned to improve Kubernetes CronJobs at Scale (Part 2 of 2)](https://eng.lyft.com/how-we-learned-to-improve-kubernetes-cronjobs-at-scale-part-2-of-2-dad0c973ffca)
* [opensource.com: A beginner's guide to Kubernetes Jobs and CronJobs](https://opensource.com/article/20/11/kubernetes-jobs-cronjobs) Use Jobs and CronJobs to control and manage Kubernetes pods and containers.
* [medium: Jobs & Cronjobs in Kubernetes Cluster](https://medium.com/avmconsulting-blog/jobs-cronjobs-in-kubernetes-cluster-d0e872e3c8c8)
* [devopscube.com: How To Create Kubernetes Jobs/Cron Jobs – Getting Started Guide](https://devopscube.com/create-kubernetes-jobs-cron-jobs/)
* [containiq.com: Kubernetes Jobs | Use Cases, Scheduling, and Failure](https://www.containiq.com/post/kubernetes-jobs) Learn more about Kubernetes best practices and job cases. This article will even teach you how to create kubernetes jobs and how to handle failures.
* [medium.com/geekculture: Setup a CronJob to execute Kubectl or AWS commands](https://medium.com/geekculture/setup-a-cronjob-to-execute-kubectl-or-aws-commands-c1c15dd4ff1f) Kubernetes Tricks | AWS CLI | CronJob | Secrets | Backup Databases | Postgres Backup in Kubernetes

### Kubernetes Deployment Strategies
- [youtube: deployment strategies in kubernetes | recreate | rolling update | blue/green | canary](https://youtu.be/efiMiaFjtn8)
- [auth0.com: Deployment Strategies In Kubernetes](https://auth0.com/blog/deployment-strategies-in-kubernetes) Learn what are the different deployment strategies available in Kubernetes and how to use them.
- [educative.io: A deep dive into Kubernetes Deployment strategies](https://www.educative.io/blog/kubernetes-deployments-strategies)
- [weave.works: Kubernetes Deployment Strategies 🌟](https://www.weave.works/blog/kubernetes-deployment-strategies)
- [sivalabs.in: Kubernetes - Blue/Green Deployments](https://www.sivalabs.in/2021/09/kubernetes-blue-green-deployments/)
- [medium.com: Kubernetes Canary Deployment #1 Gitlab CI](https://medium.com/@wuestkamp/kubernetes-canary-deployment-1-gitlab-ci-518f9fdaa7ed)
- [semaphoreci.com: Continuous Blue-Green Deployments With Kubernetes](https://semaphoreci.com/blog/continuous-blue-green-deployments-with-kubernetes)
- [medium: Fully automated canary deployments in Kubernetes](https://medium.com/containers-101/fully-automated-canary-deployments-in-kubernetes-70a671105273)
- [auth0.com: Deployment Strategies In Kubernetes](https://auth0.com/blog/deployment-strategies-in-kubernetes/) Learn what are the different deployment strategies available in Kubernetes and how to use them.

### Kubernetes API
- [kubernetes.io: Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/)
- [thenewstack.io: Living with Kubernetes: API Lifecycles and You](https://thenewstack.io/living-with-kubernetes-api-lifecycles-and-you/)
- [blog.tilt.dev: Kubernetes is so Simple You Can Explore it with Curl](https://blog.tilt.dev/2021/03/18/kubernetes-is-so-simple.html)
- [learndevops.substack.com: Hitting prometheus API with curl and jq 🌟](https://learndevops.substack.com/p/hitting-prometheus-api-with-curl) Determine offending pods that use more RAM than requested, causing OOM, with Prometheus and jq.
- [thenewstack.io: Kubernetes Is Not Just About Containers — It’s About the API 🌟](https://thenewstack.io/kubernetes-is-not-just-about-containers-its-about-the-api/)
- [kubernetes.io: Alpha in Kubernetes v1.22: API Server Tracing](https://kubernetes.io/blog/2021/09/03/api-server-tracing/)
- [evancordell.com: 16 things you didn't know about Kube APIs and CRDs](https://evancordell.com/posts/kube-apis-crds/)
- [martinheinz.dev: Could Kubernetes Pods Ever Become Deprecated? 🌟](https://martinheinz.dev/blog/53) **Could a core object or API in Kubernetes, such as Pod, Deployment or Service be removed and if so, how would that go?**
- [trstringer.com: Discover Kubernetes API Calls from kubectl](https://trstringer.com/kubernetes-api-call-from-kubectl/)
- [==iximiuz.com: Working with Kubernetes API - Resources, Kinds, and Objects==](https://iximiuz.com/en/posts/kubernetes-api-structure-and-terminology)
- [==iximiuz.com: How To Call Kubernetes API using Simple HTTP Client==](https://iximiuz.com/en/posts/kubernetes-api-call-simple-http-client/) 
    - How to get the API server address
    - How to authenticate API server to clients
    - How to authenticate clients to API server
    - How to call Kubernetes API from Pods
    - CRUD operations on resources with cURL
    - And more!

#### Multi-Cluster Services API
- [thenewstack.io: Extending Kubernetes Services with Multi-Cluster Services API](https://thenewstack.io/extending-kubernetes-services-with-multi-cluster-services-api/)
- [kubernetes.io: Introducing ClusterClass and Managed Topologies in Cluster API](https://kubernetes.io/blog/2021/10/08/capi-clusterclass-and-managed-topologies/) The Cluster API community is happy to announce the implementation of ClusterClass and Managed Topologies, a new feature that will greatly simplify how you can provision, upgrade, and operate multiple Kubernetes clusters in a declarative way.

### Kubernetes Health Checks/Probes. Startup, Liveness, Readiness
* [medium: How to Perform Health checks in Kubernetes (K8s)](https://medium.com/faun/how-to-perform-health-checks-in-kubernetes-k8s-a4e5300b1f9d)
* [If you have a livenessProbe that takes over one second, it’ll fail when you update to kubernetes 1.20, because a long-standing bug with how the default was handled has been fixed. You must override the ExecProbeTimeout if your probe takes more than 1s](https://github.com/kubernetes/kubernetes/pull/97057)
* [Liveness and Readiness Probes for Kubernetes in Phoenix application](https://blog.lelonek.me/liveness-and-readiness-probes-for-kubernetes-in-phoenix-application-890e24d0737e)
* [Kubernetes Liveness and Readiness Probes](https://theithollow.com/2020/05/18/kubernetes-liveness-and-readiness-probes/)
* [loft.sh: Kubernetes Readiness Probes - Examples & Common Pitfalls](https://loft.sh/blog/kubernetes-readiness-probes-examples-common-pitfalls/)
* [millionvisit.blogspot.com: Kubernetes for Developers #12: Effective way of using K8 Liveness Probe](http://millionvisit.blogspot.com/2021/04/kubernetes-for-developers-12-effective-way-of-using-k8-liveness-probe.html)
* [millionvisit.blogspot.com: Kubernetes for Developers #13: Effective way of using K8 Readiness Probe](http://millionvisit.blogspot.com/2021/04/kubernetes-for-developers-13-effective-way-of-using-k8-readiness-probe.html)
* [andrewlock.net: Deploying ASP.NET Core applications to Kubernetes - Part 6 - Adding health checks with Liveness, Readiness, and Startup probes](https://andrewlock.net/deploying-asp-net-core-applications-to-kubernetes-part-6-adding-health-checks-with-liveness-readiness-and-startup-probes/)
* [itnext.io: Kubernetes Probes: Startup, Liveness, Readiness](https://itnext.io/kubernetes-probes-startup-liveness-readiness-a9fc9ccff4b2)
* [itnext.io: Kubernetes Readiness Probes — Examples & Common Pitfalls](https://itnext.io/kubernetes-readiness-probes-examples-common-pitfalls-136e3a9a058d)
* [youtube: Kubernetes 101: Get Better Uptime with K8s Health Checks](https://www.youtube.com/watch?v=D9w3DH1zAc8)
* [returngis.net: Pruebas de vida de nuestros contenedores en Kubernetes](https://www.returngis.net/2020/02/pruebas-de-vida-de-nuestros-contenedores-en-kubernetes/)
* [blog.newrelic.com: Kubernetes Fundamentals, Part 2: How to Use Health Checks](https://blog.newrelic.com/engineering/kubernetes-health-checks)
* [komodor.com: Kubernetes Liveness Probes: A Practical Guide](https://komodor.com/learn/kubernetes-liveness-probes-a-practical-guide/)

### Kubernetes Limits and Requests
* [kubernetes.io Policy Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
* [sysdig.com: Understanding Kubernetes limits and requests by example](https://sysdig.com/blog/kubernetes-limits-requests/)
* [dev.to/aurelievache: Understanding Kubernetes: part 22 – LimitRange](https://dev.to/aurelievache/understanding-kubernetes-part-22-limitrange-144l)
* [dzone: Dive Deep Into Resource Requests and Limits in Kubernetes](https://dzone.com/articles/dive-deep-into-resource-requests-and-limits-in-kub) This article will be helpful for you to understand how Kubernetes requests and limits work, and why they can work in an expected way.
* [sysdig.com: How to rightsize the Kubernetes resource limits](https://sysdig.com/blog/kubernetes-resource-limits/)
* [medium: Understanding resource limits in kubernetes: cpu time](https://medium.com/@betz.mark/understanding-resource-limits-in-kubernetes-cpu-time-9eff74d3161b)
* [blog.newrelic.com: Kubernetes Fundamentals, Part 1: How to Manage Cluster Capacity with Requests and Limits](https://blog.newrelic.com/engineering/kubernetes-request-and-limits)
* [john-tucker.medium.com: Kubernetes CPU Resource Requests at Runtime](https://john-tucker.medium.com/kubernetes-cpu-resource-requests-at-runtime-c4df668d1c5c) While it is well documented how CPU resource request impact the scheduling of Pods to Nodes, it is less clear of the impact once Pods (and their Containers) are running on a Node.
* [faun.pub: Practical example of how to set requests and limits on Kubernetes](https://faun.pub/practical-example-of-how-to-set-requests-and-limits-on-kubernetes-87521b599983)

### Kube Scheduler
- [All you need to know to get started with the Kube Scheduler](https://gist.github.com/luisalfonsopreciado/40a0fc2319241d517832affdce2bc1ff)
- [medium: K8S - Creating a kube-scheduler plugin](https://medium.com/@juliorenner123/k8s-creating-a-kube-scheduler-plugin-8a826c486a1) The k8s scheduler assigns Pods to Nodes. Then, the attempt to schedule a pod is split into two phases: the Scheduling and the Binding cycle. Learn how you can build a Kube-scheduler plugin from scratch!

### Kubernetes etcd
- [medium: How to modify etcd data of your Kubernetes directly (without K8s API)](https://medium.com/flant-com/modifying-kubernetes-etcd-data-ed3d4bb42379)
- [medium: Getting Started with Kubernetes etcd](https://medium.com/@Alibaba_Cloud/getting-started-with-kubernetes-etcd-a26cba0b4258)
- [sysdig.com: How to monitor etcd](https://sysdig.com/blog/monitor-etcd/) Learning how to monitor etcd is of vital importance when running Kubernetes in production. Monitoring etcd will let you validate that things work as expected, while detecting and troubleshooting issues that could take your entire infrastructure down.
- [learnk8s.io: How etcd works with and without Kubernetes](https://learnk8s.io/etcd-kubernetes)
- [itnext.io: Breaking down and fixing etcd cluster](https://itnext.io/breaking-down-and-fixing-etcd-cluster-d81e35b9260d)
- [medium: ETCD - the Easy Way | Vaibhav Rajput](https://medium.com/nerd-for-tech/etcd-the-easy-way-4c01e243f285) This is a guide which will help you get started with etcd and help you understand how it is used in a kubernetes setup.

### Kubernetes Sidecars
* [bsucaciu.com: What is a Sidecar?](https://bsucaciu.com/?p=4645)
* [medium: Kubernetes — Learn Sidecar Container Pattern](https://medium.com/bb-tutorials-and-thoughts/kubernetes-learn-sidecar-container-pattern-6d8c21f873d) Understanding Sidecar Container Pattern With an Example Project
* [ithands-on.com: Kubernetes 101 : Extending the container's functionalities - Sidecar containers](https://www.ithands-on.com/2021/07/kubernetes-101-extending-containers.html)

### Kubernetes Annotations
* [kubernetes.io: Annotating Kubernetes Services for Humans](https://kubernetes.io/blog/2021/04/20/annotating-k8s-for-humans/) A Convention for annotations in Kubernetes.

### Kubernetes Best Practices and Tips
* [==diegolnasc/kubernetes-best-practices== 🌟](https://github.com/diegolnasc/kubernetes-best-practices) A cookbook with the best practices to working with kubernetes.
* [blog.pipetail.io: 10 most common mistakes using kubernetes](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)
* [**Optimize** Kubernetes cluster management with these 5 tips](https://searchitoperations.techtarget.com/feature/Optimize-Kubernetes-cluster-management-with-these-5-tips) Effective Kubernetes cluster management requires operations teams to balance pod and node deployments with performance and availability needs.
* [techradar.com: Three tips to implement Kubernetes with open standards](https://www.techradar.com/news/three-tips-to-implement-kubernetes-with-open-standards)
* [10 most common mistakes when using Kubernetes](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)
    * resources - requests and limits
    * liveness and readiness probes
    * LoadBalancer for every http service
    * non-kubernetes-aware cluster autoscaling
    * Not using the power of IAM/RBAC
* [geekflare.com: 10 Kubernetes Best Practices for Better Container Orchestration](https://geekflare.com/kubernetes-best-practices/)
* [wideops.com: Kubernetes best practices: Setting up health checks with readiness and liveness probes](https://wideops.com/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes/)
* [containerjournal.com: 10 Best Practices Worth Implementing to Adopt Kubernetes](https://containerjournal.com/topics/container-management/10-best-practices-worth-implementing-to-adopt-kubernetes/)
* [medium: Kubernetes Tip: How Does OOMKilled Work?](https://medium.com/tailwinds-navigator/kubernetes-tip-how-does-oomkilled-work-ba71b135993b)
* [cloud.google.com: Kubernetes Best Practices](https://cloud.google.com/blog/topics/kubernetes-best-practices) A collection of blog posts aimed at guide you through the Kubernetes best practices
* [releasehub.com: Kubernetes Health Checks - 2 Ways to Improve Stability in Your Production Applications](https://releasehub.com/blog/kubernetes-health-checks-2-ways-to-improve-stability)
* [stackpulse.com: Kubernetes and SRE: 5 Best Practices for K8s Reliability in Production](https://stackpulse.com/blog/https-stackpulse-com-blog-kubernetes-production-best-practices/)
* [fairwinds.com: Never Should You Ever In Kubernetes: #1 Do K8S The Hard Way](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-1-do-k8s-the-hard-way)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 2: Kubernetes Security Mistakes](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-part-2-kubernetes-security-mistakes)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 3: 6 K8s Reliability Mistakes](https://www.fairwinds.com/blog/6-kubernetes-reliability-mistakes)
* [fairwinds.com: Never Should You Ever In Kubernetes Part 4: Three K8s Efficiency Mistakes](https://www.fairwinds.com/blog/3-kubernetes-efficiency-mistakes)
* [stackpulse.com: Challenges of Running Services With K8s Reliably](https://stackpulse.com/blog/challenges-of-running-services-with-k8s-reliably/)
* [blog.lukechannings.com: Mistakes made and lessons learned with Kubernetes and GitOps](https://blog.lukechannings.com/2020-05-10-kubernetes-gitops-lessons.html)
* [fairwinds.com: An Intro to Kubernetes Best Practices: Start Your K8s Right](https://www.fairwinds.com/blog/intro-kubernetes-best-practices)
* [itnext.io: Lifecycle of Kubernetes Network Policies and Best Practices](https://itnext.io/lifecycle-of-kubernetes-network-policies-749b5218f684) In this blog post, you'll learn the lifecycle of Kubernetes Network Policies (e.g. creation, editing, governance, debugging)
* [==learnk8s.io: Kubernetes production best practices==](https://learnk8s.io/production-best-practices) A curated checklist of best practices designed to help you release to production.
* [github.com/PacktPublishing: Kubernetes in Production Best Practices](https://github.com/PacktPublishing/Kubernetes-in-Production-Best-Practices)
* [medium: 10 Most Common Mistakes When Using Kubernetes](https://medium.com/devops-dudes/10-most-common-mistakes-when-using-kubernetes-8a07abb8e850) Avoid your cluster from falling over in production by implementing these best practices
* [thenewstack.io: 5 Best Practices for Configuring Kubernetes Pods Running in Production](https://thenewstack.io/5-best-practices-for-configuring-kubernetes-pods-running-in-production/)
* [containiq.com: Setting and Rightsizing Kubernetes Resource Limits | Best Practices](https://www.containiq.com/post/setting-and-rightsizing-kubernetes-resource-limits) Part of managing a Kubernetes cluster is making sure your clusters aren’t using too many resources. Let’s walk through the concepts of setting and rightsizing resource limits for Kubernetes.
* [freecodecamp.org: How to Make Your Enterprise Kubernetes Environment Secure, Efficient, and Reliable](https://www.freecodecamp.org/news/make-your-kubernetes-environment-secure-efficient-reliable/)
* [geekflare.com: Diez mejores prácticas de Kubernetes para una mejor orquestación de contenedores](https://geekflare.com/es/kubernetes-best-practices/)
* [containerjournal.com: 4 Expert-Level Things I Wish I’d Known About Kubernetes](https://containerjournal.com/features/4-expert-level-things-i-wish-id-known-about-kubernetes/)
* [dev.to: Prevent Configuration Errors in Kubernetes](https://dev.to/solegaonkar/prevent-configuration-errors-in-kubernetes-30dn)
* [komodor.com: Four Best Practices to Migrate to Kubernetes (Part 1)](https://komodor.com/blog/best-practices-to-migrate-to-kubernetes/)
    * [komodor.com: Five Kubernetes Deployment Best Practices (Part 2) 🌟](https://komodor.com/blog/5-kubernetes-deployment-best-practices)
        1. Maintaining Good YAML Hygiene (AKA Your K8s Deployment Manifest)
        2. Stateless Apps FTW!
        3. Logging, but Specifically for Kubernetes
        4. Separation of Environments
        5. Invest in Proper Monitoring
* [bridgecrew.io: 5 common Kubernetes misconfigs and how to fix them](https://bridgecrew.io/blog/5-common-kubernetes-misconfigs-and-how-to-fix-them/)
* [snapt.net: Best Practices for Load Balancing Kubernetes Containers](https://www.snapt.net/blog/best-practices-for-load-balancing-kubernetes-containers)
* [==vladimir.varank.in: Making sense of requests for CPU resources in Kubernetes== 🌟](https://vladimir.varank.in/notes/2021/09/making-sense-of-requests-for-cpu-resources-in-kubernetes/)

<center>
[![k8s experts be like](images/k8sexpertsbelike.jfif){: style="width:50%"}](https://twitter.com/memenetes)
</center>

### Disruptions
- [thenewstack.io: Kubernetes: Use PodDisruptionBudgets for Application Maintenance and Upgrades](https://thenewstack.io/kubernetes-use-poddisruptionbudgets-for-application-maintenance-and-upgrades/)

### Cost Estimation Strategies
- [cncf.io: 5 Problems with Kubernetes Cost Estimation Strategies](https://www.cncf.io/blog/2020/09/18/5-problems-with-kubernetes-cost-estimation-strategies)
- [loft.sh: How To Reduce Your Kubernetes Cost](https://loft.sh/blog/reduce-kubernetes-cost/)
- [harness.io: Getting Started with Cloud Cost Optimization](https://harness.io/2020/09/getting-started-with-cloud-cost-optimization/)
- [rancher.com: Gain Better Visibility into Kubernetes Cost Allocation](https://rancher.com/blog/2020/gain-better-visibility-kubernetes-cost-allocation)
- [loft.sh: Kubernetes Cost Savings By Reducing The Number Of Clusters](https://loft.sh/blog/kubernetes-cost-savings/)
- [thenewstack.io: 5 Essential Tips to Manage Kubernetes Costs](https://thenewstack.io/5-essential-tips-to-manage-kubernetes-costs/)
- [opensource.com: 3 ways Kubernetes optimizes your IT budget](https://opensource.com/article/20/12/it-budget-kubernetes) Automation is not only good for IT, it's also beneficial to your company's bottom line.
- [thenewstack.io: 5 Expensive Kubernetes Cost Traps and How to Deal with Them](https://thenewstack.io/5-expensive-kubernetes-cost-traps-and-how-to-deal-with-them/)
- [KubeSurvival](https://github.com/aporia-ai/kubesurvival) Significantly reduce Kubernetes costs by finding the cheapest machine types that can run your workloads
- [containerjournal.com: Assessing the True Cost of Kubernetes](https://containerjournal.com/features/assessing-the-true-cost-of-kubernetes/)
- [ubuntu.com: Kubernetes Fully Managed – half the cost of AWS](https://ubuntu.com/blog/managed-kubernetes-cheaper-than-aws)
- [learnk8s.io: Kubernetes Instance Calculator 🌟🌟](https://learnk8s.io/kubernetes-instance-calculator)
- [dev.to: Kubernetes Cost Management and Analysis Guide 🌟](https://dev.to/cloudforecast/kubernetes-cost-management-and-analysis-guide-1e1b)

#### kubecost
- [==Kubecost== 🌟](https://www.kubecost.com) 
- [How to track costs in multi-tenant Amazon EKS clusters using Kubecost](https://aws.amazon.com/blogs/containers/how-to-track-costs-in-multi-tenant-amazon-eks-clusters-using-kubecost/)
- [infracloud.io: Kubernetes Cost Reporting using Kubecost](https://www.infracloud.io/blogs/kubernetes-cost-reporting-using-kubecost/)
- [github.com/kubecost: kubecost-exporter - Running Kubecost as a Prometheus metric exporter](https://github.com/kubecost/cost-model/blob/develop/kubecost-exporter.md)
- [blog.kubecost.com: Kubecost raises $5.5 million to help teams monitor and reduce their Kubernetes spend](http://blog.kubecost.com/blog/announcing-kubecost-first-round/)
- [kubectl-cost](https://github.com/kubecost/kubectl-cost) is a kubectl plugin that provides easy CLI access to Kubernetes cost allocation metrics via the kubecost APIs. It allows developers, devops, and others to quickly determine the cost & efficiency for any Kubernetes workload
- [blog.kubecost.com: AKS Cost Monitoring and Governance With Kubecost](https://blog.kubecost.com/blog/aks-cost/)
- [thenewstack.io: KubeCost: Monitor Kubernetes Costs with kubectl](https://thenewstack.io/kubecost-monitor-kubernetes-costs-with-kubectl/)

### Kubernetes Resource and Capacity Management. Capacity Planning
* [itnext.io: Kubernetes Resource Management in Production](https://itnext.io/kubernetes-resource-management-in-production-d5382c904ed1) Requests, Limits, Overcommitment, Slack/Waste, Throttling
* [medium: Ultimate Kubernetes Resource Planning Guide](https://medium.com/dev-genius/ultimate-kubernetes-resource-planning-guide-449a4fddd1d6)
* [learnk8s.io: Setting the right requests and limits in Kubernetes 🌟](https://learnk8s.io/setting-cpu-memory-limits-requests) By far the best read on requests and limits in Kubernetes.
* [openshift.com: Sizing Applications in Kubernetes](https://www.openshift.com/blog/sizing-applications-in-kubernetes)
* [magalix.com: Capacity Planning](https://www.magalix.com/blog/kubernetes-patterns-capacity-planning) When we have multiple Pods with different Priority Class values, the admission controller starts by sorting Pods according to their priority. What happens when there are no nodes with available resources to schedule a high-priority pods? 
* [sysdig.com: Kubernetes capacity planning: How to rightsize the requests of your cluster](https://sysdig.com/blog/kubernetes-capacity-planning/)
 
### Architecting Kubernetes clusters. Node Size. Multi Clusters and Hybrid Cloud
* [learnk8s.io: Architecting Kubernetes clusters — how many should you have?](https://learnk8s.io/how-many-clusters)
* [learnk8s.io: Architecting Kubernetes clusters — choosing a worker node size](https://learnk8s.io/kubernetes-node-size) This article discusses the pros and cons of having either many small clusters or few large clusters for running a given set of apps.
    * [itnext.io: Architecting Kubernetes clusters — choosing a worker node size](https://itnext.io/architecting-kubernetes-clusters-choosing-a-worker-node-size-b3729cc0c78f)
* [itnext.io: Architecting Kubernetes clusters — choosing a cluster size](https://itnext.io/architecting-kubernetes-clusters-choosing-a-cluster-size-92f6feaa2908) 
* [learnk8s.io: Allocatable memory and CPU in Kubernetes Nodes](https://learnk8s.io/allocatable-resources)
* [docs.google.com - learnk8s.io: Research on the trade offs when choosing an instance type for a kubernetes cluster](https://docs.google.com/spreadsheets/d/1yhkuBJBY2iO2Ax5FcbDMdWD5QLTVO6Y_kYt_VumnEtI/edit#gid=1994017257)
* [medium: Deploying Kubernetes — Deciding the size of your nodes](https://medium.com/swlh/deploying-kubernetes-deciding-the-size-of-your-nodes-a115e770e09)
* [dzone refcard: Kubernetes Multi-Cluster Management and Governance](https://dzone.com/refcardz/kubernetes-multi-cluster-management-and-governance)
* [thenewstack.io: A Deep Dive into Architecting a Kubernetes Infrastructure](https://thenewstack.io/a-deep-dive-into-architecting-a-kubernetes-infrastructure/)
* [thenewstack.io: Manage Multicluster Kubernetes with Operators](https://thenewstack.io/manage-multicluster-kubernetes-with-operators/)
* [kubernetes.io: Out of the Clouds onto the Ground: How to Make Kubernetes Production Grade Anywhere](https://kubernetes.io/blog/2018/08/03/out-of-the-clouds-onto-the-ground-how-to-make-kubernetes-production-grade-anywhere/)
* [cncf.io: Simplifying multi-clusters in Kubernetes](https://www.cncf.io/blog/2021/04/12/simplifying-multi-clusters-in-kubernetes/)
* [platform9.com: Difference Between multi-cluster, multi-master, multi-tenant & federated Kubernetes](https://platform9.com/blog/difference-between-multi-cluster-multi-master-multi-tenant-federated-kubernetes/)
* [datacenterknowledge.com: The Pros and Cons of Kubernetes-Based Hybrid Cloud](https://www.datacenterknowledge.com/cloud/pros-and-cons-kubernetes-based-hybrid-cloud) 
* [thenewstack.io: 4 ways to run kubernetes in production](https://thenewstack.io/4-ways-to-run-kubernetes-in-production/)
* [medium: Individual Kubernetes Clusters vs. Shared Kubernetes Clusters for Development](https://medium.com/faun/individual-kubernetes-clusters-vs-shared-kubernetes-clusters-for-development-3399576b0f1f)
* [nginx.com: Reduce Complexity with Production-Grade Kubernetes](https://www.nginx.com/blog/reduce-complexity-with-production-grade-kubernetes/)
* [elastisys.com: What do I need to add on top of Kubernetes?](https://elastisys.com/what-do-i-need-to-add-on-top-of-kubernetes/)
* [platform9.com: Kubernetes Cluster Sizing – How Large Should a Kubernetes Cluster Be?](https://platform9.com/blog/kubernetes-cluster-sizing-how-large-should-a-kubernetes-cluster-be/)
* [==redhat.com: 3 questions to answer when considering a multi-cluster Kubernetes architecture==](https://www.redhat.com/architect/multi-cluster-kubernetes-architecture) A multi-cluster Kubernetes architecture is complex, but its versatility and resiliency make the tradeoffs worthwhile for large-scale enterprise applications.

#### Wide Cluster instead of Multi-Cluster
- [itnext.io: 3 Reasons to Choose a Wide Cluster over Multi-Cluster with Kubernetes](https://itnext.io/3-reasons-to-choose-a-wide-cluster-over-multi-cluster-with-kubernetes-c923fecf4644)

## Client Libraries for Kubernetes
- [Client Libraries for Kubernetes](kubernetes-client-libraries.md)

## Helm Kubernetes Tool
- [Helm](helm.md)

## Templating YAML in Kubernetes with real code. YQ YAML processor
- [Templating YAML in Kubernetes with real code](https://learnk8s.io/templating-yaml-with-code)
    - TL;DR: You should use tools such as [yq](https://mikefarah.gitbook.io/yq/) and kustomize to template YAML resources instead of relying on tools that interpolate strings such as [Helm](https://helm.sh/). 
    - If you're working on large scale projects, you should consider using **real code** — you can find [hands-on examples on how to programmatically generate Kubernetes resources in Java, Go, Javascript, C# and Python in this repository](https://github.com/learnk8s/templating-kubernetes).

## Extending Kubernetes
### Adding Custom Resources. Extending Kubernetes API with Kubernetes Resource Definitions. CRD vs Aggregated API
- [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [itnext.io: CRD is just a table in Kubernetes](https://itnext.io/crd-is-just-a-table-in-kubernetes-13e15367bbe4)
- Use a custom resource (CRD or Aggregated API) if most of the following apply:
    - You want to use Kubernetes client libraries and CLIs to create and update the new resource.
    - You want top-level support from kubectl; for example, kubectl get my-object object-name.
    - You want to build new automation that watches for updates on the new object, and then CRUD other objects, or vice versa.
    - You want to write automation that handles updates to the object.
    - You want to use Kubernetes API conventions like .spec, .status, and .metadata.
    - You want the object to be an abstraction over a collection of controlled resources, or a summarization of other resources.
- Kubernetes provides two ways to add custom resources to your cluster:
    - CRDs are simple and can be created without any programming.
    - API Aggregation requires programming, but allows more control over API behaviors like how data is stored and conversion between API versions.
- Kubernetes provides these two options to meet the needs of different users, so that neither ease of use nor flexibility is compromised.
- Aggregated APIs are subordinate API servers that sit behind the primary API server, which acts as a proxy. This arrangement is called API Aggregation (AA). To users, it simply appears that the Kubernetes API is extended.
- CRDs allow users to create new types of resources without adding another API server. You do not need to understand API Aggregation to use CRDs.
- Regardless of how they are installed, the new resources are referred to as Custom Resources to distinguish them from built-in Kubernetes resources (like pods).

### Krew, a plugin manager for kubectl plugins
* [Krew](https://krew.sigs.k8s.io/) is the plugin manager for kubectl command-line tool.
* [itnext.io: Extending Kubernetes Cluster; Kubectl Plugins and Krew](https://itnext.io/extending-kubernetes-cluster-kubectl-plugins-and-krew-547a8bc839a3)
* [darumatic.com: Improve Kubectl Command with Krew](https://darumatic.com/blog/improve_kubectl_command_with_krew) Krew is a tool that aims to ease plugin discovery, installation, upgrade, and removal on multiple operating systems. This article will show you how easy it is to grab and experiment with existing plugins.
* kubectl trace is now on the krew index!! Go install it now!
    ```bash
    kubectl krew install trace
    ```
    And then just try to snoop into all the file openings:

    ```bash
    kubectl trace run -a  <yournode>  -e 'kprobe:do_sys_open { printf("%s: %s\n", comm, str(arg1)) }'
    ```

### OpenKruise/Kruise
- [openkruise.io](https://openkruise.io/)
- [OpenKruise/Kruise](https://github.com/openkruise/kruise)
- [thenewstack.io: Introducing CloneSet: A Production-Grade Kubernetes Deployment CRD](https://thenewstack.io/introducing-cloneset-production-grade-kubernetes-deployment-crd/)

###  Crossplane, a Universal Control Plane API for Cloud Computing. Crossplane Workloads Definitions
- [Crossplane](crossplane.md)

## Kubernetes Community
### Community Forums
- [Community Forums 🌟](https://discuss.kubernetes.io/)

### Kubernetes Special Interest Groups (SIGs)
- [Kubernetes Special Interest Groups (SIGs)](https://github.com/kubernetes/community/blob/master/README.md#special-interest-groups-sig) have been around to support the community of developers and operators since around the 1.0 release. People organized around networking, storage, scaling and other operational areas.
- [SIG Apps: build apps for and operate them in Kubernetes](https://kubernetes.io/blog/2016/08/sig-apps-running-apps-in-kubernetes/)

#### Kubernetes SIG's Repos
- [Kubernetes SIGs](https://github.com/kubernetes-sigs) Org for Kubernetes SIG-related work.
- [ExternalDNS: Configure external DNS servers (AWS Route53, Google CloudDNS and others) for Kubernetes Ingresses and Services](https://github.com/kubernetes-sigs/external-dns)
- [Kubernetes-Secrets-Store-CSI-Driver: Secrets Store CSI driver for Kubernetes secrets](https://github.com/kubernetes-sigs/secrets-store-csi-driver) Integrates secrets stores with Kubernetes via a CSI volume.
- [kustomize](https://github.com/kubernetes-sigs/kustomize) Customization of kubernetes YAML configurations.

#### Kubectl Plugins 
* [Available kubectl plugins](https://github.com/kubernetes-sigs/krew-index/blob/master/plugins.md)
* [Awesome Kubectl plugins](https://github.com/ishantanu/awesome-kubectl-plugins)
* [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
* [youtube: Welcome to the world of kubectl plugins](https://www.youtube.com/watch?v=_W2qZvQT6XY)
* [padok.fr: Getting started with kubectl plugins](https://www.padok.fr/en/blog/kubectl-plugins) 5 useful kubectl plugins:
    * whoami
    * access-matrix
    * neat
    * tree
    * node-shell
* [kubectl-trace](https://github.com/iovisor/kubectl-trace) kubectl trace is a kubectl plugin that allows you to schedule the execution of bpftrace programs in your Kubernetes cluster.
* [pixelstech.net: Build a Kubectl Plugin from Scratch](https://www.pixelstech.net/article/1606901393-Build-a-Kubectl-Plugin-from-Scratch)
* [k8scr](https://github.com/hasheddan/k8scr) A kubectl plugin for pushing OCI images through the Kubernetes API server.
* [martinheinz.dev: Making Kubernetes Operations Easy with kubectl Plugins](https://martinheinz.dev/blog/58)
* [kei6u/kubectl-secret-data](https://github.com/kei6u/kubectl-secret-data) A kubectl plugin for finding decoded secret data with productive search flags.
* [medium: Cool Kubernetes command line plugins](https://medium.com/nontechcompany/cool-kubernetes-command-line-plugins-4b0e50362426)

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_W2qZvQT6XY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
<br/>

## Enforcing Policies and governance for kubernetes workloads with Conftest
* [Accelerated Feedback Loops when Developing for Kubernetes with Conftest](https://engineering.plex.com/posts/kubernetes-policy-conftest) Learn how to validate Kubernetes resources with Conftest for faster feedback loops
    * [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest)
    * [Enforcing policies and governance for Kubernetes workloads](https://learnk8s.io/kubernetes-policies)
* [Deprek8ion](https://github.com/swade1987/deprek8ion) is a set of rego policies to monitor Kubernetes APIs deprecations and designed to work with conftest.
* [k8s-worker-pod-autoscaler](https://github.com/practo/k8s-worker-pod-autoscaler) scales the replicas in a deployment based on observed queue length.
* [kubectl-prune / kubectl-reap](https://github.com/micnncim/kubectl-reap) is a kubectl plugin that prunes unused Kubernetes resources.
* [kconnect - The Kubernetes Connection Manager CLI](https://github.com/fidelity/kconnect) kconnect is a CLI utility that can be used to discover and securely access Kubernetes clusters across multiple operating environments. Based on the authentication mechanism chosen the CLI will discover Kubernetes clusters you are allowed to access in a target hosting environment (i.e. EKS, AKS, Rancher) and generate a kubeconfig for a chosen cluster.
* [konstraint](https://github.com/plexsystems/konstraint) is a CLI tool to assist with the creation and management of templates and constraints when using [Gatekeeper](https://github.com/open-policy-agent/gatekeeper).
* [Draino](https://github.com/planetlabs/draino) Draino automatically drains Kubernetes nodes based on labels and node conditions. Nodes that match all of the supplied labels and any of the supplied node conditions will be cordoned immediately and drained after a configurable drain-buffer time.

## Kubernetes Troubleshooting
* [==learnk8s.io: A visual guide on troubleshooting Kubernetes deployments== 🌟](https://learnk8s.io/troubleshooting-deployments)
* [Understanding Kubernetes cluster events](https://banzaicloud.com/blog/k8s-cluster-logging/)
* [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
* [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)
* [medium.com: Kubernetes Tip: How To Disambiguate A Pod Crash To Application Or To Kubernetes Platform? (CrashLoopBackOff)](https://medium.com/tailwinds-navigator/kubernetes-tip-how-to-disambiguate-a-pod-crash-to-application-or-to-kubernetes-platform-f6c1395a8d09)
* [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating/)
* [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes/)
* [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples/)
* [levelup.gitconnected.com: 5 tips for troubleshooting apps on Kubernetes](https://levelup.gitconnected.com/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [medium: Common Kubernetes Errors Made by Beginners [2021] 🌟](https://medium.com/nerd-for-tech/common-kubernetes-errors-made-by-beginners-274b50e18a01)
* [cloud.redhat.com: Troubleshooting Sandboxed Containers Operator](https://cloud.redhat.com/blog/sandboxed-containers-operator-from-zero-to-hero-the-hard-way-part-2)
* [komodor.com: Kubernetes Troubleshooting: The Complete Guide](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/)
* [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes/)
* [kinvolk.io: Investigating Kubernetes performance issues with BPF](https://kinvolk.io/blog/2020/04/inside-kinvolk-labs-investigating-kubernetes-performance-issues-with-bpf/)
* [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
* [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot/)
* [youtube: 3 Ways to Detect Evil "Latest" Image Tags in Kubernetes - Kubevious](https://www.youtube.com/watch?v=93RlMqO4glM&t=6s&ab_channel=Kubevious) The "latest" image tag is a disaster waiting to happen. In this video, you will learn how to detect usage of the latest images using 3 different methods.
* [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands/)
* [dzone.com: The Three Pillars of Kubernetes Troubleshooting 🌟](https://dzone.com/articles/the-three-pillars-of-kubernetes-troubleshooting) Diving into how the three pillars of understanding, managing and preventing for Kubernetes troubleshooting, and how it helps to conceive of what’s needed to be able to properly troubleshoot real-world Kubernetes stacks that are the hallmark of complex, distributed systems.
* [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting/)
* [==itnext.io: Distroless Container Debugging on K8s/OpenShift==](https://itnext.io/distroless-container-debugging-on-k8s-openshift-e418fd66fdad)
    * When people focusing more on the security of containers, distroless based images are frequently used to reduce the attack surface. In these images, the package manager, the non-dependent modules or libraries, even the shells are stripped off, only the app and its required dependencies are kept. For the statically linked executable, produced by golang for example, we can even use “scratch” as the base.
    * The potential exploit of vulnerability is therefore greatly reduced. But, on the other hand, it is difficult to troubleshoot the application if even the shell is not available, leaving only the logs from the app.
    * In this paper, we will explore different options to facilitate debugging by bringing back the shell.
* [==containiq.com: Kubernetes Events: In-Depth Guide & Examples== 🌟](https://www.containiq.com/post/kubernetes-events) Kubernetes events help you understand how Kubernetes resource decisions are made and they can be helpful for debugging. Learn more about k8s events in this in-depth guide.
* [==loft.sh: Using Kubernetes Ephemeral Containers for Troubleshooting==](https://loft.sh/blog/using-kubernetes-ephemeral-containers-for-troubleshooting/)
* [==speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps==](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)
* [containiq.com: Debugging Your Kubernetes Nodes in the ‘Not Ready’ State | nodenotready](https://www.containiq.com/post/debugging-kubernetes-nodes-in-not-ready-state) Kubernetes clusters typically run on multiple “nodes” each having its own state. In this article, you’ll learn a few possible reasons a node might enter the **NotReady** state and how you can debug it.
* [containiq.com: Troubleshooting Kubernetes FailedAttachVolume and FailedMount](https://www.containiq.com/post/fixing-kubernetes-failedattachvolume-and-failedmount) When working with Persistent Volumes in Kubernetes, you might run into the FailedAttachVolume or FailedMount error. In this tutorial, we’ll show you how to troubleshoot these errors and find the root cause and fix them.
* [==containiq.com: Kubernetes ImagePullBackOff: Troubleshooting With Examples==](https://www.containiq.com/post/kubernetes-imagepullbackoff) If you’ve worked with Kubernetes for a while, chances are good that you have experienced the **ImagePullBackOff** status. This issue can be frustrating if you are unfamiliar with it, so in this guide, you will walk the reader through how to troubleshoot this issue, what some common causes are, and where to start if they encounter this problem.
* [==opensource.googleblog.com: Introducing Ephemeral Containers==](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html) **Ephemeral containers are a new type of container that are part of the Kubernetes core API. An Ephemeral Container may be added to an existing Pod for administrative actions like debugging, it runs until it exits, and it won't be restarted. An ephemeral container runs within the Pod's existing resource allocation and shares common container namespaces.**

<center>
[![learnk8s debug your pods](images/learnk8s_debug_your_pods.png){: style="width:30%"}](https://learnk8s.io/troubleshooting-deployments)
</center>

### Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes
* [learnk8s.io: Provisioning cloud resources (AWS, GCP, Azure) in Kubernetes](https://learnk8s.io/cloud-resources-kubernetes)
### Debugging Techniques and Strategies. Debugging with ephemeral containers
- [kubectl-debug](https://github.com/aylei/kubectl-debug)
- [kubesandclouds.com: Debugging with ephemeral containers in K8s (v1.18+)](https://kubesandclouds.com/index.php/2020/05/30/ephemeral-containers-in-k8s/)
- [How to quarantine pods](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods/)
- [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) KDBG (Kubernetes Debuger) is a small docker container based on lastest Alpine Linux image, used for debugging Kubernetes clusters from inside a pod.
- [inspektor-gadget](https://github.com/kinvolk/inspektor-gadget) Collection of gadgets for debugging and introspecting Kubernetes applications using BPF 
    - [kinvolk.io](https://kinvolk.io)
- [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments](https://learnk8s.io/troubleshooting-deployments)
- [StatusBay](https://github.com/similarweb/statusbay) is a tool that provides the missing visibility into the K8S deployment process. The main goal is to ease the experience of troubleshooting and debugging services in K8S and provide confidence while making changes.
- [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
- [codefresh.io: Using Telepresence 2 for Kubernetes debugging and local development](https://codefresh.io/kubernetes-tutorial/telepresence-2-local-development/)
- [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75) The fastest and easiest way to debug and troubleshoot any application running on Kubernetes
- [tetrate.io: How to debug microservices in Kubernetes with proxy, sidecar or service mesh?](https://www.tetrate.io/blog/how-to-debug-microservices-in-kubernetes-with-proxy-sidecar-or-service-mesh)
- [rookout.com: The Definitive Guide To Kubernetes Application Debugging](https://www.rookout.com/blog/kubernetes-application-debugging)
- [thorsten-hans.com: Debugging apps in Kubernetes with Bridge](https://www.thorsten-hans.com/debugging-apps-in-kubernetes-with-bridge/) Bridge to Kubernetes simplifies and streamlines the process of debugging applications running in Kubernetes. Debug any language using the tools you prefer and love.
    - [marketplace.visualstudio.com: Bridge to Kubernetes (VSCode)](https://marketplace.visualstudio.com/items?itemName=mindaro.mindaro)
    - [marketplace.visualstudio.com: Bridge to Kubernetes (Visual Studio)](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.mindaro) Bridge to Kubernetes for Visual Studio 2019
- [==thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads== 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads/)
- [==levelup.gitconnected.com: De-Mystifying Kubernetes Debugging==](https://levelup.gitconnected.com/de-mystifying-kubernetes-debugging-de9e1c82ac3e) __How to debug your microservice in VS Code with Bridge to Kubernetes__

## Kubernetes Tutorials
* [kubernetes.io: Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) Official documentation from Kubernetes. One can go through this official documentation and can learn much more about Kubernetes.
* [devopscube.com: Kubernetes Tutorials For Beginners: Getting Started Guide](https://devopscube.com/kubernetes-tutorials-beginners/)
* [Intoduction to Kubernetes (slides, beginners and advanced)](https://docs.google.com/presentation/d/1zrfVlE5r61ZNQrmXKx5gJmBcXnoa_WerHEnTxu5SMco)
* [medium.com: Kubernetes 101: Pods, Nodes, Containers, and Clusters](https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16)
* [medium.com: Learn Kubernetes in Under 3 Hours: A Detailed Guide to Orchestrating Containers](https://medium.com/free-code-camp/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882)
* [kubernetestutorials.com: Install and Deploy Kubernetes on CentOs 7](https://kubernetestutorials.com/install-and-deploy-kubernetes-on-centos-7/)
* [medium.com: Simplifying orchestration with Kubernetes](https://medium.com/@swapnasagarpradhan/simplifying-orchestration-with-kubernetes-e81015681a85)
* [aquasec.com: 70 Best Kubernetes Tutorials](https://www.aquasec.com/wiki/display/containers/70+Best+Kubernetes+Tutorials) Valuable Kubernetes tutorials from multiple sources, classified into the following categories: Kubernetes AWS and Azure tutorials, networking tutorials, clustering and federation tutorials and more.
* [cloud.google.com: kubernetes comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic/) Learn about kubernetes and how you can use it for continuous integration and delivery.
* [magalix.com: Kubernetes 101 - Concepts and Why It Matters](https://www.magalix.com/blog/kubernetes-101-concepts-and-why-it-matters)
* [Google Play: Learning Solution - Learn Kubernetes](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnKubernetes)
* [Google Play: TomApp - Learn Kubernetes](https://play.google.com/store/apps/details?id=tomtran.learnkubernetes)
    * [apkplz.net: Learn Kubernetes 1 APK](https://apkplz.net/app/com.LearningSolution.LearnKubernetes)
    * [Google Play Search](https://play.google.com/store/search?q=learn+kubernetes)
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [dzone: The complete kubernetes collection tutorials and tools](https://dzone.com/articles/the-complete-kubernetes-collection-tutorials-and-tools)
* [dzone: kubernetes in 10 minutes a complete guide to look](https://dzone.com/articles/kubernetes-in-10-minutes-a-complete-guide-to-look)
* [magalix.com: The Best Kubernetes Tutorials](https://www.magalix.com/blog/the-best-kubernetes-tutorials)
* [35 Advanced Tutorials to Learn Kubernetes](https://medium.com/faun/35-advanced-tutorials-to-learn-kubernetes-dae5695b1f18)
* [geekflare.com: 14 Kubernetes Tutorials for Beginner to Master](https://geekflare.com/learn-kubernetes/)
* [freecodecamp.org: The Kubernetes Handbook 🌟](https://www.freecodecamp.org/news/the-kubernetes-handbook/) 
* [youtube: Kubernetes Pods and ReplicaSets explained](https://www.youtube.com/playlist?list=PLy0Gle4XyvbGhGpX0CXAuiEsfL-MD-rND)
* [medium: DraftKings Kubernetes Workshop: Hands-on Learning in K8s (with Video Walkthrough)](https://medium.com/draftkings-engineering/draftkings-workshop-demystifying-kubernetes-4ce86c187408)
* [100 Days Of Kubernetes: 100daysofkubernetes.io](https://100daysofkubernetes.io/) 100 Days of Kubernetes is the challenge in which we aim to learn something new related to Kubernetes each day across 100 Days!!!
* [youtube playlist: Thetips4you - Kubernetes Tutorial for Beginners](https://www.youtube.com/playlist?app=desktop&list=PLVx1qovxj-akr_3XqQQgpqRyQw4GYuS4h) HPA, Deployments, YAML, Jenkins, etc.
* [youtube playlist: DevNation Lessons: Kubernetes Fundamentals](https://www.youtube.com/playlist?list=PLf3vm0UK6HKpOqIY2fcu_M0sCSpluyXMW)
* [amazee.io: Master the Fundamentals of K8s: Kubernetes 101 video series with Jeff Geerling](https://www.amazee.io/blog/post/master-the-fundamentals-of-k8s)
* [medium: How to deploy StatefulSets in Kubernetes (K8s)?](https://medium.com/avmconsulting-blog/deploying-statefulsets-in-kubernetes-k8s-5924e701d327)
* millionvisit.blogspot.com. Kubernetes for Developers Journey:
    * [millionvisit.blogspot.com: Kubernetes for Developers #1: Kubernetes Architecture and Features](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-1-kubernetes-architecture.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #2: Kubernetes for Local Development](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-2-Local-development.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #3: kubectl CLI](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-3-kubectl-cli.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #4: Enable kubectl bash autocompletion](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-4-kubectl-autocompletion.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #5: Kubernetes Web UI Dashboard](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-5-webui-dashboard.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #6: Kubernetes Objects](http://millionvisit.blogspot.com/2020/12/kubernetes-for-developers-6-KubernetesObjects.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #7: Imperative vs. Declarative Kubernetes Objects](http://millionvisit.blogspot.com/2021/01/kubernetes-for-developers-7-imperative-vs-Declarative.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #9: Kubernetes Pod Lifecycle](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-9-Kubernetes-Pod-Lifecycle.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #10: Kubernetes Pod YAML manifest in-detail ](http://millionvisit.blogspot.com/2021/03/kubernetes-for-developers-10-kubernetes-Pod-YAML-manifest.html)
    * [millionvisit.blogspot.com: Kubernetes for Developers #14: Kubernetes Deployment YAML manifest in-detail](http://millionvisit.blogspot.com/2021/05/kubernetes-for-developers-14-Kubernetes-Deployment-YAML-manifest.html)
* ithands-on.com: 
    * [ithands-on.com: Kubernetes 101 : Deployments, replicaSets, services, pods and endpoints](https://www.ithands-on.com/2021/05/kubernetes-101-deployment-replicasets.html)
    * [ithands-on.com: Kubernetes 101 : An overview of StatefulSets and Deployments](https://www.ithands-on.com/2021/05/kubernetes-101-overview-of-statefulsets.html)
    * [ithands-on.com: Kubernetes 101 : Resource Quotas (ResourceQuota) and Limit Ranges (LimitRange)](https://www.ithands-on.com/2021/05/kubernetes-101-resource-quotas.html)
    * [ithands-on.com: Kubernetes 101 : Deployments and Rolling updates - maxSurge, maxUnavailable](https://www.ithands-on.com/2021/06/kubernetes-101-deployments-and-rolling.html)
    * [ithands-on.com: Kubernetes 101 : The externalName service](https://www.ithands-on.com/2021/06/kubernetes-101-externalname-service.html)
* [dev.to: Kubernetes Crash Course for Absolute Beginners](https://dev.to/techworld_with_nana/kubernetes-crash-course-for-absolute-beginners-35pc)
* [dev.to: Let's Learn Kubernetes Series' Articles](https://dev.to/pghildiyal/series/14818)

### Online Training
* [katacoda.com](https://www.katacoda.com/) Interactive Learning and Training Platform for Software Engineers 
* [kubernetesbyexample.com](http://kubernetesbyexample.com/)
* [Play with Kubernetes](https://labs.play-with-k8s.com/) A simple, interactive and fun playground to learn Kubernetes
* [udemy.com: Learn DevOps: The Complete Kubernetes Course](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
    * [wardviaene/kubernetes-course](https://github.com/wardviaene/kubernetes-course) 
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
    * [wardviaene/advanced-kubernetes-course](https://github.com/wardviaene/advanced-kubernetes-course) 
* [Certified Kubernetes Administrator CKA course notes — diagrams for each subject area and use as reference for future refresher](https://drive.google.com/file/d/1RhPULD1IAVgCo1KD857iCoaNKuJjQKa1/view)
* [javarevisited.blogspot.com: Top 5 Free Courses to Learn Kubernetes for Developers and DevOps Engineers](https://javarevisited.blogspot.com/2019/01/top-5-free-kubernetes-courses-for-DevOps-Engineer.html)
* [kodekloud.com](https://kodekloud.com)
* [training.linuxfoundation.org: Introduction to Kubernetes (LFS158x)](https://training.linuxfoundation.org/training/introduction-to-kubernetes/) Want to learn Kubernetes? Get an in-depth primer on this powerful system for managing containerized applications in this free course.

### K8s Diagrams
- [cloudogu/k8s-diagrams](https://github.com/cloudogu/k8s-diagrams) A collection of diagrams explaining kubernetes by cloudogu, written in [PlantUML](https://twitter.com/PlantUML).

## Kubernetes Patterns and Antipatterns. Service Discovery
- [github.com/k8spatterns/examples](https://github.com/k8spatterns/examples) Examples for "Kubernetes Patterns - Reusable Elements for Designing Cloud-Native Applications"
- [kubernetes.io: container design patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
- [magalix.com: Kubernetes Patterns - The Service Discovery Pattern](https://www.magalix.com/blog/kubernetes-patterns-the-service-discovery-pattern)
- [gardener.cloud: Kubernetes Antipatterns](https://gardener.cloud/050-tutorials/content/howto/antipattern/)
- [dzone.com: Performance Patterns in Microservices-Based Integrations](https://dzone.com/articles/performance-patterns-in-microservices-based-integr-1)
- [developers.redhat.com: Top 10 must-know Kubernetes design patterns](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)
- [medium: 10 Anti-Patterns for Kubernetes Deployments](https://medium.com/better-programming/10-antipatterns-for-kubernetes-deployments-e97ce1199f2d) Common practices in Kubernetes deployments that have better solutions
- [learnsteps.com: How Kubernetes works on reconciler pattern](https://www.learnsteps.com/how-kubernetes-works-on-a-reconciler-pattern/)
- [learncloudnative.com: Sidecar Container Pattern](https://www.learncloudnative.com/blog/2020-09-30-sidecar-container/)
- [towardsdatascience.com: Kubernetes pattern for applications with external environment configuration](https://towardsdatascience.com/kubernetes-pattern-for-applications-with-external-environment-configuration-a42d7bdd7e97) Learn how to decouple configuration from the application using git-sync, Kubernetes init-containers, ConfigMaps and volumes.
- [codefresh.io: Kubernetes Deployment Antipatterns – part 1](https://codefresh.io/kubernetes-tutorial/kubernetes-antipatterns-1/)
- [codefresh.io: Kubernetes Deployment Antipatterns – part 2](https://codefresh.io/kubernetes-tutorial/kubernetes-antipatterns-2/)
- [iximiuz.com: Service discovery in Kubernetes - combining the best of two worlds](https://iximiuz.com/en/posts/service-discovery-in-kubernetes/)
- [github.com/sharadbhat/KubernetesPatterns: YAML and Golang implementations of common Kubernetes patterns](https://github.com/sharadbhat/KubernetesPatterns)
- [developers.redhat.com: Kubernetes configuration patterns, Part 1: Patterns for Kubernetes primitives](https://developers.redhat.com/blog/2021/04/28/kubernetes-configuration-patterns-part-1-patterns-for-kubernetes-primitives)
    - [developers.redhat.com: Kubernetes configuration patterns, Part 2: Patterns for Kubernetes controllers](https://developers.redhat.com/blog/2021/05/05/kubernetes-configuration-patterns-part-2-patterns-for-kubernetes-controllers/)
- [learnk8s.io: Extending applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns) Can you change an application without changing any code in Kubernetes? You can when you use multiple containers in a single Pod. Developing and deploying new apps in Kubernetes is easy. But what about legacy apps? In Kubernetes, you can use multiple containers in a Pod to change how your application works.
- [dev.to: Kubernetes Deployment Antipatterns – part 1](https://dev.to/codefreshio/kubernetes-deployment-antipatterns-part-1-2116)
- [ishantgaurav.in: Kubernetes – Sidecar Container Pattern](https://ishantgaurav.in/2021/07/18/kubernetes-sidecar-container-pattern/)
- [developers.redhat.com: Kubernetes configuration patterns, Part 1: Patterns for Kubernetes primitives](https://developers.redhat.com/blog/2021/04/28/kubernetes-configuration-patterns-part-1-patterns-for-kubernetes-primitives)
- [betterprogramming.pub: 10 Anti-Patterns for Kubernetes Deployments](https://betterprogramming.pub/10-antipatterns-for-kubernetes-deployments-e97ce1199f2d) Common practices in Kubernetes deployments that have better solutions
- [medium: Kubernetes — Learn Init Container Pattern](https://medium.com/bb-tutorials-and-thoughts/kubernetes-learn-init-container-pattern-7a757742de6b) Understanding Init Container Pattern With an Example Project.
- [weave.works: Tools for Automating and Implementing Cloud Native Patterns](https://www.weave.works/blog/tools-for-automating-and-implementing-cloud-native-patterns)
- [dzone: Microservices Patterns: Sidecar](https://dzone.com/articles/microservices-patterns-sidecar) Learn about Microservice architecture and single responsibility principle, know more on how to achieve it using sidecars.
- [dzone: Multi-Container Pod Design Patterns in Kubernetes](https://dzone.com/articles/multi-container-pod-design-patterns-in-kubernetes) In Kubernetes, Pods are the single deployable units. If an application is to be deployed, it must be so in a Pod as a container. Learn how to use multi-container pods.

[![Top 10 Kubernetes patterns](images/top_10_kubernetes_patterns.png)](https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/)

## Kubernetes Scheduling and Scheduling Profiles
* [Kubernetes Scheduling](https://kubernetes.io/docs/reference/scheduling/)
* [Scheduling Profiles](https://kubernetes.io/docs/reference/scheduling/profiles/)
* [granulate.io: A Deep Dive into Kubernetes Scheduling](https://granulate.io/a-deep-dive-into-kubernetes-scheduling/)
* [medium: K8S - Creating a kube-scheduler plugin](https://medium.com/@juliorenner123/k8s-creating-a-kube-scheduler-plugin-8a826c486a1)

### Assigning Pods to Nodes. Pod Affinity and Anti-Affinity 
* [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)

### Pod Topology Spread Constraints and PodTopologySpread Scheduling Plugin
* [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)
* [Introducing PodTopologySpread plugin](https://kubernetes.io/blog/2020/05/introducing-podtopologyspread/)
  
## Cloud Development Kit (CDK) for Kubernetes 
* [cdk8s.io](https://cdk8s.io/) Define Kubernetes apps and components using familiar languages. cdk8s is an open-source software development framework for defining Kubernetes applications and reusable abstractions using familiar programming languages and rich object-oriented APIs. cdk8s apps synthesize into standard Kubernetes manifests which can be applied to any Kubernetes cluster.
* [github.com/awslabs/cdk8s](https://github.com/awslabs/cdk8s)

### AWS Cloud Development Kit (AWS CDK)
* [AWS: Introducing CDK for Kubernetes](https://aws.amazon.com/blogs/containers/introducing-cdk-for-kubernetes/)
* Traditionally, Kubernetes applications are defined with human-readable, static YAML data files which developers write and maintain. Building new applications requires writing a good amount of boilerplate config, copying code from other projects, and applying manual tweaks and customizations. As applications evolve and teams grow, these YAML files become harder to manage. Sharing best practices or making updates involves manual changes and complex migrations.
* YAML is an excellent format for describing the desired state of your cluster, but it is does not have primitives for expressing logic and reusable abstractions. There are [multiple tools](https://github.com/ramitsurana/awesome-kubernetes#configuration) in the Kubernetes ecosystem which attempt to address these gaps in various ways:
    * [kustomize](https://github.com/kubernetes-sigs/kustomize) Customization of kubernetes YAML configurations
    * [jsonnet data templating language](https://github.com/google/jsonnet/tree/master/case_studies/kubernetes)
        * [jsonnet.org](https://jsonnet.org/)
    * [jkcfg](https://github.com/jkcfg/jk) Configuration as Code with ECMAScript
        * [jkcfg.github.io](https://jkcfg.github.io/)
    * [kubecfg](https://github.com/bitnami/kubecfg) A tool for managing complex enterprise Kubernetes environments as code.
    * [kubegen](https://github.com/errordeveloper/kubegen) Simple way to describe Kubernetes resources in a structured way, but without new syntax or magic
    * [Pulumi](https://www.pulumi.com/docs/get-started/kubernetes/) 
* We realized this was exactly the same problem our customers had faced when defining their applications through CloudFormation templates, a problem solved by the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/), and that we could apply the same design concepts from the AWS CDK to help all Kubernetes users.

## Serverless with OpenFaas and Knative
* [Serverless Architectures](serverless.md)

<center>
[![Serverless](images/from-monolith-to-serverless.jpg)](https://www.xenonstack.com/blog/serverless-openfaas-java/) 
</center>

## Multi-Cluster Federation. Hybrid Cloud Setup Tools
### KubeFed
- [KubeFed: Kubernetes Cluster Federation](https://github.com/kubernetes-sigs/kubefed)
- [aquasec.com: Kubernetes Federation: The Basics and a 5-Step Tutorial](https://www.aquasec.com/cloud-native-academy/kubernetes-in-production/kubernetes-federation/) Learn about Kubernetes Federation use cases, how it works, and see how to create your first Kubernetes Federation in 5 steps.
- Kubernetes Federation, or KubeFed, is a tool for coordinating the configuration of multiple clusters in Kubernetes. You can determine which clusters KubeFed will manage, and what their configuration looks like, all from a single group of APIs in the hosting cluster. KubeFed offers low-level mechanisms that can be used as a foundation for increasingly complex production Kubernetes use cases across multiple clusters, such as geographic redundancy and disaster recovery. 

### KubeCarrier
- [KubeCarrier](https://github.com/kubermatic/kubecarrier)

### Red Hat Operator Lifecycle Manager (OLM) 
- [Red Hat OLM](https://github.com/operator-framework/operator-lifecycle-manager) operator-lifecycle-manager is a management framework for extending Kubernetes with Operators. OLM extends Kubernetes to provide a declarative way to install, manage, and upgrade Operators and their dependencies in a cluster.

### Istio Service Mesh
- [Istio](https://istio.io/)

## Multi-Regional Architecture
- [engineering.monday.com: monday.com’s Multi-Regional Architecture: A Deep Dive](https://engineering.monday.com/monday-coms-multi-regional-architecture-a-deep-dive/) Building a global SaaS platform requires lots of preparation, deep evaluation of your request routes and a truckload of R&D cooperation. Here's how we did it

## Kubernetes Scripts
- [Kubernetes Scripts](https://github.com/eldada/kubernetes-scripts)
- [Get applied and effective apiVersion from Kubernetes objects](https://gist.github.com/ninlil/affbf7514d4e74c7634e77f47e172236)

### Kubernetes and Ansible
- [itnext.io: Automating System Updates for Kubernetes Clusters using Ansible](https://itnext.io/automating-system-updates-for-kubernetes-clusters-using-ansible-94a70f4e1972)
- [Ansible for devops: Kubernetes](https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes)

## Spot instances in Kubernetes
- [itnext.io: Embracing failures and cutting infrastructure costs: Spot instances in Kubernetes](https://itnext.io/embracing-failures-and-cutting-infrastructure-costs-spot-instances-in-kubernetes-6976781beacc)

## Kubernetes on Windows
- [loft.sh: Kubernetes on Windows: 6 Life-Saving Tools & Tips](https://loft.sh/blog/kubernetes-on-windows-6-life-saving-tools-and-tips/)

## Kubernetes Incident Report Plan IRP
- [cynet.com: Incident Report Plan (IRP)](https://www.cynet.com/incident-response/incident-response-plan/)
- [kubermatic.com: A Framework for Kubernetes Incident Response](https://www.kubermatic.com/blog/a-framework-for-kubernetes-incident-response/)

## Kubernetes interview questions
- [Kubernetes Interview Questions and Answers 2019 2020](https://linux.amitmaheshwari.in/2019/11/kubernetes-interview-questions-and.html)
- [intellipaat.com: Top Kubernetes Interview Questions and Answers](https://intellipaat.com/blog/interview-question/kubernetes-interview-questions-answers/)
- [automationreinvented.blogspot.com: Top 11 Kubernetes interview question and answers for SDET Devops QA SET-01?](https://automationreinvented.blogspot.com/2020/09/top-11-kubernetes-interview-question.html)
- [devsecops.co.in: Kubernetes Interview Questions and Answers](https://devsecops.co.in/2021/05/22/kubernetes-interview/)
- [ymmt2005.hatenablog.com: 47 things that you should know to be a Kubernetes experts (questions + answers)](https://ymmt2005.hatenablog.com/entry/k8s-things)
- [automationreinvented.blogspot.com: kubernetes posts](https://automationreinvented.blogspot.com/search/label/Kubernetes?m=1)
- [jakubstransky.com: 4 devs by devs: Kubernetes interview question made easy](https://jakubstransky.com/2021/11/05/4-devs-kubernetes-interview-question-made-easy/) Distilled introduction for developers. Things I believe that every developer should be aware of. 

## Kubernetes Certifications. CKA, CKAD and CKS
- [cncf.io: Certified Kubernetes Application Developer (CKAD)](https://www.cncf.io/certification/ckad/)
- [CKAD-Bookmarks](https://github.com/reetasingh/CKAD-Bookmarks) save time in searching docs in CKAD exam
- [itnext.io: Tips & Tricks for CKA, CKAD and CKS exams](https://itnext.io/tips-tricks-for-cka-ckad-and-cks-exams-cc9dade1f76d)
- [bmuschko/ckad-crash-course: Certified Kubernetes Application Developer (CKAD) Crash Course](https://github.com/bmuschko/ckad-crash-course) 
- [jamesbuckett/ckad-questions](https://github.com/jamesbuckett/ckad-questions) A set of exercises and solutions to prepare for the Certified Kubernetes Application Developer exam by Cloud Native Computing Foundation.
- [reddit.com/r/kubernetes: CKAD - free materials](https://www.reddit.com/r/kubernetes/comments/r4q1ec/ckad_free_materials/) This collection of useful links and resources is indispensable if you're thinking of passing the CKAD (Certified Kubernetes Application Developer) course!
    - Courses: https://www.edx.org/course/introduction-to-kubernetes
    - Exercises: https://github.com/dgkanatsios/CKAD-exercises
    - Workshops: 
        - https://kube.academy/courses/ckad-practice
        - https://kodekloud.com/courses/game-of-pods/
        - https://kubernetes.io/docs/tutorials/kubernetes-basics/
        - https://www.katacoda.com/courses/kubernetes/
    - VIM: [Vim Crash Course | How to edit files quickly in CKAD / CKA exam](https://www.youtube.com/watch?v=knyJt8d6C_8&ab_channel=TheFrontOpsGuy)
    - Cheatsheet: 
        - https://kubernetes.io/docs/reference/kubectl/cheatsheet/ 
        - https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
    - Example questions: 
        - [CKAD Example Question with Tips & Tricks](https://www.youtube.com/watch?v=wHha-Q3XVOg&ab_channel=DanLister)
        - [Mock Test - 1, CKAD Prep Exam](https://www.youtube.com/watch?v=TPXwVmvzlV4&ab_channel=TheFrontOpsGuy)
        - [Mock Test - 2, CKAD Prep Exam (Solution)](https://www.youtube.com/watch?v=BiY3b7F96wc&ab_channel=TheFrontOpsGuy)
        - https://medium.com/bb-tutorials-and-thoughts/practice-enough-with-these-questions-for-the-ckad-exam-2f42d1228552

- [kodekloud.com: CKA vs CKAD vs CKS – What is the Difference](https://kodekloud.com/cka-vs-ckad-vs-cks-what-is-the-difference/)

## Books and eBooks
- [developers.redhat.com: Kubernetes Operators](https://developers.redhat.com/books/kubernetes-operators)
- [Kubernetes 101](https://leanpub.com/kubernetes-101)
- [learnk8s.io/first-steps](https://learnk8s.io/first-steps)
- [ubuntuask.com: Best New Kubernetes Books](https://ubuntuask.com/blog/best-new-kubernetes-books)
- [suse.com: Kubernetes Management For Dummies](https://www.suse.com/lp/kubernetes-for-dummies) Getting Kubernetes up and running is one thing. Managing it successfully is quite another

### Kubernetes Patterns eBooks
* [k8spatterns.io: Free Kubernetes Patterns e-book](https://k8spatterns.io/) , [ref](https://www.redhat.com/en/engage/kubernetes-containers-architecture-s-201910240918)
* [magalix.com: Free Kubernetes Application Architecture Patterns eBook](https://www.magalix.com/kubernetes-application-patterns-e-book-download)

### Famous Kubernetes ebooks of 2019
* [Kubernetes essentials E-book](https://images.linoxide.com/ebook-kubernetes-essentials.pdf)
* [Cloud-Native DevOps With Kubernetes O'Reilly book (Free)](https://www.nginx.com/resources/library/cloud-native-devops-with-kubernetes/)
* [Kubernetes: Up and Running, 2nd Edition](http://shop.oreilly.com/product/0636920223788.do) Dive into the Future of Infrastructure. By Brendan Burns, Kelsey Hightower, Joe Beda
* [Container Security](https://www.amazon.com/gp/product/1492056707)
    * [Don't make this container security mistake](https://bitfieldconsulting.com/blog/container-security)
* [digitalocean.com: From Containers to Kubernetes with Node.js eBook](https://www.digitalocean.com/community/books/from-containers-to-kubernetes-with-node-js-ebook)

<center>
[![Kubernetes: Up and Running](images/kubernetes_up_running_kelsey_hightower.gif)](http://shop.oreilly.com/product/0636920223788.do)
</center>

## Famous Kubernetes resources of 2019
* [Kubernetes for developers](https://www.udemy.com/course/kubernetes-for-developers/)
* [Kubernetes for the Absolute Beginners](https://www.udemy.com/course/learn-kubernetes/)
* [Kubernetes: Getting Started (Free)](https://www.udemy.com/course/kubernetes-getting-started/)
* [Kubernetes Tutorial: Learn the Basics](https://dev.to/scalyr/kubernetes-tutorial-learn-the-basics-and-get-started-5dgh)
* [Complete Kubernetes Course](https://www.youtube.com/watch?v=0KQndcIedeg)
* [Getting started with Kubernetes](https://learn.pluralsight.com/programs/2019/free-course/template4)

## Famous Kubernetes resources of 2020
* [javarevisited.blogspot.com: Top 5 courses to Learn Docker and Kubernetes in 2020 - Best of Lot](https://javarevisited.blogspot.com/2019/05/top-5-courses-to-learn-docker-and-kubernetes-for-devops.html)
* [medium.com: Top 15 Online Courses to Learn Docker, Kubernetes, and AWS for Fullstack Developers and DevOps Engineers](https://medium.com/javarevisited/top-15-online-courses-to-learn-docker-kubernetes-and-aws-for-fullstack-developers-and-devops-d8cc4f16e773)
* [medium.com: 7 Free Online Courses to Learn Kubernetes in 2020](https://medium.com/javarevisited/7-free-online-courses-to-learn-kubernetes-in-2020-3b8a68ec7abc)
* [skillslane.com: 10 Best Kubernetes Courses [2020]: Beginner to Advanced Courses](https://skillslane.com/learn-kubernetes-from-these-best-online-courses/)

## Kubernetes Slack Channel
- [kubernetes.slack.com](https://kubernetes.slack.com)
- [slack.kubernetes.io](http://slack.kubernetes.io) is the way to get yourself invited.

## Slides
??? note "Click to expand!"

    <center>
    <iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/e1c397b2aa67470e9204f82f938fec78?slide=1" title="KubeCologne keynote—Troubleshooting Kubernetes apps" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 560px; height: 314px;" data-ratio="1.78343949044586"></iframe>
    </center>
## Bunch of images
??? note "Click to expand!"

    <center>

    [![Kubernetes architecture](images/kubernetes-pod-creation.png)](https://www.padok.fr/en/blog/kubernetes-architecture-clusters)

    [![10 most common mistakes](images/10_common_kubernetes_mistakes.jpg){: style="width:60%"}](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s)

    [![5 Open-source projects that make #Kubernetes even better](images/five-oss-projects-kubernetes.jpg){: style="width:80%"}](https://enterprisersproject.com/article/2020/5/kubernetes-5-open-source-projects-improve)

    [![kubernetes arch multicloud hybrid](images/kubernetes_architecture_multicloud_hybride.jpg){: style="width:70%"}](https://www.journaldunet.com/web-tech/cloud/1492047-comment-kubernetes-perce-les-frontieres-du-cloud/)

    [![Kubernetes components](images/kubernetes_components_rootsongjc.jpg)](https://github.com/rootsongjc)

    [![Container flowchart](images/container_flowchart.jpg)](https://searchcloudcomputing.techtarget.com/tip/Weigh-the-pros-and-cons-of-managed-Kubernetes-services)

    [![dockerswarm vs kubernetes](images/dockerswarm_vs_kubernetes.png)](https://www.imaginarycloud.com/blog/docker-vs-kubernetes/)

    ![simple k8s cluster meme](images/simple_k8s_cluster_meme.jfif)
    </center>

## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/PH-2FfFD2PU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9cwjtN3gkD4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/cZ1S2Gp47ng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/CmPK93hg5w8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9wvEwPLcLcA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/NrytqS43dgw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7skInj_vqN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/BE77h7dmoQU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Spanish Videos
??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/9p3llZAcyG8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Can you change an application without changing any code in Kubernetes?<br><br>You can when you use multiple containers in a single Pod.<br><br>Here’s a visual recap of <a href="https://twitter.com/EmanuelMEvans?ref_src=twsrc%5Etfw">@EmanuelMEvans</a> ’s article on extending apps on Kubernetes with multi-container pods <a href="https://t.co/afS3pPj4zb">https://t.co/afS3pPj4zb</a> <a href="https://t.co/LS5zOZErbE">pic.twitter.com/LS5zOZErbE</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1366373443780808707?ref_src=twsrc%5Etfw">March 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What if you could choose the best node for your Kubernetes cluster before writing any code?<br><br>I built a calculator to choose the optimal instance sizing for your Kubernetes cluster<a href="https://t.co/3jlyCLrvdq">https://t.co/3jlyCLrvdq</a><br><br>Discover:<br><br>- costs (used, wasted, kubelet)<br>- overcommitment<br>- utilisation <a href="https://t.co/gdRTEWkez6">pic.twitter.com/gdRTEWkez6</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1435174508860747776?ref_src=twsrc%5Etfw">September 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: What happens when you create a Pod in Kubernetes?<br><br>Spoiler: a surprisingly simple task reveals a complicated workflow that touches several components in the cluster. <a href="https://t.co/SNEufo0lBe">pic.twitter.com/SNEufo0lBe</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1291371746801545219?ref_src=twsrc%5Etfw">August 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How to quarantine a Pod in Kubernetes.<br><br>This technique helps you with debugging running Pods in production.<br><br>The Pod is detached from the Service (no traffic), and you can troubleshoot it live.<br><br>Let&#39;s get started! <a href="https://t.co/E7AUh2ylM7">pic.twitter.com/E7AUh2ylM7</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1275786970610843648?ref_src=twsrc%5Etfw">June 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How to gracefully shut down Pods without dropping production traffic in Kubernetes<br><br>If you&#39;ve ever noticed dropped connection after a rolling upgrade, this thread digs into the details.<br><br>Let&#39;s start: 𝘸𝘩𝘢𝘵 𝘩𝘢𝘱𝘱𝘦𝘯𝘴 𝘸𝘩𝘦𝘯 𝘢 𝘗𝘰𝘥 𝘪𝘴 𝘥𝘦𝘭𝘦𝘵𝘦𝘥? <a href="https://t.co/jS5litVUlw">pic.twitter.com/jS5litVUlw</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1280087657968627713?ref_src=twsrc%5Etfw">July 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: How does the scheduler work in Kubernetes?<br><br>The scheduler is in charge of deciding where your pods are deployed in the cluster.<br><br>It might sound like an easy job, but it&#39;s rather complicated!<br><br>Let&#39;s dive into it. <a href="https://t.co/iC1vnargc4">pic.twitter.com/iC1vnargc4</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1309090938673868801?ref_src=twsrc%5Etfw">September 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">MEGATHREAD<br><br>Learn Kubernetes one Twitter thread at the time!<br><br>Below you can find a collection of threads about Kubernetes and Kubernetes-related tech!<br><br>I regularly add more, so you can follow me or <a href="https://twitter.com/learnk8s?ref_src=twsrc%5Etfw">@learnk8s</a> for more updates! <a href="https://t.co/0ingxHn9vx">pic.twitter.com/0ingxHn9vx</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1298543151901155330?ref_src=twsrc%5Etfw">August 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>Running new apps in Kubernetes is straightforward.<br><br>But what happens when you have legacy apps that:<br><br>- Log to file instead of stdout?<br>- Has no support Prometheus?<br>- Has no support for HTTPS<br><br>Read on → <a href="https://t.co/m79f69Huqw">pic.twitter.com/m79f69Huqw</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1363783405389770752?ref_src=twsrc%5Etfw">February 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m often asked why I prefer zonal Kubernetes clusters over regional clusters. <a href="https://twitter.com/gctaylor?ref_src=twsrc%5Etfw">@gctaylor</a> does a great job explaining how <a href="https://twitter.com/reddit?ref_src=twsrc%5Etfw">@reddit</a> leverages zonal clusters to limit the blast radius of config changes and reduce cross AZ network traffic. <a href="https://t.co/3pW5awTtdQ">https://t.co/3pW5awTtdQ</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1372638634482884608?ref_src=twsrc%5Etfw">March 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD<br><br>How do you scale background jobs in Kubernetes?<br><br>With Python, Celery, RabbitMQ and KEDA! <a href="https://t.co/BOtwiSjIKW">pic.twitter.com/BOtwiSjIKW</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1376485484319272966?ref_src=twsrc%5Etfw">March 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Architecting <a href="https://twitter.com/hashtag/Kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#Kubernetes</a> clusters: Should you use a single cluster or many clusters for your team(s)?<br><br>There are pros and cons to both, read the thread to find out more 🧵 <a href="https://t.co/1n5ACO97Ay">pic.twitter.com/1n5ACO97Ay</a></p>&mdash; appvia (@appvia_io) <a href="https://twitter.com/appvia_io/status/1427666653668642816?ref_src=twsrc%5Etfw">August 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Unpopular opinion: Kubernetes doesn&#39;t have a clear separation between admin and app developer APIs, and we acknowledged this as a source of complexity but maybe this is why it became successful.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1435769654106988551?ref_src=twsrc%5Etfw">September 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes saved us from a world of completely proprietary Cloud APIs and provided a trustworthy basis for an open ecosystem of infrastructure tools and APIs. <a href="https://t.co/i67orzir2O">https://t.co/i67orzir2O</a></p>&mdash; Ian Lewis 💉💉 (@IanMLewis) <a href="https://twitter.com/IanMLewis/status/1436535960091590658?ref_src=twsrc%5Etfw">September 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">As more enterprises embrace <a href="https://twitter.com/hashtag/containers?src=hash&amp;ref_src=twsrc%5Etfw">#containers</a>, they’ll find they need <a href="https://twitter.com/hashtag/Kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#Kubernetes</a>, too. With our open approach, <a href="https://twitter.com/hashtag/K8s?src=hash&amp;ref_src=twsrc%5Etfw">#K8s</a> does more. Here’s how: <a href="https://t.co/y9TciK53F1">https://t.co/y9TciK53F1</a> <a href="https://t.co/CPWHcy5TOZ">pic.twitter.com/CPWHcy5TOZ</a></p>&mdash; Nicholas Gerasimatos - Red Hat (@nicholas_redhat) <a href="https://twitter.com/nicholas_redhat/status/1441064411947360266?ref_src=twsrc%5Etfw">September 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes experts be like: <a href="https://t.co/0z47Q9bdZm">pic.twitter.com/0z47Q9bdZm</a></p>&mdash; memenetes (@memenetes) <a href="https://twitter.com/memenetes/status/1447668514727280643?ref_src=twsrc%5Etfw">October 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🧵How do you keep up with Kubernetes?<br><br>If you are looking for curated Kubernetes news, we have you covered on:<br><br>- Core Kubernetes<br>- Security<br>- Architecture &amp; development<br>- Job opportunities<br>- K3s<br><br>Here are the accounts that you should follow: <a href="https://t.co/Hcw9BelCsd">pic.twitter.com/Hcw9BelCsd</a></p>&mdash; Learnk8s (@learnk8s) <a href="https://twitter.com/learnk8s/status/1450802588752830465?ref_src=twsrc%5Etfw">October 20, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/kubernetesio?ref_src=twsrc%5Etfw">@kubernetesio</a> <a href="https://twitter.com/K8sArchitect?ref_src=twsrc%5Etfw">@K8sArchitect</a> K8s Architecture <a href="https://t.co/Kbm11a8oMA">pic.twitter.com/Kbm11a8oMA</a></p>&mdash; Julien (@MapEngArch) <a href="https://twitter.com/MapEngArch/status/1452257392201289731?ref_src=twsrc%5Etfw">October 24, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How Kubernetes differs from Docker in the way it deals with containers 🔽<br><br>Under the hood, Kubernetes and Docker both rely on the same/similar lower-level components to run containers.<br><br>Often, both use containerd and runc. However, Kubernetes makes the container runtime pluggable <a href="https://t.co/5daIalpmrt">pic.twitter.com/5daIalpmrt</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1454407183383339008?ref_src=twsrc%5Etfw">October 30, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Does Kubernetes rebalance your Pods?<br><br>If there&#39;s a node that has more space, does Kubernetes recompute and balance the workloads?<br><br>🤔<br><br>Let&#39;s see! <a href="https://t.co/ML7JIGGtrq">pic.twitter.com/ML7JIGGtrq</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1458060468317143041?ref_src=twsrc%5Etfw">November 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">As we close out the year, a few 2022 predictions. 🧵<br><br>1. 2022 will be the year where Kubernetes is finally recognized as technology for platform teams enabling product groups, rather than a technology designed for direct end-usage by developers.</p>&mdash; Gabe Monroy (@gabe_monroy) <a href="https://twitter.com/gabe_monroy/status/1474731108596072449?ref_src=twsrc%5Etfw">December 25, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-168051035-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-168051035-1');
</script>