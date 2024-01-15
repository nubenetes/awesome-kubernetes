# Performance testing with jenkins and JMeter or Gatling

1. [Introduction](#introduction)
2. [Performance testing of microservices running on Kubernetes](#performance-testing-of-microservices-running-on-kubernetes)
3. [JMeter](#jmeter)
4. [JMeter based Cloud solutions](#jmeter-based-cloud-solutions)
5. [Jenkins \& JMeter](#jenkins--jmeter)
6. [Gatling](#gatling)
    1. [API Load Testing](#api-load-testing)
    2. [Gatling and Maven](#gatling-and-maven)
7. [Jenkins \& Gatling](#jenkins--gatling)
8. [Azure Load Testing Service](#azure-load-testing-service)
9. [Load Testing with GitHub Actions](#load-testing-with-github-actions)
10. [Alternatives](#alternatives)
11. [Serverless Load Testing](#serverless-load-testing)
12. [Videos](#videos)

## Introduction

- [Dzone: 14 Best Performance Testing Tools and APM Solutions](https://dzone.com/articles/14-best-performance-testing-tools-and-apm-solution)
- [blazemeter.com: Open Source Load Testing Tools: Which One Should You Use?](https://www.blazemeter.com/blog/open-source-load-testing-tools-which-one-should-you-use)
- [baeldung.com: Gatling vs JMeter vs The Grinder: Comparing Load Test Tools](https://www.baeldung.com/gatling-jmeter-grinder-comparison)
- [blog.cloud-mercato.com: New HTTP benchmark tool **pycurlb**](https://blog.cloud-mercato.com/new-http-benchmark-tool-pycurlb/)
- [Gatling vs JMeter](https://dzone.com/articles/gatling-vs-jmeter)

## Performance testing of microservices running on Kubernetes

- [dev.to: The most elegant way to performance test your microservices running on Kubernetes](https://dev.to/ksingh7/the-most-elegant-way-to-performance-test-your-microservices-running-on-kubernetes-2mo2) In this article, you'll learn how to measure the performance of backend applications running on Kubernetes & how to use Vegeta, a versatile HTTP load testing and benchmarking tool written in Golang
- [garden.io: Performance testing on a microservice architecture](https://garden.io/blog/performance-testing)

## JMeter

- [jmeter.apache.org](https://jmeter.apache.org/)
- [jmeter.apache.org: Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
- [Dzone: JMeter tutorial](https://dzone.com/articles/jmeter-tutorial-1)
- [Dzone: JMeter tutorial for beginners](https://dzone.com/articles/jmeter-tutorial-for-beginners-jmeter-load-testing)
- [Dzone: Getting started with JMeter](https://dzone.com/articles/getting-started-with-jmeter-a-basic-tutorial)
- [Dzone: Apache JMeter Keyboards shortcuts](https://dzone.com/articles/apache-jmeter-keyboard-shortcuts)
- [Dzone: Apache JMeter functions](https://dzone.com/articles/apache-jmeter-functions-an-introduction)
- [Dzone: What's new in JMeter 3.3](https://dzone.com/articles/whats-new-in-jmeter-33)
- [Dzone: The simple anatomy of a good performance report](https://dzone.com/articles/the-simple-anatomy-of-a-good-performance-report)
- [tutorialspoint.com: JMeter Quick Guide](https://www.tutorialspoint.com/jmeter/pdf/jmeter_quick_guide.pdf)
- [JMeter Distributed Testing Step-by-step](https://venkatmatta.files.wordpress.com/2016/03/jmeter_distributed_testing_step_by_step.pdf)
- [testinglpoint.com: Timer in JMeter](https://www.testinglpoint.com/timer/) Timer in JMeter is easy but crucial part of JMeter where we have to manage the thread user count and time to apply the load to the application.
- [youtube: JMeter API Performance Testing Tutorial 🌟](https://www.youtube.com/watch?v=8r5LYzUIepo)
- [testinglpoint.com: Features of JMeter](https://www.testinglpoint.com/features-of-jmeter/) Features and disadvantages.
- [linkedin.com: Tuning Grafana - Jmeter Dashboards](https://www.linkedin.com/pulse/tuning-grafana-jmeter-dashboards-ezhil-arasu/) This article is for performance testers who configured JMeter - influx - Grafana setup or Jmeter - Prometheus - Grafana setup.
- [gslab.com: How to Optimize Performance Testing with Apache JMeter and Resources Monitoring Using DStat](https://www.gslab.com/blogs/performance-testing-with-Apache-JMeter)
- [rollno748.medium.com: Load testing GCP Pub/Sub using JMeter](https://rollno748.medium.com/load-testing-gcp-pub-sub-using-jmeter-9eff79440beb)
- [softwaretestingmagazine.com: Learning JMeter : Documentation, Tutorials, Videos](https://www.softwaretestingmagazine.com/tools/learning-jmeter-documentation-tutorials-videos/)

## JMeter based Cloud solutions

- [octoperf.com](https://octoperf.com/)
- [blazemeter.com](https://www.blazemeter.com/)
- [flood.io](https://flood.io/)

## Jenkins & JMeter

- [jenkinsci/performance-plugin](https://github.com/jenkinsci/performance-plugin)
    - [plugins.jenkins.io: performance](https://plugins.jenkins.io/performance/)
- [Blazemeter.com: Continuous Integration 101 - How to run Jmeter with jenkins 🌟](https://www.blazemeter.com/blog/continuous-integration-101-how-run-jmeter-jenkins)
- [baeldung.com: Configure Jenkins to Run and Show JMeter Tests](https://www.baeldung.com/jenkins-and-jmeter)
- [DZone.com: 2 ways to integrate jmeter tests into jenkins](https://dzone.com/articles/2-ways-to-integrate-jmeter-tests-into-jenkins)
- [Guru99.com: Jmeter and BlazeMeter Integration with Jenkins](https://www.guru99.com/jenkins-jmeter-blazemeter.html)

## Gatling

- [gatling.io](https://gatling.io/)
- [Gatling Cloud Marketplaces](https://gatling.io/gatling-frontline/cloud-marketplaces/)
- [Perfomance Testing with Gatling](https://dzone.com/articles/perfomance-testing-with-gatling)
- [Gatling: A Lightweight Load Testing Tool](https://dzone.com/articles/gatling-light-weight-load-testing-tool)
- [An Introduction to Load Testing With Gatling](https://dzone.com/articles/gatling-gun-is-now-a-prospecting-tool-for-testers)
- [8 Reasons You Should Use Gatling for Your Load Testing](https://dzone.com/articles/8-reasons-you-should-use-gatling-for-your-load-tes)
- [Measuring Performance With Gatling](https://dzone.com/articles/let-measure-performance-with-gatling)
- [Gatling Performance Testing Pros and Cons](https://dzone.com/articles/gatling-performance-testing-pros-and-cons)
- [How to Set up a Gatling Test's Implementation Environment 🌟](https://dzone.com/articles/how-to-set-up-a-gatling-tests-implementation-envir)
- [Gatling Tool Review for Performance Tests (Written in Scala)](https://dzone.com/articles/gatling-tool-review-for-performance-tests-written)
- [How to Use RegEx Extractor in Gatling Projects](https://dzone.com/articles/how-to-use-regex-extractor-in-gatling-projects)
- [How to Implement Load Test Scenarios in Gatling](https://dzone.com/articles/how-to-implement-load-test-scenarios-in-gatling)
- [qautomation.blog: Power Full Load Testing Tool : Gatling](https://qautomation.blog/2019/05/03/power-full-load-testing-tool-gatling/)

### API Load Testing

- [API Load Testing With Gatling](https://dzone.com/articles/api-load-testing-with-gatling) In this article, we'll learn how to perform a load test on a REST API endpoint using Gatling and JMeter. Read on for more information!
- [Load Testing Your DataBase-Connected APIs With Gatling](https://dzone.com/articles/load-testing-your-database-connected-apis-with-gat)

### Gatling and Maven

- [How to Use Gatling With Maven](https://dzone.com/articles/how-to-use-gatling-with-maven) Learn all the details of how to integrate the Gatling performance testing framework with a Maven project in this tutorial.
- [Gatling Integration With Maven](https://dzone.com/articles/gatling-integration-with-maven)

## Jenkins & Gatling

- [gatling.io: Jenkins plugin](https://gatling.io/docs/current/extensions/jenkins_plugin/)
- [baeldung.com: Run Gatling Tests From Jenkins](https://www.baeldung.com/jenkins-run-gatling-tests)
- [plugins.jenkins.io: gatling](https://plugins.jenkins.io/gatling/)
- [medium.com: Pipeline Performance Testing with Jenkins and Gatling](https://medium.com/thepeg/pipeline-performance-testing-with-jenkins-and-gatling-b7b762274680)

## Azure Load Testing Service

- [docs.microsoft.com: Azure Load Testing](https://docs.microsoft.com/azure/load-testing/)
- [azure.microsoft.com: Introducing Azure Load Testing: Optimize app performance at scale](https://azure.microsoft.com/en-us/blog/introducing-azure-load-testing-optimize-app-performance-at-scale/)
- [venturebeat.com: Microsoft launches fully managed Azure Load Testing service](https://venturebeat.com/2021/11/30/microsoft-launches-fully-managed-azure-load-testing-service/)
- [infoq.com: Microsoft Introduces a Fully-Managed Azure Load Testing Service in Preview](https://www.infoq.com/news/2021/12/azure-load-testing-preview/)

## Load Testing with GitHub Actions

- [thenewstack.io: Simple Load Testing with GitHub Actions](https://thenewstack.io/simple-load-testing-with-github-actions/)

## Alternatives

- [webpagetest.org](https://webpagetest.org/)
- [devops.com: Catchpoint to Acquire Webpagetest.org](https://devops.com/catchpoint-to-acquire-webpagetest-org/)
- [Distributed Load Testing on AWS 🌟](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
    - [amazon.com: Introducing Distributed Load Testing v1.3](https://aws.amazon.com/about-aws/whats-new/2021/05/introducing-distributed-load-testing-v1-3/)
- [Locust](https://locust.io/) An open source load testing tool. Define user behaviour with Python code, and swarm your system with millions of simultaneous users.
- [blog.dream11engineering.com: Finding Order in Chaos: How We Automated Performance Testing with Torque](https://blog.dream11engineering.com/finding-order-in-chaos-how-we-automated-performance-testing-with-torque-6eb63706fcea)
- [blog.desdelinux.net: Microsoft Performance-Tools, una serie de herramientas open source para analizar el rendimiento del sistema](https://blog.desdelinux.net/microsoft-performance-tools-una-serie-de-herramientas-open-source-para-analizar-el-rendimiento-del-sistema/)
- [tech.loveholidays.com: Load testing in production with Grafana Loki, Kubernetes and Golang](https://tech.loveholidays.com/load-testing-in-production-with-grafana-loki-kubernetes-and-golang-1699554d2aa3)
- [==Iter8==](https://iter8.tools/) Kubernetes Release Optimizer
    - [thenewstack.io: Simple HTTP Load Testing with SLOs](https://thenewstack.io/simple-http-load-testing-with-slos/) Iter8’s command-line interface (CLI) makes it simple and easy to set up load tests for HTTP services with SLO specifications, verify that the target service meets the SLOs, and create a visual report of the load test.
- [tsenart/vegeta 🌟](https://github.com/tsenart/vegeta) HTTP load testing tool and library. It's over 9000! Vegeta is a versatile HTTP load testing tool built out of a need to drill HTTP services with a constant request rate. It can be used both as a command line utility and a library.

## Serverless Load Testing

- [betterprogramming.pub: The 5-Step Checklist for Serverless Load Testing](https://betterprogramming.pub/the-5-step-checklist-for-serverless-load-testing-346f4a60841d)

## Videos

??? note "Click to expand!"

	<center>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/_l8yIqMpWT0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</center>
