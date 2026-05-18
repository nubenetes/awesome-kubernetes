# Kubernetes Autoscaling

!!! info "Architectural Context"
    Detailed reference for Kubernetes Autoscaling in the context of The Container Stack.

## Table of Contents

---

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
  - [Amazon Web Services: EKS Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html#cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Azure: AKS Cluster Autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Google Cloud Platform: GKE Cluster Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [DigitalOcean Kubernetes: DOKS Cluster Autoscaler](https://docs.digitalocean.com/products/kubernetes/how-to/autoscale)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: 3 Autoscaling Projects to Optimise Kubernetes Costs](https://www.infracloud.io/blogs/3-autoscaling-projects-optimising-kubernetes-costs)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Kubernetes Autoscaling with Custom Metrics (updated) 🌟](https://www.infracloud.io/blogs/kubernetes-autoscaling-custom-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Reduce Kubernetes Costs Using Autoscaling Mechanisms](https://thenewstack.io/reduce-kubernetes-costs-using-autoscaling-mechanisms)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cast.ai: Guide to Kubernetes autoscaling for cloud cost optimization 🌟](https://cast.ai/blog/guide-to-kubernetes-autoscaling-for-cloud-cost-optimization)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Scaling Microservices on Kubernetes 🌟](https://thenewstack.io/scaling-microservices-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.ibm.com: Tutorial - Scalable webapp 🌟](https://cloud.ibm.com/docs/solution-tutorials?topic=solution-tutorials-scalable-webapp-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [clickittech.com: Kubernetes Autoscaling: How to use the Kubernetes Autoscaler](https://www.clickittech.com/devops/kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kubernetes: **Kubernetes Cluster Autoscaler**](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Cluster Autoscaler: More than scaling out](https://itnext.io/kubernetes-cluster-autoscaler-more-than-scaling-out-7b2d97f10b27)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [platform9.com: Kubernetes Autoscaling Options: Horizontal Pod Autoscaler, Vertical Pod Autoscaler and Cluster Autoscaler](https://platform9.com/blog/kubernetes-autoscaling-options-horizontal-pod-autoscaler-vertical-pod-autoscaler-and-cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Resources and Autoscaling — From Basics to Greatness 🌟](https://itnext.io/kubernetes-resources-and-autoscaling-from-basics-to-greatness-7cae17fbf27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [the-gigi.github.io: Advanced Kubernetes Scheduling and Autoscaling](https://the-gigi.github.io/gigi-zone/posts/2024/05/advanced-k8s-scheduling-and-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [VPA: Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [returngis.net: Escalado vertical de tus pods en Kubernetes con VerticalPodAutoscaler](https://www.returngis.net/2020/07/escalado-vertical-de-tus-pods-en-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Horizontal Pod Autoscaling with Custom Metric from Different Namespace](https://itnext.io/horizontal-pod-autoscaling-with-custom-metric-from-different-namespace-f19f8446143b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [velotio.com: Autoscaling in Kubernetes using HPA and VPA](https://www.velotio.com/engineering-blog/autoscaling-in-kubernetes-using-hpa-vpa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubectl-vpa](https://github.com/ninlil/kubectl-vpa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: K8s Vertical Pod Autoscaling 🌟](https://itnext.io/k8s-vertical-pod-autoscaling-fd9e602cbf81)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.px.dev: Horizontal Pod Autoscaling with Custom Metrics in Kubernetes 🌟](https://blog.px.dev/autoscaling-custom-k8s-metric)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [code.egym.de: Horizontal Pod Autoscaler in Kubernetes (Part 1) — Simple Autoscaling using Metrics Server](https://code.egym.de/horizontal-pod-autoscaler-in-kubernetes-part-1-simple-autoscaling-using-metrics-server-929e96cc2ab2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Stupid Simple Scalability](https://itnext.io/stupid-simple-scalability-dc4a7fbe67d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Scaling Your Application With Kubernetes | Pavan Belagatti](https://dev.to/pavanbelagatti/scaling-your-application-with-kubernetes-5715)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [code.egym.de: Vertical Pod Autoscaler in Kubernetes](https://code.egym.de/vertical-pod-autoscaler-in-kubernetes-b12a5c61393f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes: vertical Pods scaling with Vertical Pod Autoscaler](https://itnext.io/kubernetes-vertical-pods-scaling-with-vertical-pod-autoscaler-e2e5a3b8e1a9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/danielepolencic: Request-based autoscaling in Kubernetes: scaling to zero](https://dev.to/danielepolencic/request-based-autoscaling-in-kubernetes-scaling-to-zero-2i73)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [keda.sh: Kubernetes Event-driven Autoscaling. Application autoscaling made simple.](https://keda.sh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [partlycloudy.blog: Horizontal Autoscaling in Kubernetes #3 – KEDA](https://partlycloudy.blog/2020/05/29/horizontal-autoscaling-in-kubernetes-3-keda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: CNCF KEDA 2.0 Scales up Event-Driven Programming on Kubernetes](https://thenewstack.io/microsoft-keda-2-0-scales-up-event-driven-programming-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Event Driven Autoscaling](https://itnext.io/event-driven-autoscaling-503b5cefaa49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/kedacore/keda/issues/2214](https://github.com/kedacore/keda/issues/2214)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/vinod827: Scale your apps using KEDA in Kubernetes](https://dev.to/vinod827/scale-your-apps-using-keda-in-kubernetes-4i3h)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bitnami/cluster-autoscaler](https://hub.docker.com/r/bitnami/cluster-autoscaler)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/danielepolencic: Scaling Kubernetes to multiple clusters and regions 🌟](https://dev.to/danielepolencic/scaling-kubernetes-to-multiple-clusters-and-regionss-294b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.zalando.com: Building an End to End load test automation system on top of Kubernetes](https://engineering.zalando.com/posts/2021/03/building-an-end-to-end-load-test-automation-system-on-top-of-kubernetes.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
