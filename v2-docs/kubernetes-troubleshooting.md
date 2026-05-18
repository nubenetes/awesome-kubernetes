# Kubernetes Troubleshooting

!!! info "Architectural Context"
    Detailed reference for Kubernetes Troubleshooting in the context of The Container Stack.

## Table of Contents

---

  - [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments 🌟](https://learnkube.com/troubleshooting-deployments)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.redhat.com: Troubleshooting Sandboxed Containers Operator](https://www.redhat.com/en/blog/sandboxed-containers-operator-from-zero-to-hero-the-hard-way-part-2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: 3 Ways to Detect Evil "Latest" Image Tags in Kubernetes - Kubevious](https://www.youtube.com/watch?v=93RlMqO4glM&t=6s&ab_channel=Kubevious)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Understanding Kubernetes pod pending problems](https://www.sysdig.com/blog/kubernetes-pod-pending-problems)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devzero.io: Kubernetes Debugging Tips](https://www.devzero.io/blog/kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: What is Kubernetes CrashLoopBackOff? And how to fix it 🌟](https://www.sysdig.com/blog/debug-kubernetes-crashloopbackoff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudyuga.guru: How does Kubernetes assign QoS class to pods through OOM score?](https://cloudyuga.guru/blogs/k8s-qos-oomkilled)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Kubernetes OOM and CPU Throttling](https://www.sysdig.com/blog/troubleshoot-kubernetes-oom)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sysdig.com: Understanding Kubernetes Evicted Pods](https://www.sysdig.com/blog/kubernetes-pod-evicted)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft.sh: Using Kubernetes Ephemeral Containers for Troubleshooting](https://www.vcluster.com/blog/using-kubernetes-ephemeral-containers-for-troubleshooting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubetools.io: Kubeshark – API Traffic Analyzer for Kubernetes](https://kubetools.io/mastering-kubernetes-debugging-and-troubleshooting-with-kubeshark-real-time-visibility-query-language-service-map-and-integrations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Distroless Container Debugging on K8s/OpenShift](https://itnext.io/distroless-container-debugging-on-k8s-openshift-e418fd66fdad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: How to Troubleshoot Applications on Kubernetes 🌟](https://blog.alexellis.io/troubleshooting-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: What David Flanagan Learned Fixing Kubernetes Clusters](https://thenewstack.io/what-david-flanagan-learned-fixing-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/metaleapca: metaleap-k8s-troubleshooting.pdf](https://github.com/metaleapca/metaleap-k8s-troubleshooting/blob/main/metaleap-k8s-troubleshooting.pdf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnitguide.net: How To Troubleshoot Kubernetes Pods](https://www.learnitguide.net/2023/04/how-to-troubleshoot-kubernetes-pods.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnitguide.net: How to Check Memory Usage of a Pod in Kubernetes?](https://www.learnitguide.net/2023/04/how-to-check-memory-usage-of-pod-in.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kubernetes Troubleshooting Primer](https://thenewstack.io/kubernetes-troubleshooting-primer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [groundcover.com: Failure Is an Option: How to Stay on Top of K8s Container Events](https://www.groundcover.com/blog/k8s-container-events)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [decisivedevops.com: Kubernetes Events — News feed of your cluster](https://decisivedevops.com/kubernetes-events-news-feed-of-your-kubernetes-cluster-826e08892d7a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Tracing Pod2Pod Network Traffic in Kubernetes | Daniele Polencic](https://itnext.io/tracing-pod-to-pod-network-traffic-in-kubernetes-112523a325b2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Exit Codes In Containers & Kubernetes – The Complete Guide  🌟](https://komodor.com/learn/exit-codes-in-containers-and-kubernetes-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devtron.ai: Troubleshoot: Pod Crashloopbackoff](https://devtron.ai/blog/troubleshoot_crashloopbackoff_pod)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Kubernetes CrashLoopBackOff Error: What It Is and How to Fix It](https://komodor.com/learn/how-to-fix-crashloopbackoff-kubernetes-error)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Silent Pod Killer](https://itnext.io/kubernetes-silent-pod-killer-104e7c8054d9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubectl-debug](https://github.com/aylei/kubectl-debug)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kinvolk.io](https://kinvolk.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [StatusBay](https://github.com/similarweb/statusbay)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thorsten-hans.com: Debugging apps in Kubernetes with Bridge](https://www.thorsten-hans.com/debugging-apps-in-kubernetes-with-bridge)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [marketplace.visualstudio.com: Bridge to Kubernetes (VSCode)](https://marketplace.visualstudio.com/items?itemName=mindaro.mindaro)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.googleblog.com: Introducing Ephemeral Containers](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkedin.com: Kubernetes Ephemeral Containers | Bibin Wilson](https://www.linkedin.com/pulse/kubernetes-ephemeral-containers-bibin-wilson)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iximiuz.com: Kubernetes Ephemeral Containers and kubectl debug Command 🌟](https://iximiuz.com/en/posts/kubernetes-ephemeral-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/airwallex: k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com](https://komodor.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Kubernetes Troubleshooting: The Complete Guide 🌟](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [palaemon.io](https://palaemon.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iximiuz/cdebug](https://github.com/iximiuz/cdebug)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [felipecruz91/debug-ctr](https://github.com/felipecruz91/debug-ctr)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
