# Kubernetes Troubleshooting
- [Introduction](#introduction)
- [Debugging Techniques and Strategies. Debugging with ephemeral containers](#debugging-techniques-and-strategies-debugging-with-ephemeral-containers)
- [Slides](#slides)
- [Images](#images)
- [Tweets](#tweets)

## Introduction
* [==learnk8s.io: A visual guide on troubleshooting Kubernetes deployments== 🌟](https://learnk8s.io/troubleshooting-deployments)
* [Understanding Kubernetes cluster events](https://banzaicloud.com/blog/k8s-cluster-logging/)
* [nigelpoulton.com: Troubleshooting kubernetes service discovery - Part 1](https://nigelpoulton.com/blog/f/troubleshooting-kubernetes-service-discovery---part-1)
* [medium: 5 tips for troubleshooting apps on Kubernetes](https://medium.com/@alexellisuk/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)
* [medium.com: Kubernetes Tip: How To Disambiguate A Pod Crash To Application Or To Kubernetes Platform? (CrashLoopBackOff)](https://medium.com/tailwinds-navigator/kubernetes-tip-how-to-disambiguate-a-pod-crash-to-application-or-to-kubernetes-platform-f6c1395a8d09)
* [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating/)
* [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes/)
* [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples/)
* [levelup.gitconnected.com: 5 tips for troubleshooting apps on Kubernetes](https://levelup.gitconnected.com/5-tips-for-troubleshooting-apps-on-kubernetes-835b6b539c24)
* [medium: Common Kubernetes Errors Made by Beginners [2021] 🌟](https://medium.com/nerd-for-tech/common-kubernetes-errors-made-by-beginners-274b50e18a01)
* [cloud.redhat.com: Troubleshooting Sandboxed Containers Operator](https://cloud.redhat.com/blog/sandboxed-containers-operator-from-zero-to-hero-the-hard-way-part-2)
* [komodor.com: Kubernetes Troubleshooting: The Complete Guide](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/)
* [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes/)
* [kinvolk.io: Investigating Kubernetes performance issues with BPF](https://kinvolk.io/blog/2020/04/inside-kinvolk-labs-investigating-kubernetes-performance-issues-with-bpf/)
* [medium: Better Debugging Environment for your Micro-Services](https://medium.com/@moshe.beladev.mb/better-debugging-environment-for-your-micro-services-9420a71b8a37)
* [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot/)
* [youtube: 3 Ways to Detect Evil "Latest" Image Tags in Kubernetes - Kubevious](https://www.youtube.com/watch?v=93RlMqO4glM&t=6s&ab_channel=Kubevious) The "latest" image tag is a disaster waiting to happen. In this video, you will learn how to detect usage of the latest images using 3 different methods.
* [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands/)
* [dzone.com: The Three Pillars of Kubernetes Troubleshooting 🌟](https://dzone.com/articles/the-three-pillars-of-kubernetes-troubleshooting) Diving into how the three pillars of understanding, managing and preventing for Kubernetes troubleshooting, and how it helps to conceive of what’s needed to be able to properly troubleshoot real-world Kubernetes stacks that are the hallmark of complex, distributed systems.
* [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting/)
* [==itnext.io: Distroless Container Debugging on K8s/OpenShift==](https://itnext.io/distroless-container-debugging-on-k8s-openshift-e418fd66fdad)
    * When people focusing more on the security of containers, distroless based images are frequently used to reduce the attack surface. In these images, the package manager, the non-dependent modules or libraries, even the shells are stripped off, only the app and its required dependencies are kept. For the statically linked executable, produced by golang for example, we can even use “scratch” as the base.
    * The potential exploit of vulnerability is therefore greatly reduced. But, on the other hand, it is difficult to troubleshoot the application if even the shell is not available, leaving only the logs from the app.
    * In this paper, we will explore different options to facilitate debugging by bringing back the shell.
* [==containiq.com: Kubernetes Events: In-Depth Guide & Examples== 🌟](https://www.containiq.com/post/kubernetes-events) Kubernetes events help you understand how Kubernetes resource decisions are made and they can be helpful for debugging. Learn more about k8s events in this in-depth guide.
* [==speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps==](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)
* [containiq.com: Debugging Your Kubernetes Nodes in the ‘Not Ready’ State | nodenotready](https://www.containiq.com/post/debugging-kubernetes-nodes-in-not-ready-state) Kubernetes clusters typically run on multiple “nodes” each having its own state. In this article, you’ll learn a few possible reasons a node might enter the **NotReady** state and how you can debug it.
* [containiq.com: Troubleshooting Kubernetes FailedAttachVolume and FailedMount](https://www.containiq.com/post/fixing-kubernetes-failedattachvolume-and-failedmount) When working with Persistent Volumes in Kubernetes, you might run into the FailedAttachVolume or FailedMount error. In this tutorial, we’ll show you how to troubleshoot these errors and find the root cause and fix them.
* [==containiq.com: Kubernetes ImagePullBackOff: Troubleshooting With Examples==](https://www.containiq.com/post/kubernetes-imagepullbackoff) If you’ve worked with Kubernetes for a while, chances are good that you have experienced the **ImagePullBackOff** status. This issue can be frustrating if you are unfamiliar with it, so in this guide, you will walk the reader through how to troubleshoot this issue, what some common causes are, and where to start if they encounter this problem.
* [medium.com/@andrewachraf: Detect crashes in your Kubernetes cluster using kwatch and Slack 🌟](https://medium.com/@andrewachraf/detect-crashes-in-your-cluster-using-kwatch-an-slack-84b979e93e03) Monitor all changes in your Kubernetes(K8s) cluster & detects crashes in your running apps in real time
* [==research.nccgroup.com: Detection Engineering for Kubernetes clusters==](https://research.nccgroup.com/2021/11/10/detection-engineering-for-kubernetes-clusters/) In this article you will learn how to detect anomalies in your cluster using Kubernetes Audit logs and Anomalies Detection Engineering.
* [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 1)](https://pauldally.medium.com/debugging-networkpolicy-part-1-249921cdba37)
    * [pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 2)](https://pauldally.medium.com/debugging-networkpolicy-part-2-2d5c42d8465c)
* [==medium.com/@tina168wong: Kubernetes Ingress and Services troubleshooting==](https://medium.com/@tina168wong/kubernetes-ingress-and-services-troubleshooting-e2bb01007175) In this article, you will find some useful tips for troubleshooting the traffic flow in your cluster: from the Ingress to your Pods.
* [medium.com/geekculture: Common Pod Errors in Kubernetes to Watch Out For](https://medium.com/geekculture/common-pod-errors-in-kubernetes-to-watch-out-for-d808737f4ade)
* [==faun.pub: Kubernetes — Debugging NetworkPolicy (Part 1)==](https://faun.pub/debugging-networkpolicy-part-1-249921cdba37) For something as important as NetworkPolicy, debugging is surprisingly painful. In this article you will learn a few practical tips on how to debug your network policies
    * [==pauldally.medium.com: Kubernetes — Debugging NetworkPolicy (Part 2)==](https://pauldally.medium.com/debugging-networkpolicy-part-2-2d5c42d8465c)
* [tratnayake.dev: Oncall Adventures - When your Prometheus-Server mounted to GCE Persistent Disk on K8s is Full](https://tratnayake.dev/oncall-adventures-prometheus-filled-disk) In this article, you will follow Thilina's journey on debugging a failing Prometheus server on Kubernetes. The story starts with a wake-up call at 3.30 am 😅
* [==sysdig.com: Understanding Kubernetes pod pending problems==](https://sysdig.com/blog/kubernetes-pod-pending-problems/)

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
- [==thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads== 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads/)
- [==levelup.gitconnected.com: De-Mystifying Kubernetes Debugging==](https://levelup.gitconnected.com/de-mystifying-kubernetes-debugging-de9e1c82ac3e) __How to debug your microservice in VS Code with Bridge to Kubernetes__
- [==opensource.googleblog.com: Introducing Ephemeral Containers==](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html) **Ephemeral containers are a new type of container that are part of the Kubernetes core API. An Ephemeral Container may be added to an existing Pod for administrative actions like debugging, it runs until it exits, and it won't be restarted. An ephemeral container runs within the Pod's existing resource allocation and shares common container namespaces.**
- [linkedin.com: Kubernetes Ephemeral Containers | Bibin Wilson](https://www.linkedin.com/pulse/kubernetes-ephemeral-containers-bibin-wilson/) Ephemeral Containers is one of the k8s beta features. The following command will add the debug-image container to the running frontend pod and take an exec session for debugging: ```kubectl debug -it pods/frontend --image=debug-image```
- [sumanthkumarc.medium.com: Debugging namespace deletion issue in Kubernetes](https://sumanthkumarc.medium.com/debugging-namespace-deletion-issue-in-kubernetes-f6f8b40a4368)

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
    </center>