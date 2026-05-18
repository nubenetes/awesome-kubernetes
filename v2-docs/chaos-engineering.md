# Chaos Engineering

!!! info "Architectural Context"
    Detailed reference for Chaos Engineering in the context of Platform & Site Reliability.

## Table of Contents

---

  - [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pingcap.com: chaos-mesh-action: Integrate Chaos Engineering into Your CI](https://www.pingcap.com/blog/chaos-mesh-action-integrate-chaos-engineering-into-your-ci)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Introduction to Kraken, a Chaos Tool for OpenShift/Kubernetes](https://www.redhat.com/en/blog/introduction-to-kraken-a-chaos-tool-for-openshift/kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.flant.com: Open Source solutions for chaos engineering in Kubernetes](https://palark.com/blog/chaos-engineering-in-kubernetes-open-source-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.palark.com: Attaining harmony of chaos in Kubernetes with Chaos Mesh](https://palark.com/blog/chaos-mesh-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Azure Chaos Studio](https://azure.microsoft.com/en-us/products/chaos-studio/#overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Awesome Chaos Engineering](https://github.com/dastergon/awesome-chaos-engineering)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Chaos Engineering Is Not Just for Ops](https://thenewstack.io/chaos-engineering-is-not-just-for-ops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Why Chaos Engineering Isn’t Just for Operations](https://thenewstack.io/why-chaos-engineering-isnt-just-for-operations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opsmx.com: What is Chaos Engineering?](https://www.opsmx.com/blog/what-is-chaos-engineering)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.amazon.com: Verify the resilience of your workloads using Chaos Engineering](https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [GitHub: kube-monkey](https://github.com/asobti/kube-monkey)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Litmus Chaos is a toolset to do chaos engineering in a kubernetes native way. Litmus provides chaos CRDs for Cloud-Native developers and SREs to inject, orchestrate and monitor chaos to find weaknesses in Kubernetes deployments](https://github.com/litmuschaos/litmus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Using Chaos Engineering to Improve the Resilience of Stateful Applications on Kubernetes](https://thenewstack.io/using-chaos-engineering-to-improve-the-resilience-of-stateful-applications-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Chaos Engineering on Kubernetes : Chaos Mesh Generally Available with v1.0](https://www.infoq.com/news/2020/10/kubernetes-chaos-mesh-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [chaos-mesh.org: Chaos Mesh 1.0: Chaos Engineering on Kubernetes Made Easier](https://chaos-mesh.org/blog/chaos-mesh-1.0-chaos-engineering-on-kubernetes-made-easier)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Develop a Daily Reporting System for Chaos Mesh to Improve System Resilience](https://thenewstack.io/develop-a-daily-reporting-system-for-chaos-mesh-to-improve-system-resilience)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Chaos Engineering Progressively Moves to Production](https://thenewstack.io/chaos-engineering-progressively-moves-to-production)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [PowerfulSeal](https://github.com/powerfulseal/powerfulseal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [BuggyApp: Simulate performance problems](https://buggyapp.ycrash.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Chaos Mesh 🌟](https://chaos-mesh.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: 5 lessons I learned about chaos engineering for Kubernetes](https://opensource.com/article/21/10/chaos-engineering-kubernetes-ebook)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Chaos Engineering Made Simple](https://thenewstack.io/chaos-engineering-made-simple)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Use Chaos Engineering to Strengthen Your Incident Response](https://thenewstack.io/use-chaos-engineering-to-strengthen-your-incident-response)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Operationalizing Chaos Engineering with GitOps](https://thenewstack.io/operationalizing-chaos-engineering-with-gitops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.amazon.com: Chaos Engineering with LitmusChaos on Amazon EKS](https://aws.amazon.com/blogs/containers/chaos-engineering-with-litmuschaos-on-amazon-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.container-solutions.com: Comparing Chaos Engineering Tools for Kubernetes Workloads](https://blog.container-solutions.com/comparing-chaos-engineering-tools)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Breaking Serverless on Purpose with Chaos Engineering](https://thenewstack.io/breaking-serverless-on-purpose-with-chaos-engineering)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [chaosblade](https://github.com/chaosblade-io/chaosblade)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.amazon.com: Automating and Scaling Chaos Engineering using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/industries/automating-and-scaling-chaos-engineering-using-aws-fault-injection-simulator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
