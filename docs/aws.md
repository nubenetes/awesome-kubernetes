# Public Cloud Provider. Amazon Web Services
<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/aws.png">
</p>
<br/>
<!-- MarkdownTOC -->

- [Amazon Web Services](#amazon-web-services)
- [Blogs](#blogs)
- [AWS Free Resources](#aws-free-resources)
- [Introduction](#introduction)
	- [Books](#books)
- [Training](#training)
- [AWS Certification](#aws-certification)
- [AWS Glossary](#aws-glossary)
- [Awesome AWS](#awesome-aws)
- [AWS Marketplace](#aws-marketplace)
- [AWS Pricing](#aws-pricing)
	- [AWS Calculator](#aws-calculator)
- [AWS on Twitter](#aws-on-twitter)
- [AWS Architecture](#aws-architecture)
- [AWS Youtube channel and Podcasts](#aws-youtube-channel-and-podcasts)
- [Closed groups for AWS certified professionals](#closed-groups-for-aws-certified-professionals)
- [AWS Architecture Blog, Official Blog, AWS Labs, AWS Quick Start](#aws-architecture-blog-official-blog-aws-labs-aws-quick-start)
- [AWS Case Studies](#aws-case-studies)
- [AWS tips. AWS Performance. Handling AWS Failures and Outages](#aws-tips-aws-performance-handling-aws-failures-and-outages)
- [AWS Clients](#aws-clients)
- [AWS New Features](#aws-new-features)
- [AWS Management Console](#aws-management-console)
- [AWS Management Tools Blog](#aws-management-tools-blog)
- [AWS Cloudwatch](#aws-cloudwatch)
- [AWS Schema Conversion Tool](#aws-schema-conversion-tool)
- [AWS RDS](#aws-rds)
	- [AWS DMS](#aws-dms)
	- [AWS RDS Proxy](#aws-rds-proxy)
- [AWS Application Discovery Service](#aws-application-discovery-service)
- [AWS Migrations](#aws-migrations)
	- [AWS Database Migration Service](#aws-database-migration-service)
- [AWS Redshift](#aws-redshift)
- [AWS DevOps. AWS CodePipeline](#aws-devops-aws-codepipeline)
- [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
- [AWS OpsWorks](#aws-opsworks)
- [AWS Networking](#aws-networking)
- [AWS Route 53](#aws-route-53)
- [AWS Elastic Load Balancing](#aws-elastic-load-balancing)
- [AWS Application Load Balancer (ALB)](#aws-application-load-balancer-alb)
- [NGINX](#nginx)
- [AWS Latency](#aws-latency)
- [Amazon ECS optimized AMI](#amazon-ecs-optimized-ami)
- [AWS EC2 Container Registry ECR (Docker)](#aws-ec2-container-registry-ecr-docker)
- [Docker for AWS](#docker-for-aws)
- [AWS CLI and AWS SDK](#aws-cli-and-aws-sdk)
- [AWS VPC](#aws-vpc)
	- [AWS Client VPN](#aws-client-vpn)
	- [Tailscale](#tailscale)
- [AWS SQS. Amazon Simple Queue Service](#aws-sqs-amazon-simple-queue-service)
- [AWS Application Discovery Service Update. Agentless Discovery for VMware](#aws-application-discovery-service-update-agentless-discovery-for-vmware)
- [VMware Cloud on AWS](#vmware-cloud-on-aws)
- [AWS Developer Blog](#aws-developer-blog)
- [AWS Application Services](#aws-application-services)
- [AWS Serverless](#aws-serverless)
- [AWS API Gateway](#aws-api-gateway)
- [AWS CloudFormation. Free Templates](#aws-cloudformation-free-templates)
- [Infrastructure Code Template Generators](#infrastructure-code-template-generators)
	- [Former2 to generate IaC templates](#former2-to-generate-iac-templates)
- [AWS for Windows](#aws-for-windows)
- [Continuous Deployment with AWS](#continuous-deployment-with-aws)
- [AWS Security](#aws-security)
	- [Policy as Code with AWS CDK and Open Policy Agent](#policy-as-code-with-aws-cdk-and-open-policy-agent)
	- [Payment Card Industry Data Security Standard compliance](#payment-card-industry-data-security-standard-compliance)
	- [AWS IAM](#aws-iam)
	- [AWS Organizations](#aws-organizations)
	- [AWS CloudFront](#aws-cloudfront)
	- [AWS Firewalls](#aws-firewalls)
	- [AWS WAF Web Application Firewall](#aws-waf-web-application-firewall)
	- [AWS Vault](#aws-vault)
- [AWS S3 & EBS. AWS Storage Gateway](#aws-s3--ebs-aws-storage-gateway)
- [Amazon EFS Elastic File System](#amazon-efs-elastic-file-system)
- [AWS Transfer](#aws-transfer)
- [AWS Fargate](#aws-fargate)
	- [Admiralty](#admiralty)
- [AWS Backup and Recovery. Design for failure](#aws-backup-and-recovery-design-for-failure)
- [AWS Config Rules](#aws-config-rules)
- [AWS Big Data](#aws-big-data)
	- [AWS Data Lake](#aws-data-lake)
	- [AWS Data Pipeline (aka Big Data Pipelines or Data Streams)](#aws-data-pipeline-aka-big-data-pipelines-or-data-streams)
- [AWS NoSQL DynamoDB](#aws-nosql-dynamodb)
- [AWS IoT](#aws-iot)
- [AWS Elastic Transcoder. Video streaming](#aws-elastic-transcoder-video-streaming)
- [AWS and Splunk](#aws-and-splunk)
- [AWS Monitoring](#aws-monitoring)
- [Amazon Alexa. Voice User Interface](#amazon-alexa-voice-user-interface)
- [AWS Partner Network (APN)](#aws-partner-network-apn)
- [AWS Startup Collection. For startups building on AWS](#aws-startup-collection-for-startups-building-on-aws)
- [AWS ECS](#aws-ecs)
- [Rancher on AWS](#rancher-on-aws)
- [AWS App Mesh](#aws-app-mesh)
- [AWS Fargate](#aws-fargate-1)
- [Interview Questions](#interview-questions)
- [Local Testing](#local-testing)
	- [Localstack](#localstack)
- [Migrating On Premise VM to AWS](#migrating-on-premise-vm-to-aws)
- [AWS configuration files](#aws-configuration-files)
- [Open Source at AWS](#open-source-at-aws)
- [AWS Service Quota Requests](#aws-service-quota-requests)
- [Resource Hierarchies](#resource-hierarchies)
- [AWS Systems Manager Explorer](#aws-systems-manager-explorer)
- [AWS Systems Manager Incident Manager](#aws-systems-manager-incident-manager)
- [AWS Managed Services for Prometheus and Grafana](#aws-managed-services-for-prometheus-and-grafana)
- [AWS Chaos Engineeering. AWS Fault Injection Simulator](#aws-chaos-engineeering-aws-fault-injection-simulator)
- [Best Practices](#best-practices)
- [New Features](#new-features)
- [Superwerker](#superwerker)
- [Tools](#tools)
- [Third party tools](#third-party-tools)
- [AWS Amplify](#aws-amplify)
- [AWS Control Tower](#aws-control-tower)
- [Spain](#spain)
- [Scripts](#scripts)
- [Development](#development)
- [Cloud Development Kit CDK](#cloud-development-kit-cdk)
- [AWS Secrets Manager](#aws-secrets-manager)
- [AWS Cloud Map and HealthChecks](#aws-cloud-map-and-healthchecks)
- [AWS Cloud Endure](#aws-cloud-endure)
- [AWS Patterns](#aws-patterns)
- [AWS Tags](#aws-tags)
- [ECommerce](#ecommerce)
- [Bunch of Images](#bunch-of-images)
- [Videos](#videos)
- [Tweets](#tweets)

<!-- /MarkdownTOC -->

## Amazon Web Services
- [AWS Cloud Products](https://aws.amazon.com/products/)
- [status.aws.amazon.com: Service Health Dashboard](https://status.aws.amazon.com) 
- [aws.amazon.com/new: What's New with AWS?](https://aws.amazon.com/new)
- [aws.amazon.com/releasenotes](https://aws.amazon.com/releasenotes)
- [AWS Forums](https://forums.aws.amazon.com)
- [AWS Knowledge Center](https://aws.amazon.com/en/premiumsupport/knowledge-center/)
- [AWS Support](https://aws.amazon.com/en/premiumsupport/)
- [github.com/awslabs](https://github.com/awslabs)
- [slideshare.net/AmazonWebServices](http://www.slideshare.net/AmazonWebServices)
- [AWS 10-Minute Tutorials](https://aws.amazon.com/getting-started/tutorials/)
- [How do I create and activate a new Amazon Web Services account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- [onlineitguru.com: AWS Services](https://onlineitguru.com/tutorial/aws-services)
- [The Open Guide to Amazon Web Services](https://github.com/open-guides/og-aws)
- [AWS Ramp-Up Guides](https://aws.amazon.com/es/training/ramp-up-guides/) Your guides to learning the AWS Cloud. Build Your AWS Cloud Knowledge with Ramp-Up Guides.
- [serverlessland.com](https://serverlessland.com/) This site brings together all the latest blogs, videos, and training for AWS Serverless. Learn to use and build apps that scale automatically on low-cost, fully-managed serverless architecture.
	- [serverlessland.com/patterns: Serverless Patterns Collection](https://serverlessland.com/patterns) Use serverless patterns to quickly build integrations using AWS SAM and CDK templates. Filter by pattern and copy the template directly into your application.
	- [AWS SAM Pipelines](https://serverlessland.com/explore/sam-pipelines) Video tutorials: Learn how to generate CI/CD pipelines and deployment templates for serverless applications with AWS’ best practices for CloudBees, JenkinsCI, GitLab, GitHub using AWS SAM Pipelines.
- [AWS Activate](https://aws.amazon.com/activate) AWS Activate offers startups free tools, resources, and more to quickly get started on AWS. Build and scale with up to $100,000 in AWS Activate credits
- [aws/containers-roadmap: AWS Containers Roadmap](https://github.com/aws/containers-roadmap) This is the public roadmap for AWS container services (ECS, ECR, Fargate, and EKS).

## Blogs
- [Jayendra's Blog🌟🌟](https://jayendrapatil.com/)
- [aws.plainenglish.io](https://aws.plainenglish.io/)

## AWS Free Resources
- https://aws.amazon.com/architecture
- https://aws.amazon.com/whitepapers
- https://docs.aws.amazon.com
- https://www.aws.training
- https://aws.amazon.com/solutions/case-studies
- https://www.youtube.com/user/amazonWebServices
- https://forums.aws.amazon.com
- https://aws.amazon.com/blogs
- https://www.slideshare.net/AmazonWebServices 
- https://www.twitch.tv/aws
- [Everything AWS | Search and discover 6K+ quality AWS repositories](https://app.polymersearch.com/discover/aws)
- [workshops.aws: AWS Workshops](https://workshops.aws/) This website lists workshops created by the teams at Amazon Web Services (AWS). Workshops are hands-on events designed to teach or introduce practical skills, techniques, or concepts which you can use to solve business problems.
You can filter by topic using the toolbar above.

## Introduction
- [dzone: AWS Basics](https://dzone.com/articles/aws-basics)
- [dzone: AWS Elastic Compute Cloud (EC2) Basics](https://dzone.com/articles/aws-elastic-compute-cloud-ec2-basics) We will learn about IP Addresses and also connect to public EC2 instances externally using SSH. Let's have a look at public and private IP behavior first.
- [dzone: AWS Basics: Bastion Hosts and NAT](https://dzone.com/articles/aws-basics-bastian-hosts-and-nat) In this post, we will set up Bastion Host and NAT instances in our VPC. We will learn why we need those and some of the options available to us.
- [acloudguru.com: The Cloud Dictionary of Pain: Five Of AWS’s Toughest Cloud Topics](https://acloudguru.com/blog/engineering/the-cloud-dictionary-of-pain-five-of-awss-toughest-cloud-topics)
- [dannys.cloud: 10 Best Free AWS Learning Resources for Beginners](https://dannys.cloud/10-best-free-aws-learning-resources-for-beginners) This blogpost provides free resources for beginners to get started with AWS through videos, whitepapers, labs, and certification guides.
- [linkedin pulse: Listado de todos los Servicios de AWS (actualizado 1 de Enero 2021)](https://www.linkedin.com/pulse/listado-de-todos-los-servicios-amazon-web-services-daniel-pe%25C3%25B1a-silva)
- [towardsaws.com: A Gentle Introduction to Amazon Web Services (AWS)](https://towardsaws.com/a-gentle-introduction-to-amazon-web-services-aws-50f18c7c57dc)
- [docs.aws.amazon.com: The AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html)
- [thenewstack.io: The AWS Shared Responsibility Model for Kubernetes](https://thenewstack.io/understand-the-aws-shared-responsibility-model-for-kubernetes/)
- [dzone: Migrating to AWS](https://dzone.com/articles/migrating-to-aws) AWS Cloud is the way to go, but migrating to the cloud is not simple. Read this article for a step-by-step migration strategy.
- [medium: AWS Services Every Developer Should Be Aware Of](https://medium.com/@ashish_fagna/aws-services-every-developer-should-be-aware-of-f7c48aaa854f)
- [blog.cloudyali.io: The Absolute minimum every developer must know about AWS security!](https://blog.cloudyali.io/absolute-minimum-every-developer-must-know-about-aws-security)
- [acloudguru.com: 12 AWS Config rules that every account should have](https://acloudguru.com/blog/engineering/12-aws-config-rules-that-every-account-should-have)
- [cloudonaut.io: EC2 Checklist: 7 things to do after launching an instance](https://cloudonaut.io/ec2-checklist-seven-things-to-do-after-launching-an-instance/)
- [medium: 6 Lessons Learned - Migrating Application on Production](https://medium.com/swlh/6-lessons-learned-from-migrating-web-application-on-production-ce9add8e63f3)
- [lastweekinaws.com: 17 More Ways to Run Containers on AWS](https://www.lastweekinaws.com/blog/17-more-ways-to-run-containers-on-aws/)
- [What is Streaming Data?](https://aws.amazon.com/streaming-data/)

### Books
- [gocloudarchitects.com: AWS Certified Solutions Architect Associate Exam Guide](https://www.gocloudarchitects.com/free-csa-a-ebook/)

## Training
- [New digital course and lab: AWS Cloud Development Kit (CDK) Primer](https://aws.amazon.com/about-aws/whats-new/2021/01/new-digital-course-and-lab-aws-cloud-development-kit-cdk-primer/)
- [acloudguru.com](https://acloudguru.com/)
- [twitch.tv/acloudguruofficial](https://www.twitch.tv/acloudguruofficial)
- [learn.cantrill.io 🌟](https://learn.cantrill.io/)
	- [github.com/acantril/learn-cantrill-io-labs](https://github.com/acantril/learn-cantrill-io-labs)
	- [linkedin.com/pulse: So, you think you're an associate level Solutions Architect?](https://www.linkedin.com/pulse/so-you-think-youre-associate-level-solutions-adrian-cantrill/)
- [analyticsindiamag.com: Free Online Resources To Get Started On Cloud Computing](https://analyticsindiamag.com/free-online-resources-to-get-started-on-cloud-computing/)
## AWS Certification
- [linkedin: Sharing My Top 10 resources to use while preparing for AWS Certification Exams](https://www.linkedin.com/pulse/sharing-my-top-10-resources-use-while-preparing-aws-exams-semaan/)
- [Schedule an Exam](https://aws.amazon.com/certification/certification-prep/testing) Find the testing option that works best for you

## AWS Glossary
- [AWS Glossary](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

## Awesome AWS
- [Awesome AWS](https://github.com/donnemartin/awesome-aws)

## AWS Marketplace
- [AWS Marketplace](https://aws.amazon.com/marketplace)

## AWS Pricing
- [May 2020: EC2 Price Reduction – For EC2 Instance Saving Plans and Standard Reserved Instances](https://aws.amazon.com/es/blogs/aws/ec2-price-reduction-for-ec2-instance-saving-plans-and-standard-reserved-instances/)
- [ec2.shop: Compare AWS EC2 instance price from the CLI](https://ec2.shop/)
- [infoq.com: AWS Launches Low-Cost Burstable T4g Instances Powered by AWS Graviton2](https://www.infoq.com/news/2020/09/aws-ec2-t4g-instances/)
- [freecodecamp.org: How to Optimize your AWS Cloud Architecture Costs](https://www.freecodecamp.org/news/cost-optimization-in-aws/)
- [aws.amazon.com: Amazon S3 Glacier Price Reduction](https://aws.amazon.com/es/blogs/aws/amazon-s3-glacier-price-reduction/)
- [infoq.com: AWS Announces Lower Cost Storage Classes for Amazon Elastic File System](https://www.infoq.com/news/2021/03/aws-efs-one-zone-storage-classes/)
- [dzone: Understanding AWS Costs](https://dzone.com/articles/understanding-aws-costs) In this article, I'll provide a comprehensive guide on how to understand your AWS costs and needs.
- [thenewstack.io: 7 Tips for Cutting Down Your AWS Kubernetes Bill](https://thenewstack.io/7-tips-for-cutting-down-your-aws-kubernetes-bill/)
- [cast.ai: Keep your AWS Kubernetes costs in check with intelligent allocation (EKS)](https://cast.ai/blog/keep-your-aws-kubernetes-costs-in-check-with-intelligent-allocation) A guide to intelligently allocating Kubernetes costs with EKS
- [thenewstack.io: Cloud Bill Risks of AWS Reserved Instances and Savings Plans](https://thenewstack.io/cloud-bill-risks-of-aws-reserved-instances-and-savings-plans/)
- [dzone: A Guide on Estimating AWS EC2 Workloads for a Microservice Application](https://dzone.com/articles/a-guide-on-estimating-aws-ec2-workloads-for-a-micr) AWS EC2 instance costs can be a significant part of the cloud bill, so it's always a good idea to estimate the workloads using the AWS pricing calculator.

### AWS Calculator
- [calculator.aws: AWS Total Cost of Ownership (TCO) Calculators](https://calculator.aws/)
- [Understanding your AWS Cost Datasets: A Cheat Sheet](https://aws.amazon.com/blogs/aws-cost-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
- [Announcing General Availability of AWS Cost Anomaly Detection](https://aws.amazon.com/blogs/aws-cost-management/announcing-general-availability-of-aws-cost-anomaly-detection/)

## AWS on Twitter
- [twitter.com/awscloud](https://twitter.com/awscloud)
- [twitter.com/AWSreInvent](https://twitter.com/AWSreInvent)
- [twitter.com/jeffbarr](https://twitter.com/jeffbarr)
- [twitter.com/AWSstartups](https://twitter.com/AWSstartups)
- [twitter.com/AWS_Partners](https://twitter.com/AWS_Partners)

## AWS Architecture
- [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS application-architecture](http://www.conceptdraw.com/examples/application-architecture)
- [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)

## AWS Youtube channel and Podcasts
- [Amazon Web Services Youtube](https://www.youtube.com/user/AmazonWebServices)
- [AWS Tutorial Series](https://www.youtube.com/user/awstutorialseries)
- [AWS Webinar Channel](https://www.youtube.com/user/AWSwebinars)
- [AWS Podcasts](https://aws.amazon.com/podcasts/aws-podcast/)
- [AWS Techchat](https://aws.amazon.com/podcasts/aws-techchat)
- [Stitcher AWS Podcasts](http://www.stitcher.com/podcast/amazon-web-services/aws-podcast)

## Closed groups for AWS certified professionals
- [awscerts.slack.com](https://awscerts.slack.com)
- [Amazon AWS Certification Preparation Tips](http://walkintocloud.com/index.php/2016/06/04/amazon-aws-certification-preparation-tips/)
- [A curated list of AWS resources to prepare for the AWS Certifications](https://gist.github.com/leonardofed)
- [AWS Certified Solutions Architect Professional – Study Guide](https://blue-clouds.com/category/study-guide/)
- [aws.amazon.com: First AWS Certification Study Guide Now Available](https://aws.amazon.com/es/about-aws/whats-new/2016/10/first-aws-certification-study-guide-now-available/)
- [Tips on Passing AWS Certified Solutions Architect - Professional Level](https://www.linkedin.com/pulse/passed-aws-certified-solutions-architect-level-harshit-agarwal)

## AWS Architecture Blog, Official Blog, AWS Labs, AWS Quick Start
- [AWS Architecture Blog](https://www.awsarchitectureblog.com)
- [AWS Official Blog](http://blogs.aws.amazon.com/)
- [AWS Labs GitHub](https://github.com/awslabs)
- [AWS Quick Start Reference Deployments](http://aws.amazon.com/es/quickstart/)
	- [AWS Quick Start - GitHub](https://github.com/awslabs/aws-quickstart)
- [InfoWorld Review – Amazon Aurora Rocks MySQL](https://aws.amazon.com/blogs/aws/infoworld-review-amazon-aurora-rocks-mysql/)
- [AWS Cost Explorer Update – Access to EC2 Usage Data](https://aws.amazon.com/blogs/aws/aws-cost-explorer-update-access-to-ec2-usage-data/)

## AWS Case Studies
- [Thomas Publishing Case Study](https://aws.amazon.com/solutions/case-studies/thomas-publishing/)  After moving to AWS, we were able to shut down our largest data center, eliminating hundreds of thousands of dollars in associated real estate, facility operations, and power and cooling costs.   

## AWS tips. AWS Performance. Handling AWS Failures and Outages
- [AWS Tips I Wish I'd Known Before I Started (Feb 2014)](https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/) A collection of random tips for Amazon Web Services (AWS) that I wish I'd been told a few years ago, based on what I've learned by building and deploying various applications on AWS.
- [Amazon AWS Tips and Gotchas – Part 1 (Feb 2016)](http://www.tekhead.org/blog/2016/02/amazon-aws-tips-and-gotchas-part-1/)
- [DZone: 5 Tips for Better AWS Performance](https://dzone.com/articles/5-tips-for-better-aws-performance) The Ngnix team has a nice list of tips for better performance when using the AWS services. Some of them are related to Ngnix, but others are completely usable for anyone.
- [How do I get started with AWS cloud computing?](https://aws.amazon.com/premiumsupport/knowledge-center/get-started-aws/)
- [DZone: Dude, Where's My Performance?](https://dzone.com/articles/dude-wheres-my-performance)
- [DZone: A Guide to Performance Challenges with AWS EC2: Part 1](https://blog.appdynamics.com/cloud/a-guide-to-performance-challenges-with-aws-ec2-part-1/) 
- [DZone: A Guide to Performance Challenges With AWS EC2: Part 2](https://dzone.com/articles/a-guide-to-performance-challenges-with-aws-ec2-par-1) Using Amazon Web Services? Learn how to get your Elastic Compute Cloud instances to perform better than your competitors.
- [DZone: A Guide to Performance Challenges With AWS EC2: Part 3](https://dzone.com/articles/a-guide-to-performance-challenges-with-aws-ec2-par-2) In the second part of his guide covering performance challenges in AWS EC2, Saba Anees covers instances and the right applications for your workloads.
- [DZone: A Guide to Performance Challenges With AWS EC2: Part 4](https://dzone.com/articles/a-guide-to-performance-challenges-with-aws-ec2-par-3) In the final part of his series covering performance challenges with AWS EC2, Saba Anees goes over poor ELB performance and handling AWS failures and outages.
- [blog.datapath.io: Dynamic Web Accelerator for AWS Hosted Applications](http://blog.datapath.io/dynamic-web-accelerator-for-aws-hosted-applications)
- [The Truth About Downtime in the Cloud](http://cloud.netapp.com/blog/prepare-for-the-day-of-all-cloud)

## AWS Clients
- [Trainline.com dumps Oracle and Microsoft, gulps AWS Kool-Aid](http://www.theregister.co.uk/2016/07/13/trainline_dumps_oracle_microsoft_goes_full_aws_cto_interview/)
- [London DevOps - Trainline, A DevOps Journey - Chris Turvil](https://www.youtube.com/watch?v=IUvUmqu1MBQ)
- [aws.amazon.com: Trainline Case Study](https://aws.amazon.com/solutions/case-studies/trainline/)

## AWS New Features
- [AWS Config Rules – Dynamic Compliance Checking for Cloud Resources](https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/)
- [Amazon Inspector – Automated Security Assessment Service](https://aws.amazon.com/blogs/aws/amazon-inspector-automated-security-assessment-service)
- [Coming Soon – EC2 Dedicated Hosts](https://aws.amazon.com/blogs/aws/coming-soon-ec2-dedicated-hosts)
- [AWS Device Farm: Improve the quality of your web and mobile applications by testing across desktop browsers and real mobile devices hosted in the AWS Cloud](https://aws.amazon.com/device-farm)
- [AWS Mobile Hub – Build, Test, and Monitor Mobile Applications](https://aws.amazon.com/blogs/aws/aws-mobile-hub-build-test-and-monitor-mobile-applications)
- [EC2 Container Service Update – Container Registry, ECS CLI, AZ-Aware Scheduling, and More](https://aws.amazon.com/blogs/aws/ec2-container-service-update-container-registry-ecs-cli-az-aware-scheduling-and-more)
- [CloudWatch Dashboards – Create & Use Customized Metrics Views](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views)
- [AWS Lambda Update – Python, VPC, Increased Function Duration, Scheduling, and More](https://aws.amazon.com/blogs/aws/aws-lambda-update-python-vpc-increased-function-duration-scheduling-and-more)
- [AWS IoT – Cloud Services for Connected Devices](https://aws.amazon.com/blogs/aws/aws-iot-cloud-services-for-connected-devices)
- [Amazon EFS: Amazon Elastic File System – Shared File Storage for Amazon EC2](https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-shared-file-storage-for-amazon-ec2/)
- [New – Encrypted EBS Boot Volumes](https://aws.amazon.com/blogs/aws/new-encrypted-ebs-boot-volumes)
	- [Amazon EBS Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
- [Now Add or Modify Request Headers Forwarded From Amazon CloudFront to Origin](https://aws.amazon.com/about-aws/whats-new/2015/12/now-add-or-modify-request-headers-forwarded-from-amazon-cloudfront-to-origin/)
- [AWS CloudFormation Adds Support for AWS WAF and AWS Directory Service for Microsoft Active Directory](https://aws.amazon.com/es/about-aws/whats-new/2015/12/aws-cloudformation-adds-support-for-aws-waf-and-aws-directory-service-for-microsoft-active-directory/)
- [Amazon WorkMail – Now Generally Available](https://aws.amazon.com/blogs/aws/amazon-workmail-now-generally-available/)
- [London Calling! An AWS Region is coming to the UK!](http://www.allthingsdistributed.com/2015/11/aws-announces-uk-region.html)
- [New – Scheduled Reserved Instances](https://aws.amazon.com/blogs/aws/new-scheduled-reserved-instances/)
- [AWS CloudShell - Command-Line Access to AWS Resources](https://aws.amazon.com/es/blogs/aws/aws-cloudshell-command-line-access-to-aws-resources/)
- [zdnet.com: AWS rolls out S3 Object Lambda to process data for multiple applications](https://www.zdnet.com/google-amp/article/aws-rolls-out-s3-object-lambda-to-process-data-for-multiple-applications/) The new capability allows you to share data across applications, without having to manage a proxy layer or create copies of the dataset.
- [github.com/hayao-k/cdk-ecr-image-scan-notify](https://github.com/hayao-k/cdk-ecr-image-scan-notify)
- [cloudonaut.io: Seamless EC2 monitoring with the Unified CloudWatch Agent](https://cloudonaut.io/seamless-ec2-monitoring-with-the-unified-cloudwatch-agent/)
- [amazon.com: Reduce Unwanted Traffic on Your Website with New AWS WAF Bot Control](https://aws.amazon.com/blogs/aws/reduce-unwanted-traffic-on-your-web-site-with-aws-bot-control/)
- [infoq.com: AWS Introduces EC2 Serial Console: Troubleshoot Boot and Networking Issues](https://www.infoq.com/news/2021/04/aws-ec2-serial-console/)
- [infoq.com: AWS Introduces a New Workflow Studio for AWS Step Functions](https://www.infoq.com/news/2021/06/step-functions-workflow-studio/)
- [New AWS Solutions Implementation: Tag Tamer](https://aws.amazon.com/about-aws/whats-new/2021/06/new-aws-solutions-implementation-tag-tamer/) Tag Tamer helps you apply tags to new and existing AWS resources. Using the pre-built web user interface ensures a consistent tagging implementation—providing improved cost allocations, automation, access controls, and organization.
- [Introducing new self-paced courses to improve Java and Python code quality with Amazon CodeGuru](https://aws.amazon.com/blogs/devops/new-self-paced-courses-to-improve-java-and-python-code-quality-with-amazon-codeguru/)
- [Automate preapproved operations with AWS Service Catalog service actions](https://aws.amazon.com/blogs/mt/automate-preapproved-operations-with-aws-service-catalog-service-actions/) Most of my enterprise customers have the need to allow their users to execute self-service operational tasks while restricting access to a minimum set of services. With AWS Service Catalog, you can provision pre-approved products, when combined with AWS Service Catalog service actions, you can provide simple predefined actions associated with the AWS Service Catalog products that their users can execute.
- [Amazon Virtual Private Cloud (VPC) customers can now assign IP prefixes to their EC2 instances](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-virtual-private-cloud-vpc-customers-can-assign-ip-prefixes-ec2-instances/)
- [Amazon RDS Proxy can now be created in a shared Virtual Private Cloud (VPC)](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-rds-proxy-created-shared-virtual-private-cloud-vpc/)
- [Amazon VPC CNI plugin increases pods per node limits](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-vpc-cni-plugin-increases-pods-per-node-limits/)
- [theregister.com: AWS to retire EC2-Classic – the network glue that helped start the IaaS rush](https://www.theregister.com/2021/07/29/amazon_web_services_ec2_classic_networking/) You've got a year to sort yourself out if you're still using it for some reason
- [AWS Security Hub adds 18 new controls to its Foundational Security Best Practices standard and 8 new partners for enhanced cloud security posture monitoring](https://aws.amazon.com/about-aws/whats-new/2021/08/aws-security-hub-adds-18-new-controls-foundational-security-best-practices-standard-8-new-partners-enhanced-cloud-security-posture-monitoring/)
- [EC2 VM Import/Export now supports migration of virtual machines with Unified Extensible Firmware Interface (UEFI) boot to AWS](https://aws.amazon.com/es/about-aws/whats-new/2021/08/ec2-vm-import-export-unified-extensible-firmware-interface-aws/)
- [Amazon Virtual Private Cloud (VPC) customers can now resize their prefix list](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-vpc-resize-prefix-list)
- [New for AWS CloudFormation – Quickly Retry Stack Operations from the Point of Failure](https://aws.amazon.com/es/blogs/aws/new-for-aws-cloudformation-quickly-retry-stack-operations-from-the-point-of-failure/)
- [AWS Site-to-Site VPN releases updated Download Configuration utility](https://aws.amazon.com/about-aws/whats-new/2021/09/aws-site-to-site-vpn-download-configuration-utility/) With this update, Site-to-Site VPN customers can generate configuration templates for compatible Customer Gateway (CGW) devices, making it easier to create VPN connections to AWS.
- [New for AWS Distro for OpenTelemetry – Tracing Support is Now Generally Available](https://aws.amazon.com/blogs/aws/new-for-aws-distro-for-opentelemetry-tracing-support-is-now-generally-available/)
- [Application Load Balancer now enables AWS PrivateLink and static IP addresses by direct integration with Network Load Balancer](https://aws.amazon.com/about-aws/whats-new/2021/09/application-load-balancer-aws-privatelink-static-ip-addresses-network-load-balancer/) 
- [Amazon EC2 now offers Global View on the console to view all resources across regions together](https://aws.amazon.com/about-aws/whats-new/2021/09/amazon-ec2-global-view-console-regions/)
- [siliconangle.com: Amazon debuts fully managed, Prometheus-based container monitoring service](https://siliconangle.com/2021/09/29/amazon-debuts-fully-managed-prometheus-based-container-monitoring-service/)

## AWS Management Console
- [Working with the AWS Management Console](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)

## AWS Management Tools Blog
- [AWS Management Tools Blog](https://aws.amazon.com/blogs/mt/)
- [Metabadger](https://github.com/salesforce/metabadger) Prevent SSRF attacks on AWS EC2 via automated upgrades to the more secure Instance Metadata Service v2 (IMDSv2).

## AWS Cloudwatch
- [threatstack.com: 50 Best AWS CloudWatch Tutorials](https://www.threatstack.com/blog/50-best-aws-cloudwatch-tutorials)
- [Amazon CloudWatch now monitors Prometheus metrics from Container environments](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-monitors-prometheus-metrics-container-environments/)
- [Amazon CloudWatch Dashboards now supports sharing](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-dashboards-supports-sharing/)
- [How BT uses Amazon CloudWatch to monitor millions of devices](https://aws.amazon.com/blogs/mt/how-bt-uses-amazon-cloudwatch-to-monitor-millions-of-devices/)

## AWS Schema Conversion Tool
- [cloudacademy.com: Migrating Data to AWS Using the AWS Schema Conversion Tool: A Preview](http://cloudacademy.com/blog/migrating-data-to-aws/)
- [AWS Schema Conversion Tool now supports PostgreSQL as conversion target](http://aws.amazon.com/about-aws/whats-new/2016/01/aws-schema-conversion-tool-postgresql-support/)
- [Creating an AWS Schema Conversion Tool Project](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_SchemaConversionTool.Converting.CreateProject.html) Use SSL to connect to your source DB with the AWS Schema Conversion Tool. 
- [AWS Schema Conversion Tool now supports conversions from Oracle DW and Teradata to Amazon Redshift, Embedded Code Conversion, and Cloud native Code Optimization](https://aws.amazon.com/es/about-aws/whats-new/2016/07/aws-schema-conversion-tool-now-supports-conversions-from-oracle-dw-and-teradata-to-amazon-redshift-embedded-code-conversion-and-cloud-native-code-optimization)

## AWS RDS
- [Tutorial: Restoring a DB Instance from a DB Snapshot](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.RestoringFromSnapshot.html)
- [Partitioning MySQL on RDS: "How We Partitioned Airbnb’s Main Database in Two Weeks"](https://medium.com/airbnb-engineering/how-we-partitioned-airbnb-s-main-database-in-two-weeks-55f7e006ff21)
- [Amazon RDS for SQL Server – Support for Windows Authentication](https://aws.amazon.com/blogs/aws/amazon-rds-for-sql-server-support-for-windows-authentication/)
- [Why Support of PostgreSQL 9.5 by Amazon RDS is Such Great News](http://blog.rubyroidlabs.com/2016/04/postgresql-9-5/)
- [AWS Tutorials: Create and Connect to a MySQL Database with Amazon RDS](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/)
- [Migrating from MySQL (RDS) to Aurora with no downtime](http://cantrill.io/howto/aws/2016/06/06/migrating-from-mysql-to-aurora-with-almost-no-downtime.html)
- [Replicating Amazon Aurora DB Clusters Across AWS Regions](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.CrossRegion.html)
- [Working with PostgreSQL, MySQL, and MariaDB Read Replicas - Amazon](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) Use RDS PostgreSQL cross-region Read Replicas to get data close to customers. 
- [Working with an Amazon RDS DB Instance in a VPC](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)
- [Creating a DB Instance Running the Oracle Database Engine](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateOracleInstance.html) In RDS, create Oracle Standard Edition 2 DB instances with the License Included model.
- [Oracle Database on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/10/oracle-database-on-the-aws-cloud-quick-start-reference-deployment/)
- [besanttechnologies.com: AWS – Relational Database Service](https://www.besanttechnologies.com/amazon-web-services-relational-database)
- [Introducing the Aurora Storage Engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/)
- [dzone: AWS Relational Database Service (RDS): PostgreSQL in Cloud](https://dzone.com/articles/aws-relational-database-service-rds-postgresql-in) Today, we will go into details of Amazon RDS. We also set up a PostgreSQL instance using this service and connect to it using a tool Azure Data Studio.
- [sysadminxpert.com: How to Enable Slow Query Logs in AWS RDS MySQL](https://sysadminxpert.com/how-to-enable-slow-query-logs-in-aws-rds-mysql/)
- [New – Create Microsoft SQL Server Instances of Amazon RDS on AWS Outposts](https://aws.amazon.com/blogs/aws/new-create-microsoft-sql-server-instances-of-amazon-rds-on-aws-outposts/)
- [percona.com: The Benefits of Amazon RDS for MySQL](https://www.percona.com/blog/2019/12/19/the-benefits-of-amazon-rds-for-mysql/)
- [medium: AWS Backup Service for Amazon RDS](https://medium.com/avmconsulting-blog/aws-backup-service-for-amazon-rds-3e6f5827aa66)

### AWS DMS
- [Amazon RDS for PostgreSQL Enhancements: Support for new minor versions, Logical Replication, and Amazon RDS PostgreSQL as a source for AWS DMS](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-rds-for-postgresql-enhancements-support-for-new-minor-versions-logical-replication-and-amazon-rds-postgresql-as-a-source-for-aws-dms/)
- [Migrating Oracle databases with near-zero downtime using AWS DMS](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/)
- [Migrating a commercial database to open source with AWS SCT and AWS DMS](https://aws.amazon.com/blogs/database/migrating-a-commercial-database-to-open-source-with-aws-sct-and-aws-dms/)
- [revenuecat.com: Replicating a postgresql cluster to redshift](https://www.revenuecat.com/blog/replicating-a-postgresql-cluster-to-redshift)

### AWS RDS Proxy
- [Amazon RDS Proxy – Now Generally Available](https://aws.amazon.com/es/blogs/aws/amazon-rds-proxy-now-generally-available/) A fully managed, highly available database proxy for Amazon Relational Database Service (RDS) that makes applications more scalable, more resilient to database failures, and more secure.

## AWS Application Discovery Service
- [AWS Application Discovery Service](http://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)

## AWS Migrations
- [New AWS Competency – AWS Migration](https://aws.amazon.com/blogs/aws/new-aws-competency-aws-migration/)
- [Migrate Resources Between AWS Accounts](https://aws.amazon.com/blogs/architecture/migrate-resources-between-aws-accounts)

### AWS Database Migration Service
- [AWS Database Migration Service](https://aws.amazon.com/es/blogs/aws/aws-database-migration-service/)
- [Whitepaper: Migrating Your Databases to AWS](https://aws.amazon.com/es/dms/learn-more/)

## AWS Redshift
- [Tutorial: Tuning Table Design](http://docs.aws.amazon.com/redshift/latest/dg/tutorial-tuning-tables.html) In this tutorial, you will learn how to optimize the design of your tables.

## AWS DevOps. AWS CodePipeline
* [AWS DevOps](https://aws.amazon.com/devops/)
- [AWS DevOps Blog](https://blogs.aws.amazon.com/application-management/)
- [Setting Up the Jenkins Plugin for AWS CodeDeploy](https://blogs.aws.amazon.com/application-management/post/TxMJROUIFQZ4HS/Setting-Up-the-Jenkins-Plugin-for-AWS-CodeDeploy)
- [Continuous Delivery for a PHP Application Using AWS CodePipeline, AWS Elastic Beanstalk, and Solano Labs](https://blogs.aws.amazon.com/application-management/post/TxYSRRBH57NP2P/Continuous-Delivery-for-a-PHP-Application-Using-AWS-CodePipeline-AWS-Elastic-Bea)
- [Building Continuous Deployment on AWS with AWS CodePipeline, Jenkins and AWS Elastic Beanstalk](https://blogs.aws.amazon.com/application-management/post/Tx34AXRMYLXG5OT/Building-Continuous-Deployment-on-AWS-with-AWS-CodePipeline-Jenkins-and-AWS-Elas)
- [AWS CodeDeploy: Deploying from a Development Account to a Production Account](http://blogs.aws.amazon.com/application-management/post/Tx3PE3JTSVJSFI7/AWS-CodeDeploy-Deploying-from-a-Development-Account-to-a-Production-Account)
- [blazemeter.com: Three Ways DevOps Benefit from AWS CodePipeline](https://blazemeter.com/blog/three-ways-devops-benefit-aws-codepipeline)
- [AWS Partner Network - CodePipeline Integrations](https://aws.amazon.com/es/codepipeline/product-integrations/)
- [**Multi-Region Infrastructure Deployment**](https://aws.amazon.com/solutions/multi-region-infrastructure-deployment/) This solution automatically provisions and configures AWS CodePipeline to automate the CI/CD pipeline for CloudFormation templates
- [k21academy.com: AWS DevOps Vs. Azure DevOps](https://k21academy.com/amazon-web-services/aws-devops-vs-azure-devops/?utm_source=linkedin&utm_medium=referral&utm_campaign=awsdevops17_dec20_aws_cloud_computing_for_interested_parties__users)
- [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/) ML-powered cloud operations service to improve application availability
	- [infoq.com: AWS Launches Amazon DevOps Guru](https://www.infoq.com/news/2021/01/aws-devops-guru/)
- [aws.plainenglish.io: AWS CodePipeline for Amazon ECS](https://aws.plainenglish.io/aws-codepipeline-for-amazon-ecs-part-2-a-blue-green-deployment-type-c162fd73be91) In this tutorial, I would like to explain to you how to create an AWS CodePipeline for ECS with a Blue/green deployment type.

## AWS Elastic Beanstalk
- [AWS Elastic Beanstalk Documentation](http://aws.amazon.com/documentation/elastic-beanstalk/)
- [Deploying a High-Availability PHP Application with an External Amazon RDS Database to Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-ha-tutorial.html)
- [Creating and Deploying PHP Applications on AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP_eb.html)
- [AWS Elastic Beanstalk Supports ASP.NET Core and Multi-App .NET Support](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-asp-net-core-and-multi-app-net-support/)
- [AWS Elastic Beanstalk Supports Application Load Balancer](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-application-load-balancer/)
- [Configuring an Application Load Balancer](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-applicationloadbalancer.html)
- [AWS Elastic Beanstalk Supports Nginx Proxy Server with Tomcat](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-nginx-proxy-server-with-tomcat/) 

## AWS OpsWorks
- [AWS OpsWorks](https://aws.amazon.com/opsworks/)
- [AWS OpsWorks - Chef Versions](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-chef11.html)
- [youtube: AWS OpsWorks Overview and Demo](https://www.youtube.com/watch?v=cj_LoG6C2xk&list=PLR3sVanzLpJN6BiYS20K4BMPpiDGifbZy)
- [Use OpsWorks to create and manage instances that run CentOS 7](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os-linux.html?adbsc=docs_20160709_63418706&adbid=UPDATE-c2382910-6157610151248490496&adbpl=li&adbpr=2382910#workinginstances-os-linux-centos)

## AWS Networking
- [AWS Networking for Developers](https://aws.amazon.com/es/blogs/apn/aws-networking-for-developers/)
- [Elastic Network Adapter](https://aws.amazon.com/blogs/aws/elastic-network-adapter-high-performance-network-interface-for-amazon-ec2)
- [AWS Cloud Networking – Zero to Hero](http://www.netdesignarena.com/index.php/2020/04/15/new-blog-series-aws-cloud-networking-zero-to-hero/)
- [cloudonaut.io: What Architects Need to Know About Networking on AWS](https://cloudonaut.io/what-architects-need-to-know-about-networking-on-aws/)
- [cloudonaut.io: Advanced AWS Networking: Pitfalls That You Should Avoid](https://cloudonaut.io/advanved-aws-networking-pitfalls-that-you-should-avoid/)
- [gprakash-sharma.medium.com: AWS Site-to-Site VPN with NAT](https://gprakash-sharma.medium.com/aws-site-to-site-vpn-with-nat-8bb99f4653ab)
- [Resolve DNS names of Network Load Balancer nodes to limit cross-Zone traffic](https://aws.amazon.com/blogs/networking-and-content-delivery/resolve-dns-names-of-network-load-balancer-nodes-to-limit-cross-zone-traffic)
- [github.com/seligman/aws-ip-ranges: AWS's ip-ranges.json](https://github.com/seligman/aws-ip-ranges) AWS adds an extra 5.5M IPv4 addresses. Tracking the history and size of AWS's ip-ranges.json file. AWS provides a data file showing the current IP ranges their services use, called ip-ranges.json. This repository tracks changes to that file, and based off a trigger on the SNS topic automatically produces this chart showing how what percentage of the Internet's IPv4 address space AWS is in control of.

## AWS Route 53
- [How do I transfer a domain to AWS from another registrar?](https://aws.amazon.com/premiumsupport/knowledge-center/transfer-domain-to-aws/)

## AWS Elastic Load Balancing
- [AWS Summit Series 2016 | London: Deep Dive on Elastic Load Balancing](https://www.youtube.com/watch?v=HinwLb2lpLQ)
- [docs.aws.amazon.com: What Is Elastic Load Balancing?](http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [ably.com: Balancing act: the current limits of AWS network load balancers](https://ably.com/blog/limits-aws-network-load-balancers)

## AWS Application Load Balancer (ALB)
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/)
- [aws blogs - New – AWS Application Load Balancer](https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer/)
- [medium: 10 reasons why you should think about using an AWS Application Load Balancer](https://medium.com/ankercloud-engineering/10-reasons-why-you-should-think-about-using-an-aws-application-loadbalancer-945f57816c34)
- [Introducing the AWS Load Balancer Controller](https://aws.amazon.com/blogs/containers/introducing-aws-load-balancer-controller/)
- [Fine-tuning blue/green deployments on application load balancer](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)

## NGINX
- [NGINX Plus on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/09/nginx-plus-on-the-aws-cloud-quick-start-reference-deployment/)

## AWS Latency
- [Find the fastest region from your location](http://aws-latency.altaircp.com/) Check AWS response time from you browser. Sharing my mini-project, it measures response time from AWS services from different regions base on your location. let me know what you think.
- [Linkedin Discussion](https://www.linkedin.com/groups/49531/49531-6092152919937794052)
>1. Don't do just a single check, the first check will be a lot slower as DNS lookups will need to be done, etc.
>2. I'd recommend doing at least 3 checks getting an average.
- Run 6 checks (with a random 3-10 second delay between each one), the first can be ignored, the highest one is also ignored (as a likely outlier), then for the next 4 show the minimum, maximum and average (mean).
- [medium.com: Optimizing Latency and Bandwidth for AWS Traffic](https://medium.com/aws-activate-startup-blog/optimizing-latency-and-bandwidth-for-aws-traffic-cdfd18d0d0f7)

## Amazon ECS optimized AMI
- [Amazon ECS-optimized AMI](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)

## AWS EC2 Container Registry ECR (Docker)
- [A Better Dev/Test Experience: Docker and AWS](https://medium.com/aws-activate-startup-blog/a-better-dev-test-experience-docker-and-aws-291da5ab1238)
- [Amazon EC2 Container Registry Documentation](http://aws.amazon.com/es/documentation/ecr/)
- [Get started with Amazon EC2 Container Registry (Amazon ECR)](http://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html)
- [Using Docker Machine with AWS](http://blog.scottlowe.org/2016/03/22/using-docker-machine-with-aws/)
- [Docker Datacenter on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/es/about-aws/whats-new/2016/06/docker-datacenter-on-the-aws-cloud-quick-start-reference-deployment/)
- [ecrcp](https://github.com/bit-cloner/ecrcp) aims to mimic cp command in Linux systems as closely as possible in its implementation. Consider ecrcp to be the cp equivalent to copy container images from docker hub to ECR.
- [aws.plainenglish.io: How to Push a Docker Image to the AWS ECR](https://aws.plainenglish.io/how-to-push-an-image-to-aws-ecr-b2be848c2ef)

## Docker for AWS
- [DZone: Getting Started With Docker for AWS and Scaling Nodes](https://dzone.com/articles/getting-started-with-docker-for-aws-and-scaling-no) This blog will explain how to get started with Docker for AWS and deploy a multi-host Swarm cluster on Amazon.
- [blog.couchbase.com: Getting Started with Docker for AWS and Scaling Nodes](http://blog.couchbase.com/2016/july/docker-for-aws-getting-started-scaling-nodes)

## AWS CLI and AWS SDK
- [Amazon CLI Documentation](https://aws.amazon.com/cli)
- [AWS CLI Command Reference](http://docs.aws.amazon.com/cli/latest/index.html)
- [New usage examples have been added to the CLI for CodePipeline API Reference](http://docs.aws.amazon.com/cli/latest/reference/codepipeline/index.html)
- [ec2-ssh-yplan: A pair of command line utilities for finding and SSH-ing into your Amazon EC2 instances by tag (such as ‘Name’)](https://pypi.python.org/pypi/ec2-ssh-yplan/)
- List running instances using 'awscli':
  
```bash
aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query 'Reservations[].Instances[].[InstanceID]'
```

- List all AWS instances in a table format using 'awscli':

```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].[Placement.AvailabilityZone, State.Name, InstanceID,InstanceType,Platform,Tags.Value,State.Code,Tags.Values]' --output table
```

- [Announcing the end of support for Python 2.7 in the AWS SDK for Python and AWS CLI v1](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1/)
- [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/)

## AWS VPC
- [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)
- [linuxjournal.com: AWS EC2 VPC CLI](http://www.linuxjournal.com/content/aws-ec2-vpc-cli)
- [Build a Modular and Scalable Amazon VPC Architecture with New Quick Start](https://aws.amazon.com/about-aws/whats-new/2016/07/build-a-modular-and-scalable-amazon-vpc-architecture-with-new-quick-start) Build a modular virtual network architecture with Amazon VPC in 5 minutes with our new Quick Start
- [Specifying the VPC for your Amazon RDS DB Instance](https://aws.amazon.com/about-aws/whats-new/2016/08/specifying-the-vpc-for-your-amazon-rds-db-instance/) You can now easily change the Amazon VPC used by your Amazon RDS DB instance!
- [awsfundamentals.blogspot.com: AWS Virtual Private Cloud - VPC](https://awsfundamentals.blogspot.com/2019/12/aws-vpc-fundamental.html)
- [Reduce Cost and Increase Security with Amazon VPC Endpoints](https://aws.amazon.com/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/)
- [ealtili.medium.com: Deepdive to VPCs and Connections to VPC](https://ealtili.medium.com/deepdive-to-vpcs-and-connections-to-vpc-2de3fb164d7c)
- [Centralize access using VPC interface endpoints to access AWS services across multiple VPCs](https://aws.amazon.com/blogs/networking-and-content-delivery/centralize-access-using-vpc-interface-endpoints/)

### AWS Client VPN
- [cloudonaut.io: AWS Client VPN: Connected with the Cloud](https://cloudonaut.io/aws-client-vpn-connected-with-the-cloud/)

### Tailscale
- [tailscale.com: Connect to an AWS VPC using subnet routes](https://tailscale.com/kb/1021/install-aws/)

## AWS SQS. Amazon Simple Queue Service
- [Limits in Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html)
- [Amazon SQS FAQs](https://aws.amazon.com/sqs/faqs/)

## AWS Application Discovery Service Update. Agentless Discovery for VMware 
- [AWS Application Discovery Service Update – Agentless Discovery for VMware](https://aws.amazon.com/es/blogs/aws/aws-application-discovery-service-update-agentless-discovery-for-vmware/)

## VMware Cloud on AWS
- [VMware Cloud on AWS](https://aws.amazon.com/es/vmware/) The Only Way to Extend Your VMware Environment into AWS
- [infoworld.com: 4 no-bull insights into the AWS/VMware deal](http://www.infoworld.com/article/3131347/hybrid-cloud/4-no-bull-insights-into-the-awsvmware-deal.html)

## AWS Developer Blog
- [The AWS Developer Blog now includes Python & GoLang](https://aws.amazon.com/blogs/developer/)
- [Create an API Using the Swagger Specification and the API Gateway Extensions](http://docs.aws.amazon.com/apigateway/latest/developerguide/create-api-using-import-export-api.html)

## AWS Application Services
- [k21academy.com: AWS Application Services: Lambda, SES, SNS, SQS, SWF](https://k21academy.com/amazon-web-services/aws-solutions-architect/aws-application-services/)

## AWS Serverless
- [martinfowler.com: Serverless Architectures](http://martinfowler.com/articles/serverless.html)
- [you can use Python with AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
- [Build a Python Microservice with Amazon Web Services Lambda & API Gateway](http://www.giantflyingsaucer.com/blog/?p=5730)
- [AWS Lambda, Echo, and the Future of Cloud Automation](http://www.logicworks.net/blog/2016/01/aws-lambda-echo-cloud-automation/) A fantastic blog article by Logicworks on Lambda, the coming move to serverless architecture and even the possibility of using Amazon's Echo to launch entire AWS environments by using just your voice
- [Serverless: The Future of Software Architecture?](https://read.acloud.guru/serverless-the-future-of-software-architecture-d4473ffed864#.uk7setw47)
- [npmjs.com: Lambda load test](https://www.npmjs.com/package/lambda-load-test)
- [AWS Lambda Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
- [blog.powerupcloud.com: AWS inventory details in CSV using lambda](http://blog.powerupcloud.com/2016/02/07/aws-inventory-details-in-csv-using-lambda)
- [How do I stop and start EC2 instances at regular intervals using AWS Lambda? (Video)](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)
- [Youtube channel: AWS Serverless](https://www.youtube.com/channel/UC_vJsnqdpuEoRseFmlkHMkA)
- [Using Amazon EFS for AWS Lambda in your serverless applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/)
- [medium: AWS Serverless Application Lens — A Summary](https://medium.com/swlh/aws-serverless-application-lens-a-summary-4f740c4f376d) 
- [blog.usejournal.com: Building a Serverless Back-end with AWS](https://blog.usejournal.com/building-a-serverless-back-end-with-aws-5bb3642a3f4)
- [dashbird.io: Deploying AWS Lambda with Docker Containers: I Gave it a Try and Here’s My Review](https://dashbird.io/blog/deploying-aws-lambda-with-docker/)
- [aws.amazon.com: Operating Lambda: Understanding event-driven architecture – Part 1](https://aws.amazon.com/blogs/compute/operating-lambda-understanding-event-driven-architecture-part-1/)
- [aws.amazon.com: Optimizing Lambda functions packaged as container images](https://aws.amazon.com/es/blogs/compute/optimizing-lambda-functions-packaged-as-container-images/)
- [Security Overview of AWS Lambda](https://d1.awsstatic.com/whitepapers/Overview-AWS-Lambda-Security.pdf)
- [cloudonaut.io: Serverless Hybrid Cloud: Accessing an API Gateway via VPN or Direct Connect](https://cloudonaut.io/serverless-hybrid-cloud-accessing-an-api-gateway-via-vpn-or-direct-connect/)
- [infoworld.com: Serverless computing with AWS Lambda, Part 1](https://www.infoworld.com/article/3210726/serverless-computing-with-aws-lambda.html) Get an overview of AWS Lambda's nanoservices architecture and execution model, then build your first Lambda function in Java
- [dashbird.io: 4 Tips for AWS Lambda Optimization for Production](https://dashbird.io/blog/optimizing-aws-lambda-for-production/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [kothiyal-anuj.medium.com: Serverless Diary: The Ultimate Guide to **Caching in the Cloud**](https://kothiyal-anuj.medium.com/serverless-diary-the-ultimate-guide-to-caching-in-the-cloud-249f6a06915f)
- [medium: Going Serverless (on AWS)](https://medium.com/galvanize/going-serverless-on-aws-116a04a0defd)
- [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/)
- [Introducing AWS SAM Pipelines: Automatically generate deployment pipelines for serverless applications](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications)
- [Simplify CI/CD configuration for serverless applications and your favorite CI/CD system — Public Preview](https://aws.amazon.com/about-aws/whats-new/2021/07/simplify-ci-cd-configuration-serverless-applications-your-favorite-ci-cd-system-public-preview/)
- [Building a Serverless Back-end with AWS](https://blog.usejournal.com/building-a-serverless-back-end-with-aws-5bb3642a3f4)
- [liavyona09.medium.com: Spice up Your Kubernetes Environment with AWS Lambda](https://liavyona09.medium.com/spice-up-your-kubernetes-environment-with-aws-lambda-a07d81347607)
- [Achieve up to 34% better price/performance with AWS Lambda Functions powered by AWS Graviton2 processor](https://aws.amazon.com/about-aws/whats-new/2021/09/better-price-performance-aws-lambda-functions-aws-graviton2-processor/)

## AWS API Gateway
- [alexdebrie.com: A Detailed Overview of AWS API Gateway](https://www.alexdebrie.com/posts/api-gateway-elements/)

## AWS CloudFormation. Free Templates
- [AWS Cloud Formation Release History](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)
- [All the AWS Resource Types Reference for AWS CloudFormation ](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
- [Introducing Cloud Formation Guard - a new opensource CLI for infrastructure compliance](https://aws.amazon.com/about-aws/whats-new/2020/06/introducing-aws-cloudformation-guard-preview/)
	- [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) Guard offers a policy-as-code domain-specific language (DSL) to write rules and validate JSON- and YAML-formatted data such as CloudFormation Templates, K8s configurations, and Terraform JSON plans/configurations against those rules.
- [cloudonaut.io: Getting Started with Free Templates for AWS CloudFormation](https://cloudonaut.io/getting-started-with-aws-cf-templates/) - [Free Templates for AWS CloudFormation](https://github.com/widdix/aws-cf-templates/) - [templates.cloudonaut.io](https://templates.cloudonaut.io/)
- [Use Git pre-commit hooks to avoid AWS CloudFormation errors](https://aws.amazon.com/es/blogs/infrastructure-and-automation/use-git-pre-commit-hooks-avoid-aws-cloudformation-errors/)
- [Introducing a Public Registry for AWS CloudFormation](https://aws.amazon.com/es/blogs/aws/introducing-a-public-registry-for-aws-cloudformation/)
- [cloudkatha.com: How to Setup S3 Bucket CORS Configuration using CloudFormation](https://cloudkatha.com/how-to-setup-s3-bucket-cors-configuration-using-cloudformation)
- [cloudkatha.com: How to Configure AWS SQS Dead Letter Queue using CloudFormation](https://cloudkatha.com/how-to-configure-aws-sqs-dead-letter-queue-using-cloudformation/)
- [cloudkatha.com: How to Create an S3 Bucket using CloudFormation](https://cloudkatha.com/how-to-create-an-s3-bucket-using-cloudformation/)
- [cloudkatha.com: How to use CloudFormation to Create SNS Topic and Subscription](https://cloudkatha.com/how-to-use-cloudformation-to-create-sns-topic-and-subscription/)

## Infrastructure Code Template Generators
- [aws.amazon.com: Amazon EC2 announces Spot Blueprints, an infrastructure code template generator to get started with EC2 Spot Instances](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-ec2-announces-spot-blueprints-an-infrastructure-code-template-generator-to-get-started-with-ec2-spot-instances/)

### Former2 to generate IaC templates
- [former2.com](https://former2.com/)
- [Accelerate infrastructure as code development with open source Former2](https://aws.amazon.com/blogs/opensource/accelerate-infrastructure-as-code-development-with-open-source-former2/)


## AWS for Windows
- [blog.rackspace.com: Patch and AMI Management for Windows on AWS](http://blog.rackspace.com/patch-and-ami-management-for-windows-on-aws) step-by-step guide about patch and AMI management for Windows on AWS

## Continuous Deployment with AWS
- [Continuous Deployment with AWS](https://aws.amazon.com/blogs/devops/tag/continuous-deployment/)

## AWS Security
- [AWS Security Blog](http://blogs.aws.amazon.com/security)
- [AWS Security](https://aws.amazon.com/security/)
- [AWS Security docs](https://docs.aws.amazon.com/security/)
- [Tutorial: Configure Apache Web Server on Amazon Linux to use SSL/TLS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html)
- [The Most Popular AWS Security Blog Posts in 2015](http://blogs.aws.amazon.com/security/post/Tx4QX7W51NDSLO/The-Most-Popular-AWS-Security-Blog-Posts-in-2015)
- [dzone: Private Subnets Are Broken on AWS](https://dzone.com/articles/private-subnets-are-broken-on-aws)
- [Amazon’s customer service backdoor](https://medium.com/@espringe/amazon-s-customer-service-backdoor-be375b3428c4#.qyixu5mu3)
- [Announcing Industry Best Practices for Securing AWS Resources](http://blogs.aws.amazon.com/security/post/Tx3PTTZB14FWPBA/Announcing-Industry-Best-Practices-for-Securing-AWS-Resources)
- [The Most Viewed AWS Security Blog Posts so Far in 2016](http://blogs.aws.amazon.com/security/post/Tx2N52FR8XGJVL3/The-Most-Viewed-AWS-Security-Blog-Posts-so-Far-in-2016)
- [Oracle Database Encryption Options on Amazon RDS](https://aws.amazon.com/es/blogs/apn/oracle-database-encryption-options-on-amazon-rds/)
- [Learn AWS Security Fundamentals with Free and Online Training](https://aws.amazon.com/about-aws/whats-new/2016/06/learn-aws-security-fundamentals-with-free-and-online-training)
- [How to Restrict Amazon S3 Bucket Access to a Specific IAM Role](http://blogs.aws.amazon.com/security/post/TxK5WUJK3DG9G8/How-to-Restrict-Amazon-S3-Bucket-Access-to-a-Specific-IAM-Role)
- [Updated Whitepaper Available: AWS Best Practices for DDoS Resiliency](http://blogs.aws.amazon.com/security/post/Tx6QAIBSQTJPHB/Updated-Whitepaper-Available-AWS-Best-Practices-for-DDoS-Resiliency)
- [AWS Security Blog: In Case You Missed These: AWS Security Blog Posts from June, July, and August 2016](http://blogs.aws.amazon.com/security/post/Tx3KVD6T490MM47/In-Case-You-Missed-These-AWS-Security-Blog-Posts-from-June-July-and-August)
- [Amazon Inspector Announces General Availability for Windows](https://aws.amazon.com/es/about-aws/whats-new/2016/08/amazon-inspector-announces-general-availability-for-windows/)
- [encrypt and decrypt data: Importing Key Material in AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) Use your own encryption keys with AWS Key Management Service.
- [Amazon s2n: AWS’s new Open Source implementation of the SSL/TLS network encryption protocols](http://blogs.aws.amazon.com/security/post/TxLEHNNDPUFDU9/Automated-Reasoning-and-Amazon-s2n)
- [dzone: 9 AWS Security Best Practices: Securing Your AWS Cloud](https://dzone.com/articles/9-aws-security-best-practices-securing-your-aws-cl) Working with Amazon facilities, it is necessary to implement AWS security best practices to ensure the safety of the data and the cloud.
- [Encrypt global data client-side with AWS KMS multi-Region keys](https://aws.amazon.com/blogs/security/encrypt-global-data-client-side-with-aws-kms-multi-region-keys/) Today, AWS Key Management Service (AWS KMS) is introducing multi-Region keys, a new capability that lets you replicate keys from one Amazon Web Services (AWS) Region into another. Multi-Region keys are designed to simplify management of client-side encryption when your encrypted data has to be copied into other Regions for disaster recovery or is replicated in Amazon DynamoDB global tables.
- [dzone: Removing the Bastion Host and Improving the Security in AWS](https://dzone.com/articles/removing-the-bastion-host-and-improving-the-securi) This article covers the security in AWS and overcoming the classic SSH/RDP jump with a better alternative for all OS.
- [acloudguru.com: How to audit and secure an AWS account](https://acloudguru.com/blog/engineering/how-to-audit-and-secure-an-aws-account)
- [yobyot.com: AWS multi-region KMS keys and Data Lifecycle Manager: better together](https://www.yobyot.com/aws/aws-multi-region-keys-and-ec2-data-lifecycle-manager/2021/08/18/)
- [try.jupiterone.com: The Absolute Minimum Every Developer Must Know about AWS Security](https://try.jupiterone.com/the-absolute-minimum-every-developer-must-know-about-aws-security)

### Policy as Code with AWS CDK and Open Policy Agent
- [Realize Policy-as-Code with AWS Cloud Development Kit through Open Policy Agent 🌟](https://aws.amazon.com/blogs/opensource/realize-policy-as-code-with-aws-cloud-development-kit-through-open-policy-agent/)

### Payment Card Industry Data Security Standard compliance
- [PCI DSS Standardized Architecture on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/05/pci-dss-standardized-architecture-on-the-aws-cloud-quick-start-reference-deployment/)

### AWS IAM
- [AWS Identity and Access Management - Getting Started](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
- [AWS Identity and Access Management (IAM) best practices in 2016](http://blogs.aws.amazon.com/security/post/Tx2OB7YGHMB7WCM/Adhere-to-IAM-Best-Practices-in-2016)
- [How to Record and Govern Your IAM Resource Configurations Using AWS Config](http://blogs.aws.amazon.com/security/post/Tx14ADBJOCAT9NS/How-to-Record-and-Govern-Your-IAM-Resource-Configurations-Using-AWS-Config)
- [How to Use SAML to Automatically Direct Federated Users to a Specific AWS Management Console Page](http://blogs.aws.amazon.com/security/post/Tx2CGWIB8SBYW2J/How-to-Use-SAML-to-Automatically-Direct-Federated-Users-to-a-Specific-AWS-Manage)
- [New IAMCTL tool compares multiple IAM roles and policies](https://aws.amazon.com/es/blogs/security/new-iamctl-tool-compares-multiple-iam-roles-and-policies/)
- [Bring your own CLI to Session Manager with configurable shell profiles](https://aws.amazon.com/es/blogs/mt/bring-your-own-cli-session-manager-configurable-shell-profiles/)
- [keepler.io: Gestionando el control de accesos en nuestro data lake en AWS](https://keepler.io/2021/03/gestionando-el-control-de-accesos-en-nuestro-data-lake-en-aws/)
- [aws.amazon.com: IAM Access Analyzer now supports over 100 policy checks with actionable recommendations to help you author secure and functional policies](https://aws.amazon.com/about-aws/whats-new/2021/03/iam-access-analyzer-supports-over-100-policy-checks-with-actionable-recommendations/)
- [aws.amazon.com: IAM Access Analyzer Update – Policy Validation](https://aws.amazon.com/blogs/aws/iam-access-analyzer-update-policy-validation/)
- [netflixtechblog.com: ConsoleMe: A Central Control Plane for AWS Permissions and Access](https://netflixtechblog.com/consoleme-a-central-control-plane-for-aws-permissions-and-access-fd09afdd60a8) - [github.com/Netflix/consoleme](https://github.com/Netflix/consoleme)
- [cloudkatha.com: Difference between Root User and IAM User in AWS You Need to Know](https://cloudkatha.com/difference-between-root-user-and-iam-user-in-aws-you-need-to-know/)
- [ben11kehoe.medium.com: AWS Authentication: Principals (users and roles) in AWS IAM](https://ben11kehoe.medium.com/principals-in-aws-iam-38c4a3dc322a) this article uses the boto3, the AWS Python SDK, as an example, but other SDKs have analogous features.

### AWS Organizations
- [Simplifying permissions management at scale using tags in AWS Organizations](https://aws.amazon.com/blogs/mt/simplifying-permissions-management-at-scale-using-tags-in-aws-organizations/)
- [Standardize compliance in AWS using DevOps and a Cloud Center of Excellence (CCOE) approach](https://aws.amazon.com/blogs/mt/standardize-compliance-in-aws-using-devops-and-a-cloud-center-of-excellence-ccoe-approach/)

### AWS CloudFront
- [Amazon CloudFront now supports HTTP/2](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-cloudfront-now-supports-http2/)

### AWS Firewalls
- [doit-intl.com: AWS Firewalls 101: How and when to use each one](https://blog.doit-intl.com/aws-firewalls-101-how-and-when-to-use-each-one-d4ad8087a6b3)
- [Automatically block suspicious traffic with AWS Network Firewall and Amazon GuardDuty](https://aws.amazon.com/es/blogs/security/automatically-block-suspicious-traffic-with-aws-network-firewall-and-amazon-guardduty)

### AWS WAF Web Application Firewall
- [AWS WAF - Web Application Firewall](https://aws.amazon.com/waf/)
- [How to Automatically Update Your Security Groups for Amazon CloudFront and AWS WAF by Using AWS Lambda (boto3 python)](http://blogs.aws.amazon.com/security/post/Tx1LPI2H6Q6S5KC/How-to-Automatically-Update-Your-Security-Groups-for-Amazon-CloudFront-and-AWS-W)
- [How to Use AWS WAF to Block IP Addresses That Generate Bad Requests](http://blogs.aws.amazon.com/security/post/Tx223ZW25YRPRKV/How-to-Use-AWS-WAF-to-Block-IP-Addresses-That-Generate-Bad-Requests)
- [How to Reduce Security Threats and Operating Costs Using AWS WAF and Amazon CloudFront](http://blogs.aws.amazon.com/security/post/Tx1G747SE1R2ZWE/How-to-Reduce-Security-Threats-and-Operating-Costs-Using-AWS-WAF-and-Amazon-Clou)
- [AWS WAF sample rules](https://github.com/awslabs/aws-waf-sample)
- [medium: Blocking bots using AWS WAF](https://medium.com/cloud-techies/blocking-bots-using-aws-waf-d449e6d159ca)
- [medium: Protecting your Web Application or APIs using AWS WAF](https://medium.com/avmconsulting-blog/protecting-your-web-application-or-apis-using-aws-waf-1829ff79275a)

### AWS Vault
- [AWS Vault](https://github.com/99designs/aws-vault) is a tool to securely store and access AWS credentials in a development environment.
- [AWS: Sourcing AWS CLI Credentials using a Custom AWS CLI Credential Provider and AWS Vault](https://thomas.geens.be/2020/05/24/aws-sourcing-aws-cli-credentials-using-a-custom-aws-cli-credential-provider-and-aws-vault/)

## AWS S3 & EBS. AWS Storage Gateway
- [S3 FAQ](https://aws.amazon.com/s3/faqs/)
- [Making Requests to Amazon S3 over IPv6](http://docs.aws.amazon.com/AmazonS3/latest/dev/ipv6-access.html) Amazon Simple Storage Service (Amazon S3) supports the ability to access S3 buckets using the Internet Protocol version 6 (IPv6), in addition to the IPv4 protocol.
- [How to Build Sparse EBS Volumes for Fun and Easy Snapshotting](https://aws.amazon.com/blogs/apn/how-to-build-sparse-ebs-volumes-for-fun-and-easy-snapshotting/)
- [Getting Started with AWS Storage Gateway](http://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStarted-common.html)
- [devopscube.com: How to Automate EBS Snapshot Creation, Retention and Deletion](https://devopscube.com/automate-ebs-snapshot-creation-deletion/)
- [cloudkatha.com: Is S3 Region Specific or Global? What do you think?](https://cloudkatha.com/is-s3-region-specific-or-global-what-do-you-think/)
- [cloudkatha.com: This is why S3 Bucket Names are unique Globally](https://cloudkatha.com/why-s3-bucket-names-are-unique-globally/)
- [cloudkatha.com: AWS S3 Storage Classes: Everything You Need to Know](https://cloudkatha.com/aws-s3-storage-classes-everything-you-need-to-know/)
- [A step-by-step guide to synchronize data between Amazon S3 buckets](https://aws.amazon.com/blogs/storage/a-step-by-step-guide-to-synchronize-data-between-amazon-s3-buckets)
- [percona.com: Performance of Various EBS Storage Types in AWS](https://www.percona.com/blog/performance-of-various-ebs-storage-types-in-aws/)
- [harness.io: Tutorial: [Artifact Servers] S3 – How to Provide Cross-Account Access Via Bucket Policies](https://harness.io/blog/devops/tutorial-s3-cross-account/)

## Amazon EFS Elastic File System
- [EFS Elastic File System](https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-production-ready-in-three-regions)
- [Amazon Elastic File System triples read throughput](https://aws.amazon.com/about-aws/whats-new/2021/01/amazon-elastic-file-system-triples-read-throughput/)

## AWS Transfer
- [infoq.com: AWS Transfer Family Introduces Support for EFS](https://www.infoq.com/news/2021/01/aws-transfer-ftp-efs/)

## AWS Fargate
- [Amazon EFS with Amazon ECS and AWS Fargate – Part 1](https://aws.amazon.com/es/blogs/containers/developers-guide-to-using-amazon-efs-with-amazon-ecs-and-aws-fargate-part-1/)

### Admiralty
- [admiralty.io](https://admiralty.io/) The simplest way to deploy applications to multiple Kubernetes clusters.
- [thenewstack.io: Making Kubernetes Serverless and Global with AWS Fargate on EKS and Admiralty](https://thenewstack.io/making-kubernetes-serverless-and-global-with-aws-fargate-on-eks-and-admiralty/)
  - [admiralty.io: Multi-Region AWS Fargate on EKS](https://admiralty.io/docs/tutorials/fargate/)

## AWS Backup and Recovery. Design for failure
- [Quantum Taps AWS for Cloud-Powered Disaster Recovery](http://www.infostor.com/backup-and_recovery/quantum-taps-aws-for-cloud-powered-disaster-recovery.html)
- [Linkedin discussion: Need help on Backup and restore methods of EC2 using s3 services](https://www.linkedin.com/groups/49531/49531-6093375473969090562)
- [Design for failure lessons learnt from the Sydney AWS outage](https://www.hava.io/blog/design-for-failure-lessons-learnt-from-the-sydney-aws-outage)
- [Chaos Monkey](https://github.com/Netflix/SimianArmy/wiki/Chaos-Monkey) The Netflix Chaos Monkey tool allows you to proactively launch attack code against your infrastructure to cause failures and give you the chance to fix potential problems before they occur on their own. 
- [Udemy - AWS: How to Architect with a Design for Failure Approach](https://www.udemy.com/how-to-architect-with-a-design-for-failure-approach/)
- [How to Restore Your Instance Data from a Backup using Snapshots on AWS EC2/EBS](https://www.cloudinsidr.com/content/how-to-restore-your-instance-data-from-a-backup-using-snapshots-on-aws-ec2ebs/)
- [Backup and archive to AWS Storage Gateway VTL with Veeam Backup & Replication v9](https://aws.amazon.com/es/about-aws/whats-new/2016/08/backup-and-archive-to-aws-storage-gateway-vtl-with-veeam-backup-and-replication-v9/)

## AWS Config Rules
- [AWS Config Rules now available in 4 new regions: US West (Oregon), EU (Ireland), EU (Frankfurt) and Asia Pacific (Tokyo)](https://aws.amazon.com/es/about-aws/whats-new/2016/04/aws-config-rules-now-available-in-4-new-regions-us-west-oregon-eu-ireland-eu-frankfurt-and-asia-pacific-tokyo/)

## AWS Big Data 
- [aws.amazon.com/big-data](http://aws.amazon.com/big-data)
- [blogs.aws.amazon.com/bigdata](http://blogs.aws.amazon.com/bigdata/)
- [Querying Amazon Kinesis Streams Directly with SQL and Spark Streaming](https://aws.amazon.com/blogs/big-data/querying-amazon-kinesis-streams-directly-with-sql-and-spark-streaming/)
- [Using Spark SQL for ETL](http://blogs.aws.amazon.com/bigdata/post/Tx2D93GZRHU3TES/Using-Spark-SQL-for-ETL)
- [whizlabs.com: AWS Kinesis vs Kafka Apache](https://www.whizlabs.com/blog/kinesis-vs-kafka/)

### AWS Data Lake
- [Building a Data Lake on AWS](https://aws.amazon.com/big-data/data-lake-on-aws/) AWS provides a highly scalable, flexible, secure, and cost-effective solution for your organization to build a Data Lake – a data repository for both structured and unstructured data that is designed to be easily accessible for on-demand data analytics enabling you to answer questions as they arise.

### AWS Data Pipeline (aka Big Data Pipelines or Data Streams)
- [AWS Data Pipeline](https://aws.amazon.com/datapipeline/)
- [AWS Data Pipeline Documentation](https://docs.aws.amazon.com/data-pipeline/index.html)
- [medium: No-Code Data Collect API on AWS](https://medium.com/@dima.statz_89242/no-code-data-collect-api-on-aws-d79e3681d204) A No-Code Data Collections mechanism for Big Data Pipelines on AWS.
- [AWS Big Data Blog: Category - AWS Data Pipeline](https://aws.amazon.com/blogs/big-data/category/analytics/aws-data-pipeline/)

## AWS NoSQL DynamoDB
- [Easily model your app data in a NoSQL database with AWS Mobile Hub](https://aws.amazon.com/es/about-aws/whats-new/2016/06/easily-model-your-app-data-in-a-nosql-database-with-aws-mobile-hub/)
- [medium: An Ultimate Guide to AWS Serverless database — DynamoDB](https://medium.com/javascript-in-plain-english/an-ultimate-guide-to-aws-serverless-database-dynamodb-aa048a62f2da) AWS DynamoDb is a fully managed, NoSQL, Single digit latency, a serverless database that can handle any kind of online workloads.

## AWS IoT
- [aws.amazon.com/en/iot](https://aws.amazon.com/en/iot)
- [What Is AWS IoT?](http://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

## AWS Elastic Transcoder. Video streaming
- [Settings that You Specify When You Create an Elastic Transcoder Job](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/job-settings.html)

## AWS and Splunk
- [blogs.splunk.com: AWS Agility + Splunk Visibility = Customer Success](http://blogs.splunk.com/2016/06/22/aws-video/)

## AWS Monitoring
- [github: Steps I used to install Nagios in the cloud](https://github.com/andrewpuch/nagios_setup)
- [github: ElectricEye](https://github.com/jonrau1/ElectricEye/blob/master/README.md) is a set of Python scripts (affectionately called Auditors) that continuously monitor your AWS infrastructure looking for configurations related to confidentiality, integrity and availability that do not align with AWS best practices.
- [medium: AWS Account Security Monitoring](https://medium.com/swlh/aws-account-security-monitoring-d7ca129d52ac)

## Amazon Alexa. Voice User Interface
- [New Alexa Skills Kit Template: Build a Trivia Skill in under an Hour](https://developer.amazon.com/public/community/post/TxDJWS16KUPVKO/New-Alexa-Skills-Kit-Template-Build-a-Trivia-Skill-in-under-an-Hour)

## AWS Partner Network (APN)
- [AWS Partner Network](https://aws.amazon.com/partners/)
	- [APN Technology Partners](https://aws.amazon.com/partners/technology/)
	- [APN Consulting Partners](https://aws.amazon.com/partners/consulting/)
- [AWS Partner Network (APN) blog](https://aws.amazon.com/blogs/apn/)
	- [Active Directory Single Sign-On (SSO) on AWS with Bitium](https://aws.amazon.com/blogs/apn/active-directory-single-sign-on-sso-on-aws-with-bitium)
    - [How to Deploy a High Availability Web Service on AWS Using Spotinst](https://aws.amazon.com/blogs/apn/how-to-deploy-a-high-availability-web-service-on-aws-using-spotinst/)

## AWS Startup Collection. For startups building on AWS
- [bitmovin: Improving Video Quality on the Web](https://medium.com/aws-activate-startup-blog/bitmovin-improving-video-quality-on-the-web-8670039c4334)
- [What Startups Should Know about Amazon VPC — Part 1](https://medium.com/aws-activate-startup-blog/what-startups-should-know-about-amazon-vpc-part-1-bebe94b7f228)
- [Scaling on AWS (Part 3): >500K Users](https://medium.com/aws-activate-startup-blog/scaling-on-aws-part-3-500k-users-3750b227b761)
- [medium.com: Building a Serverless Dynamic DNS System with AWS](https://medium.com/aws-activate-startup-blog/building-a-serverless-dynamic-dns-system-with-aws-a32256f0a1d8#.qq54pucbd)
- [medium.com: The Top 10 AWS Startup Blog Posts of 2015](https://medium.com/aws-activate-startup-blog/the-top-10-aws-startup-blog-posts-of-2015-d2975e3778bb)

## AWS ECS
- [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks/)
- [medium: Creating CI/CD Pipeline for AWS ECS — Part I](https://medium.com/@harshvijaythakkar/creating-ci-cd-pipeline-for-aws-ecs-part-i-b2f61bb1522f)
- [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform](https://www.clickittech.com/aws/amazon-ecs-vs-eks/)
- [dev.to: Sharing secrets to ECS in an AWS multi-account architecture](https://dev.to/aws-builders/sharing-secrets-to-ecs-in-an-aws-multi-account-architecture-5h1i)
- [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes/)
- [neal-davis.medium.com: ECS vs EC2 vs Lambda](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)

## Rancher on AWS
- [aws-quickstart.github.io: Rancher on the AWS Cloud. Quick Start Reference Deployment](https://aws-quickstart.github.io/quickstart-eks-rancher/)

## AWS App Mesh 
- [AWS App Mesh Workshop](https://www.appmeshworkshop.com/)
- [amazon.com: Leveraging App Mesh with Amazon EKS in a Multi-Account environment](https://aws.amazon.com/blogs/containers/leveraging-app-mesh-with-amazon-eks-in-a-multi-account-environment/)

## AWS Fargate
- [Deploy Machine Learning Pipeline on AWS Fargate](https://www.kdnuggets.com/2020/07/deploy-machine-learning-pipeline-aws-fargate.html)

## Interview Questions
- [intellipaat.com: Top Amazon AWS Interview Questions – Most Asked](https://intellipaat.com/blog/interview-question/amazon-aws-interview-questions/)
- [Frequently Asked AWS Interview Questions](https://www.interviewbit.com/aws-interview-questions/)

## Local Testing
- [Amazon EC2 Metadata Mock](https://github.com/aws/amazon-ec2-metadata-mock)

### Localstack
- [localstack.cloud](https://localstack.cloud/) Develop and test your cloud apps offline. A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline! 
- [github.com/localstack/localstack](https://github.com/localstack/localstack)

## Migrating On Premise VM to AWS
- [youtube: Migrating On Premise VM to AWS | VM Import/Export | Create EC2 instance based on on-premises server](https://youtu.be/buzusNljpy4)

## AWS configuration files
- [medium: AWS configuration files, explained](https://medium.com/@ben11kehoe/aws-configuration-files-explained-9a7ea7a5b42e)

## Open Source at AWS
- [OpenSource at AWS](https://aws.github.io/)

## AWS Service Quota Requests
- [How can I troubleshoot errors using the AWS CLI to manage my service quota requests?](https://aws.amazon.com/es/premiumsupport/knowledge-center/troubleshoot-service-quotas-cli-commands/)
- [AWS API: get-service-quota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-service-quota.html) 

## Resource Hierarchies
- [AWS, Azure, GCP: Resource Hierarchies](https://levelup.gitconnected.com/aws-azure-gcp-resource-hierarchies-25b829127511)

## AWS Systems Manager Explorer
- [Multi-account AWS Trusted Advisor summaries now available in AWS Systems Manager Explorer](https://aws.amazon.com/blogs/mt/multi-account-aws-trusted-advisor-summaries-now-available-aws-systems-manager-explorer/)

## AWS Systems Manager Incident Manager
- [How to automate incident response to security events with AWS Systems Manager Incident Manager](https://aws.amazon.com/blogs/security/how-to-automate-incident-response-to-security-events-with-aws-systems-manager-incident-manager/)

## AWS Managed Services for Prometheus and Grafana
- [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) Highly available, secure, and managed monitoring for your containers
- [Amazon Managed Service for Grafana](https://aws.amazon.com/grafana/) Powerful, interactive data visualizations for builders, operators, and business leaders
- [infoq.com: AWS Introduces Amazon Managed Service for Grafana and Amazon Managed Service for Prometheus](https://www.infoq.com/news/2021/01/aws-grafana-prometheus/)

## AWS Chaos Engineeering. AWS Fault Injection Simulator 
- [techcrunch.com: AWS introduces new Chaos Engineering as a Service offering](https://techcrunch.com/2020/12/15/aws-introduces-new-chaos-engineering-as-a-service-offering/)

## Best Practices
- [thenewstack.io: Avoid the 5 Most Common Amazon Web Services Misconfigurations in Build-Time](https://thenewstack.io/avoid-the-5-most-common-amazon-web-services-misconfigurations-in-build-time/)
- [zarantech.com: Top 5 Pillars of AWS Well-Architected Structure](https://www.zarantech.com/blog/top-5-pillars-of-aws-well-architected-structure/)
- [foreseeti.com: How to become and stay AWS well architected in a smart way](https://foreseeti.com/how-to-become-and-stay-aws-well-architected-in-a-smart-way/)

## New Features
- [thenewstack.io: HashiCorp Adds Consul and Vault to Cloud Platform for AWS](https://thenewstack.io/hashicorp-adds-consul-and-vault-to-cloud-platform-for-aws/)
- [Amazon EKS clusters now support user authentication with OIDC compatible identity providers](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-eks-clusters-support-user-authentication-oidc-compatible-identity-providers/)
- [Amazon Managed Service for Grafana (AMG) preview updated with new capabilities](https://aws.amazon.com/blogs/mt/amazon-managed-service-for-grafana-amg-preview-updated-with-new-capabilities/)
- [xataka.com: Hasta AWS se pasa al low-code: Workflow Studio es su primera herramienta de desarrollo de bajo código](https://www.xataka.com/pro/aws-se-pasa-al-low-code-workflow-studio-su-primera-herramienta-desarrollo-codigo)
- [Easily Manage Security Group Rules with the New Security Group Rule ID](https://aws.amazon.com/blogs/aws/easily-manage-security-group-rules-with-the-new-security-group-rule-id)
- [Amazon Virtual Private Cloud (VPC) customers can now assign IP prefixes to their EC2 instances](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-virtual-private-cloud-vpc-customers-can-assign-ip-prefixes-ec2-instances)
- [AWS Network Firewall – Nuevo Servicio Gestionado de Firewall para VPC](https://aws.amazon.com/es/blogs/aws-spanish/aws-network-firewall-nuevo-servicio-gestionado-de-firewall-para-vpc/)
- [Amazon EC2 Auto Scaling now lets you control which instances to terminate on scale-in](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-ec2-auto-scaling-now-lets-you-control-which-instances-to-terminate-on-scale-in/)
- [EC2-Classic Networking is Retiring – Here’s How to Prepare](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/)
- [Announcing General Availability of Amazon Redshift Cross-account Data Sharing](https://aws.amazon.com/about-aws/whats-new/2021/08/announcing-general-availability-amazon-redshift-cross-account-data-sharing/)
- [infoq.com: Amazon Introduces Cloudwatch Cross Account Alarms to Consolidate Management](https://www.infoq.com/news/2021/08/aws-cloudwatch-alarms/)
- [Monitor, Evaluate, and Demonstrate Backup Compliance with AWS Backup Audit Manager](https://aws.amazon.com/blogs/aws/monitor-evaluate-and-demonstrate-backup-compliance-with-aws-backup-audit-manager/)
- [Amazon Managed Grafana Is Now Generally Available with Many New Features](https://aws.amazon.com/blogs/aws/amazon-managed-grafana-is-now-generally-available-with-many-new-features)

## Superwerker
- [superwerker](https://aws.amazon.com/quickstart/architecture/superwerker/) Automates AWS Cloud deployments backed by decades of expertise and best practices

## Tools
- [ec2-spot-converter](https://github.com/jcjorel/ec2-spot-converter) This tool converts existing EC2 instances back and forth from on-demand and 'persistent' Spot billing models while preserving instance attributes (Launch configuration, Tags..), network attributes (existing Private IP addresses, Elastic IP), storage (Volumes), Elastic Inference accelerators and Elastic GPUs. It also allows replacement of existing Spot instances with new "identical" ones to update the instance type and cpu options.  
- [github.com/aws-samples/aws-auto-inventory: AWS Automated Inventory](https://github.com/aws-samples/aws-auto-inventory) A command line tool that allows you to quickly and easily generate inventory reports of your AWS resources.
- [github.com/aws-samples/aws-waf-ops-dashboards](https://github.com/aws-samples/aws-waf-ops-dashboards) In this repository, we share code for building infrastructure to collect, enrich, and visualize AWS Web Application Firewall logs. Implementing this project in your AWS account will allow you to view and filter the logs through Kibana dashboards below, as well as customize views and dashboards to your needs.

## Third party tools
- [techcrunch.com: Vantage makes managing AWS easier](https://techcrunch.com/2021/01/12/vantage-makes-managing-aws-easier/)
- [vantage.sh](https://www.vantage.sh/)

## AWS Amplify
- [blog.logrocket.com: AWS Amplify and React Native: A tutorial](https://blog.logrocket.com/aws-amplify-and-react-native-a-tutorial/)
- [dev.to: 10 New AWS Amplify Features to Check Out](https://dev.to/aws/10-new-aws-amplify-features-to-check-out-4291)

## AWS Control Tower
- [AWS Control Tower](https://aws.amazon.com/controltower/) The easiest way to set up and govern a secure multi-account AWS environment

## Spain
- [xataka.com: Por qué Amazon ha elegido Aragón para instalar sus tres primeros centros de datos en España](https://www.xataka.com/servicios/que-amazon-ha-elegido-aragon-para-instalar-sus-tres-primeros-centros-datos-espana)
- [RESOURCE HUB: Eventos y webinars de AWS](https://emea-resources.awscloud.com/spain-events-webinars)

## Scripts
- [AWS IP inventory](https://github.com/okelet/awsipinventory) Tool to generate an inventory of all IP addresses in use in an account, one or multiple VPC, or one or multiple subnet.
- [dev.to: How to Copy a Security Group with Rules from one AWS Account to Another account ?](https://dev.to/dineshrathee12/how-to-copy-a-security-group-with-rules-from-one-aws-account-to-another-account-36mb)
	- [CopySGFromOneAWSAccountToAnotherScript.py](https://github.com/dineshrathee12/CopySecurityGroupWithRulesFromOneAWSAccountToAnotherAWSAccount/blob/main/CopySGFromOneAWSAccountToAnotherScript.py)
- [github.com/awslabs/assisted-log-enabler-for-aws: Assisted Log Enabler - Find resources that are not logging, and turn them on](https://github.com/awslabs/assisted-log-enabler-for-aws)
- https://github.com/dannysteenman/aws-toolbox A collection of useful Shell & Python scripts that make your DevOps life easier in AWS. Furthermore you'll also find a list of links that point to awesome DevOps tools from other creators.

## Development
- [thenewstack.io: Remote Debugging in AWS: The Missing Link in Your Debugging Toolset](https://thenewstack.io/remote-debugging-in-aws-the-missing-link-in-your-debugging-toolset/)

## Cloud Development Kit CDK 
- [CDK](https://aws.amazon.com/cdk/)
- [bbvanexttechnologies.com: Cómo definir infraestructura como código en AWS con CDK](https://www.bbvanexttechnologies.com/como-definir-infraestructura-como-codigo-en-aws-con-cdk/)
- [itnext.io: AWS CDK for EKS — Handling Helm Charts](https://itnext.io/aws-cdk-for-eks-handling-helm-charts-aa002afedde4)

## AWS Secrets Manager
- [How to replicate secrets in AWS Secrets Manager to multiple Regions](https://aws.amazon.com/blogs/security/how-to-replicate-secrets-aws-secrets-manager-multiple-regions/)
- [AWS Secrets Manager controller POC: an EKS operator for automatic rotation of secrets](https://aws.amazon.com/blogs/containers/aws-secrets-manager-controller-poc-an-eks-operator-for-automatic-rotation-of-secrets/)
- [k21academy.com: AWS Secrets Manager](https://k21academy.com/amazon-web-services/aws-solutions-architect/aws-secrets-manager/)

## AWS Cloud Map and HealthChecks
- [Custom Health Check: HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html) Cloud Map will eventually mark the instance as unhealthy if it doesn't receive the health status in 30 seconds. Custom health checks are implemented as regular Route53 healthchecks that check S3 bucket keys (note http access instead of https).

## AWS Cloud Endure
- [AWS Cloud Endure Migration](https://aws.amazon.com/cloudendure-migration/)

## AWS Patterns
- [medium: Top 4 AWS Patterns of Highly Available API](https://medium.com/greenm/top-4-aws-patterns-of-highly-available-api-d34599bfbb96) We want to tell you about a few common patterns that can be used to build highly available APIs on top of AWS infrastructure. We will highlight each of them and briefly describe the pros and cons.

## AWS Tags
- [bridgecrew.io: Best practices for AWS tagging with Yor](https://bridgecrew.io/blog/best-practices-for-aws-tagging-with-yor/)

## ECommerce
- [Architecting a Highly Available Serverless, Microservices-Based Ecommerce Site](https://aws.amazon.com/blogs/architecture/architecting-a-highly-available-serverless-microservices-based-ecommerce-site/)

---
## Bunch of Images
<details>
  <summary>Click to expand!</summary>

<center>

![aws responsability model](images/s3_storage_classes.jfif)

[![aws responsability model](images/aws_shared_responsability_model.jpg)](https://aws.amazon.com/compliance/shared-responsibility-model/)
</center>
</details>

## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="https://www.youtube.com/embed/GBLPi-mno7M" frameborder="0" allow="accelerometer; autoplay; encrypted-media" allowfullscreen></iframe>
</center>
</details>

## Tweets
<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">You don&#39;t know how to get started with AWS?<br><br>I can relate!<br>When I started, AWS already offered so much that I literally couldn&#39;t find an entry point.<br><br>If you still feel this way, let me give you a little guide.<br><br>🧵⏬</p>&mdash; Oliver Jumpertz (@oliverjumpertz) <a href="https://twitter.com/oliverjumpertz/status/1379096498592432128?ref_src=twsrc%5Etfw">April 5, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is BIG! You can now assign IPv4 and IPv6 prefixes to your ENIs. The net result is that EC2 instances will now support vastly larger number of IP addresses, and managing those addresses will become easier. 1/n<a href="https://t.co/3ilNrFtuAp">https://t.co/3ilNrFtuAp</a></p>&mdash; Joe Magerramov (@_joemag_) <a href="https://twitter.com/_joemag_/status/1418345704964063232?ref_src=twsrc%5Etfw">July 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">When we first launched the managed Prometheus service, one of the feedback was about cost of ingestion. We announced a pricing discount up to 84% recently in case you haven&#39;t seen it. <a href="https://t.co/wqioBvSXme">https://t.co/wqioBvSXme</a> <a href="https://t.co/64ezXUg753">pic.twitter.com/64ezXUg753</a></p>&mdash; Jaana Dogan ヤナ ドガン (@rakyll) <a href="https://twitter.com/rakyll/status/1435717610704834566?ref_src=twsrc%5Etfw">September 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">💫 AWS VPC 101<br><br>Virtual Private Cloud is a fundamental concept of AWS ☁️<br><br>Let&#39;s explore it together in this thread 🧵👇</p>&mdash; Simon ☁️ (@simonholdorf) <a href="https://twitter.com/simonholdorf/status/1441452612331704321?ref_src=twsrc%5Etfw">September 24, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">📚 AWS 1x1<br><br>ɪᴅᴇɴᴛɪᴛʏ- &amp; ᴀᴄᴄᴇꜱꜱ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ (ɪᴀᴍ) 🔑<br><br>The concepts are crucial &amp; being confident in them is a necessity.<br><br>From basics to advanced concepts 🧵↓</p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1442880455179657219?ref_src=twsrc%5Etfw">September 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">AWS Amplify refers to different products.<br><br>You are confused what Amplify exactly is? <br><br>We know that AWS isn&#39;t the best with naming its products so let&#39;s see what Amplify products are exactly out there.<br><br>1/6 <a href="https://t.co/9dUtwpdjPU">pic.twitter.com/9dUtwpdjPU</a></p>&mdash; Sandro Volpic (@sandro_vol) <a href="https://twitter.com/sandro_vol/status/1442762063416283139?ref_src=twsrc%5Etfw">September 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
