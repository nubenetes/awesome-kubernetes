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
- [codefresh.io: Using Helm 3 with Helm 2 charts](https://codefresh.io/helm-tutorial/taking-helm-3-spin/)
- [helm.sh: How to migrate from Helm v2 to Helm v3](https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3/)
- [Helm 3: Validating Helm Chart Values with JSON Schemas 🌟](https://www.arthurkoziel.com/validate-helm-chart-values-with-json-schemas/)
- [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2)
- [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
- [dev.to: Introduction to Helm 🌟](https://dev.to/edlegaultle/introduction-to-helm-50jl)
- [jfrog.com: Steering Straight with Helm Charts Best Practices 🌟](https://jfrog.com/blog/helm-charts-best-practices/)
- [youtube.com: Demystifying Helm 🌟](https://www.youtube.com/watch?v=2HPsPOwHOlY&ab_channel=DonovanBrown)
- [harness.io: Introduction to Helm: Charts, Deployments, & More 🌟](https://harness.io/blog/continuous-delivery/what-is-helm/)
- [freecodecamp.org: What is a Helm Chart? A Tutorial for Kubernetes Beginners](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners)
- [youtube: GitOps Guide to the Galaxy: Working with Helm](https://www.youtube.com/watch?v=1FzOlSed5ts&ab_channel=OpenShift)
- [blog.heyal.co.uk: How to unit-test your helm charts with Golang 🌟](https://blog.heyal.co.uk/unit-testing-helm-charts/) Learn how to write Golang unit tests for your Helm charts to keep quality high and make changes with confidence.
- [redhat.com: Red Hat OpenShift Certification extends support for Kubernetes-native technologies with Helm 🌟](https://www.redhat.com/en/blog/red-hat-openshift-certification-extends-support-kubernetes-native-technologies-helm) __Helm or Operators: how to choose__
- [blog.flant.com: Making the most out of Helm templates 🌟](https://blog.flant.com/advanced-helm-templating/) The standard Helm library and traditional approaches to creating Helm charts are generally okay to automate non-complex tasks. But the growing complexity and number of Helm charts rapidly make the minimalistic Helm templates and controversial standard Helm library insufficient. In this article, we will show you how to make your Helm templates much more flexible and dynamic by implementing your own Helm “functions” and exploiting the capabilities of the tpl function.
- [thenewstack.io: Upgrade Helm if You Don’t Want to Share Your Username and Password (Helm’s CVE-2021-32690) 🌟](https://thenewstack.io/upgrade-helm-if-you-dont-want-to-share-your-username-and-password/)
- [thedeveloperstory.com: Helm 101: Brief introduction to kubernetes package manager](https://thedeveloperstory.com/2021/07/12/helm-101-brief-introduction-to-kubernetes-package-manager/)
- if you're having either https://github.com/helm/helm/issues/10005 or https://github.com/helm/helm/issues/10004, it's because the older Helm 2 backing store is finally gone. You REALLY should upgrade to Helm 3, and now. You're risking your security more than you should.
- [cloud.redhat.com: Application Management in Kubernetes Environments with Helm Charts and Kubernetes Operators](https://cloud.redhat.com/blog/application-management-in-kubernetes-environments-with-helm-charts-and-kubernetes-operators)
- [codersociety.com: 13 Best Practices for using Helm](https://codersociety.com/blog/articles/helm-best-practices) Helm is an indispensable tool for deploying applications to Kubernetes clusters. But it is only by following best practices that you’ll truly reap the benefits of Helm. Here are 13 best practices to help you create, operate, and upgrade applications using Helm.
- [codefresh.io: Using Helm with GitOps 🌟](https://codefresh.io/helm-tutorial/using-helm-with-gitops/)
- [==learn.hashicorp.com: Deploy a Helm-based application automatically with GitOps==](https://learn.hashicorp.com/tutorials/waypoint/gitops-helm-deployment)
- [==apiiro.com: Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments==](https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments/)
- [==dev.to/francoislp: Post-mortem: 1h30 downtime on a Saturday morning==](https://dev.to/francoislp/post-mortem-1h30-downtime-on-a-saturday-morning-5af0) Read how 4 YAML lines brought down 3 APIs for 1h30 on a Saturday morning. In the end, the issue was a Helm chart misconfiguration where 2 settings were conflicting with each other.
    - Common vs multiple Helm charts
    - Values YAML hierarchy
    - Git repository management
- [community.ops.io: [K8s] Fix Helm release failing with an upgrade still in progress](https://community.ops.io/the_cozma/k8s-fix-helm-release-failing-with-an-upgrade-still-in-progress-4660) This article applies to: Helm v3.8.0. If you use Helm to manage your releases, you might end up in a case where the release is stuck in a pending state and all subsequent releases keep failing. This article explains how to fix it with two options:
    - Helm rollback
    - Deleting the state
- [dev.to: HULL Tutorial 01: Introducing HULL, the Helm Universal Layer Library](https://dev.to/gre9ory/hull-tutorial-01-introducing-hull-the-helm-universal-layer-library-4njb)
- [dev.to: Helm Release Time-To-Live(TTL)⏳💀 for Temporary Environments](https://dev.to/rtpro/helm-release-time-to-livettl-for-temporary-environments-1239) When working with Kubernetes, it’s often the case that you’ll need to create temporary environments/namespaces. You might need this as a way to limit the resources use, handle dev/staging environments, or just as a way to contain your tests while working on them. If you have used Helm before, you know that installing applications via Helm charts is simple by using the helm install command. The problem is that after installing a package, you or the user still needs to manually delete the package. With this in mind, we are going to explore how we set Time-To-Live Expiration for helm releases via the Helm release plugin, and create temporary Environments with Time-To-Live to make our lives easier with Helm.
- [sysdig.com: Helm security and best practices](https://sysdig.com/blog/how-to-secure-helm/)
    - Overriding values from a parent chart
    - Making child chart data available to the parent chart
    - Global chart values
    - Sharing templates with subcharts

- [blog.knell.it: Making your Helm Chart observable for Prometheus](https://blog.knell.it/making-your-helm-chart-observable-for-prometheus/) In this blog post, I walk you through the various steps required to make an existing Helm chart observable by Prometheus.
- [==mattias.engineer/courses/kubernetes/helm: Kubernetes-101: Helm== 🌟](https://mattias.engineer/courses/kubernetes/helm/)

## Helm Plugins

- [Helm Diff Plugin 🌟](https://github.com/databus23/helm-diff) A helm plugin that shows a diff explaining what a helm upgrade would change
- [Helm Kanvas Snapshot](https://github.com/meshery/helm-kanvas-snapshot) Plugin that generates a visual snapshot of Helm charts.
- [Helm mapkubeapis Plugin](https://github.com/helm/helm-mapkubeapis) This is a Helm plugin which map deprecated or removed Kubernetes APIs in a release to supported APIs. __With kubernetes 1.22 dropping support for more beta APIs, you might be in need of a helmpack plugin to help you with that..__
- [JovianX/helm-release-plugin](https://github.com/JovianX/helm-release-plugin) Helm3 plugin that pulls(re-creates) helm Charts from deployed releases, and updates values of deployed releases without the chart.

## Helm Chart Documentation

- [chart-doc-gen: Helm Chart Documentation Generator](https://github.com/kubepack/chart-doc-gen)
- [Frigate](https://frigate.readthedocs.io/) is a tool for automatically generating documentation for your Helm charts. It will use the chart’s Chart.yaml and values.yaml files in order to generate the content in a markup language of your choice.
- [rafay.co: Helm Chart Hooks Tutorial](https://rafay.co/the-kubernetes-current/helm-chart-hooks-tutorial/)
- [thenewstack.io: Applying Kubernetes Security Best Practices to Helm Charts 🌟](https://thenewstack.io/applying-kubernetes-security-best-practices-to-helm-charts/)
- [helm-docs](https://github.com/norwoodj/helm-docs) The `helm-docs` tool auto-generates documentation from helm charts into markdown files. The resulting files contain metadata about their respective chart and a table with each of the chart's values, their defaults, and an optional description parsed from comments.

## Helm Dashboard

- [github.com/komodorio/helm-dashboard 🌟](https://github.com/komodorio/helm-dashboard) The Helm Dashboard plugin offers a UI-driven way to view the installed Helm charts, and see their revision history and corresponding Kubernetes resources. Also, you can perform simple actions like roll back to a revision or upgrade to a newer version

## Kubecrt

- [Kubecrt](https://github.com/blendle/kubecrt)

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
- [Artifact Hub 🌟](https://artifacthub.io/) Find, install and publish Kubernetes packages
- [KubeApps Hub](https://hub.kubeapps.com/)
- [github: Nova 🌟](https://github.com/fairwindsops/nova) Find outdated or deprecated Helm charts running in your cluster.
- [github: Kubernetes Deployment Orchestrator](https://github.com/SAP/kubernetes-deployment-orchestrator) This project brings the starlark scripting language to helm charts.
- [harness.io: Tutorial: Turning a GitHub Repo Into a Helm Chart Repo](https://harness.io/blog/devops/helm-chart-repo/)

## Helm Charts

- [Jenkins](https://github.com/helm/charts/tree/master/stable/jenkins)
- [Nexus3](https://github.com/helm/charts/tree/master/stable/sonatype-nexus)
- [Choerodon Nexus3 🌟](https://hub.helm.sh/charts/choerodon/nexus3) Helm 3 compliant (Simpler and more secure than helm 2)
- [Sonar](https://github.com/helm/charts/tree/master/stable/sonarqube)
- [Selenium](https://github.com/helm/charts/tree/master/stable/selenium)
- [Jmeter](https://github.com/helm/charts/tree/master/stable/distributed-jmeter)
- [openshift.com: Introducing the Quarkus Helm Chart](https://www.openshift.com/blog/introducing-the-quarkus-helm-chart)
- [artifacthub.io: Official Helm charts for HAProxy and the HAProxy Kubernetes Ingress Controller on Artifact Hub 🌟](https://artifacthub.io/packages/search?repo=haproxytech)
- [prometheus-community.github.io: Prometheus Community Kubernetes Helm Charts 🌟](https://prometheus-community.github.io/helm-charts/)
- [boxunix.com: Developer’s Guide to Writing a Good Helm Chart](https://boxunix.com/2022/02/05/developers-guide-to-writing-a-good-helm-chart/)
- [HULL](https://github.com/vidispine/hull) The incredible HULL - Helm Uniform Layer Library - is a Helm library chart to improve Helm chart based workflows

## Shalm. Scriptable helm charts


## Helmfile

- https://helmfile.readthedocs.io Helmfile is a declarative spec for deploying Helm charts. It lets you:
    - Keep a directory of chart value files and maintain changes in version control
    - Apply CI/CD to configuration changes
    - Periodically sync to avoid skew in environments
- [github.com/helmfile/helmfile](https://github.com/helmfile/helmfile) Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases in one shot

## Database Migrations


## Helm Tools

- [redhat-certification: chart-verifier: Rules based tool to certify Helm charts 🌟](https://github.com/redhat-certification/chart-verifier)
- [helm-changelog: Create changelogs for Helm Charts, based on git history](https://github.com/mogensen/helm-changelog)
- [helm-scanner](https://github.com/bridgecrewio/helm-scanner/) Open source IaC security scanner for public Helm charts. Helm-scanner is a tool designed to automate discovering, templating, security scanning, then recording and providing easy access to the results for publicly available Helm charts
- [Helmsman: Helm Charts as Code 🌟](https://github.com/Praqma/helmsman) Helmsman is a Helm Charts (k8s applications) as Code tool which allows you to automate the deployment/management of your Helm charts from version controlled code.
- [tellerops/helm-teller](https://github.com/tellerops/helm-teller) Helm Teller allows you to inject configuration and secrets from multiple providers into your chart while masking the secrets at the deployment
- [sstarcher/helm-exporter](https://github.com/sstarcher/helm-exporter) Exports helm release, chart, and version statistics in the prometheus format.
- [github.com/mumoshu/helm-x: Helm X Plugin](https://github.com/mumoshu/helm-x) Treat any Kustomization or K8s manifests directory as a Helm chart. No more "Kustomize vs Helm". Helm-x is a helm plugin that makes Helm better integrate with vanilla Kubernetes manifests, kustomize, and manual sidecar injections. With helm-x, you can install and sidecar-inject helm charts, manifests, kustomize apps in the same way.
- [maorfr/helm-backup: Helm Backup Plugin](https://github.com/maorfr/helm-backup) Helm plugin which performs backup/restore of releases in a namespace to/from a file
- [helmwave/helmwave](https://github.com/helmwave/helmwave) Helmwave is helm3-native tool for deploy your Helm Charts. HelmWave is like docker-compose for helm.
- [github.com/jkosik: helm-decomposer](https://github.com/jkosik/helm-decomposer) Decomposes Helm package and visualizes hierarchy of subcharts and images
- [github.com/projectsveltos: sveltosctl](https://github.com/projectsveltos/sveltosctl#display-outcome-of-clusterprofiles-in-dryrun-mode) A CLI to nicely display resources/helm charts deployed in CAPI Cluster by Sveltos. Collect tech-support from managed Kubernetes clusters sveltosctl nicely displays resources and Helm charts info in CAPI Kubernetes Clusters deployed using ClusterProfile. It also provides the ability to generate configuration snapshots and roll backs to a previously taken configuration snapshot.

## Helm Books


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