# Kubernetes Troubleshooting

1. [Introduction](#introduction)
2. [Kubernetes Events](#kubernetes-events)
3. [Kubernetes Network Troubleshooting](#kubernetes-network-troubleshooting)
4. [Exit Codes in Containers and Kubernetes](#exit-codes-in-containers-and-kubernetes)
5. [ImagePullBackOff](#imagepullbackoff)
6. [CrashLoopBackOff](#crashloopbackoff)
7. [Failed to Create Pod Sandbox](#failed-to-create-pod-sandbox)
8. [Terminated with exit code 1 error](#terminated-with-exit-code-1-error)
9. [Pod in Terminating or Unknown Status](#pod-in-terminating-or-unknown-status)
10. [OOM Kills](#oom-kills)
11. [Pause Container](#pause-container)
12. [Preempted Pod](#preempted-pod)
13. [Evited Pods](#evited-pods)
14. [Stuck Namespace](#stuck-namespace)
15. [Access PVC Data without the POD](#access-pvc-data-without-the-pod)
16. [CoreDNS issues](#coredns-issues)
17. [Debugging Techniques and Strategies. Debugging with ephemeral containers](#debugging-techniques-and-strategies-debugging-with-ephemeral-containers)
18. [Troubleshooting Tools](#troubleshooting-tools)
     1. [Komodor](#komodor)
     2. [Palaemon](#palaemon)
     3. [cdebug and debug-ctr](#cdebug-and-debug-ctr)
     4. [kubectl-debug](#kubectl-debug)
     5. [Kubeshark](#kubeshark)
19. [Slides](#slides)
20. [Images](#images)
21. [Tweets](#tweets)

## Introduction

- [==learnk8s.io: A visual guide on troubleshooting Kubernetes deployments== 🌟](https://learnk8s.io/troubleshooting-deployments)
- [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
- [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
- [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)
- [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating/)
- [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes/)
- [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples/)
- [levelup.gitconnected.com: 5 tips for troubleshooting apps on Kubernetes](https://levelup.gitconnected.com/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
- [medium: Common Kubernetes Errors Made by Beginners [2021] 🌟](https://medium.com/nerd-for-tech/common-kubernetes-errors-made-by-beginners-274b50e18a01)
- [cloud.redhat.com: Troubleshooting Sandboxed Containers Operator](https://cloud.redhat.com/blog/sandboxed-containers-operator-from-zero-to-hero-the-hard-way-part-2)
- [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes/)
- [kinvolk.io: Investigating Kubernetes performance issues with BPF](https://kinvolk.io/blog/2020/04/inside-kinvolk-labs-investigating-kubernetes-performance-issues-with-bpf/)
- [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
- [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot/)
- [youtube: 3 Ways to Detect Evil "Latest" Image Tags in Kubernetes - Kubevious](https://www.youtube.com/watch?v=93RlMqO4glM&t=6s&ab_channel=Kubevious) The "latest" image tag is a disaster waiting to happen. In this video, you will learn how to detect usage of the latest images using 3 different methods.
- [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands/)
- [dzone.com: The Three Pillars of Kubernetes Troubleshooting 🌟](https://dzone.com/articles/the-three-pillars-of-kubernetes-troubleshooting) Diving into how the three pillars of understanding, managing and preventing for Kubernetes troubleshooting, and how it helps to conceive of what’s needed to be able to properly troubleshoot real-world Kubernetes stacks that are the hallmark of complex, distributed systems.
- [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting/)
- [==itnext.io: Distroless Container Debugging on K8s/OpenShift==](https://itnext.io/distroless-container-debugging-on-k8s-openshift-e418fd66fdad)
    - When people focusing more on the security of containers, distroless based images are frequently used to reduce the attack surface. In these images, the package manager, the non-dependent modules or libraries, even the shells are stripped off, only the app and its required dependencies are kept. For the statically linked executable, produced by golang for example, we can even use “scratch” as the base.
    - The potential exploit of vulnerability is therefore greatly reduced. But, on the other hand, it is difficult to troubleshoot the application if even the shell is not available, leaving only the logs from the app.
    - In this paper, we will explore different options to facilitate debugging by bringing back the shell.
- [==speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps==](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)
- [containiq.com: Debugging Your Kubernetes Nodes in the ‘Not Ready’ State | nodenotready](https://www.containiq.com/post/debugging-kubernetes-nodes-in-not-ready-state) Kubernetes clusters typically run on multiple “nodes” each having its own state. In this article, you’ll learn a few possible reasons a node might enter the **NotReady** state and how you can debug it.
- [containiq.com: Troubleshooting Kubernetes FailedAttachVolume and FailedMount](https://www.containiq.com/post/fixing-kubernetes-failedattachvolume-and-failedmount) When working with Persistent Volumes in Kubernetes, you might run into the FailedAttachVolume or FailedMount error. In this tutorial, we’ll show you how to troubleshoot these errors and find the root cause and fix them.
- [medium.com/@andrewachraf: Detect crashes in your Kubernetes cluster using kwatch and Slack 🌟](https://medium.com/@andrewachraf/detect-crashes-in-your-cluster-using-kwatch-an-slack-84b979e93e03) Monitor all changes in your Kubernetes(K8s) cluster & detects crashes in your running apps in real time
- [==research.nccgroup.com: Detection Engineering for Kubernetes clusters==](https://research.nccgroup.com/2021/11/10/detection-engineering-for-kubernetes-clusters/) In this article you will learn how to detect anomalies in your cluster using Kubernetes Audit logs and Anomalies Detection Engineering.
- [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 1)](https://pauldally.medium.com/debugging-networkpolicy-part-1-249921cdba37)
    - [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 2)](https://pauldally.medium.com/debugging-networkpolicy-part-2-2d5c42d8465c)
- [==medium.com/@tina168wong: Kubernetes Ingress and Services troubleshooting==](https://medium.com/@tina168wong/kubernetes-ingress-and-services-troubleshooting-e2bb01007175) In this article, you will find some useful tips for troubleshooting the traffic flow in your cluster: from the Ingress to your Pods.
- [medium.com/geekculture: Common Pod Errors in Kubernetes to Watch Out For](https://medium.com/geekculture/common-pod-errors-in-kubernetes-to-watch-out-for-d808737f4ade)
- [==faun.pub: Kubernetes — Debugging NetworkPolicy (Part 1)==](https://faun.pub/debugging-networkpolicy-part-1-249921cdba37) For something as important as NetworkPolicy, debugging is surprisingly painful. In this article you will learn a few practical tips on how to debug your network policies
    - [==pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 2)==](https://pauldally.medium.com/debugging-networkpolicy-part-2-2d5c42d8465c)
- [tratnayake.dev: Oncall Adventures - When your Prometheus-Server mounted to GCE Persistent Disk on K8s is Full](https://tratnayake.dev/oncall-adventures-prometheus-filled-disk) In this article, you will follow Thilina's journey on debugging a failing Prometheus server on Kubernetes. The story starts with a wake-up call at 3.30 am 😅
- [==sysdig.com: Understanding Kubernetes pod pending problems==](https://sysdig.com/blog/kubernetes-pod-pending-problems/)
- [containiq.com: Kubernetes Node Disk Pressure | Troubleshooting w/ Example](https://www.containiq.com/post/kubernetes-disk-pressure) In this article, you’ll learn more about Kubernetes nodes experiencing disk pressure, including causes of disk pressure and a step-by-step guide to troubleshooting the error.
- [==blog.alexellis.io: How to Troubleshoot Applications on Kubernetes== 🌟](https://blog.alexellis.io/troubleshooting-on-kubernetes/) In this article, you will learn a practical framework to troubleshoot applications deployed on Kubernetes:
    - Is it there?
    - Why isn't it working?
    - It starts, but doesn't work
    - There are too many pods!
    - But can you `curl` it?
- [blog.devgenius.io: All You Need to Know about Debugging Kubernetes Cronjob](https://blog.devgenius.io/all-you-need-to-know-about-debugging-kubernetes-cronjob-61989a998513) Walkthrough tools & configs & knowledge used in Kubernetes cronjob/deployment debug. In this article, you will create and deploy a (broken) CronJob. Then you will debug it and in the process learn about environment variables, RBAC, pod resource configuration, logging, and more.
- [saiteja313.medium.com: Tracing DNS issues in Kubernetes](https://saiteja313.medium.com/tracing-dns-issues-in-kubernetes-28b38f782103)
- [medium.com/@jasonmfehr: Kubernetes Informers: Opening the Mystery Box](https://medium.com/@jasonmfehr/kubernetes-informers-opening-the-mystery-box-4cd690a43a4) In this article, you will learn how the team at Cloudera found a performance issue with Kubernetes informers and how they managed to rectify the issue
- [maxilect-company.medium.com: Graceful shutdown in a cloud environment (the example of Kubernetes + Spring Boot) 🌟](https://maxilect-company.medium.com/graceful-shutdown-in-a-cloud-environment-the-example-of-kubernetes-spring-boot-f922b41adaa0) In this article, you'll learn why it is crucial to think about graceful shutdown in Kubernetes and how you can approach this task. Many people think about starting an application in the cloud but rarely pay attention to how it ends. Once, we caught quite a few errors explicitly related to pods stopping. For example, we saw that Kubernetes occasionally kills our application before it releases resources, although it seems that this should not happen. It was impossible to reproduce the problem immediately, and we wondered what was happening under the hood?
- [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing API](https://martinheinz.dev/blog/85) Kubernetes v1.25 introduced Container Checkpointing API as an alpha feature. This provides a way to backup-and-restore containers running in Pods, without ever stopping them. This feature is primarily aimed at forensic analysis, but general backup-and-restore is something any Kubernetes user can take advantage of. So, let's take a look at this brand-new feature and see how we can enable it in our clusters and leverage it for backup-and-restore or forensic analysis.
- [madeeshafernando.medium.com: Capturing Heap Dumps of stateless Kubernetes pods before container termination and export to AWS S3](https://madeeshafernando.medium.com/capturing-heap-dumps-of-stateless-kubernetes-pods-before-container-termination-and-export-to-aws-s3-9602378ee60b)
- [faun.pub: Troubleshooting Kubernetes nodes storage space shortage on Aliyun (Alibaba Cloud)](https://faun.pub/troubleshooting-kubernetes-nodes-storage-space-shortage-on-aliyun-alibaba-cloud-ac28230fe3d3) In this article, you will follow Stephen's journey to identifying the root cause for cluster nodes running out of space on the Aliyun cloud
- [thenewstack.io: What David Flanagan Learned Fixing Kubernetes Clusters](https://thenewstack.io/what-david-flanagan-learned-fixing-kubernetes-clusters/) David Flanagan has fixed 50+ Kubernetes clusters as part of his YouTube series, 'Klustered.' He shared what he learned at Civo Navigate.
- [==github.com/metaleapca: metaleap-k8s-troubleshooting.pdf== 🌟🌟🌟](https://github.com/metaleapca/metaleap-k8s-troubleshooting/blob/main/metaleap-k8s-troubleshooting.pdf)
- [nicolasbarlatier.hashnode.dev: .NET Core Tip 2: How to troubleshoot Memory Leaks within a .NET Console application running in a Linux Docker Container in Kubernetes](https://nicolasbarlatier.hashnode.dev/net-core-tip-2-how-to-troubleshoot-memory-leaks-within-a-net-console-application-running-in-a-linux-docker-container-in-kubernetes) In this step-by-step guide, you will learn how to troubleshoot a memory leak in a .Net Core application running within a Kubernetes cluster.
- [blog.devgenius.io: All You Need to Know about Debugging Kubernetes Cronjob](https://blog.devgenius.io/all-you-need-to-know-about-debugging-kubernetes-cronjob-61989a998513) Walkthrough tools & configs & knowledge used in Kubernetes cronjob/deployment debug. In this article, you will create and deploy a (broken) CronJob. Then you will debug it and in the process learn about environment variables, RBAC, pod resource configuration, logging, and more
- [==dzone.com: Tackling the Top 5 Kubernetes Debugging Challenges==](https://dzone.com/articles/tackling-the-top-5-kubernetes-debugging-challenges) Bugs are inevitable and typically occur as a result of an error or oversight. Learn five Kubernetes debugging challenges and how to tackle them.
- [levelup.gitconnected.com: Access Kubernetes Objects Data From /Proc Directory 🌟](https://levelup.gitconnected.com/access-kubernetes-objects-data-from-proc-directory-8d2ec6a0faba) **The `/proc` directory is a special directory that holds all the details about our Linux system, such as — kernel, processes, and configuration parameters. In this article, you will learn how to explore the directory in a Kubernetes cluster**
- [learnitguide.net: How To Troubleshoot Kubernetes Pods](https://www.learnitguide.net/2023/04/how-to-troubleshoot-kubernetes-pods.html)
- [learnitguide.net: How to Check Memory Usage of a Pod in Kubernetes?](https://www.learnitguide.net/2023/04/how-to-check-memory-usage-of-pod-in.html)
- [alexsniffin.medium.com: Debugging Remotely with Go in Kubernetes](https://alexsniffin.medium.com/debugging-remotely-in-kubernetes-with-go-fda4f3332316) In this tutorial, you will learn how to debug an application deployed in Kubernetes remotely using VS Code and Delve
- [thenewstack.io: Kubernetes Troubleshooting Primer](https://thenewstack.io/kubernetes-troubleshooting-primer/) A quick methodology for overcoming common error messages with examples of commands to help — useful for both the administrator and developer alike.
- [devzero.io: Kubernetes Debugging Tips](https://www.devzero.io/blog/kubernetes-debugging-tips)
- [vik-y.medium.com: An easier way to auto-remediate memory leaks on Kubernetes!](https://vik-y.medium.com/an-easier-way-to-auto-remediate-memory-leaks-on-kubernetes-a922457674f4)
- [medium.com/@yusufkaratoprak: Advanced Troubleshooting Techniques in Kubernetes Pods](https://medium.com/@yusufkaratoprak/advanced-troubleshooting-techniques-in-kubernetes-pods-24ee0cebfa6f)

## Kubernetes Events

- [Understanding Kubernetes cluster events](https://banzaicloud.com/blog/k8s-cluster-logging/)
- [==containiq.com: Kubernetes Events: In-Depth Guide & Examples== 🌟](https://www.containiq.com/post/kubernetes-events) Kubernetes events help you understand how Kubernetes resource decisions are made and they can be helpful for debugging. Learn more about k8s events in this in-depth guide.
- [groundcover.com: Failure Is an Option: How to Stay on Top of K8s Container Events](https://www.groundcover.com/blog/k8s-container-events) Gain a deep understanding of how Kubernetes tracks container and Pod status, how it reports error information and how you can collect all of the above in an efficient way
- [decisivedevops.com: Kubernetes Events — News feed of your cluster](https://decisivedevops.com/kubernetes-events-news-feed-of-your-kubernetes-cluster-826e08892d7a/) Understand Kubernetes Events and learn to use kubectl events to monitor and troubleshoot your cluster’s issues effectively.

## Kubernetes Network Troubleshooting

- [==hwchiu.medium.com: Kubernetes Network Troubleshooting Approach== 🌟](https://hwchiu.medium.com/kubernetes-network-troubleshooting-approach-701de9463493)
- [itnext.io: Tracing Pod2Pod Network Traffic in Kubernetes | Daniele Polencic](https://itnext.io/tracing-pod-to-pod-network-traffic-in-kubernetes-112523a325b2)

## Exit Codes in Containers and Kubernetes

- [==komodor.com: Exit Codes In Containers & Kubernetes – The Complete Guide==  🌟](https://komodor.com/learn/exit-codes-in-containers-and-kubernetes-the-complete-guide/) In this article, you will learn everything there is to know about exit codes used by container engines to indicate reasons for container termination.

## ImagePullBackOff

- [==containiq.com: Kubernetes ImagePullBackOff: Troubleshooting With Examples==](https://www.containiq.com/post/kubernetes-imagepullbackoff) If you’ve worked with Kubernetes for a while, chances are good that you have experienced the **ImagePullBackOff** status. This issue can be frustrating if you are unfamiliar with it, so in this guide, you will walk the reader through how to troubleshoot this issue, what some common causes are, and where to start if they encounter this problem.
- [blog.ediri.io: Kubernetes: ImagePullBackOff!](https://blog.ediri.io/kubernetes-imagepullbackoff) How to keep your calm and fix this like a pro!

## CrashLoopBackOff

- [medium.com: Kubernetes Tip: How To Disambiguate A Pod Crash To Application Or To Kubernetes Platform? (CrashLoopBackOff)](https://medium.com/tailwinds-navigator/kubernetes-tip-how-to-disambiguate-a-pod-crash-to-application-or-to-kubernetes-platform-f6c1395a8d09)
- [devtron.ai: Troubleshoot: Pod Crashloopbackoff](https://devtron.ai/blog/troubleshoot_crashloopbackoff_pod/)
- [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods/) Why are Pod not fully restartable in Kubernetes? Why is Kubernetes not restarting the Pod in **CrashLoopBackOff**?
- [pauldally.medium.com: Why Leaving Pods in CrashLoopBackOff Can Have a Bigger Impact Than You Might Think](https://pauldally.medium.com/why-leaving-pods-in-crashloopbackoff-can-have-a-bigger-impact-than-you-might-think-c0d3dbd067a)
- [sysdig.com: What is Kubernetes CrashLoopBackOff? And how to fix it 🌟](https://sysdig.com/blog/debug-kubernetes-crashloopbackoff/) CrashLoopBackOff is a Kubernetes state representing a restart loop that is happening in a Pod: a container in the Pod is started but crashes and is then restarted over and over again. Learn what it is and how to fix it in this article
- [komodor.com: Kubernetes CrashLoopBackOff Error: What It Is and How to Fix It](https://komodor.com/learn/how-to-fix-crashloopbackoff-kubernetes-error)

## Failed to Create Pod Sandbox

- [containiq.com: Troubleshooting the “Failed to Create Pod Sandbox” Error](https://www.containiq.com/post/troubleshooting-failed-to-create-pod-sandbox-error) The “failed to create pod sandbox” error is a common problem when you’re trying to create a pod in Kubernetes. This article will explain the possible causes of the problem as well as how to fix it.

## Terminated with exit code 1 error

- [containiq.com: Troubleshooting ‘terminated with exit code 1’ error](https://www.containiq.com/post/terminated-with-exit-code-1) Sometimes Kubernetes pods die, leaving behind only cryptic messages such as “terminated with exit code 1”. In this guide, you’ll learn what this error indicates and how to troubleshoot it.

## Pod in Terminating or Unknown Status

- [tonylixu.medium.com: K8s Troubleshooting — Pod in Terminating or Unknown Status](https://tonylixu.medium.com/k8s-troubleshooting-pod-in-terminating-or-unknown-status-2878f6ec66b8) K8s Troubleshooting handbook
- [blog.devgenius.io: K8s Troubleshooting — Pod in Terminating or Unknown Status](https://blog.devgenius.io/k8s-troubleshooting-pod-in-terminating-or-unknown-status-2878f6ec66b8)

## OOM Kills

- [medium.com/@reefland: Tracking Down “Invisible” OOM Kills in Kubernetes](https://medium.com/@reefland/tracking-down-invisible-oom-kills-in-kubernetes-192a3de33a60) An “Invisible” OOM Kill happens when a child process in a container is killed, not the init process. It is “invisible” to Kubernetes and not detected. What is OOM? well.. not a good thing.
- [baykara.medium.com: A Gentle Inspection of OOMKilled in Kubernetes](https://baykara.medium.com/a-gentle-inspection-of-oomkilled-in-kubernetes-4b4124cd23a8) Quality of Service in Kubernetes
- [cloudyuga.guru: How does Kubernetes assign QoS class to pods through OOM score?](https://cloudyuga.guru/hands_on_lab/k8s-qos-oomkilled) This article discusses how to handle OOMKilled errors and how to configure Pod QoS to avoid them
- [sysdig.com: Kubernetes OOM and CPU Throttling](https://sysdig.com/blog/troubleshoot-kubernetes-oom/) Troubleshooting Memory and CPU problems. Do you know how memory and CPU usage can affect your cloud applications? In this article, you will discuss Out of Memory (OOM) and Throttling in Kubernetes.
- [medium.com/@bm54cloud: Stressing a Kubernetes Pod to Induce an OOMKilled Error](https://medium.com/@bm54cloud/stressing-a-kubernetes-pod-to-induce-an-oomkilled-error-96f3be9c931d) Learn about memory requests and limits, and what happens when those limits are exceeded
- [itnext.io: Kubernetes Silent Pod Killer](https://itnext.io/kubernetes-silent-pod-killer-104e7c8054d9) Tracking down invisible OOM Kills in Kubernetes
    - This article delves into the issue of "Invisible OOM Kills" in Kubernetes, where child processes getting OOM Killed go unnoticed.
    - An “Invisible” OOM Kill occurs when a child process in a container ( any process which is not the main process, PID 1 ) gets OOM Killed. In that scenario, the OOM Kill that occurred is “invisible” to Kubernetes, and as users we wouldn’t be aware of it.
    - The Solution: The entire scenario changes with Kubernetes version 1.28. Starting from that version, Kubernetes enables, by default, a cgroup v2 feature known as “cgroup grouping.”

## Pause Container

- [blog.devgenius.io: K8s — pause container](https://blog.devgenius.io/k8s-pause-container-f7abd1e9b488) Why we have pause container in K8s pod?

## Preempted Pod

- [blog.kumomind.com: What You Need To Know To Debug A Preempted Pod On Kubernetes](https://blog.kumomind.com/what-you-need-to-know-to-debug-a-preempted-pod-on-kubernetes) The purpose of this post is to share some thoughts on the management of a Kubernetes platform in production. The idea is to focus on a major problem that many beginners encounter: the management of preempted pods.

## Evited Pods

- [sysdig.com: Understanding Kubernetes Evicted Pods](https://sysdig.com/blog/kubernetes-pod-evicted/) What does it mean that Kubernetes Pods are evicted? They are terminated, usually due to a lack of resources. But why does this happen?

## Stuck Namespace

- [blog.ediri.io: How to remove a stuck namespace](https://blog.ediri.io/how-to-remove-a-stuck-namespace) With the help of the Kubernetes API
- [medium.com/@it-craftsman: How to fix Kubernetes namespaces stuck in terminating state](https://medium.com/@it-craftsman/how-to-fix-kubernetes-namespaces-stuck-in-terminating-state-ea46c5fff045)

## Access PVC Data without the POD

- [medium.com/@reefland: Access PVC Data without the POD; troubleshooting Kubernetes.](https://medium.com/@reefland/access-pvc-data-without-the-pod-troubleshooting-kubernetes-b28bfdd7502) I recently had a situation where Prometheus was stuck in a crash loop and unable to start. The solution is to delete a file within the Persistent Volume Claim (PVC). Seemed simple enough, however with the pod in a crash loop the PVC was not mounted within the Prometheus container. How can I deleted the file?

## CoreDNS issues

- [medium.com/geekculture: K8s Troubleshooting — How to Debug CoreDNS Issues](https://medium.com/geekculture/k8s-troubleshooting-how-to-debug-coredns-issues-724e8b973cfc)

## Debugging Techniques and Strategies. Debugging with ephemeral containers

- [kubectl-debug](https://github.com/aylei/kubectl-debug)
- [==loft.sh: Using Kubernetes Ephemeral Containers for Troubleshooting==](https://loft.sh/blog/using-kubernetes-ephemeral-containers-for-troubleshooting/)
- [kubesandclouds.com: Debugging with ephemeral containers in K8s (v1.18+)](https://kubesandclouds.com/index.php/2020/05/30/ephemeral-containers-in-k8s/)
- [How to quarantine pods](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods/)
- [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) KDBG (Kubernetes Debuger) is a small docker container based on lastest Alpine Linux image, used for debugging Kubernetes clusters from inside a pod.
- [inspektor-gadget](https://github.com/kinvolk/inspektor-gadget) Collection of gadgets for debugging and introspecting Kubernetes applications using BPF
    - [kinvolk.io](https://kinvolk.io)
- [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments](https://learnk8s.io/troubleshooting-deployments)
- [StatusBay](https://github.com/similarweb/statusbay) is a tool that provides the missing visibility into the K8S deployment process. The main goal is to ease the experience of troubleshooting and debugging services in K8S and provide confidence while making changes.
- [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
- [codefresh.io: Using Telepresence 2 for Kubernetes debugging and local development](https://codefresh.io/kubernetes-tutorial/telepresence-2-local-development/)
- [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75) The fastest and easiest way to debug and troubleshoot any application running on Kubernetes
- [tetrate.io: How to debug microservices in Kubernetes with proxy, sidecar or service mesh?](https://www.tetrate.io/blog/how-to-debug-microservices-in-kubernetes-with-proxy-sidecar-or-service-mesh)
- [rookout.com: The Definitive Guide To Kubernetes Application Debugging](https://www.rookout.com/blog/kubernetes-application-debugging)
- [thorsten-hans.com: Debugging apps in Kubernetes with Bridge](https://www.thorsten-hans.com/debugging-apps-in-kubernetes-with-bridge/) Bridge to Kubernetes simplifies and streamlines the process of debugging applications running in Kubernetes. Debug any language using the tools you prefer and love.
    - [marketplace.visualstudio.com: Bridge to Kubernetes (VSCode)](https://marketplace.visualstudio.com/items?itemName=mindaro.mindaro)
    - [marketplace.visualstudio.com: Bridge to Kubernetes (Visual Studio)](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.mindaro) Bridge to Kubernetes for Visual Studio 2019
- [==thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads== 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads/) **Kubernetes can't fix broken code. But if your container won't start or the app gets intermittent errors, here's how you can start debugging it. Most of the commands presented in the article will use kubectl or plugins which you can install via krew.**
- [==levelup.gitconnected.com: De-Mystifying Kubernetes Debugging==](https://levelup.gitconnected.com/de-mystifying-kubernetes-debugging-de9e1c82ac3e) __How to debug your microservice in VS Code with Bridge to Kubernetes__
- [==opensource.googleblog.com: Introducing Ephemeral Containers==](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html) **Ephemeral containers are a new type of container that are part of the Kubernetes core API. An Ephemeral Container may be added to an existing Pod for administrative actions like debugging, it runs until it exits, and it won't be restarted. An ephemeral container runs within the Pod's existing resource allocation and shares common container namespaces.**
- [linkedin.com: Kubernetes Ephemeral Containers | Bibin Wilson](https://www.linkedin.com/pulse/kubernetes-ephemeral-containers-bibin-wilson/) Ephemeral Containers is one of the k8s beta features. The following command will add the debug-image container to the running frontend pod and take an exec session for debugging: ```kubectl debug -it pods/frontend --image=debug-image```
- [sumanthkumarc.medium.com: Debugging namespace deletion issue in Kubernetes](https://sumanthkumarc.medium.com/debugging-namespace-deletion-issue-in-kubernetes-f6f8b40a4368)
- [medium.com/linux-shots: Debug Kubernetes Pods Using Ephemeral Container](https://medium.com/linux-shots/debug-kubernetes-pods-using-ephemeral-container-f01378243ff)
- [medium.com/@blgreco72: Debugging Kubernetes Services Locally 🌟](https://medium.com/@blgreco72/debugging-kubernetes-services-locally-8cb14bf8745a) There are various approaches for debugging Microservices hosted within Kubernetes. The approach used here does not alter the Kubernetes cluster in anyway to support developing Microservices, running external to the cluster, within the developer’s IDE. This is accomplished by mapping ports on the developer’s workstation to services that are normally only accessible from containers running within the cluster.
- [zendesk.engineering: Debugging containerd](https://zendesk.engineering/debugging-containerd-a20f28a2a8bf)
- [==heka-ai.medium.com: Introduction to Debugging: locally and live on Kubernetes with VSCode== 🌟](https://heka-ai.medium.com/introduction-to-debugging-locally-and-live-on-kubernetes-8c8ecd3acbaa) In this article, you'll learn how to debug your code in real-time on a Pod running on Kubernetes using VS Code
- [iximiuz.com: Kubernetes Ephemeral Containers and kubectl debug Command 🌟](https://iximiuz.com/en/posts/kubernetes-ephemeral-containers/) Learn how to use Ephemeral Containers to debug Kubernetes workloads with and without the kubectl debug command
- [eminaktas.medium.com: Debug Containerd in Production](https://eminaktas.medium.com/debug-containerd-in-production-fe93ef4e3ce2) In this article, you will learn how you can debug containerd with VSCode in a remote production environment.
- [medium.com/@alex.ivenin: Exploring ephemeral containers in kubernetes 🌟](https://medium.com/@alex.ivenin/exploring-ephemeral-containers-in-kubernetes-bcceaf21101c) Ephemeral containers, a feature that was introduced in Kubernetes 1.16 as an alpha release, advanced to beta status in version 1.23, and has finally graduated to stable status in Kubernetes 1.25. This capability provides an easy and safe way to debug running containers in a pod, without requiring full access to the underlying node.
- [labs.iximiuz.com: How to work with container images using ctr](https://labs.iximiuz.com/courses/containerd-cli/ctr/image-management) ctr is a command-line client shipped as part of the containerd project. If you have containerd running on a machine, chances are the ctr binary is also present there.
- [medium.com/@danielepolencic: Isolating kubernetes pods for debugging](https://medium.com/@danielepolencic/isolating-kubernetes-pods-for-debugging-5fe41e630e9) This article introduces a technique that helps you with debugging running Pods in production by changing labels, you can detach Pods from the Service (no traffic), and you troubleshoot them live
- [medium.com/adaltas: Kubernetes: debugging with ephemeral containers](https://medium.com/adaltas/kubernetes-debugging-with-ephemeral-containers-e4be659d9ef6) In this article, you will learn how to debug pods using kubectl debug and ephemeral containers

## Troubleshooting Tools

- [github.com/replicatedhq/troubleshoot](https://github.com/replicatedhq/troubleshoot) Troubleshoot is a framework for collecting and analyzing diagnostic information about a Kubernetes cluster. The framework is customizable and allows third-party application developers to create troubleshoot specs that can be run by cluster operators.
- [github.com/airwallex: k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector) k8s-pod-restart-info-collector is a simple Kubernetes customer controller that watches for Pods changes and collects K8s Pod restart reasons, logs, and events to Slack channels when a Pod restarts

### Komodor

- [==komodor.com==](https://komodor.com) Turn troubleshooting chaos into clarity. Komodor is an observability tool that gives you insight into what’s happening with your clusters and workloads. It integrates tools that we all use, like Datadog, Okta, LaunchDarkly, and PagerDuty.
- [==komodor.com: Kubernetes Troubleshooting: The Complete Guide== 🌟](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/)

### Palaemon

- [==palaemon.io==](https://palaemon.io) Open-source developer tool for monitoring Kubernetes clusters and error analysis
- [medium.com/@ospalaemon: Introducing Palaemon, the Savior of Kubernetes Pods!](https://medium.com/@ospalaemon/introducing-palaemon-the-savior-of-kubernetes-pods-85576c33287c)

### cdebug and debug-ctr

- [==iximiuz/cdebug==](https://github.com/iximiuz/cdebug) a swiss army knife of container debugging. It's like "docker exec", but it works even for containers without a shell (scratch, distroless, slim, etc). The "cdebug exec" command allows you to bring your own toolkit and start a shell inside of a running container.
- [==felipecruz91/debug-ctr==](https://github.com/felipecruz91/debug-ctr) A commandline tool for interactive troubleshooting when a container has crashed or a container image doesn't include debugging utilities, such as distroless images. Heavily inspired by kubectl debug, but for containers instead of Pods.

### kubectl-debug

- [github.com/JamesTGrant/kubectl-debug](https://github.com/JamesTGrant/kubectl-debug) kubectl-debug is a tool that lets you debug a target container in a Kubernetes cluster by automatically creating a new, non-invasive, 'debug' container in the same PID, network, user, and IPC namespace as the target container without any disruption

### Kubeshark

- [kubetools.io: Kubeshark – API Traffic Analyzer for Kubernetes](https://www.kubetools.io/kubernetes/mastering-kubernetes-debugging-and-troubleshooting-with-kubeshark-real-time-visibility-query-language-service-map-and-integrations/)

## Slides

??? note "Click to expand!"

    <center>
    <iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/e1c397b2aa67470e9204f82f938fec78?slide=1" title="KubeCologne keynote—Troubleshooting Kubernetes apps" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 560px; height: 314px;" data-ratio="1.78343949044586"></iframe>
    </center>

## Images

??? note "Click to expand!"

    <center>
    [![learnk8s debug your pods](images/learnk8s_debug_your_pods.png){: style="width:30%"}](https://learnk8s.io/troubleshooting-deployments)
    </center>

## Tweets

??? note "Click to expand!"

    <center>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">My top 8 commands and tools for debugging applications running on <a href="https://twitter.com/kubernetesio?ref_src=twsrc%5Etfw">@kubernetesio</a> 🧵👇</p>&mdash; Daniel Bryant (@danielbryantuk) <a href="https://twitter.com/danielbryantuk/status/1492893332850237444?ref_src=twsrc%5Etfw">February 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is your favourite Kubernetes troubleshooting command? Looking for some new ones 😉</p>&mdash; Saiyam Pathak (@SaiyamPathak) <a href="https://twitter.com/SaiyamPathak/status/1513572111721271298?ref_src=twsrc%5Etfw">April 11, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">I made a tool... to debug containers 🧙‍♂️<br><br>It&#39;s like &quot;docker exec&quot;, but it works even for containers without a shell (scratch, distroless, slim, etc).<br><br>The &quot;cdebug exec&quot; command allows you to bring your own toolkit and start a shell inside of a running container.<br><br>A short demo 👇 <a href="https://t.co/82m4vzPYJr">pic.twitter.com/82m4vzPYJr</a></p>&mdash; Ivan Velichko (@iximiuz) <a href="https://twitter.com/iximiuz/status/1584244173347074049?ref_src=twsrc%5Etfw">October 23, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">There is a Kubernetes deployment which processes items from a queue. Most items are very small and completed immediately. Occasionally a whopping big item comes along and causes an OOMKill. Retries don&#39;t help for obvious reasons.<br><br>How would you solve it?</p>&mdash; Natan Yellin (@aantn) <a href="https://twitter.com/aantn/status/1597653772255346691?ref_src=twsrc%5Etfw">November 29, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">How does Pod to Pod communication work in Kubernetes?<br><br>How does the traffic reach the pod?<br><br>Let&#39;s dive into how low-level networking works in Kubernetes. <a href="https://t.co/K8bBT8YiOf">pic.twitter.com/K8bBT8YiOf</a></p>&mdash; Daniele Polencic — @danielepolencic@hachyderm.io (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1655540892365889538?ref_src=twsrc%5Etfw">May 8, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>
