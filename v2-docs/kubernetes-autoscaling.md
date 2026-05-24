# Kubernetes Autoscaling

!!! info "Architectural Context"
    Detailed reference for Kubernetes Autoscaling in the context of The Container Stack.

## Standard Reference

  - [blog.scaleway.com: Understanding Kubernetes Autoscaling](https://www.scaleway.com/en/blog/understanding-kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Kubernetes pod autoscaler using custom metrics](https://www.sysdig.com/blog/kubernetes-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnk8s.io: Architecting Kubernetes clusters — choosing the best autoscaling strategy 🌟](https://learnkube.com/kubernetes-autoscaling-strategies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thinksys.com: Understanding Kubernetes Autoscaling](https://thinksys.com/devops/kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [HPA: Horizontal Pod Autoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [around25.com: Horizontal Pod Autoscaler in Kubernetes 🌟](https://www.around25.com/blog/horizontal-pod-autoscaler-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Trigger a Kubernetes HPA with Prometheus metrics](https://www.sysdig.com/blog/kubernetes-hpa-prometheus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [hub.helm.sh: cluster-autoscaler](https://artifacthub.io/packages/helm/stable/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kedify.io: Prometheus and Kubernetes Horizontal Pod Autoscaler don’t talk, KEDA does](https://www.kedify.io/resources/blog/prometheus-and-kubernetes-horizontal-pod-autoscaler-dont-talk-keda-does)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opcito.com: A guide to mastering autoscaling in Kubernetes with KEDA](https://www.opcito.com/blogs/a-guide-to-mastering-autoscaling-in-kubernetes-with-keda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Amazon Web Services: EKS Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html#cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — - [eksworkshop.com: Configure Cluster Autoscaler (CA)](https://eksworkshop.com/scaling/deploy_ca)
  - [Azure: AKS Cluster Autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Google Cloud Platform: GKE Cluster Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [DigitalOcean Kubernetes: DOKS Cluster Autoscaler](https://docs.digitalocean.com/products/kubernetes/how-to/autoscale)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: K8s Resource Management: An Autoscaling Cheat Sheet' 🌟](https://thenewstack.io/k8s-resource-management-an-autoscaling-cheat-sheet)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eksworkshop.com: Configure Cluster Autoscaler (CA)](https://eksworkshop.com/scaling/deploy_ca)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tomd.xyz: Event-driven integration on Kubernetes with Camel & KEDA](https://tomd.xyz/kubernetes-event-driven-keda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Effects of Docker Image Size on AutoScaling w.r.t' Single and Multi-Node Kube Cluster](https://levelup.gitconnected.com/effects-of-docker-image-size-on-autoscaling-w-r-t-single-and-multi-node-kube-cluster-29c4f689cd99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: 3 Autoscaling Projects to Optimise Kubernetes Costs](https://www.infracloud.io/blogs/3-autoscaling-projects-optimising-kubernetes-costs)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Kubernetes Autoscaling with Custom Metrics (updated) 🌟](https://www.infracloud.io/blogs/kubernetes-autoscaling-custom-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Reduce Kubernetes Costs Using Autoscaling Mechanisms](https://thenewstack.io/reduce-kubernetes-costs-using-autoscaling-mechanisms)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cast.ai: Guide to Kubernetes autoscaling for cloud cost optimization 🌟](https://cast.ai/blog/guide-to-kubernetes-autoscaling-for-cloud-cost-optimization)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Scaling Microservices on Kubernetes 🌟](https://thenewstack.io/scaling-microservices-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.ibm.com: Tutorial - Scalable webapp 🌟](https://cloud.ibm.com/docs/solution-tutorials?topic=solution-tutorials-scalable-webapp-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/airbnb-engineering: Dynamic Kubernetes Cluster Scaling at Airbnb](https://medium.com/airbnb-engineering/dynamic-kubernetes-cluster-scaling-at-airbnb-d79ae3afa132)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [chaitu-kopparthi.medium.com: Scaling Kubernetes workloads using custom Prometheus' metrics](https://chaitu-kopparthi.medium.com/scaling-kubernetes-workloads-using-custom-prometheus-metrics-1eb64b23919e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@niklas.uhrberg: Auto scaling in Kubernetes using Kafka and application' metrics — part 1](https://medium.com/@niklas.uhrberg/auto-scaling-in-kubernetes-using-kafka-and-application-metrics-part-1-a509256b64ff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openai.com: Scaling Kubernetes to 7,500 Nodes](https://openai.com/blog/scaling-kubernetes-to-7500-nodes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/mindboard: What is Autoscaling in Kubernetes?](https://medium.com/mindboard/what-is-autoscaling-in-kubernetes-109c7b5d321)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [clickittech.com: Kubernetes Autoscaling: How to use the Kubernetes Autoscaler](https://www.clickittech.com/devops/kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes: **Kubernetes Cluster Autoscaler**](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) <span class='md-tag md-tag--info'>⭐ 8858</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [gitconnected.com: Kubernetes Autoscaling 101: Cluster Autoscaler, Horizontal' Pod Autoscaler, and Vertical Pod Autoscaler](https://levelup.gitconnected.com/kubernetes-autoscaling-101-cluster-autoscaler-horizontal-pod-autoscaler-and-vertical-pod-2a441d9ad231)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [packet.com: Kubernetes Cluster Autoscaler](https://www.packet.com/resources/guides/kubernetes-cluster-autoscaler-on-packet)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Cluster Autoscaler: More than scaling out](https://itnext.io/kubernetes-cluster-autoscaler-more-than-scaling-out-7b2d97f10b27)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.ibm.com: Containers Troubleshoot Cluster Autoscaler](https://cloud.ibm.com/docs/containers?topic=containers-troubleshoot_cluster_autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [platform9.com: Kubernetes Autoscaling Options: Horizontal Pod Autoscaler,' Vertical Pod Autoscaler and Cluster Autoscaler](https://platform9.com/blog/kubernetes-autoscaling-options-horizontal-pod-autoscaler-vertical-pod-autoscaler-and-cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [banzaicloud.com: Autoscaling Kubernetes clusters](https://banzaicloud.com/blog/k8s-cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tech.deliveryhero.com: Dynamically overscaling a Kubernetes cluster with' cluster-autoscaler and Pod Priority](https://tech.deliveryhero.com/dynamically-overscaling-a-kubernetes-cluster-with-cluster-autoscaler-and-pod-priority)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Build Kubernetes Autoscaling for Cluster Nodes and Application Pods' 🌟](https://medium.com/better-programming/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Auto-Scaling Your Kubernetes Workloads (K8s) 🌟](https://medium.com/faun/autoscaling-in-kubernetes-cluster-bc55b8393a19)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Cluster Autoscaler in Kubernetes](https://medium.com/avmconsulting-blog/cluster-autoscaler-type-in-kubernetes-part2-f2ae432eefbb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Resources and Autoscaling — From Basics to Greatness' 🌟](https://itnext.io/kubernetes-resources-and-autoscaling-from-basics-to-greatness-7cae17fbf27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubedex.com: autoscaling 🌟](https://kubedex.com/autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [chrisedrego.medium.com: Kubernetes AutoScaling Series: Cluster AutoScaler' 🌟](https://chrisedrego.medium.com/kubernetes-autoscaling-series-cluster-autoscaler-5d60c10c3dc1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [the-gigi.github.io: Advanced Kubernetes Scheduling and Autoscaling](https://the-gigi.github.io/gigi-zone/posts/2024/05/advanced-k8s-scheduling-and-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [returngis.net: Escalado vertical de tus pods en Kubernetes con VerticalPodAutoscaler](https://www.returngis.net/2020/07/escalado-vertical-de-tus-pods-en-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Horizontal Pod Autoscaling with Custom Metric from Different' Namespace](https://itnext.io/horizontal-pod-autoscaling-with-custom-metric-from-different-namespace-f19f8446143b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes autoscaling with Istio metrics 🌟](https://medium.com/google-cloud/kubernetes-autoscaling-with-istio-metrics-76442253a45a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: 1/3 Autoscaling in Kubernetes: A Primer on Autoscaling](https://medium.com/expedia-group-tech/autoscaling-in-kubernetes-a-primer-on-autoscaling-7b8f0f95a928)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [superawesome.com: Scaling pods with HPA using custom metrics. How we scale' our kid-safe technology using Kubernetes 🌟](https://www.superawesome.com/blog/how-we-scale-our-kid-safe-technology-using-auto-scaling-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [velotio.com: Autoscaling in Kubernetes using HPA and VPA](https://www.velotio.com/engineering-blog/autoscaling-in-kubernetes-using-hpa-vpa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubectl-vpa](https://github.com/ninlil/kubectl-vpa) <span class='md-tag md-tag--info'>⭐ 4</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: K8s Vertical Pod Autoscaling 🌟](https://itnext.io/k8s-vertical-pod-autoscaling-fd9e602cbf81)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [czakozoltan08.medium.com: Stupid Simple Scalability](https://czakozoltan08.medium.com/stupid-simple-scalability-dc4a7fbe67d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudnatively.com: Understanding Horizontal Pod Autoscaling](https://www.cloudnatively.com/kubernetes-hpa-explanation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.px.dev: Horizontal Pod Autoscaling with Custom Metrics in Kubernetes' 🌟](https://blog.px.dev/autoscaling-custom-k8s-metric)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [awstip.com: Kubernetes HPA](https://awstip.com/kubernetes-hpa-8b7cf54f115)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@CloudifyOps: Setting up a Horizontal Pod Autoscaler for Kubernetes' cluster](https://medium.com/@CloudifyOps/setting-up-a-horizontal-pod-autoscaler-for-kubernetes-cluster-a7d3cf3be7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterprogramming.pub: Advanced Features of Kubernetes’ Horizontal Pod Autoscaler](https://betterprogramming.pub/advanced-features-of-kubernetes-horizontal-pod-autoscaler-536ebd7893ad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [code.egym.de: Horizontal Pod Autoscaler in Kubernetes (Part 1) — Simple' Autoscaling using Metrics Server](https://code.egym.de/horizontal-pod-autoscaler-in-kubernetes-part-1-simple-autoscaling-using-metrics-server-929e96cc2ab2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@kewynakshlley: Performance evaluation of the autoscaling strategies' vertical and horizontal using Kubernetes](https://medium.com/@kewynakshlley/performance-evaluation-of-the-autoscaling-strategies-vertical-and-horizontal-using-kubernetes-42d9a1663e6b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Stupid Simple Scalability](https://itnext.io/stupid-simple-scalability-dc4a7fbe67d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Scaling Your Application Using Kubernetes - Harness | Pavan Belagatti](https://faun.pub/scaling-your-application-using-kubernetes-9ad0d6bcf0d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dnastacio.medium.com: Infinite scaling with containers and Kubernetes](https://dnastacio.medium.com/kubernetes-resources-1a1fa1e72dcf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@badawekoo: Scaling in Kubernetes _What, Why and How?](https://medium.com/@badawekoo/scaling-in-kubernetes-what-why-and-how-d120e99be071)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pauldally.medium.com: HorizontalPodAutoscaler uses request (not limit) to' determine when to scale by percent](https://pauldally.medium.com/horizontalpodautoscaler-uses-request-not-limit-to-determine-when-to-scale-97643d808997)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Scaling Your Application With Kubernetes | Pavan Belagatti](https://dev.to/pavanbelagatti/scaling-your-application-with-kubernetes-5715)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [waswani.medium.com: Autoscaling Pods in Kubernetes](https://waswani.medium.com/autoscaling-pods-in-kubernetes-37d05000c41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mckornfield.medium.com: Working with HPAs in Kubernetes](https://mckornfield.medium.com/working-with-hpas-in-kubernetes-ced39263b596)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [code.egym.de: Vertical Pod Autoscaler in Kubernetes](https://code.egym.de/vertical-pod-autoscaler-in-kubernetes-b12a5c61393f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Intelligently estimating your Kubernetes resource needs!](https://faun.pub/intelligently-estimating-your-kubernetes-resource-needs-c12a75ea3138)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes: vertical Pods scaling with Vertical Pod Autoscaler](https://itnext.io/kubernetes-vertical-pods-scaling-with-vertical-pod-autoscaler-e2e5a3b8e1a9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@adityadhopade18: Mastering K8s Event Driven AutoScaling](https://medium.com/@adityadhopade18/mastering-k8s-event-driven-autoscaling-cd1b9df78903)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: Scale to Zero With Kubernetes with KEDA and/or Knative](https://dzone.com/articles/scale-to-zero-with-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/danielepolencic: Request-based autoscaling in Kubernetes: scaling' to zero](https://dev.to/danielepolencic/request-based-autoscaling-in-kubernetes-scaling-to-zero-2i73)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [keda.sh: Kubernetes Event-driven Autoscaling. Application autoscaling' made simple.](https://keda.sh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/backstagewitharchitects: How Autoscaling Works in Kubernetes?' Why You Need To Start Using KEDA?](https://medium.com/backstagewitharchitects/how-autoscaling-works-in-kubernetes-why-you-need-to-start-using-keda-b601b483d355)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [partlycloudy.blog: Horizontal Autoscaling in Kubernetes #3 – KEDA](https://partlycloudy.blog/2020/05/29/horizontal-autoscaling-in-kubernetes-3-keda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: CNCF KEDA 2.0 Scales up Event-Driven Programming on Kubernetes](https://thenewstack.io/microsoft-keda-2-0-scales-up-event-driven-programming-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudacode.com: How to Autoscale Kubernetes pods based on ingress request' — Prometheus, KEDA, and K6](https://blog.cloudacode.com/how-to-autoscale-kubernetes-pods-based-on-ingress-request-prometheus-keda-and-k6-84ae4250a9f3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@toonvandeuren: Kubernetes Scaling: The Event Driven Approach' - KEDA](https://medium.com/@toonvandeuren/kubernetes-scaling-the-event-driven-approach-bdd58ded4e3f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Autoscaling Your Kubernetes Microservice with KEDA](https://dzone.com/articles/autoscaling-your-kubernetes-microservice-with-keda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Scaling an app in Kubernetes with KEDA (no Prometheus is needed)](https://faun.pub/keda-ec9fc7c8dd81)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Event Driven Autoscaling](https://itnext.io/event-driven-autoscaling-503b5cefaa49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@casperrubaek: Why KEDA is a game-changer for scaling in Kubernetes](https://medium.com/@casperrubaek/why-keda-is-a-game-changer-for-scaling-in-kubernetes-4ebf34cb4b61)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Scale your Apps using KEDA in Kubernetes](https://levelup.gitconnected.com/scale-your-apps-using-keda-in-kubernetes-a1f2142ecc20)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devops.dev: KEDA: Autoscaling Kubernetes apps using Prometheus](https://blog.devops.dev/keda-autoscaling-kubernetes-apps-using-prometheus-da037fe572cf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [purushothamkdr453.medium.com: Event driven autoscaling in kubernetes using' KEDA](https://purushothamkdr453.medium.com/event-driven-autoscaling-in-kubernetes-using-keda-a0c16a383619)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@rtaplamaci: Horizontal Scaling on Kubernetes Clusters Based' on AWS CloudWatch Metrics with KEDA](https://medium.com/@rtaplamaci/horizontal-scaling-on-kubernetes-clusters-based-on-aws-cloudwatch-metrics-with-keda-7c9e0e3ba5f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@hirushanonline: Dynamic Scaling with Kubernetes Event-driven' Autoscaling (KEDA)](https://medium.com/@hirushanonline/dynamic-scaling-with-kubernetes-event-driven-autoscaling-keda-caaa15096e1c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kedacore/keda/issues/2214](https://github.com/kedacore/keda/issues/2214) <span class='md-tag md-tag--info'>⭐ 10216</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [dev.to/vinod827: Scale your apps using KEDA in Kubernetes](https://dev.to/vinod827/scale-your-apps-using-keda-in-kubernetes-4i3h)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bitnami/cluster-autoscaler](https://hub.docker.com/r/bitnami/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/danielepolencic: Scaling Kubernetes to multiple clusters and regions' 🌟](https://dev.to/danielepolencic/scaling-kubernetes-to-multiple-clusters-and-regionss-294b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.zalando.com: Building an End to End load test automation system' on top of Kubernetes](https://engineering.zalando.com/posts/2021/03/building-an-end-to-end-load-test-automation-system-on-top-of-kubernetes.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/teamsnap-engineering: Load Testing a Service with ~20,000 Requests' per Second with Locust, Helm, and Kustomize](https://medium.com/teamsnap-engineering/load-testing-a-service-with-20-000-requests-per-second-with-locust-helm-and-kustomize-ea9bea02ae28)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>


---
💡 **Explore Related:** [Container Managers](./container-managers.md) | [Kubernetes Monitoring](./kubernetes-monitoring.md) | [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md)

