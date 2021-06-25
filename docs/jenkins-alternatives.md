# Jenkins Alternatives for Continuous Integration
- [Alternatives](#alternatives)
- [Cloud Native CI/CD](#cloud-native-cicd)
- [Comparisons](#comparisons)
- [Integration with other CI/CD engines](#integration-with-other-cicd-engines)
## Alternatives
* [Cloudbees Flow](https://www.cloudbees.com/products/flow/overview)
* [Circle CI](https://circleci.com/)
    * [Getting started with Kubernetes: how to set up your first cluster](https://circleci.com/blog/getting-started-with-kubernetes-how-to-set-up-your-first-cluster/)
    * [Adding approval jobs to your CI pipeline](https://circleci.com/blog/adding-approval-jobs-to-your-ci-pipeline/)
    * [uilding CI/CD pipelines using dynamic config](https://circleci.com/blog/building-cicd-pipelines-using-dynamic-config/)
* [Travis CI](https://travis-ci.org/)
    * [lambdatest.com: How To Build Your First CI/CD Pipeline With Travis CI?](https://www.lambdatest.com/blog/build-your-first-ci-cd-pipeline-with-travis-ci/)
* [Concourse](https://concourse-ci.org/)
    * [Building a continious deployment pipeline with Kubernetes and Concourse-CI](https://blog.alterway.fr/en/building-a-continious-deployment-pipeline-with-kubernetes-and-concourse-ci.html)
* [GoCD](https://www.gocd.org/)
* [Codefresh](https://codefresh.io/)
* [skaffold](https://skaffold.dev/)
* [JFrog Pipelines](https://jfrog.com/pipelines/)
* [Atlassian CI/CD](https://www.atlassian.com/continuous-delivery)
     * [Bamboo](https://www.atlassian.com/software/bamboo)
     * [lambdatest.com: How To Setup CI/CD Pipeline With Bamboo For PHP Projects](https://www.lambdatest.com/blog/how-to-setup-cicd-pipeline-with-bamboo-for-php-projects/)
* [GitLab CI](https://dzone.com/articles/gitlab-ci-with-docker-environment-variable-quirks)
* [GitHub Actions CI/CD](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/)
    * [docs.github.com: Learn GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)
    * [blog.bitsrc.io: Github Actions or Jenkins? Making the Right Choice for You](https://blog.bitsrc.io/github-actions-or-jenkins-making-the-right-choice-for-you-9ac774684c8) GitHub Actions and Jenkins both get the job done. Let’s find out whether it’s worth considering moving from Jenkins.
    * [openshift.com: Deploying to OpenShift using GitHub Actions](https://www.openshift.com/blog/deploying-to-openshift-using-github-actions)
    * [particule.io: Automatic build with Github Actions and Github Container Registry](https://particule.io/en/blog/cicd-github-registry/)
    * [proandroiddev.com: Improving CI/CD pipeline for Android via Fastlane and GitHub Actions](https://proandroiddev.com/improving-ci-cd-pipeline-for-android-via-fastlane-and-github-actions-a635162d2c53)
    * [redhat-actions](https://github.com/redhat-actions)
    * [redhat-actions/openshift-actions-runner](https://github.com/redhat-actions/openshift-actions-runner)
        * [redhat.com: Red Hat and GitHub Collaborate to Expand the Developer Experience on Red Hat OpenShift with GitHub Actions](https://www.redhat.com/en/about/press-releases/red-hat-and-github-collaborate-expand-developer-experience-red-hat-openshift-github-actions) Industry’s leading enterprise Kubernetes platform now integrates with GitHub, bringing DevOps automation tools from the world’s largest developer platform into the OpenShift ecosystem
    * [Awesome GitHub Actions](https://github.com/sdras/awesome-actions)
    * [yokawasa/action-setup-kube-tools](https://github.com/yokawasa/action-setup-kube-tools) A GitHub Action that setup Kubernetes tools (kubectl, kustomize, helm, kubeval, conftest, yq) and cache them on the runner. It is like a typescript version of stefanprodan/kube-tools with no command input param, but it's very fast as it installs the tools asynchronously.
    * [summerwind/actions-runner-controller](https://github.com/summerwind/actions-runner-controller) This controller operates self-hosted runners for GitHub Actions on your Kubernetes cluster.
* [Prow](https://github.com/kubernetes/test-infra/tree/master/prow)
* [Agola](https://agola.io/)
* [keptn](https://keptn.sh/) Keptn not only orchestrates Continuous Deployment, but it also orchestrates Continuous or Automated Operations.    
    * [dynatrace.com: What is keptn, how it works and how to get started!](https://www.dynatrace.com/news/blog/what-is-keptn-how-it-works-and-how-to-get-started/) 
    * [medium: Keptn 0.6.0 — My top 5 favorite improvements](https://medium.com/keptn/keptn-0-6-0-my-top-5-favorite-improvements-242d8ac1abfe)
    * [Quick Start](https://keptn.sh/docs/quickstart/)
    * [altoros.com: Automating Event-Based Continuous Delivery on Kubernetes with keptn](https://www.altoros.com/blog/automating-event-based-continuous-delivery-on-kubernetes-with-keptn/)
* [harness.io](https://harness.io/)
* [Drone](https://drone.io/)
* [Shippable (now part of JFrog Pipelines)](https://www.shippable.com/)
    * [JFrog Pipelines](https://jfrog.com/pipelines/)
* [Buildbot](https://buildbot.net/)
* [AWS DevOps - CICD](https://aws.amazon.com/devops/#cicd)
* [Google Cloud Build](https://cloud.google.com/cloud-build)
* [Azure DevOps](https://azure.microsoft.com/services/devops/)
    * [k21academy.com: Azure pipelines VS Jenkins](https://k21academy.com/microsoft-azure/az-400/azure-pipelines-vs-jenkins/)
* [Kubeflow](https://www.kubeflow.org/) The Machine Learning Toolkit for Kubernetes
* [shuttleOps](https://www.shuttleops.io/)
  * [thenewstack.io: ShuttleOps: No-Code Docker and Kubernetes](https://thenewstack.io/shuttleops-no-code-docker-and-kubernetes/)
* [HashiCorp Waypoint](https://www.waypointproject.io/)
  * [hashicorp.com: Announcing HashiCorp Waypoint](https://www.hashicorp.com/blog/announcing-waypoint)
* [onedev](https://github.com/theonedev/onedev)
    * [Hands-on GitOps with OneDev and Kubernetes](https://robinshen.medium.com/hands-on-gitops-with-onedev-f05bd278f07c)
* [lambdatest.com: 21 Of The Best Jenkins Alternatives For Developers](https://www.lambdatest.com/blog/best-jenkins-alternatives/)
* [Screwdriver API](https://github.com/screwdriver-cd/screwdriver) Screwdriver is a self-contained, pluggable service to help you build, test, and continuously deliver software using the latest containerization technologies.
* [TeamCity](https://www.jetbrains.com/teamcity/)
    * [jetbrains.com: Storing Project Settings in Version Control](https://www.jetbrains.com/help/teamcity/storing-project-settings-in-version-control.html)
    * [blog.jetbrains.com: Configuration as Code, Part 1: Getting Started with Kotlin DSL](https://blog.jetbrains.com/teamcity/2019/03/configuration-as-code-part-1-getting-started-with-kotlin-dsl/)
    * [github.com/OctopusDeploy/Octopus-TeamCity: JetBrains TeamCity plugin to trigger releases on build completion](https://github.com/OctopusDeploy/Octopus-TeamCity)
* [Octopus Deploy - deployment tool](https://octopus.com/)
    * [octopus.com: Octopus Configuration-as-Code with a language based on Hashicorp's HCL](https://octopus.com/blog/shaping-config-as-code)
    * [octopus.com: Deployment process as code](https://octopus.com/docs/deployments/patterns/deployment-process-as-code) If you want to do Octopus configuration as code today, we recommend using our .NET SDK which will always be supported. The Terraform provider will be a simpler, more declarative approach, that we will support in the future.
    * [registry.terraform.io: octopusdeploy Provider](https://registry.terraform.io/providers/OctopusDeployLabs/octopusdeploy/latest/docs)
    * [github.com/OctopusDeploy/go-octopusdeploy](https://github.com/OctopusDeploy/go-octopusdeploy) Go API Client for Octopus Deploy. A Go client for the Octopus Deploy API. This client is used by the [Octopus Deploy Terraform Provider](https://github.com/OctopusDeploy/terraform-provider-octopusdeploy).

## Cloud Native CI/CD
* [jenkins-x.io](https://jenkins-x.io/)
    * [cloudbees.com: what is jenkins-x](https://www.cloudbees.com/jenkins-x/what-is-jenkins-x)
    * [devopstoolkitseries.com](https://www.devopstoolkitseries.com/)
        * [youtube: Jenkins X: The Recipe For Continuous Delivery](https://www.youtube.com/watch?v=ihHr-iLfEGo)
    * [Book: The DevOps 2.6 Toolkit: Jenkins X](https://leanpub.com/the-devops-2-6-toolkit)
    * [Traces for your pipelines: Jenkins X v3 now comes with tracing support for your pipelines out of the box](https://jenkins-x.io/blog/2021/04/08/jx3-pipeline-trace/)
* [spinnaker.io deployment tool](https://www.spinnaker.io/)
    * [Deploy Spinnaker CD Pipelines in Kubernetes](https://www.opsmx.com/blog/deploy-spinnaker-cd-pipelines-in-kubernetes/)
    * [speakerdeck.com: Introduction to Spinnaker Managed Pipeline Templates](https://speakerdeck.com/keisukeyamashita/introduction-to-spinnaker-managed-pipeline-templates)
    * [speakerdeck.com: Spinnaker Application management by Terraform Plugins](https://speakerdeck.com/keisukeyamashita/spinnaker-application-management-by-terraform-plugins)
    * [medium: Spinnaker The Hard Way](https://medium.com/searce/spinnaker-the-hard-way-278913f3f1d8)
    * [opensource.com: Why Spinnaker matters to CI/CD](https://opensource.com/article/19/8/why-spinnaker-matters-cicd) Spinnaker provides unique building blocks to create tailor-made, and highly-collaborative continuous delivery pipelines. 
    * [medium: How we rolled out our Kubernetes platform in Adevinta Spain](https://medium.com/adevinta-tech-blog/how-we-rolled-out-our-kubernetes-platform-in-adevinta-spain-63495884a1db)
    * [harness.io: Best Spinnaker Alternatives to Consider](https://harness.io/blog/continuous-delivery/spinnaker-alternatives/)
    * [armory.io: Build a Deployment Pipeline with Spinnaker on Kubernetes](https://www.armory.io/blog/build-a-deployment-pipeline-with-spinnaker-on-kubernetes/)
* [ArgoCD](https://argoproj.github.io/argo-cd/) Declarative GitOps CD for Kubernetes
    * [Cloud Native Computing Foundation Accepts Argo as an Incubator Project](https://www.intuit.com/blog/technology/cloud-native-computing-foundation-accepts-argo-as-an-incubator-project/)
    * [openshift.com: OpenShift Authentication Integration with ArgoCD](https://www.openshift.com/blog/openshift-authentication-integration-with-argocd)
    * [developers.redhat.com: OpenShift joins the Argo CD community (KubeCon Europe 2020)](https://developers.redhat.com/blog/2020/08/17/openshift-joins-the-argo-cd-community-kubecon-europe-2020/)
    * [thenewstack.io: Applied GitOps with ArgoCD](https://thenewstack.io/applied-gitops-with-argocd/)
    * [IBM/argocd-vault-plugin](https://github.com/IBM/argocd-vault-plugin) An ArgoCD plugin to retrieve secrets from Hashicorp Vault and inject them into Kubernetes secrets.
    * [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)
    * [openshift.com: Getting Started with ApplicationSets](https://www.openshift.com/blog/getting-started-with-applicationsets) "App of Apps" pattern.
    * [argocd-autopilot](https://github.com/argoproj-labs/argocd-autopilot) The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps repositories.
    * [gspann.com: Significance of Using Spinnaker When Adopting a Kubernetes Environment 🌟](https://www.gspann.com/resources/blogs/significance-of-using-spinnaker-when-adopting-a-kubernetes-environment/) Spinnaker acts as a multi-cloud deployment tool to support continuous workflows in a Kubernetes environment. Understand the Spinnaker architecture and learn about the best practices that can help you better deploy applications on Kubernetes clusters.
* [Tekton](https://github.com/tektoncd/)
    * [Tekton PetClinic Demo](https://github.com/tektoncd/pipeline)
    * [Tekton PetClinic Demo Youtube](https://www.youtube.com/watch?v=igwFpZOUTnw)
    * [OpenShift Tekton pipelines](https://www.openshift.com/learn/topics/pipelines)
    * [developers.redhat.com: An introduction to cloud native CI/CD with Red Hat OpenShift pipelines](https://developers.redhat.com/blog/2019/07/18/an-introduction-to-cloud-native-ci-cd-with-red-hat-openshift-pipelines/)
    * [blog.openshift.com: cloud native CI/CD with openshift pipelines](https://blog.openshift.com/cloud-native-ci-cd-with-openshift-pipelines/) 
    * [learn.openshift.com/middleware/pipelines](https://learn.openshift.com/middleware/pipelines/)
    * [Easily reuse Tekton and Jenkins X from Jenkins](https://www.jenkins.io/blog/2021/04/21/tekton-plugin/)
    * [lambda.grofers.com: Evolving Continuous Delivery in a Cloud-Native Environment 🌟](https://lambda.grofers.com/evolving-cd-in-a-cloud-native-environment-bb64a38145ae) In this post, we’ll discuss the stages through which continuous delivery infrastructure has evolved at Grofers. We’ll start with how we began with Kubernetes and Jenkins and managed its growing adoption. We’ll then discuss why we decided to move from Jenkins to Tekton, how we plan to scale it beyond a few teams, and what kind of challenges we have faced and are currently facing.
        * We started with Jenkins shared libs, and wrote common implementation for one group of engineering teams. This worked very well because not only were we able to consolidate and refactor all pipelines at once leading to several optimizations, it also made it easy to understand the CI implementation for all similar services and if we were to add common features and bug fixes it was really easy to push it through a common implementation.
        * There were benefits of doing this, but what was not desirable is that it took us a lot of effort to build these shared libs and despite our efforts to keep them simple, they ended up looking very complicated. Standard pipeline specs had departed from being declarative in nature and there was a lot of imperative Groovy logic mixed with Pipeline DSL.
    * [itnext.io: Tekton Pipelines Kickstarter. Cloud Native CI/CD with Tekton — Laying The Foundation](https://itnext.io/cloud-native-ci-cd-with-tekton-laying-the-foundation-a377a1b59ac0)
    * [cd.foundation: Tekton Pipelines Kickstarter. Cloud Native CI/CD with Tekton — Building Custom Tasks](https://cd.foundation/blog/2021/04/22/cloud-native-ci-cd-with-tekton-building-custom-tasks)
    * [openshift.com: Running Testcontainers in OpenShift Pipelines With Docker-in-Docker (with Tekton)](https://www.openshift.com/blog/running-testcontainers-in-openshift-pipelines-with-docker-in-docker)
    * [blog.harbur.io: The Seven Steps to build a Cloud Native CI/CD for GitHub repos using Tekton](https://blog.harbur.io/the-seven-steps-to-build-a-cloud-native-ci-cd-for-github-repos-using-tekton-31a445a3bde)
* [Jenkins-X + Tekton on OpenShift](https://github.com/openshift/tektoncd-pipeline-operator)
    * [CI/CD OpenShift and Tekton](https://blog.sonatype.com/new-cloud-native-ci/cd-projects-openshift-and-tekton)
    * [github.com/openshift/pipelines-tutorial](https://github.com/openshift/pipelines-tutorial)
    * [https://github.com/jenkins-x/jenkins-x-openshift-image](https://github.com/jenkins-x/jenkins-x-openshift-image)
    * [medium: Dailymotion’s journey from Jenkins to Jenkins X](https://medium.com/dailymotion/from-jenkins-to-jenkins-x-604b6cde0ce3)
* HAT is the acronym for Helm, ArgoCD and Tekton:
    * [empathy.co: HAT: CI/CD for Deploying Cloud Native Applications](https://www.empathy.co/blog/hat-ci-cd-for-deploying-cloud-native-applications/) 

## Comparisons
* [dzone: Which CI is Best For My Team?](https://dzone.com/articles/which-ci-is-best-for-my-team)
* [inovex.de: Spinnaker vs. Argo CD vs. Tekton vs. Jenkins X: Cloud-Native CI/CD](https://www.inovex.de/blog/spinnaker-vs-argo-cd-vs-tekton-vs-jenkins-x/)
* [medium: Top 7 Best CI/CD Tools you should get your hands on in 2020](https://medium.com/devops-dudes/top-7-best-ci-cd-tools-you-should-get-your-hands-on-in-2020-832c29db936a)
* [dzone: Jenkins vs GitLab CI: Battle of CI/CD Tools](https://dzone.com/articles/jenkins-vs-gitlab-ci-battle-of-cicd-tools) The battle of CI/CD tools rages on — come and find out which is the right tool for your DevOps testing needs.
* [lambdatest.com: TeamCity vs. Jenkins: Picking The Right CI/CD Tool](https://www.lambdatest.com/blog/teamcity-vs-jenkins-picking-the-right-ci-cd-tool/)
* [cBamboo vs Jenkins: Showdown Of CI/CD Tools](https://www.lambdatest.com/blog/bamboo-vs-jenkins-showdown-of-ci-cd-tools/)
* [blog.thundra.io: The CI/CD War of 2021: A Look at the Most Popular Technologies](https://blog.thundra.io/the-ci/cd-war-of-2021-a-look-at-the-most-popular-technologies)
* [lambdatest.com: CircleCI Vs. GitLab: Choosing The Right CI/CD Tool](https://www.lambdatest.com/blog/circleci-vs-gitlab/)

## Integration with other CI/CD engines
* [CloudBees Integrates Software Delivery Management Platform With Google Cloud Build and Tekton to Break Down Development Silos](https://www.previous.cloudbees.com/press/cloudbees-integrates-software-delivery-management-platform-google-cloud-build-and-tekton-break)

---
<center>
[![gitlab](images/gitlab.jpg)](https://gitlab.com/)
</center>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD: Is it possible that Kubeflow pipeline is one of the best CI/CD tools for Kubernetes?<br><br>I spent some time playing with Kubernetes &amp; <a href="https://twitter.com/kubeflow?ref_src=twsrc%5Etfw">@kubeflow</a> pipelines, and they have one feature which is just great:<br><br>You can define the pipeline with real code! <a href="https://t.co/gNDzvvkCij">pic.twitter.com/gNDzvvkCij</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1285929877493800961?ref_src=twsrc%5Etfw">July 22, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<script async class="speakerdeck-embed" data-id="4792e3bc2f474efb8589d231314091e8" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>
</center>