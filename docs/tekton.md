# Tekton and Tekton Pipelines

1. [Introduction](#introduction)
2. [Videos](#videos)
3. [Slides](#slides)

## Introduction

- [==tekton.dev==](https://tekton.dev/)
- [github.com/tektoncd](https://github.com/tektoncd/)
- [Tekton community](https://github.com/tektoncd/community)
- [github: Tekton Pipelines](https://github.com/tektoncd/pipeline)
- [Tekton Pipelines Docs](https://tekton.dev/docs/pipelines/pipelines/)
- [opensource.googleblog.com: The Tekton Pipelines Beta release](https://opensource.googleblog.com/2020/05/the-tekton-pipelines-beta-release.html)
- [tekline 🌟](https://github.com/joyrex2001/tekline) tekline is a tekton delegated-pipeline to enable a bring-your-own pipeline configuration.
- [Tekton PetClinic Demo Youtube](https://www.youtube.com/watch?v=igwFpZOUTnw)
- [OpenShift Tekton pipelines](https://www.openshift.com/learn/topics/pipelines)
- [blog.openshift.com: cloud native CI/CD with openshift pipelines](https://blog.openshift.com/cloud-native-ci-cd-with-openshift-pipelines/)
- [Easily reuse Tekton and Jenkins X from Jenkins](https://www.jenkins.io/blog/2021/04/21/tekton-plugin/)
    - We started with Jenkins shared libs, and wrote common implementation for one group of engineering teams. This worked very well because not only were we able to consolidate and refactor all pipelines at once leading to several optimizations, it also made it easy to understand the CI implementation for all similar services and if we were to add common features and bug fixes it was really easy to push it through a common implementation.
    - There were benefits of doing this, but what was not desirable is that it took us a lot of effort to build these shared libs and despite our efforts to keep them simple, they ended up looking very complicated. Standard pipeline specs had departed from being declarative in nature and there was a lot of imperative Groovy logic mixed with Pipeline DSL.
- [==opensource.com: Write your first CI/CD pipeline in Kubernetes with Tekton== 🌟](https://opensource.com/article/21/11/cicd-pipeline-kubernetes-tekton) Tekton is a Kubernetes-native open source framework for creating continuous integration and continuous delivery (CI/CD) systems.
- [opensource.com: Dynamic scheduling of Tekton workloads using Triggers](https://opensource.com/article/21/11/kubernetes-dynamic-scheduling-tekton) Upgrade your CI/CD pipeline with this Kubernetes-native application. Tekton Triggers is a Tekton component that allows you to detect and extract information from events from various sources and execute TaskRuns and PipelineRuns based on that information. It also enables passing extracted information to TaskRuns and PipelineRuns from events.
- [==piotrminkowski.com: Validate Kubernetes Deployment in CI/CD with Tekton and Datree==](https://piotrminkowski.com/2022/02/21/validate-kubernetes-deployment-in-ci-cd-with-tekton-and-datree)
- [==piotrminkowski.com: Canary Release on Kubernetes with Knative and Tekton==](https://piotrminkowski.com/2022/03/29/canary-release-on-kubernetes-with-knative-and-tekton/)

## Videos

<details>
  <summary>Click to expand!</summary>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7mvrpxz_BfE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZOXPWPt8Iiw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/CnVCgMRE4xI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Slides

<details>
  <summary>Click to expand!</summary>

<center>
<script async class="speakerdeck-embed" data-id="d3d70ab67e894e74912beb835e927d10" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

<script async class="speakerdeck-embed" data-id="63bd2b3c53d748b0be8e2f91ac3e6870" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>
</details>