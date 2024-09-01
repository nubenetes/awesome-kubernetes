# AWS Networking

1. [Introduction](#introduction)
2. [AWS Route 53](#aws-route-53)
3. [AWS Elastic Load Balancing (ELB)](#aws-elastic-load-balancing-elb)
4. [AWS Application Load Balancer (ALB)](#aws-application-load-balancer-alb)
5. [Gateway Load Balancer (GWLB)](#gateway-load-balancer-gwlb)
6. [AWS WAF](#aws-waf)
7. [NGINX](#nginx)
8. [AWS Latency](#aws-latency)
9. [AWS VPC](#aws-vpc)
    1. [AWS Client VPN](#aws-client-vpn)
    2. [Tailscale](#tailscale)
10. [AWS CloudFront](#aws-cloudfront)
11. [AWS API Gateway](#aws-api-gateway)
12. [Tweets](#tweets)

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
- [aws.amazon.com: Creating active/passive BGP connections over AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-active-passive-bgp-connections-over-aws-direct-connect/)
- [towardsaws.com: Networking Basics in AWS](https://towardsaws.com/networking-basics-in-aws-ab72882855c4)
- [aws.amazon.com: Network operations with AWS Network Manager](https://aws.amazon.com/products/networking/network-operations/) Efficiently manage and monitor your AWS network
- [Secure Connectivity from Public to Private: Introducing EC2 Instance Connect Endpoint](https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/)

## AWS Route 53

- [How do I transfer a domain to AWS from another registrar?](https://aws.amazon.com/premiumsupport/knowledge-center/transfer-domain-to-aws/)
- [Configuring Route 53 for cost protection from NXDOMAIN attacks](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/configuring-route53-for-cost-protection-from-nxdomain-attacks.html)

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
- [faun.pub: End To End SSL Encryption With AWS Application Load Balancer](https://faun.pub/end-to-end-ssl-encryption-with-aws-application-load-balancer-b43db918bd9e)
- [aws.amazon.com/about-aws: Application Load Balancer enables configuring HTTP client keepalive duration](https://aws.amazon.com/about-aws/whats-new/2024/03/application-load-balancer-http-keepalive-duration/)

## Gateway Load Balancer (GWLB)

- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)

## AWS WAF

- [AWS WAF enhances rate-based rules to support lower rate limits](https://aws.amazon.com/about-aws/whats-new/2024/08/aws-waf-rate-based-rules-lower-rate-limits/)

## NGINX

- [NGINX Plus on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/09/nginx-plus-on-the-aws-cloud-quick-start-reference-deployment/)

## AWS Latency

- [Find the fastest region from your location](http://aws-latency.altaircp.com/) Check AWS response time from you browser. Sharing my mini-project, it measures response time from AWS services from different regions base on your location. let me know what you think.
- [Linkedin Discussion](https://www.linkedin.com/groups/49531/49531-6092152919937794052)
    1. Don't do just a single check, the first check will be a lot slower as DNS lookups will need to be done, etc.
    2. I'd recommend doing at least 3 checks getting an average.
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
- [==betterprogramming.pub: AWS: Creating a VPC With an Auto-scaling Group Using T2.micro Instances==](https://betterprogramming.pub/aws-creating-a-vpc-with-an-auto-scaling-group-using-t2-micro-instances-4ac2c5c7795b) **Maintain a self-healing architecture**
- [alanblackmore.medium.com: What is AWS VPC Peering? 🌟](https://alanblackmore.medium.com/what-is-aws-vpc-peering-af85c1e29fb2)
- [awstip.com: Setting Up AWS VPC Endpoint Connection](https://awstip.com/setting-up-aws-vpc-endpoint-connection-d4294d0c2204)
- [towardsaws.com: How to centralize VPC endpoints in AWS](https://towardsaws.com/how-to-centralize-vpc-endpoints-in-aws-64c68b5b9d50)

### AWS Client VPN

- [cloudonaut.io: AWS Client VPN: Connected with the Cloud](https://cloudonaut.io/aws-client-vpn-connected-with-the-cloud/)

### Tailscale

- [tailscale.com: Connect to an AWS VPC using subnet routes](https://tailscale.com/kb/1021/install-aws/)

## AWS CloudFront

- [Amazon CloudFront now supports HTTP/2](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-cloudfront-now-supports-http2/)
- [aws.amazon.com: Authorization@Edge using cookies: Protect your Amazon CloudFront content from being downloaded by unauthenticated users](https://aws.amazon.com/de/blogs/networking-and-content-delivery/authorizationedge-using-cookies-protect-your-amazon-cloudfront-content-from-being-downloaded-by-unauthenticated-users/)

## AWS API Gateway

- [alexdebrie.com: A Detailed Overview of AWS API Gateway](https://www.alexdebrie.com/posts/api-gateway-elements/)
- [towardsaws.com: Accessing a Private REST API from another Private REST API in AWS API Gateway](https://towardsaws.com/accessing-a-private-rest-api-from-another-private-rest-api-in-aws-api-gateway-5112b835c0d4) In this post, we’ll see how we can access a Private REST API From Another Private REST API In AWS API Gateway. We will create 2 EC2 Instances(EC2A and EC2B) and 2 API Gateways(APIA and APIB). EC2A will be accessing EC2B with following workflow.
- [faun.pub: Using AWS API Gateway As Proxy To Our Internal Application](https://faun.pub/using-aws-api-gateway-as-proxy-to-our-internal-application-369eb115db70)
- [aws.amazon.com: Architecture patterns for consuming private APIs cross-account](https://aws.amazon.com/blogs/compute/architecture-patterns-for-consuming-private-apis-cross-account/) Architecture patterns for consuming private APIs cross-account over AWS PrivateLink

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">𝗔𝗺𝗮𝘇𝗼𝗻 𝗩irtual 𝗣rivate 𝗖loud ☁️ 🔐<br>Your 𝗹𝗼𝗴𝗶𝗰𝗮𝗹𝗹𝘆 𝗶𝘀𝗼𝗹𝗮𝘁𝗲𝗱 𝘃𝗶𝗿𝘁𝘂𝗮𝗹 𝗻𝗲𝘁𝘄𝗼𝗿𝗸 in the cloud 🛠<br><br>From Security Groups, over Route Tables to VPC Peering ↓ <a href="https://t.co/OWhIWVbJwu">pic.twitter.com/OWhIWVbJwu</a></p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1582330939442536448?ref_src=twsrc%5Etfw">October 18, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>
