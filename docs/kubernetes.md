<!-- TOC -->

- [1. Kubernetes](#1-kubernetes)
    - [1.1. Local Installers](#11-local-installers)
    - [1.2. Production Cluster Installers](#12-production-cluster-installers)
    - [1.3. Videos](#13-videos)

<!-- /TOC -->

# 1. Kubernetes
* [Wikipedia.org: Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [youtube: Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [Awesome kubernetes 🌟🌟🌟🌟](https://github.com/ramitsurana/awesome-kubernetes)
* [https://www.reddit.com/r/kubernetes 🌟🌟🌟](https://www.reddit.com/r/kubernetes) 
* [stackify.com: The Advantages of Using Kubernetes and Docker Together 🌟🌟🌟](https://stackify.com/kubernetes-docker-deployments/)
* [udemy.com: Learn DevOps: The Complete Kubernetes Course 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-the-complete-kubernetes-course)
* [udemy.com: Learn DevOps: Advanced Kubernetes Usage 🌟🌟🌟🌟](https://www.udemy.com/learn-devops-advanced-kubernetes-usage)
* [Ansible for devops: Kubernetes](https://github.com/geerlingguy/ansible-for-devops/tree/master/kubernetes)
* [Dzone refcard: Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [developers.redhat.com: Kubernetes Cheat Sheet 🌟](https://developers.redhat.com/cheat-sheets/kubernetes/)
* [kubedex.com 🌟🌟🌟](https://kubedex.com/) Discover, Compare and Share Kubernetes Applications
    * [kubedex.com: autoscaling 🌟](https://kubedex.com/autoscaling)
* [Google Play: Learning Solution - Learn Kubernetes 🌟🌟🌟](https://play.google.com/store/apps/details?id=com.LearningSolution.LearnKubernetes)
* [Google Play: TomApp - Learn Kubernetes](https://play.google.com/store/apps/details?id=tomtran.learnkubernetes)
* [Play with Kubernetes 🌟🌟🌟🌟](https://labs.play-with-k8s.com/) A simple, interactive and fun playground to learn Kubernetes

## 1.1. Local Installers
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.

## 1.2. Production Cluster Installers

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

## 1.3. Videos
<iframe width="560" height="315" src="https://www.youtube.com/embed/PH-2FfFD2PU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>




