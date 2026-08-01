---
description: "Top Dotnet resources for 2026, AI-ranked: Oakton, Lamar and more — curated Cloud Native tools, guides and references."
---
# Microsoft .NET

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/dotnet/).

!!! info "Architectural Context"
    Detailed reference for Microsoft .NET in the context of Developer Ecosystem.

## Application Development

### .NET Framework

#### API Security

  - **(2022)** [==devblogs.microsoft.com: Announcing Rate Limiting for .NET==](https://devblogs.microsoft.com/dotnet/announcing-rate-limiting-for-dotnet) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces native, built-in rate-limiting middleware for ASP.NET Core. Explores implementing Token Bucket, Fixed Window, and Concurrency algorithms directly within modern APIs to safeguard microservices from traffic overloads.
#### Architectural Guides

  - **(2024)** [==docs.microsoft.com: .NET Microservices: Architecture for Containerized .NET Applications==](https://learn.microsoft.com/en-us/dotnet/architecture/microservices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The definitive architectural design guide for planning and building containerized .NET microservices. Focuses on Domain-Driven Design (DDD) principles, CQRS patterns, Outbox event delivery, and deployment best practices inside Docker environments.
#### Blazor and Static Web Apps

  - **(2022)** [**techcommunity.microsoft.com: Full-stack .NET 6 Apps with Blazor WebAssembly and Azure Static Web Apps**](https://techcommunity.microsoft.com/blog/appsonazureblog/full-stack-net-6-apps-with-blazor-webassembly-and-azure-static-web-apps/2933428) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Outlines deploying full-stack Blazor WebAssembly client applications with Azure Static Web Apps. Details integrated serverless API hosting using Azure Functions, explaining how this architecture reduces hosting costs compared to traditional VM models.
#### Core Architecture

  - **(2026)** [==wikipedia.org: .NET==](https://en.wikipedia.org/wiki/.NET) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — High-level reference outlining the modern cross-platform, open-source .NET framework. Explores how its high-performance runtime (CLR), optimized garbage collection, and fast JIT compiler make it suitable for modern container deployments.
#### Ecosystem Comparisons

  - **(2022)** [stackify.com: Who will Dominate in the future: .Net or Java?](https://stackify.com/who-will-dominate-in-the-future-net-or-java) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares performance metrics, runtime speeds, and support costs of .NET against Oracle Java. Analyzes how container optimizations, start-up times, and ecosystem tooling affect cloud resource efficiency.
#### Grpc Communication

  - **(2021)** [**blog.jetbrains.com: Getting Started with ASP.NET Core and gRPC**](https://blog.jetbrains.com/dotnet/2021/07/19/getting-started-with-asp-net-core-and-grpc) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Presents a technical guide on configuring high-performance gRPC services using ASP.NET Core. Details protobuf schema creation, client generation, and HTTP/2 connection pooling to achieve ultra-low latency between microservices.
#### Microservices Design

  - **(2021)** [**telerik.com: Your First Microservice in .NET 6**](https://www.telerik.com/blogs/your-first-microservice-dotnet-6) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A hands-on guide to building a microservice using ASP.NET Core 6 Minimal APIs. Demonstrates how to write lightweight, highly optimized web APIs with minimal boilerplate code, perfect for deployment within containerized clusters.
#### Openshift Containers

  - **(2021)** [**developers.redhat.com: Three ways to containerize .NET applications on Red Hat OpenShift**](https://developers.redhat.com/blog/2021/03/16/three-ways-to-containerize-net-applications-on-red-hat-openshift) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Details three distinct strategies to containerize and run .NET applications on Red Hat OpenShift. Evaluates the benefits of Dockerfile builds, Source-to-Image (S2I) pipelines, and deployment templates for enterprise scalability.
#### RHEL Support

  - **(2021)** [**developers.redhat.com: .NET 6 now available for RHEL and OpenShift**](https://developers.redhat.com/articles/2021/11/15/net-60-now-available-rhel-and-openshift) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Announces native Red Hat Enterprise Linux (RHEL) and OpenShift support for .NET 6. Focuses on pre-configured, secure container base images and integration setups that simplify enterprise deployments.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [dzone: Building a RESTful Service Using ASP.NET Core and dotConnect for' PostgreSQL](https://dzone.com/articles/building-a-restful-service-using-aspnet-core-and-d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Building a RESTful Service Using ASP.NET Core and dotConnect for' PostgreSQL in the Kubernetes Tools ecosystem.
## Cloud Infrastructure and Orchestration

### Container Orchestration

#### Helm and Packaging

  - **(2022)** [andrewlock.net: Series: Deploying ASP.NET Core applications to Kubernetes with Helm 🌟](https://andrewlock.net/series/deploying-asp-net-core-applications-to-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive deep-dive tutorial series on orchestrating .NET applications inside Kubernetes using Helm. Analyzes templating, YAML manifests, dependency injections, dynamic secret handling, and values customization patterns.
#### Kubernetes

  - **(2021)** [dotnetcurry.com: Kubernetes for ASP.NET Core Developers – Introduction, Architecture, Hands-On](https://www.dotnetcurry.com/aspnet-core/kubernetes-for-developers) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An educational guide targeted at .NET architects migrating legacy backends to Kubernetes. Details fundamental infrastructure layers including Pods, ReplicaSets, Deployments, Services, and containerization pipelines using Docker.
## Mobile Development

### Cross-platform

#### Xamarin

  - **(2024)** [dotnet.microsoft.com: What is Xamarin?](https://dotnet.microsoft.com/en-us/apps/xamarin) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory resource detailing Xamarin's architecture, demonstrating how C# code gets compiled to native binaries using Mono or .NET execution runtimes. It highlights the historically unified codebase approach for mobile UI design. This documentation is primarily of historical interest as the ecosystem transitions entirely to modern .NET MAUI runtimes.
## Software Architecture and .NET Development

### Application Diagnostics

#### CLI Engines

  - **(2025)** [Oakton](https://jasperfx.github.io/oakton) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An robust CLI command parser and diagnostic middleware for .NET console applications. Enables advanced command-line tool structuring, service health assessments, and native execution hook extensions within standard ASP.NET Core hosts.
#### Environment Validation

  - **(2021)** [jeremydmiller.com: Self Diagnosing Deployments with Oakton and Lamar](https://jeremydmiller.com/2021/10/12/self-diagnosing-deployments-with-oakton-and-lamar) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents a design paradigm combining Lamar's compilation-safe IoC container with Oakton's self-diagnostics capability. Outlines systems validation strategies that trigger build failures if container registrations or service setups fail.
#### Ioc Containers

  - **(2025)** [Lamar](https://jasperfx.github.io/lamar) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced, high-performance IoC container and assembly scanning engine compatible with Microsoft's DI standards. Leverages Roslyn-powered dynamic code compilation to optimize dependency resolution pathways in microservices.
### Client Technologies

#### CICD and DevOps

  - **(2022)** [devblogs.microsoft.com: Getting Started with DevOps and .NET MAUI](https://devblogs.microsoft.com/dotnet/devops-for-dotnet-maui) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines continuous integration and continuous delivery patterns configured specifically for .NET MAUI multi-platform client applications. Walks through pipeline configuration across iOS, Android, and desktop build targets using GitHub Actions and Azure Pipelines.
### Microservices

#### Resilience Patterns

  - **(2026)** [==App-vNext/Polly==](https://github.com/App-vNext/Polly) <span class='md-tag md-tag--info'>⭐ 14192</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a2a0e361" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 13 L 20 6 L 30 7 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-a2a0e361)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier resilient fault-handling library for the .NET ecosystem. Enables developers to configure sophisticated reliability policies including Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback, acting as the bedrock for stable microservices.
  - **(2022)** [procodeguide.com: Build Resilient Microservices (Web API) using Polly in ASP.NET Core](https://procodeguide.com/programming/polly-in-aspnet-core) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides a hands-on architectural approach to integrating Polly policy frameworks inside ASP.NET Core Web APIs. Details proper HttpClientFactory patterns, fallback strategies, and configuring resilient endpoint routing.
### Package Management

#### Ecosystem Curation

  - **(2022)** [syncfusion.com: 10 Best C# NuGet Packages to Improve Your Productivity in 2022](https://www.syncfusion.com/blogs/post/10-best-c-nuget-packages-to-improve-your-productivity-in-2022) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated evaluation of top-tier NuGet packages designed to elevate developer productivity inside modern .NET enterprise ecosystems. Features utility frameworks covering high-speed serialization, deep-object mapping, unit testing extensions, logging, and database interfacing.
#### Nuget Specification

  - **(2026)** [NuGet/docs.microsoft.com-nuget: nuspec](https://github.com/NuGet/docs.microsoft.com-nuget/blob/main/docs/reference/nuspec.md) <span class='md-tag md-tag--info'>⭐ 160</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bf8c02da" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 3 L 20 10 L 30 13 L 40 3 L 50 6" fill="none" stroke="url(#spark-grad-bf8c02da)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[XML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This reference specification details the .nuspec XML manifest schema governing NuGet packages. It provides structured guidance on targeting framework frameworks, orchestrating assembly dependencies, defining metadata, and managing compilation assemblies, acting as the foundational automation configuration schema for .NET artifact pipelines.
  - **(2023)** [devblogs.microsoft.com: Introducing Compatible Packages on NuGet.org](https://devblogs.microsoft.com/dotnet/introducing-compatible-frameworks-on-nuget-org) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Details framework compatibility structures implemented by NuGet.org, facilitating cross-platform library discovery. Explains target framework resolution paradigms mapping dependencies across .NET Standard, .NET Core, and legacy frameworks.
#### Publishing Workflows

  - **(2023)** [gist.github.com: Creating and Publishing NuGet Packages](https://gist.github.com/andykuszyk/a5ee80ae263e77f651bed878c1deb03b) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A concise, developer-centric guide mapping the CLI workflows required to construct and publish NuGet packages. Explores packing commands, validation, local server configuration, target registry configuration, and security practices for handling API keys.
  - **(2020)** [khalidabuhakmeh.com: A .NET 5.0 Guide: From Idea To NuGet Package](https://khalidabuhakmeh.com/a-dotnet-five-guide-from-idea-to-nuget-package) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth guide detailing library creation from conceptual design down to artifact compilation in .NET. Focuses on setting up proper SDK project styles, automating versioning, target framework multi-targeting rules, and optimizing continuous integration for deployment.
### Web Frameworks

#### Microservices (1)

  - **(2024)** [Paradigm framework](https://www.paradigm.net.co) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source development platform designed to facilitate rapid, highly structured .NET microservice engineering. Standardizes dependency configurations, modular architectures, data mapping protocols, and enterprise repository patterns.

---
💡 **Explore Related:** [Java_Frameworks](./java_frameworks.md) | [Javascript](./javascript.md) | [Web3](./web3.md)

🔗 **See Also:** [AWS Pricing](./aws-pricing.md) | [Ansible](./ansible.md)

