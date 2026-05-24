# Performance Testing With Jenkins And Jmeter

!!! info "Architectural Context"
    Detailed reference for Performance Testing With Jenkins And Jmeter in the context of Platform & Site Reliability.

## Continuous Integration

### CI Tools

#### GitHub Actions

  - [thenewstack.io: Simple Load Testing with GitHub Actions](https://thenewstack.io/simple-load-testing-with-github-actions) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide for implementing low-overhead load testing routines within CI pipelines. Explores triggering synthetic benchmarks during typical code validation runs inside GitHub runners.
#### Jenkins

  - [performance-plugin](https://github.com/jenkinsci/performance-plugin) <span class='md-tag md-tag--info'>⭐ 194</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A stable Jenkins CI plugin designed to ingest, compile, and visualize execution metrics from varied load-testing libraries including JMeter, Taurus, and JUnit.
  - [plugins.jenkins.io: gatling](https://plugins.jenkins.io/gatling) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Integrates Gatling load simulation tests into modern Jenkins jobs. Features automated metrics visualization, pipeline validation, and conditional build-failing mechanisms.
## Observability and Performance

### Kubernetes Internals

#### Autotuning

  - [How Kruize Optimizes OpenShift Workloads](https://developers.redhat.com/articles/2025/06/25/how-kruize-optimizes-openshift-workloads#what_is_kruize_autotune_) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a comprehensive overview of how Kruize Autotune optimizes resource efficiency in OpenShift and Kubernetes workloads. Evaluates real-time scaling mechanisms and automated recommendations to reduce resource waste.
#### Resource Management

  - [The Hidden CPU Throttling Crisis in Kubernetes Clusters](https://www.kubenatives.com/p/the-hidden-cpu-throttling-crisis) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth analysis exposing the silent threat of CPU throttling inside Kubernetes clusters caused by rigid CFS quota management. Demonstrates how microservices suffer latency spikes even with low aggregate CPU consumption.
### Performance Testing

#### APIs

  - [youtube: JMeter API Performance Testing Tutorial 🌟](https://www.youtube.com/watch?v=8r5LYzUIepo) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A rich step-by-step video tutorial demonstrating the creation and deployment of API performance tests. Focuses on payload modeling, validation assertions, and interpreting stress test metrics under high-throughput conditions.
#### Cloud Platforms

  - [docs.microsoft.com: Azure Load Testing](https://learn.microsoft.com/en-us/azure/app-testing) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official portal documenting Microsoft Azure Load Testing, a fully managed performance validation platform that natively ingests JMeter tests to target complex cloud environments.
  - [azure.microsoft.com: Introducing Azure Load Testing: Optimize app performance' at scale](https://azure.microsoft.com/en-us/blog/introducing-azure-load-testing-optimize-app-performance-at-scale) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An informative product reveal detailing Azure Load Testing's architecture. Explains how it connects with Azure Monitor to surface service-side bottlenecks alongside synthetic request stats.
  - [infoq.com: Microsoft Introduces a Fully-Managed Azure Load Testing Service' in Preview](https://www.infoq.com/news/2021/12/azure-load-testing-preview) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — High-level overview of Microsoft’s fully-managed Azure Load Testing release. Illustrates how developers can leverage native cloud scaling to validate app reliability and discover performance boundaries.
#### Commercial Platforms

  - [octoperf.com](https://octoperf.com) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An enterprise-grade SaaS platform enabling rapid cloud-native scaling of JMeter scripts. Provides simplified infrastructure setup, robust real-time analytics, and automated reporting out-of-the-box.
  - [flood.io](https://flood.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A scalable load testing suite by Tricentis that supports JMeter, Gatling, and browser-driven scaling. Integrates directly into cloud environments to spawn distributed agents on demand.
#### Distributed Load Testing

  - **(2016)** [JMeter Distributed Testing Step-by-step](https://venkatmatta.com/wp-content/uploads/2016/03/jmeter_distributed_testing_step_by_step.pdf) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed execution manual outlining steps to orchestrate distributed JMeter server architectures. Teaches how to configure multiple remote load injectors managed by a master engine to bypass network bottlenecks.
#### HTTP Benchmarking

  - [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive introducing `pycurlb`, a fast performance tool wrapping libcurl for rapid HTTP request benchmarking in Python. Explores real-world performance results and technical comparisons.
#### Load Testing

  - [jmeter.apache.org](https://jmeter.apache.org) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Apache JMeter is the industry standard for performing robust load tests across varied protocols (HTTP, FTP, SOAP, Database). Allows extensive functional testing and architectural load emulation.
  - [jmeter.apache.org: Best Practices](https://jmeter.apache.org/usermanual/best-practices.html) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official JMeter optimization playbook outlining key configuration standards. Focuses on minimizing CLI resource utilization, visual component overhead, and tuning JVM garbage collection for stable testing.
  - [tutorialspoint.com: JMeter Quick Guide](https://www.tutorialspoint.com/jmeter/pdf/jmeter_quick_guide.pdf) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A fundamental PDF reference covering JMeter elements, request structures, variables, assertions, and visualization. Acts as an excellent quick-reference material for performance engineers.
  - [softwaretestingmagazine.com: Learning JMeter : Documentation, Tutorials,' Videos](https://www.softwaretestingmagazine.com/tools/learning-jmeter-documentation-tutorials-videos) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An aggregated knowledge index linking to advanced tutorials, video courses, and functional documentation designed to accelerate the learning curve for Apache JMeter load tests.
  - [gatling.io](https://gatling.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Gatling is an elite developer-centric performance benchmarking framework. Relies on an asynchronous engine built upon Netty and Akka to simulate massive loads using minimal system resources.
  - [Locust](https://locust.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Locust is a highly flexible, open-source distributed user simulation tool written in Python. Test behaviors are defined naturally as Python code, avoiding complex UI scripting configurations.
  - [thenewstack.io: Simple HTTP Load Testing with SLOs](https://thenewstack.io/simple-http-load-testing-with-slos) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into managing performance validations by mapping assertions to specific SLO thresholds. Emphasizes maintaining strict error budgets during automated application updates.
  - [tsenart/vegeta 🌟](https://github.com/tsenart/vegeta) <span class='md-tag md-tag--info'>⭐ 25040</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Vegeta is an exceptionally fast, command-line HTTP load-testing library written in Go. Ideal for asserting constant request rates and visualizing detailed performance latencies under heavy loads.
#### Microservices

  - [dev.to: The most elegant way to performance test your microservices running' on Kubernetes](https://dev.to/ksingh7/the-most-elegant-way-to-performance-test-your-microservices-running-on-kubernetes-2mo2) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured guide demonstrating elegant and scalable patterns for performance testing distributed microservices. Focuses on cluster-native deployments and simulating traffic anomalies directly within Kubernetes namespaces.
#### Monitoring

  - [linkedin.com: Tuning Grafana - Jmeter Dashboards](https://www.linkedin.com/pulse/tuning-grafana-jmeter-dashboards-ezhil-arasu) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized optimization guide detailing Grafana and JMeter integration. Focuses on pipeline configurations, exporting live telemetry to InfluxDB, and maintaining high-fidelity visualization dashboards without performance degradation.
#### Operating Systems

  - [blog.desdelinux.net: Microsoft Performance-Tools, una serie de herramientas' open source para analizar el rendimiento del sistema](https://blog.desdelinux.net/microsoft-performance-tools-una-serie-de-herramientas-open-source-para-analizar-el-rendimiento-del-sistema) <span class='md-tag md-tag--warning'>[ES CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Análisis en español de Microsoft Performance-Tools, una suite de código abierto basada en .NET Core para recopilar trazas y métricas del sistema operativo en entornos Linux y Windows. [SPANISH CONTENT]
#### Web Performance

  - [devops.com: Catchpoint to Acquire Webpagetest.org](https://devops.com/catchpoint-to-acquire-webpagetest-org) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines Catchpoint’s strategic acquisition of the highly popular open-source tool WebPageTest. Highlights long-term development roadmaps and standardizations for internet performance tools.
## Operations and Reliability

### Service Level Objectives

#### Progressive Delivery

  - [Iter8](https://iter8.tools) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A Kubernetes-native progressive delivery platform that orchestrates metric-driven canary releases and A/B tests. Live grounding shows Iter8's ability to validate runtime SLO performance, using Prometheus and OpenTelemetry targets to automate application promotion or rollbacks.

---
💡 **Explore Related:** [Scaffolding](./scaffolding.md) | [Sre](./sre.md) | [Testops](./testops.md)

