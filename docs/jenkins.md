# Jenkins & CloudBees
- [Jenkins](#jenkins)
- [Awesome Jenkins](#awesome-jenkins)
- [Jenkins Cheat Sheet](#jenkins-cheat-sheet)
- [Online Learning](#online-learning)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Jenkins Architecture. Performance and Scalability](#jenkins-architecture-performance-and-scalability)
- [Ansible and Jenkins. Running Ansible Playbooks From Jenkins](#ansible-and-jenkins-running-ansible-playbooks-from-jenkins)
- [Jenkins Plugins](#jenkins-plugins)
    - [Selection of Jenkins Plugins](#selection-of-jenkins-plugins)
    - [Job DSL Plugin (Jenkins Job DSL API used in Jenkins Pipelines)](#job-dsl-plugin-jenkins-job-dsl-api-used-in-jenkins-pipelines)
    - [Jenkins Configuration as Code Plugin](#jenkins-configuration-as-code-plugin)
    - [Jenkins Blue Ocean](#jenkins-blue-ocean)
    - [Cloudbees Flow](#cloudbees-flow)
- [Monitoring jenkins](#monitoring-jenkins)
- [Jenkins and Spring Boot](#jenkins-and-spring-boot)
- [Kubernetes Native Jenkins Operator](#kubernetes-native-jenkins-operator)
- [Jervis: Jenkins as a service](#jervis-jenkins-as-a-service)
- [Jenkins X](#jenkins-x)

## Jenkins
* [CloudBees](https://www.cloudbees.com/)
* [Wikipedia.org: Jenkins Software](https://en.wikipedia.org/wiki/Jenkins_(software))
* [Jenkins.io (new Jenkins 2.0 site) 🌟🌟🌟🌟](https://jenkins.io/)
* [jenkinsci.github.io 🌟🌟🌟🌟](http://jenkinsci.github.io/)
* [Official Jenkins Docker image](https://github.com/michaelneale/jenkins-ci.org-docker)
* [github.com/jenkinsci 🌟🌟🌟🌟](https://github.com/jenkinsci)
* [reddit.com/r/jenkinsci 🌟🌟🌟🌟](https://www.reddit.com/r/jenkinsci) 
* [dzone: getting started with jenkins the ultimate guide](https://dzone.com/articles/getting-started-with-jenkins-the-ultimate-guide)
* [dzone: jenkins in a nutshell](https://dzone.com/articles/jenkins-in-a-nutshell)
* [opensource.com: running jenkins builds containers 🌟](https://opensource.com/article/18/4/running-jenkins-builds-containers)
* [WebSocket support in now available for Jenkins CLI and agent networking!](https://jenkins.io/blog/2020/02/02/web-socket/)
* [webhookrelay.com: Receive Github webhooks on Jenkins without public IP 🌟🌟](https://webhookrelay.com/blog/2017/11/23/github-jenkins-guide/)
* [Dzone refcard: Jenkins on PaaS](https://dzone.com/refcardz/jenkins-paas) Continuous Integration with Jenkins for Java Projects. Includes a review of the most useful plugins, best practices, security, integration to an enterprise environment, and more.

## Awesome Jenkins
* [sahilsk/awesome-jenkins](https://github.com/sahilsk/awesome-jenkins)
* [Hacking jenkins](https://github.com/orangetw/awesome-jenkins-rce-2019)

## Jenkins Cheat Sheet
* [edureka.co: Jenkins Cheat Sheet 🌟🌟🌟🌟](https://www.edureka.co/blog/cheatsheets/jenkins-cheat-sheet/)
* [medium: Jenkins Cheat Sheet](https://medium.com/edureka/jenkins-cheat-sheet-e0f7e25558a3)
* [cheatography.com: Jenkins Cheat Sheet](https://cheatography.com/funthomas424242/cheat-sheets/jenkins/)

## Online Learning
* [udemy.com: Master Jenkins CI For DevOps and Developers](https://www.udemy.com/the-complete-jenkins-course-for-developers-and-devops/)
* [udemy.com: Learn DevOps: CI/CD with Jenkins using Pipelines and Docker](https://www.udemy.com/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker/) Use Jenkins the DevOps way. Automate your Jenkins jobs by using Jenkins Pipelines, Docker, and the Jenkins Job DSL
* [wardviaene/jenkins-course](https://github.com/wardviaene/jenkins-course) 🌟🌟🌟🌟

## Jenkins Pipeline
* [jenkins.io - doc/book/pipeline 🌟🌟🌟](https://jenkins.io/doc/book/pipeline/)
* [jenkins.io - **jenkinsfile** 🌟🌟🌟](https://jenkins.io/doc/book/pipeline/jenkinsfile/) With **version 2** of the Jenkins Continuous Integration/Continuous Delivery (CI/CD) server, **a new job definition file has been introduced, called Jenkinsfile**. The initial Jenkinsfile format was based on Groovy. As groovy knowledge is not that widespread, a new and more straight forward was published in spring 2017. **This format is called Declarative Pipeline**. [This visual studio code extension](https://marketplace.visualstudio.com/items?itemName=jmMeessen.jenkins-declarative-support) is aimed at making the manipulation of this file type easier.
* [Dzone refcard: **Continuous Delivery with Jenkins Workflow** 🌟🌟](https://dzone.com/refcardz/continuous-delivery-with-jenkins-workflow)
* [GitHub Gist - Faheetah/Jenkinsfile.groovy: **Jenkinsfile idiosynchrasies with escaping and quotes**](https://gist.github.com/Faheetah/e11bd0315c34ed32e681616e41279ef4)
* [jenkins.io: Jenkins CD and Pipelines Microsite](https://jenkins.io/solutions/pipeline/)
* [dzone.com: Jenkins Pipeline - Software Delivery Made Easy](https://dzone.com/articles/jenkins-pipeline-software-delivery-made-easy) Jenkins 2.0 has focused on solving the problem for organizations wanting to continuously deliver software.
* [DZone refcard: declarative pipeline with jenkins 🌟🌟](https://dzone.com/refcardz/declarative-pipeline-with-jenkins)
* [sdtimes.com: CI/CD pipelines are expanding 🌟🌟🌟](https://sdtimes.com/devops/ci-cd-pipelines-are-expanding/) The “basic” CI/CD pipeline includes five processes, which are: merge, build, test, package and deploy. All of these are individually defined so readers have a common reference point. The basic pipeline includes sub-pipelines associated with each step, such as moving artifacts from a build into a repository.
* [magalix.com: Create a CI/CD pipeline with Kubernetes and Jenkins (Ansible, Docker, Golang App) 🌟🌟🌟](https://www.magalix.com/blog/create-a-ci/cd-pipeline-with-kubernetes-and-jenkins)
* [dzone: learn how to setup a cicd pipeline from scratch 🌟🌟🌟](https://dzone.com/articles/learn-how-to-setup-a-cicd-pipeline-from-scratch)
* [dzone: how to use basic jenkins pipelines](https://dzone.com/articles/how-to-use-basic-jenkins-pipelines)
* [opensource.com - building cicd pipelines with jenkins 🌟🌟🌟](https://opensource.com/article/19/9/intro-building-cicd-pipelines-jenkins)
* [opensource.com: Jenkins Pipeline as Code Tutorial For Beginners 🌟🌟🌟](https://devopscube.com/jenkins-pipeline-as-code/)
* [loves.cloud: CI/CD Pipeline Using Docker and Jenkins](https://loves.cloud/ci-cd-pipeline-using-docker-and-jenkins/)
    * [github.com/LovesCloud/java-groovy-docker](https://github.com/LovesCloud/java-groovy-docker/) 
* [medium: jenkins cicd getting started with groovy and docker](https://medium.com/@fvtool/jenkins-cicd-getting-started-with-groovy-and-docker-containers-part-2-b03a1b934a49)
* [Dzone: Top 10 Best Practices for Jenkins Pipeline](https://dzone.com/articles/top-10-best-practices-for-jenkins-pipeline)
* [opensource.com - Introduction to writing pipelines-as-code and implementing DevOps with Jenkins 2](https://opensource.com/article/18/8/devops-jenkins-2)
* [thoughtworks.com: Modernizing your build pipelines 🌟🌟🌟](https://www.thoughtworks.com/es/insights/blog/modernizing-your-build-pipelines)

## Jenkins Architecture. Performance and Scalability
* [devopscube.com: Jenkins Architecture Explained – Beginners Guide](https://devopscube.com/jenkins-architecture-explained/)
* [dzone: how to setup scalable jenkins on top of a kubernetes cluster](https://dzone.com/articles/how-to-setup-scalable-jenkins-on-top-of-a-kubernet)
* [devops.com: kubernetes jenkins master slave scalability](https://devops.com/kubernetes-jenkins-master-slave-scaling-the-scalability-issue/)
* [rancher.com: scaling jenkins](https://rancher.com/blog/2018/2018-11-27-scaling-jenkins/)
* [rancher.com: Deploying and Scaling Jenkins on Kubernetes 🌟🌟🌟](https://rancher.com/blog/2018/2018-11-27-scaling-jenkins/)
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [dzone.com: How to Set Up Scalable Jenkins on Top of a Kubernetes Cluster 🌟🌟🌟](https://dzone.com/articles/how-to-setup-scalable-jenkins-on-top-of-a-kubernet)
* [devops.com: Kubernetes Jenkins Master-Slave: Scaling the Scalability Issue](https://devops.com/kubernetes-jenkins-master-slave-scaling-the-scalability-issue/)
* [7 Ways to Optimize Jenkins](https://www.sitepoint.com/7-ways-optimize-jenkins/)
* [devopscube.com: How to Setup Docker containers as Build Slaves for Jenkins](https://devopscube.com/docker-containers-as-build-slaves-jenkins/)

## Ansible and Jenkins. Running Ansible Playbooks From Jenkins
* [Dzone: Running Ansible Playbooks From Jenkins](https://dzone.com/articles/running-ansible-playbooks-from-jenkins)
* [itnext.io: Ansible and Jenkins — automate your scritps 🌟](https://itnext.io/ansible-and-jenkins-automate-your-scritps-8dff99ef653)
* [ansible-role-jenkins](https://github.com/geerlingguy/ansible-role-jenkins) Installs Jenkins CI on RHEL/CentOS and Debian/Ubuntu servers.

## Jenkins Plugins
* [dev.to: 8 Jenkins plugins I can't live without (2019)](https://dev.to/jcoelho/8-jenkins-plugins-i-cant-live-without-3bin)
* [caylent: 20 Jenkins Plugins You Can’t Live Without (2018) 🌟🌟🌟🌟](https://caylent.com/jenkins-plugins)
* [blazemeter.com: Top Jenkins Plugins You Can’t Miss in 2018](https://www.blazemeter.com/blog/top-jenkins-plugins-you-cant-miss-in-2018/)
* [dzone: Top 5 Jenkins Plugins (2017)](https://dzone.com/articles/5-best-jenkins-plugins-recommended-by-our-team)
* [devops.com: 15 must have Jenkins plugins to increase productivity](https://devops.com/15-must-jenkins-plugins-increase-productivity/)
* [jrebel.com: Top 10 Jenkins Plugins and Features (2014)](https://www.jrebel.com/blog/top-10-jenkins-plugins-and-features)
* [devteam.space: 10 Best Jenkins Plugins For DevOps](https://www.devteam.space/blog/10-best-jenkins-plugins-for-devops/)
* [devops.com: Top 10 Best Practices for Jenkins Pipeline Plugin 🌟🌟🌟](https://devops.com/top-10-best-practices-for-jenkins-pipeline-plugin/)

### Selection of Jenkins Plugins
* [performance-plugin](https://github.com/jenkinsci/performance-plugin)
* [Matrix 🌟🌟🌟](https://jenkins.io/blog/2019/11/22/welcome-to-the-matrix/)
* [Compress-buildlog](https://plugins.jenkins.io/compress-buildlog)
* [syslog-logger](https://plugins.jenkins.io/syslog-logger)
* [openshift-pipeline](https://plugins.jenkins.io/openshift-pipeline)
* [openshift-sync](https://plugins.jenkins.io/openshift-sync)
* [openshift-client](https://plugins.jenkins.io/openshift-client)
* [openshift-login](https://plugins.jenkins.io/openshift-login)
* [openshift-deployer](https://plugins.jenkins.io/openshift-deployer)
* [kubernetes plugin](https://plugins.jenkins.io/kubernetes)
* [Kubernetes Continuous Deploy 🌟🌟🌟](https://plugins.jenkins.io/kubernetes-cd)
* [Atlassian's new Bitbucket Server integration for Jenkins 🌟🌟🌟](https://jenkins.io/blog/2020/01/08/atlassians-new-bitbucket-server-integration-for-jenkins/)
* [Blue Ocean 🌟🌟🌟](https://plugins.jenkins.io/blueocean/)
* [Cloudbees Flow 🌟🌟🌟](https://plugins.jenkins.io/electricflow)
* [Cloudbees Credentials 🌟🌟](https://plugins.jenkins.io/cloudbees-credentials)
* [CloudBees Health Advisor](https://plugins.jenkins.io/cloudbees-jenkins-advisor)
* [CloudBees Disk Usage Simple](https://plugins.jenkins.io/cloudbees-disk-usage-simple)
* [CloudBees AWS Credentials 🌟🌟](https://plugins.jenkins.io/aws-credentials)
* [CloudBees Docker Custom Build Environment](https://plugins.jenkins.io/docker-custom-build-environment)
* [Code Average API](https://plugins.jenkins.io/code-coverage-api)
* [Fortify](https://plugins.jenkins.io/fortify)
* [medium: ECS Jenkins Plugin to create ephemeral Slaves in Fargate](https://medium.com/@jportasa/ecs-jenkins-plugin-to-create-ephemeral-slaves-in-fargate-8cb80b46fb75)
* [Pipeline: SCM Step (workflow-scm-step)](https://www.jenkins.io/doc/pipeline/steps/workflow-scm-step/) The following plugin provides functionality available through Pipeline-compatible steps.
* [Amazon EC2 plugin](https://plugins.jenkins.io/ec2/)
* [Copy Artifact](https://plugins.jenkins.io/copyartifact/)
* [Credentials Binding](https://plugins.jenkins.io/credentials-binding/)
* [CVS plugin](https://plugins.jenkins.io/cvs/)
* [SCM Filter Jervis YAML Plugin](https://plugins.jenkins.io/scm-filter-jervis/) This plugin is intended for Jenkins infrastructure relying on [jervis](https://github.com/samrocketman/jervis/wiki) to deliver software in a self-service manner. This plugin can also be used for Travis CI YAML.
* etc

### Job DSL Plugin (Jenkins Job DSL API used in Jenkins Pipelines)
* [plugins.jenkins.io/job-dsl](https://plugins.jenkins.io/job-dsl/)
    * [github.com/jenkinsci/job-dsl-plugin](https://github.com/jenkinsci/job-dsl-plugin/wiki)
* [Jenkins Job DSL API 🌟](http://jenkinsci.github.io/job-dsl-plugin/)
* [job-dsl **Gradle** Example](https://github.com/sheehan/job-dsl-gradle-example)
* [Jenkins DSL for **Nexus**](https://accenture.github.io/adop-cartridges-cookbook/docs/recipes/archiving-artefact-to-nexus/)
* Jenkins DSL for **Maven**:
    * [ref 1](https://jenkinsci.github.io/job-dsl-plugin/#method/javaposse.jobdsl.dsl.helpers.step.StepContext.maven)
    * [ref 2](https://deors.wordpress.com/2019/04/25/jenkins-ci-pipeline-java-spring-boot-maven-docker/)

### Jenkins Configuration as Code Plugin 
* [Jenkins Configuration as Code](https://www.jenkins.io/projects/jcasc/)
    * [plugins.jenkins.io/configuration-as-code](https://plugins.jenkins.io/configuration-as-code/)
    * [github.com/jenkinsci/configuration-as-code-plugin](https://github.com/jenkinsci/configuration-as-code-plugin)
* [devops.com: Using jenkins configuration as code](https://devops.com/using-jenkins-configuration-as-code/)
* [opensource.com: Getting started with Jenkins Configuration as Code 🌟](https://opensource.com/article/20/4/getting-started-jcasc-jenkins) JCasC uses YAML formats to set up Jenkins configurations.
* [dzone.com: Jenkins Configuration as Code: Need for Speed! 🌟](https://dzone.com/articles/jenkins-configuration-as-code-need-for-speed)
      * [https://github.com/jenkinsci/configuration-as-code-plugin](https://github.com/jenkinsci/configuration-as-code-plugin)
* [Dzone: Running Jenkins Server With Configuration-as-Code 🌟](https://dzone.com/articles/running-jenkins-server-with-configuration-as-code) Take a look at the new plugin for Jenkins that allows you to to create pipelines using YAML! Let's check out the details and examples.
* [docs.cloudbees.com: Configuration as Code for CloudBees Core on modern cloud platforms](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern)
* [cloudbees.com: CloudBees Core Configuration as Code](https://www.previous.cloudbees.com/blog/cloudbees-core-configuration-code-preview)
* [Visual Studio Code JCasC-Plugin 🌟](https://marketplace.visualstudio.com/items?itemName=jcasc-developers.jcasc-plugin) This extension is used to integrate a live jenkins instance configuration with your editor. It can be used to edit and validate YAML files.

### Jenkins Blue Ocean
* [Jenkins BlueOcean 🌟](https://www.jenkins.io/doc/book/blueocean/getting-started/)
* [Blue Ocean plugin](https://plugins.jenkins.io/blueocean/)

|<iframe src="https://www.youtube.com/embed/NVicei-Ew4A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|<iframe src="https://www.youtube.com/embed/ZJZW0j2eTQY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|:---:|:---:|

### Cloudbees Flow
* [**Cloudbees Flow** 🌟🌟🌟](https://www.cloudbees.com/products/flow/overview)
* [CloudBees Flow plugin](https://plugins.jenkins.io/electricflow/)

<iframe src="https://www.youtube.com/embed/tuhGzaQx8gY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Monitoring jenkins
* [Performance plugin](https://github.com/jenkinsci/performance-plugin)
* [Splunk Plugins](https://plugins.jenkins.io/splunk-devops)
    * [Splunk App for Jenkins](https://splunkbase.splunk.com/app/3332/)
* [Logstash](https://plugins.jenkins.io/logstash)
* [Build Monitor Plugin](https://wiki.jenkins.io/display/JENKINS/Build+Monitor+Plugin)
    * [Monitor CI nodes with Jenkins](http://www.ampelofilosofies.gr/software/2017/03/04/monitor-ci-nodes-with-jenkins#sthash.eLP0PanT.dpbs)
    * [youtube: How to create Build Monitor View](https://www.youtube.com/watch?v=WnQK6-puXSM)
    * [youtube: monitoring jenkins job with build monitor view](https://www.youtube.com/watch?v=y6RNLNvnYIw)
    * [tatiyants.com: jenkins build monitor](http://tatiyants.com/jenkins-build-monitor/)
* [Monitor Pro Plugin](https://wiki.jenkins.io/display/JENKINS/Monitor+Pro+Plugin)
* [ALM Performance: Continuously Monitor Performance and Vitality of your Jenkins Deployment](https://www.almtoolbox.com/jenkins-monitoring.php)
* [Monitoring jenkins using instana](https://www.instana.com/blog/monitoring-jenkins-using-instana/)
* [medium: prometheus and grafana dashboard](https://medium.com/@gangsta_black/grafana-cool-dashboard-for-monitoring-jenkins-with-prometheus-c7ba4f1c6297)
* [youtube: Monitoring Jenkins with Grafana and Prometheus](https://www.youtube.com/watch?v=EWFJem7GUAc)
* [dynatrace.com: optimizing jenkins to ensure fast build times with dynatrace](https://www.dynatrace.com/news/blog/optimizing-jenkins-to-ensure-fast-build-times-with-dynatrace/)
* [opsview.com: opspack](https://www.opsview.com/product/system-monitoring/application/jenkins-monitoring)
* [Chrome Extension](https://chrome.google.com/webstore/detail/monitor-me-jenkins/jhbokpimjgedmpcmfoghhiokhpihlkgc)
* [Jenkins plugin to provide automatic status for multibranch jobs (Grafana)](https://plugins.jenkins.io/github-autostatus)
    * [github.com/jenkinsci/github-autostatus-plugin](https://github.com/jenkinsci/github-autostatus-plugin)
* [20 Jenkins Plugins You Can’t Live Without](https://caylent.com/jenkins-plugins)
* [youtube - CloudBeesTV: Jenkins Performance: Avoiding Pitfalls, Diagnosing Issues & Scaling for Growth](https://www.youtube.com/watch?v=yTafQ-e84eY)

## Jenkins and Spring Boot
* [jaxenter.com - CI/CD for Spring Boot Microservices](https://jaxenter.com/cicd-microservices-docker-162408.html)
* [piotrminkowski.wordpress.com: Kotlin microservice with spring boot](https://piotrminkowski.wordpress.com/2019/01/15/kotlin-microservice-with-spring-boot/)

## Kubernetes Native Jenkins Operator 
* [github.com/jenkinsci/kubernetes-operator: 🌟🌟🌟](https://github.com/jenkinsci/kubernetes-operator) Kubernetes platform was released ten years after the first version of Hudson project. It means Jenkins couldn’t be designed to run on top of it. Jenkins Operator tries to bridge that gap.

## Jervis: Jenkins as a service
* [Jervis](https://github.com/samrocketman/jervis/wiki) is [Sam Gleske](https://github.com/samrocketman)'s vision of a good way to roll out Jenkins as a service in very large organizations.
* [SCM Filter Jervis YAML Plugin](https://plugins.jenkins.io/scm-filter-jervis/) This plugin is intended for Jenkins infrastructure relying on [jervis](https://github.com/samrocketman/jervis/wiki) to deliver software in a self-service manner. This plugin can also be used for Travis CI YAML.

## Jenkins X
[**Jenkins X**](https://jenkins-x.io) is a specialized Jenkins for Kubernetes: This is how it works from a bird eye the CI/CD:  a developer creates a branch, then Jenkins X creates a ephemeral namespace with that branch. The developer tests it and once it is ok, a PR is created, then, the branch is deployed in staging.  When I merge it, it goes to QA, and with a manual command "jx promote" it goes to production.  Jenkins X deletes automatically after N hours the branch namespace.

* [**jenkins-x.io**](https://jenkins-x.io/)
* [itnext.io/tagged/jenkins-x](https://itnext.io/tagged/jenkins-x)
* [itnext.io: Jenkins X — Managing Jenkins](https://itnext.io/jenkins-x-managing-jenkins-926f0e0f8bcf)
* Video Tutorials:
    * [Youtube: Jenkins X: Continuous Delivery for Kubernetes with James Strachan](https://www.youtube.com/watch?v=BF3MhFjvBTU)
    * [Youtube: Kubernetes Package Management with Helm and CI/CD with Jenkins X - Webinar by Neependra Khare](https://www.youtube.com/watch?v=oZOZiL6XIfA&feature=emb_title)
    * [go.digitalocean.com/cicd-on-k8s](https://go.digitalocean.com/cicd-on-k8s)

[![jenkins and openshift](images/jenkins-ose.png)](https://www.cloudbees.com/)

[![jenkins hub CD](images/jenkins-hub.png)](https://hostadvice.com/blog/devops-toolbox-jenkins-ansible-chef-puppet-vagrant-saltstack/)

