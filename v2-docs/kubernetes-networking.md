# Kubernetes Networking

!!! info "Architectural Context"
    Detailed reference for Kubernetes Networking in the context of Networking & Service Mesh.

## Standard Reference

  - [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://blog.ovhcloud.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containo.us: Kubernetes Ingress & Service API Demystified](https://traefik.io/blog/kubernetes-ingress-service-api-demystified)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devclass.com: HAProxy Ingress Controller 1.5 introduces mTLS support, gives load balancing experts more power](https://www.devclass.com/containers/2021/01/26/haproxy-ingress-controller-15-introduces-mtls-support-gives-load-balancing-experts-more-power/1619777)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [getenroute.io: Drive API Security At Kubernetes Ingress Using Helm And Envoy 🌟](https://docs.getenroute.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: gRPC or HTTP/2 Ingress Connectivity in OpenShift 🌟](https://www.redhat.com/en/blog/grpc-or-http/2-ingress-connectivity-in-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [searchitoperations.techtarget.com: Differences between Kubernetes Ingress vs. load balancer](https://www.techtarget.com/searchitoperations/feature/Differences-between-Kubernetes-Ingress-vs-load-balancer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.redhat.com: Global Load Balancer Approaches 🌟](https://www.redhat.com/en/blog/global-load-balancer-approaches)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft.sh: Kubernetes NGINX Ingress: 10 Useful Configuration Options 🌟](https://www.vcluster.com/blog/kubernetes-nginx-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnk8s.io: Tracing the path of network traffic in Kubernetes 🌟](https://learnkube.com/kubernetes-network-packets)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.palark.com: Comparing Ingress controllers for Kubernetes](https://palark.com/blog/comparing-ingress-controllers-for-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Kubernetes Services: ClusterIP, Nodeport and LoadBalancer](https://www.sysdig.com/blog/kubernetes-services-clusterip-nodeport-loadbalancer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [otterize.com: Mastering Kubernetes networking: A journey in cloud-native packet management](https://www.cyera.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [editor.cilium.io 🌟🌟🌟](https://editor.networkpolicy.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Network Policies: Controlling Cross-Project Communication on OpenShift](https://www.redhat.com/en/blog/network-policies-controlling-cross-project-communication-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft.sh: Kubernetes Network Policies: A Practitioner's Guide 🌟](https://www.vcluster.com/blog/kubernetes-network-policies-a-practitioners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft.sh: Kubernetes Network Policies for Isolating Namespaces 🌟](https://www.vcluster.com/blog/kubernetes-network-policies-for-isolating-namespaces)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [buoyant.io: Kubernetes network policies with Cilium and Linkerd](https://www.buoyant.io/blog/kubernetes-network-policies-with-cilium-and-linkerd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fusionlayer.com: Software-Defined IP Address Management (IPAM)](https://www.fusionlayer.com/products/infinity)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — - Cloud computing and service automation are changing the way in which applications and data are being delivered and consumed. The existing 30-year-old networking model is failing to keep up with the automated service architectures and the Internet of Things (IoT) based on end-to-end automation.
    - **To facilitate the migration to cloud-era computing, service providers and data centers must add networking into the automated service workflows.** This requires agility and elasticity that traditional networking products are not designed to provide. As IT environments of tomorrow involve a plethora of orchestrators and controllers spinning up services and applications inside shared networks, they all must be managed and provisioned by a unified solution authoritative for all network-related information.
  - [Flannel](https://github.com/flannel-io/flannel) <span class='md-tag md-tag--info'>⭐ 9454</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — - [Weave-net](https://www.weave.works/)
  - [sysdig.com: How to monitor coreDNS 🌟](https://www.sysdig.com/blog/how-to-monitor-coredns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Project Calico](https://www.projectcalico.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Network Node Manager](https://github.com/kakao/network-node-manager) <span class='md-tag md-tag--info'>⭐ 109</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Fighting Service Latency in Microservices With Kubernetes](https://medium.com/@sindhujacynixit/fighting-service-latency-in-microservices-with-kubernetes-f5a584f5af36)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Kubernetes NodePort vs LoadBalancer vs Ingress? When should' I use what? 🌟](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: Get a LoadBalancer for your private Kubernetes cluster](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dustinspecker.com: How Do Kubernetes and Docker Create IP Addresses?!](https://dustinspecker.com/posts/how-do-kubernetes-and-docker-create-ip-addresses)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Service Types in Kubernetes? 🌟](https://medium.com/faun/service-types-in-kubernetes-24a1587677d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [speakerdeck.com: Kubernetes and networks. Why is this so dan hard? 🌟](https://speakerdeck.com/thockin/kubernetes-and-networks-why-is-this-so-dang-hard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eevans.co: Deconstructing Kubernetes Networking](https://eevans.co/blog/deconstructing-kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [externalTrafficPolicy=local on kubernetes. How to preserve the source IP in kubernetes](https://blog.getambassador.io/externaltrafficpolicy-local-on-kubernetes-e66e498212f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Why I use Ingress Controllers to expose Kubernetes services](https://opensource.com/article/20/8/ingress-controllers-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to setup Hetzner load balancer on a Kubernetes cluster](https://medium.com/@jmrobles/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [zhimin-wen.medium.com: Sticky Sessions in Kubernetes 🌟](https://zhimin-wen.medium.com/sticky-sessions-in-kubernetes-56eb0e8f257d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Kubernetes Ingress Is Now Generally Available](https://www.infoq.com/news/2020/09/kubernetes-ingress-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jmrobles.medium.com: How to setup Hetzner load balancer on a Kubernetes' cluster](https://jmrobles.medium.com/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Scaling Kubernetes Networking With EndpointSlices](https://kubernetes.io/blog/2020/09/02/scaling-kubernetes-networking-with-endpointslices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Create a Custom Annotation for the Kubernetes ingress-nginx Controller](https://medium.com/better-programming/creating-a-custom-annotation-for-the-kubernetes-ingress-nginx-controller-444e9d486192)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [haproxy.com: Announcing HAProxy Kubernetes Ingress Controller 1.5 🌟](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: HAProxy Kubernetes Ingress Controller Moves Outside the' Cluster](https://thenewstack.io/haproxy-kubernetes-ingress-controller-moves-outside-the-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [suse.com: NGINX Guest Blog: NGINX Kubernetes Ingress Controller 🌟](https://www.suse.com/c/nginx-guest-blog-kubernetes-ingress-controller)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudflare.com: Moving k8s communication to gRPC](https://blog.cloudflare.com/moving-k8s-communication-to-grpc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [K8GB - Kubernetes Global Balancer](https://github.com/AbsaOSS/k8gb) <span class='md-tag md-tag--info'>⭐ 1</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [altoros.com: Kubernetes Networking: How to Write Your Own CNI Plug-in with' Bash](https://www.altoros.com/blog/kubernetes-networking-writing-your-own-simple-cni-plug-in-with-bash)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ithands-on.com: Kubernetes 101 : External services - ExternalName, DNS and' Endpoints](https://www.ithands-on.com/2021/04/kubernetes-101-external-services.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.googleblog.com: Kubernetes: Efficient Multi-Zone Networking with' Topology Aware Routing](https://opensource.googleblog.com/2020/11/kubernetes-efficient-multi-zone.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nbailey.ca: Domesticated Kubernetes Networking](https://nbailey.ca/post/k8s-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sookocheff.com: A Guide to the Kubernetes Networking Model 🌟](https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [build.thebeat.co: A curious case of AWS NLB timeouts in Kubernetes](https://build.thebeat.co/a-curious-case-of-aws-nlb-timeouts-in-kubernetes-522bd88a3399)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Generating Kubernetes Network Policies Automatically By Sniffing' Network Traffic 🌟](https://itnext.io/generating-kubernetes-network-policies-by-sniffing-network-traffic-6d5135fe77db)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Using nginx-ingress controller to restrict access by IP (ip whitelisting)' for a service deployed to a Kubernetes (AKS) cluster](https://medium.com/@maninder.bindra/using-nginx-ingress-controller-to-restrict-access-by-ip-ip-whitelisting-for-a-service-deployed-to-bd5c86dc66d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [inlets.dev: Fixing Ingress for short-lived local Kubernetes clusters](https://inlets.dev/blog/2021/07/08/short-lived-clusters.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.teamhephy.info: Running Workflow Without Any LoadBalancer](https://blog.teamhephy.info/blog/posts/tutorials/running-workflow-without-any-loadbalancer.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Access Application Externally In Kubernetes Cluster using Load Balancer' Service](https://medium.com/codex/access-application-externally-in-kubernetes-cluster-using-load-balancer-service-d1b7858d51)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Why and How of Kubernetes Ingress (and Networking) 🌟](https://itnext.io/why-and-how-of-kubernetes-ingress-and-networking-6cb308ca03d2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [techdozo.dev: gRPC load balancing on Kubernetes (using Headless Service)](https://techdozo.dev/grpc-load-balancing-on-kubernetes-using-headless-service)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: ZeroLB, a New Decentralized Pattern for Load Balancing](https://thenewstack.io/zerolb-a-new-decentralized-pattern-for-load-balancing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ungleich.ch: Making kubernetes kube-dns publicly reachable](https://ungleich.ch/u/blog/kubernetes-making-dns-publicly-reachable)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ungleich.ch: Building Ingress-less Kubernetes Clusters](https://ungleich.ch/u/blog/kubernetes-without-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Ingress Controllers: The More the Merrier](https://thenewstack.io/ingress-controllers-the-more-the-merrier)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Setting up Application Load Balancer (Ingress)' for the Pods running in AWS EKS Fargate](https://levelup.gitconnected.com/setting-up-application-load-balancer-ingress-for-the-pods-running-in-aws-eks-fargate-519e20e97497)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: Kubernetes Ingress Tutorial For Beginners 🌟](https://devopscube.com/kubernetes-ingress-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ystatit.medium.com: How to Change Kubernetes Kube-apiserver IP Address](https://ystatit.medium.com/how-to-change-kubernetes-kube-apiserver-ip-address-402d6ddb8aa2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ithands-on.com: Kubernetes 101 : Changing a service type](https://www.ithands-on.com/2021/09/kubernetes-101-changing-service-type.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [technos.medium.com: Kubernetes Services for Absolute Beginners — NodePort' 🌟](https://technos.medium.com/kubernetes-services-for-absolute-beginners-nodeport-139b7060fe3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fransemalila.medium.com: Kubernetes Networking](https://fransemalila.medium.com/kubernetes-networking-cea2e1b7d2b3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Ingress Controllers: The Swiss Army Knife of Kubernetes](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/the-programmer: Working With ClusterIP Service Type In Kubernetes](https://medium.com/the-programmer/working-with-clusterip-service-type-in-kubernetes-45f2c01a89c8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [olamiko.medium.com: Technical Series: Kubernetes Networking](https://olamiko.medium.com/technical-series-kubernetes-networking-5a5dc3823163)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopslearners.com: Kubernetes Ingress Tutorial For Beginners](https://devopslearners.com/kubernetes-ingress-tutorial-for-beginners-26c2f7727bc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: How To Configure Ingress TLS/SSL Certificates in Kubernetes](https://devopscube.com/configure-ingress-tls-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: Getting Started with Kubernetes Ingress | Ben Hirschberg](https://www.armosec.io/blog/kubernetes-ingress-beginners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Service Type LB for On Prem Deployments](https://itnext.io/kubernetes-service-type-lb-for-on-prem-deployments-89e9b2a73a0c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/techbeatly: Kubernetes Networking Fundamentals](https://medium.com/techbeatly/kubernetes-networking-fundamentals-d30baf8a28c8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rajivsharma-2205.medium.com: Demystify how traffic reaches directly to pod' on using alb.ingress.kubernetes.io/target-type: ip](https://rajivsharma-2205.medium.com/demystify-how-traffic-reaches-directly-to-pod-on-using-alb-ingress-kubernetes-io-target-type-ip-f2d1be346b46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/linux-shots: Kubernetes ingress as reverse proxy to Application' running outside cluster](https://medium.com/linux-shots/kubernetes-ingress-as-reverse-proxy-to-application-running-outside-cluster-206b6003f9cb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@zhaoyi0113: Kubernetes — How does service network work in the' cluster](https://medium.com/@zhaoyi0113/kubernetes-how-does-service-network-work-in-the-cluster-d235b69ff536)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@pavanbelagatti: Kubernetes Service Types Explained 🌟](https://medium.com/@pavanbelagatti/kubernetes-service-types-explained-2709cde3bc0c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tkng.io: The Kubernetes Networking Guide 🌟🌟](https://www.tkng.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tkng.io/arch: THE KUBERNETES NETWORK MODEL 🌟🌟](https://www.tkng.io/arch)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/stakater: Efficiently Expose Services on Kubernetes (part 1)' 🌟](https://medium.com/stakater/efficiently-expose-services-on-kubernetes-494a80f88aad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [platform9.com: Ultimate Guide to Kubernetes Ingress Controllers 🌟](https://platform9.com/blog/ultimate-guide-to-kubernetes-ingress-controllers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kubernetes Service Types Tutorial | Pavan Belagatti 🌟](https://faun.pub/kubernetes-service-types-tutorial-39223391316c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/slalom-build: Managing Ingress Traffic on Kubernetes Platforms' 🌟](https://medium.com/slalom-build/managing-ingress-traffic-on-kubernetes-platforms-ebd537cdfb46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [craig-godden-payne.medium.com: How does ingress work in Kubernetes?](https://craig-godden-payne.medium.com/how-does-ingress-work-in-kubernetes-f3b121d0351f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dustinspecker.com: Kubernetes Networking from Scratch: Using BGP and BIRD' to Advertise Pod Routes](https://dustinspecker.com/posts/kubernetes-networking-from-scratch-bgp-bird-advertise-pod-routes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [home.robusta.dev: The ultimate guide to Kubernetes Services, LoadBalancers,' and Ingress 🌟🌟🌟](https://home.robusta.dev/blog/kubernetes-service-vs-loadbalancer-vs-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sanjimoh.medium.com: Demystifying Kubernetes Networking — Episode 1](https://sanjimoh.medium.com/demystifying-kubernetes-networking-episode-1-ca5605a97f87)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Tune up your Kubernetes Application Performance with a small DNS' Configuration](https://dev.to/imjoseangel/tune-up-your-kubernetes-application-performance-with-a-small-dns-configuration-1o46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@mehmetodabashi: Kubernetes networking and service object: Understanding' ClusterIp and nodePort with hands on study](https://medium.com/@mehmetodabashi/kubernetes-networking-and-service-object-understanding-clusterip-and-nodeport-with-hands-on-study-90cfeaf66e8c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jasonmfehr: Inspecting Kubernetes Client to API Server Network' Traffic](https://medium.com/@jasonmfehr/inspecting-kubernetes-client-to-api-server-network-traffic-cd6d1802bb43)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: K8s Network — CNI Introduction](https://medium.com/geekculture/k8s-network-cni-introduction-b035d42ad68f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/patilswapnilv: Getting Started with Kubernetes Networking' 🌟](https://medium.com/patilswapnilv/getting-started-with-kubernetes-networking-7e10623fc78f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kubernetes Ingress with Nginx](https://faun.pub/kubernetes-ingress-with-nginx-3c77e703e91a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Inspecting and Understanding k8s Service Network 🌟](https://itnext.io/inspecting-and-understanding-service-network-dfd8c16ff2c5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ovidiuborlean.medium.com: Networking latency measurement in Kubernetes with' Sockperf plugin](https://ovidiuborlean.medium.com/networking-latency-measurement-in-kubernetes-with-sockperf-plugin-68283a0ed989)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes networking deep dive: Did you make the right choice?](https://itnext.io/kubernetes-network-deep-dive-7492341e0ab5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@muhidabid.cs: Why does Kubernetes need Ingress?](https://medium.com/@muhidabid.cs/why-does-kubernetes-need-ingress-73d969fb6ffe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s — ipvs Mode Introduction](https://blog.devgenius.io/k8s-ipvs-mode-introduction-6457a02cd91a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [edureka.co: Kubernetes Networking – A Comprehensive Guide To The Networking' Concepts In Kubernetes](https://www.edureka.co/blog/kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [whyk8s.substack.com: Why not DNS?](https://whyk8s.substack.com/p/why-not-dns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: Kubernetes Gateway API: The Intro You Need To Read](https://medium.com/geekculture/kubernetes-gateway-api-the-intro-you-need-to-read-80965f7acd82)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ksingh7.medium.com: Kubernetes Endpoint Object: Your Bridge to External' Services 🌟🌟](https://ksingh7.medium.com/kubernetes-endpoint-object-your-bridge-to-external-services-3fc48263b776)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@ahmet16ck: What Is Load Balancer and How Does It Work In Kubernetes' ? 🌟](https://medium.com/@ahmet16ck/what-is-load-balancer-and-how-does-it-work-in-kubernetes-5ab5f0537069)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [api7.ai: How Does APISIX Ingress Support Thousands of Pod Replicas?](https://api7.ai/blog/apisix-ingress-support-thousands-pod-replicas)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/illuminations-mirror: Basic | Networking and Communication Between' Pods in Kubernetes](https://medium.com/illuminations-mirror/basic-networking-and-communication-between-pods-in-kubernetes-2e1627b03a87)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devops.dev: Networking in Kubernetes](https://blog.devops.dev/networking-in-kubernetes-55dcf794b9cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@mustafaaltunok: How Ingress, Service, Deployment and Pod Link' to each other](https://medium.com/@mustafaaltunok/how-ingress-service-deployment-and-pod-link-to-eachother-d3a6ae2c0e06)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [inlets.dev: How to Get Ingress for Private Kubernetes Clusters](https://inlets.dev/blog/2023/02/24/ingress-for-local-kubernetes-clusters.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devops.dev: Demystifying Kubernetes:Understanding Ingress, Configuration,' and Best Practices](https://blog.devops.dev/demystifying-kubernetes-understanding-ingress-configuration-and-best-practices-fb34e33e5f5f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/narasimha1997: Communication between Microservices in a Kubernetes' cluster 🌟](https://dev.to/narasimha1997/communication-between-microservices-in-a-kubernetes-cluster-1n41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/google-cloud: Kubernetes Ingress Vs Gateway API 🌟](https://medium.com/google-cloud/kubernetes-ingress-vs-gateway-api-647ee233693d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/nerd-for-tech: Kubernetes: Deploying NGINX with a ConfigMap |' Chanel Jemmott](https://medium.com/nerd-for-tech/kubernetes-deploying-nginx-with-a-configmap-e8a2fe59bcb1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@sangjinn: How to communicate with Kubernetes workloads — Part' I. Service | Brandon Kang](https://medium.com/@sangjinn/how-to-communicate-with-kubernetes-workloads-1-service-abe1c5b03fc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [shahneil.medium.com: What Are Kubernetes Endpoints?](https://shahneil.medium.com/what-are-kubernetes-endpoints-and-how-to-use-them-a5a5da56f4d4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fr4nk.xyz: Understanding Ingress in Kubernetes: A Comprehensive Guide](https://fr4nk.xyz/understanding-ingress-in-kubernetes-a-comprehensive-guide-b23b5cf37f8d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Otterize: Intent-Based Access Control for Kubernetes and' Cloud](https://thenewstack.io/otterize-intent-based-access-control-for-kubernetes-and-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [community.ops.io: Kubernetes Ingress Controller. How does it work?=](https://community.ops.io/danielepolencic/learning-how-an-ingress-controller-works-by-building-one-in-bash-3fni)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@rasikzilte711: Kubernetes Networking — A Guide to Services,' Ingress, Network Policies, DNS, and CNI Plugins](https://medium.com/@rasikzilte711/kubernetes-networking-a-guide-to-services-ingress-network-policies-dns-and-cni-plugins-fc1ad7d22ab4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/codex: Capture tcpdump with ksniff and wireshark from Kubernetes](https://medium.com/codex/capture-tcpdump-with-ksniff-and-wireshark-from-kubernetes-c212b93ff9f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudtechtwitter.com: Reverse Proxy vs. Forward Proxy: The Differences](https://www.cloudtechtwitter.com/2022/05/reverse-proxy-vs-forward-proxy.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [matthewpalmer.net: Kubernetes Networking Guide for Beginners](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-networking-guide-beginners.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Deciphering the Kubernetes Networking Maze: Navigating Load-Balance,' BGP, IPVS and Beyond](https://itnext.io/deciphering-the-kubernetes-networking-maze-navigating-load-balance-bgp-ipvs-and-beyond-7123ef428572)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [adil.medium.com: Network Traffic Shaping in Kubernetes: Topology Aware Routing](https://adil.medium.com/network-traffic-shaping-in-kubernetes-topology-aware-routing-e4ea4a03dd20)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudsigma.com: Kubernetes DNS Service: A Beginner’s Guide](https://blog.cloudsigma.com/kubernetes-dns-service-a-beginners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kuderko.medium.com: Fixing bad CPU usage distribution in Kubernetes 🌟](https://kuderko.medium.com/fixing-bad-cpu-usage-distribution-in-kubernetes-e1e43ed87cd6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Headless Kubernetes Service](https://medium.com/@bubu.tripathy/headless-k8s-service-924c689607a7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [goglides.dev: Headless services in Kubernetes Vs Regular Service: What,' Why, and How?](https://www.goglides.dev/bkpandey/headless-services-in-kubernetes-what-why-and-how-39fl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: What you need to know about Kubernetes NetworkPolicy](https://opensource.com/article/21/10/kubernetes-networkpolicy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: CKAD Scenarios about Ingress and NetworkPolicy](https://itnext.io/ckad-scenarios-about-ingress-and-networkpolicy-155ce958c9ce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [whyk8s.substack.com: Why NetworkPolicies?](https://whyk8s.substack.com/p/why-networkpolicies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [yuminlee2.medium.com: Kubernetes Network Policies](https://yuminlee2.medium.com/kubernetes-network-policies-a93c2f588e31)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bagas-awibowo.medium.com: Helm — Templating Network Policy using Helm](https://bagas-awibowo.medium.com/helm-templating-network-policy-using-helm-783b2f7e401a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NGINX Ingress Controller - v1.0.0](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.0.0) <span class='md-tag md-tag--info'>⭐ 19495</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>
  - [amy-ma.medium.com: Nginx Ingress Configuration](https://amy-ma.medium.com/ingress-configuration-d9f13c5bcf1a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: How to Setup Nginx Ingress Controller On Kubernetes – Detailed' Guide 🌟](https://devopscube.com/setup-ingress-kubernetes-nginx-controller)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jonathan_37674: How to secure Kubernetes ingress? | By ARMO](https://medium.com/@jonathan_37674/how-to-secure-kubernetes-ingress-by-armo-cb86086ec540)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.backmarket.com: How we improved third-party availability and' latency with Nginx in Kubernetes 🌟](https://engineering.backmarket.com/how-we-improved-third-party-availability-and-latency-with-nginx-in-kubernetes-bb3fc7224ae4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [towardsdev.com: Kubernetes: Deploying Nginx Servers with ConfigMaps & Shared' Services with Minikube](https://towardsdev.com/kubernetes-deploying-nginx-servers-with-configmaps-shared-services-with-minikube-618aee9a8ff6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: How to Monitor and Alert on Ingress-NGINX in Kubernetes](https://faun.pub/how-to-monitor-and-alert-on-nginx-ingress-in-kubernetes-6d7d172f0399)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sumanprasad.hashnode.dev: A Beginner's Guide to Ingress and Ingress Controllers' in Kubernetes](https://sumanprasad.hashnode.dev/a-beginners-guide-to-ingress-and-ingress-controllers-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [akyriako.medium.com: Configure path-based routing with Nginx Ingress Controller](https://akyriako.medium.com/configure-path-based-routing-with-nginx-ingress-controller-64a63cd4d6bd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mattias.engineer: Kubernetes-101: Ingress 🌟](https://mattias.engineer/k8s/ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [trstringer.com: Kubernetes Ingress with Contour](https://trstringer.com/kubernetes-ingress-with-contour)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gateway-api.sigs.k8s.io 🌟](https://gateway-api.sigs.k8s.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Evolving Kubernetes networking with the Gateway API](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-the-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Unifying Kubernetes Service Networking (Again) with the' Gateway API 🌟](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.flomesh.io: Kubernetes Gateway API — Evolution of Service Networking](https://blog.flomesh.io/kubernetes-gateway-api-evolution-of-service-networking-aa76ec4efa7e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: The New Kubernetes Gateway API and Its Use Cases](https://www.armosec.io/blog/kubernetes-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/google-cloud: Security with Kubernetes Gateway API 🌟](https://medium.com/google-cloud/security-with-kubernetes-gateway-api-dcbb934ed2a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [navendu.me: Comparing Kubernetes Gateway and Ingress APIs](https://navendu.me/posts/gateway-vs-ingress-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Use Skupper to connect multiple Kubernetes clusters' 🌟](https://developers.redhat.com/blog/2021/04/20/use-skupper-to-connect-multiple-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Multi-Cluster Kubernetes Networking with Netmaker](https://itnext.io/multi-cluster-kubernetes-networking-with-netmaker-bfa4e22eb2fb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtoforge.com: Network Policy in Kubernetes 🌟](https://www.howtoforge.com/kubernetes_network_policy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to Provision Network Policies in Kubernetes | AWS 🌟](https://medium.com/avmconsulting-blog/exploring-network-policies-in-kubernetes-c8a3d8ed00cb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learncloudnative.com: Kubernetes Network Policy](https://www.learncloudnative.com/blog/2020-10-07-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bionconsulting.com: Kubernetes Network Policies](https://www.bionconsulting.com/blog/kubernetes-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Kubernetes Network Security Effect 🌟](https://thenewstack.io/the-kubernetes-network-security-effect)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Control traffic flow to and from Kubernetes pods with Network' Policies](https://faun.pub/control-traffic-flow-to-and-from-kubernetes-pods-with-network-policies-bc384c2d1f8c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft-sh.medium.com: Kubernetes Network Policies: A Practitioner’s Guide' 🌟](https://loft-sh.medium.com/kubernetes-network-policies-a-practitioners-guide-c9bb4cdd0dbc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Kubernetes Network Policies: Are They Really Useful? 🌟](https://medium.com/codex/kubernetes-network-polices-are-they-really-useful-c3a153c49316)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [arthurchiao.art: Cracking Kubernetes Network Policy](https://arthurchiao.art/blog/cracking-k8s-network-policy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.mercari.com: Managing Network Policies for namespaces isolation' on a multi-tenant Kubernetes cluster](https://engineering.mercari.com/en/blog/entry/20220214-managing-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Simplify Kubernetes Network Policy Generation](https://blog.devgenius.io/kubernetes-namespace-wide-network-policy-1126fafdf221)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.slycreator.com: Network Policies: Understanding Kubernetes Network' Policies](https://blog.slycreator.com/network-policies-understanding-kubernetes-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: NetworkPolicy Editor: Create, Visualize, and Share Kubernetes' NetworkPolicies 🌟](https://cilium.io/blog/2021/02/10/network-policy-editor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Installing Cilium on Kubernetes in a fast and efficient way](https://itnext.io/installing-cilium-on-kubernetes-in-a-fast-and-efficient-way-dbcb79ce9699)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: CNI Benchmark: Understanding Cilium Network Performance](https://cilium.io/blog/2021/05/11/cni-benchmark)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cockroachlabs.com: How to use Cluster Mesh for Multi-Region Kubernetes Pod' Communication](https://www.cockroachlabs.com/blog/cockroachdb-kubernetes-cilium)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: Cilium 1.10: WireGuard, BGP Support, Egress IP Gateway, New Cilium' CLI, XDP Load Balancer, Alibaba Cloud Integration and more](https://cilium.io/blog/2021/05/20/cilium-110)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@charled.breteche: Kubernetes Security — Control pod to pod communications' with Cilium network policies](https://medium.com/@charled.breteche/kubernetes-security-control-pod-to-pod-communications-with-cilium-network-policies-d7275b2ed378)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterprogramming.pub: K8s: Network Policy Made Simple With Cilium Editor' 🌟](https://betterprogramming.pub/k8s-network-policy-made-simple-with-cilium-editor-a5b55781291c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ahmetb/kubernetes-network-policy-recipes 🌟](https://github.com/ahmetb/kubernetes-network-policy-recipes) <span class='md-tag md-tag--info'>⭐ 6139</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Ingress service types in Kubernetes 🌟](https://medium.com/faun/ingress-service-types-in-kubernetes-3e9b68b78307)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Autoscaling Ingress Controllers in  Kubernetes (Daniele Polencic)](https://itnext.io/autoscaling-ingress-controllers-in-kubernetes-c64b47088485)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/stakater/Xposer](https://github.com/stakater/Xposer) <span class='md-tag md-tag--info'>⭐ 32</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [IP Address Management (IPAM)](https://en.wikipedia.org/wiki/IP_address_management)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes.io: Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/containernetworking 🌟](https://github.com/containernetworking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: How to Understand and Set Up Kubernetes Networking 🌟](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Container Networking Interface aka CNI](https://medium.com/@vikram.fugro/container-networking-interface-aka-cni-bdfe23f865cf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Benchmark results of Kubernetes network plugins (CNI) over 10Gbit/s' network (Updated: August 2020)](https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-august-2020-6e1b757b9e49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Damn](https://github.com/nokia/danm) <span class='md-tag md-tag--info'>⭐ 393</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tigera.io](https://www.tigera.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Calico for Kubernetes networking: the basics & examples](https://medium.com/flant-com/calico-for-kubernetes-networking-792b41e19d69)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [projectcalico.org: Advertising Kubernetes Service IPs with Calico and BGP](https://www.projectcalico.org/advertising-kubernetes-service-ips-with-calico-and-bgp)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mhmxs.blogspot.com: Autoscaling Calico Route Reflector topology in Kubernetes](https://mhmxs.blogspot.com/2020/12/autoscaling-calico-route-reflector.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tigera.io: Enforcing Network Security Policies with GitOps – Part 1 (Calico' + ArgoCD)](https://www.tigera.io/blog/enforcing-network-security-policies-with-gitops-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s Networking — Calico (Part1)](https://blog.devgenius.io/k8s-networking-calico-part1-7f74395b6fe2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@arbnair97: Introduction to Kubernetes Network Policy and Calico' Based Network Policy](https://medium.com/@arbnair97/introduction-to-kubernetes-network-policy-and-calico-based-network-policy-675a7fa6b5dc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to Autoscale the DNS Service in a Kubernetes Cluster](https://medium.com/faun/how-to-autoscale-the-dns-service-in-a-kubernetes-cluster-cbb46ae89678)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Supercharge CoreDNS with Cluster Addons 🌟](https://thenewstack.io/supercharge-coredns-with-cluster-addons)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iamitcohen.medium.com: DNS in Kubernetes, how does it work?](https://iamitcohen.medium.com/dns-in-kubernetes-how-does-it-work-7c4690fd813e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nslookup.io: The life of a DNS query in Kubernetes](https://www.nslookup.io/learning/the-life-of-a-dns-query-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Kubernetes with CoreDNS](https://levelup.gitconnected.com/kubernetes-with-coredns-e40772c5e6ee)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NodeLocal DNSCache](https://github.com/kubernetes/enhancements) <span class='md-tag md-tag--info'>⭐ 3877</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [Kubernetes Node Local DNS Cache](https://povilasv.me/kubernetes-node-local-dns-cache)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.abaganon.com: Why you probably won’t use K8gb.io](https://blog.abaganon.com/going-global-with-kubernetes-490cf51e2bf8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/aws-builders: Amazon VPC Lattice — Build Applications, Not Networks](https://dev.to/aws-builders/amazon-vpc-lattice-build-applications-not-networks-59j8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Native Infrastructure

### Networking

#### Egress Traffic Control

##### Case Studies

  - [Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly regarded engineering case study by Monzo bank detailing how they designed and operated egress gateways to control and audit outbound traffic. Explains compliance benefits, custom proxy layers, and high-availability engineering patterns.
## Cloud Native Security

### Network Security

#### Network Policies

  - [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith' to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a methodology to empirically test and verify active Kubernetes Network Policies. Details the usage of programmatic probes to transition network security evaluation from abstract policy syntax configurations to verifiable network boundaries.

---
💡 **Explore Related:** [Caching](./caching.md) | [Web Servers](./web-servers.md) | [Istio](./istio.md)

