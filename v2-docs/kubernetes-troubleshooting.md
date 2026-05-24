# Kubernetes Troubleshooting

!!! info "Architectural Context"
    Detailed reference for Kubernetes Troubleshooting in the context of The Container Stack.

## Standard Reference

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
  - [github.com/replicatedhq/troubleshoot](https://github.com/replicatedhq/troubleshoot) <span class='md-tag md-tag--info'>⭐ 582</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [A Complete Guide to Kubectl exec](https://refine.dev/blog/kubectl-exec-command)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/JamesTGrant/kubectl-debug](https://github.com/JamesTGrant/kubectl-debug) <span class='md-tag md-tag--info'>⭐ 374</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing' API](https://martinheinz.dev/blog/85)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Awesome Chaos Engineering](https://github.com/dastergon/awesome-chaos-engineering) <span class='md-tag md-tag--info'>⭐ 6564</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [labs.iximiuz.com: How to work with container images using ctr](https://labs.iximiuz.com/courses/containerd-cli/ctr/image-management)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [10 Real-World Kubernetes Troubleshooting Scenarios and Solutions](https://livingdevops.com/devops/10-real-world-kubernetes-troubleshooting-scenarios-and-solutions)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status' “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: 5 tips for troubleshooting apps on Kubernetes](https://levelup.gitconnected.com/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Distroless Container Debugging on K8s/OpenShift](https://itnext.io/distroless-container-debugging-on-k8s-openshift-e418fd66fdad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@andrewachraf: Detect crashes in your Kubernetes cluster using' kwatch and Slack 🌟](https://medium.com/@andrewachraf/detect-crashes-in-your-cluster-using-kwatch-an-slack-84b979e93e03)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 1)](https://pauldally.medium.com/debugging-networkpolicy-part-1-249921cdba37)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: Common Pod Errors in Kubernetes to Watch Out For](https://medium.com/geekculture/common-pod-errors-in-kubernetes-to-watch-out-for-d808737f4ade)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kubernetes — Debugging NetworkPolicy (Part 1)](https://faun.pub/debugging-networkpolicy-part-1-249921cdba37)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 2)](https://pauldally.medium.com/debugging-networkpolicy-part-2-2d5c42d8465c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tratnayake.dev: Oncall Adventures - When your Prometheus-Server mounted' to GCE Persistent Disk on K8s is Full](https://tratnayake.dev/oncall-adventures-prometheus-filled-disk)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: How to Troubleshoot Applications on Kubernetes 🌟](https://blog.alexellis.io/troubleshooting-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: All You Need to Know about Debugging Kubernetes Cronjob](https://blog.devgenius.io/all-you-need-to-know-about-debugging-kubernetes-cronjob-61989a998513)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [saiteja313.medium.com: Tracing DNS issues in Kubernetes](https://saiteja313.medium.com/tracing-dns-issues-in-kubernetes-28b38f782103)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jasonmfehr: Kubernetes Informers: Opening the Mystery Box](https://medium.com/@jasonmfehr/kubernetes-informers-opening-the-mystery-box-4cd690a43a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [maxilect-company.medium.com: Graceful shutdown in a cloud environment (the' example of Kubernetes + Spring Boot) 🌟](https://maxilect-company.medium.com/graceful-shutdown-in-a-cloud-environment-the-example-of-kubernetes-spring-boot-f922b41adaa0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [madeeshafernando.medium.com: Capturing Heap Dumps of stateless Kubernetes' pods before container termination and export to AWS S3](https://madeeshafernando.medium.com/capturing-heap-dumps-of-stateless-kubernetes-pods-before-container-termination-and-export-to-aws-s3-9602378ee60b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Troubleshooting Kubernetes nodes storage space shortage on Aliyun' (Alibaba Cloud)](https://faun.pub/troubleshooting-kubernetes-nodes-storage-space-shortage-on-aliyun-alibaba-cloud-ac28230fe3d3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: What David Flanagan Learned Fixing Kubernetes Clusters](https://thenewstack.io/what-david-flanagan-learned-fixing-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/metaleapca: metaleap-k8s-troubleshooting.pdf](https://github.com/metaleapca/metaleap-k8s-troubleshooting/blob/main/metaleap-k8s-troubleshooting.pdf) <span class='md-tag md-tag--info'>⭐ 40</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nicolasbarlatier.hashnode.dev: .NET Core Tip 2: How to troubleshoot Memory' Leaks within a .NET Console application running in a Linux Docker Container in Kubernetes](https://nicolasbarlatier.hashnode.dev/net-core-tip-2-how-to-troubleshoot-memory-leaks-within-a-net-console-application-running-in-a-linux-docker-container-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone.com: Tackling the Top 5 Kubernetes Debugging Challenges](https://dzone.com/articles/tackling-the-top-5-kubernetes-debugging-challenges)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Access Kubernetes Objects Data From /Proc Directory' 🌟](https://levelup.gitconnected.com/access-kubernetes-objects-data-from-proc-directory-8d2ec6a0faba)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnitguide.net: How To Troubleshoot Kubernetes Pods](https://www.learnitguide.net/2023/04/how-to-troubleshoot-kubernetes-pods.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learnitguide.net: How to Check Memory Usage of a Pod in Kubernetes?](https://www.learnitguide.net/2023/04/how-to-check-memory-usage-of-pod-in.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [alexsniffin.medium.com: Debugging Remotely with Go in Kubernetes](https://alexsniffin.medium.com/debugging-remotely-in-kubernetes-with-go-fda4f3332316)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kubernetes Troubleshooting Primer](https://thenewstack.io/kubernetes-troubleshooting-primer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [vik-y.medium.com: An easier way to auto-remediate memory leaks on Kubernetes!](https://vik-y.medium.com/an-easier-way-to-auto-remediate-memory-leaks-on-kubernetes-a922457674f4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@yusufkaratoprak: Advanced Troubleshooting Techniques in Kubernetes' Pods](https://medium.com/@yusufkaratoprak/advanced-troubleshooting-techniques-in-kubernetes-pods-24ee0cebfa6f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Understanding Kubernetes cluster events](https://banzaicloud.com/blog/k8s-cluster-logging)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [groundcover.com: Failure Is an Option: How to Stay on Top of K8s Container' Events](https://www.groundcover.com/blog/k8s-container-events)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [decisivedevops.com: Kubernetes Events — News feed of your cluster](https://decisivedevops.com/kubernetes-events-news-feed-of-your-kubernetes-cluster-826e08892d7a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [hwchiu.medium.com: Kubernetes Network Troubleshooting Approach 🌟](https://hwchiu.medium.com/kubernetes-network-troubleshooting-approach-701de9463493)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Tracing Pod2Pod Network Traffic in Kubernetes | Daniele Polencic](https://itnext.io/tracing-pod-to-pod-network-traffic-in-kubernetes-112523a325b2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Exit Codes In Containers & Kubernetes – The Complete Guide  🌟](https://komodor.com/learn/exit-codes-in-containers-and-kubernetes-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.ediri.io: Kubernetes: ImagePullBackOff!](https://blog.ediri.io/kubernetes-imagepullbackoff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Kubernetes Tip: How To Disambiguate A Pod Crash To Application' Or To Kubernetes Platform? (CrashLoopBackOff)](https://medium.com/tailwinds-navigator/kubernetes-tip-how-to-disambiguate-a-pod-crash-to-application-or-to-kubernetes-platform-f6c1395a8d09)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devtron.ai: Troubleshoot: Pod Crashloopbackoff](https://devtron.ai/blog/troubleshoot_crashloopbackoff_pod)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pauldally.medium.com: Why Leaving Pods in CrashLoopBackOff Can Have a Bigger' Impact Than You Might Think](https://pauldally.medium.com/why-leaving-pods-in-crashloopbackoff-can-have-a-bigger-impact-than-you-might-think-c0d3dbd067a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Kubernetes CrashLoopBackOff Error: What It Is and How to Fix' It](https://komodor.com/learn/how-to-fix-crashloopbackoff-kubernetes-error)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tonylixu.medium.com: K8s Troubleshooting — Pod in Terminating or Unknown' Status](https://tonylixu.medium.com/k8s-troubleshooting-pod-in-terminating-or-unknown-status-2878f6ec66b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s Troubleshooting — Pod in Terminating or Unknown Status](https://blog.devgenius.io/k8s-troubleshooting-pod-in-terminating-or-unknown-status-2878f6ec66b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@reefland: Tracking Down “Invisible” OOM Kills in Kubernetes](https://medium.com/@reefland/tracking-down-invisible-oom-kills-in-kubernetes-192a3de33a60)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [baykara.medium.com: A Gentle Inspection of OOMKilled in Kubernetes](https://baykara.medium.com/a-gentle-inspection-of-oomkilled-in-kubernetes-4b4124cd23a8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@bm54cloud: Stressing a Kubernetes Pod to Induce an OOMKilled' Error](https://medium.com/@bm54cloud/stressing-a-kubernetes-pod-to-induce-an-oomkilled-error-96f3be9c931d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Silent Pod Killer](https://itnext.io/kubernetes-silent-pod-killer-104e7c8054d9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s — pause container](https://blog.devgenius.io/k8s-pause-container-f7abd1e9b488)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kumomind.com: What You Need To Know To Debug A Preempted Pod On Kubernetes](https://blog.kumomind.com/what-you-need-to-know-to-debug-a-preempted-pod-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.ediri.io: How to remove a stuck namespace](https://blog.ediri.io/how-to-remove-a-stuck-namespace)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@it-craftsman: How to fix Kubernetes namespaces stuck in terminating' state](https://medium.com/@it-craftsman/how-to-fix-kubernetes-namespaces-stuck-in-terminating-state-ea46c5fff045)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@reefland: Access PVC Data without the POD; troubleshooting Kubernetes.](https://medium.com/@reefland/access-pvc-data-without-the-pod-troubleshooting-kubernetes-b28bfdd7502)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: K8s Troubleshooting — How to Debug CoreDNS Issues](https://medium.com/geekculture/k8s-troubleshooting-how-to-debug-coredns-issues-724e8b973cfc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubectl-debug](https://github.com/aylei/kubectl-debug) <span class='md-tag md-tag--info'>⭐ 2306</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [How to quarantine pods](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) <span class='md-tag md-tag--info'>⭐ 36</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kinvolk.io](https://kinvolk.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [StatusBay](https://github.com/similarweb/statusbay) <span class='md-tag md-tag--info'>⭐ 387</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tetrate.io: How to debug microservices in Kubernetes with proxy, sidecar' or service mesh?](https://www.tetrate.io/blog/how-to-debug-microservices-in-kubernetes-with-proxy-sidecar-or-service-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads' 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.googleblog.com: Introducing Ephemeral Containers](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [linkedin.com: Kubernetes Ephemeral Containers | Bibin Wilson](https://www.linkedin.com/pulse/kubernetes-ephemeral-containers-bibin-wilson)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sumanthkumarc.medium.com: Debugging namespace deletion issue in Kubernetes](https://sumanthkumarc.medium.com/debugging-namespace-deletion-issue-in-kubernetes-f6f8b40a4368)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/linux-shots: Debug Kubernetes Pods Using Ephemeral Container](https://medium.com/linux-shots/debug-kubernetes-pods-using-ephemeral-container-f01378243ff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@blgreco72: Debugging Kubernetes Services Locally 🌟](https://medium.com/@blgreco72/debugging-kubernetes-services-locally-8cb14bf8745a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [zendesk.engineering: Debugging containerd](https://zendesk.engineering/debugging-containerd-a20f28a2a8bf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [heka-ai.medium.com: Introduction to Debugging: locally and live on Kubernetes' with VSCode 🌟](https://heka-ai.medium.com/introduction-to-debugging-locally-and-live-on-kubernetes-8c8ecd3acbaa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iximiuz.com: Kubernetes Ephemeral Containers and kubectl debug Command 🌟](https://iximiuz.com/en/posts/kubernetes-ephemeral-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eminaktas.medium.com: Debug Containerd in Production](https://eminaktas.medium.com/debug-containerd-in-production-fe93ef4e3ce2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@alex.ivenin: Exploring ephemeral containers in kubernetes 🌟](https://medium.com/@alex.ivenin/exploring-ephemeral-containers-in-kubernetes-bcceaf21101c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@danielepolencic: Isolating kubernetes pods for debugging](https://medium.com/@danielepolencic/isolating-kubernetes-pods-for-debugging-5fe41e630e9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/adaltas: Kubernetes: debugging with ephemeral containers](https://medium.com/adaltas/kubernetes-debugging-with-ephemeral-containers-e4be659d9ef6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/airwallex: k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com](https://komodor.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [komodor.com: Kubernetes Troubleshooting: The Complete Guide 🌟](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [palaemon.io](https://palaemon.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@ospalaemon: Introducing Palaemon, the Savior of Kubernetes Pods!](https://medium.com/@ospalaemon/introducing-palaemon-the-savior-of-kubernetes-pods-85576c33287c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iximiuz/cdebug](https://github.com/iximiuz/cdebug) <span class='md-tag md-tag--info'>⭐ 1646</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [felipecruz91/debug-ctr](https://github.com/felipecruz91/debug-ctr) <span class='md-tag md-tag--info'>⭐ 52</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Debugging Kubernetes Systems: Practical Advice with Quality Telemetry](https://…)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Kubernetes

### Cluster Operations

#### GUI Clients

  - [KubeUI: A Desktop Kubernetes Client](https://github.com/IvanJosipovic/KubeUI) <span class='md-tag md-tag--info'>⭐ 308</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A native, desktop-optimized UI designed to stream, monitor, and interact with live cluster metrics and objects. Enhances developer agility through dynamic views of multi-cluster namespaces, container outputs, and active workload parameters.

---
💡 **Explore Related:** [Container Managers](./container-managers.md) | [Kubernetes Monitoring](./kubernetes-monitoring.md) | [Kubernetes Storage](./kubernetes-storage.md)

