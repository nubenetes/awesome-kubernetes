# Monitoring

!!! info "Architectural Context"
    Detailed reference for Monitoring in the context of Architectural Foundations.

## Cloud Native Infrastructure

### Observability

#### Distributed Tracing

##### Jaeger Platform

  - **(2025)** [==jaegertracing.io==](https://www.jaegertracing.io) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official gateway for Jaeger, a CNCF-graduated distributed tracing platform. Essential for microservice architectures to monitor transactions, perform root-cause analysis, optimize performance bottlenecks, and visualize complex request propagation paths.
#### Log Analysis

##### Visualization Tools

  - **(2025)** [==Kibana==](https://www.elastic.co/kibana) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The foundational visualization and management interface for the Elastic Stack. Enables operators to search, index, analyze, and construct real-time security dashboards and log analysis patterns for high-throughput microservice applications.
## Cloud Native Languages

### Java

#### Performance Tuning

  - **(2024)** [fastthread.io](https://fastthread.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Industrial-grade online Java thread dump analyzer that uses AI diagnostics to identify CPU spikes, thread leaks, and deadlock patterns. Essential for post-mortem analysis of containerized JVM workloads.
  - **(2024)** [gceasy.io](https://gceasy.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Machine-learning powered JVM Garbage Collection log analyzer. Automates the detection of memory leaks, GC pauses, and heap sizing misconfigurations, offering actionable recommendations for optimization.
  - **(2024)** [heaphero.io](https://heaphero.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An automated cloud-based JVM heap dump analyzer built to parse large memory dumps quickly. Detects memory leaks and optimizes data structure footprints to resolve OutOfMemoryError crashes.
  - **(2022)** [tier1app.com](https://tier1app.com) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A dedicated APM tool for analyzing Java thread dumps and performance. Provides automated diagnostics for thread contention and deadlocks to optimize JVM application responsiveness.
## Observability (1)

### Monitoring Practices

#### Enterprise Best Practices

  - **(2022)** [sysdig.com: Seven Kubernetes monitoring best practices every monitoring solution should enable](https://www.sysdig.com/blog/kubernetes-monitoring-best-practices) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Sysdig's analysis outlining seven foundational best practices for Kubernetes metric collection. Focuses on cluster plane telemetry, standard label metadata usage, dynamic scraping strategies, and optimizing alert signal-to-noise ratios.
## Observability and Performance

### Performance Testing

#### HTTP Benchmarking

  - **(2022)** [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive introducing `pycurlb`, a fast performance tool wrapping libcurl for rapid HTTP request benchmarking in Python. Explores real-world performance results and technical comparisons.
## Operations and Reliability

### Observability and Monitoring

#### Foundations

  - **(2016)** [==Monitoring Distributed Systems - Google SRE Book==](https://sre.google/sre-book/monitoring-distributed-systems) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry-standard chapter from Google's SRE book detailing the implementation of distributed systems monitoring. It defines the 'Four Golden Signals'—latency, traffic, errors, and saturation—providing practical blueprints to prevent alert fatigue and build actionable dashboard designs.
## Runtime Optimizations

### Kubernetes Tuning

#### Monitoring and Profiling

  - **(2021)** [blog.openshift.com: Debugging Java Applications On OpenShift and Kubernetes](https://www.redhat.com/en/blog/debugging-java-applications-on-openshift-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walkthrough covering remote JVM agent connection attachment procedures targeting pods deployed within secured target Kubernetes namespaces.

---
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Cheatsheets](./cheatsheets.md) | [Linux](./linux.md)

