# Helm Kubernetes Tool
- [Helm](#helm)
- [Helm Chart Documentation](#helm-chart-documentation)
- [Kubecrt](#kubecrt)
- [Helm Charts repositories](#helm-charts-repositories)
- [Helm Charts](#helm-charts)
- [Helmfile](#helmfile)
- [Database Migrations](#database-migrations)
- [Helm Books](#helm-books)

## Helm
* [thoughtworks.com: Helm](https://www.thoughtworks.com/radar/tools/helm)
* [helm.sh](https://helm.sh/)
    * [helm.sh/docs](https://helm.sh/docs) 
* [GitHub: Helm, the Kubernetes Package Manager](https://github.com/helm/helm) Installing and managing Kubernetes applications
* [Helm and Kubernetes Tutorial - Introduction](https://www.youtube.com/watch?v=9cwjtN3gkD4)
* [Delve into Helm: Advanced DevOps](https://www.youtube.com/watch?v=cZ1S2Gp47ng)
* [Continuously delivering apps to Kubernetes using Helm](https://www.youtube.com/watch?v=CmPK93hg5w8)
* [Zero to Kubernetes CI/CD in 5 minutes with Jenkins and Helm](https://www.youtube.com/watch?v=eMOzF_xAm7w)
* [DevOps with Azure, Kubernetes, and Helm](https://www.youtube.com/watch?v=INv-VCZvM_o)
* [dzone: the art of the helm chart patterns](https://dzone.com/articles/the-art-of-the-helm-chart-patterns-from-the-offici)
* [dzone: 15 useful helm chart tools](https://dzone.com/articles/15-useful-helm-charts-tools)
* [dzone: create install upgrade and rollback a helm chart - part 1](https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p)
* [dzone: create install upgrade and rollback a helm chart - part 2](https://dzone.com/articles/create-install-upgrade-rollback-a-helm-chart-part)
* [dzone: cicd with kubernetes and helm](https://dzone.com/articles/cicd-with-kubernetes-and-helm)
* [dzone: do you need helm?](https://dzone.com/articles/do-you-need-helm)
* [dzone: managing helm releases the gitops way](https://dzone.com/articles/managing-helm-releases-the-gitops-way)
* [codefresh.io: Using Helm 3 with Helm 2 charts](https://codefresh.io/helm-tutorial/taking-helm-3-spin/)
* [banzaicloud.com: Helm 3, the Good, the Bad and the Ugly](https://banzaicloud.com/blog/helm3-the-good-the-bad-and-the-ugly/)
* [helm.sh: How to migrate from Helm v2 to Helm v3](https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3/)
* [Helm 3: Validating Helm Chart Values with JSON Schemas 🌟](https://www.arthurkoziel.com/validate-helm-chart-values-with-json-schemas/)
* [hackernoon.com: Kubernetes and Helm: A Deadly Combo to Help You Deploy with Ease](https://hackernoon.com/kubernetes-and-helm-a-deadly-combo-to-help-you-deploy-with-ease-rjr30x2)
* [medium: Helm Chart — Development Guide 🌟](https://medium.com/swlh/helm-chart-development-guide-bbc525d3b448) Writing maintainable and reliable charts with few tricks
* [medium: Multi-namespace Helm deploy in Kubernetes](https://medium.com/analytics-vidhya/multi-namespace-helm-deploy-in-kubernetes-26d1baf1ca5c)
* [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
* [daveops.xyz: Running DB migrations on Kubernetes with Helm](https://daveops.xyz/en/2020/09/18/running-db-migrations-on-kubernetes-with-helm/)
* [itnext.io: Database migrations on Kubernetes using Helm hooks](https://itnext.io/database-migrations-on-kubernetes-using-helm-hooks-fb80c0d97805)
* [mbbaig.blog: How to create custom Helm charts 🌟](https://mbbaig.blog/how-to-create-custom-helm-charts/)
* [medium: Using Helm with Amazon EKS without kubeconfigs](https://medium.com/analytics-vidhya/using-helm-with-amazon-eks-without-a-kubeconfig-733f44a31b1d)
* [dev.to: Introduction to Helm 🌟](https://dev.to/edlegaultle/introduction-to-helm-50jl)
* [itnext.io: Helm 3 Umbrella Charts & Standalone Chart Image Tags — An Alternative Approach](https://itnext.io/helm-3-umbrella-charts-standalone-chart-image-tags-an-alternative-approach-78a218d74e2d) Helm umbrella charts, for those who aren’t familiar, describe and encapsulate a deployable collection of loosely couple Kubernetes components as a higher-order Helm chart. In other words, a collection of software elements that each have their own individual charts but, for whatever reason (e.g. design choices, ease of deployability, versioning complexities), must be installed or upgraded as a since atomic unit.
* [rancher.com: Create Reproducible Security in Kubernetes with Helm 3 and Helm Charts](https://rancher.com/blog/2020/helm-security)
* [itnext.io: Database migrations on Kubernetes using Helm hooks](https://itnext.io/database-migrations-on-kubernetes-using-helm-hooks-fb80c0d97805)
* [jfrog.com: Steering Straight with Helm Charts Best Practices 🌟](https://jfrog.com/blog/helm-charts-best-practices/)

## Helm Chart Documentation
* [chart-doc-gen: Helm Chart Documentation Generator](https://github.com/kubepack/chart-doc-gen)
* [Frigate](https://frigate.readthedocs.io/) is a tool for automatically generating documentation for your Helm charts. It will use the chart’s Chart.yaml and values.yaml files in order to generate the content in a markup language of your choice.

## Kubecrt
* [Kubecrt](https://github.com/blendle/kubecrt)
* [Kubecrt - Convert HELM charts to kubernetes resources 🌟](https://toolbox.kali-linuxtr.net/kubecrt-convert-helm-charts-to-kubernetes-resources.tool)

## Helm Charts repositories
* [codeengineered.com: 4 Places To Find Helm Charts](https://codeengineered.com/blog/2020/helm-find-charts/)
* [hub.helm.sh 🌟](http://hub.helm.sh) -> [artifacthub.io 🌟](https://artifacthub.io/) Find, install and publish
Kubernetes packages
    * [New Location For Stable and Incubator Charts](https://helm.sh/blog/new-location-stable-incubator-charts/)
    * [charts.helm.sh/stable 🌟](https://charts.helm.sh/stable)
    * [charts.helm.sh/incubator 🌟](https://charts.helm.sh/incubator/)
* [Bitnami Helm Charts](https://bitnami.com/stacks/helm)
* [JFrog ChartCenter](https://chartcenter.io/)
    * [Navigating Kubernetes With Helm 3 Charts and ChartCenter 🌟](https://dzone.com/articles/navigating-kubernetes-with-helm-3-charts-and-chart) ChartCenter is a free central repository for discovering Helm Charts, created to help manage your Kubernetes applications 
* [Artifact Hub](https://artifacthub.io/)
* [KubeApps Hub](https://hub.kubeapps.com/)

## Helm Charts
* [Jenkins](https://github.com/helm/charts/tree/master/stable/jenkins) 
* [Codecentric Jenkins 🌟](https://github.com/codecentric/helm-charts/tree/master/charts/jenkins) Helm 3 compliant (Simpler and more secure than helm 2)
* [Nexus3](https://github.com/helm/charts/tree/master/stable/sonatype-nexus)
* [Choerodon Nexus3 🌟](https://hub.helm.sh/charts/choerodon/nexus3) Helm 3 compliant (Simpler and more secure than helm 2)
* [Sonar](https://github.com/helm/charts/tree/master/stable/sonarqube)
* [Selenium](https://github.com/helm/charts/tree/master/stable/selenium)
* [Jmeter](https://github.com/helm/charts/tree/master/stable/distributed-jmeter)
* [bitnami: create your first helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)

## Helmfile
- [helmfile](https://github.com/linuxadvise/helmfile)
- [linuxadvise.com: Helmfile - Next Level to manage your helm Charts](https://www.linuxadvise.com/amp/helmfile-next-level-to-manage-your-helm-charts)

## Database Migrations
- [itnext.io: Database migrations on Kubernetes using Helm hooks](https://itnext.io/database-migrations-on-kubernetes-using-helm-hooks-fb80c0d97805)

## Helm Books
- [Learn Helm](https://www.packtpub.com/cloud-networking/learn-helm)
