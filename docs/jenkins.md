# Jenkins
* https://en.wikipedia.org/wiki/Jenkins_(software)
* [Jenkins.io (new Jenkins 2.0 site)](https://jenkins.io/)
* [jenkins.io: Jenkins CD and Pipelines Microsite](https://jenkins.io/solutions/pipeline/)
* [dzone.com: Jenkins Pipeline - Software Delivery Made Easy](https://dzone.com/articles/jenkins-pipeline-software-delivery-made-easy) Jenkins 2.0 has focused on solving the problem for organizations wanting to continuously deliver software.
* [dzone.com: Jenkins Configuration as Code: Need for Speed! 🌟🌟🌟🌟](https://dzone.com/articles/jenkins-configuration-as-code-need-for-speed)
    * https://github.com/jenkinsci/configuration-as-code-plugin
* [Dzone: Running Jenkins Server With Configuration-as-Code 🌟🌟🌟](https://dzone.com/articles/running-jenkins-server-with-configuration-as-code) Take a look at the new plugin for Jenkins that allows you to to create pipelines using YAML! Let's check out the details and examples.
* [jenkins.io - Tuning Jenkins GC For Responsiveness and Stability with Large Instances 🌟🌟🌟](https://jenkins.io/blog/2016/11/21/gc-tuning/)
* [dzone.com: How to Set Up Scalable Jenkins on Top of a Kubernetes Cluster 🌟🌟🌟](https://dzone.com/articles/how-to-setup-scalable-jenkins-on-top-of-a-kubernet)
* [devops.com: Kubernetes Jenkins Master-Slave: Scaling the Scalability Issue](https://devops.com/kubernetes-jenkins-master-slave-scaling-the-scalability-issue/)
* [udemy.com: Master Jenkins CI For DevOps and Developers](https://www.udemy.com/the-complete-jenkins-course-for-developers-and-devops/)
* [udemy.com: Learn DevOps: CI/CD with Jenkins using Pipelines and Docker](https://www.udemy.com/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker/) Use Jenkins the DevOps way. Automate your Jenkins jobs by using Jenkins Pipelines, Docker, and the Jenkins Job DSL
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
* [Dzone refcard: Jenkins on PaaS](https://dzone.com/asset/download/230) Continuous Integration with Jenkins for Java Projects. Includes a review of the most useful plugins, best practices, security, integration to an enterprise environment, and more.
* [7 Ways to Optimize Jenkins](https://www.sitepoint.com/7-ways-optimize-jenkins/)
* [Dzone: Top 10 Best Practices for Jenkins Pipeline](https://dzone.com/articles/top-10-best-practices-for-jenkins-pipeline)
* [opensource.com: Running Jenkins builds in Openshift containers](https://opensource.com/article/18/4/running-jenkins-builds-containers)

## Performance Testing with Jenkins and JMeter
* https://github.com/jenkinsci/performance-plugin
* https://www.blazemeter.com/blog/continuous-integration-101-how-run-jmeter-jenkins 🌟
* https://www.baeldung.com/jenkins-and-jmeter
* https://dzone.com/articles/2-ways-to-integrate-jmeter-tests-into-jenkins
* https://www.guru99.com/jenkins-jmeter-blazemeter.html

## Jenkins and Openshift
* [Building Declarative Pipelines with OpenShift DSL Plugin 🌟🌟🌟](https://blog.openshift.com/building-declarative-pipelines-openshift-dsl-plugin/)
* [slideshare.net: CI/CD with Openshift and Jenkins 🌟🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins)
* [slideshare.net: OPENSHIFT CONTAINER PLATFORM CI/CD Build & Deploy  🌟🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy)

# Kubernetes VS Openshift
* [cloudowski.com: 10 most important differences between OpenShift and Kubernetes 🌟🌟🌟](https://cloudowski.com/articles/10-differences-between-openshift-and-kubernetes/)

# Kubernetes
* https://en.wikipedia.org/wiki/Kubernetes
* [youtube: Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [developers.redhat.com: Why Kubernetes is The New Application Server](https://developers.redhat.com/blog/2018/06/28/why-kubernetes-is-the-new-application-server/)
* [Awesome kubernetes 🌟🌟🌟🌟](https://github.com/ramitsurana/awesome-kubernetes)
* https://www.reddit.com/r/kubernetes 🌟🌟🌟
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟🌟🌟](https://stackify.com/kubernetes-docker-deployments/)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [developers.redhat.com: Kubernetes Cheat Sheet 🌟](https://developers.redhat.com/cheat-sheets/kubernetes/)
* [Local Install Option 1: Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
* [Local Install Option 2: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [Production Cluster Install Option 3: Kubernetes Cluster with Kops:](https://github.com/kubernetes/kops) 
    * Minikube and docker client are great for local setups, but not for real clusters. Kops and kubeadm are tools to spin up a production cluster. You don't need both tools, just one of them. 
    * On AWS, the best tool is **kops**
    * At some point AWS EKS (hosted kubernetes) will be available, at that point this will probably be the preferred option. (You won't need to maintain the masters).
    * For other installs, or if you can't get kops to work, you can use kubeadm
    * **kubeadm** is an alternative approach, kops is still recommended (on AWS) - you also have AWS integrations with kops automatically
    * Setup **kops** in your windows with **virtualbox.org** and **vagrantup.com** . Once downloaded, to type a new linux VM, just type in cmd/powershell:
    1) Spin up ubuntu via vagrant:
    ```
        C:\ubuntu> vagrant init ubuntu/xenial64
        C:\ubuntu> vagrant up
        [...]
        C:\ubuntu> vagrant ssh-config
        C:\ubuntu> vagrant ssh
    ```
    2) Runt kops installer:
    ```
        curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
        chmod +x kops-linux-amd64
        sudo mv kops-linux-amd64 /usr/local/bin/kops
    ```
* [Production Cluster Install Option 4: Kubernetes Cluster with Kubeadm](https://github.com/kubernetes/kubeadm) It works on any deb / rpm compatible Linux OS, for example Ubuntu, Debian, RedHat or CentOS. This is the main advantage of kubeadm. The tool itself is still in beta (Q1 2018), but is expected to become stable somewhere this year. It's very easy to use and lets you spin kubernetes cluster in just a couple of minutes.
* [Production Cluster Install Option 5: Ansible Role - Kubernetes (Jeff Geerling)](https://github.com/geerlingguy/ansible-role-kubernetes)
* [kubedex.com 🌟🌟🌟](https://kubedex.com/) Discover, Compare and Share Kubernetes Applications
    * [kubedex.com: autoscaling 🌟](https://kubedex.com/autoscaling)