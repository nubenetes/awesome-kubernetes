# Non-production Kubernetes Local Installers. Kubernetes distributions for local environments
- [Introduction](#introduction)
- [Telepresence local development for k8s and openshift microservices](#telepresence-local-development-for-k8s-and-openshift-microservices)

## Introduction
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
    * [itnext.io: How to experiment locally on Kubernetes with minikube and your local Dockerfiles](https://itnext.io/how-to-experiment-locally-on-kubernetes-with-minikube-and-your-local-dockerfiles-48833fcd90c9)
* [**kind**](https://github.com/kubernetes-sigs/kind) Kubernetes IN Docker - local clusters for testing Kubernetes
    * [kubernetes-development-environment-in-a-box](https://github.com/ManagedKube/kubernetes-development-environment-in-a-box) This project is geared toward running multiple isolated KinD cluster on a single instance. This project produces an AMI image that can run an instance that has Docker and multiple isolated Kubernetes clusters running in it using KinD. The main use case is to setup one node that can run multiple fully isolated Kubernetes cluster on it for development purposes.
* [store.docker.com: Docker Community Edition EDGE with kubernetes. Installing Kubernetes using the Docker Client](https://store.docker.com/editions/community/docker-ce-desktop-windows) Currently only available in **Edge** edition.
* [medium.com: Local Kubernetes for Linux — MiniKube vs MicroK8s](https://medium.com/containers-101/local-kubernetes-for-linux-minikube-vs-microk8s-1b2acad068d3)
* [itnext.io: Run Kubernetes On Your Machine](https://itnext.io/run-kubernetes-on-your-machine-7ee463af21a2) Several options to start playing with K8s in no time
* [padok.fr: MiniKube, Kubeadm, Kind, K3S, how to get started on Kubernetes?](https://www.padok.fr/en/blog/minikube-kubeadm-kind-k3s)
* [loft.sh: Kubernetes Development Environments – A Comparison](https://loft.sh/blog/kubernetes-development-environments-comparison/)
* [opensource.com: 4 ways to run Kubernetes locally](https://opensource.com/article/20/11/run-kubernetes-locally) Set up a local development environment or just try out the container orchestration platform with these tools.
* [dex.dev: Local Development Clusters](https://www.dex.dev/dex-videos/development-clusters)
* [itnext.io: Kubernetes local playground alternatives](https://itnext.io/kubernetes-local-playground-alternatives-e1a590632b9f)
* [dex.dev: Local Development Clusters](https://www.dex.dev/dex-videos/development-clusters)
* [blog.radwell.codes: What’s the best Kubernetes distribution for local environments? 🌟](https://blog.radwell.codes/2021/05/best-kubernetes-distribution-for-local-environments/)
* [Metal Kubes](https://github.com/shank-git/metal-kubes) Create OnPrem Kubernetes Cluster. Install Kubernetes Cluster on Bare Metal Machines

## Telepresence local development for k8s and openshift microservices
* [telepresence.io 🌟](https://www.telepresence.io) Fast, local development for kubernetes and openshift microservices.
* [telepresence.io: Debug a Kubernetes service locally 🌟](https://www.telepresence.io/tutorials/kubernetes) Imagine you have a service running in a cluster, and someone reports a bug. You want to run the service locally but how? Enter Telepresence
* [betterprogramming.pub: Do Faster Development and Testing on Kubernetes Apps With Telepresence](https://betterprogramming.pub/do-faster-development-and-testing-on-kubernetes-apps-with-telepresence-b7eac604dca4) Use Telepresence to instantly deploy your code change to a Kubernetes cluster
* [telepresence.io: Intercept a service in your own environment 🌟](https://www.telepresence.io/docs/latest/howtos/intercepts/) Today, I needed to intercept traffic sent to the application running on Kubernetes and forward it to the local dev instance.
