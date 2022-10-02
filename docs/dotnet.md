# Microsoft .NET

1. [Introduction](#introduction)
2. [ASP.NET Core](#aspnet-core)
3. [NuGet Packages and nuspec file](#nuget-packages-and-nuspec-file)
4. [.NET MAUI](#net-maui)
5. [Polly .NET resilience and transient-fault-handling library](#polly-net-resilience-and-transient-fault-handling-library)
6. [Paradigm framework](#paradigm-framework)
7. [More dotnet frameworks and tools](#more-dotnet-frameworks-and-tools)
8. [Kubernetes for ASP.NET Core Developers](#kubernetes-for-aspnet-core-developers)
9. [Deploying ASP.NET Core applications to Kubernetes](#deploying-aspnet-core-applications-to-kubernetes)
10. [Tweets](#tweets)

## Introduction

- [wikipedia.org: .NET](https://en.wikipedia.org/wiki/.NET) .NET (previously named .NET Core) is a free and open-source, managed computer software framework for Windows, Linux, and macOS operating systems. It is a cross-platform successor to .NET Framework. The project is primarily developed by Microsoft employees by way of the .NET Foundation, and released under the MIT License.
- https://dotnet.microsoft.com
- https://github.com/dotnet/core
- [techcommunity.microsoft.com: Full-stack .NET 6 Apps with Blazor WebAssembly and Azure Static Web Apps](https://techcommunity.microsoft.com/t5/apps-on-azure/full-stack-net-6-apps-with-blazor-webassembly-and-azure-static/ba-p/2933428)
- [developers.redhat.com: Three ways to containerize .NET applications on Red Hat OpenShift](https://developers.redhat.com/blog/2021/03/16/three-ways-to-containerize-net-applications-on-red-hat-openshift)
- [developers.redhat.com: .NET 6 now available for RHEL and OpenShift](https://developers.redhat.com/articles/2021/11/15/net-60-now-available-rhel-and-openshift)
- [telerik.com: Your First Microservice in .NET 6](https://www.telerik.com/blogs/your-first-microservice-dotnet-6)
- [docs.microsoft.com: .NET Microservices: Architecture for Containerized .NET Applications](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/)
- [stackify.com: Who will Dominate in the future: .Net or Java?](https://stackify.com/who-will-dominate-in-the-future-net-or-java/)
- [devblogs.microsoft.com: Announcing Rate Limiting for .NET](https://devblogs.microsoft.com/dotnet/announcing-rate-limiting-for-dotnet/)

## ASP.NET Core

- [blog.jetbrains.com: Getting Started with ASP.NET Core and gRPC](https://blog.jetbrains.com/dotnet/2021/07/19/getting-started-with-asp-net-core-and-grpc/)
- [dzone: Building a RESTful Service Using ASP.NET Core and dotConnect for PostgreSQL](https://dzone.com/articles/building-a-restful-service-using-aspnet-core-and-d) This article looks at RESTful architecture and how we can implement a RESTful service using ASP.NET Core and dotConnect for PostgreSQL.
- [enlear.academy: Repository Pattern and Unit of Work with ASP.NET Core Web API](https://enlear.academy/repository-pattern-and-unit-of-work-with-asp-net-core-web-api-6802e1aa4f78)
- [itnext.io: How to Build an Event-Driven ASP.NET Core Microservice Architecture](https://itnext.io/how-to-build-an-event-driven-asp-net-core-microservice-architecture-e0ef2976f33f) Use RabbitMQ, C#, REST-API and Entity Framework for asynchronous decoupled communication and eventually consistency with integration events and publish-subscribe

## NuGet Packages and nuspec file

- [dzone: How to Create and Publish NuGet Packages Using .NET Core CLI](https://dzone.com/articles/how-to-create-and-publish-nuget-packages-using-net)
- [NuGet/docs.microsoft.com-nuget: nuspec](https://github.com/NuGet/docs.microsoft.com-nuget/blob/main/docs/reference/nuspec.md)
- [gist.github.com: Creating and Publishing NuGet Packages](https://gist.github.com/andykuszyk/a5ee80ae263e77f651bed878c1deb03b)
- [khalidabuhakmeh.com: A .NET 5.0 Guide: From Idea To NuGet Package](https://khalidabuhakmeh.com/a-dotnet-five-guide-from-idea-to-nuget-package)
- [syncfusion.com: 10 Best C# NuGet Packages to Improve Your Productivity in 2022](https://www.syncfusion.com/blogs/post/10-best-c-nuget-packages-to-improve-your-productivity-in-2022.aspx)
- [devblogs.microsoft.com: Introducing Compatible Packages on NuGet.org](https://devblogs.microsoft.com/nuget/introducing-compatible-frameworks-on-nuget-org/)

## .NET MAUI

- [devblogs.microsoft.com: Getting Started with DevOps and .NET MAUI](https://devblogs.microsoft.com/dotnet/devops-for-dotnet-maui/) .NET Multi-platform App UI (.NET MAUI) unifies Android, iOS, macOS, and Windows UI frameworks into a single framework so you can write one app that runs natively on many platforms. In this post, we will look at how easy it is to implement basic DevOps pipelines for .NET MAUI apps using GitHub Actions and Azure DevOps.

## Polly .NET resilience and transient-fault-handling library 

- [App-vNext/Polly](https://github.com/App-vNext/Polly) Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.
- [medium: Microservices Resilience and Fault Tolerance with applying Retry and Circuit-Breaker patterns using Polly](https://medium.com/aspnetrun/microservices-resilience-and-fault-tolerance-with-applying-retry-and-circuit-breaker-patterns-c32e518db990)
- [procodeguide.com: Build Resilient Microservices (Web API) using Polly in ASP.NET Core](https://procodeguide.com/programming/polly-in-aspnet-core/)

## Paradigm framework

- [Paradigm framework](https://www.paradigm.net.co) Built for NetCore, and featuring its own ORM and code generation tools, Paradigm sets the stage for a new breed of high-performance, multiplatform applications.
- Paradigm Framework is a .net core Enterprise libraries, ORM and code scaffolding tool.

## More dotnet frameworks and tools

- [Oakton](https://jasperfx.github.io/oakton/) Add Robust Command Line Options to .Net Applications
- [Lamar](https://jasperfx.github.io/lamar/) Lamar is a .NET library that provides two pieces of functionality:
    - A fast Inversion of Control Container that natively supports the ASP.Net Core DI abstractions and a subset of the older StructureMap library
    - The dynamic code generation and compilation features used underneath the IoC implementation
- [jeremydmiller.com: Self Diagnosing Deployments with Oakton and Lamar](https://jeremydmiller.com/2021/10/12/self-diagnosing-deployments-with-oakton-and-lamar/)

## Kubernetes for ASP.NET Core Developers

- [dotnetcurry.com: Kubernetes for ASP.NET Core Developers – Introduction, Architecture, Hands-On](https://www.dotnetcurry.com/aspnet-core/kubernetes-for-developers)

## Deploying ASP.NET Core applications to Kubernetes 

- [andrewlock.net: Series: Deploying ASP.NET Core applications to Kubernetes with Helm 🌟](https://andrewlock.net/series/deploying-asp-net-core-applications-to-kubernetes/)
- [dzone: CI/CD as a Code for .NET Core Application and Kubernetes 🌟](https://dzone.com/articles/cicd-as-a-code-for-net-core-application-and-kubern) The process of building a simple CI/CD pipeline for existing .net core application to moving it to Azure Kubernetes Services using Azure DevOps.

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My favorite .NET 6 feature: single file deployment and executable binaries across multiple platforms. <a href="https://t.co/Zfd7zJGf0N">https://t.co/Zfd7zJGf0N</a> <a href="https://t.co/jpu9R36S7v">pic.twitter.com/jpu9R36S7v</a></p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/1457772150576742415?ref_src=twsrc%5Etfw">November 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
