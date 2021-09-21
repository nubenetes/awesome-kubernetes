# Site Reliability Engineering (SRE) 
- [SRE](#sre)
- [SRE Tools](#sre-tools)
- [Service Level Objectives (SLO)](#service-level-objectives-slo)
  - [OpenSLO](#openslo)
- [Videos](#videos)
- [Tweets](#tweets)
## SRE
- [wikipedia: Site Reliability Engineering](https://en.wikipedia.org/wiki/Site_Reliability_Engineering)
- [sre.google: What is Site Reliability Engineering (SRE)? 🌟](https://sre.google/)
- [cloud.google.com: SRE vs. DevOps: competing standards or close friends?](https://cloud.google.com/blog/products/gcp/sre-vs-devops-competing-standards-or-close-friends)
- [overops.com: DevOps vs. SRE: What’s the Difference Between Them, and Which One Are You?](https://blog.overops.com/devops-vs-sre-whats-the-difference-between-them-and-which-one-are-you/)
- [victorops.com: SRE vs. DevOps](https://victorops.com/blog/sre-vs-devops)
- [devops.com: SRE vs. DevOps — a False Distinction?](https://devops.com/sre-vs-devops-false-distinction/)
- [devops.com: SRE vs. DevOps vs. Cloud Native: The Server Cage Match](https://devops.com/sre-devops-cloud-native-server-cage-match/)
- [devops.com: Site Reliability Engineering 101: DevOps Versus SRE](https://devops.com/site-reliability-engineering-101-devops-versus-sre/)
- [bmc.com: SRE vs DevOps: What’s The Difference?](https://www.bmc.com/blogs/sre-vs-devops/)
- [dzone: SRE vs. DevOps: SRE Is to DevOps What Scrum Is to Agile](https://dzone.com/articles/sre-vs-devopssre-is-to-devops-what-scrum-is-to-agi)
- [linkedin: DevOps vs Site Reliability Engineering](https://www.linkedin.com/pulse/devops-vs-site-reliability-engineering-sean-washington/)
- [Google: What is Site Reliability Engineering (SRE)?](https://landing.google.com/sre/) SRE is what you get when you treat operations as if it’s a software problem. Our mission is to protect, provide for, and progress the software and systems behind all of Google’s public services — Google Search, Ads, Gmail, Android, YouTube, and App Engine, to name just a few — with an ever-watchful eye on their availability, latency, performance, and capacity.
- [opensource.com: What is an SRE and how does it relate to DevOps?](https://opensource.com/article/18/10/sre-startup) The SRE role is common in large enterprises, but smaller businesses need it, too.
- [thenewstack.io: Where Site Reliability Engineering Overlaps with DevOps](https://thenewstack.io/where-the-site-reliability-engineer-role-overlaps-with-devops/)
- [openshift.com: From Ops to SRE - Evolution of the OpenShift Dedicated Team](https://www.openshift.com/blog/from-ops-to-sre-evolution-of-the-openshift-dedicated-team)
- [cncf.io: DevOps vs. SRE](https://www.cncf.io/blog/2020/07/17/site-reliability-engineering-sre-101-with-devops-vs-sre/)
- [kelda.io: Why SREs Should be Responsible for Development Environments](https://kelda.io/blog/sres-should-manage-development-environments/)
- [youtube: Platform9’s Madhura Maskasky says observability is also essential for diagnosing and debugging in order for SREs to "get to the root cause quickly enough so that you can feed that back to the development teams." 🌟](https://www.youtube.com/watch?v=tgRPlAQpHYk&ab_channel=TheNewStack) Debugging remains complex. Debugging in "a world of microservices is a very difficult task," requiring the identification of which specific part in a microservices deployment must be fixed, says Platform9’s Madhura Maskasky.
    - "What's happening to the system administrator or is the system administrator becoming an SRE? Are they going into different roles? Are they taking multiple roles? How do they play a part in ensuring that reliability in these new roles?"
    - "The way Google defines SRE is that an SRE by nature needs to be someone who develops or writes code 50% of the time and only remaining 50% of the time they do the traditional ops/operations and this is because they want to do more through automation as part of the role of the requirements of the SRE himself, so that you can run apps that can serve billions of requests but that are still handled by a few dozens of SREs."
    - "Suddenly the role for SRE gets democratized and distributed among different roles (developers included)".
    - "Debugging remains complex. Debugging in "a world of microservices is a very difficult task", requiring the identification of which specific part in a microservices deployment must be fixed"
    - Observability is also essential for diagnosing and debugging in order for SREs to "get to the root cause quickly enough so that you can feed that back to the development teams."
- [linkedin.com: SRE: Key Insights-"Done the right way”](https://www.linkedin.com/pulse/sre-key-insights-done-right-way-shankar-muniyappa/)
- [hernan-david-hd.medium.com: 5 pilares del SRE/DevOps](https://hernan-david-hd.medium.com/5-pilares-del-sre-devops-f16e45f8d3fd)
- [hernan-david-hd.medium.com: Breaking down SRE/DevOps into 5 key areas](https://hernan-david-hd.medium.com/breaking-down-sre-devops-into-5-key-areas-5aacf40e8392)
- [devops.com: How the SRE Role Is Evolving](https://devops.com/how-the-sre-role-is-evolving/)
- [itprotoday.com: Why Site Reliability Engineering Is Key to Modern DevOps](https://www.itprotoday.com/testing-and-quality-assurance/why-site-reliability-engineering-key-modern-devops) Among the hottest areas of growth in DevOps is the emerging field of site reliability engineering as organizations look to bake reliability into the earliest stages of the software development cycle.
- [stackpulse.com: Managing Reliability for Monoliths vs. Microservices: The Challenges for SREs](https://stackpulse.com/blog/monoliths-vs-microservices-challenges/)
- [stackpulse.com: Managing Reliability for Monoliths vs. Microservices: Best Practices for SREs](https://stackpulse.com/blog/monoliths-vs-microservices-best-practices/)
- [cloud.google.com: SRE at Google: Our complete list of CRE life lessons 🌟](https://cloud.google.com/blog/products/devops-sre/sre-at-google-our-complete-list-of-cre-life-lessons)
- [circonus.com: Monitoring for Success: What All SREs Need to Know](https://www.circonus.com/2021/04/monitoring-for-success-what-all-sres-need-to-know/)
- [infracloud.io: Site Reliability Engineering (SRE) Best Practices](https://www.infracloud.io/blogs/sre-best-practices/)
- [stackpulse.com: No, SRE Is Not the New DevOps – Unless It Is](https://stackpulse.com/blog/no-sre-is-not-the-new-devops-unless-it-is/)
- [youtube: Viktor Farcic - What is the difference between SRE and DevOps?](https://www.youtube.com/watch?v=jgW4r9FxItI&ab_channel=DevOpsToolkitbyViktorFarcic)
- [dzone: Remote server management - Common architectural elements](https://dzone.com/articles/remote-server-management-common-architectural-elem)
- [dzone: Upcoming Trends in DevOps and SRE in 2021](https://dzone.com/articles/upcoming-trends-in-devops-and-sre) DevOps and SRE are domains with rapid growth and frequent innovations. With this blog you can explore the latest trends in DevOps, SRE and stay ahead of the curve.
- [dzone: SRE vs. DevOps: What are the Differences?](https://dzone.com/articles/sre-vs-devops-what-are-the-differences) SRE and DevOps are closely related concepts with some important distinctions between both, and many businesses can benefit from embracing both of them.

## SRE Tools
- [thenewstack.io: The Site Reliability Engineering Tool Stack](https://thenewstack.io/the-site-reliability-engineering-tool-stack/)
- [getcortexapp.com: A guide to the best SRE tools](https://www.getcortexapp.com/post/a-guide-to-the-best-sre-tools)
- [thenewstack.io: The Best Site Reliability Engineering Tools in 2021](https://thenewstack.io/the-best-site-reliability-engineering-tools-in-2021/)

## Service Level Objectives (SLO)
- [SLOconf](https://www.sloconf.com/) The first SLO Conference for Site Reliability Engineers
- [thenewstack.io: Automate User Satisfaction with This GitOps-Friendly Spec for Service Level Objectives](https://thenewstack.io/automate-user-satisfaction-with-this-gitops-friendly-spec-for-service-level-objectives/) Organizations looking to tighten up their ops with some site reliability engineering (SRE) should take a look at the recently-released OpenSLO specification, a GitOps-friendly template for establishing Service Level Objectives (SLO) to specify and even enforce the range of reliability required (and afforded) for a system.

### OpenSLO
- [OpenSLO specification 🌟](https://github.com/OpenSLO/OpenSLO) The goal of this project is to provide an open specification for defining and interfacing with SLOs to allow for a common approach, giving a set vendor-agnostic solution to defining and tracking SLOs. Platform specific implementation details are purposefully excluded from the scope of this specification.

<center>
[![cn do sre](images/CN-DO-SRE.png)](https://devops.com/sre-devops-cloud-native-server-cage-match/)

[![devops vs sre](images/devops_vs_sre.jpg)](https://devops.com/site-reliability-engineering-101-devops-versus-sre/)
</center>

## Videos
<details>
  <summary>Click to expand!</summary>

<center>
<iframe src="https://www.youtube.com/embed/tgRPlAQpHYk" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/jgW4r9FxItI" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
</details>

## Tweets
<details>
  <summary>Click to expand!</summary>

</center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Is it hard to find SREs? Dell: Developers do a good job as SREs because they know what exactly is happening. At the same time, we are also thinking about how we can have a developer rotation model too; essentially a rotation policy which is a learning process for us.</p>&mdash; The New Stack (@thenewstack) <a href="https://twitter.com/thenewstack/status/1390691219831934981?ref_src=twsrc%5Etfw">May 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
</details>  