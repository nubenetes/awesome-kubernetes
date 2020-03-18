<!-- TOC -->

- [Openshift](#openshift)
    - [Openshift 4](#openshift-4)
    - [Openshift 4 roadmap](#openshift-4-roadmap)
    - [Other Awesome Lists](#other-awesome-lists)
    - [Red Hat Communities of Practice](#redhat-communities-of-practice)
    - [Identity Management](#identity-management)
    - [Quota Management](#quota-management)
    - [OKD4](#okd4)
    - [Serverless with Knative](#serverless-with-knative)
    - [Helm and OpenShift](#helm-and-openShift)
    - [E-Books](#e-books)
    - [Online learning](#online-learning)
    - [Local Installers](#local-installers)
    - [Cluster Installers](#cluster-installers)
    - [Network Policy](#network-policy)
    - [Security](#security)
    - [Operators](#operators)
    - [Networking](#networking)
    - [Demos](#demos)
    - [Videos](#videos)
    - [Openshift Compliant Docker Images](#openshift-compliant-docker-images)
    - [Quay](#quay)
    - [OpenShift on AWS](#openshift-on-aws)
    - [Slides](#slides)

<!-- /TOC -->

# Openshift
* [Wikipedia.org: Openshift](https://en.wikipedia.org/wiki/OpenShift)
* [try.openshift.com 🌟🌟🌟🌟](https://try.openshift.com/) 
* [openshift.io 🌟🌟🌟](https://openshift.io/) an online IDE for building container-based apps, built for team collaboration.
* [docs.openshift.com](https://docs.openshift.com/)
* [https://github.com/openshift/origin 🌟🌟🌟](https://github.com/openshift/origin)
    * [Using Jenkins Pipelines with OpenShift 🌟](https://github.com/openshift/origin/tree/master/examples/jenkins/pipeline)
* [docs.openshift.com: OpenShift Pipeline Builds](https://docs.openshift.com/container-platform/3.10/dev_guide/dev_tutorials/openshift_pipeline.html)
* [https://hub.docker.com/u/openshift/](https://hub.docker.com/u/openshift/)
* [https://www.reddit.com/r/openshift 🌟🌟🌟](https://www.reddit.com/r/openshift)
* [PodCTL Podcasts](https://blog.openshift.com/tag/podctl/)
* [Dzone.com: OpenShift Quick Start 🌟](https://dzone.com/articles/openshift-quick-start)
* [Dzone.com: OpenShift Quick Start: Build, Deployment, and Pipeline 🌟🌟🌟](https://dzone.com/articles/openshift-quick-start-build-deployment-and-pipelin) Automation is the key to microservices success. Learn how to use the OpenShift platform to implement a continuous build and deployment platform. 
* [redhat.com: **How to gather and display metrics in Red Hat OpenShift** (Prometheus + Grafana)](https://www.redhat.com/en/blog/how-gather-and-display-metrics-red-hat-openshift)
* [claydesk.com: Google Cloud App Engine Vs Red Hat OpenShift](https://www.claydesk.com/ecampus/google-cloud-app-engine-vs-red-hat/)
* [https://github.com/fabric8io/fabric8-pipeline-library 🌟🌟🌟](https://github.com/fabric8io/fabric8-pipeline-library)
* [https://twitter.com/openshift](https://twitter.com/openshift) 
* [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes/)
* OpenShift Cheat Sheets:
    * [developers.redhat.com: Red Hat OpenShift Container Platform Cheat Sheet](https://developers.redhat.com/cheat-sheets/red-hat-openshift-container-platform/)
    * [github.com: Openshift cheat sheet 1](https://github.com/nekop/openshift-sandbox/blob/master/docs/command-cheatsheet.md)
    * [gist.github.com: Openshift cheat sheet 2](https://gist.github.com/rafaeltuelho/111850b0db31106a4d12a186e1fbc53e)
    * [github.com: openshift cheat sheet 3](https://github.com/mhausenblas/openshift-cheat-sheet)
    * [monodot.co.uk: openshift cheat sheet 4](https://monodot.co.uk/openshift-cheatsheet/)
* [Red Hat Consulting DevOps And OpenShift Playbooks 🌟🌟🌟](http://v1.uncontained.io/) Red Hat Consulting DevOps and OpenShift Playbooks are guides for implementing DevOps technical practices and container automation approaches using Red Hat commercial open source products, including OpenShift Enterprise 3. They are intended to reflect real-world experience delivering solutions through these processes and technologies.
* [certdepot.net: OpenShift Free available resources 🌟🌟🌟](https://www.certdepot.net/openshift-free-available-resources/)
* [blog.openshift.com: From zero to container deployment hero with OpenShift 3 (Video) 🌟🌟🌟](https://blog.openshift.com/openshift-3-walkthrough/)
* [blog.openshift.com: Using OpenShift 3 on your local environment 🌟](https://blog.openshift.com/using-openshift-3-on-your-local-environment/)
* [developers.redhat.com: Securing .NET Core on OpenShift using HTTPS](https://developers.redhat.com/blog/2018/10/12/securing-net-core-on-openshift-using-https/)
* [OpenShift Commons 🌟](https://commons.openshift.org/) Where users, partners, customers, and contributors come together to collaborate and work together on OpenShift.
* [ODO: OpenShift Command line for Developers 🌟🌟🌟](https://github.com/redhat-developer/odo) OpenShift Do (Odo) is a CLI tool for developers who are writing, building, and deploying applications on OpenShift. With Odo, developers get an opinionated CLI tool that supports fast, iterative development which abstracts away Kubernetes and OpenShift concepts, thus allowing them to focus on what's most important to them: code.
* Chaos Monkey for kubernetes/Openshift:
    * [reddit: Help with Kube Monkey setup](https://www.reddit.com/r/openshift/comments/e1j5qz/rbac_for_container_access_to_destroy_other/)
    * [GitHub: kube-monkey](https://github.com/asobti/kube-monkey)
    * [GitHub: monkey-ops, Openshift compliant, no cluster-admin required](https://github.com/joshmsmith/monkey-ops)
    * [chaoskube periodically kills random pods in your Kubernetes cluster](https://github.com/linki/chaoskube)
    * [Chaos Mesh](https://github.com/pingcap/chaos-mesh)
* OpenShift GitOps:
    * [blog.openshift.com: Introduction to GitOps with OpenShift](https://blog.openshift.com/introduction-to-gitops-with-openshift/)
        * [learn.openshift.com: GitOps introduction](https://learn.openshift.com/introduction/gitops-introduction/ )
    * [blog.openshift.com: is it too late to integrate GitOps?](https://blog.openshift.com/is-it-too-late-to-integrate-gitops/)
    * [blog.openshift.com: OpenShift Authentication Integration with **ArgoCD**](https://blog.openshift.com/openshift-authentication-integration-with-argocd/)
* Debugging apps 🌟🌟🌟:
    * [developers.redhat.com: Installing debugging tools into a Red Hat OpenShift container with **oc-inject**](https://developers.redhat.com/blog/2020/01/15/installing-debugging-tools-into-a-red-hat-openshift-container-with-oc-inject/)
    * [developers.redhat.com: **Debugging applications** within Red Hat OpenShift containers](https://developers.redhat.com/blog/2020/01/09/debugging-applications-within-red-hat-openshift-containers/)
* [blog.openshift.com - Kubernetes: A Pod’s Life 🌟🌟🌟](https://blog.openshift.com/kubernetes-pods-life/)
* [Container-native virtualization allows to run and manage virtual machine workloads alongside container workloads](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.2/html/container-native_virtualization/container-native-virtualization-2-1-release-notes)
* Capacity Management:
    * [blog.openshift.com/full-cluster-capacity-management-monitoring-openshift](https://blog.openshift.com/full-cluster-capacity-management-monitoring-openshift/)
    * [blog.openshift.com/full-cluster-part-2-protecting-nodes](https://blog.openshift.com/full-cluster-part-2-protecting-nodes/)
    * [full-cluster-part-3-capacity-management](https://blog.openshift.com/full-cluster-part-3-capacity-management/)
    * [blog.openshift.com/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler](https://blog.openshift.com/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler/)
    * [blog.openshift.com/how-full-is-my-cluster-part-5-a-capacity-management-dashboard](https://blog.openshift.com/how-full-is-my-cluster-part-5-a-capacity-management-dashboard/)
* OpenShift High Availability:
    * [blog.openshift.com/tag/multi-datacenter](https://blog.openshift.com/tag/multi-datacenter/)
    * [blog.openshift.com/deploying-openshift-applications-multiple-datacenters](https://blog.openshift.com/deploying-openshift-applications-multiple-datacenters/)
    * [blog.openshift.com/metro-area-openshift-stretch-cluster-how-to-survive-an-outage-and-live-to-tell-about-it](https://blog.openshift.com/metro-area-openshift-stretch-cluster-how-to-survive-an-outage-and-live-to-tell-about-it/)
    * [blog.openshift.com/stateful-workloads-and-the-two-data-center-conundrum](https://blog.openshift.com/stateful-workloads-and-the-two-data-center-conundrum/)
    * [OpenShift 3.11 Multi-cluster Federation](https://blog.openshift.com/kubernetes-federation-v2-on-openshift-3-11/)
    * [Multi-cluster Federation in OpenShift 4 is called **KubeFed**](https://blog.openshift.com/federation-v2-is-now-kubefed/)
    * [Using KubeFed to deploy applications](https://blog.openshift.com/using-kubefed-to-deploy-applications-to-ocp3-and-ocp4-clusters/)
    * [Katacoda e-learning platform – Federated Clusters](https://www.katacoda.com/openshift/courses/introduction/federated-clusters)
    * [KubeFed Operator](https://operatorhub.io/operator/kubefed-operator)
* Troubleshooting Java applications on Openshift (Openshift 3):
    * [developers.redhat.com: Troubleshooting java applications on openshift](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift/)
    * [dzone: 8 Options for Capturing Thread Dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)
* [developers.redhat.com: Handling Angular environments in continuous delivery with Red Hat OpenShift](https://developers.redhat.com/blog/2019/11/27/handling-angular-environments-in-continuous-delivery-with-red-hat-openshift/)
* [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository/)
* [developers.redhat.com: Customizing OpenShift project creation 🌟](https://developers.redhat.com/blog/2020/02/05/customizing-openshift-project-creation/)

## Other Awesome Lists
* [Awesome Openshift](https://github.com/dudash/openshift-is-awesome)
* [Awesome Openshift 2](https://github.com/oscp/awesome-openshift3)

## Red Hat Communities of Practice
* [uncontained.io](http://uncontained.io/)
    * [uncontained.io/articles/openshift-ha-installation](http://uncontained.io/articles/openshift-ha-installation/ )
    * [uncontained.io/articles/openshift-and-the-org](http://uncontained.io/articles/openshift-and-the-org/) 
* [v1.uncontained.io](http://v1.uncontained.io/) Red Hat Consulting DevOps & OpenShift Playbooks
* [Red Hat Communities of Practice](https://github.com/redhat-cop)
* [OpenShift Toolkit 🌟🌟🌟🌟](https://github.com/redhat-cop/openshift-toolkit/)
* [OpenShift Container Pipelines 🌟🌟🌟](https://github.com/redhat-cop/container-pipelines)
* [OpenShift Pipeline Library 🌟🌟🌟](https://github.com/redhat-cop/pipeline-library)
* [OpenShift Playbooks](https://github.com/redhat-cop/openshift-playbooks)

## Identity Management
* [GitHub redhat-cop: Ansible Role](https://github.com/redhat-cop/infra-ansible/tree/master/roles/identity-management )

## Quota Management
* [GitHub redhat-cop: OpenShift Toolkit - Quota Management 🌟🌟🌟🌟](https://github.com/redhat-cop/openshift-toolkit/tree/master/quota-management)
* [OpenShift 4 Resource Management](https://www.youtube.com/watch?v=JC_PB1yZcIc)
* [techbeatly.com: How to create, increase or decrease project quota](https://www.techbeatly.com/2018/11/how-to-create-increase-or-decrease-project-quota-in-openshift.html/#.Xd5OE9WCGUk)
* [Quotas setting per project](https://docs.openshift.com/container-platform/4.2/applications/quotas/quotas-setting-per-project.html)
* [Quotas setting across multiple projects](https://docs.openshift.com/container-platform/4.2/applications/quotas/quotas-setting-across-multiple-projects.html)

## Openshift 4
* [blog.openshift.com: Introducing Red Hat OpenShift 4](https://blog.openshift.com/introducing-red-hat-openshift-4/)
* [Dzone: What’s in OpenShift 4?](https://dzone.com/articles/whats-in-openshift-4)
* [youtube: Installing OpenShift 4 on AWS with operatorhub.io integration 🌟🌟🌟🌟](https://www.youtube.com/watch?v=kQJxGtsqphk)
* [blog.openshift.com: OpenShift 4 Install Experience](https://blog.openshift.com/openshift-4-install-experience/)
* [operatorhub.io](https://operatorhub.io/) OperatorHub.io is a new home for the Kubernetes community to share Operators. Find an existing Operator or list your own today.
* [developers.redhat.com: Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4/)
* Tekton CI/CD pipelines:
    * [https://blog.openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://blog.openshift.com/cloud-native-ci-cd-with-openshift-pipelines/)
    * [github.com: Tekton pipelines](https://github.com/tektoncd/pipeline)
    * [OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab)
* [youtube: OpenShift 4 OAuth Identity Providers](https://www.youtube.com/watch?v=eFxFtUpAT9s)
* [cloudowski.com: Honest review of OpenShift 4 🌟🌟🌟🌟](https://cloudowski.com/articles/honest-review-of-openshift-4/)
* OpenShift 4 Training:
    * [github.com: Openshift 4 training](https://github.com/openshift/training)
    * [learn.openshift.com](https://learn.openshift.com/)
    * [learn.crunchydata.com](https://learn.crunchydata.com/)
* [kubevirt.io 🌟🌟🌟🌟](https://kubevirt.io/)
* [Getting Started with KubeVirt Containers and Virtual Machines Together](https://blog.openshift.com/getting-started-with-kubevirt/)
* [Open Policy Agent 🌟🌟🌟](https://www.openpolicyagent.org/)
* [blog.openshift.com: Fine-Grained Policy Enforcement in OpenShift with Open Policy Agent 🌟🌟](https://blog.openshift.com/fine-grained-policy-enforcement-in-openshift-with-open-policy-agent/)
* [OpenShift 4.2 documentation 🌟🌟🌟](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.2/)
* [OpenShift Youtube](https://www.youtube.com/user/rhopenshift/videos)
* [Enabling OpenShift 4 Clusters to Stop and Resume Cluster VMs](https://blog.openshift.com/enabling-openshift-4-clusters-to-stop-and-resume-cluster-vms/)
* [youtube: OpenShift on Google Cloud, AWS, Azure and localhost](https://www.youtube.com/watch?v=G-baPg3XhBo)
* [blog.openshift.com: Simplifying OpenShift Case Information Gathering Workflow: **Must-Gather Operator** (In the context of Red Hat OpenShift 4.x and Kubernetes, it is considered a bad practice to ssh into a node and perform debugging actions) 🌟🌟🌟🌟](https://blog.openshift.com/simplifying-openshift-case-information-gathering-workflow-must-gather-operator/)
* [blog.openshift.com: Introducing Red Hat OpenShift 4.3 to Enhance Kubernetes Security 🌟🌟🌟](https://blog.openshift.com/introducing-red-hat-openshift-4-3-to-enhance-kubernetes-security/) OpenShift 4.3 adds new capabilities and platforms to the installer, helping customers to embrace their company’s best security practices and gain greater access control across hybrid cloud environments. Customers can deploy OpenShift clusters to customer-managed, pre-existing VPN / VPC (Virtual Private Network / Virtual Private Cloud) and subnets on AWS, Microsoft Azure and Google Cloud Platform. They can also install OpenShift clusters with private facing load balancer endpoints, not publicly accessible from the Internet, on AWS, Azure and GCP.
    * [containerjournal.com: Red Hat Delivers Latest Kubernetes Enhancements](https://containerjournal.com/topics/container-management/red-hat-delivers-latest-kubernetes-enhancements/)
    * [Create an OpenShift 4.2 Private Cluster in AWS 🌟](https://access.redhat.com/solutions/4363731)
    * [cloud.ibm.com: openshift-security](https://cloud.ibm.com/docs/openshift?topic=openshift-security)
    * [docs.aporeto.com: OpenShift Master API Protection](https://docs.aporeto.com/docs/main/guides/okd-master-api-protection/)
* [youtube: Getting Started with OpenShift 4 Security 🌟🌟🌟](https://www.redhat.com/en/about/videos/getting-started-openshift-4-security)
* [blog.openshift.com: Migrating your applications to OpenShift 4 🌟🌟🌟](https://blog.openshift.com/migrating-your-applications-to-openshift-4/)
* Red Hat CodeReady containers:
    * [Red Hat OpenShift 4.2 on your laptop: Introducing **Red Hat CodeReady Containers** 🌟🌟🌟
](https://developers.redhat.com/blog/2019/09/05/red-hat-openshift-4-on-your-laptop-introducing-red-hat-codeready-containers/)
    * [dzone: Code Ready Containers - Decision Management Developer Tools Update](https://dzone.com/articles/code-ready-containers-decision-management-develope)
* [blog.openshift.com: Configure the OpenShift Image Registry backed by OpenShift Container Storage](https://blog.openshift.com/configure-the-openshift-image-registry-backed-by-openshift-container-storage/)
* **OpenShift Hive: Cluster-as-a-Service. Easily provision new PaaS environments for developers**
    * OpenShift Hive is an operator which enables operations teams to easily provision new PaaS environments for developers improving productivity and reducing process burden due to internal IT regulations.
    * [blog.openshift.com: openshift hive cluster as a service](https://blog.openshift.com/openshift-hive-cluster-as-a-service/)
    * [youtube: how to deliver OpenShift as a service (just like Red Hat)](https://www.youtube.com/watch?v=b_NOrGxfH5Y)
* Kubestone - Benchmarking Operator for K8s and OpenShift:
    * [kubestone.io](https://kubestone.io)
    * [https://operatorhub.io/operator/kubestone](https://operatorhub.io/operator/kubestone)
* [youtube playlist: London 2020 | OpenShift Commons Gathering 🌟🌟🌟](https://www.youtube.com/playlist?list=PLaR6Rq6Z4Iqcy9rg0JF6SCFst5lyyftQ-) OCP4 Updates & Roadmaps, Customer Stories, OpenShift Hive (case study), Operator Ecosystem. 
* **OpenShift Cost Management**:
    * [blog.openshift.com: Tech Preview: Get visibility into your OpenShift costs across your hybrid infrastructure](https://blog.openshift.com/tech-preview-get-visibility-into-your-openshift-costs-across-your-hybrid-infrastructure/)
* [blog.openshift.com: OpenShift Scale: Running 500 Pods Per Node 🌟🌟🌟](https://blog.openshift.com/500_pods_per_node/)

## OpenShift 4 roadmap
* [blog.openshift.com: OpenShift 4 Roadmap (slides) 🌟🌟🌟🌟](https://blog.openshift.com/wp-content/uploads/Red-Hat-OpenShift-4.0-Roadmap-Public-Feb-2019-Ali.pdf)
* [blog.openshift.com: OpenShift Container Storage (OCS 3 & 4 slides) 🌟🌟🌟🌟](https://blog.openshift.com/wp-content/uploads/OPENSHIFT-CONTAINER-STORAGE.pdf)
* [blog.openshift.com: OpenShift 4 Roadmap Update (slides) 🌟🌟🌟🌟](https://blog.openshift.com/wp-content/uploads/OpenShift-4-Roadmap-Update-William-Markito-and-Chris-Blum.pdf)

## OKD4
* [docs.okd.io 🌟🌟🌟](https://docs.okd.io/)
* [GitHub: OKD4](https://github.com/openshift/okd/blob/master/README.md)
* [youtube.com: OKD4](https://www.youtube.com/watch?v=_nl-45ulj1s)
* [blog.openshift.com: OKD4 Roadmap: The Road To OKD4: Operators, FCOS and K8S 🌟🌟🌟](https://blog.openshift.com/wp-content/uploads/DevConf-CZ-2020_OKD4_FCOS__Mueller.pdf)
* [github.com: OKD 4 Roadmap](https://github.com/openshift/community/blob/master/ROADMAP.md)

## Serverless with Knative
* [redhat.com: What is knative?](https://www.redhat.com/en/topics/microservices/what-is-knative)
* [developers.redhat.com: Serverless Architecture](https://developers.redhat.com/topics/serverless-architecture/)
* [datacenterknowledge.com: Explaining Knative, the Project to Liberate Serverless from Cloud Giants](https://www.datacenterknowledge.com/open-source/explaining-knative-project-liberate-serverless-cloud-giants)
* [knative-tutorial](https://github.com/redhat-developer-demos/knative-tutorial) A pratical guide to get started with knative. Knative concepts are explained simple and easy way with lots of demos and exercises.
* [Announcing OpenShift Serverless 1.5.0 Tech Preview – A sneak peek of our GA](https://blog.openshift.com/announcing-openshift-serverless-1-5-0-tech-preview-a-sneak-peek-of-our-ga/)

## Helm and OpenShift
* [blog.openshift.com: From Templates to Openshift Helm Charts](https://blog.openshift.com/from-templates-to-openshift-helm-charts/)
* [Templating on OpenShift: should I use Helm templates or OpenShift templates? 🌟🌟🌟](https://www.padok.fr/en/blog/templating-openshift-helm-templates)
* Helm Charts and OpenShift 4:
    * [The supported method of using Helm charts with Openshift4 is via the Helm Operator](https://blog.openshift.com/build-kubernetes-operators-from-helm-charts-in-5-steps/)
    * [youtube](https://www.youtube.com/watch?v=6NM6sqXIsoA)
    * [blog.openshift.com: Helm and Operators on OpenShift, Part 1](https://blog.openshift.com/helm-and-operators-on-openshift-part-1/)
    * [blog.openshift.com: Helm and Operators on OpenShift, Part 2](https://blog.openshift.com/helm-and-operators-on-openshift-part-2/)

## E-books
* [O'Reilly Free Book: DevOps with OpenShift](https://www.openshift.com/devops-with-openshift/)
* [O'Reilly Free Book: Openshift for developers](https://www.openshift.com/for-developers/)
* [O’Reilly: Free ebook: Kubernetes Operators: Automating the Container Orchestration Platform](https://www.redhat.com/en/resources/oreilly-kubernetes-operators-automation-ebook)
* [Manning: Openshift in action](https://www.manning.com/books/openshift-in-action)
* [Packt publishing: Learn Openshift](https://www.packtpub.com/application-development/learn-openshift)

## Online Learning
* [learn.openshift.com 🌟🌟🌟🌟](https://learn.openshift.com) Interactive Learning Portal
* [katacoda.com 🌟🌟🌟🌟](https://www.katacoda.com/) Interactive Learning and Training Platform for Software Engineers 
* [Red Hat Tutorials & Examples: github.com/redhat-developer-demos 🌟🌟🌟](https://github.com/redhat-developer-demos)
* [redhatgov.io 🌟🌟](http://redhatgov.io/)
* [udemy.com: Red Hat OpenShift With Jenkins: DevOps For Beginners](https://www.udemy.com/red-hat-openshift)
* [udemy.com: OpenShift Enterprise v3.2 Installation and Configuration](https://www.udemy.com/openshift-enterprise-installation-and-configuration/learn/v4/overview)
* [udemy.com: Ultimate Openshift (2018) Bootcamp by School of Devops 🌟🌟🌟](https://www.udemy.com/ultimate-openshift-bootcamp-by-school-of-devops/) With Openshift Origin 3.10 / OKD 2018, Kubernetes, Jenkins Pipelines, Prometheus, Istio, Micro Services, PaaS

## Local Installers
* [developers.redhat.com: **Red Hat Container Development Kit**](https://developers.redhat.com/products/cdk/overview/)
* [Fabric8.io Microservices Development Platform](https://fabric8.io/) It is an open source microservices platform based on Docker, Kubernetes and Jenkins. It is built by the Red Hat guys.The purpose of the project is to make it easy to create microservices, build, test and deploy them via Continuous Delivery pipelines then run and manage them with Continuous Improvement and ChatOps. Fabric8 installs and configures the following things for you automatically: Jenkins, Gogs, Fabric8 registry, Nexus, SonarQube.
* A few other options to use OKD locally include [oc cluster up](https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md) and [minishift](https://www.okd.io/minishift/). These may be a better fit for your use case if you only need a quick throwaway environment.
* [github.com/redhatdemocentral: OpenShift Container Platform Install Demo 🌟🌟](https://github.com/redhatdemocentral/ocp-install-demo)
    * [Dzone.com: Installing OpenShift Container Platform v3.5 in Minutes](https://dzone.com/articles/installing-openshift-container-platform-v35-in-min)
    * [Dzone.com: Install OpenShift Container Platform 3.6 in Minutes](https://dzone.com/articles/cloud-happiness-install-openshift-container-platfo)
    * [Dzone.com: How to Install New OpenShift Container Platform 3.7](https://dzone.com/articles/cloud-happiness-how-to-install-new-openshift-conta-2)
    * [Dzone.com: Install OpenShift Container Platform in Minutes [Video]](https://dzone.com/articles/install-openshift-container-platform-in-minutes-video)

## Cluster Installers
* [blog.openshift.com: Installing OKD 3.10 on a Single Host 🌟🌟🌟🌟](https://blog.openshift.com/installing-okd-3-10-on-a-single-host/)
    * [youtube.com: OpenShift Origin is now OKD. Installation of OKD 3.10 from start to finish](https://www.youtube.com/watch?v=ZkFIozGY0IA)
    * [Install RedHat OKD 3.10 on your development box:](https://github.com/gshipley/installcentos) This repository is a set of scripts that will allow you easily install the latest version (3.10) of OKD in a single node fashion. What that means is that all of the services required for OKD to function (master, node, etcd, etc.) will all be installed on a single host. The script supports a custom hostname which you can provide using the interactive mode.]
* [docs.okd.io: Planning your installation](https://docs.okd.io/latest/install/)
* [belgium.devoteam.com: Using Ansible Tower to deploy OpenShift 3 on Azure: a step-by-step guide](https://belgium.devoteam.com/blog/ansible-tower-openshift-azure-tower-installation-prerequisites/)
* [github.com/openshift/installer openshift installer 🌟🌟🌟](https://github.com/openshift/installer)
* [CI/CD Pipeline to deploy OpenShift Container Platform 4.x to AWS 🌟](https://github.com/r3dact3d/rhocp4_aws)
* [blog.openshift.com: 9 steps to awesome with kubernetes openshift](https://blog.openshift.com/9-steps-to-awesome-with-kubernetes-openshift-presented-by-burr-sutter/)
    * [github: burrsutter/9stepsawesome](https://github.com/burrsutter/9stepsawesome) 
* OpenShift 4.2 deployment on vSphere:
    * [reddit](https://www.reddit.com/r/openshift/comments/e1kw48/openshift_42_vsphere_install/)
    * [blog.openshift.com: OpenShift 4.2 vSphere Install Quickstart](https://blog.openshift.com/openshift-4-2-vsphere-install-quickstart/) 
    * [blog.openshift.com: OpenShift 4.2 vsphere install with static IPs 🌟🌟🌟](https://blog.openshift.com/openshift-4-2-vsphere-install-with-static-ips/)
    * [youtube](https://www.youtube.com/watch?v=DLB9m17aGus)    
 
## Network Policy
* [GitHub - redhat-cop - OpenShift toolkit 🌟🌟🌟🌟](https://github.com/redhat-cop/openshift-toolkit/tree/master/networkpolicy)

## Security
- [OpenShift and Network Security Zones: Coexistence Approaches 🌟🌟🌟🌟](https://blog.openshift.com/openshift-and-network-security-zones-coexistence-approaches/)
- How is OpenShift Container Platform Secured?:
    - [docs.openshift.com/container-platform/3.11/architecture/index.html](https://docs.openshift.com/container-platform/3.11/architecture/index.html)
    - [docs.openshift.com/container-platform/3.11/security/securing_container_platform.html](https://docs.openshift.com/container-platform/3.11/security/securing_container_platform.html)
    - [ocs.openshift.com/container-platform/4.2/authentication/understanding-authentication.html](https://docs.openshift.com/container-platform/4.2/authentication/understanding-authentication.html)
- [docs.openshift.com: Managing Security Context Constraints](https://docs.openshift.com/container-platform/3.11/admin_guide/manage_scc.html)
    - [docs.openshift.com: Managing Security Context Constraints. Security Context Constraints](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#security-context-constraints)
- [Dzone: Understanding OpenShift Security Context Constraints](https://dzone.com/articles/understanding-openshift-security-context-constrain)

```
Review Security Context Constraints
Security Context Constraints (SCCs) control what actions pods can perform and what resources they can access. 
SCCs combine a set of security configurations into a single policy object that can be applied to pods. These security configurations include, but are not limited to, Linux Capabilities, Seccomp Profiles, User and Group ID Ranges, and types of mounts.

OpenShift ships with several SCCs. The most constrained is the restricted SCC, and the least constrained in the privileged SCC. 
The other SCCs provide intermediate levels of constraint for various use cases. The restricted SCC is granted to all authenticated users by default.

The default SCC for most pods should be the restricted SCC. If required, a cluster administrator may allow certain pods to run with different SCCs. Pods should be run with the most restrictive SCC possible.

Pods inherit their SCC from the Service Account used to run the pod. With the default project template, new projects get a Service Account named default that is used to run pods. This default service account is only granted the ability to run the restricted SCC.

Recommendation:
Use OpenShift's Security Context Constraint feature, which has been contributed to Kubernetes as Pod Security Policies. PSPs are still beta in Kubernetes 1.10, 1.11, and 1.12.
Use the restricted SCC as the default 
For pods that require additional access, use the SCC that grants the least amount of additional privileges or create a custom SCC
Audit
To show all available SCCs:
oc describe scc
To audit a single pod:
oc describe pod <POD> | grep openshift.io\/scc
Remediation
Apply the SCC with the least privilege required
```

## Operators
- [OLM operator lifecycle manager](https://github.com/operator-framework/operator-lifecycle-manager/blob/master/Documentation/design/architecture.md)
- [Top Kubernetes Operators](https://blog.openshift.com/top-kubernetes-operators-advancing-across-the-operator-capability-model/)
- [operatorhub.io](https://operatorhub.io/)
- [learn.crunchydata.com](https://learn.crunchydata.com/) 
- [developers.redhat.com: Operator pattern: REST API for Kubernetes and Red Hat OpenShift 🌟🌟🌟](https://developers.redhat.com/blog/2020/01/22/operator-pattern-rest-api-for-kubernetes-and-red-hat-openshift/)

## Networking
- [Using sidecars to analyze and debug network traffic in OpenShift and Kubernetes pods](https://developers.redhat.com/blog/2019/02/27/sidecars-analyze-debug-network-traffic-kubernetes-pod/)
* [developers.redhat.com: Skupper.io: Let your services communicate across Kubernetes clusters](https://developers.redhat.com/blog/2020/01/01/skupper-io-let-your-services-communicate-across-kubernetes-clusters/)
* [blog.openshift.com: Troubleshooting OpenShift network performance with a netperf DaemonSet](https://blog.openshift.com/troubleshooting-openshift-network-performance-with-a-netperf-daemonset/)
* [blog.openshift.com: Advanced Network customizations for OpenShift Install](https://blog.openshift.com/advanced-network-customizations-for-openshift-install/)

## Demos
* [kubernetesbyexample.com 🌟🌟🌟](http://kubernetesbyexample.com/)
* [github Red Hat Tutorials & Examples 🌟🌟🌟🌟](https://github.com/redhat-developer-demos)
* [redhatgov.io](http://redhatgov.io) RedHatGov.io is an open source collection of workshop materials that cover various topics relating to Red Hat's product portfolio.
* [Deploying Docker Images to OpenShift](https://dzone.com/articles/deploying-docker-images-to-openshift) We take a look at how to deploy a Docker image from DockerHub into RedHat's OpenShift environment, bringing added functionality along the way.
* [Deploying PostgreSQL in MiniShift/OpenShift 3](https://blog.dbi-services.com/deploying-postgresql-in-minishiftopenshift/)
* [Clustering WildFly on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/clustering-wildfly-on-openshift-using-wildfly-operator)
* [Java EE example on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/java-ee-example-application-on-openshift)
* [Microprofile example on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/running-microprofile-applications-on-openshift)
* [Deploying WildFly apps on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/using-wildfly-on-openshift)
* [Running Thorntail apps on Openshift](http://www.mastertheboss.com/soa-cloud/openshift/thorntail-on-openshift)
* [Running Spring Boot applications on Openshift](http://www.mastertheboss.com/jboss-frameworks/spring/deploy-your-springboot-applications-on-openshift)
* [github.com/openshiftdemos 🌟🌟](https://github.com/openshiftdemos)
* [github.com/openshift-labs 🌟🌟](https://github.com/openshift-labs)

## Openshift Compliant Docker Images
- [Red Hat Container Catalog - RedHat Registry (registry.redhat.io)](https://access.redhat.com/containers/) License required
- [DockerHub openshift](https://hub.docker.com/r/openshift/)
- [https://github.com/sclorg/](https://github.com/sclorg/)
- [https://github.com/sclorg/postgresql-container/](https://github.com/sclorg/)
- [https://github.com/sclorg/mariadb-container](https://github.com/sclorg/mariadb-container)

## Quay
* [Red Hat Introduces open source Project Quay container registry](https://www.redhat.com/en/blog/red-hat-introduces-open-source-project-quay-container-registry)
* [Red Hat Quay](https://www.openshift.com/products/quay)
* [projectquay.io](https://www.projectquay.io/)
* [quay.io](https://quay.io/)
* [GitHub Quay (OSS)](https://github.com/quay/quay)
* [blog.openshift.com: Introducing Red Hat Quay](https://blog.openshift.com/introducing-red-hat-quay/)
* [operatorhub.io/operator/quay](https://operatorhub.io/operator/quay)

## OpenShift on AWS
* [blog.openshift.com: AWS and red hat quickstart workshop](https://blog.openshift.com/aws-and-red-hat-quickstart-workshop/)
* [aws.amazon.com: AWS Quick Start (OpenShift 3.11 on AWS)](https://aws.amazon.com/quickstart/architecture/openshift/) View deployment guide

## Videos
<iframe src="https://www.youtube.com/embed/yFPYGeKwmpk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/qaIROwHUm54" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/Rj0We91ec9Y" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/B0bziEVHyqg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/mgR0BspLr1w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/_zDDAwLctUg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/WwQ62OyCNz4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Slides
<iframe src="//www.slideshare.net/slideshow/embed_code/key/qUTP0wDDEH9bVo" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen class="video"> </iframe>
