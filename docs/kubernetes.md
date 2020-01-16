<!-- TOC -->

- [Kubernetes](#kubernetes)
    - [Local Installers](#local-installers)
    - [Production Cluster Installers](#production-cluster-installers)
    - [Rancher](#rancher) Rancher is enterprise management for Kubernetes
    - [Helm and Kubernetes](#helm-and-kubernetes)
    - [Other tools](#other-tools)
    - [Demos](#demos)
    - [Spring PetClinic Sample Application](#spring-petclinic-sample-application)
    - [SpringBoot with Docker](#springboot-with-docker)
    - [Troubleshooting](#troubleshooting)
    - [Security](#security)
    - [EKS](#eks)
    - [Docker in Docker](#docker-in-docker)
    - [Videos](#videos)

<!-- /TOC -->

# Kubernetes
* [Wikipedia.org: Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [youtube: Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [katacoda.com 🌟🌟🌟🌟](https://www.katacoda.com/) Interactive Learning and Training Platform for Software Engineers 
* [Awesome kubernetes 🌟🌟🌟🌟](https://github.com/ramitsurana/awesome-kubernetes)
* [https://www.reddit.com/r/kubernetes 🌟🌟🌟](https://www.reddit.com/r/kubernetes) 
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟🌟🌟](https://stackify.com/kubernetes-docker-deployments/)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* [Ansible for devops: Kubernetes](https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes)
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* Kubernetes Cheat Sheets:
    * [developers.redhat.com: Kubernetes Cheat Sheet 🌟](https://developers.redhat.com/cheat-sheets/kubernetes/)
    * [kubernetes.io 🌟🌟](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
    * [linuxacademy](https://linuxacademy.com/blog/containers/kubernetes-cheat-sheet/)
    * [fabric8 - kubectl](https://github.com/fabric8io/kansible/blob/master/vendor/k8s.io/kubernetes/docs/user-guide/kubectl-cheatsheet.md)
* [kubedex.com 🌟🌟🌟](https://kubedex.com/) Discover, Compare and Share Kubernetes Applications
    * [kubedex.com: autoscaling 🌟](https://kubedex.com/autoscaling)
* [Google Play: Learning Solution - Learn Kubernetes 🌟🌟🌟](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnKubernetes)
* [Google Play: TomApp - Learn Kubernetes](https://play.google.com/store/apps/details?id=tomtran.learnkubernetes)
* [Play with Kubernetes 🌟🌟🌟🌟](https://labs.play-with-k8s.com/) A simple, interactive and fun playground to learn Kubernetes
* [Intoduction to Kubernetes (slides, beginners and advanced) 🌟🌟🌟🌟🌟🌟🌟🌟](https://docs.google.com/presentation/d/1zrfVlE5r61ZNQrmXKx5gJmBcXnoa_WerHEnTxu5SMco/edit#slide=id.g3cfa019267_4_0)
* [medium.com: The Kubernetes Scheduler: this series aims to advance the understanding of Kubernetes and its underlying concepts](https://medium.com/@dominik.tornow/the-kubernetes-scheduler-cd429abac02f)
* [medium.com: A Year Of Running Kubernetes at MYOB, And The Importance Of Empathy](https://medium.com/@jpcontad/a-year-of-running-kubernetes-as-a-product-7eed1204eecd)
* [medium.com: Kubernetes 101: Pods, Nodes, Containers, and Clusters](https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16)
* [medium.com: Learn Kubernetes in Under 3 Hours: A Detailed Guide to Orchestrating Containers](https://medium.com/free-code-camp/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882)
* [kubernetestutorials.com: Install and Deploy Kubernetes on CentOs 7](https://kubernetestutorials.com/install-and-deploy-kubernetes-on-centos-7/)
* [kubernetesbyexample.com 🌟🌟🌟](http://kubernetesbyexample.com/)
* [devopscube.com: Kubernetes Tutorials For Beginners: Getting Started Guide 🌟🌟🌟](https://devopscube.com/kubernetes-tutorials-beginners/)
* [medium.com: Simplifying orchestration with Kubernetes](https://medium.com/@swapnasagarpradhan/simplifying-orchestration-with-kubernetes-e81015681a85)
* [aquasec.com: 70 Best Kubernetes Tutorials 🌟🌟🌟🌟](https://www.aquasec.com/wiki/display/containers/70+Best+Kubernetes+Tutorials) Valuable Kubernetes tutorials from multiple sources, classified into the following categories: Kubernetes AWS and Azure tutorials, networking tutorials, clustering and federation tutorials and more.
* [cloud.google.com: kubernetes comic 🌟🌟🌟](https://cloud.google.com/kubernetes-engine/kubernetes-comic/) Learn about kubernetes and how you can use it for continuous integration and delivery.
* [blogs.mulesoft.com - K8s: 8 questions about Kubernetes](https://blogs.mulesoft.com/dev/resources-dev/k8s-kubernetes/)
* [labs.mwrinfosecurity.com: Attacking Kubernetes through Kubelet](https://labs.mwrinfosecurity.com/blog/attacking-kubernetes-through-kubelet/)
* [magalix.com: Kubernetes 101 - Concepts and Why It Matters](https://www.magalix.com/blog/kubernetes-101-concepts-and-why-it-matters)
* [blog.doit-intl.com: Kubernetes and Secrets Management in the Cloud](https://blog.doit-intl.com/kubernetes-and-secrets-management-in-cloud-858533c20dca)
* **Famous Kubernetes resources of 2019:**
    * [Kubernetes for developers](https://lnkd.in/eTNwZ69)
    * [Kubernetes for the Absolute Beginners](https://lnkd.in/ecCR3vT)
    * [Kubernetes: Getting Started (Free)](https://lnkd.in/eF3ZxZ5)
    * [Kubernetes Tutorial: Learn the Basics](https://lnkd.in/e7BE7qE)
    * [Kubernetes essentials E-book 🌟🌟🌟](https://lnkd.in/ezCTYyi)
    * [Cloud-Native DevOps With Kubernetes O'Reilly book (Free) 🌟🌟🌟](https://lnkd.in/e7f2HVv)
    * [Complete Kubernetes Course](https://lnkd.in/eVG5Za9)
    * [Getting started with Kubernetes](https://lnkd.in/emPjNM9)
* [medium.com: Kubernetes Canary Deployment #1 Gitlab CI](https://medium.com/@wuestkamp/kubernetes-canary-deployment-1-gitlab-ci-518f9fdaa7ed)
* [wardviaene/kubernetes-course 🌟🌟🌟🌟](https://github.com/wardviaene/kubernetes-course) 
* [wardviaene/advanced-kubernetes-course 🌟🌟🌟🌟](https://github.com/wardviaene/advanced-kubernetes-course) 
* [dzone: The complete kubernetes collection tutorials and tools 🌟🌟🌟🌟](https://dzone.com/articles/the-complete-kubernetes-collection-tutorials-and-tools)
* [dzone: kubernetes in 10 minutes a complete guide to look](https://dzone.com/articles/kubernetes-in-10-minutes-a-complete-guide-to-look)
* [kubernetes-on-aws.readthedocs.io](https://kubernetes-on-aws.readthedocs.io/ )
* [kubernetes login](https://blog.christianposta.com/kubernetes/logging-into-a-kubernetes-cluster-with-kubectl/)
* Kubernetes Networking:
    * [dzone: how to setup kubernetes networking](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking)
    * [AWS and Kubernetes Networking Options and Trade-Offs (part 1)](https://www.weave.works/blog/introduction-to-kubernetes-pod-networking--part-1)
    * [AWS and Kubernetes Networking Options and Trade-Offs (part 2)](https://www.weave.works/blog/aws-networking-overview---part-2)
    * [AWS and Kubernetes Networking Options and Trade-Offs (part 3)](https://dzone.com/articles/aws-and-kubernetes-networking-options-and-trade-of) 
    * [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://www.ovh.com/blog/getting-external-traffic-into-kubernetes-clusterip-nodeport-loadbalancer-and-ingress/)
    * [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)
* [Kubernetes Certs](https://github.com/jetstack/cert-manager/)
* [KSS - Kubernetes pod status on steroid](https://github.com/chmouel/kss)
* Kubernetes Patterns:
    * [redhat.com: Kubernetes Patterns e-book 🌟🌟🌟🌟](https://www.redhat.com/en/engage/kubernetes-containers-architecture-s-201910240918)
    * [kubernetes.io: container design patterns](https://kubernetes.io/blog/2016/06/container-design-patterns/)
    * [magalix.com: Kubernetes Patterns - The Service Discovery Pattern 🌟🌟🌟](https://www.magalix.com/blog/kubernetes-patterns-the-service-discovery-pattern)
* [kruschecompany.com: What is a Kubernetes Operator and Where it Can be Used?](https://kruschecompany.com/kubernetes-operator/)
* [kruschecompany.com: Prometheus Operator – Installing Prometheus Monitoring Within The Kubernetes Environment](https://kruschecompany.com/kubernetes-prometheus-operator/)

## Local Installers
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [medium.com: Local Kubernetes for Linux — MiniKube vs MicroK8s](https://medium.com/containers-101/local-kubernetes-for-linux-minikube-vs-microk8s-1b2acad068d3)

## Production Cluster Installers

* [Kubernetes Cluster with Kops:](https://github.com/kubernetes/kops) 
    * Minikube and docker client are great for local setups, but not for real clusters. Kops and kubeadm are tools to spin up a production cluster. You don't need both tools, just one of them. 
    * On AWS, the best tool is **kops**
    * At some point AWS EKS (hosted kubernetes) will be available, at that point this will probably be the preferred option. (You won't need to maintain the masters).
    * For other installs, or if you can't get kops to work, you can use kubeadm
    * **kubeadm** is an alternative approach, kops is still recommended (on AWS) - you also have AWS integrations with kops automatically
    * Setup **kops** in your windows with **virtualbox.org** and **vagrantup.com** . Once downloaded, to type a new linux VM, just type in cmd/powershell:

    1. Spin up ubuntu via vagrant:
    
    ```
    C:\ubuntu> vagrant init ubuntu/xenial64
    C:\ubuntu> vagrant up
    [...]
    C:\ubuntu> vagrant ssh-config
    C:\ubuntu> vagrant ssh
    ```
    
    2. Runt kops installer:
    
    ```
    curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
    chmod +x kops-linux-amd64
    sudo mv kops-linux-amd64 /usr/local/bin/kops
    ```
* [Kubernetes Cluster with Kubeadm](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.
* [Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)
* [Kubespray](https://github.com/kubernetes-sigs/kubespray)
* [Conjure up](https://conjure-up.io/)
* [A Comparative Analysis of Kubernetes Deployment Tools: Kubespray, kops, and conjure-up](https://www.altoros.com/research-papers/a-comparative-analysis-of-kubernetes-deployment-tools-kubespray-kops-and-conjure-up-2/)
* [wecloudpro.com: Deploy HA kubernetes cluster in AWS in less than 5 minutes](http://wecloudpro.com/2020/01/13/kube-autp-aws.html)

## Rancher
* [rancher.com](https://rancher.com/)
* [Rancher.com: Setup a basic Kubernetes cluster with ease using RKE](https://rancher.com/blog/2018/2018-09-26-setup-basic-kubernetes-cluster-with-ease-using-rke/)

## Helm and Kubernetes
* [helm.sh](https://helm.sh/)
    * [helm.sh/docs](https://helm.sh/docs) 
* [GitHub: Helm, the Kubernetes Package Manager](https://github.com/helm/helm) Installing and managing Kubernetes applications
* [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4)
* [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng)
* [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8)
* [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w)
* [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o)
* [dzone: the art of the helm chart patterns](https://dzone.com/articles/the-art-of-the-helm-chart-patterns-from-the-offici)
* [dzone: 15 useful helm chart tools](https://dzone.com/articles/15-useful-helm-charts-tools)
* [dzone: create install upgrade and rollback a helm chart - part 1](https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p)
* [dzone: create install upgrade and rollback a helm chart - part 2](https://dzone.com/articles/create-install-upgrade-rollback-a-helm-chart-part)
* [dzone: cicd with kubernetes and helm](https://dzone.com/articles/cicd-with-kubernetes-and-helm)
* [dzone: do you need helm?](https://dzone.com/articles/do-you-need-helm)
* [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)
* [codefresh.io: Using Helm 3 with Helm 2 charts](https://codefresh.io/helm-tutorial/taking-helm-3-spin/)
* Helm Charts:
    * [Jenkins](https://github.com/helm/charts/tree/master/stable/jenkins) 
    * [Codecentric Jenkins](https://github.com/codecentric/helm-charts/tree/master/charts/jenkins)
    * [Nexus3](https://github.com/helm/charts/tree/master/stable/sonatype-nexus)
    * [Choerodon Nexus3](https://hub.helm.sh/charts/choerodon/nexus3)
    * [Sonar](https://github.com/helm/charts/tree/master/stable/sonarqube)
    * [Selenium](https://github.com/helm/charts/tree/master/stable/selenium)
    * [Jmeter](https://github.com/helm/charts/tree/master/stable/distributed-jmeter)
    * [bitnami: create your first helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)
* Helm Charts repositories:
    * [hub.helm.sh 🌟🌟🌟](http://hub.helm.sh) 
    * [Bitnami Helm Charts](https://bitnami.com/stacks/helm)

## Other tools
* [VMware octant 🌟🌟🌟](https://github.com/vmware/octant) A web-based, highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
* [kubectl-debug](https://github.com/aylei/kubectl-debug)

## Demos
* [kubernetesbyexample.com 🌟🌟🌟](http://kubernetesbyexample.com/)
* [github.com/eon01/kubernetes-workshop](https://github.com/eon01/kubernetes-workshop)
* [github.com/wardviaene (kubernetes, terraform, ansible, docker, etc) 🌟🌟🌟](https://github.com/wardviaene)
    * [wardviaene/jenkins-course](https://github.com/wardviaene/jenkins-course)
    * [wardviaene/kubernetes-course](https://github.com/wardviaene/kubernetes-course)
* [github.com/kubernetes-course/container_workshops](https://github.com/kubernetes-course/container_workshops)
* [Mautic](https://github.com/mautic/docker-mautic)
* [bitbucket.org: setting up a cicd pipeline with spring mvc and kubernetes on aws](https://bitbucket.org/blog/setting-up-a-ci-cd-pipeline-with-spring-mvc-jenkins-and-kubernetes-on-aws )
* [codeburst.io: getting started with kubernetes, deploy a docker container in 5 minutes](https://codeburst.io/getting-started-with-kubernetes-deploy-a-docker-container-with-kubernetes-in-5-minutes-eb4be0e96370)
* Medium.com - Simple Spring Boot microservice deployed in Kubernetes using Docker and Nexus 🌟🌟🌟:
    * [Part 1](https://medium.com/@simionrazvan/simple-spring-boot-microservice-deployed-in-kubernetes-using-docker-and-nexus-part-1-b581e3ca8916)
    * [Part 2](https://medium.com/@simionrazvan/simple-spring-boot-microservice-deployed-in-kubernetes-using-docker-and-nexus-part-2-25dc2a3982cf)
* [kublr.com: cicd pipeline with jenkins nexus kubernetes](https://kublr.com/blog/cicd-pipeline-with-jenkins-nexus-kubernetes/)

## Spring PetClinic Sample Application
* [spring-petclinic.github.io](https://spring-petclinic.github.io)
    * [spring-petclinic.github.io Docs](https://spring-petclinic.github.io/docs/resources.html)
* [github.com/spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)
    * [gitlab.beuth-hochschule.de](https://gitlab.beuth-hochschule.de/s70178/petclinic-ansible-jenkins-ci-cd)
    * [gitlab.comquent.de: Microservices branch](https://gitlab.comquent.de/petclinic/spring-petclinic-microservices)
* [deors/deors-demos-petclinic jenkinsfile](https://github.com/deors/deors-demos-petclinic/blob/master/Jenkinsfile)
* [liatrio.com: building with docker using jenkins pipelines](https://www.liatrio.com/blog/building-with-docker-using-jenkins-pipelines)
* [stackoverflow: How to define BuildConfig object with Jenkins and openshift
](https://stackoverflow.com/questions/52337851/how-to-define-buildconfig-object-with-jenkins-and-openshift)
* [cloudogu.com: CD with Jenkins, Nexus and cloudogu](https://cloudogu.com/en/blog/cd-with-nexus-jenkins-ces)
* [experfy.com e-learning: Effective Jenkins - Continuous Delivery and Continuous Integration](https://www.experfy.com/training/courses/effective-jenkins-continuous-delivery-and-continuous-integration)
* Modular Pipeline Library: 4. Petclinic Pipeline 🌟🌟🌟🌟 
    * [griddynamics/mpl](https://github.com/griddynamics/mpl)
    * [blog.griddynamics.com: Developing a modular pipeline library to improve DevOps collaboration](https://blog.griddynamics.com/developing-a-modular-pipeline-library-to-improve-devops-collaboration/)
    * [youtube: Modular Pipeline Library: 4. Petclinic Pipeline](https://www.youtube.com/watch?v=GLtvxY1S3Aw)
* PetClinic on Kubernetes:
    * [github.com/spring-petclinic/spring-petclinic-kubernetes 🌟🌟](https://github.com/spring-petclinic/spring-petclinic-kubernetes)
    * [github.com/paulczar/k8s-spring-petclinic](https://github.com/paulczar/k8s-spring-petclinic)
    * [tech.paulcz.net/blog/spring-into-kubernetes-part-1](https://tech.paulcz.net/blog/spring-into-kubernetes-part-1/)
    * [github.com/kohsuke/petclinic Jenkinsfile](https://github.com/kohsuke/petclinic/blob/master/Jenkinsfile)
    * [pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images 🌟](https://pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images/)
* PetClinic Docker images:
    * [ref 1](https://hub.docker.com/r/ibuchh/petclinic-spinnaker-jenkins)
    * [ref 2](https://hub.docker.com/r/sarjunkumar24391/petclinic)
    * [ref 3](https://hub.docker.com/r/bmoussaud/petclinic)
    * [ref 4](https://hub.docker.com/r/alwin2/petclinic-customers-service)
    * [ref 5 arey/springboot-petclinic](https://hub.docker.com/r/arey/springboot-petclinic/)
    * [ref 6](https://hub.docker.com/r/anthonydahanne/spring-petclinic)
    * [ref 7](https://hub.docker.com/r/jbrisbin/spring-petclinic/)
    * [ref 8](https://github.com/spring-projects/spring-petclinic/issues/339)
    * [ref 9 - I have a branch that adds Docker, Kubernetes and Knative into the mix - planning on submitting a PR at some point](https://github.com/trisberg/spring-petclinic/tree/kubernetes)

## SpringBoot with Docker
* [spring.io: spring boot with docker 🌟](https://spring.io/guides/gs/spring-boot-docker/)

## Troubleshooting
* [Kubernetes troubleshooting diagram 🌟🌟🌟](https://github.com/inafev/awesome-kubernetes/blob/master/docs/images/kubernetes-troubleshooting.jpg)
* [Understanding Kubernetes cluster events 🌟🌟](https://banzaicloud.com/blog/k8s-cluster-logging/)

## Security
* [cilium.io](https://cilium.io/)
* [openpolicyagent.org](https://www.openpolicyagent.org/)
    * [compile OpenPolicyAgent policies into WebAssembly and run them on the edge](https://github.com/open-policy-agent/contrib/tree/master/wasm/cloudflare-worker)
* [Dzone - devops security at scale](https://dzone.com/articles/devops-security-at-scale)
* [searchitoperations.techtarget.com: kubernetes policy project](https://searchitoperations.techtarget.com/news/252467102/Kubernetes-policy-project-takes-enterprise-IT-by-storm) 
* [Dzone - Kubernetes Policy Management with Kyverno](https://dzone.com/articles/kubernetes-policy-management-with-kyverno)
    * [github Kyverno - Kubernetes Native Policy Management](https://github.com/nirmata/kyverno/)
* [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)
* [Kubernetes Security Best Practices 🌟🌟🌟🌟](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire)
* [Pod Security Policy (SCC in OpenShift) 🌟](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
* EKS Security:
    * [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
    * [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)
    * [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/calico.html )

## EKS
* [dzone: kops VS EKS](https://dzone.com/articles/kops-vs-eks-a-comparison-guide)
* [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/)
* [eksworkshop.com](https://eksworkshop.com/ )
* [eksctl: EKS installer](https://github.com/weaveworks/eksctl)
* Deploy example microservices on EKS:
    * [eksworkshop.com/x-ray/microservices](https://eksworkshop.com/x-ray/microservices/)
    * [aws.amazon.com: Deploy a kubernetes application](https://aws.amazon.com/getting-started/projects/deploy-kubernetes-app-amazon-eks/)
    * [aws blogs: Git Push to Deploy Your App on EKS](https://aws.amazon.com/blogs/opensource/git-push-deploy-app-eks-gitkube/)
    * [medium: create your first application on aws eks kubernetes](https://medium.com/faun/create-your-first-application-on-aws-eks-kubernetes-cluster-874ee9681293)
    * [dzone: deploying a kubernetes cluster with amazon eks 🌟🌟](https://dzone.com/articles/deploying-a-kubernetes-cluster-with-amazon-eks)
    
## Docker in Docker
* [Building Docker images when running Jenkins in Kubernetes](https://www.reddit.com/r/jenkinsci/comments/ctirsc/building_docker_images_when_running_jenkins_in/)
    * [pushbuildtestdeploy.com: jenkins on kubernetes building docker images 🌟🌟](https://pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images/)
    * [ref2](https://github.com/samrocketman/docker-jenkins-jervis/blob/master/README.md#working-with-docker-in-docker)
* [itnext.io: docker in docker](https://itnext.io/docker-in-docker-521958d34efd)
* [code-maze.com: ci jenkins docker](https://code-maze.com/ci-jenkins-docker/)
* [medium: quickstart ci with jenkins and docker in docker](https://medium.com/swlh/quickstart-ci-with-jenkins-and-docker-in-docker-c3f7174ee9ff)
* [getintodevops.com: the simplest way to run docker in docker](https://getintodevops.com/blog/the-simple-way-to-run-docker-in-docker-for-ci#%3A~%3AtargetText=Building+Docker+containers+with+Jenkins+inside+a+container)
* Docker in Docker on EKS:
    * [ref1: docker build --network=host](https://github.com/awslabs/amazon-eks-ami/issues/183)
    * [ref2](https://github.com/weaveworks/eksctl/issues/942)

## Videos
<center>
    
<iframe src="https://www.youtube.com/embed/PH-2FfFD2PU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<iframe src="https://www.youtube-nocookie.com/embed/9cwjtN3gkD4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/cZ1S2Gp47ng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/CmPK93hg5w8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</center>




