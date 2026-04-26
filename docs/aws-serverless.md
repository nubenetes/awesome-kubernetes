# AWS Serverless

1. [Introduction](#introduction)
2. [AWS Fargate](#aws-fargate)

## Introduction

- [you can use Python with AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
- [Serverless: The Future of Software Architecture?](https://read.acloud.guru/serverless-the-future-of-software-architecture-d4473ffed864#.uk7setw47)
- [AWS Lambda Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
- [How do I stop and start EC2 instances at regular intervals using AWS Lambda? (Video)](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)
- [Youtube channel: AWS Serverless](https://www.youtube.com/channel/UC_vJsnqdpuEoRseFmlkHMkA)
- [Using Amazon EFS for AWS Lambda in your serverless applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/)
- [dashbird.io: Deploying AWS Lambda with Docker Containers: I Gave it a Try and Here’s My Review](https://dashbird.io/blog/deploying-aws-lambda-with-docker/)
- [aws.amazon.com: Operating Lambda: Understanding event-driven architecture – Part 1](https://aws.amazon.com/blogs/compute/operating-lambda-understanding-event-driven-architecture-part-1/)
- [aws.amazon.com: Optimizing Lambda functions packaged as container images](https://aws.amazon.com/es/blogs/compute/optimizing-lambda-functions-packaged-as-container-images/)
- [Security Overview of AWS Lambda](https://d1.awsstatic.com/whitepapers/Overview-AWS-Lambda-Security.pdf)
- [cloudonaut.io: Serverless Hybrid Cloud: Accessing an API Gateway via VPN or Direct Connect](https://cloudonaut.io/serverless-hybrid-cloud-accessing-an-api-gateway-via-vpn-or-direct-connect/)
- [infoworld.com: Serverless computing with AWS Lambda, Part 1](https://www.infoworld.com/article/3210726/serverless-computing-with-aws-lambda.html) Get an overview of AWS Lambda's nanoservices architecture and execution model, then build your first Lambda function in Java
- [dashbird.io: 4 Tips for AWS Lambda Optimization for Production](https://dashbird.io/blog/optimizing-aws-lambda-for-production/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/)
- [Introducing AWS SAM Pipelines: Automatically generate deployment pipelines for serverless applications](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications)
- [Simplify CI/CD configuration for serverless applications and your favorite CI/CD system — Public Preview](https://aws.amazon.com/about-aws/whats-new/2021/07/simplify-ci-cd-configuration-serverless-applications-your-favorite-ci-cd-system-public-preview/)
- [Achieve up to 34% better price/performance with AWS Lambda Functions powered by AWS Graviton2 processor](https://aws.amazon.com/about-aws/whats-new/2021/09/better-price-performance-aws-lambda-functions-aws-graviton2-processor/)
- [==Deploying AWS Lambda layers automatically across multiple Regions==](https://aws.amazon.com/blogs/compute/deploying-aws-lambda-layers-automatically-across-multiple-regions/) Many developers import libraries and dependencies into their AWS Lambda functions. These dependencies can be zipped and uploaded as part of the build and deployment process but it’s often easier to use Lambda layers instead.
- [dev.to: Manage webhooks at scale with AWS Serverless](https://dev.to/aws-builders/manage-webhooks-at-scale-with-aws-serverless-fof)
- [Issues to Avoid When Implementing Serverless Architecture with AWS Lambda](https://aws.amazon.com/blogs/architecture/mistakes-to-avoid-when-implementing-serverless-architecture-with-lambda)
- [freecodecamp.org: How to Setup a Basic Serverless REST API with AWS Lambda and API Gateway](https://www.freecodecamp.org/news/how-to-setup-a-basic-serverless-backend-with-aws-lambda-and-api-gateway/)
- [Migrating a monolithic .NET REST API to AWS Lambda](https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/)
- [aws.amazon.com: Scaling AWS Lambda permissions with Attribute-Based Access Control (ABAC)](https://aws.amazon.com/blogs/compute/scaling-aws-lambda-permissions-with-attribute-based-access-control-abac/)
- [aws.amazon.com: Understanding AWS Lambda scaling and throughput](https://aws.amazon.com/blogs/compute/understanding-aws-lambda-scaling-and-throughput/)
- [How to enforce user quota on AWS AppSync with Lambda Authorizer](https://aws.amazon.com/blogs/mobile/how-to-enforce-user-quota-on-aws-appsync-with-lambda-authorizer/) API Quotas define the valid amount of calls available for a consumer during a specific amount of time. Enforcing quotas protects your API from unintentional abuse, minimizes data exfiltration and protects your resources from excessive usage. Beyond the mentioned security benefits, it can also unlock your capabilities to monetize the digital assets sitting behind the API.
- [theserverlessmindset.com: Choosing the Best Database for Your Serverless Project](https://www.theserverlessmindset.com/p/best-serverless-database) It comes down to a few options, and one of them is the best (but your prior experience may change that)
- [aidansteele/secretsctx](https://github.com/aidansteele/secretsctx) secretsctx is a Lambda extension (packaged as a Lambda layer) that injects secret values from AWS Parameter Store and AWS Secrets Manager into your Lambda function's invocation "context".
- [aws.amazon.com: New – Accelerate Your Lambda Functions with Lambda SnapStart](https://aws.amazon.com/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart/)
- [infoworld.com: AWS Lambda kickstarts Java functions](https://www.infoworld.com/article/3681549/aws-lambda-kickstarts-java-functions.html) AWS Lambda SnapStart cuts Java startup times by initializing Java functions ahead of time and caching a snapshot of the initialized execution environment.
- [tutorialsdojo.com: Real-time Monitoring of 5XX Errors using AWS Lambda, CloudWatch Logs and Slack](https://tutorialsdojo.com/real-time-monitoring-of-5xx-errors-using-aws-lambda-cloudwatch-logs-slack/)
- [dev.to: Go fast and reduce risk: using CDK to deploy your serverless applications on AWS](https://dev.to/aws-builders/go-fast-and-reduce-risk-using-cdk-to-deploy-your-serverless-applications-on-aws-2i3k)
- [dev.to: Event driven architectures using AWS with example](https://dev.to/aws-builders/event-driven-architectures-using-aws-with-example-3d2d)
- [terrateam.io: AWS Lambda Function with Terraform](https://terrateam.io/blog/aws-lambda-function-with-terraform)
- [dev.to/aws-builders: Introduction to AWS SAM (Serverless Application Model)](https://dev.to/aws-builders/introduction-to-aws-sam-serverless-application-model-12oc)

## AWS Fargate

- [Amazon EFS with Amazon ECS and AWS Fargate – Part 1](https://aws.amazon.com/es/blogs/containers/developers-guide-to-using-amazon-efs-with-amazon-ecs-and-aws-fargate-part-1/)
- [Deploy Machine Learning Pipeline on AWS Fargate](https://www.kdnuggets.com/2020/07/deploy-machine-learning-pipeline-aws-fargate.html)
- [deloitte.com: Fargate con EKS](https://www2.deloitte.com/es/es/blog/todo-tecnologia/2021/fargate-con-eks.html) ¿Es Fargate la solución de AWS con la que siempre soñamos para evitar manejar infraestructura con Kubernetes? Sí, pero…
- [element7.io: A Hidden Gem: Two Ways to Improve AWS Fargate Container Launch Times](https://www.element7.io/2022/10/a-hidden-gem-two-ways-to-improve-aws-fargate-container-launch-times/) In this post you will learn two strategies to speed up the pod creation time:
    - zstd compressed container images
    - Seekable OCI for lazy loading container images
- [github.com/awslabs/specctl](https://github.com/awslabs/specctl) CLI to convert Kubernetes specifications to ECS Fargate and vice-versa