# AWS Monitoring and Logging

1. [Introduction](#introduction)
2. [Metrics](#metrics)
3. [AWS Cloudwatch](#aws-cloudwatch)
4. [AWS Cloud Map and HealthChecks](#aws-cloud-map-and-healthchecks)
5. [AWS Managed Services for Prometheus and Grafana](#aws-managed-services-for-prometheus-and-grafana)
6. [AWS and Splunk](#aws-and-splunk)

## Introduction

- [github: Steps I used to install Nagios in the cloud](https://github.com/andrewpuch/nagios_setup)
- [github: ElectricEye](https://github.com/jonrau1/ElectricEye/blob/master/README.md) is a set of Python scripts (affectionately called Auditors) that continuously monitor your AWS infrastructure looking for configurations related to confidentiality, integrity and availability that do not align with AWS best practices.
- [medium: AWS Account Security Monitoring](https://medium.com/swlh/aws-account-security-monitoring-d7ca129d52ac)
- [==elastic.co: Elastic and AWS: Accelerating the cloud migration journey==](https://www.elastic.co/blog/elastic-and-aws-accelerate-your-cloud-migration-journey)
- [How to use AWS Config and CloudTrail to find who made changes to a resource](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-and-cloudtrail-to-find-who-made-changes-to-a-resource)
- [kevintuei.medium.com: A Deep Dive into Logs and Metrics for AWS Observability — One Observability Workshop](https://kevintuei.medium.com/a-deep-dive-into-logs-and-metrics-for-aws-observability-one-observability-workshop-14c162932174)

## Metrics

- [logz.io: What are AWS EC2 Instances? A Tutorial for EC2 Metrics Shipping with Logz.io](https://logz.io/blog/aws-ec2-metrics)
- [logz.io: A Guide to Monitoring AWS Lambda Metrics with Prometheus & Logz.io](https://logz.io/blog/aws-lambda-metrics-monitoring-guide)

## AWS Cloudwatch

- [threatstack.com: 50 Best AWS CloudWatch Tutorials](https://www.f5.com/company/blog)
- [Amazon CloudWatch now monitors Prometheus metrics from Container environments](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-monitors-prometheus-metrics-container-environments)
- [Amazon CloudWatch Dashboards now supports sharing](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-dashboards-supports-sharing)
- [How BT uses Amazon CloudWatch to monitor millions of devices](https://aws.amazon.com/blogs/mt/how-bt-uses-amazon-cloudwatch-to-monitor-millions-of-devices)
- [Extending and exploring alarm history in Amazon CloudWatch – part 2](https://aws.amazon.com/blogs/mt/extending-and-exploring-alarm-history-in-amazon-cloudwatch-part-2)
- [dzone: Optimize AWS Costs With CloudWatch's Advanced Metrics, Dashboards, and Alerts](https://dzone.com/articles/optimize-aws-costs-with-cloudwatchs-advanced-metri) leveraging advanced dashboarding with Amazon CloudWatch to efficiently manage and analyze AWS costs.

## AWS Cloud Map and HealthChecks

- [Custom Health Check: HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html) Cloud Map will eventually mark the instance as unhealthy if it doesn't receive the health status in 30 seconds. Custom health checks are implemented as regular Route53 healthchecks that check S3 bucket keys (note http access instead of https).

## AWS Managed Services for Prometheus and Grafana

- [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus) Highly available, secure, and managed monitoring for your containers
    - [medium.com: Up and running with Amazon Managed Service for Prometheus](https://medium.com/devops-techable/up-and-running-with-amazon-managed-service-for-prometheus-6fd12e56bff6)
- [Amazon Managed Service for Grafana](https://aws.amazon.com/grafana) Powerful, interactive data visualizations for builders, operators, and business leaders
- [infoq.com: AWS Introduces Amazon Managed Service for Grafana and Amazon Managed Service for Prometheus](https://www.infoq.com/news/2021/01/aws-grafana-prometheus)

## AWS and Splunk

- [blogs.splunk.com: AWS Agility + Splunk Visibility = Customer Success](https://blogs.splunk.com/2016/06/22/aws-video)

## Service Topology and Dependency Mapping
  - **(2026)** [From Silos to Service Topology: Why Netflix Built a Real-Time Service Map](https://netflixtechblog.com/from-silos-to-service-topology-why-netflix-built-a-real-time-service-map-0165ba13a7bc?gi=82dbd1ef7444&source=rss----2615bd06b42e---4) 🌟 - Netflix details the architecture of Service Topology, a system that combines eBPF, IPC metrics, and distributed tracing to construct a real-time microservice dependency graph.
