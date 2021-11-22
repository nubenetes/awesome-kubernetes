# GitOps
- [Introduction](#introduction)
- [GitOps Working Group](#gitops-working-group)
- [Git Repositories Structures](#git-repositories-structures)
- [GitOps Tools](#gitops-tools)
	- [Flux. The GitOps Operator for Kubernetes](#flux-the-gitops-operator-for-kubernetes)
	- [Kustomize. Kubernetes native configuration management](#kustomize-kubernetes-native-configuration-management)
	- [Flagger](#flagger)
	- [WKSctl. Weave Kubernetes System Control](#wksctl-weave-kubernetes-system-control)
	- [Helm](#helm)
	- [Jenkins](#jenkins)
	- [Terraform](#terraform)
	- [Config Sync and Anthos Config Management](#config-sync-and-anthos-config-management)
	- [Portworx AutoPilot](#portworx-autopilot)
	- [OpenShift Applier](#openshift-applier)
	- [HashiCorp Waypoint](#hashicorp-waypoint)
	- [Weave GitOps](#weave-gitops)
- [GitOps Frameworks](#gitops-frameworks)
- [Kubernetes Platforms and GitOps](#kubernetes-platforms-and-gitops)
	- [OpenShift GitOps](#openshift-gitops)
	- [AWS Kubernetes](#aws-kubernetes)
	- [Weave Kubernetes Platform](#weave-kubernetes-platform)
	- [Ubuntu Charmed Kubernetes](#ubuntu-charmed-kubernetes)
- [Tweets](#tweets)
- [Videos](#videos)

## Introduction
- [gitops.tech 🌟](https://www.gitops.tech/)
- [weave.works: Guide to GitOps](https://www.weave.works/technologies/gitops/)
- [weave.works: What Is GitOps?](https://www.weave.works/blog/what-is-gitops-really)
- [atlassian.com: Is GitOps the next big thing in DevOps?](https://www.atlassian.com/git/tutorials/gitops)
- [cloudbees.com: What is GitOps?](https://www.cloudbees.com/gitops/what-is-gitops)
- [dzone: What Is GitOps, Really?](https://dzone.com/articles/what-is-gitops-really) This article will help you understand what GitOps really is as a strategy for development, and its benefits over other CI/CD approaches
- [Continuous GitOps, the way to do DevOps in Kubernetes](https://medium.com/@imarunrk/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster.  
- [thenewstack.io: What Is GitOps and Why It Might Be The Next Big Thing for DevOps](https://thenewstack.io/what-is-gitops-and-why-it-might-be-the-next-big-thing-for-devops/)
- [opensource.substack.com: All You Need To Know About GitOps](https://opensource.substack.com/p/all-you-need-to-know-about-gitops) A complete guide about GitOps, what why and how
- [itnext.io: Continuous GitOps, the way to do DevOps in Kubernetes](https://itnext.io/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster 
- [container-solutions.com: GitOps: The Bad and the Ugly](https://blog.container-solutions.com/gitops-the-bad-and-the-ugly)
- [itnext.io: Principles, Patterns, and Practices for Effective Infrastructure as Code](https://itnext.io/principles-patterns-and-practices-for-effective-infrastructure-as-code-e5f7bbe13df1) Deliver Infrastructure and Software running on it Rapidly and Reliably at Scale.
- [medium: GitOps: Build infrastructure resilient applications 🌟](https://medium.com/@franoisdagostini/gitops-build-infrastructure-resilient-applications-95bbc939046d)
- [itnext.io: Continuous GitOps, the way to do DevOps in Kubernetes 🌟](https://itnext.io/continuous-gitops-the-way-to-do-devops-in-kubernetes-896b0ea1d0fb) Continuous GitOps, the new age DevOps practice to increase the delivery velocity by achieving an end to end “Git source of truth” with Zero manual changes into the Kubernetes cluster.
- [itnext.io: Managing Kubernetes Secrets Securely with GitOps 🌟](https://itnext.io/managing-kubernetes-secrets-securely-with-gitops-b8174b4f4d30)
- [sufle.io: Adopting GitOps for Enhanced Operations](https://www.sufle.io/blog/adopting-gitops-for-enhanced-operations)
- [medium: GitOps : The Next Big Thing for DevOps and Automation!](https://medium.com/searce/gitops-the-next-big-thing-for-devops-and-automation-2a9597e51559) If you have similar questions like: “What’s GitOps?”, “Why we are moving towards this?”, “How and when one can implement this strategy in now running environment?”, “What are the tools it included?” then you have landed on the right page.
- [thenewstack.io: Understanding GitOps: The Latest Tools and Philosophies](https://thenewstack.io/understanding-gitops-the-latest-tools-and-philosophies/)
- [samiyaakhtar.medium.com: GitOps Observability — Visualizing the journey of a container](https://samiyaakhtar.medium.com/gitops-observability-visualizing-the-journey-of-a-container-5f6ef1f3c9d2)
- [clickittech.com: What is GitOps? 🌟](https://www.clickittech.com/devops/what-is-gitops)
- [blog.container-solutions.com: 11 Reasons for Adopting GitOps](https://blog.container-solutions.com/why-adopt-gitops)
- [opensource.com: GitOps vs. DevOps: What's the difference? 🌟](https://opensource.com/article/21/3/gitops) Get to know GitOps, an evolved form of DevOps.
- [geekflare.com: An Introduction to GitOps](https://geekflare.com/gitops-introduction/)
- [thenewstack.io: GitOps Use Cases You May Not Have Considered](https://thenewstack.io/gitops-use-cases-you-may-not-have-considered/)
- [kumomind.medium.com: Should I consider the GitOps methodology?](https://kumomind.medium.com/should-i-consider-the-gitops-methodology-f49e042b8c22)
- [dzone: GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.
- [braindose.blog: 4 Key Characteristics for a Successful GitOps Implementation](https://braindose.blog/2020/03/18/4-key-characteristics-of-gitops/)
- [blog.container-solutions.com: GitOps: The Bad and the Ugly](https://blog.container-solutions.com/gitops-limitations)
- [cloudogu.com: GitOps in Software Development 🌟](https://cloudogu.com/en/glossary/gitops/)
- [gitops.tech: What is GitOps? 🌟](https://www.gitops.tech/#tools)
- [dzone: GitOps – DevOps for Infrastructure Automation 🌟](https://dzone.com/articles/gitops-devops-for-infrastructure-automation) GitOps offers a way to automate and manage infrastructure by using proven DevOps best practices such as version control, code review, and CI/CD pipelines.
- [unifiedguru.com: GitOps and the Cloud Operating Model – VMware Cloud Community 🌟](https://www.unifiedguru.com/gitops-and-the-cloud-operating-model-vmware-cloud-community/)
- [thenewstack.io: Misconfiguration Worries Grow](https://thenewstack.io/misconfiguration-worries-grow/)
- [codefresh.io: The pains of GitOps 1.0 🌟](https://codefresh.io/devops/pains-gitops-1-0/) GitOps as a practice for releasing software has several advantages, but like all other solutions before it, has also several shortcomings. 
- [weave.works: Managing Kubernetes with GitOps in a multi-cluster, multi-cloud world](https://www.weave.works/blog/managing-kubernetes-with-gitops-in-a-multi-cluster-multi-cloud-world)
- [viewnext.com: ¿Qué es GitOps?](https://www.viewnext.com/que-es-gitops/)
- [thenewstack.io: Have Containers Will Travel: Why GitOps Is Essential for Multicloud 🌟](https://thenewstack.io/have-containers-will-travel-why-gitops-is-essential-for-multicloud/)
- [weave.works: Put Your Security Worries to Rest with GitOps Operational Control 🌟](https://www.weave.works/use-cases/security-with-gitops/) GitOps workflows in the Weave Kubernetes Platform give teams a head start since they rely on Git’s strong correctness and security. Every pull request has a built-in and fully auditable trail. Many companies need to look beyond just compliance and seek a full GRC solution that’s integral to their workflows.
- [thenewstack.io: Push vs. Pull in GitOps: Is There Really a Difference?](https://thenewstack.io/push-vs-pull-in-gitops-is-there-really-a-difference/)
- [about.gitlab.com: 3 Ways to approach GitOps 🌟](https://about.gitlab.com/blog/2021/04/27/gitops-done-3-ways/) 
- [developers.redhat.com: Why should developers care about GitOps?](https://developers.redhat.com/blog/2021/05/13/why-should-developers-care-about-gitops)
- [openshift.com: Our Favorite Things from GitOps Con at KubeCon EU 🌟](https://www.openshift.com/blog/our-favorite-things-from-gitops-con-at-kubecon-eu)
- [devsecops.co.in: GitOps Guide – What, Why and How? 🌟](https://devsecops.co.in/2021/05/13/gitops-guide-what-why-and-how/)
- [en.sokube.ch: GitOps and the Millefeuille dilemma 🌟](https://en.sokube.ch/post/gitops-and-the-millefeuille-dilemma-1)
- [octopus.com: How to structure your Git repository for DevOps automation](https://octopus.com/blog/devops-automation-repo-design)
- [testingclouds.wordpress.com: GitOps Demystified](https://testingclouds.wordpress.com/2021/06/02/gitops-demystified/)
- [weave.works: Ops Automation - GitOps in the Modern Enterprise](https://www.weave.works/blog/gitops-in-the-modern-enterprise)
- [openshift.com: What is GitOps? 🌟](https://www.openshift.com/learn/topics/gitops/) While DevOps provides an agile team structure, GitOps is a framework to start executing on the vision.
- [thenewstack.io: Security Will Be Instrumental for the Success of GitOps](https://thenewstack.io/security-will-be-instrumental-for-the-success-of-gitops/)
- [weave.works: There’s More to GitOps Than Meets the Eye](https://www.weave.works/blog/theres-more-to-gitops-than-meets-the-eye)
- [solo.io: GlooOps: Progressive delivery, the GitOps way](https://www.solo.io/blog/glooops-progressive-delivery-the-gitops-way)
- [go.weave.works: The GitOps Maturity Model - 4 evolutionary steps to continuous delivery (pdf)](https://go.weave.works/2021_GitOps_Maturity_Model.html)
- [thenewstack.io: A Look at GitOps for the Modern Enterprise 🌟](https://thenewstack.io/a-look-at-gitops-for-the-modern-enterprise/)
- [shipa.io: GitOps in the enterprise 🌟](https://www.shipa.io/innovation/gitops-in-the-enterprise/)
- [itnext.io: GitOps with Kubernetes 🌟](https://itnext.io/gitops-with-kubernetes-740f37ea015b) 
- [shipa.io: GitOps meets AppOps](https://www.shipa.io/innovation/gitops-meets-appops/)
- [weave.works: Automating Kubernetes with GitOps (whitepaper) 🌟](https://go.weave.works/automating-kubernetes-with-gitops-wp.html)
- [devopslearners.com: What is GitOps?](https://devopslearners.com/what-is-gitops-168aac9a2ee) A small explanation for GitOps
- [go.weave.works: The Practical Guide to GitOps (eBook)](https://go.weave.works/gitops-ebook.html)
- [enterprisersproject.com: How to explain GitOps in plain English](https://enterprisersproject.com/article/2021/6/gitops-explained-plain-english) What is GitOps and why is it important? How can IT leaders explain GitOps to others, especially if they don’t speak DevOps or cloud-native? Experts break it down
- [redhat.com: An illustrated guide to GitOps](https://www.redhat.com/architect/illustrated-guide-gitops) Understanding the basic principles driving GitOps offers Enterprise Architects a new way of working in the modern enterprise.
- [bunnyshell.com: GitOps vs. DevOps: What’s the Difference? 🌟](https://www.bunnyshell.com/blog/gitops-vs-devops)
- [jimangel.io: Self-Updating GitOps](https://jimangel.io/post/auto-gitops-isitstillrunning.com/) Self-hosted, Self-healing, Self-updating, Self-patching Kubernetes madness
- [stevesmith.tech: GitOps is a placebo](https://www.stevesmith.tech/blog/gitops-is-a-placebo/)
- [weave.works: The History of GitOps 🌟](https://www.weave.works/blog/the-history-of-gitops)
- [opensource.com: How to get the most out of GitOps right now](https://opensource.com/article/21/8/gitops) GitOps is a great starting point to understand what is running in production, but it may need a little more augmentation to get it working just right for your engineering team.
- [redhat.com: 3 rules for applying principles of GitOps to enterprise architecture](https://www.redhat.com/architect/3-gitops-rules-architecture) Check out these three rules for using GitOps to get your enterprise architecture up and running effectively.
- [weave.works: Hardening Git for GitOps (white paper)](https://go.weave.works/hardening-git-for-gitops.html)
- [magalix.com: GitOps 101: What’s It All About?](https://www.magalix.com/blog/what-is-gitops)
- [containerjournal.com: The 4 Levels of GitOps Maturity](https://containerjournal.com/features/the-4-levels-of-gitops-maturity/)
- [thenewstack.io: How to Get the Most out of GitOps](https://thenewstack.io/how-to-get-the-most-out-of-gitops) **Just as Kubernetes was accepted as the best way to do cloud native applications, GitOps is gaining recognition as the best way to do Kubernetes.**
- [weave.works: Case Study: National Australia Bank Decreases Operational Overhead with GitOps](https://www.weave.works/blog/case-study-national-australia-bank-decreases-operational-overhead-with-gitops) New case study on how GitOps helped NAB, Australia's largest business bank decrease operational overhead for their move to EKS: "We turned to Weaveworks because of their extensive EKS and Kubernetes experience, including their close partnership with AWS".
- [betterprogramming.pub: How GitOps Can Help Prevent Security Misconfigurations](https://betterprogramming.pub/how-gitops-can-help-prevent-security-misconfigurations-8b506dcd89e1) Cloud-native development comes with its own set of security risks. Know how to tackle them
- [blogs.sap.com: Decentralized GitOps over multiple environments](https://blogs.sap.com/2021/05/06/decentralized-gitops-over-environments/)
- [thenewstack.io: Application Deployment Is Faster with GitOps](https://thenewstack.io/application-deployment-is-faster-with-gitops/)
- [As an ops engineer not too familiar with Git, you just need to know 6 commands](https://twitter.com/janakiramm) - git init, git add, git commit, git status, git log, git revert - to harness the power of GitOps.
- [thenewstack.io: Wait, Do We Need to Hold Up on GitOps?](https://thenewstack.io/wait-do-we-need-to-hold-up-on-gitops/)
- [redhat.com: How to use GitOps in your enterprise architecture strategy 🌟](https://www.redhat.com/architect/understanding-gitops) Understanding the four guiding principles is like runway lighting for implementing GitOps in your enterprise.
- [codefresh.io: The pains of GitOps 1.0](https://codefresh.io/about-gitops/pains-gitops-1-0/) GitOps as a practice for releasing software has several advantages, but like all other solutions before it, has also several shortcomings. It seems that the honeymoon period is now over, and we can finally talk about the issues of GitOps (and the current generation of GitOps tools)
- [==thenewstack.io: CNCF Working Group Sets Some Standards for ‘GitOps’==](https://thenewstack.io/cncf-working-group-sets-some-standards-for-gitops/) GitOps must meet these four requirements: 
	1. **Declarative:** A system managed by GitOps must have its desired state expressed declaratively. “You’re no longer giving instructions, you’re describing state,” Murillo described.
	2. **Versioned and Immutable:** Desired state is stored in a way that enforces immutability, versioning and retains a complete version history. “The only way for you to introduce change in your system is by creating a new version of your desired state,’ Murillo added.
	3. **Pulled Automatically:** Software agents automatically pull the desired state declarations from the source. Agents within the system pull the desired state from the repository.
	4. **Continuously Reconciled:** Software agents continuously observe the actual system state and attempt to apply the desired state. “The desired state [of the system or software] is continually reconciled, Murillo said.
- [thenewstack.io: GitOps and the Cheap Cloud Myth](https://thenewstack.io/repatriation-or-cloud-what-we-need-is-control/)

<center>
[![gitops in a nutshell](images/GitOps-in-a-nutshell.png)](https://www.unifiedguru.com/gitops-and-the-cloud-operating-model-vmware-cloud-community/)
</center>

<center>
[![app ops](images/appops.png)](https://www.shipa.io/innovation/gitops-in-the-enterprise/)
</center>

## GitOps Working Group
- [GitOps Working Group 🌟](https://github.com/gitops-working-group/gitops-working-group)
- The Five GitOps Principles (as defined by the GitOps Working Group) to the lifecycle of an infrastructure resource, like a virtual machine or load balancer:
	- Declarative Configuration (define the resource as code)
	- Version controlled (use source control to manage the resource definition)
	- Automated delivery (provision and manage the resource from the definition using automation)
	- Software Agents (implement automated configuration management for the resource)
	- Closed loop (build the delivery pipeline for integration testing for resource changes)

## Git Repositories Structures
- [GitOps: How to Ops Your Git the Right Way 🌟](https://dzone.com/articles/gitops-how-to-ops-your-git-the-right-way) In this article we’ll look into the specifics of creating Git repositories structures  —  the very core of the GitOps approach.

## GitOps Tools
- [FluxCD, ArgoCD or Jenkins X: Which Is the Right GitOps Tool for You?](https://blog.container-solutions.com/fluxcd-argocd-or-jenkins-x-which-is-the-right-gitops-tool-for-you)
- [slideshare: GitOps, Jenkins X & Future of CI/CD](https://slideshare.net/rakutentech/gitops-jenkins-x-future-of-cicd)
- [kubesandclouds.com: Werf: Fully customizable GitOps](https://kubesandclouds.com/index.php/2020/09/01/werf-gitops/)
- [searchitoperations.techtarget.com: GitOps pros grapple with Kubernetes configuration management. GitOps users seek ideal Kubernetes config tool 🌟](https://searchitoperations.techtarget.com/news/252492459/GitOps-pros-grapple-with-Kubernetes-configuration-management) Configuration management challenges GitOps early adopters, especially at large enterprises with millions of lines of Kubernetes YAML to manage. Ultimately, the industry hasn't found an ideal approach to Kubernetes configuration management, especially for GitOps.
	- [Tanka](https://tanka.dev/tutorial/jsonnet) a utility that blends Helm charts with Jsonnet, which combines the deployment speed and ubiquity of Helm charts with the more granular customizability supported by Jsonnet.
- [openshift.com: Announcing OpenShift GitOps](https://www.openshift.com/blog/announcing-openshift-gitops)
- [ibm.com: Enable GitOps](https://www.ibm.com/garage/method/practices/run/gitops/) GitOps focuses on the Ops side of DevOps and shows how operations configurations, infrastructures, and actions are like software. Everything is code and code is managed with Git.
- [openshift.com: OpenShift Pipelines and OpenShift GitOps are now Generally Available 🌟](https://www.openshift.com/blog/openshift-pipelines-and-openshift-gitops-are-now-generally-available)
- [weave.works: Weave Kubernetes Platform (WKP) Unlocks Cross Team Collaboration with Workspaces](https://www.weave.works/blog/wkp-team-workspaces-rbac)
- [blog.container-solutions.com: FluxCD, ArgoCD or Jenkins X: Which Is the Right GitOps Tool for You? 🌟](https://blog.container-solutions.com/fluxcd-argocd-jenkins-x-gitops-tools)
- [cloudogu.com: Automation Assistants: GitOps tools in comparison 🌟](https://cloudogu.com/en/blog/gitops-tools)
- [shipa.io: From Terraform to GitOps to Pulumi 🌟](https://shipa.io/2021/10/from-terraform-to-gitops-to-pulumi/) 

<center>
[![gitops pipeline](images/gitops-pipeline.png)](https://www.unifiedguru.com/gitops-and-the-cloud-operating-model-vmware-cloud-community/)
</center>

### Flux. The GitOps Operator for Kubernetes
- [Flux. The GitOps operator for Kubernetes](flux.md) 

### Kustomize. Kubernetes native configuration management
- [kustomize.io 🌟](https://kustomize.io/) Kustomize introduces a template-free way to customize application configuration that simplifies the use of off-the-shelf applications. Now, built into kubectl as apply -k.

### Flagger
- [Flagger](https://flagger.app/) Progressive Delivery Operator for Kubernetes. Release new versions of your application/services to Kubernetes like a pro with Weaveworks's Flagger.
- [partlycloudy.blog: Release to Kubernetes like a Pro with Flagger](https://partlycloudy.blog/2020/07/08/release-to-k8s-like-a-pro-with-flagger/)

### WKSctl. Weave Kubernetes System Control
* [Weave Kubernetes System Control - wksctl](https://github.com/weaveworks/wksctl) Open Source Weaveworks Kubernetes System
* [WKSctl - A New OSS Kubernetes Manager using GitOps](https://www.weave.works/blog/wksctl-a-new-oss-kubernetes-manager-using-gitops)
* [WKSctl: a Tool for Kubernetes Cluster Management Using GitOps](https://www.infoq.com/news/2020/02/wksctl-kubernetes-gitops/)

### Helm
* [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)

### Jenkins
- There are many tools in the market that have been technically built for GitOps, like [ArgoCD](https://argoproj.github.io/argo-cd/), [Flux](https://github.com/fluxcd/flux), and [Jenkins X](https://jenkins-x.io/). All these tools have in-built proficiency to implement GitOps process for you. But we are going to use our old beloved Jenkins.
- [GitOps for Kubernetes with Jenkins](https://medium.com/stakater/gitops-for-kubernetes-with-jenkins-7db6304216e0)
    - [github.com/stakater/Xposer](https://github.com/stakater/Xposer) (with fabric8 java client library for kubernetes)
- [GitOps with Jenkins and Kubernetes](https://medium.com/@abhishekbhardwaj510/gitops-with-jenkins-and-kubernetes-c20425244c73)
    - [github.com: Opstree-Go-WebApp](https://github.com/opstree/Opstree-Go-WebApp) A loaded GoLang app to do various DevOps POC's
    - [opstree.github.io](https://opstree.github.io/)

### Terraform
- [How to Create a GitOps Workflow with Terraform and Jenkins](https://www.hashicorp.com/resources/how-create-gitops-workflow-terraform-jenkins/)

### Config Sync and Anthos Config Management 
- [Config Sync](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/overview)
- [Anthos Config Management](https://cloud.google.com/anthos/config-management)
- Google built a tool called [Config Sync](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/overview) which acts as the bridge between an external source code repository and the Kubernetes API server. [Anthos Config Management](https://cloud.google.com/anthos/config-management) is based on Config Sync to extend it to multicluster scenarios.

### Portworx AutoPilot
- [Portworx AutoPilot](https://docs.portworx.com/portworx-install-with-kubernetes/autopilot/)
- [portworx.com: Automating Kubernetes Data Management with GitOps & AutoPilot](https://portworx.com/automating-kubernetes-data-management-with-gitops-autopilot)

### OpenShift Applier
- [openshift-applier](https://github.com/redhat-cop/openshift-applier)
- [dzone: GitOps With OpenShift Applier 🌟](https://dzone.com/articles/gitops-with-openshift-applier) GitOps in short is a set of practices to use Git pull requests to manage infrastructure and application configurations.

### HashiCorp Waypoint
- [waypointproject.io](https://www.waypointproject.io/) Waypoint provides a modern workflow to build, deploy, and release across platforms. Waypoint uses a single configuration file and common workflow to manage and observe deployments across platforms such as Kubernetes, Nomad, EC2, Google Cloud Run, and more.
- [hashicorp.com: Using Waypoint Runners To Enable GitOps Workflows](https://www.hashicorp.com/blog/using-waypoint-runners-to-enable-gitops-workflows) Waypoint runners perform builds, deployments, poll for Git repository changes, and allow deployments for any platform.

### Weave GitOps
- [Weave GitOps Enterprise](https://www.weave.works/product/gitops-enterprise/) 
	- Weave GitOps Enterprise is a continuous operations product that makes it easy to deploy and manage Kubernetes clusters and applications in any environment. With a single management console that lets you operate clusters running anywhere, in the public cloud, on the edge or in any hybrid scenario. Strong multi-tenancy can accelerate app delivery by providing developers with self-serve isolated workload namespaces across environments.
	- With Weave GitOps Enterprise, every change is recorded in Git – whether it's a change to application code or platform config and whoever was responsible. So you have a self-generating audit trail available at all times, and far fewer...
- [thenewstack.io: Weave GitOps Core Integrates Git with Kubernetes ](https://thenewstack.io/weave-gitops-core-integrates-git-with-kubernetes/)

## GitOps Frameworks
- [dzone: Why Now Is the Time for the Spring Boot of Infrastructure Automation 🌟](https://dzone.com/articles/why-now-is-the-time-for-the-spring-boot-of-infrast) Application teams move fast using frameworks built to boost developer productivity. Learn how a productivity framework can help your DevOps initiative succeed.
- [Kubestack 🌟](https://www.kubestack.com/): [Doc:](https://www.kubestack.com/framework/documentation) Kubestack is an open-source GitOps framework for infrastructure automation built on Terraform and Kustomize. It’s designed for teams that want to automate Kubernetes based infrastructure and not reinvent automation. Think of it this way, Kubestack is to Terraform and infrastructure automation, what Spring Boot is to Java and cloud native applications. The framework supports all three major cloud providers and has been used as the foundation for a number of real world customer projects as part of my colleagues’ and my consulting work. It is fully documented, has a step-by-step tutorial to help users get started and even includes a local [GitOps development lab](https://www.kubestack.com/framework/documentation/tutorial-build-local-lab). So you can test-drive Kubestack and learn more about GitOps for infrastructure automation in the comfort of your own localhost.
	- [thenewstack.io: KubeStack: Towards Full-Stack GitOps](https://thenewstack.io/kubestack-towards-full-stack-gitops/)

## Kubernetes Platforms and GitOps
### OpenShift GitOps
* [blog.openshift.com: Introduction to GitOps with OpenShift](https://blog.openshift.comintroduction-to-gitops-with-openshift/)
* [learn.openshift.com: GitOps introduction](https://learn.openshift.com/introduction/gitops-introduction/)
* [blog.openshift.com: is it too late to integrate GitOps?](https://blog.openshift.comis-it-too-late-to-integrate-gitops/)
* [blog.openshift.com: OpenShift Authentication Integration with ArgoCD](https://blogopenshift.com/openshift-authentication-integration-with-argocd/)
* [openshift.com: From Code to Production with GitOps, Tekton and ArgoCD](https://www.openshift.com/blog/from-code-to-production-with-gitops)
* [medium: GitOps with Istio, Tekton and Argo CD — on OpenShift 4](https://medium.com/@joelkaplan1/gitops-with-istio-tekton-and-argo-cd-on-openshift-4-5e42d22994e3)
* [thenewstack.io: Red Hat Delivers Full GitOps CI/CD Built on Tekton and Argo](https://thenewstack.io/red-hat-delivers-full-gitops-ci-cd-built-on-tekton-and-argo/)
* [redhat.com: Red Hat Makes DevOps a Reality with OpenShift GitOps and OpenShift Pipelines 🌟](https://www.redhat.com/en/about/press-releases/red-hat-makes-devops-reality-openshift-gitops-and-openshift-pipelines) New Red Hat OpenShift features provide fully-integrated CI/CD pipeline for organizations to deliver applications more consistently and with greater predictability across the open hybrid cloud.

### AWS Kubernetes
* [info.acloud.guru: Adopting GitOps for Kubernetes on AWS](https://info.acloud.guru/resources/deploying-kubernetes-with-gitops)

### Weave Kubernetes Platform
* [weave.works: Weave Kubernetes Platform](https://www.weave.works/) Automate Enterprise Kubernetes the GitOps way
* [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave)

### Ubuntu Charmed Kubernetes
* [Charmed Kubernetes](https://ubuntu.com/kubernetes/features)
* [Kubernetes GitOps with Azure Arc and Charmed Kubernetes](https://ubuntu.com/blog/gitops-with-azure-arc-and-charmed-kubernetes)

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: What is GitOps?<br><br>Is this something that you should learn?<br><br>Let&#39;s dive into it. <a href="https://t.co/hsMUesvP23">pic.twitter.com/hsMUesvP23</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1288469479693803525?ref_src=twsrc%5Etfw">July 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If you do a canary release on <a href="https://twitter.com/hashtag/Kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#Kubernetes</a> with <a href="https://twitter.com/hashtag/Istio?src=hash&amp;ref_src=twsrc%5Etfw">#Istio</a> use Flagger (<a href="https://t.co/4s6NFwvaXz">https://t.co/4s6NFwvaXz</a>). It allows e.g.:<br>🔹 run acceptance and load tests<br>🔹 do an automatic rollback<br>🔹 make a progressive traffic shifting</p>&mdash; Piotr Mińkowski (@piotr_minkowski) <a href="https://twitter.com/piotr_minkowski/status/1438802863015215108?ref_src=twsrc%5Etfw">September 17, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>

## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/IpvFd41R9Vg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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