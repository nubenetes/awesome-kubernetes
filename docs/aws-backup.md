# AWS Backup and Migrations. Design for failure. Disaster Recovery

1. [Introduction](#introduction)
2. [AWS Backup Service](#aws-backup-service)
3. [AWS Migrations](#aws-migrations)
    1. [Migrating On Premise VM to AWS](#migrating-on-premise-vm-to-aws)

## Introduction

- [Quantum Taps AWS for Cloud-Powered Disaster Recovery](http://www.infostor.com/backup-and_recovery/quantum-taps-aws-for-cloud-powered-disaster-recovery.html)
- [Linkedin discussion: Need help on Backup and restore methods of EC2 using s3 services](https://www.linkedin.com/groups/49531/49531-6093375473969090562)
- [Design for failure lessons learnt from the Sydney AWS outage](https://www.hava.io/blog/design-for-failure-lessons-learnt-from-the-sydney-aws-outage)
- [Chaos Monkey](https://github.com/Netflix/SimianArmy/wiki/Chaos-Monkey) The Netflix Chaos Monkey tool allows you to proactively launch attack code against your infrastructure to cause failures and give you the chance to fix potential problems before they occur on their own.
- [Udemy - AWS: How to Architect with a Design for Failure Approach](https://www.udemy.com/how-to-architect-with-a-design-for-failure-approach/)
- [How to Restore Your Instance Data from a Backup using Snapshots on AWS EC2/EBS](https://www.cloudinsidr.com/content/how-to-restore-your-instance-data-from-a-backup-using-snapshots-on-aws-ec2ebs/)
- [Backup and archive to AWS Storage Gateway VTL with Veeam Backup & Replication v9](https://aws.amazon.com/es/about-aws/whats-new/2016/08/backup-and-archive-to-aws-storage-gateway-vtl-with-veeam-backup-and-replication-v9/)
- [Creating Disaster Recovery Mechanisms Using Amazon Route 53 🌟](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/)
    - [Disaster recovery with AWS managed services, Part 2: Multi-Region/backup and restore 🌟](https://aws.amazon.com/blogs/architecture/disaster-recovery-with-aws-managed-services-part-ii-multi-region-backup-and-restore/)
- [dev.to: Best way to Automate AWS EBS Snapshots (without scripts)](https://dev.to/aws-builders/how-to-automate-aws-ebs-snapshots-54og)
- [Quick Restoration through Replacing the Root Volumes of Amazon EC2 instances](https://aws.amazon.com/blogs/compute/quick-restoration-through-replacing-the-root-volumes-of-amazon-ec2/)

## AWS Backup Service

- [AWS Backup Service](https://aws.amazon.com/backup)
- [medium: AWS Backup Service for Amazon RDS](https://medium.com/avmconsulting-blog/aws-backup-service-for-amazon-rds-3e6f5827aa66)
- [Automate and centrally manage data protection for Amazon S3 with AWS Backup](https://aws.amazon.com/blogs/storage/automate-and-centrally-manage-data-protection-for-amazon-s3-with-aws-backup/)
- [Preview – AWS Backup Adds Support for Amazon S3](https://aws.amazon.com/blogs/aws/preview-aws-backup-adds-support-for-amazon-s3/)
- [Disaster Recovery with AWS Managed Services, Part I: Single Region](https://aws.amazon.com/blogs/architecture/disaster-recovery-with-aws-managed-services-part-i-single-region/)
- [AWS Backup supports cross-Region backups in four new Regions](https://aws.amazon.com/about-aws/whats-new/2023/05/aws-backup-cross-region-backups-four-regions/)

## AWS Migrations

- [New AWS Competency – AWS Migration](https://aws.amazon.com/blogs/aws/new-aws-competency-aws-migration/)
- [Migrate Resources Between AWS Accounts](https://aws.amazon.com/blogs/architecture/migrate-resources-between-aws-accounts)
- [==Multi-Region Migration using AWS Application Migration Service==](https://aws.amazon.com/blogs/architecture/multi-region-migration-using-aws-application-migration-service/) I built my infrastructure in Region A, I want to now move it to Region B.

### Migrating On Premise VM to AWS

- [youtube: Migrating On Premise VM to AWS | VM Import/Export | Create EC2 instance based on on-premises server](https://youtu.be/buzusNljpy4)