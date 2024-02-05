# Tekton and Tekton Pipelines

1. [Introduction](#introduction)
2. [Videos](#videos)
3. [Slides](#slides)

## Introduction

- [==tekton.dev==](https://tekton.dev/)
- [github.com/tektoncd](https://github.com/tektoncd/)
- [tekton.dev/try: Interactive Tutorials](https://tekton.dev/try/)
- [Tekton community](https://github.com/tektoncd/community)
- [github: Tekton Pipelines](https://github.com/tektoncd/pipeline)
- [Tekton Pipelines Docs](https://tekton.dev/docs/pipelines/pipelines/)
- [opensource.googleblog.com: The Tekton Pipelines Beta release](https://opensource.googleblog.com/2020/05/the-tekton-pipelines-beta-release.html)
- [tekline 🌟](https://github.com/joyrex2001/tekline) tekline is a tekton delegated-pipeline to enable a bring-your-own pipeline configuration.
- [Tekton PetClinic Demo](https://github.com/tektoncd/pipeline)
- [Tekton PetClinic Demo Youtube](https://www.youtube.com/watch?v=igwFpZOUTnw)
- [OpenShift Tekton pipelines](https://www.openshift.com/learn/topics/pipelines)
- [developers.redhat.com: An introduction to cloud native CI/CD with Red Hat OpenShift pipelines](https://developers.redhat.com/blog/2019/07/18an-introduction-to-cloud-native-ci-cd-with-red-hat-openshift-pipelines/)
- [blog.openshift.com: cloud native CI/CD with openshift pipelines](https://blog.openshift.com/cloud-native-ci-cd-with-openshift-pipelines/)
- [learn.openshift.com/middleware/pipelines](https://learn.openshift.com/middleware/pipelines/)
- [Easily reuse Tekton and Jenkins X from Jenkins](https://www.jenkins.io/blog/2021/04/21/tekton-plugin/)
- [lambda.grofers.com: Evolving Continuous Delivery in a Cloud-Native Environment 🌟](https://lambda.grofers.com/evolving-cd-in-a-cloud-native-environment-bb64a38145ae) In thispost, we’ll discuss the stages through which continuous delivery infrastructure has evolved at Grofers. We’ll start with how we began with Kubernetes and Jenkins and managed itsgrowing adoption. We’ll then discuss why we decided to move from Jenkins to Tekton, how we plan to scale it beyond a few teams, and what kind of challenges we have faced and arecurrently facing.
    - We started with Jenkins shared libs, and wrote common implementation for one group of engineering teams. This worked very well because not only were we able to consolidate and refactor all pipelines at once leading to several optimizations, it also made it easy to understand the CI implementation for all similar services and if we were to add common features and bug fixes it was really easy to push it through a common implementation.
    - There were benefits of doing this, but what was not desirable is that it took us a lot of effort to build these shared libs and despite our efforts to keep them simple, they ended up looking very complicated. Standard pipeline specs had departed from being declarative in nature and there was a lot of imperative Groovy logic mixed with Pipeline DSL.
- [itnext.io: Tekton Pipelines Kickstarter. Cloud Native CI/CD with Tekton — Laying The Foundation](https://itnext.iocloud-native-ci-cd-with-tekton-laying-the-foundation-a377a1b59ac0)
- [cd.foundation: Tekton Pipelines Kickstarter. Cloud Native CI/CD with Tekton — Building Custom Tasks](https://cd.foundation/blog/2021/04/22cloud-native-ci-cd-with-tekton-building-custom-tasks)
- [openshift.com: Running Testcontainers in OpenShift Pipelines With Docker-in-Docker (with Tekton)](https://www.openshift.com/blogrunning-testcontainers-in-openshift-pipelines-with-docker-in-docker)
- [blog.harbur.io: The Seven Steps to build a Cloud Native CI/CD for GitHub repos using Tekton](https://blog.harbur.iothe-seven-steps-to-build-a-cloud-native-ci-cd-for-github-repos-using-tekton-31a445a3bde)
- [itnext.io: Cloud Native CI/CD with Tekton — Building Custom Tasks](https://itnext.io/cloud-native-ci-cd-with-tekton-building-custom-tasks-663e63c1f4fb) Learn how to use, buildand deploy custom Tasks for Cloud-Native CI/CD on Kubernetes with Tekton Pipelines…
- [==opensource.com: Write your first CI/CD pipeline in Kubernetes with Tekton== 🌟](https://opensource.com/article/21/11/cicd-pipeline-kubernetes-tekton) Tekton is a Kubernetes-native open source framework for creating continuous integration and continuous delivery (CI/CD) systems.
- [opensource.com: Dynamic scheduling of Tekton workloads using Triggers](https://opensource.com/article/21/11/kubernetes-dynamic-scheduling-tekton) Upgrade your CI/CD pipeline with this Kubernetes-native application. Tekton Triggers is a Tekton component that allows you to detect and extract information from events from various sources and execute TaskRuns and PipelineRuns based on that information. It also enables passing extracted information to TaskRuns and PipelineRuns from events.
- [==piotrminkowski.com: Validate Kubernetes Deployment in CI/CD with Tekton and Datree==](https://piotrminkowski.com/2022/02/21/validate-kubernetes-deployment-in-ci-cd-with-tekton-and-datree)
- [sm43.medium.com: World of Tekton 😺 (Part 1)](https://sm43.medium.com/world-of-tekton-part-1-999738d63e25) This series will introduce you to the World of Tekton, its concepts and how you can leverage it to build an end to end CI/CD pipeline.
    - [Tekton: Concepts of Pipelines (Part 2)](https://sm43.medium.com/tekton-concepts-of-pipelines-part-2-cd86ad40bd34)
    - [sm43.medium.com: Tekton: Concepts of Triggers (Part 3)](https://sm43.medium.com/tekton-concepts-of-triggers-part-3-2ee17764addb)
    - [sm43.medium.com: Tekton: Building a Pipeline (Part 4)](https://sm43.medium.com/tekton-build-a-pipeline-part-4-baafd530b6fe)
    - [sm43.medium.com: Tekton: Triggering the Pipeline (Part 5)](https://sm43.medium.com/tekton-triggering-the-pipeline-part-5-dc38d73411fb)
- [==piotrminkowski.com: Canary Release on Kubernetes with Knative and Tekton==](https://piotrminkowski.com/2022/03/29/canary-release-on-kubernetes-with-knative-and-tekton/)
- [anadimisra.com: On Demand CI/CD with Serverless Tekton](https://www.anadimisra.com/post/on-demand-ci-cd-with-serverless-tekton) In this article, you will learn how to run Tekton with Terraform and EKS Fargate to build a serverless CI/CD platform
- [==hashnode.com: Tekton CI simplified==](https://hashnode.com/post/tekton-ci-simplified-ckzleauyw0n6beks1diq6ejvv) Complete guide to getting started with Tekton. In this blog, you will learn how to get started with Tekton and build a real-world pipeline for a containerized NodeJS application.
- [==devops.com: Using LLMs to Automate Pipeline Conversions From Legacy to Tekton==](https://devops.com/using-llms-to-automate-pipeline-conversions-from-legacy-to-tekton)

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