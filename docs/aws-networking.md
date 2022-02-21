# AWS Networking
- [Introduction](#introduction)
- [AWS Route 53](#aws-route-53)
- [AWS Elastic Load Balancing (ELB)](#aws-elastic-load-balancing-elb)
- [AWS Application Load Balancer (ALB)](#aws-application-load-balancer-alb)
- [Gateway Load Balancer (GWLB)](#gateway-load-balancer-gwlb)
- [NGINX](#nginx)
- [AWS Latency](#aws-latency)
- [AWS VPC](#aws-vpc)
    - [AWS Client VPN](#aws-client-vpn)
    - [Tailscale](#tailscale)
- [AWS CloudFront](#aws-cloudfront)
- [AWS API Gateway](#aws-api-gateway)

## Introduction
- [AWS Networking for Developers](https://aws.amazon.com/es/blogs/apn/aws-networking-for-developers/)
- [Elastic Network Adapter](https://aws.amazon.com/blogs/aws/elastic-network-adapter-high-performance-network-interface-for-amazon-ec2)
- [AWS Cloud Networking – Zero to Hero](http://www.netdesignarena.com/index.php/2020/04/15/new-blog-series-aws-cloud-networking-zero-to-hero/)
- [cloudonaut.io: What Architects Need to Know About Networking on AWS](https://cloudonaut.io/what-architects-need-to-know-about-networking-on-aws/)
- [cloudonaut.io: Advanced AWS Networking: Pitfalls That You Should Avoid](https://cloudonaut.io/advanved-aws-networking-pitfalls-that-you-should-avoid/)
- [gprakash-sharma.medium.com: AWS Site-to-Site VPN with NAT](https://gprakash-sharma.medium.com/aws-site-to-site-vpn-with-nat-8bb99f4653ab)
- [Resolve DNS names of Network Load Balancer nodes to limit cross-Zone traffic](https://aws.amazon.com/blogs/networking-and-content-delivery/resolve-dns-names-of-network-load-balancer-nodes-to-limit-cross-zone-traffic)
- [github.com/seligman/aws-ip-ranges: AWS's ip-ranges.json](https://github.com/seligman/aws-ip-ranges) AWS adds an extra 5.5M IPv4 addresses. Tracking the history and size of AWS's ip-ranges.json file. AWS provides a data file showing the current IP ranges their services use, called ip-ranges.json. This repository tracks changes to that file, and based off a trigger on the SNS topic automatically produces this chart showing how what percentage of the Internet's IPv4 address space AWS is in control of.
- [medium: Building a Global Network with AWS Transit Gateway](https://medium.com/avmconsulting-blog/building-a-global-network-with-aws-transit-gateway-7ab0e5222f12) Connecting branch and corporate offices into the AWS cloud to build a global network is necessary to provide ubiquitous accessibility for users. This solution uses AWS Transit Gateway, AWS Direct Connect, and AWS Accelerated Site-to-Site VPN to build a modern, secure, scalable, and cost-efficient WAN on top of the AWS global network.

## AWS Route 53
- [How do I transfer a domain to AWS from another registrar?](https://aws.amazon.com/premiumsupport/knowledge-center/transfer-domain-to-aws/)

## AWS Elastic Load Balancing (ELB)
- [AWS Summit Series 2016 | London: Deep Dive on Elastic Load Balancing](https://www.youtube.com/watch?v=HinwLb2lpLQ)
- [docs.aws.amazon.com: What Is Elastic Load Balancing?](http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [ably.com: Balancing act: the current limits of AWS network load balancers](https://ably.com/blog/limits-aws-network-load-balancers)
- [==luis-sena.medium.com: Automated AWS Load Balancer Warm-Up==](https://luis-sena.medium.com/automated-aws-load-balancer-warm-up-d0b4084c8bbc) Automate AWS load balancer to avoid issues with huge traffic spikes
- [==dashbird.io: AWS Elastic Load Balancing from a Serverless perspective==](https://dashbird.io/blog/aws-application-load-balancer/) Should you switch your AWS API Gateway out for an Application Load Balancer (ALB)? A cheat sheet for all you need to know about ALB:
	- Pricing 
	- Regions 
	- Transformations 
	- Limits 
	- Permissions 
	- Health 

## AWS Application Load Balancer (ALB)
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/)
- [aws blogs - New – AWS Application Load Balancer](https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer/)
- [medium: 10 reasons why you should think about using an AWS Application Load Balancer](https://medium.com/ankercloud-engineering/10-reasons-why-you-should-think-about-using-an-aws-application-loadbalancer-945f57816c34)
- [Introducing the AWS Load Balancer Controller](https://aws.amazon.com/blogs/containers/introducing-aws-load-balancer-controller/)
- [Fine-tuning blue/green deployments on application load balancer](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)

## Gateway Load Balancer (GWLB)
- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)

## NGINX
- [NGINX Plus on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/09/nginx-plus-on-the-aws-cloud-quick-start-reference-deployment/)

## AWS Latency
- [Find the fastest region from your location](http://aws-latency.altaircp.com/) Check AWS response time from you browser. Sharing my mini-project, it measures response time from AWS services from different regions base on your location. let me know what you think.
- [Linkedin Discussion](https://www.linkedin.com/groups/49531/49531-6092152919937794052)
>1. Don't do just a single check, the first check will be a lot slower as DNS lookups will need to be done, etc.
>2. I'd recommend doing at least 3 checks getting an average.
- Run 6 checks (with a random 3-10 second delay between each one), the first can be ignored, the highest one is also ignored (as a likely outlier), then for the next 4 show the minimum, maximum and average (mean).
- [medium.com: Optimizing Latency and Bandwidth for AWS Traffic](https://medium.com/aws-activate-startup-blog/optimizing-latency-and-bandwidth-for-aws-traffic-cdfd18d0d0f7)

## AWS VPC
- [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)
- [linuxjournal.com: AWS EC2 VPC CLI](http://www.linuxjournal.com/content/aws-ec2-vpc-cli)
- [Build a Modular and Scalable Amazon VPC Architecture with New Quick Start](https://aws.amazon.com/about-aws/whats-new/2016/07/build-a-modular-and-scalable-amazon-vpc-architecture-with-new-quick-start) Build a modular virtual network architecture with Amazon VPC in 5 minutes with our new Quick Start
- [Specifying the VPC for your Amazon RDS DB Instance](https://aws.amazon.com/about-aws/whats-new/2016/08/specifying-the-vpc-for-your-amazon-rds-db-instance/) You can now easily change the Amazon VPC used by your Amazon RDS DB instance!
- [awsfundamentals.blogspot.com: AWS Virtual Private Cloud - VPC](https://awsfundamentals.blogspot.com/2019/12/aws-vpc-fundamental.html)
- [Reduce Cost and Increase Security with Amazon VPC Endpoints](https://aws.amazon.com/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/)
- [ealtili.medium.com: Deepdive to VPCs and Connections to VPC](https://ealtili.medium.com/deepdive-to-vpcs-and-connections-to-vpc-2de3fb164d7c)
- [Centralize access using VPC interface endpoints to access AWS services across multiple VPCs](https://aws.amazon.com/blogs/networking-and-content-delivery/centralize-access-using-vpc-interface-endpoints/)

### AWS Client VPN
- [cloudonaut.io: AWS Client VPN: Connected with the Cloud](https://cloudonaut.io/aws-client-vpn-connected-with-the-cloud/)

### Tailscale
- [tailscale.com: Connect to an AWS VPC using subnet routes](https://tailscale.com/kb/1021/install-aws/)

## AWS CloudFront
- [Amazon CloudFront now supports HTTP/2](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-cloudfront-now-supports-http2/)

## AWS API Gateway
- [alexdebrie.com: A Detailed Overview of AWS API Gateway](https://www.alexdebrie.com/posts/api-gateway-elements/)