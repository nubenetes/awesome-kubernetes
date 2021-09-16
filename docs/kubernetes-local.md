# Kubernetes distributions for local environments. Kubernetes Development Tools and Dashboards
- [Non-production Kubernetes Local Installers. Kubernetes distributions for local environments](#non-production-kubernetes-local-installers-kubernetes-distributions-for-local-environments)
- [Kubernetes Development Tools. Kubernetes Clients and Dashboards](#kubernetes-development-tools-kubernetes-clients-and-dashboards)
    - [Okteto local kubernetes development](#okteto-local-kubernetes-development)
    - [Lens Kubernetes IDE](#lens-kubernetes-ide)
    - [Kubenav](#kubenav)
    - [Cloud Manager](#cloud-manager)
    - [Skaffold. Local Kubernetes Development](#skaffold-local-kubernetes-development)
    - [Telepresence local development for k8s and openshift microservices](#telepresence-local-development-for-k8s-and-openshift-microservices)

## Non-production Kubernetes Local Installers. Kubernetes distributions for local environments
* [Minikube](https://github.com/kubernetes/minikube) A tool that makes it easy to run Kubernetes locally inside a Linux VM. It's aimed on users who want to just test it out or use it for development. It cannot spin up a production cluster, it's a one node machine with no high availability.
    * [murchie85.github.io: Installling minikube](https://murchie85.github.io/Kubernetes.html)
    * [itnext.io: How to experiment locally on Kubernetes with minikube and your local Dockerfiles](https://itnext.io/how-to-experiment-locally-on-kubernetes-with-minikube-and-your-local-dockerfiles-48833fcd90c9)
* [**kind**](https://github.com/kubernetes-sigs/kind) Kubernetes IN Docker - local clusters for testing Kubernetes. Kind is a tool for running local Kubernetes clusters using Docker container “nodes”. kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.
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

## Kubernetes Development Tools. Kubernetes Clients and Dashboards
- [ordina-jworks.github.io: A comparison of Kubernetes clients and dashboards](https://ordina-jworks.github.io/cloud/2020/08/28/kubernetes-clients-comparison.html)
- [loft.sh: Kubernetes Development Environments – A Comparison](https://loft.sh/blog/kubernetes-development-environments-comparison/)
- [yitaek.medium.com: Useful Tools for Better Kubernetes Development 🌟](https://yitaek.medium.com/useful-tools-for-better-kubernetes-development-87820c2b9435) Lens, Polaris, kube-hunter, kube-bench, Trivy, Goldilocks, Kyverno, kube-ps1, kubectx + kubens , krew, kubectl-neat, kube-no-trouble, helm-mapkubeapis, kube-diff + helm-diff , kube forwarder, kubecost, kubespy.
- [kccncna20.sched.com: A Walk Through the Kubernetes UI Landscape](https://kccncna20.sched.com/event/ekAd/a-walk-through-the-kubernetes-ui-landscape-joaquim-rocha-kinvolk-henning-jacobs-zalando-se) Working with Kubernetes clusters and workloads can be overwhelming, both for operators, as well as application developers. While kubectl is the de-facto standard interface to interact with Kubernetes' API, a graphical user interface can provide a better experience for newcomers and advanced users alike. This talk will look at the current landscape of Open Source Kubernetes web and desktop UIs, including Kubernetes Dashboard, Lens, Octant, Kubernetes Web View, and Headlamp. Particularly, how different dashboards are built, for what purpose they can be used, and how they compare in terms of functionality, so attendees can get the most out of the vast landscape of Kubernetes UIs.
    - [PDF](https://static.sched.com/hosted_files/kccncna20/02/A%20Walk%20Through%20the%20Kubernetes%20UI%20Landscape%20%28KubeCon%20Talk%202020%29.pdf)
- [tilt.dev 🌟](https://tilt.dev) You can use Tilt to easily build and run your application on Kubernetes. In comparison with similar tools, it provides [UI for managing the process and cloud platform](https://cloud.tilt.dev) to share data with your team.
- [microcks.io 🌟](https://microcks.io) K8s-based API mock/test tool. 
    - [microcks.io: Podman Compose support in Microcks](https://microcks.io/blog/podman-compose-support)
- [kinvolk.io: Shining a light on the Kubernetes User Experience with Headlamp](https://kinvolk.io/blog/2020/11/shining-a-light-on-the-kubernetes-user-experience-with-headlamp/)
- [kubevious](https://github.com/kubevious/kubevious)
- [cncf.io: Tools to develop apps on Kubernetes 🌟](https://www.cncf.io/blog/2021/05/10/tools-to-develop-apps-on-kubernetes)
- [blog.usejournal.com: Useful Tools for Better Kubernetes Development](https://blog.usejournal.com/useful-tools-for-better-kubernetes-development-87820c2b9435)
- [loft.sh: Kubernetes Dashboards: Headlamp](https://loft.sh/blog/kubernetes-dashboards-headlamp/) - [Headlamp Dashboard](https://kinvolk.io/docs/headlamp/latest)
- [blog.tekspace.io: Deploying Kubernetes Dashboard in K3S Cluster](https://blog.tekspace.io/deploying-kubernetes-dashboard-in-k3s-cluster/)
- [williamlam.com: Useful Interactive Terminal and Graphical UI Tools for Kubernetes](https://williamlam.com/2020/04/useful-interactive-terminal-and-graphical-ui-tools-for-kubernetes.html)
- [hackerxone.com: How To Install Kubernetes Dashboard with NodePort in Linux](https://www.hackerxone.com/2021/07/10/how-install-kubernetes-dashboard-nodeport-linux/)
- [loft.sh: Kubernetes Monitoring Dashboards - 5 Best Open-Source Tools](https://loft.sh/blog/kubernetes-monitoring-dashboards-5-best-open-source-tools/)
- [loft.sh: Kubernetes Development Environments – A Comparison](https://loft.sh/blog/kubernetes-development-environments-comparison/)
- [medium: YAKD: Yet Another Kubernetes Dashboard](https://medium.com/geekculture/yakd-yet-another-kubernetes-dashboard-7766bd) A list of most popular opensource kubernetes dashboard both for local development & in production as well
- [adamtheautomator.com: How to Install and Set Up Kubernetes Dashboard [Step by Step]](https://adamtheautomator.com/kubernetes-dashboard/)
- [thenewstack.io: Who Needs a Dashboard? Why the Kubernetes Command Line Is Not Enough](https://thenewstack.io/who-needs-a-dashboard-why-the-kubernetes-command-line-is-not-enough/)
### Okteto local kubernetes development
- [okteto.com: How to Develop and Debug Java Applications on Kubernetes](https://okteto.com/blog/how-to-develop-java-apps-in-kubernetes/)
- [codefresh.io: Tutorial - Local Kubernetes Development with Okteto 🌟](https://codefresh.io/kubernetes-tutorial/okteto/)

### Lens Kubernetes IDE
- [Lens Kubernetes IDE 🌟](https://k8slens.dev/) Lens is the only IDE you’ll ever need to take control of your Kubernetes clusters. It's open source and free. Download it today!
- [medium: Lens 5 Released](https://medium.com/k8slens/lens-5-released-f7e58e8842cf)
- [medium: How To Give Developers Secure Access to Kubernetes Clusters](https://medium.com/k8slens/how-to-give-developers-secure-access-to-kubernetes-clusters-c6025f0dd288)
- [Lens Resource Map extension](https://github.com/nevalla/lens-resource-map-extension) Lens - The Kubernetes IDE extension that displays Kubernetes resources and their relations as a force graph.

[![lens ide](images/header-lens.png)](https://k8slens.dev/)

### Kubenav
- [kubenav](https://github.com/kubenav/kubenav) is the navigator for your Kubernetes clusters right in your pocket. kubenav is a mobile, desktop and web app to manage Kubernetes clusters and to get an overview of the status of your resources.

### Cloud Manager
- [thenewstack.io: Cloud Manager: A New Multicloud PaaS Platform Built on Kubernetes](https://thenewstack.io/cloud-manager-a-new-multicloud-paas-platform-built-on-kubernetes/)
- [medium: Do It All Kubernetes Dashboard](https://medium.com/faun/do-it-all-kubernetes-dashboard-81375833e01c)

### Skaffold. Local Kubernetes Development
- [Skaffold 🌟](https://skaffold.dev/)
- [infracloud.io: Build and deploy Kubernetes apps with Skaffold](https://www.infracloud.io/blogs/skaffold-usecases/)
- [testingclouds.wordpress.com: Migrating from Docker Compose to Skaffold 🌟](https://testingclouds.wordpress.com/2021/03/09/migrating-from-docker-compose-to-skaffold/)

### Telepresence local development for k8s and openshift microservices
* [telepresence.io 🌟](https://www.telepresence.io) Fast, local development for kubernetes and openshift microservices.
* [telepresence.io: Debug a Kubernetes service locally 🌟](https://www.telepresence.io/tutorials/kubernetes) Imagine you have a service running in a cluster, and someone reports a bug. You want to run the service locally but how? Enter Telepresence
* [betterprogramming.pub: Do Faster Development and Testing on Kubernetes Apps With Telepresence](https://betterprogramming.pub/do-faster-development-and-testing-on-kubernetes-apps-with-telepresence-b7eac604dca4) Use Telepresence to instantly deploy your code change to a Kubernetes cluster
* [telepresence.io: Intercept a service in your own environment 🌟](https://www.telepresence.io/docs/latest/howtos/intercepts/) Today, I needed to intercept traffic sent to the application running on Kubernetes and forward it to the local dev instance.





