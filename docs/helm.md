# Helm Kubernetes Tool

1. [Helm](#helm)
2. [Helm Plugins](#helm-plugins)
3. [Helm Chart Documentation](#helm-chart-documentation)
4. [Helm Dashboard](#helm-dashboard)
5. [Kubecrt](#kubecrt)
6. [Datree](#datree)
7. [Helm Charts repositories](#helm-charts-repositories)
8. [Helm Charts](#helm-charts)
9. [Shalm. Scriptable helm charts](#shalm-scriptable-helm-charts)
10. [Helmfile](#helmfile)
11. [Database Migrations](#database-migrations)
12. [Helm Tools](#helm-tools)
13. [Helm Books](#helm-books)
14. [Videos](#videos)
15. [Tweets](#tweets)

## Helm

- [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)
- [thoughtworks.com: Helm](https://www.thoughtworks.com/radar/tools/helm)
- [helm.sh](https://helm.sh/)
    - [helm.sh/docs](https://helm.sh/docs)
    - [helm.sh: Getting Started 🌟](https://helm.sh/docs/chart_template_guide/getting_started/)
- [GitHub: Helm, the Kubernetes Package Manager](https://github.com/helm/helm) Installing and managing Kubernetes applications
- [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4)
- [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng)
- [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8)
- [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w)
- [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o)
- [dzone: the art of the helm chart patterns](https://dzone.com/articles/the-art-of-the-helm-chart-patterns-from-the-offici)
- [dzone: 15 useful helm chart tools](https://dzone.com/articles/15-useful-helm-charts-tools)
- [dzone: create install upgrade and rollback a helm chart - part 1](https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p)
- [dzone: create install upgrade and rollback a helm chart - part 2](https://dzone.com/articles/create-install-upgrade-rollback-a-helm-chart-part)
- [dzone: cicd with kubernetes and helm](https://dzone.com/articles/cicd-with-kubernetes-and-helm)
- [dzone: do you need helm?](https://dzone.com/articles/do-you-need-helm)
- [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)
- [codefresh.io: Using Helm 3 with Helm 2 charts](https://codefresh.io/helm-tutorial/taking-helm-3-spin/)
- [banzaicloud.com: Helm 3, the Good, the Bad and the Ugly](https://banzaicloud.com/blog/helm3-the-good-the-bad-and-the-ugly/)
- [helm.sh: How to migrate from Helm v2 to Helm v3](https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3/)
- [Helm 3: Validating Helm Chart Values with JSON Schemas 🌟](https://www.arthurkoziel.com/validate-helm-chart-values-with-json-schemas/)
- [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2)
- [medium: Helm Chart — Development Guide 🌟](https://medium.com/swlh/helm-chart-development-guide-bbc525d3b448) Writing maintainable and reliable charts with few tricks
- [medium: Multi-namespace Helm deploy in Kubernetes](https://medium.com/analytics-vidhya/multi-namespace-helm-deploy-in-kubernetes-26d1baf1ca5c)
- [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
- [daveops.xyz: Running DB migrations on Kubernetes with Helm](https://daveops.xyz/en/2020/09/18/running-db-migrations-on-kubernetes-with-helm/)
- [mbbaig.blog: How to create custom Helm charts 🌟](https://mbbaig.blog/how-to-create-custom-helm-charts/)
- [medium: Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
- [dev.to: Introduction to Helm 🌟](https://dev.to/edlegaultle/introduction-to-helm-50jl)
- [itnext.io: Helm 3 Umbrella Charts & Standalone Chart Image Tags — An Alternative Approach](https://itnext.io/helm-3-umbrella-charts-standalone-chart-image-tags-an-alternative-approach-78a218d74e2d) Helm umbrella charts, for those who aren’t familiar, describe and encapsulate a deployable collection of loosely couple Kubernetes components as a higher-order Helm chart. In other words, a collection of software elements that each have their own individual charts but, for whatever reason (e.g. design choices, ease of deployability, versioning complexities), must be installed or upgraded as a since atomic unit.
- [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
- [jfrog.com: Steering Straight with Helm Charts Best Practices 🌟](https://jfrog.com/blog/helm-charts-best-practices/)
- [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
- [youtube.com: Demystifying Helm 🌟](https://www.youtube.com/watch?v=2HPsPOwHOlY&ab_channel=DonovanBrown)
- [harness.io: Introduction to Helm: Charts, Deployments, & More 🌟](https://harness.io/blog/continuous-delivery/what-is-helm/)
- [freecodecamp.org: What is a Helm Chart? A Tutorial for Kubernetes Beginners](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners)
- [youtube: GitOps Guide to the Galaxy: Working with Helm](https://www.youtube.com/watch?v=1FzOlSed5ts&ab_channel=OpenShift)
- [cncf.io: Quick application deployments on MicroK8s using Helm Charts](https://www.cncf.io/blog/2021/03/23/quick-application-deployments-on-microk8s-using-helm-chart)
- [cncf.io: Add Java Agents to Existing Kubernetes and Helm Applications Instantly](https://www.cncf.io/blog/2021/03/24/add-java-agents-to-existing-kubernetes-and-helm-applications-instantly)
- [medium: Create Helm Charts to manage Kubernetes applications](https://medium.com/marionete/create-helm-charts-to-manage-kubernetes-applications-9c4235acf99e) Understand what is Helm, Helm Charts and how to configure GitHub pages to store and share your Charts.
- [blog.heyal.co.uk: How to unit-test your helm charts with Golang 🌟](https://blog.heyal.co.uk/unit-testing-helm-charts/) Learn how to write Golang unit tests for your Helm charts to keep quality high and make changes with confidence.
- [bridgecrew.io: Part 1: Top trends from analyzing the security posture of open-source Helm charts](https://bridgecrew.io/blog/open-source-helm-security-research/)
    - [bridgecrew.io: Part 2: Top trends from analyzing the security posture of open-source Helm charts](https://bridgecrew.io/blog/open-source-helm-security-research-part-2/)
    - [bridgecrew.io: Part 3: Top trends from analyzing the security posture of open-source Helm charts](https://bridgecrew.io/blog/open-source-helm-security-research-part-3/)
- [redhat.com: Red Hat OpenShift Certification extends support for Kubernetes-native technologies with Helm 🌟](https://www.redhat.com/en/blog/red-hat-openshift-certification-extends-support-kubernetes-native-technologies-helm) __Helm or Operators: how to choose__
- [jasiek-petryk.medium.com: Setting up a private Helm chart repository on GitHub](https://jasiek-petryk.medium.com/setting-up-a-private-helm-chart-repository-on-github-4a767703cec8)
- [betterprogramming.pub: How To Continuously Test and Deploy Your Helm Charts on Kubernetes Clusters Using Kind](https://betterprogramming.pub/how-to-continuously-test-and-deploy-your-helm-charts-on-kubernetes-clusters-using-kind-d71e3585d2dc) Set up your CI/CD tools to easily test and publish charts on ephemeral Kubernetes clusters
- [blog.flant.com: Making the most out of Helm templates 🌟](https://blog.flant.com/advanced-helm-templating/) The standard Helm library and traditional approaches to creating Helm charts are generally okay to automate non-complex tasks. But the growing complexity and number of Helm charts rapidly make the minimalistic Helm templates and controversial standard Helm library insufficient. In this article, we will show you how to make your Helm templates much more flexible and dynamic by implementing your own Helm “functions” and exploiting the capabilities of the tpl function.
- [levelup.gitconnected.com: Helm 101 for Developers](https://levelup.gitconnected.com/helm-101-for-developers-1c28e734937e)
- [developers.redhat.com: Deploy Helm charts with Jenkins CI/CD in Red Hat OpenShift 4 🌟](https://developers.redhat.com/articles/2021/05/24/deploy-helm-charts-jenkins-cicd-red-hat-openshift-4)
- [developers.redhat.com: Deploy Node.js applications to Red Hat OpenShift with Helm](https://developers.redhat.com/articles/2021/07/20/deploy-nodejs-applications-red-hat-openshift-helm)
- [thenewstack.io: Upgrade Helm if You Don’t Want to Share Your Username and Password (Helm’s CVE-2021-32690) 🌟](https://thenewstack.io/upgrade-helm-if-you-dont-want-to-share-your-username-and-password/)
- [thedeveloperstory.com: Helm 101: Brief introduction to kubernetes package manager](https://thedeveloperstory.com/2021/07/12/helm-101-brief-introduction-to-kubernetes-package-manager/)
- [betterprogramming.pub: 6 Tips for Creating Helm Charts in Kubernetes Applications](https://betterprogramming.pub/6-tips-for-creating-helm-charts-in-kubernetes-applications-452a37446f31) Build, maintain, and control Helm chart releases with fewer bugs and code issues
- if you're having either https://github.com/helm/helm/issues/10005 or https://github.com/helm/helm/issues/10004, it's because the older Helm 2 backing store is finally gone. You REALLY should upgrade to Helm 3, and now. You're risking your security more than you should.
- [medium: Kubernetes Deployment using Helm Charts and Krane 🌟](https://medium.com/groupon-eng/kubernetes-deployment-using-helm-charts-and-krane-e0100b55d00c)
- [cloud.redhat.com: Application Management in Kubernetes Environments with Helm Charts and Kubernetes Operators](https://cloud.redhat.com/blog/application-management-in-kubernetes-environments-with-helm-charts-and-kubernetes-operators)
- [codersociety.com: 13 Best Practices for using Helm](https://codersociety.com/blog/articles/helm-best-practices) Helm is an indispensable tool for deploying applications to Kubernetes clusters. But it is only by following best practices that you’ll truly reap the benefits of Helm. Here are 13 best practices to help you create, operate, and upgrade applications using Helm.
- [bridgecrew.io: Applying Kubernetes security best practices to Helm charts](https://bridgecrew.io/blog/applying-kubernetes-security-best-practices-to-helm-charts/)
- [dzone.com: Deploy a Java application using Helm, Part 1 (OpenShift) 🌟](https://dzone.com/articles/deploy-a-java-application-using-helm-part-1)
- [codefresh.io: Using Helm with GitOps 🌟](https://codefresh.io/helm-tutorial/using-helm-with-gitops/)
    - [medium: Using Helm with GitOps](https://medium.com/containers-101/using-helm-with-gitops-555443340369)
- [==medium: Test Helm Release in Production Environment with Zero Downtime== 🌟](https://medium.com/@deejiw/test-helm-release-in-production-environment-with-zero-downtime-400c5d41ecdf) Helm has been very popular for Kubernetes production. However, to ensure consistency across releases, today we are going to learn how to test deployment on production environment without any interruption with production pods.
- [==learn.hashicorp.com: Deploy a Helm-based application automatically with GitOps==](https://learn.hashicorp.com/tutorials/waypoint/gitops-helm-deployment)
- [hashicorp.com: Deploying Helm Apps to Kubernetes with Waypoint and GitOps](https://www.hashicorp.com/blog/deploying-helm-apps-to-kubernetes-with-waypoint-and-gitops)
- [medium.com/dailymotion: Deploying apps on multiple Kubernetes clusters with Helm](https://medium.com/dailymotion/deploying-apps-on-multiple-kubernetes-clusters-with-helm-19ee2b06179e)
- [gennyallcroft.medium.com: Understanding Kubernetes deployments with Helm](https://gennyallcroft.medium.com/understanding-kubernetes-deployments-with-helm-444116a622be)
- [medium.com/codex: Helm Charts For Kubernetes Developers](https://medium.com/codex/helm-charts-for-kubernetes-developers-dce5719d4c8c)
- [==apiiro.com: Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments==](https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments/)
- [medium.com/@paolo.gallina: How-to release Helm Charts maintaining your mental health 🌟](https://medium.com/@paolo.gallina/releasing-helm-charts-maintaining-your-mental-health-b382685390c8) Three tips for maintaining and developing Helm charts.
- [devopslearners.com: How to Convert Helm Chart to Kubernetes YAML](https://devopslearners.com/how-to-convert-helm-chart-to-kubernetes-yaml-fbe6d6722f6)
- [mlepeshkin.medium.com: Automated Kubernetes deployment with Helm and additional templating](https://mlepeshkin.medium.com/automated-kubernetes-deployment-with-helm-and-additional-templating-dc960689609f)
- [==dev.to/francoislp: Post-mortem: 1h30 downtime on a Saturday morning==](https://dev.to/francoislp/post-mortem-1h30-downtime-on-a-saturday-morning-5af0) Read how 4 YAML lines brought down 3 APIs for 1h30 on a Saturday morning. In the end, the issue was a Helm chart misconfiguration where 2 settings were conflicting with each other.
- [==blog.ediri.io: How To Unit Test Your Helm Charts==](https://blog.ediri.io/how-to-unit-test-your-helm-charts) With the help of helm-unittest and the AAA pattern
- [==itnext.io: Reference Other Values in Helm Chart Values File==](https://itnext.io/reference-other-values-in-helm-chart-values-file-19d44d9276c7) Helm offers a template engine that allows you to merge configuration values into templates. This article introduces the __"tpl" function to evaluate strings as templates to have even more flexibility in your values.yaml__
- [medium.com/linkbynet: Helm chart releaser with GitLab CI, Generated and Parent-Child Pipelines](https://medium.com/linkbynet/helm-chart-releaser-with-gitlab-ci-generated-and-parent-child-pipelines-b57b50e6c442)
- [==medium.com/@percenuage: My adventure with Helm as GitOps in a distributed architecture==](https://medium.com/@percenuage/my-adventure-with-helm-as-gitops-in-a-distributed-architecture-6a6fdc6f11bd) In this article, you will learn some practical tips on how to manage your Helm charts and __GitOps__ workflows:
    - Common vs multiple Helm charts
    - Values YAML hierarchy
    - Git repository management
- [medium.com/avmconsulting-blog: How to Deploy Applications using Helm in Kubernetes |AWS|](https://medium.com/avmconsulting-blog/deploying-applications-using-helm-in-kubernetes-b5c8b609e4b5)
- [medium.com/tech-chronicles: Helm tests](https://medium.com/tech-chronicles/helm-test-tested-my-patience-732eeab0e935) Helm tests are helpful to test your charts in your CI/CD pipeline, but when they fail due to network issues (e.g. pod takes time to serve the response) they are difficult to debug.
- [xbery.medium.com: Deploy helm charts using Terraform module 🌟](https://xbery.medium.com/deploy-helm-charts-using-terraform-module-63684efbd221)
- [community.ops.io: [K8s] Fix Helm release failing with an upgrade still in progress](https://community.ops.io/the_cozma/k8s-fix-helm-release-failing-with-an-upgrade-still-in-progress-4660) This article applies to: Helm v3.8.0. If you use Helm to manage your releases, you might end up in a case where the release is stuck in a pending state and all subsequent releases keep failing. This article explains how to fix it with two options:
    - Helm rollback
    - Deleting the state
- [dev.to: HULL Tutorial 01: Introducing HULL, the Helm Universal Layer Library](https://dev.to/gre9ory/hull-tutorial-01-introducing-hull-the-helm-universal-layer-library-4njb)
- [medium.com/@lasithih927: Helm on Kubernetes - Zero to Hero in 5 Minutes 🌟](https://medium.com/@lasithih927/helm-zero-to-hero-4cab17fac38e) A Helm cheat sheet for getting your desired application installed on a Kubernetes cluster with the config you need in no time. Even if you haven’t heard of Helm before! This will take you from zero to hero.
- [==medium.com/codex: Simplifying Kubernetes Deployments With Helm Package Manager== 🌟](https://medium.com/codex/simplifying-kubernetes-deployments-with-helm-package-manager-bf834c51818d)
- [==medium.com/geekculture: Helm — Advanced Commands== 🌟](https://medium.com/geekculture/helm-advanced-commands-9365097475b)
- [levelup.gitconnected.com: Helm—Named Templates](https://levelup.gitconnected.com/helm-named-templates-de2efc3875d0) A deep dive into partial or subtemplates
- [faun.pub: Helm — Template Actions, Functions, and Pipelines 🌟](https://faun.pub/helm-template-actions-functions-and-pipelines-16ed23ed336f) Overview of helm template actions, functions, and pipelines
- [shipmight.com: Understanding Helm upgrade flags](https://shipmight.com/blog/understanding-helm-upgrade-reset-reuse-values) Every now and then you’ll need to use the `--reset-values` and `--reuse-values` flags when running a Helm upgrade. Let's dive into how they actually work and also look at a gotcha when the values of a chart have changed in-between upgrades
- [==blog.devops.dev: Stop cloning helm charts! Enough!== 🌟](https://blog.devops.dev/stop-cloning-helm-charts-enough-b40fb5d67ac7)
- [medium.com/kubeshop-i: Monokle, Helm & Quality Kubernetes Deployments](https://medium.com/kubeshop-i/monokle-helm-quality-kubernetes-deployments-af050fcc91db)
- [blog.devops.dev: Hosting Your Own Helm Chart on GitHub with Chart Releaser](https://blog.devops.dev/hosting-your-own-helm-chart-on-github-with-chart-releaser-a356ac10ce5c)
- [faun.pub: Package and Deploy Your Application Using Helm Chart](https://faun.pub/package-and-deploy-your-application-using-helm-chart-21f0c568e65c) In this tutorial, you will learn the end-to-end process of creating a spring boot application and deploying it as a Helm chart on a minikube cluster
- [medium.com/@badawekoo: Helm theory, demo and commands you need to know!](https://medium.com/@badawekoo/helm-theory-demo-and-commands-you-need-to-know-628777fdb0c2)
- [dev.to: Helm Release Time-To-Live(TTL)⏳💀 for Temporary Environments](https://dev.to/rtpro/helm-release-time-to-livettl-for-temporary-environments-1239) When working with Kubernetes, it’s often the case that you’ll need to create temporary environments/namespaces. You might need this as a way to limit the resources use, handle dev/staging environments, or just as a way to contain your tests while working on them. If you have used Helm before, you know that installing applications via Helm charts is simple by using the helm install command. The problem is that after installing a package, you or the user still needs to manually delete the package. With this in mind, we are going to explore how we set Time-To-Live Expiration for helm releases via the Helm release plugin, and create temporary Environments with Time-To-Live to make our lives easier with Helm.
- [sysdig.com: Helm security and best practices](https://sysdig.com/blog/how-to-secure-helm/)
- [medium.com: Helm Your Kubernetes Application](https://medium.com/zeals-tech-blog/helm-your-kubernetes-application-7af6293bcfcf)
- [medium.com/linux-shots: Use PostgreSQL database as backend storage for helm](https://medium.com/linux-shots/use-postgresql-as-backend-storage-for-helm-de407cd9c43) By default, Helm 3 stores all release information in Kubernetes cluster itself using K8s secret in release namespace.
- [tratnayake.dev: Using Helm To Include All Files From A Directory In-line](https://tratnayake.dev/helm-include-all-files-from-directory-in-line) In this article, you will learn how to use Helm to fetch all files and their contents from a directory and include them in-line
- [fenyuk.medium.com: Helm for Kubernetes. Datree for keeping cluster secure and healthy 🌟](https://fenyuk.medium.com/helm-for-kubernetes-datree-for-keeping-cluster-secure-and-healthy-6fbd10f0d958)
- [fenyuk.medium.com: Helm for Kubernetes. GitOps with Argo CD 🌟](https://fenyuk.medium.com/helm-for-kubernetes-gitops-with-argo-cd-c8f80330596)
- [medium.com/geekculture: HELM — How Release Information is Stored](https://medium.com/geekculture/helm-how-release-information-is-stored-778d7f0b7498) Advanced Helm usage
- [levelup.gitconnected.com: Helm — Data Sharing Between Parent and Child Chart](https://levelup.gitconnected.com/helm-data-sharing-between-parent-and-child-chart-c4487a452d4e) Data exchange between parent and child chart in helm. In this article, you will explore a few strategies to share data between Helm charts:
    - Overriding values from a parent chart
    - Making child chart data available to the parent chart
    - Global chart values
    - Sharing templates with subcharts

- [blog.searce.com: Transform Kubernetes Manifests into Helm Chart](https://blog.searce.com/transform-kubernetes-manifests-into-helm-chart-f3d100688423)
- [medium.com/geekculture: Helm Chart Wait for All Dependencies Before Starting Kubernetes Pods](https://medium.com/geekculture/helm-chart-wait-for-all-dependencies-before-starting-kubernetes-pods-cc0a3ddbf02b) Improve the quality of your helm charts by supporting wait for dependencies feature
- [blog.knell.it: Making your Helm Chart observable for Prometheus](https://blog.knell.it/making-your-helm-chart-observable-for-prometheus/) In this blog post, I walk you through the various steps required to make an existing Helm chart observable by Prometheus.
- [==mattias.engineer/courses/kubernetes/helm: Kubernetes-101: Helm== 🌟](https://mattias.engineer/courses/kubernetes/helm/)

## Helm Plugins

- [Helm Diff Plugin 🌟](https://github.com/databus23/helm-diff) A helm plugin that shows a diff explaining what a helm upgrade would change
- [Helm mapkubeapis Plugin](https://github.com/helm/helm-mapkubeapis) This is a Helm plugin which map deprecated or removed Kubernetes APIs in a release to supported APIs. __With kubernetes 1.22 dropping support for more beta APIs, you might be in need of a helmpack plugin to help you with that..__
- [medium.com/@marc.khouzam: Shell completion for plugins with Helm 3.8](https://medium.com/@marc.khouzam/shell-completion-for-plugins-with-helm-3-8-7cb001012a54) (This post is mostly targeted towards helm plugin developers)
- [JovianX/helm-release-plugin](https://github.com/JovianX/helm-release-plugin) Helm3 plugin that pulls(re-creates) helm Charts from deployed releases, and updates values of deployed releases without the chart.

## Helm Chart Documentation

- [chart-doc-gen: Helm Chart Documentation Generator](https://github.com/kubepack/chart-doc-gen)
- [Frigate](https://frigate.readthedocs.io/) is a tool for automatically generating documentation for your Helm charts. It will use the chart’s Chart.yaml and values.yaml files in order to generate the content in a markup language of your choice.
- [rafay.co: Helm Chart Hooks Tutorial](https://rafay.co/the-kubernetes-current/helm-chart-hooks-tutorial/)
- [itnext.io: Helm: reusable chart — named templates, and a generic chart for multiple applications](https://itnext.io/helm-reusable-chart-named-templates-and-a-generic-chart-for-multiple-applications-13d9b26e9244) Designing reusable chart with Helm:  named templates, and a generic chart for multiple applications
- [jfrog.com: Helm is for everyone! (download your free helm guide)](https://jfrog.com/assets/helm-is-for-everyone/)
- [thenewstack.io: Applying Kubernetes Security Best Practices to Helm Charts 🌟](https://thenewstack.io/applying-kubernetes-security-best-practices-to-helm-charts/)
- [medium: Highway to Helm: How to efficiently manage chart sources](https://medium.com/adevinta-tech-blog/highway-to-helm-how-to-efficiently-manage-chart-sources-f5749ba8031e) In this post, we’ll go through two ways to manage the source files of Helm charts, we’ll discuss the different factors that make one more suitable than the other, depending on your organisational structure, and we’ll provide guidance on choosing the right way to go by sharing what conditions are in favour of each of the two methods.
- [helm-docs](https://github.com/norwoodj/helm-docs) The `helm-docs` tool auto-generates documentation from helm charts into markdown files. The resulting files contain metadata about their respective chart and a table with each of the chart's values, their defaults, and an optional description parsed from comments.

## Helm Dashboard

- [medium.com/geekculture: K8s — Helm Dashboard](https://medium.com/geekculture/k8s-helm-dashboard-d7509c5fee88) The missing UI of Helm
- [levelup.gitconnected.com: Introduction to Helm Dashboard](https://levelup.gitconnected.com/introduction-to-helm-dashboard-dddf43e38cc2)
- [github.com/komodorio/helm-dashboard 🌟](https://github.com/komodorio/helm-dashboard) The Helm Dashboard plugin offers a UI-driven way to view the installed Helm charts, and see their revision history and corresponding Kubernetes resources. Also, you can perform simple actions like roll back to a revision or upgrade to a newer version

## Kubecrt

- [Kubecrt](https://github.com/blendle/kubecrt)
- [Kubecrt - Convert HELM charts to kubernetes resources 🌟](https://toolbox.kali-linuxtr.net/kubecrt-convert-helm-charts-to-kubernetes-resources.tool)

## Datree

- https://github.com/datreeio/datree Prevent Kubernetes misconfigurations from reaching production (again 😤 )! __Datree__ is a CLI tool to ensure K8s manifests and Helm charts follow best practices as well as your organization’s policies. See our docs: https://hub.datree.io/
- [datree.io: How to build a Helm plugin in minutes](https://www.datree.io/resources/how-to-build-a-helm-plugin-in-minutes)
- [opensource.com: What Kubernetes taught me about development](https://opensource.com/article/21/12/kubernetes-developer) Why policy management was the key to understanding Kubernetes and the DevOps pipeline.
- [aws.amazon.com: Preventing Kubernetes misconfigurations using Datree](https://aws.amazon.com/blogs/containers/preventing-kubernetes-misconfigurations-using-datree/)

## Helm Charts repositories

- [codeengineered.com: 4 Places To Find Helm Charts](https://codeengineered.com/blog/2020/helm-find-charts/)
- [hub.helm.sh 🌟](http://hub.helm.sh) -> [artifacthub.io 🌟](https://artifacthub.io/) Find, install and publish
Kubernetes packages
    - [New Location For Stable and Incubator Charts](https://helm.sh/blog/new-location-stable-incubator-charts/)
    - [charts.helm.sh/stable 🌟](https://charts.helm.sh/stable)
    - [charts.helm.sh/incubator 🌟](https://charts.helm.sh/incubator/)
- [Bitnami Helm Charts](https://bitnami.com/stacks/helm)
- [JFrog ChartCenter](https://chartcenter.io/)
    - [Navigating Kubernetes With Helm 3 Charts and ChartCenter 🌟](https://dzone.com/articles/navigating-kubernetes-with-helm-3-charts-and-chart) ChartCenter is a free central repository for discovering Helm Charts, created to help manage your Kubernetes applications
- [Artifact Hub 🌟](https://artifacthub.io/) Find, install and publish Kubernetes packages
- [KubeApps Hub](https://hub.kubeapps.com/)
- [github: Nova 🌟](https://github.com/fairwindsops/nova) Find outdated or deprecated Helm charts running in your cluster.
- [github: Kubernetes Deployment Orchestrator](https://github.com/SAP/kubernetes-deployment-orchestrator) This project brings the starlark scripting language to helm charts.
- [harness.io: Tutorial: Turning a GitHub Repo Into a Helm Chart Repo](https://harness.io/blog/devops/helm-chart-repo/)

## Helm Charts

- [Jenkins](https://github.com/helm/charts/tree/master/stable/jenkins)
- [Codecentric Jenkins 🌟](https://github.com/codecentric/helm-charts/tree/master/charts/jenkins) Helm 3 compliant (Simpler and more secure than helm 2)
- [Nexus3](https://github.com/helm/charts/tree/master/stable/sonatype-nexus)
- [Choerodon Nexus3 🌟](https://hub.helm.sh/charts/choerodon/nexus3) Helm 3 compliant (Simpler and more secure than helm 2)
- [Sonar](https://github.com/helm/charts/tree/master/stable/sonarqube)
- [Selenium](https://github.com/helm/charts/tree/master/stable/selenium)
- [Jmeter](https://github.com/helm/charts/tree/master/stable/distributed-jmeter)
- [bitnami: create your first helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)
- [openshift.com: Introducing the Quarkus Helm Chart](https://www.openshift.com/blog/introducing-the-quarkus-helm-chart)
- [artifacthub.io: Official Helm charts for HAProxy and the HAProxy Kubernetes Ingress Controller on Artifact Hub 🌟](https://artifacthub.io/packages/search?repo=haproxytech)
- [prometheus-community.github.io: Prometheus Community Kubernetes Helm Charts 🌟](https://prometheus-community.github.io/helm-charts/)
- [boxunix.com: Developer’s Guide to Writing a Good Helm Chart](https://boxunix.com/2022/02/05/developers-guide-to-writing-a-good-helm-chart/)
- [HULL](https://github.com/vidispine/hull) The incredible HULL - Helm Uniform Layer Library - is a Helm library chart to improve Helm chart based workflows

## Shalm. Scriptable helm charts

- [shalm: Scriptable helm charts](https://github.com/wonderix/shalm) This project brings the starlark scripting language to helm charts.

## Helmfile

- https://helmfile.readthedocs.io Helmfile is a declarative spec for deploying Helm charts. It lets you:
    - Keep a directory of chart value files and maintain changes in version control
    - Apply CI/CD to configuration changes
    - Periodically sync to avoid skew in environments
- [github.com/helmfile/helmfile](https://github.com/helmfile/helmfile) Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases in one shot
- [linuxadvise.com: Helmfile - Next Level to manage your helm Charts](https://www.linuxadvise.com/amp/helmfile-next-level-to-manage-your-helm-charts)
- [kubesandclouds.com: Helmfile: turbocharging Helm](https://kubesandclouds.com/index.php/2020/12/16/helmfile/)

## Database Migrations

- [itnext.io: Database migrations on Kubernetes using Helm hooks](https://itnext.io/database-migrations-on-kubernetes-using-helm-hooks-fb80c0d97805)

## Helm Tools

- [redhat-certification: chart-verifier: Rules based tool to certify Helm charts 🌟](https://github.com/redhat-certification/chart-verifier)
- [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog)
- [helm-scanner](https://github.com/bridgecrewio/helm-scanner/) Open source IaC security scanner for public Helm charts. Helm-scanner is a tool designed to automate discovering, templating, security scanning, then recording and providing easy access to the results for publicly available Helm charts
- [helm-diff: Helm Diff Plugin](https://github.com/databus23/helm-diff)
- [Helmsman: Helm Charts as Code 🌟](https://github.com/Praqma/helmsman) Helmsman is a Helm Charts (k8s applications) as Code tool which allows you to automate the deployment/management of your Helm charts from version controlled code.
    - [medium: Gitops using Helmsman to apply Helm Charts to k8s](https://medium.com/@marco.franssen/gitops-using-helmsman-to-apply-helm-charts-to-k8s-1a7217ced411)
- [tellerops/helm-teller](https://github.com/tellerops/helm-teller) Helm Teller allows you to inject configuration and secrets from multiple providers into your chart while masking the secrets at the deployment
- [sstarcher/helm-exporter](https://github.com/sstarcher/helm-exporter) Exports helm release, chart, and version statistics in the prometheus format.
- [github.com/mumoshu/helm-x: Helm X Plugin](https://github.com/mumoshu/helm-x) Treat any Kustomization or K8s manifests directory as a Helm chart. No more "Kustomize vs Helm". Helm-x is a helm plugin that makes Helm better integrate with vanilla Kubernetes manifests, kustomize, and manual sidecar injections. With helm-x, you can install and sidecar-inject helm charts, manifests, kustomize apps in the same way.
- [maorfr/helm-backup: Helm Backup Plugin](https://github.com/maorfr/helm-backup) Helm plugin which performs backup/restore of releases in a namespace to/from a file
- [helmwave/helmwave](https://github.com/helmwave/helmwave) Helmwave is helm3-native tool for deploy your Helm Charts. HelmWave is like docker-compose for helm.
- [github.com/jkosik: helm-decomposer](https://github.com/jkosik/helm-decomposer) Decomposes Helm package and visualizes hierarchy of subcharts and images
- [github.com/projectsveltos: sveltosctl](https://github.com/projectsveltos/sveltosctl#display-outcome-of-clusterprofiles-in-dryrun-mode) A CLI to nicely display resources/helm charts deployed in CAPI Cluster by Sveltos. Collect tech-support from managed Kubernetes clusters sveltosctl nicely displays resources and Helm charts info in CAPI Kubernetes Clusters deployed using ClusterProfile. It also provides the ability to generate configuration snapshots and roll backs to a previously taken configuration snapshot.
- [abhaypore.medium.com: Migrate your manifest yaml files into Helm Chart](https://abhaypore.medium.com/migrate-your-manifest-yaml-files-into-helm-chart-32a44230f3b5)

## Helm Books

- [Learn Helm](https://www.packtpub.com/cloud-networking/learn-helm)

## Videos

??? note "Click to expand!"

    <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/-ykwb1d0DXU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9cwjtN3gkD4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/cZ1S2Gp47ng" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/CmPK93hg5w8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </center>

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">What is Three-way Strategic Merge Update in <a href="https://twitter.com/hashtag/Helm?src=hash&amp;ref_src=twsrc%5Etfw">#Helm</a>?<br><br>A 3-way merge reconciles a modified configuration with an original configuration while preserving any changes or deletions made to the original configuration in the interim.<br>more... 👇<a href="https://twitter.com/learnk8s?ref_src=twsrc%5Etfw">@learnk8s</a> <a href="https://twitter.com/hashtag/kubernetes?src=hash&amp;ref_src=twsrc%5Etfw">#kubernetes</a> <a href="https://twitter.com/hashtag/cncf?src=hash&amp;ref_src=twsrc%5Etfw">#cncf</a> <a href="https://twitter.com/hashtag/k8s?src=hash&amp;ref_src=twsrc%5Etfw">#k8s</a> <a href="https://twitter.com/hashtag/devops?src=hash&amp;ref_src=twsrc%5Etfw">#devops</a> <a href="https://t.co/HlmPeHG8On">pic.twitter.com/HlmPeHG8On</a></p>&mdash; Rahul Rai🌥️ (@rahulrai_in) <a href="https://twitter.com/rahulrai_in/status/1397768176297865221?ref_src=twsrc%5Etfw">May 27, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Truth is, most applications don&#39;t need complex automation hooks. You can go a long way with health checks, liveness probes, metrics, logs, and basic signal handling, which is why generic automation tools like Helm works well for most situations.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1435644371773186049?ref_src=twsrc%5Etfw">September 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Highway To Helm ! <a href="https://t.co/2UkS5kD4AG">pic.twitter.com/2UkS5kD4AG</a></p>&mdash; Sébastien Blanc 🇪🇺 🥑 (@sebi2706) <a href="https://twitter.com/sebi2706/status/1459204115481911310?ref_src=twsrc%5Etfw">November 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Artifact Hub is now able to check if Helm charts stored in OCI registries have been signed with 𝐜𝐨𝐬𝐢𝐠𝐧 from <a href="https://twitter.com/projectsigstore?ref_src=twsrc%5Etfw">@projectsigstore</a> 🔏🚀 <a href="https://t.co/DL6Z30U8Vu">pic.twitter.com/DL6Z30U8Vu</a></p>&mdash; Artifact Hub (@cncfartifacthub) <a href="https://twitter.com/cncfartifacthub/status/1462824128390606858?ref_src=twsrc%5Etfw">November 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
