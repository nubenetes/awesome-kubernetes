# AWS Messaging Services

1. [AWS SNS and SQS. Amazon Simple Notification Service and Amazon Simple Queue Service](#aws-sns-and-sqs-amazon-simple-notification-service-and-amazon-simple-queue-service)
    1. [SNS vs SQS](#sns-vs-sqs)
2. [AWS EventBridge](#aws-eventbridge)
3. [Tweets](#tweets)

## AWS SNS and SQS. Amazon Simple Notification Service and Amazon Simple Queue Service

- [dev.to: Getting started with SNS and SQS](https://dev.to/aws-builders/getting-started-with-sns-and-sqs-3m4i)
- [Limits in Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html)
- [Amazon SQS FAQs](https://aws.amazon.com/sqs/faqs/)
- The **Simple Notification Service**, or SNS for short, is one of the central services to build serverless architectures in the AWS cloud. SNS itself is a serverless messaging service that can distribute massive numbers of messages to different recipients. These include mobile end-user devices, like smartphones and tablets, but also other services inside the AWS ecosystem.
- SNS’ ability to target AWS services makes it the perfect companion for AWS Lambda. If you need custom logic, go for Lambda; if you need to fan out messages to multiple other services in parallel, SNS is the place to be.
- [dashbird.io: [Infographic] AWS SNS from a serverless perspective](https://dashbird.io/blog/aws-sns/)
- [enlear.academy: How To Build a Scalable Email Notification Service Using AWS](https://enlear.academy/how-to-build-a-scalable-email-service-using-aws-d404b347a7fb) Using AWS Lambda, DynamoDB, Amazon SQS, Amazon SES, and Amazon API Gateway to build a scalable email notification service.

### SNS vs SQS

- [==dev.to: When to SNS or SQS==](https://dev.to/aws-builders/when-to-sns-or-sqs-2aji)

## AWS EventBridge

- https://aws.amazon.com/eventbridge
- [==Building an event-driven application with Amazon EventBridge==](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/) **“In event-driven architecture, each component of the application raises an event whenever anything changes. Other components listen and decide what to do with it and how they would like to react.”** – by @talia_nassi
- [faun.pub: Implementing Event Driven Architecture With AWS EventBridge — Event-Driven Messaging Pattern](https://faun.pub/implementing-event-driven-architecture-with-aws-eventbridge-event-driven-messaging-pattern-9d29262bfade)

## Tweets

<details>
  <summary>Click to expand!</summary>

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A handy Decision Tree for choosing the right messaging service on AWS.<br><br>As per my calculations, following it gives you a 90% chance of making the right choice.<br><br>Read more in the thread 🧵👇 <a href="https://t.co/s7Q5uoENop">pic.twitter.com/s7Q5uoENop</a></p>&mdash; Maciej Radzikowski (@radzikowski_m) <a href="https://twitter.com/radzikowski_m/status/1513941279175942155?ref_src=twsrc%5Etfw">April 12, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">AWS SNS: a fully-managed messaging service 📨<br><br>A collection of the fundamentals to get you started 📚 <a href="https://t.co/6betCtkscC">pic.twitter.com/6betCtkscC</a></p>&mdash; Tobias Schmidt (@tpschmidt_) <a href="https://twitter.com/tpschmidt_/status/1537465068488740864?ref_src=twsrc%5Etfw">June 16, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>