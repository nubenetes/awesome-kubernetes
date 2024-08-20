# AWS Storage. S3 & EBS. AWS Storage Gateway

1. [Introduction](#introduction)
2. [Amazon EFS Elastic File System](#amazon-efs-elastic-file-system)
3. [AWS Transfer](#aws-transfer)
4. [AWS S3 Sync](#aws-s3-sync)

## Introduction

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
- [Connect Amazon S3 File Gateway using AWS PrivateLink for Amazon S3](https://aws.amazon.com/es/blogs/architecture/connect-amazon-s3-file-gateway-using-aws-privatelink-for-amazon-s3/)
- [blog.min.io: Certificate-based Authentication for S3](https://blog.min.io/certificate-based-authentication-with-s3/) MinIO encrypts data when stored on disk and when transmitted over the network.
- [==acloudguru.com: S3 Glacier Instant Retrieval deep dive: Which S3 Storage Class is right for me?==](https://acloudguru.com/blog/engineering/s3-glacier-instant-retrieval-deep-dive-which-s3-storage-class-is-right-for-me)
- [Monitor Amazon S3 activity using S3 server access logs and Pandas in Python](https://aws.amazon.com/blogs/storage/monitor-amazon-s3-activity-using-s3-server-access-logs-and-pandas-in-python/)
- [Building an active-active, latency-based application across multiple Regions 🌟](https://aws.amazon.com/blogs/storage/building-an-active-active-latency-based-application-across-multiple-regions/)
- [dev.to: Adding an EBS volume to a running AWS EC2 Instance](https://dev.to/aws-builders/adding-an-ebs-volume-to-a-running-aws-ec2-instance-311l)
- [awstip.com: Uploading files to S3 through API Gateway](https://awstip.com/uploading-files-to-s3-through-api-gateway-7bb78c0d0483)
    - When you have a front-end application and need to upload files to an S3 bucket securely and keep your bucket private, you can use API Gateway to post your files to S3.
    - If you don´t want to make any modifications to the file and upload it as is, you can upload the files directly from API Gateway to S3. But if some modifications are required, you may consider using Lambda to receive the request from API Gateway and upload to S3. In this article we will not use Lambda.

## Amazon EFS Elastic File System

- [EFS Elastic File System](https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-production-ready-in-three-regions)
- [Amazon Elastic File System triples read throughput](https://aws.amazon.com/about-aws/whats-new/2021/01/amazon-elastic-file-system-triples-read-throughput/)

## AWS Transfer

- [infoq.com: AWS Transfer Family Introduces Support for EFS](https://www.infoq.com/news/2021/01/aws-transfer-ftp-efs/)

## AWS S3 Sync

- [==blog.awsfundamentals.com: AWS S3 Sync - An Extensive Guide==](https://blog.awsfundamentals.com/aws-s3-sync) Learn all about AWS S3 sync - covering download, upload, synchronize buckets, file selection patterns, dry-run, and more - examples included. The CLI is a daily tool for every DevOps engineer working with AWS. A deep-dive for the 𝗮𝘄𝘀 𝘀𝟯 𝘀𝘆𝗻𝗰 command & its powerful options.
