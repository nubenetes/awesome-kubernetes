# Kubernetes Networking
- [Introduction](#introduction)
- [NetworkPolicy](#networkpolicy)
- [Nginx Ingress controller](#nginx-ingress-controller)
- [Gateway API](#gateway-api)
- [Kube-proxy](#kube-proxy)
- [Multicloud communication for Kubernetes](#multicloud-communication-for-kubernetes)
- [Multi-Cluster Kubernetes Networking](#multi-cluster-kubernetes-networking)
- [Kubernetes Network Policy](#kubernetes-network-policy)
    - [Cilium](#cilium)
    - [Kubernetes Network Policy Samples](#kubernetes-network-policy-samples)
- [Kubernetes Ingress Specification](#kubernetes-ingress-specification)
- [Xposer Kubernetes Controller To Manage Ingresses](#xposer-kubernetes-controller-to-manage-ingresses)
- [Software-Defined IP Address Management (IPAM)](#software-defined-ip-address-management-ipam)
- [CNI Container Networking Interface](#cni-container-networking-interface)
    - [List of existing CNI Plugins (IPAM)](#list-of-existing-cni-plugins-ipam)
    - [Project Calico](#project-calico)
- [DNS Service with CoreDNS](#dns-service-with-coredns)
- [Kubernetes Node Local DNS Cache](#kubernetes-node-local-dns-cache)
- [Kubernetes Sidecars](#kubernetes-sidecars)
- [Tweets](#tweets)

## Introduction
* [kubernetes.io: The Kubernetes network model. How to implement the Kubernetes networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
* [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://www.ovh.com/blog/getting-external-traffic-into-kubernetes-clusterip-nodeport-loadbalancer-and-ingress/)
* [learnk8s.io: Load balancing and scaling long-lived connections in Kubernetes 🌟](https://learnk8s.io/kubernetes-long-lived-connections)
* [stackrox.com: Kubernetes Networking Demystified: A Brief Guide](https://www.stackrox.com/post/2020/01/kubernetes-networking-demystified/)
* [medium.com: Fighting Service Latency in Microservices With Kubernetes](https://medium.com/@sindhujacynixit/fighting-service-latency-in-microservices-with-kubernetes-f5a584f5af36)
* [medium.com: Kubernetes NodePort vs LoadBalancer vs Ingress? When should I use what? 🌟](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)
* [blog.alexellis.io: Get a LoadBalancer for your private Kubernetes cluster](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster/)
* [dustinspecker.com: How Do Kubernetes and Docker Create IP Addresses?!](https://dustinspecker.com/posts/how-do-kubernetes-and-docker-create-ip-addresses/)
* [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 1)](https://www.weave.works/blog/introduction-to-kubernetes-pod-networking--part-1)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 2)](https://www.weave.works/blog/aws-networking-overview---part-2)
* [AWS and Kubernetes Networking Options and Trade-Offs (part 3)](https://dzone.com/articles/aws-and-kubernetes-networking-options-and-trade-of) 
* [medium: Service Types in Kubernetes? 🌟](https://medium.com/faun/service-types-in-kubernetes-24a1587677d6) A Service enables network access to a set of Pods in Kubernetes.
* [containo.us: Kubernetes Ingress & Service API Demystified](https://containo.us/blog/kubernetes-ingress-service-api-demystified/)
* [speakerdeck.com: Kubernetes and networks. Why is this so dan hard? 🌟](https://speakerdeck.com/thockin/kubernetes-and-networks-why-is-this-so-dang-hard)
* [eevans.co: Deconstructing Kubernetes Networking](https://eevans.co/blog/deconstructing-kubernetes-networking/)
* [externalTrafficPolicy=local on kubernetes. How to preserve the source IP in kubernetes](https://blog.getambassador.io/externaltrafficpolicy-local-on-kubernetes-e66e498212f9) externalTrafficPolicy=local is an annotation on the Kubernetes service resource that can be set to preserve the client source IP. When it is set, the actual IP address of a client is propagated to the K8s service instead of the IP address of the node.
* [ronaknathani.com: How a Kubernetes Pod Gets an IP Address 🌟](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address/)
* [opensource.com: Why I use Ingress Controllers to expose Kubernetes services](https://opensource.com/article/20/8/ingress-controllers-kubernetes) Kubernetes ingress controllers will make or break your cloud architecture.
* [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification/)
* [medium: How to setup Hetzner load balancer on a Kubernetes cluster](https://medium.com/@jmrobles/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)
* [zhimin-wen.medium.com: Sticky Sessions in Kubernetes 🌟](https://zhimin-wen.medium.com/sticky-sessions-in-kubernetes-56eb0e8f257d)
* [infoq.com: Kubernetes Ingress Is Now Generally Available](https://www.infoq.com/news/2020/09/kubernetes-ingress-ga/)
* [Learnk8s: Comparison of Kubernetes Ingress Controllers 🌟🌟](https://docs.google.com/spreadsheets/d/191WWNpjJ2za6-nbG4ZoUMXMpUK8KlCIosvQB0f-oq3k/edit#gid=907731238) How do you choose the *right* Kubernetes Ingress controller when: Not all Ingress controllers support UDP, Only Kong has a free LDAP integration, Nginx Ingress and HAProxy are the only two ingress without CRDs.
* [blog.alexellis.io: Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere/)
* [jmrobles.medium.com: How to setup Hetzner load balancer on a Kubernetes cluster](https://jmrobles.medium.com/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)
* [kubernetes.io: Scaling Kubernetes Networking With EndpointSlices](https://kubernetes.io/blog/2020/09/02/scaling-kubernetes-networking-with-endpointslices/) EndpointSlices are a new Kubernetes API that provides a scalable and extensible alternative to the Endpoints API.
* [medium: Create a Custom Annotation for the Kubernetes ingress-nginx Controller](https://medium.com/better-programming/creating-a-custom-annotation-for-the-kubernetes-ingress-nginx-controller-444e9d486192)
* [haproxy.com: Announcing HAProxy Kubernetes Ingress Controller 1.5 🌟](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-5/)
* [devclass.com: HAProxy Ingress Controller 1.5 introduces mTLS support, gives load balancing experts more power](https://devclass.com/2021/01/26/haproxy-ingress-controller-1_5/)
* [thenewstack.io: HAProxy Kubernetes Ingress Controller Moves Outside the Cluster](https://thenewstack.io/haproxy-kubernetes-ingress-controller-moves-outside-the-cluster/)
* [suse.com: NGINX Guest Blog: NGINX Kubernetes Ingress Controller 🌟](https://www.suse.com/c/nginx-guest-blog-kubernetes-ingress-controller)
* [blog.cloudflare.com: Moving k8s communication to gRPC](https://blog.cloudflare.com/moving-k8s-communication-to-grpc/)
* [K8GB - Kubernetes Global Balancer](https://github.com/AbsaOSS/k8gb) - [openshift.com: K8GB - Kubernetes Global Balancer ](https://www.openshift.com/blog/openshift-commons-briefing-k8gb-kubernetes-global-balancer-with-yuri-tsarev-absa-and-paul-morie-red-hat)
* [altoros.com: Kubernetes Networking: How to Write Your Own CNI Plug-in with Bash](https://www.altoros.com/blog/kubernetes-networking-writing-your-own-simple-cni-plug-in-with-bash/)
* [Network Node Manager](https://github.com/kakao/network-node-manager) network-node-manager is a kubernetes controller that controls the network configuration of a node to resolve network issues of kubernetes. By simply deploying and configuring network-node-manager, you can solve kubernetes network issues that cannot be resolved by kubernetes or resolved by the higher kubernetes Version. Below is a list of kubernetes's issues to be resolved by network-node-manager. network-node-manager is based on kubebuilder v2.3.1.
* [getenroute.io: Drive API Security At Kubernetes Ingress Using Helm And Envoy 🌟](https://getenroute.io/docs/ingress-filter-legos-secure-microservices-apis-using-helm-envoy/)
* [ithands-on.com: Kubernetes 101 : External services - ExternalName, DNS and Endpoints](https://www.ithands-on.com/2021/04/kubernetes-101-external-services.html)
* [ibm.com: Multizone Kubernetes and VPC Load Balancer Setup](https://www.ibm.com/cloud/blog/multizone-kubernetes-and-vpc-load-balancer-setup) Securely expose your Kubernetes app by setting up a Load Balancer for VPC in a different zone.
* [opensource.googleblog.com: Kubernetes: Efficient Multi-Zone Networking with Topology Aware Routing](https://opensource.googleblog.com/2020/11/kubernetes-efficient-multi-zone.html)
* [nbailey.ca: Domesticated Kubernetes Networking](https://nbailey.ca/post/k8s-networking/)
* [sookocheff.com: A Guide to the Kubernetes Networking Model 🌟](https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model/)
* [build.thebeat.co: A curious case of AWS NLB timeouts in Kubernetes](https://build.thebeat.co/a-curious-case-of-aws-nlb-timeouts-in-kubernetes-522bd88a3399) A debugging adventure that allowed us to solve the tail latencies our Kubernetes applications were experiencing when talking with our AWS NLB.
* [dzone: Multizone Kubernetes and VPC Load Balancer Setup](https://dzone.com/articles/multizone-kubernetes-and-vpc-load-balancer-setup) Securely expose your Kubernetes app by setting up a Load Balancer for VPC in a different zone.
* [ingressbuilder.jetstack.io 🌟🌟](https://ingressbuilder.jetstack.io) Ingress Builder allows users to select any annotation from the list of available controllers, to add to the ingress manifest.
* [itnext.io: Generating Kubernetes Network Policies Automatically By Sniffing Network Traffic 🌟](https://itnext.io/generating-kubernetes-network-policies-by-sniffing-network-traffic-6d5135fe77db) This blog post is about an experiment to automate creation of Kubernetes Network Policies based on actual network traffic captured from applications running on a Kubernetes cluster - [code](https://github.com/mcelep/blog/tree/master/automated-networkpolicy-generation)
* [medium: Using nginx-ingress controller to restrict access by IP (ip whitelisting) for a service deployed to a Kubernetes (AKS) cluster](https://medium.com/@maninder.bindra/using-nginx-ingress-controller-to-restrict-access-by-ip-ip-whitelisting-for-a-service-deployed-to-bd5c86dc66d6)
* [openshift.com: gRPC or HTTP/2 Ingress Connectivity in OpenShift 🌟](https://www.openshift.com/blog/grpc-or-http/2-ingress-connectivity-in-openshift)
* [inlets.dev: Fixing Ingress for short-lived local Kubernetes clusters](https://inlets.dev/blog/2021/07/08/short-lived-clusters.html)
* [nginx.com: How to Simplify Kubernetes Ingress and Egress Traffic Management](https://www.nginx.com/blog/how-to-simplify-kubernetes-ingress-egress-traffic-management/)
* [blog.teamhephy.info: Running Workflow Without Any LoadBalancer](https://blog.teamhephy.info/blog/posts/tutorials/running-workflow-without-any-loadbalancer.html)
* [blog.alexellis.io: Get a public LoadBalancer for your private Kubernetes cluster 🌟](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster/)
* [searchitoperations.techtarget.com: Differences between Kubernetes Ingress vs. load balancer](https://searchitoperations.techtarget.com/feature/Differences-between-Kubernetes-Ingress-vs-load-balancer) To manage Kubernetes cluster traffic, admins have a few choices. Compare Kubernetes Ingress vs. load balancers, as well as the NodePort and ClusterIP service types.
* [monzo.com: Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes)
* [medium: Access Application Externally In Kubernetes Cluster using Load Balancer Service](https://medium.com/codex/access-application-externally-in-kubernetes-cluster-using-load-balancer-service-d1b7858d51) Learn how to create a Pod and how to create a Load Balancer service using Kubernetes cluster. And access the application from outside.
* [itnext.io: Why and How of Kubernetes Ingress (and Networking) 🌟](https://itnext.io/why-and-how-of-kubernetes-ingress-and-networking-6cb308ca03d2)
* [techdozo.dev: gRPC load balancing on Kubernetes (using Headless Service)](https://techdozo.dev/grpc-load-balancing-on-kubernetes-using-headless-service/) 
* [thenewstack.io: ZeroLB, a New Decentralized Pattern for Load Balancing](https://thenewstack.io/zerolb-a-new-decentralized-pattern-for-load-balancing/)
* [ungleich.ch: Making kubernetes kube-dns publicly reachable](https://ungleich.ch/u/blog/kubernetes-making-dns-publicly-reachable/)
* [ungleich.ch: Building Ingress-less Kubernetes Clusters](https://ungleich.ch/u/blog/kubernetes-without-ingress/) Building Ingress-less Kubernetes Clusters with IPv6
* [thenewstack.io: Ingress Controllers: The More the Merrier](https://thenewstack.io/ingress-controllers-the-more-the-merrier/)
* [levelup.gitconnected.com: Setting up Application Load Balancer (Ingress) for the Pods running in AWS EKS Fargate](https://levelup.gitconnected.com/setting-up-application-load-balancer-ingress-for-the-pods-running-in-aws-eks-fargate-519e20e97497)
* [devopscube.com: Kubernetes Ingress Tutorial For Beginners 🌟](https://devopscube.com/kubernetes-ingress-tutorial/) In this Kubernetes ingress tutorial, you will learn the basic concepts of ingress, the native ingress resource object, and the concepts involved in ingress controllers
* [ystatit.medium.com: How to Change Kubernetes Kube-apiserver IP Address](https://ystatit.medium.com/how-to-change-kubernetes-kube-apiserver-ip-address-402d6ddb8aa2)
* [monzo.com: Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes)
* [tech2fun.net: Using Service Endpoints and Alias for accessing External Service in K8s](https://tech2fun.net/using-k8s-service-resource-for-enabling-clients-discovering-talking-to-pods/)
* [nginx.com: Reducing Kubernetes Costs by 70% in the Cloud with NGINX, Opsani, and Prometheus](https://www.nginx.com/blog/reducing-kubernetes-costs-70-percent-in-cloud-nginx-opsani-prometheus/)
* [ithands-on.com: Kubernetes 101 : Changing a service type](https://www.ithands-on.com/2021/09/kubernetes-101-changing-service-type.html) If we realize that our service, a ClusterIP doesn't suit our needs anymore, we could change its type to a  nodePort service for example.
* [cloud.redhat.com: Global Load Balancer Approaches 🌟](https://cloud.redhat.com/blog/global-load-balancer-approaches)
* [==loft.sh: Kubernetes NGINX Ingress: 10 Useful Configuration Options== 🌟](https://loft.sh/blog/kubernetes-nginx-ingress-10-useful-configuration-options) Kubernetes Ingress is the object that provides routing rules into your cluster. To best serve traffic to your app, you need to correctly configure it. This is an incredible article from loft.sh with 10 useful options for configuring NginX Ingress
* [==technos.medium.com: Kubernetes Services for Absolute Beginners — NodePort== 🌟](https://technos.medium.com/kubernetes-services-for-absolute-beginners-nodeport-139b7060fe3)
* [fransemalila.medium.com: Kubernetes Networking](https://fransemalila.medium.com/kubernetes-networking-cea2e1b7d2b3) To access the application over the network, K8s services must be used to expose the pods to external traffic and load balancing the traffic across multiple pods.
    * Cluster IP
    * Target Ports
    * Node Port
    * External IPs
    * Load Balancer

* [netris.ai: A Cloud-Like On-Prem Load Balancer for Kubernetes? (a practical guide)](https://www.netris.ai/cloud-like-load-balancer/)
* [==thenewstack.io: Ingress Controllers: The Swiss Army Knife of Kubernetes==](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)
* [==nginx.com: Kubernetes Networking 101==](https://www.nginx.com/blog/kubernetes-networking-101)
* [medium.com/the-programmer: Working With ClusterIP Service Type In Kubernetes](https://medium.com/the-programmer/working-with-clusterip-service-type-in-kubernetes-45f2c01a89c8) Working with services in Kubernetes Using ClusterIP
* [olamiko.medium.com: Technical Series: Kubernetes Networking](https://olamiko.medium.com/technical-series-kubernetes-networking-5a5dc3823163)
* [learnk8s.io: Tracing the path of network traffic in Kubernetes 🌟](https://learnk8s.io/kubernetes-network-packets)

## NetworkPolicy
- [opensource.com: What you need to know about Kubernetes NetworkPolicy](https://opensource.com/article/21/10/kubernetes-networkpolicy) Understanding Kubernetes NetworkPolicy is one of the fundamental requirements to learn before deploying an application to Kubernetes.

## Nginx Ingress controller
* [tech2fun.net: K8s Nginx Ingress Handling TLS Traffic and Using Pod Readiness Probes](https://tech2fun.net/k8s-nginx-ingress-handling-tls-traffic-and-using-pod-readiness-probes/)
* [blog.teamhephy.info: Learn how to use the Nginx Ingress controller to serve traffic over SSH with TCP load balancing](https://blog.teamhephy.info/blog/posts/tutorials/running-workflow-without-any-loadbalancer.html)
* [nginx.com: A Guide to Choosing an Ingress Controller, Part 4: NGINX Ingress Controller Options](https://www.nginx.com/blog/guide-to-choosing-ingress-controller-part-4-nginx-ingress-controller-options/)
* [NGINX Ingress Controller - v1.0.0](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.0.0) NGINX Ingress Controller v1.0.0 released today! The biggest change is the support to stable/v1 ingress object, and dropping support to v1beta1.
* [amy-ma.medium.com: Nginx Ingress Configuration](https://amy-ma.medium.com/ingress-configuration-d9f13c5bcf1a) Configure NGINX basic routing with TLS on HPCC. This tutorial provides steps on how to set up basic routing for ECLWatch with the NGINX Ingress controller and configure certificates using Cert-Manager.

## Gateway API
* [gateway-api.sigs.k8s.io 🌟](https://gateway-api.sigs.k8s.io/) Gateway API is an open source project managed by the SIG-NETWORK community. It's is a collection of resources that model service networking in Kubernetes. These resources - GatewayClass,Gateway, HTTPRoute, TCPRoute, Service, etc - aim to evolve Kubernetes service networking through expressive, extensible, and role-oriented interfaces that are implemented by many vendors and have broad industry support.
* [kubernetes.io: Evolving Kubernetes networking with the Gateway API](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-the-gateway-api/)
* [thenewstack.io: Unifying Kubernetes Service Networking (Again) with the Gateway API 🌟](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api/) The [Gateway API](https://gateway-api.sigs.k8s.io/), formerly known as the Services API and before that Ingress V2, was first discussed in detail — and in-person — at Kubecon 2019 in San Diego. There were already many well-known and [well-documented](https://dave.cheney.net/paste/ingress-is-dead-long-live-ingressroute.pdf) limitations of Ingress and Kubernetes networking APIs. The [Gateway API](https://www.youtube.com/watch?v=GiFQNevrxYA) was intended as a redo of these APIs, built on the lessons from Services, Ingress and the service mesh community.

## Kube-proxy
- [dustinspecker.com: iptables: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/iptables-how-kubernetes-services-direct-traffic-to-pods) In this article you will learn how Kubernetes's kube-proxy uses iptables to direct traffic to pods randomly. You'll focus on the ClusterIP type of Kubernetes services.
- [arthurchiao.art: Cracking kubernetes node proxy (aka kube-proxy)](https://arthurchiao.art/blog/cracking-k8s-node-proxy/) This post analyzes the Kubernetes node proxy model, and provides 5 demo implementations (within couples of lines of code) of the model, each based on different tech-stacks (userspace/iptables/ipvs/tc-ebpf/sock-ebpf).

## Multicloud communication for Kubernetes
* [developers.redhat.com: Use Skupper to connect multiple Kubernetes clusters 🌟](https://developers.redhat.com/blog/2021/04/20/use-skupper-to-connect-multiple-kubernetes-clusters/) - [skupper.io](https://skupper.io/) Multicloud communication for Kubernetes. Skupper is a layer 7 service interconnect. It enables secure communication across Kubernetes clusters with no VPNs or special firewall rules. With Skupper, your application can span multiple cloud providers, data centers, and regions.

## Multi-Cluster Kubernetes Networking
* [itnext.io: Multi-Cluster Kubernetes Networking with Netmaker](https://itnext.io/multi-cluster-kubernetes-networking-with-netmaker-bfa4e22eb2fb)
    * [NetMaker](https://github.com/gravitl/netmaker) Netmaker makes networks with WireGuard. Netmaker automates fast, secure, and distributed virtual networks.

## Kubernetes Network Policy
* [howtoforge.com: Network Policy in Kubernetes 🌟](https://www.howtoforge.com/kubernetes_network_policy/) By default, pods accept traffic from any source. A network policy helps to specify how a group of pods can communicate with each other and other network endpoints.
* [medium: How to Provision Network Policies in Kubernetes | AWS 🌟](https://medium.com/avmconsulting-blog/exploring-network-policies-in-kubernetes-c8a3d8ed00cb)
* [learncloudnative.com: Kubernetes Network Policy](https://www.learncloudnative.com/blog/2020-10-07-network-policies)
* [bionconsulting.com: Kubernetes Network Policies](https://www.bionconsulting.com/blog/kubernetes-network-policies)
    * [bionconsulting.com: Kubernetes Network Policies - Part 2](https://www.bionconsulting.com/blog/kubernetes-network-policies-part-2)
* [thenewstack.io: The Kubernetes Network Security Effect 🌟](https://thenewstack.io/the-kubernetes-network-security-effect/) Kubernetes has a built-in object for managing network security: NetworkPolicy. While it allows the user to define the relationship between pods with ingress and egress policies, it is basic and requires very precise IP mapping of a solution — which changes constantly, so most users I’ve talked to are not using it.
* [faun.pub: Control traffic flow to and from Kubernetes pods with Network Policies](https://faun.pub/control-traffic-flow-to-and-from-kubernetes-pods-with-network-policies-bc384c2d1f8c)
* [openshift.com: Network Policies: Controlling Cross-Project Communication on OpenShift](https://www.openshift.com/blog/network-policies-controlling-cross-project-communication-on-openshift)
* [loft-sh.medium.com: Kubernetes Network Policies: A Practitioner’s Guide 🌟](https://loft-sh.medium.com/kubernetes-network-policies-a-practitioners-guide-c9bb4cdd0dbc)
* [loft.sh: Kubernetes Network Policies: A Practitioner's Guide 🌟](https://loft.sh/blog/kubernetes-network-policies-a-practitioners-guide)
* [medium: Kubernetes Network Policies: Are They Really Useful? 🌟](https://medium.com/codex/kubernetes-network-polices-are-they-really-useful-c3a153c49316)
* [loft.sh: Kubernetes Network Policies for Isolating Namespaces 🌟](https://loft.sh/blog/kubernetes-network-policies-for-isolating-namespaces)

### Cilium 
* [cilium.io 🌟](https://cilium.io/) eBPF-based Networking, Observability, and Security
* [cilium.io: NetworkPolicy Editor: Create, Visualize, and Share Kubernetes NetworkPolicies 🌟](https://cilium.io/blog/2021/02/10/network-policy-editor)
* [editor.cilium.io 🌟](https://editor.cilium.io/) Learn how to create Network Policies for Kubernetes using an interactive playground
* [buoyant.io: Kubernetes network policies with Cilium and Linkerd](https://buoyant.io/2020/12/23/kubernetes-network-policies-with-cilium-and-linkerd)
* [itnext.io: Installing Cilium on Kubernetes in a fast and efficient way](https://itnext.io/installing-cilium-on-kubernetes-in-a-fast-and-efficient-way-dbcb79ce9699)
* [cilium.io: CNI Benchmark: Understanding Cilium Network Performance](https://cilium.io/blog/2021/05/11/cni-benchmark)

<center>
<script async class="speakerdeck-embed" data-id="9251193501114da199d70b2a679c552f" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>

### Kubernetes Network Policy Samples
- [==ahmetb/kubernetes-network-policy-recipes== 🌟](https://github.com/ahmetb/kubernetes-network-policy-recipes) Example recipes for Kubernetes Network Policies that you can just copy paste. This repository contains various use cases of Kubernetes Network Policies and sample YAML files to leverage in your setup. If you ever wondered how to drop/restrict traffic to applications running on Kubernetes, this is for you

## Kubernetes Ingress Specification
- [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18/)
- [medium: Ingress service types in Kubernetes 🌟](https://medium.com/faun/ingress-service-types-in-kubernetes-3e9b68b78307)

## Xposer Kubernetes Controller To Manage Ingresses
* [Xposer 🌟](https://github.com/stakater/Xposer) A Kubernetes controller to manage (create/update/delete) Kubernetes Ingresses based on the Service
    * Problem: We would like to watch for services running in our cluster; and create Ingresses and generate TLS certificates automatically (optional)
    * Solution: Xposer can watch for all the services running in our cluster; Creates, Updates, Deletes Ingresses and uses certmanager to generate TLS certificates automatically based on some annotations.

## Software-Defined IP Address Management (IPAM)
- [IP Address Management (IPAM)](https://en.wikipedia.org/wiki/IP_address_management)
- [fusionlayer.com: Software-Defined IP Address Management (IPAM)](https://www.fusionlayer.com/products/ip-address-management-software-defined-ipam-infinity)
    - Cloud computing and service automation are changing the way in which applications and data are being delivered and consumed. The existing 30-year-old networking model is failing to keep up with the automated service architectures and the Internet of Things (IoT) based on end-to-end automation.
    - **To facilitate the migration to cloud-era computing, service providers and data centers must add networking into the automated service workflows.** This requires agility and elasticity that traditional networking products are not designed to provide. As IT environments of tomorrow involve a plethora of orchestrators and controllers spinning up services and applications inside shared networks, they all must be managed and provisioned by a unified solution authoritative for all network-related information.

## CNI Container Networking Interface 
* [Kubernetes.io: Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
* [rancher.com: Container Network Interface (CNI) Providers](https://rancher.com/docs/rancher/v2.x/en/faq/networking/cni-providers/)
* [github.com/containernetworking 🌟](https://github.com/containernetworking)
    * [CNI](https://github.com/containernetworking/cni)
* [dzone: How to Understand and Set Up Kubernetes Networking 🌟](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking) Take a look at this tutorial that goes through and explains the inner workings of Kubernetes networking, including working with multiple networks.
* [medium: Container Networking Interface aka CNI](https://medium.com/@vikram.fugro/container-networking-interface-aka-cni-bdfe23f865cf)
* [itnext.io: Benchmark results of Kubernetes network plugins (CNI) over 10Gbit/s network (Updated: August 2020)](https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-august-2020-6e1b757b9e49) 

### List of existing CNI Plugins (IPAM)
- [Kubernetes Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- Overlay Network plugins:
    - [Flannel](https://github.com/coreos/flannel)
    - [Weave-net](https://www.weave.works/docs/net/latest/overview/)
- Routed Network Plugins:
    - [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)
    - [kube-router](https://www.kube-router.io/)
    - [Calico](https://www.projectcalico.org/)
    - [Canal](https://docs.projectcalico.org/getting-started/kubernetes/flannel/flannel)
    - [VMware-tanzu Antrea](https://github.com/vmware-tanzu/antrea)
- [IPAM](https://en.wikipedia.org/wiki/IP_address_management) modules:
    - dhcp
    - host-local
- Multi CNI plugins:
    - [Damn](https://github.com/nokia/danm)
    - [Multus](https://github.com/openshift/multus-cni)
    - [CNI-Genie](https://github.com/cni-genie/CNI-Genie)

<center>
[![kubernetes sdn solutions](images/kubernetes_sdn_solutions.png)](https://thenewstack.io/tigera-aims-ease-connectivity-pain-kubernetes/)
</center>

### Project Calico
* [tigera.io](https://www.tigera.io/)
* [Project Calico 🌟](https://www.projectcalico.org/) Secure networking for the cloud native era
* [medium: Calico for Kubernetes networking: the basics & examples](https://medium.com/flant-com/calico-for-kubernetes-networking-792b41e19d69)
* [thenewstack.io: Tigera's Calico Aims to Ease Connectivity Pain with Kubernetes](https://thenewstack.io/tigera-aims-ease-connectivity-pain-kubernetes/)
* [projectcalico.org: Advertising Kubernetes Service IPs with Calico and BGP](https://www.projectcalico.org/advertising-kubernetes-service-ips-with-calico-and-bgp/)
* [mhmxs.blogspot.com: Autoscaling Calico Route Reflector topology in Kubernetes](https://mhmxs.blogspot.com/2020/12/autoscaling-calico-route-reflector.html)
* [tigera.io: Enforcing Network Security Policies with GitOps – Part 1 (Calico + ArgoCD)](https://www.tigera.io/blog/enforcing-network-security-policies-with-gitops-part-1) Network policy is a key element of Kubernetes security. Network policy is expressed as a YAML configuration and works very well with GitOps. By adopting GitOps, security teams benefit in the following ways:
    * Take your policies with you. Kubernetes cluster creation from code is fairly common. It is much easier and less error-prone to push your Git-based policies to a new cluster.
    * You can monitor policy changes using information from pull requests. This will also be easy to integrate with your existing systems, instead of writing integrations from scratch. If something goes wrong, you can simply roll back to an earlier commit.
    * You can lock down who can deploy security policies. If you lock it down to only a single Git user, that will be easy to control. Everybody else can push their policy changes into Git via pull request.
    * Your GitOps tool can ensure that it will override any accidental or malicious change at runtime. This solves a major compliance concern. Git becomes the source of truth for your security policies.
    * It would be much easier to manage if no user could create a security policy from kubectl. Then you can enable de-centralized security by creating specific users for different services, and giving them rights to deploy only specific policies. Developers and DevOps teams are very comfortable with the notion of a Git pipeline.

## DNS Service with CoreDNS 
- [medium: How to Autoscale the DNS Service in a Kubernetes Cluster](https://medium.com/faun/how-to-autoscale-the-dns-service-in-a-kubernetes-cluster-cbb46ae89678)
- [thenewstack.io: Supercharge CoreDNS with Cluster Addons 🌟](https://thenewstack.io/supercharge-coredns-with-cluster-addons/)
- [sysdig.com: How to monitor coreDNS 🌟](https://sysdig.com/blog/how-to-monitor-coredns/) The most common problems and outages in a Kubernetes cluster come from coreDNS, so learning how to monitor coreDNS is crucial.
- [ungleich.ch: Making kubernetes kube-dns/CoreDNS publicly reachable](https://ungleich.ch/u/blog/kubernetes-making-dns-publicly-reachable/) 

## Kubernetes Node Local DNS Cache
- [NodeLocal DNSCache](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/20190424-NodeLocalDNS-beta-proposal.md)
- [Kubernetes Node Local DNS Cache](https://povilasv.me/kubernetes-node-local-dns-cache/)

## Kubernetes Sidecars
* [banzaicloud.com: Sidecar container lifecycle changes in Kubernetes 1.18 🌟](https://banzaicloud.com/blog/k8s-sidecars/)
* [medium: Delaying application start until sidecar is ready](https://medium.com/@marko.luksa/delaying-application-start-until-sidecar-is-ready-2ec2d21a7b74) Taking advantage of a peculiar Kubernetes implementation detail to block containers from starting before another container starts.


## Tweets
<details>
  <summary>Click to expand!</summary>

<center>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kubernetes is an example of what happens when you have an indefinitely complex network stack and no troubleshooting tools in place.</p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1458317772941713408?ref_src=twsrc%5Etfw">November 10, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Let&#39;s see how many folks here haven&#39;t seen this thread on Kubernetes Networking.<br><br>Once again, the thread doesn&#39;t try to explain the subject matter in great detail but offers a particular learning order instead.<br><br>As usual, based on my personal experience 🔽 <a href="https://t.co/pxCWJUxj5j">pic.twitter.com/pxCWJUxj5j</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1464922049604997121?ref_src=twsrc%5Etfw">November 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🧵 How does Pod to Pod communication work in Kubernetes?<br><br>How does the traffic reach the right Pod?<br><br>Let&#39;s see 👇 <a href="https://t.co/gF2eVWYL4Q">pic.twitter.com/gF2eVWYL4Q</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1488119972463218690?ref_src=twsrc%5Etfw">January 31, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>