---
description: "Top Kubernetes Troubleshooting resources for 2026, AI-ranked: Awesome Chaos Engineering, kubectl-debug and more — curated Cloud Native tools, guides and references."
---
# Kubernetes Troubleshooting

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-troubleshooting/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Troubleshooting in the context of The Container Stack.

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status' “Terminating”](https://veducate.co.uk/kubernetes-pvc-terminating)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering veducate.co.uk: How to fix in Kubernetes – Deleting a PVC stuck in status' “Terminating” in the Kubernetes Tools ecosystem.
  - [dzone.com: Tackling the Top 5 Kubernetes Debugging Challenges](https://dzone.com/articles/tackling-the-top-5-kubernetes-debugging-challenges)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==dzone.com: Tackling the Top 5 Kubernetes Debugging Challenges== in the Kubernetes Tools ecosystem.
  - [Kubernetes Troubleshooting: A Step-by-Step Guide](https://www.cncf.io/blog/2025/03/13/kubernetes-troubleshooting-a-step-by-step-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Kubernetes Troubleshooting: A Step-by-Step Guide in the Kubernetes Tools ecosystem.
  - [How to quarantine pods](https://www.reddit.com/r/kubernetes/comments/gt3uvg/how_to_quarantine_pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering How to quarantine pods in the Kubernetes Tools ecosystem.
## Architecture

### Pod Lifecycle

#### Ephemeral Containers

  - **(2023)** [linkedin.com: Kubernetes Ephemeral Containers | Bibin Wilson](https://www.linkedin.com/pulse/kubernetes-ephemeral-containers-bibin-wilson)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical implementation breakdown demonstrating how engineers can leverage kubectl debug to attach ephemeral containers to scratch or distroless pods. Provides real-world configuration examples and use cases.
  - **(2023)** [iximiuz.com: Kubernetes Ephemeral Containers and kubectl debug Command 🌟](https://iximiuz.com/en/posts/kubernetes-ephemeral-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive deep-dive into the architectural mechanics of kubectl debug and ephemeral containers. Explains container namespaces sharing, security contexts, and step-by-step diagnostic workflows on live clusters.
  - **(2022)** [opensource.googleblog.com: Introducing Ephemeral Containers](https://opensource.googleblog.com/2022/01/Introducing%20Ephemeral%20Containers.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The foundational announcement from Google detailing the integration of ephemeral containers in Kubernetes. Outlines the architectural mechanics of injecting debugging tooling directly into running distroless or minimal containers via the API.
## Chaos Engineering

### Curated Playbooks

#### Awesome Lists

  - **(2023)** [==Awesome Chaos Engineering==](https://github.com/dastergon/awesome-chaos-engineering) <span class='md-tag md-tag--info'>⭐ 6589</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-65c32571" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 4 L 20 5 L 30 11 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-65c32571)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier curated directory of resources, tools, and papers dedicated to the practice of Chaos Engineering. It indexes tools for simulating network latency, injecting resource stress, and terminating instances across various platforms, with a strong focus on cloud-native environments. This is a must-have reference for engineering teams building self-healing, fault-tolerant distributed systems.
## Cloud Infrastructure

### Infrastructure As Code

#### Migration Strategies

  - **(2026)** [The Definitive Guide to Importing Your Cloud Resources into IaC](https://blog.cloudgeni.ai/the-definitive-guide-to-importing-your-cloud-resources-into-iac) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed technical review addressing drift reconciliation when converting untracked click-ops clouds into declarative state files. Reviews native state import commands and toolkits that automate resource generation.
## Cloud-native Platforms

### Operating Systems

#### Flatcar Linux

  - **(2024)** [kinvolk.io](https://kinvolk.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official portal of Kinvolk (acquired by Microsoft), pioneers of Flatcar Container Linux, Lokomotive Kubernetes, and Inspektor Gadget. The platform represents an essential pillar in the development of minimal, immutable operating systems and eBPF-based Kubernetes tooling.
## Container Runtimes

### Containerd

#### Ctr CLI

  - **(2023)** [labs.iximiuz.com: How to work with container images using ctr](https://labs.iximiuz.com/courses/containerd-cli/ctr/image-management) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep technical laboratory exercise focused on managing low-level container images using the containerd 'ctr' CLI. Vital for operations engineers debugging nodes directly where high-level runtimes like docker are not installed.
## Development Workflow

### Local Development

#### Bridge To Kubernetes

  - **(2021)** [thorsten-hans.com: Debugging apps in Kubernetes with Bridge](https://www.thorsten-hans.com/debugging-apps-in-kubernetes-with-bridge)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Hands-on guide focusing on Microsoft's 'Bridge to Kubernetes' tool for direct local debugging within an active cluster context. Evaluates how the mechanism redirects traffic to a local machine without modifying production routing topologies.
## Infrastructure

### Cluster Management

#### RKE2

  - **(2024)** [RKE2 Standalone Disaster Recovery Guide](https://support.tools/post/rke2-standalone-disaster-recovery) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Critical disaster recovery operational manual targeting RKE2 standalone clusters. Focuses on backup restoration, etcd snapshot recovery, and certificate rotation when cluster management planes fail.
### Compute

#### CPU Performance

  - **(2023)** [The Hidden CPU Throttling Crisis in Kubernetes Clusters](https://www.kubenatives.com/p/the-hidden-cpu-throttling-crisis) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates latency spikes caused by the Linux CFS (Completely Fair Scheduler) quota enforcement mechanism in Kubernetes. Highlights how kernel bugs throttle containerized workloads even when usage is far below limits, providing remediation strategies such as adjusting quotas or using CPU pins.
## Kubernetes

### Core Mechanics

#### Pod Lifecycle (1)

  - **(2020)** [erkanerol.github.io: I wish pods were fully restartable](https://erkanerol.github.io/post/restartable-pods) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This reflective post explores the architectural limitations of the Kubernetes Pod lifecycle, specifically the inability to easily restart individual containers without recreating the entire Pod. It analyzes proposed community designs and current workarounds, such as mutating controllers or rollout restarts. It provides deep architectural insights into the design decisions governing Kubernetes resource controllers.
### Data Management

#### Backup

  - **(2021)** [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Ensuring disaster recovery capability in Kubernetes requires robust backup strategies for both cluster state (etcd) and persistent volume data. This reference highlights best practices including scheduling automated snapshot intervals, isolating backup storage, and regularly testing recovery procedures. Adhering to these patterns safeguards enterprise workloads against data corruption and ransomware.
#### Checkpointing API

  - **(2022)** [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing API](https://martinheinz.dev/blog/85) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — The Kubernetes Checkpointing API introduces the revolutionary ability to freeze and snapshot a running container's state to disk for backup or migration purposes. This technical analysis demonstrates how to leverage this API to capture memory-level states, enabling ultra-fast recovery and deep forensics of active workloads. However, as of 2026, this feature remains highly experimental and runtime-dependent.
### Networking

#### Ingress Troubleshooting

  - **(2019)** [managedkube.com: Troubleshooting a Kubernetes ingress](https://managedkube.com/kubernetes/trace/ingress/service/port/not/matching/pod/k8sbot/2019/02/13/trace-ingress.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubernetes Ingress troubleshooting requires systematically tracing path matching, port definitions, and target service selectors. This guide isolates a common failure pattern where configuration mismatches between Ingress specifications and Pod ports disrupt traffic flow. It provides actionable diagnostic commands to verify endpoint connectivity and route mapping.
### Observability

#### Events

  - **(2023)** [groundcover.com: Failure Is an Option: How to Stay on Top of K8s Container Events](https://www.groundcover.com/blog/k8s-container-events)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubernetes events are transient cluster logs that provide critical context for system state changes and errors, but their short lifespan makes persistent logging essential. This article analyzes strategies for collecting, storing, and visualizing container events to catch intermittent failures. Utilizing event streaming helps platform engineers build early-warning systems before issues escalate to outages.
#### Events Logging

  - **(2022)** [decisivedevops.com: Kubernetes Events — News feed of your cluster](https://decisivedevops.com/kubernetes-events-news-feed-of-your-kubernetes-cluster-826e08892d7a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This guide explains the utility of Kubernetes events as a real-time diagnostic feed of cluster activities. It demonstrates how to capture, filter, and stream these resource events to external observability backends using open-source collectors. Properly configured event logging ensures that platform teams maintain a historical record of pod crashes and scheduling failures.
### Resource Management

#### CPU Scheduling

  - **(2021)** [andydote.co.uk: The Problem with CPUs and Kubernetes](https://andydote.co.uk/2021/06/02/os-cpus-and-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A low-level analysis of how the Linux kernel scheduler interacting with CFS quota limits can severely throttle Kubernetes pods, even when total CPU utilization is low. The author exposes the architectural friction between container resource limits and multi-threaded application runtimes like Java and Go. Platform engineers will find valuable tuning techniques to mitigate silent latency spikes caused by CPU throttling.
#### CPU Throttling

  - **(2024)** [CPU Limits in Kubernetes: Deep Dive into Pod Throttling and Kernel Interactions](https://www.linkedin.com/pulse/cpu-limits-kubernetes-why-your-pod-idle-still-deep-dive-lazarev-k3m7f) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exceptionally detailed deep dive into kernel interactions, Linux control groups (cgroups), and the Completely Fair Scheduler (CFS) quota mechanism inside Kubernetes. It demystifies why pods experience severe throttling even when aggregate CPU metrics appear healthy, analyzing the impact of short-duration burst workloads. It provides essential mathematical formulas and kernel parameters to fine-tune pod limits safely.
#### Metrics Collection

  - **(2023)** [learnitguide.net: How to Check Memory Usage of a Pod in Kubernetes?](https://www.learnitguide.net/2023/04/how-to-check-memory-usage-of-pod-in.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Monitoring memory consumption is critical to preventing out-of-memory (OOM) evictions and performance degradation. This guide explains how to leverage the Kubernetes Metrics Server via kubectl top, alongside advanced Prometheus queries, to track real-time memory footprints. It contrasts raw memory utilization against requested resource boundaries to help right-size workloads.
#### OOM and Throttling

  - **(2021)** [sysdig.com: Kubernetes OOM and CPU Throttling](https://www.sysdig.com/blog/troubleshoot-kubernetes-oom)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly analytical post from Sysdig comparing the operational impacts of memory exhaustion (OOM) versus CPU exhaustion (Throttling). While OOM errors lead to sudden container termination and service disruption, CPU throttling leads to slow response times and latency degradation. The guide explains how to monitor these metrics to balance cluster cost against application performance.
#### Qos and OOM Score

  - **(2020)** [cloudyuga.guru: How does Kubernetes assign QoS class to pods through OOM score?](https://cloudyuga.guru/blogs/k8s-qos-oomkilled) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This article provides a rigorous, technical exploration of how Kubernetes maps container memory/CPU requests and limits to Quality of Service (QoS) classes: Guaranteed, Burstable, and BestEffort. It details how the orchestrator translates these classes into Linux OOM scores, which the kernel uses to select victim processes during memory pressure. Mastering this mapping is vital for designing reliable, high-density cluster workloads.
### Runtime Security

#### Sandboxed Containers

  - **(2022)** [cloud.redhat.com: Troubleshooting Sandboxed Containers Operator](https://www.redhat.com/en/blog/sandboxed-containers-operator-from-zero-to-hero-the-hard-way-part-2) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deploying secure, isolated runtimes within Kubernetes demands deep knowledge of sandboxed container configurations, such as Kata Containers. This guide explores troubleshooting the Sandboxed Containers Operator on OpenShift, focusing on kernel module loading and hardware virtualization flags. It is an indispensable resource for platform engineers managing untrusted multi-tenant workloads.
### Security

#### Container Images

  - **(2020)** [youtube: 3 Ways to Detect Evil "Latest" Image Tags in Kubernetes - Kubevious](https://www.youtube.com/watch?v=93RlMqO4glM&ab_channel=Kubevious)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Using the 'latest' container image tag in production is a critical antipattern that breaks deployment reproducibility and introduces security risks. This guide uses Kubevious to outline three automated detection techniques to intercept and block these non-deterministic tags in deployment pipelines. It emphasizes implementing admission controllers to enforce strict version tagging.
### Troubleshooting

#### Architectural Slides

  - **(2019)** [speakerdeck.com/mhausenblas (redhat): Troubleshooting Kubernetes apps](https://speakerdeck.com/mhausenblas/kubecologne-keynote-troubleshooting-kubernetes-apps)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This presentation slide deck by Michael Hausenblas maps out the complete lifecycle of Kubernetes application troubleshooting, from log collection to packet analysis. It offers a structured classification of failure domains, targeting scheduling, networking, and application-level errors. Highly recommended for visual learners seeking a comprehensive overview of cloud-native debugging patterns.
#### Case Study

  - **(2021)** [thenewstack.io: What David Flanagan Learned Fixing Kubernetes Clusters](https://thenewstack.io/what-david-flanagan-learned-fixing-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This synthesis highlights critical real-world lessons from fixing broken Kubernetes clusters under pressure, illustrating how misconfigurations lead to spectacular outages. It emphasizes that basic oversights in DNS configuration, RBAC permissions, and resource constraints cause the majority of cluster-wide failures. This post-mortem review serves as a warning and a guide to preventative cluster maintenance.
#### Command Line

  - **(2021)** [thenewstack.io: Living with Kubernetes: Debug Clusters in 8 Commands 🌟](https://thenewstack.io/living-with-kubernetes-debug-clusters-in-8-commands)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly practical command-line cheat sheet that isolates eight crucial kubectl commands for diagnosing cluster and application failures. By leveraging advanced output formatting and resource filtering, engineers can quickly drill down from high-level service failures to underlying node exhaustion. This primer is designed for rapid incident response and system validation.
#### Crashloopbackoff

  - **(2023)** [devtron.ai: Troubleshoot: Pod Crashloopbackoff](https://devtron.ai/blog/troubleshoot_crashloopbackoff_pod)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A targeted diagnostic manual focusing exclusively on resolving Pod CrashLoopBackOff errors within a Kubernetes cluster. It details the precise troubleshooting path, examining application configuration errors, environment variable omissions, and permission issues. It also includes strategies for extracting logs from previously terminated container instances.
  - **(2022)** [komodor.com: Kubernetes CrashLoopBackOff Error: What It Is and How to Fix It](https://komodor.com/learn/how-to-fix-crashloopbackoff-kubernetes-error)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive playbook from Komodor designed to help engineers systematically isolate the root causes of CrashLoopBackOff errors. It covers common trigger events such as database connection timeouts, file access permissions, and mismatched configuration maps. By mapping these triggers, it helps engineers transition from reactive troubleshooting to proactive reliability planning.
  - **(2021)** [sysdig.com: What is Kubernetes CrashLoopBackOff? And how to fix it 🌟](https://www.sysdig.com/blog/debug-kubernetes-crashloopbackoff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A definitive guide from Sysdig addressing the causes, mechanics, and remediation steps for the ubiquitous CrashLoopBackOff state. The article unpacks how the kubelet manages backoff loops when an application continuously crashes on startup. It outlines diagnostic strategies combining container telemetry with log output to pinpoint runtime exceptions.
#### Developer Enablement

  - **(2021)** [thenewstack.io: 6 Kubernetes Best Practices to Empower Devs to Troubleshoot](https://thenewstack.io/6-kubernetes-best-practices-to-empower-devs-to-troubleshoot)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — DevOps maturity relies on empowering application developers to diagnose and resolve their own Kubernetes errors without administrative intervention. By providing accessible log aggregation, standardized event alerts, and ephemeral debugging shells, platform teams can eliminate operational bottlenecks. This framework details how to design developer-friendly observability environments.
#### Development Environments

  - **(2023)** [devzero.io: Kubernetes Debugging Tips](https://www.devzero.io/blog/kubernetes-autoscaling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Optimizing the inner-loop developer experience in Kubernetes requires special tooling to bypass slow build-and-deploy cycles. This guide reviews practical tips for configuring local debugging environments, port forwarding, and syncing code directly into remote dev clusters. Implementing these techniques allows developers to debug code in real time within a cluster-like context.
#### Diagnostic Manuals

  - **(2022)** [==github.com/metaleapca: metaleap-k8s-troubleshooting.pdf==](https://github.com/metaleapca/metaleap-k8s-troubleshooting/blob/main/metaleap-k8s-troubleshooting.pdf) <span class='md-tag md-tag--info'>⭐ 40</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bcd615ec" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 13 L 20 5 L 30 5 L 40 8 L 50 6" fill="none" stroke="url(#spark-grad-bcd615ec)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An exhaustive community-driven reference PDF that serves as a diagnostic field manual for complex Kubernetes cluster issues. It covers everything from low-level CNI networking issues to control plane degradation and API server latency. This document is a valuable offline resource for operations teams handling large-scale production incidents.
#### Ephemeral Containers (1)

  - **(2022)** [loft.sh: Using Kubernetes Ephemeral Containers for Troubleshooting](https://www.vcluster.com/blog/using-kubernetes-ephemeral-containers-for-troubleshooting) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This guide explains how to leverage Kubernetes Ephemeral Containers—the native, standard way to troubleshoot running pods without pre-packaging debug tools in production images. By launching a temporary diagnostic container within the target pod's namespace, engineers can safely run tools like curl, tcpdump, or strace. This represents the modern, secure gold standard for debugging production distroless containers.
#### Exit Codes

  - **(2022)** [komodor.com: Exit Codes In Containers & Kubernetes – The Complete Guide  🌟](https://komodor.com/learn/exit-codes-in-containers-and-kubernetes-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry-standard reference guide demystifying exit codes returned by failing containers, from common application errors (Exit Code 1) to system-level kills (Exit Code 137). It details how the container runtime and Linux kernel interact to generate these codes, providing a crucial diagnostic map for troubleshooting CrashLoopBackOffs. Understanding these codes is essential for automated root-cause analysis.
#### Fundamentals

  - **(2021)** [thenewstack.io: Kubernetes Troubleshooting Primer](https://thenewstack.io/kubernetes-troubleshooting-primer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational text that introduces the core mechanics of the Kubernetes control plane and how components interact during deployment failures. It explains the relationship between the API server, controller manager, scheduler, and kubelet, illustrating where common failures arise. This primer establishes the necessary context for executing advanced diagnostics.
#### General Guide

  - **(2021)** [blog.alexellis.io: How to Troubleshoot Applications on Kubernetes 🌟](https://blog.alexellis.io/troubleshooting-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A classic, hands-on troubleshooting guide tailored for engineers deploying applications to Kubernetes clusters. It provides a logical flow of commands from checking container logs and inspecting events to executing commands inside a container. This resource is excellent for developing the primary instincts required to resolve containerized application failures.
#### Guides

  - **(2023)** [Kubernetes Troubleshooting Guide: Common Pitfalls and Solutions](https://autodotes.com/posts/s90PP9397WYTsAWaRapd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A robust troubleshooting guide compiling common pitfalls, anti-patterns, and direct remedies for everyday Kubernetes operation. It spans topics from service networking misconfigurations to persistent volume mounting failures. This resource provides clear checklists to help platform engineers accelerate incident resolution times.
#### Methodologies

  - **(2022)** [freecodecamp.org: How to Simplify Kubernetes Troubleshooting](https://www.freecodecamp.org/news/how-to-simplify-kubernetes-troubleshooting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This comprehensive troubleshooting guide reframes cluster diagnostics into a logical, step-by-step methodology rather than chaotic guesswork. It focuses on isolating issues systematically across the application layer, the container runtime, and the underlying orchestrator networking. Utilizing this structured approach significantly lowers the cognitive load of on-call engineers.
#### Playbooks

  - **(2023)** [10 Real-World Kubernetes Troubleshooting Scenarios and Solutions](https://livingdevops.com/devops/10-real-world-kubernetes-troubleshooting-scenarios-and-solutions)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This compilation details ten authentic, highly technical outage scenarios encountered in production Kubernetes clusters, complete with step-by-step diagnostic paths and resolutions. It covers complex issues like DNS resolution failure, certificate expiration, and stateful volume mounting locks. The practical nature of these scenarios makes this an invaluable resource for active operations teams.
#### Pod Diagnostics

  - **(2023)** [learnitguide.net: How To Troubleshoot Kubernetes Pods](https://www.learnitguide.net/2023/04/how-to-troubleshoot-kubernetes-pods.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A focused tutorial describing standard commands and methodologies to diagnose Pod failures such as ImagePullBackOff, CrashLoopBackOff, and Evicted states. It systematically walks through the utilization of kubectl describe, logs, and events to construct an accurate failure timeline. It is perfect for junior engineers looking to build baseline debugging proficiency.
#### Pod Eviction

  - **(2021)** [sysdig.com: Understanding Kubernetes Evicted Pods](https://www.sysdig.com/blog/kubernetes-pod-evicted)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pod eviction is a proactive defense mechanism executed by the kubelet when a node faces critical resource pressure, such as low disk space or memory exhaustion. This guide details the eviction lifecycle, explaining the difference between soft and hard eviction thresholds. It provides practical strategies for configuring tolerations and cluster autoscaling to prevent widespread application downtime.
#### Pod Scheduling

  - **(2021)** [sysdig.com: Understanding Kubernetes pod pending problems](https://www.sysdig.com/blog/kubernetes-pod-pending-problems)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pods trapped in a 'Pending' state point directly to scheduling failures caused by resource exhaustion, node selectors, or volume binding delays. This deep dive from Sysdig explains how to read scheduler events and analyze resource request limits to unlock stuck deployments. Engineers will learn how to identify node-affinity conflicts and taint/toleration mismatches.
#### Real-world Examples

  - **(2022)** [tennexas.com: Kubernetes Troubleshooting Examples](https://tennexas.com/kubernetes-troubleshooting-examples)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An essential compilation of practical Kubernetes troubleshooting scenarios focusing on common network, storage, and configuration failures. It provides hands-on diagnostic scripts and commands to dissect failing pods and unresolvable services. This playbook bridges the gap between theoretical knowledge and day-to-day cluster administration.
### Troubleshooting Tooling

#### Kubectl Plugins

  - **(2020)** [==kubectl-debug==](https://github.com/aylei/kubectl-debug) <span class='md-tag md-tag--info'>⭐ 2305</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3ce999e8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 6 L 20 4 L 30 9 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-3ce999e8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Originally a popular community-built plugin to launch debugging containers within target pods, `kubectl-debug` has largely been superseded by native Kubernetes Ephemeral Containers (`kubectl debug` command) in modern releases. This project remains a valuable reference for historical context and legacy cluster compatibility. For modern clusters, engineers are strongly advised to transition to built-in Kubernetes diagnostic commands.
## Kubernetes Developer Experience

### Inner-loop Automation

#### Guides (1)

  - **(2021)** [rookout.com: Developer Tools for Kubernetes in 2021: Helm, Kustomize, and Skaffold (Part 1)](https://www.dynatrace.com/solutions/observability-for-developers) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive multi-part review of critical Kubernetes development tools. Examines deployment mechanisms (Helm, Kustomize), real-time sync engines (Skaffold, Tilt, Garden), IDE extensions, and container building alternatives.
## Kubernetes Platform Engine

### Cluster Operations

#### Memory Management

  - **(2025)** [OOMKilled in Kubernetes: Understanding and Preventing Hidden Memory Leaks](https://unixarena.com/2025/04/oomkilled-in-kubernetes-the-hidden-memory-leaks-youre-missing.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Diagnoses Kubernetes `OOMKilled` (Exit Code 137) events caused by memory leaks, misconfigured resource limits, and JVM heap management issues. Explains how to set appropriate limits/requests while implementing profiling tools to prevent container churn.
## Observability (1)

### Debugging

#### Automation

  - **(2022)** [github.com/airwallex: k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An automated utility designed to capture and log state configuration, events, and logs instantly when a pod restarts, offering immediate post-mortem insights for ephemeral microservices.
#### CLI Extensions

  - **(2021)** [github.com/JamesTGrant/kubectl-debug](https://github.com/JamesTGrant/kubectl-debug) <span class='md-tag md-tag--info'>⭐ 373</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-582e5a31" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 9 L 20 13 L 30 7 L 40 11 L 50 12" fill="none" stroke="url(#spark-grad-582e5a31)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A kubectl plugin designed to launch temporary debugging containers within a target pod namespace. Streamlines manual container introspection prior to the widespread adoption of native ephemeral containers.
#### CLI Operations

  - **(2023)** [A Complete Guide to Kubectl exec](https://refine.dev/blog/kubectl-exec-command)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comprehensive guide explaining the inner workings of the 'kubectl exec' command. Breaks down how connection handshakes occur between the API server, Kubelet, and container runtimes (CRI).
  - **(2021)** [thenewstack.io: Living with Kubernetes: 12 Commands to Debug Your Workloads 🌟](https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curated list of 12 essential kubectl commands designed to streamline low-level container and network diagnostics. Targets common day-2 operational challenges, addressing resource pressure, storage attachments, and system event inspection.
#### Container Debugging

  - **(2025)** [iximiuz/cdebug](https://github.com/iximiuz/cdebug) <span class='md-tag md-tag--info'>⭐ 1652</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-55e54588" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 5 L 20 12 L 30 7 L 40 4 L 50 2" fill="none" stroke="url(#spark-grad-55e54588)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized CLI tool for debugging running containers. Allows attaching ephemeral tooling environments into running, stripped-down containers (even without Kubernetes, working directly with Docker/containerd).
  - **(2022)** [felipecruz91/debug-ctr](https://github.com/felipecruz91/debug-ctr) <span class='md-tag md-tag--info'>⭐ 52</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3ff64d25" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 4 L 20 5 L 30 11 L 40 7 L 50 9" fill="none" stroke="url(#spark-grad-3ff64d25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Lightweight helper utility targeting runtimes at the node level. Allows developers to run custom debug tools directly inside active containerd namespaces without impacting root node security models.
#### Containers

  - **(2023)** [KDBG: Small Kubernetes debugging container](https://github.com/nvucinic/kdbg) <span class='md-tag md-tag--info'>⭐ 36</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-9b83afe9" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 7 L 20 12 L 30 12 L 40 9 L 50 10" fill="none" stroke="url(#spark-grad-9b83afe9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight Kubernetes debugging container designed to simplify troubleshooting inside active pods. It packages key diagnostic tools (curl, dig, iproute2, etc.) for direct execution inside the cluster networking space, serving as an effective sidecar or ephemeral debugging agent.
#### Legacy Tooling

  - **(2021)** [palaemon.io](https://palaemon.io)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Legacy troubleshooting tool aimed at optimizing container workloads and analyzing scheduling configurations. Now largely archived but remains historically relevant for declarative scheduling architectures.
#### Pre-flight Checks

  - **(2025)** [github.com/replicatedhq/troubleshoot](https://github.com/replicatedhq/troubleshoot) <span class='md-tag md-tag--info'>⭐ 582</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8ad46e8a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 4 L 20 8 L 30 11 L 40 6 L 50 3" fill="none" stroke="url(#spark-grad-8ad46e8a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A framework providing preflight checks and support-bundle collection capabilities for Kubernetes applications. Crucial for enterprise environments deploying applications onto heterogeneous on-premises or customer-managed clusters.
#### Troubleshooting Guide

  - **(2023)** [learnk8s.io: A visual guide on troubleshooting Kubernetes deployments](https://learnkube.com/troubleshooting-deployments)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A high-density visual guide detailing a deterministic flowchart for troubleshooting Kubernetes deployment failures. It systematically walks engineers through checking ingress, service routing, selector matching, and pod-level failures (e.g., CrashLoopBackOff).
  - **(2023)** [komodor.com: Kubernetes Troubleshooting: The Complete Guide 🌟](https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An exhaustive architectural manual dissecting everyday Kubernetes failure patterns including OOMKilled, ImagePullBackOff, CrashLoopBackOff, and CPU throttling.
#### Workloads

  - **(2022)** [towardsdatascience.com: The Easiest Way to Debug Kubernetes Workloads](https://towardsdatascience.com/the-easiest-way-to-debug-kubernetes-workloads-ff2ff5e3cc75)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical overview detailing baseline approaches to troubleshooting Kubernetes workloads, focusing on common command-line routines. It bridges the gap for data engineers and developers needing rapid context on kubectl logs, describes, and port-forwards.
### Deployments

#### Telemetry

  - **(2021)** [StatusBay](https://github.com/similarweb/statusbay) <span class='md-tag md-tag--info'>⭐ 387</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0d1c06fc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 8 L 20 10 L 30 6 L 40 7 L 50 2" fill="none" stroke="url(#spark-grad-0d1c06fc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active deployment monitoring tool that provides real-time visibility into Kubernetes deployment sequences. By aggregating event logs and state transitions, StatusBay offers clean diagnostic traces for failed releases, improving post-mortem analysis.
### Networking (1)

#### API Traffic Analyzer

  - **(2024)** [kubetools.io: Kubeshark – API Traffic Analyzer for Kubernetes](https://kubetools.io/mastering-kubernetes-debugging-and-troubleshooting-with-kubeshark-real-time-visibility-query-language-service-map-and-integrations) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced network analyzer for Kubernetes (formerly API Tap) that captures and decrypts cluster traffic in real-time. Leverages modern eBPF and packet capture technologies to trace service-to-service communication.
### Troubleshooting Platforms

#### Enterprise Monitoring

  - **(2024)** [komodor.com](https://komodor.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Commercial troubleshooting and observability platform offering absolute end-to-end lineage visualization for Kubernetes resources. Pinpoints root causes of failures by cross-referencing changes, logs, and metrics.
### UI Clients

#### Multi-cluster

  - **(2024)** [KubeUI: A Desktop Kubernetes Client](https://github.com/IvanJosipovic/KubeUI) <span class='md-tag md-tag--info'>⭐ 311</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-723a78a4" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 6 L 20 11 L 30 7 L 40 10 L 50 8" fill="none" stroke="url(#spark-grad-723a78a4)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[C# CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-performance, desktop-optimized UI designed to stream, monitor, and interact with live cluster metrics and objects. It enhances developer agility through dynamic views of multi-cluster namespaces and active workload metrics.
## Security and Compliance

### CICD

#### Penetration Testing

  - **(2021)** [research.nccgroup.com: 10 real-world stories of how we’ve compromised CI/CD pipelines](https://www.nccgroup.com/research) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Case-study driven review from NCC Group outlining real-world exploits used to compromise continuous delivery channels. Common vectors include poorly protected secrets, dependency confusion attacks, and unauthenticated pipeline runners. This security research highlights the critical importance of runtime monitoring and pipeline isolation to prevent supply-chain compromises.

---
💡 **Explore Related:** [Kubernetes Storage](./kubernetes-storage.md) | [Docker](./docker.md) | [Kubernetes Releases](./kubernetes-releases.md)

🔗 **See Also:** [Cloud Asset Inventory](./cloud-asset-inventory.md) | [AWS Storage](./aws-storage.md)

