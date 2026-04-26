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
- [Resolve DNS names of Network Load Balancer nodes to limit cross-Zone traffic](https://aws.amazon.com/blogs/networking-and-content-delivery/resolve-dns-names-of-network-load-balancer-nodes-to-limit-cross-zone-traffic)
- [github.com/seligman/aws-ip-ranges: AWS's ip-ranges.json](https://github.com/seligman/aws-ip-ranges) AWS adds an extra 5.5M IPv4 addresses. Tracking the history and size of AWS's ip-ranges.json file. AWS provides a data file showing the current IP ranges their services use, called ip-ranges.json. This repository tracks changes to that file, and based off a trigger on the SNS topic automatically produces this chart showing how what percentage of the Internet's IPv4 address space AWS is in control of.
- [aws.amazon.com: Creating active/passive BGP connections over AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-active-passive-bgp-connections-over-aws-direct-connect/)
- [aws.amazon.com: Network operations with AWS Network Manager](https://aws.amazon.com/products/networking/network-operations/) Efficiently manage and monitor your AWS network
- [Secure Connectivity from Public to Private: Introducing EC2 Instance Connect Endpoint](https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/)

## AWS Route 53

- [How do I transfer a domain to AWS from another registrar?](https://aws.amazon.com/premiumsupport/knowledge-center/transfer-domain-to-aws/)
- [Configuring Route 53 for cost protection from NXDOMAIN attacks](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/configuring-route53-for-cost-protection-from-nxdomain-attacks.html)

## AWS Elastic Load Balancing (ELB)

- [AWS Summit Series 2016 | London: Deep Dive on Elastic Load Balancing](https://www.youtube.com/watch?v=HinwLb2lpLQ)
- [docs.aws.amazon.com: What Is Elastic Load Balancing?](http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
- [ably.com: Balancing act: the current limits of AWS network load balancers](https://ably.com/blog/limits-aws-network-load-balancers)
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
- [Introducing the AWS Load Balancer Controller](https://aws.amazon.com/blogs/containers/introducing-aws-load-balancer-controller/)
- [Fine-tuning blue/green deployments on application load balancer](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)
- [aws.amazon.com/about-aws: Application Load Balancer enables configuring HTTP client keepalive duration](https://aws.amazon.com/about-aws/whats-new/2024/03/application-load-balancer-http-keepalive-duration/)

## Gateway Load Balancer (GWLB)

- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)

## AWS WAF

- [AWS WAF enhances rate-based rules to support lower rate limits](https://aws.amazon.com/about-aws/whats-new/2024/08/aws-waf-rate-based-rules-lower-rate-limits/)

## NGINX

- [NGINX Plus on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/09/nginx-plus-on-the-aws-cloud-quick-start-reference-deployment/)

## AWS Latency

- [Linkedin Discussion](https://www.linkedin.com/groups/49531/49531-6092152919937794052)
    1. Don't do just a single check, the first check will be a lot slower as DNS lookups will need to be done, etc.
    2. I'd recommend doing at least 3 checks getting an average.
- Run 6 checks (with a random 3-10 second delay between each one), the first can be ignored, the highest one is also ignored (as a likely outlier), then for the next 4 show the minimum, maximum and average (mean).

## AWS VPC

- [linuxjournal.com: AWS EC2 VPC CLI](http://www.linuxjournal.com/content/aws-ec2-vpc-cli)
- [Build a Modular and Scalable Amazon VPC Architecture with New Quick Start](https://aws.amazon.com/about-aws/whats-new/2016/07/build-a-modular-and-scalable-amazon-vpc-architecture-with-new-quick-start) Build a modular virtual network architecture with Amazon VPC in 5 minutes with our new Quick Start
- [Specifying the VPC for your Amazon RDS DB Instance](https://aws.amazon.com/about-aws/whats-new/2016/08/specifying-the-vpc-for-your-amazon-rds-db-instance/) You can now easily change the Amazon VPC used by your Amazon RDS DB instance!
- [awsfundamentals.blogspot.com: AWS Virtual Private Cloud - VPC](https://awsfundamentals.blogspot.com/2019/12/aws-vpc-fundamental.html)
- [Reduce Cost and Increase Security with Amazon VPC Endpoints](https://aws.amazon.com/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/)
- [Centralize access using VPC interface endpoints to access AWS services across multiple VPCs](https://aws.amazon.com/blogs/networking-and-content-delivery/centralize-access-using-vpc-interface-endpoints/)

### AWS Client VPN

- [cloudonaut.io: AWS Client VPN: Connected with the Cloud](https://cloudonaut.io/aws-client-vpn-connected-with-the-cloud/)

### Tailscale

- [tailscale.com: Connect to an AWS VPC using subnet routes](https://tailscale.com/kb/1021/install-aws/)

## AWS CloudFront

- [Amazon CloudFront now supports HTTP/2](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-cloudfront-now-supports-http2/)
- [aws.amazon.com: Authorization@Edge using cookies: Protect your Amazon CloudFront content from being downloaded by unauthenticated users](https://aws.amazon.com/de/blogs/networking-and-content-delivery/authorizationedge-using-cookies-protect-your-amazon-cloudfront-content-from-being-downloaded-by-unauthenticated-users/)

## AWS API Gateway

- [alexdebrie.com: A Detailed Overview of AWS API Gateway](https://www.alexdebrie.com/posts/api-gateway-elements/)
- [aws.amazon.com: Architecture patterns for consuming private APIs cross-account](https://aws.amazon.com/blogs/compute/architecture-patterns-for-consuming-private-apis-cross-account/) Architecture patterns for consuming private APIs cross-account over AWS PrivateLink

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">𝗔𝗺𝗮𝘇𝗼𝗻 𝗩irtual 𝗣rivate 𝗖loud ☁️ 🔐<br>Your 𝗹𝗼𝗴𝗶𝗰𝗮𝗹𝗹𝘆 𝗶𝘀𝗼𝗹𝗮𝘁𝗲𝗱 𝘃𝗶𝗿𝘁𝘂𝗮𝗹 𝗻𝗲𝘁𝘄𝗼𝗿𝗸 in the cloud 🛠<br><br>From Security Groups, over Route Tables to VPC Peering ↓ <a href="https://t.co/OWhIWVbJwu">pic.twitter.com/OWhIWVbJwu</a></p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1582330939442536448?ref_src=twsrc%5Etfw">October 18, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>