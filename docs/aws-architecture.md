# AWS Architecture and Best Practices

1. [Introduction](#introduction)
2. [AWS Well Architected Framework](#aws-well-architected-framework)
3. [AWS Architecture Blog, Official Blog, AWS Labs, AWS Quick Start](#aws-architecture-blog-official-blog-aws-labs-aws-quick-start)
4. [AWS Case Studies](#aws-case-studies)
5. [AWS Best Practices and Tips. AWS Performance. Handling AWS Failures and Outages](#aws-best-practices-and-tips-aws-performance-handling-aws-failures-and-outages)

## Introduction

- [AWS application-architecture](http://www.conceptdraw.com/examples/application-architecture)
- [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)
- [==AWS App2Container: Migrate your Applications to Containers at Scale==](https://aws.amazon.com/blogs/architecture/migrate-your-applications-to-containers-at-scale/)
- [dev.to: How Well-Architected Enables Junior Engineers](https://dev.to/aws-builders/how-well-architected-enables-junior-engineers-24j)
- [==This is My Architecture==](https://aws.amazon.com/architecture/this-is-my-architecture) Innovative cloud architectures from AWS partners and customers. **'This is My Architecture' is a video series that showcases innovative architectural solutions on the AWS Cloud by customers and partners.** Each episode examines the most interesting and technically creative elements of each cloud architecture.
- [==Creating a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security==](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/)
- [==Creating a Multi-Region Application with AWS Services – Part 2, Data and Replication==](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-2-data-and-replication/)
- [==Let’s Architect! Architecting microservices with containers==](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-microservices-with-containers/) Microservices structure an application as a set of independently deployable services. They speed up software development and allow architects to quickly update systems to adhere to changing business requirements. According to best practices, the different services should be loosely coupled, organized around business capabilities, independently deployable, and owned by a single team. If applied correctly, there are multiple advantages to using microservices. However, working with microservices can also bring challenges. In this edition of Let’s Architect!, we explore the advantages, mental models, and challenges deriving from microservices with containers.
- [Strategies for consolidating AWS environments](https://aws.amazon.com/de/blogs/mt/strategies-for-consolidating-aws-environments/)
- [Maintain visibility over the use of cloud architecture patterns](https://aws.amazon.com/blogs/architecture/maintain-visibility-over-the-use-of-cloud-architecture-patterns/) Cloud platform and enterprise architecture teams use architecture patterns to provide guidance for different use cases. Cloud architecture patterns are typically aggregates of multiple Amazon Web Services (AWS) resources, such as Elastic Load Balancing with Amazon Elastic Compute Cloud, or Amazon Relational Database Service with Amazon ElastiCache. In a large organization, cloud platform teams often have limited governance over cloud deployments, and, therefore, lack control or visibility over the actual cloud pattern adoption in their organization.
- [Architecture patterns for consuming private APIs cross-account](https://aws.amazon.com/pt/blogs/compute/architecture-patterns-for-consuming-private-apis-cross-account/)
- [==github.com/ministryofjustice: Modernisation Platform - Architecture Decisions==](https://github.com/ministryofjustice/modernisation-platform/tree/main/architecture-decision-record) This is our architecture decision log, made during the design and build of the Modernisation Platform.

## AWS Well Architected Framework

- [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [==aws.amazon.com/well-architected-tool: AWS Well-Architected Tool==](https://aws.amazon.com/well-architected-tool) Do couple of WAR (Well-Architect Review) for public cloud. Basically it is to scan the cloud on 5-6 KPI's : Performance, Cost, Operations, Business etc..
- [infoq.com: AWS Updates the Well-Architected Framework](https://www.infoq.com/news/2023/04/aws-well-architected-framework/)

## AWS Architecture Blog, Official Blog, AWS Labs, AWS Quick Start

- [AWS Architecture Blog](https://www.awsarchitectureblog.com)
- [AWS Official Blog](http://blogs.aws.amazon.com/)
- [AWS Labs GitHub](https://github.com/awslabs)
- [AWS Quick Start Reference Deployments](http://aws.amazon.com/es/quickstart/)
- [InfoWorld Review – Amazon Aurora Rocks MySQL](https://aws.amazon.com/blogs/aws/infoworld-review-amazon-aurora-rocks-mysql/)
- [AWS Cost Explorer Update – Access to EC2 Usage Data](https://aws.amazon.com/blogs/aws/aws-cost-explorer-update-access-to-ec2-usage-data/)

## AWS Case Studies

- [Thomas Publishing Case Study](https://aws.amazon.com/solutions/case-studies/thomas-publishing/)  After moving to AWS, we were able to shut down our largest data center, eliminating hundreds of thousands of dollars in associated real estate, facility operations, and power and cooling costs.

## AWS Best Practices and Tips. AWS Performance. Handling AWS Failures and Outages

- [AWS Tips I Wish I'd Known Before I Started (Feb 2014)](https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/) A collection of random tips for Amazon Web Services (AWS) that I wish I'd been told a few years ago, based on what I've learned by building and deploying various applications on AWS.
- [thenewstack.io: Avoid the 5 Most Common Amazon Web Services Misconfigurations in Build-Time](https://thenewstack.io/avoid-the-5-most-common-amazon-web-services-misconfigurations-in-build-time/)
- [AWS Architecture Blog: Use templated answers to perform Well-Architected reviews at scale](https://aws.amazon.com/blogs/architecture/use-templated-answers-to-perform-well-architected-reviews-at-scale/)
- [==cbui.dev: Every company has an "old" production AWS account==](https://cbui.dev/every-company-has-an-old-production-aws-account/) When companies are in the startup phase, they create their root AWS account and put everything in it. Later on, it might become necessary for the company to have SOC2 certification. These certifications' audit and security requirements require a lockdown of the root AWS account. It is an expensive and painful migration from the root AWS account to a new production account. I've seen it at Venmo and Flex. If you're starting today, I highly recommend setting up your AWS organizations and a sub-account under your root account. This will save you potentially hundreds of thousands to millions of dollars in migration costs down the line.