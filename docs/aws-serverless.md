# AWS Serverless

1. [Introduction](#introduction)
2. [AWS Fargate](#aws-fargate)

## Introduction

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
- [==Deploying AWS Lambda layers automatically across multiple Regions==](https://aws.amazon.com/blogs/compute/deploying-aws-lambda-layers-automatically-across-multiple-regions/) Many developers import libraries and dependencies into their AWS Lambda functions. These dependencies can be zipped and uploaded as part of the build and deployment process but it’s often easier to use Lambda layers instead.
- [medium: Serverless enterprise-grade multi-tenancy using AWS | Tarek Becker](https://medium.com/@tarekbecker/serverless-enterprise-grade-multi-tenancy-using-aws-76ff5f4d0a23)
- [dev.to: Manage webhooks at scale with AWS Serverless](https://dev.to/aws-builders/manage-webhooks-at-scale-with-aws-serverless-fof)
- [Issues to Avoid When Implementing Serverless Architecture with AWS Lambda](https://aws.amazon.com/blogs/architecture/mistakes-to-avoid-when-implementing-serverless-architecture-with-lambda)
- [medium.com/@andrewjr350: Misunderstanding of Serverless (AWS)](https://medium.com/@andrewjr350/misunderstanding-of-serverless-aws-835c7076ea4c)
- [freecodecamp.org: How to Setup a Basic Serverless REST API with AWS Lambda and API Gateway](https://www.freecodecamp.org/news/how-to-setup-a-basic-serverless-backend-with-aws-lambda-and-api-gateway/)
- [Migrating a monolithic .NET REST API to AWS Lambda](https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/)
- [==medium.com/aws-serverless-microservices-with-patterns-best: Cloud-Native Microservices Evolves to AWS Serverless Event-driven Architectures==](https://medium.com/aws-serverless-microservices-with-patterns-best/cloud-native-microservices-evolves-to-aws-serverless-event-driven-architectures-9a38c473f4f8) In this article, we are going to discuss about How Cloud-Native Microservices Evolves to AWS Serverless Event-driven Architectures when developing Serverless E-Commerce application.
- [betterprogramming.pub: Exploring the Serverless Event-Driven Architecture](https://betterprogramming.pub/exploring-the-serverless-event-driven-architecture-8d6bda93e823) Meet your old friends Terraform, Lambda, SQS, and Python
- [==betterprogramming.pub: Lambda vs. Step Functions: The Battle of Cost and Performance==](https://betterprogramming.pub/lambda-vs-step-functions-the-battle-of-cost-and-performance-5f008045e2ab) With the big push to use Step Functions over Lambda, you might be wondering “which is more cost-effective”? The answer might surprise you.
    - There are use cases for both, but the consensus for production development lives with a hybrid approach: performing a base set of actions synchronously, like validations and id creation **and kicking off the rest of the processing asynchronously**. You’d then [use a WebSocket](https://betterprogramming.pub/introduction-to-aws-websockets-8b336a92c379) to inform the user when the workflow is complete.
- [medium.com/awesome-cloud: AWS — Difference between Serverless (Lambda) and Containers (Kubernetes)](https://medium.com/awesome-cloud/aws-difference-between-serverless-lambda-and-containers-kubernetes-serverless-vs-containers-lambda-vs-k8s-a166931870a2)
- [aws.amazon.com: Scaling AWS Lambda permissions with Attribute-Based Access Control (ABAC)](https://aws.amazon.com/blogs/compute/scaling-aws-lambda-permissions-with-attribute-based-access-control-abac/)
- [aws.amazon.com: Understanding AWS Lambda scaling and throughput](https://aws.amazon.com/blogs/compute/understanding-aws-lambda-scaling-and-throughput/)
- [How to enforce user quota on AWS AppSync with Lambda Authorizer](https://aws.amazon.com/blogs/mobile/how-to-enforce-user-quota-on-aws-appsync-with-lambda-authorizer/) API Quotas define the valid amount of calls available for a consumer during a specific amount of time. Enforcing quotas protects your API from unintentional abuse, minimizes data exfiltration and protects your resources from excessive usage. Beyond the mentioned security benefits, it can also unlock your capabilities to monetize the digital assets sitting behind the API.
- [aws.plainenglish.io: Let's design a serverless ETL pipeline with AWS services](https://aws.plainenglish.io/lets-design-a-serverless-etl-pipeline-with-aws-services-9ab88c95afd4)
- [theserverlessmindset.com: Choosing the Best Database for Your Serverless Project](https://www.theserverlessmindset.com/p/best-serverless-database) It comes down to a few options, and one of them is the best (but your prior experience may change that)
- [aidansteele/secretsctx](https://github.com/aidansteele/secretsctx) secretsctx is a Lambda extension (packaged as a Lambda layer) that injects secret values from AWS Parameter Store and AWS Secrets Manager into your Lambda function's invocation "context".
- [faun.pub: Serverless With Spring Boot & AWS Lambda](https://faun.pub/serverless-with-spring-boot-aws-lambda-bc76c1de2b12)
- [aws.amazon.com: New – Accelerate Your Lambda Functions with Lambda SnapStart](https://aws.amazon.com/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart/)
- [infoworld.com: AWS Lambda kickstarts Java functions](https://www.infoworld.com/article/3681549/aws-lambda-kickstarts-java-functions.html) AWS Lambda SnapStart cuts Java startup times by initializing Java functions ahead of time and caching a snapshot of the initialized execution environment.
- [medium.com/@dan.avila7: Prueba tus proyectos serverless de forma local con serverless-offline](https://medium.com/@dan.avila7/prueba-tus-proyectos-serverless-de-forma-local-con-serverless-offline-2e555f2b5e9b) En este artículo veremos como instalar y configurar el plugin serverless-offline con sls framework para realizar pruebas locales de las funciones lambda antes de realizar el deploy en AWS.
- [tutorialsdojo.com: Real-time Monitoring of 5XX Errors using AWS Lambda, CloudWatch Logs and Slack](https://tutorialsdojo.com/real-time-monitoring-of-5xx-errors-using-aws-lambda-cloudwatch-logs-slack/)
- [dev.to: Go fast and reduce risk: using CDK to deploy your serverless applications on AWS](https://dev.to/aws-builders/go-fast-and-reduce-risk-using-cdk-to-deploy-your-serverless-applications-on-aws-2i3k)
- [awstip.com: Tips for keeping your Lambda functions secure](https://awstip.com/tips-for-keeping-your-lambda-functions-secure-25349dd5d9df)
- [dev.to: Event driven architectures using AWS with example](https://dev.to/aws-builders/event-driven-architectures-using-aws-with-example-3d2d)
- [terrateam.io: AWS Lambda Function with Terraform](https://terrateam.io/blog/aws-lambda-function-with-terraform)
- [medium.com/lego-engineering: A Journey into Serverless and Handling Step Function Failures](https://medium.com/lego-engineering/a-journey-into-serverless-and-handling-step-function-failures-dba51b4e8e99) Have you ever wondered how you would handle failures in your AWS Step Functions? And what benefits would a robust failure-handling system have?
- [dev.to/aws-builders: Introduction to AWS SAM (Serverless Application Model)](https://dev.to/aws-builders/introduction-to-aws-sam-serverless-application-model-12oc)
- [blog.devops.dev: Deploying Awesome App on AWS Serverless Services — Step-by-Step Guide](https://blog.devops.dev/deploying-awesome-app-on-aws-serverless-services-step-by-step-guide-54bc89e4d236)
- [medium.com/@sassenthusiast: Serverless Simplified: Integrating Docker Containers into AWS Lambda via serverless.yml](https://medium.com/@sassenthusiast/serverless-simplified-integrating-docker-containers-into-aws-lambda-via-serverless-yml-cdef9be1681e)

## AWS Fargate

- [Amazon EFS with Amazon ECS and AWS Fargate – Part 1](https://aws.amazon.com/es/blogs/containers/developers-guide-to-using-amazon-efs-with-amazon-ecs-and-aws-fargate-part-1/)
- [Deploy Machine Learning Pipeline on AWS Fargate](https://www.kdnuggets.com/2020/07/deploy-machine-learning-pipeline-aws-fargate.html)
- [deloitte.com: Fargate con EKS](https://www2.deloitte.com/es/es/blog/todo-tecnologia/2021/fargate-con-eks.html) ¿Es Fargate la solución de AWS con la que siempre soñamos para evitar manejar infraestructura con Kubernetes? Sí, pero…
- [element7.io: A Hidden Gem: Two Ways to Improve AWS Fargate Container Launch Times](https://www.element7.io/2022/10/a-hidden-gem-two-ways-to-improve-aws-fargate-container-launch-times/) In this post you will learn two strategies to speed up the pod creation time:
    - zstd compressed container images
    - Seekable OCI for lazy loading container images
- [medium.com/@HirenDhaduk1: Best choice to run your containers: AWS FARGATE or AWS LAMBDA or Both?](https://medium.com/@HirenDhaduk1/best-choice-to-run-your-containers-aws-fargate-or-aws-lambda-or-both-d9e14685a363)
- [github.com/awslabs/specctl](https://github.com/awslabs/specctl) CLI to convert Kubernetes specifications to ECS Fargate and vice-versa