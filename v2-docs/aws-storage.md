# Aws Storage

!!! info "Architectural Context"
    Detailed reference for Aws Storage in the context of Cloud Providers (Hyperscalers).

## Cloud Infrastructure

### AWS Storage

#### Amazon EBS

  - **(2022)** [devopscube.com: How to Automate EBS Snapshot Creation, Retention and Deletion](https://devopscube.com/automate-ebs-snapshot-creation-deletion) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains various mechanisms for lifecycle management of AWS EBS snapshots. Covers automated configuration using Amazon DLM (Data Lifecycle Manager), custom Lambda functions, and AWS CLI scripts.
  - **(2021)** [percona.com: Performance of Various EBS Storage Types in AWS](https://www.percona.com/blog/performance-of-various-ebs-storage-types-in-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth performance analysis of EBS volume classes (gp2, gp3, io2, etc.) when hosting database engines. Contains IOPS benchmarking, throughput limits, and cost-efficiency matrices vital for database architects.
  - **(2021)** [dev.to: Adding an EBS volume to a running AWS EC2 Instance](https://dev.to/aws-builders/adding-an-ebs-volume-to-a-running-aws-ec2-instance-311l) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step tutorial on attaching, partition formatting (ext4/xfs), and mounting a new EBS volume onto an active Linux EC2 instance without triggering server downtime.
  - **(2017)** [How to Build Sparse EBS Volumes for Fun and Easy Snapshotting](https://aws.amazon.com/blogs/apn/how-to-build-sparse-ebs-volumes-for-fun-and-easy-snapshotting) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced architectural post detailing how to create sparse files inside loop devices on EBS volumes to minimize storage footprints. Analyzes the financial and performance benefits of sparse block allocations during automated snapshots.
#### Amazon EFS

  - **(2021)** [Amazon Elastic File System triples read throughput](https://aws.amazon.com/about-aws/whats-new/2021/01/amazon-elastic-file-system-triples-read-throughput) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement detailing architectural performance enhancements to AWS EFS. Details how the platform tripled read limits, providing immediate benefits to read-heavy workloads like distributed machine learning or CMS host arrays.
  - **(2021)** [infoq.com: AWS Transfer Family Introduces Support for EFS](https://www.infoq.com/news/2021/01/aws-transfer-ftp-efs) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reports on the strategic integration between AWS Transfer Family (SFTP/FTPS/FTP) and EFS. Enables developers to expose shared file systems securely directly to remote partners without managing SFTP instance clusters.
  - **(2016)** [EFS Elastic File System](https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-production-ready-in-three-regions) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The historic production-ready announcement of AWS Elastic File System (EFS). Establishes the core characteristics of shared NFS storage scaling dynamically for concurrent EC2/container instances.
#### Amazon S3


??? abstract "Architect's Technical Comparison Table"
    | Solution | Maturity | Primary Focus | Language | Stars |
    | :--- | :--- | :--- | :--- | :--- |
    | [S3 FAQ](https://aws.amazon.com/s3/faqs) |  | Amazon S3 | English | 🌟🌟🌟🌟🌟 |
    | [cloudkatha.com: Is S3 Region Specific or Global? What do you think?](https://cloudkatha.com/is-s3-region-specific-or-global-what-do-you-think) |  | Amazon S3 | English | 🌟🌟🌟 |
    | [cloudkatha.com: This is why S3 Bucket Names are unique Globally](https://cloudkatha.com/why-s3-bucket-names-are-unique-globally) |  | Amazon S3 | English | 🌟🌟🌟 |
    | [cloudkatha.com: AWS S3 Storage Classes: Everything You Need to Know](https://cloudkatha.com/aws-s3-storage-classes-everything-you-need-to-know) |  | Amazon S3 | English | 🌟🌟🌟 |
    | [acloudguru.com: S3 Glacier Instant Retrieval deep dive: Which S3 Storage Class is right for me?](https://www.pluralsight.com/resources/blog/cloud/s3-glacier-instant-retrieval-deep-dive-which-s3-storage-class-is-right-for-me) |  | Amazon S3 | English | 🌟🌟🌟 |
    | [A step-by-step guide to synchronize data between Amazon S3 buckets](https://aws.amazon.com/blogs/storage/a-step-by-step-guide-to-synchronize-data-between-amazon-s3-buckets) |  | Amazon S3 | English | 🌟🌟🌟 |

  - **(2026)** [==S3 FAQ==](https://aws.amazon.com/s3/faqs) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official AWS documentation addressing technical details of Simple Storage Service (S3). Provides absolute specifications for consistency models, replication capabilities, access control lists, and durability guarantees.
  - **(2022)** [cloudkatha.com: Is S3 Region Specific or Global? What do you think?](https://cloudkatha.com/is-s3-region-specific-or-global-what-do-you-think) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Clarifies the architectural paradox of Amazon S3's namespace being globally unique while data is stored physically in regional clusters. Details the implications on DNS, endpoint routing, and latency.
  - **(2022)** [cloudkatha.com: This is why S3 Bucket Names are unique Globally](https://cloudkatha.com/why-s3-bucket-names-are-unique-globally) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the technical constraints under the hood that necessitate globally unique S3 bucket names. Outlines DNS mapping to S3 regional endpoints and the routing restrictions of the HTTP REST API.
  - **(2022)** [cloudkatha.com: AWS S3 Storage Classes: Everything You Need to Know](https://cloudkatha.com/aws-s3-storage-classes-everything-you-need-to-know) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A complete comparative guide to S3 Storage Classes, detailing Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, and Glacier options. Analyzes pricing structures, retrieval latency, and redundancy across availability zones.
  - **(2021)** [acloudguru.com: S3 Glacier Instant Retrieval deep dive: Which S3 Storage Class is right for me?](https://www.pluralsight.com/resources/blog/cloud/s3-glacier-instant-retrieval-deep-dive-which-s3-storage-class-is-right-for-me) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into S3 Glacier Instant Retrieval, analyzing costs and access latency. Explains the strategic sweet spot of the tier for archival data that requires millisecond retrieval speeds without standard Glacier delays.
  - **(2020)** [A step-by-step guide to synchronize data between Amazon S3 buckets](https://aws.amazon.com/blogs/storage/a-step-by-step-guide-to-synchronize-data-between-amazon-s3-buckets) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS blog showing patterns for cross-bucket data synchronization. Compares the use of AWS CLI Sync, S3 Batch Operations, and S3 Same-Region / Cross-Region Replication (SRR/CRR) for diverse use cases.
#### Analytics

  - **(2021)** [Monitor Amazon S3 activity using S3 server access logs and Pandas in Python](https://aws.amazon.com/blogs/storage/monitor-amazon-s3-activity-using-s3-server-access-logs-and-pandas-in-python) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Shows how to parse raw S3 access logs using Python and Pandas. Walks through identifying bad actors, evaluating storage patterns, and monitoring data transfer metrics for cost control.
#### Hybrid Cloud

  - **(2021)** [Connect Amazon S3 File Gateway using AWS PrivateLink for Amazon S3](https://aws.amazon.com/es/blogs/architecture/connect-amazon-s3-file-gateway-using-aws-privatelink-for-amazon-s3) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural post detailing how to establish a secure, private connection from on-premises Storage Gateways to S3 via AWS PrivateLink. Prevents traffic traversal over the public internet, satisfying rigorous enterprise compliance models.
### High Availability

#### Multi-Region

  - **(2022)** [**Building an active-active, latency-based application across multiple Regions 🌟**](https://aws.amazon.com/blogs/storage/building-an-active-active-latency-based-application-across-multiple-regions) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An elite architectural blueprint for active-active multi-region AWS applications. Uses S3 Cross-Region Replication (CRR), Route 53 latency-based routing, and DynamoDB Global Tables to design highly resilient services.
### Object Storage

#### MinIO

  - **(2022)** [**blog.min.io: Certificate-based Authentication for S3**](https://www.min.io/blog/certificate-based-authentication-with-s3) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explains how to implement robust Mutual TLS (mTLS) and client certificate-based authentication with MinIO. Outlines secure key exchanges and architectural mapping of certificates to IAM policies.
### Storage

#### Distributed Filesystems

  - **(2026)** [==Ceph: A Distributed Object, Block, and File Storage Platform==](https://github.com/ceph/ceph) <span class='md-tag md-tag--info'>⭐ 16621</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry-standard unified, distributed storage system designed to provide excellent performance, reliability, and scalability.

*   Provides object, block, and file storage within a single cluster.
*   Acts as a foundational storage engine for large-scale Kubernetes PV platforms (Rook-Ceph) and private clouds.

---
💡 **Explore Related:** [Aws Tools Scripts](./aws-tools-scripts.md) | [Aws Databases](./aws-databases.md) | [Aws Spain](./aws-spain.md)

