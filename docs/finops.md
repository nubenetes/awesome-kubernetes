# Cloud FinOps. Collaborative, Real-Time Cloud Financial Management (CFM)

1. [Introduction](#introduction)
2. [Compute Cost Calculator](#compute-cost-calculator)
3. [AWS Cost Optimizations](#aws-cost-optimizations)
4. [Azure Cost Governance](#azure-cost-governance)
5. [Kubernetes Cost Optimization](#kubernetes-cost-optimization)
6. [Licence Managers](#licence-managers)
7. [EKS](#eks)
8. [Books](#books)
9. [Kubernetes Governance and Cost Management for the Cloud-Native Enterprise](#kubernetes-governance-and-cost-management-for-the-cloud-native-enterprise)
    1. [Replex](#replex)
10. [Cost Optimization Tools](#cost-optimization-tools)
11. [Tweets](#tweets)

## Introduction

- [FinOps Foundation: FinOps.org](https://www.finops.org/) Collaborative, Real-Time Cloud Financial Management
- [finops.org: What is FinOps?](https://www.finops.org/what-is-finops/)
- [deloitte.com: Matching cloud costs to need: Using FinOps for more effective cloud governance](https://www2.deloitte.com/us/en/pages/consulting/articles/using-finops-to-effectively-match-cloud-costs-to-value-for-cloud-professionals-podcast-automation-governance.html) Using FinOps to more effectively govern cloud usage and match cost to need to value can help organizations avoid potentially costly reactions, such as overprovisioning.
- [medium: DevOps, NoOps, and Now FinOps?](https://medium.com/better-programming/devops-noops-finops-64e0df91bcb8) Why do we need an accountant in IT?
- [padok.fr: FinOps, or the Culture of Cloud Cost Optimization](https://www.padok.fr/en/blog/finops-cloud)
- [slideshare: FinOps: A Culture Transformation to Bring DevOps, Finance and the Business Together - AWS Summit Sydney](https://es.slideshare.net/AmazonWebServices/finops-a-culture-transformation-to-bring-devops-finance-and-the-business-together-sponsored-by-cloudability-aws-summit-sydney)
- [aws.amazon.com: Introducing FinOps—Excuse Me, DevSecFinBizOps](https://aws.amazon.com/es/blogs/enterprise-strategy/introducing-finops-excuse-me-devsecfinbizops/)
- [devops.com: FinOps Foundation to Help Rein in Cloud Costs](https://devops.com/finops-foundation-to-help-rein-in-cloud-costs/)
- [infoq.com: Why Every DevOps Team Needs A FinOps Lead](https://www.infoq.com/articles/every-devops-team-needs-finops-lead/)
- [cncf.io: FinOps for Kubernetes: Insufficient – or nonexistent – Kubernetes cost monitoring is causing overspend](https://www.cncf.io/blog/2021/06/29/finops-for-kubernetes-insufficient-or-nonexistent-kubernetes-cost-monitoring-is-causing-overspend/)
- [loft.sh: The Cost of Managed Kubernetes - A Comparison 🌟](https://loft.sh/blog/the-cost-of-managed-kubernetes-a-comparison/)
- [thenewstack.io: 4 Reasons Your Cloud Operations Need a FinOps Team](https://thenewstack.io/4-reasons-your-cloud-operations-need-a-finops-team/)
- [faun.pub: FinOps – introduction, origins and next steps](https://faun.pub/finops-introduction-origins-and-next-steps-bcdaa8b82417) Financial Operations (FinOps) is a culture that will help you creating cost awareness in your organisation!
- [cloud.google.com: 5 key metrics to measure Cloud FinOps impact in your organization in 2022 and beyond](https://cloud.google.com/blog/topics/cloud-first/key-metrics-to-measure-impact-of-cloud-finops)
- [thenewstack.io: Cloud Cost Management for DevOps](https://thenewstack.io/cloud-cost-management-for-devops)
- [zdnet.com: As cloud costs spiral upward, enterprises turn to a thing called FinOps](https://www.zdnet.com/article/as-cloud-costs-spiral-upward-enterprises-turn-to-a-thing-called-finops/) Organizations waste 32% of cloud spend, up from 30% a year ago. 'More and more users are swimming in the FinOps side of the pool, even if they may not know it - or call it FinOps yet.'
- [thenewstack.io: Tricks for Cloud Cost Optimization | Pavan Belagatti](https://thenewstack.io/tricks-for-cloud-cost-optimization)
- [venturebeat.com: Cloud costs are unmanageable: It’s time we standardize billing](https://venturebeat.com/datadecisionmakers/cloud-costs-are-unmanageable-its-time-we-standardize-billing/)
- [medium.com/@pratzy99: Adoption of FinOps for Kubernetes Cost Optimization 🌟](https://medium.com/@pratzy99/adoption-of-finops-for-kubernetes-cost-optimization-6263bc7b3f57)
- AWS Tip 💛 Avoid billing surprises:
    - Avoid billing surprises 💸
    - 𝗿𝗲𝘃𝗶𝗲𝘄 𝗰𝗼𝘀𝘁𝘀 (bi-)weekly
    - get familiar with 𝗔𝗪𝗦 𝗖𝗼𝘀𝘁 𝗲𝘅𝗽𝗹𝗼𝗿𝗲𝗿
    - set up 𝗯𝗶𝗹𝗹𝗶𝗻𝗴 𝗮𝗹𝗲𝗿𝘁𝘀
    - understand your cost 𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲: which services contribute significantly to your costs?
- [hystax.com: The difference between cloud cost management and FinOps](https://hystax.com/the-difference-between-cloud-cost-management-and-finops/)
- [infoworld.com: Are we experiencing cloudflation?](https://www.infoworld.com/article/3674048/are-we-experiencing-cloudflation.html) The sticker shock of cloud computing bills has many in the C-suite looking for answers. A solid finops program can close the budget holes and pay for itself.
- [edgebricks.com: Why Public Clouds Get So Expensive Over Time 🌟](https://edgebricks.com/why-public-clouds-get-so-expensive-over-time/)
- [aws.amazon.com: Four Principles of Cloud Financial Management Small and Medium Business Owners Need to Know](https://aws.amazon.com/blogs/smb/four-principles-of-cloud-financial-management-small-and-medium-business-owners-need-to-know/)
- [logz.io: FinOps Observability: Monitoring Kubernetes Cost](https://logz.io/blog/finops-observability-monitoring-kubernetes-cost/)
- [medium.com/adeo-tech: How to save money fast with Kubernetes — Do FinOps](https://medium.com/adeo-tech/how-to-save-money-fast-with-kubernetes-do-finops-3a9cafc9beba) In this article, you will learn how to reduce your cloud bill and some tips on cloud infrastructure optimization
- [infoworld.com: Kubernetes cost management for the real world](https://www.infoworld.com/article/3695569/kubernetes-cost-management-for-the-real-world.html) How much will Kubernetes cost to run? That question has become much easier to answer for Azure Kubernetes Service, thanks to OpenCost integration.
- [infoworld.com: When finops costs you more in the end](https://www.infoworld.com/article/3688332/when-finops-costs-you-more-in-the-end.html) Cloud finops can save you tons of money on cloud spending and return more value to the business. Unfortunately, mistakes are costing companies big time.
- [infoworld.com: Kubernetes costs less, but less than what?](https://www.infoworld.com/article/3696277/kubernetes-costs-less-but-less-than-what.html) Sure, compared to traditional IT, Kubernetes is great, but not much will beat public cloud in the long run.
- [bitsand.cloud: Slashing Data Transfer Costs in AWS by 99%](https://www.bitsand.cloud/posts/slashing-data-transfer-costs/)

## Compute Cost Calculator

- https://compute-cost.com 🌟
- This tool finds the lowest price of compute resources from different services (currently just in AWS). To balance simplicity and utility, only the most common features are available as filters.
- "As an AWS user, I often want to know the cheapest options for compute resources given some project-specific criteria. So, I made a tool to show me that data in a way that is useful to me. Maybe it will be useful to you" @ericwastl

## AWS Cost Optimizations

- [medium.com/@tarunbehal02: AWS Cost Optimizations : My Learnings](https://medium.com/@tarunbehal02/aws-cost-optimizations-my-learnings-fcdc14da1f58)
- [aws.amazon.com/blogs/architecture: Overview of Data Transfer Costs for Common Architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/)

## Azure Cost Governance

- [==github.com/dolevshor/azure-finops-guide: The Azure FinOps Guide== 🌟](https://github.com/dolevshor/azure-finops-guide) Centralizes Azure FinOps information and tools to enabling a better understanding and optimization of cloud costs
- [info.microsoft.com: The Road to Azure Cost Governance](https://info.microsoft.com/ww-landing-the-road-to-azure-cost-governance-e-book.html) Learn how to gain full control of your Azure costs by creating a continuous cost governance and optimization process. This comprehensive Packt e-book covers essential topics like cloud cost management and sustainable modeling of cloud expenses.
- [==github.com/mivano/azure-cost-cli==](https://github.com/mivano/azure-cost-cli) CLI tool to perform cost analysis on your Azure subscription
    - [github.com/mivano/azure-cost-cli: Cost by tag](https://github.com/mivano/azure-cost-cli#cost-by-tag)
- [==techcommunity.microsoft.com: Azure Savings Dashboard== 🌟](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/azure-savings-dashboard/ba-p/3816131)
- [https://learn.microsoft.com: View Kubernetes costs (AKS)](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/view-kubernetes-costs)
- [techcommunity.microsoft.com: Azure Pricing: How to navigate Azure pricing options and resources 🌟](https://techcommunity.microsoft.com/t5/azure-governance-and-management/azure-pricing-how-to-navigate-azure-pricing-options-and/ba-p/4166276)
- [techcommunity.microsoft.com: Azure Pricing: How to estimate Azure project costs 🌟](https://techcommunity.microsoft.com/t5/azure-governance-and-management/azure-pricing-how-to-estimate-azure-project-costs/ba-p/4166297)
- [techcommunity.microsoft.com: Identify your savings potential in Azure 🌟](https://techcommunity.microsoft.com/t5/finops-blog/identify-your-savings-potential-in-azure/ba-p/4131194)

## Kubernetes Cost Optimization

- [medium.com/armory: Continuous Cost Optimization for Kubernetes](https://medium.com/armory/continuous-cost-optimization-for-kubernetes-4361045f0215)
- [==learnk8s/xlskubectl==](https://github.com/learnk8s/xlskubectl) A spreadsheet to control your Kubernetes cluster. xlskubectl integrates Google Spreadsheet with Kubernetes. You can finally administer your cluster from the same spreadsheet that you use to track your expenses.
- [==medium.com/empathyco: Cloud FinOps — Part 4: Kubernetes Cost Report==](https://medium.com/empathyco/cloud-finops-part-4-kubernetes-cost-report-b4964be02dc3) In this article, you will learn how to build your own Kubernetes cost explorer dashboard using Prometheus and Grafana.
- [==medium.com/@danielepolencic: In Kubernetes, are there hidden costs to running many cluster nodes?==](https://medium.com/@danielepolencic/reserved-cpu-and-memory-in-kubernetes-nodes-65aee1946afd) Yes, since not all CPU and memory in your Kubernetes nodes can be used to run Pods.
- [medium.com/develeap: Cutting down Kubernetes Costs: Cast.ai vs. Karpenter](https://medium.com/develeap/cutting-down-kubernetes-costs-cast-ai-vs-karpenter-20f6788b4c67)
- [engineering.razorpay.com: The Culture of Cost Optimization — Reducing Kubernetes cost by $300,000](https://engineering.razorpay.com/the-culture-of-cost-optimization-reducing-kubernetes-cost-by-300-000-32611cdd19d9)
- [infoworld.com: 5 steps to bringing Kubernetes costs in line](https://www.infoworld.com/article/3693050/5-steps-to-bringing-kubernetes-costs-in-line.html)
- [medium.com/@suleimanabualrob: Kubernetes cost optimisation](https://medium.com/@suleimanabualrob/kubernetes-cost-optimisation-9e81b76814f6) In this article, you'll discuss resource over-provisioning in Kubernetes and learn some tips to improve utilisation to save money and have a well-architected workload
- [itnext.io: Kubernetes Cost Optimization Made Easy: Efficient Tools for Streamlining FinOps](https://itnext.io/kubernetes-cost-optimization-made-easy-efficient-tools-for-streamlining-finops-be0b6a54d2bb)
- [thenewstack.io: Grafana Wants to Help You Avoid Getting Dinged by Kubernetes Costs](https://thenewstack.io/grafana-wants-to-help-you-avoid-getting-dinged-by-kubernetes-costs/) Grafana introduces new infrastructure and cost monitoring capabilities in Grafana Cloud.

## Licence Managers

- [marketplace.atlassian.com:  License Manager - Easily track your software licenses](https://marketplace.atlassian.com/apps/1227641/license-manager-easily-track-your-software-licenses) Unified view of software usage, SaaS, cloud resources, domains, SSL certificates info across the enterprise from one place in Jira.

## EKS

- [dev.to: FinOps EKS: 10 tips to reduce the bill up to 90% on AWS managed Kubernetes clusters](https://dev.to/zenika/eks-10-tips-to-reduce-the-bill-up-to-90-on-aws-managed-kubernetes-clusters-epe)
- [aws.amazon.com: Understanding and Cost Optimizing Amazon EKS Control Plane Logs](https://aws.amazon.com/blogs/containers/understanding-and-cost-optimizing-amazon-eks-control-plane-logs/) This post describes different EKS log types and ways to optimize costs. Understanding the levers available for consuming logs not only helps you in optimizing costs but also allows you to focus on the root causes analysis and attribution.

## Books

- [Cloud FinOps O’Reilly Book](https://www.finops.org/cloud-finops-oreilly-book/)

## Kubernetes Governance and Cost Management for the Cloud-Native Enterprise

- [medium.com/compass-true-north: Halving Kubernetes Compute Costs With Vertical Pod Autoscaler](https://medium.com/compass-true-north/halving-kubernetes-compute-costs-with-vertical-pod-autoscaler-df658c043301) In this article, you'll learn how the team at Compass managed to reduce the need for over 50 per cent of the total nodes in each cluster (halving their compute costs) by using the vertical pod autoscaler

### Replex

- [replex.io](https://www.replex.io/)
- [replex.io: An Introduction to Kubernetes FinOps](https://www.replex.io/blog/an-introduction-to-kubernetes-finops) FinOps is a cross domain discipline that represents a set of tools, best practices and processes aimed towards making software and infrastructure more cost effective. In this article we provide an introduction to Kubernetes Finops.

## Cost Optimization Tools

- [CAST AI](https://cast.ai/) cuts your cloud bill automatically so engineers can focus on building a better product
- [cremich/cdk-bill-bot: Welcome to Bill - the cost optimization bot](https://github.com/cremich/cdk-bill-bot) The serverless cost optimization bot. Bill enables AWS customers to proactively monitor their infrastructure costs and identify unforeseen expenses in a timely manner. Bill wants to prevent AWS customers from receiving bad surprises in their monthly bill. Therefore he addresses two primary problem areas:
    - Cost history is not monitored on a regular basis
    - Basic cost optimization best practices are not setup
- [thenewstack.io: Finout Gets a Handle on Kubernetes Costs](https://thenewstack.io/finout-gets-a-handle-on-kubernetes-costs/) Finout has expanded its cost analysis platform for enterprise software to Kubernetes, providing a way to understand the costs of running the open source orchestration tool.

## Tweets

??? note "Click to expand!"

	<center>
	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Q: What is FinOps Architect job in Cloud?<br>This has got very popular on Public cloud to manage companies - Cloud Financial Management. <br><br>Here&#39;s how you can be a Cloud FinOps Consultant<br>🧵1/?<br>1. Learn architecture well</p>&mdash; Satyen Kumar (@SatyenKumar) <a href="https://twitter.com/SatyenKumar/status/1498705725874483205?ref_src=twsrc%5Etfw">March 1, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🏗 AWS Tip 💛<br><br>Avoid billing surprises 💸<br><br>• 𝗿𝗲𝘃𝗶𝗲𝘄 𝗰𝗼𝘀𝘁𝘀 (bi-)weekly<br>• get familiar with 𝗔𝗪𝗦 𝗖𝗼𝘀𝘁 𝗲𝘅𝗽𝗹𝗼𝗿𝗲𝗿<br>• set up 𝗯𝗶𝗹𝗹𝗶𝗻𝗴 𝗮𝗹𝗲𝗿𝘁𝘀<br>• understand your cost 𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲: which services contribute significantly to your costs?</p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1551934589945450501?ref_src=twsrc%5Etfw">July 26, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">In Kubernetes, are there hidden costs to running many cluster nodes?<br><br>Let me explain… (spoiler: yes) <a href="https://t.co/ErYdu8JR5E">pic.twitter.com/ErYdu8JR5E</a></p>&mdash; Daniele Polencic (@danielepolencic) <a href="https://twitter.com/danielepolencic/status/1584893971544915968?ref_src=twsrc%5Etfw">October 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </center>
