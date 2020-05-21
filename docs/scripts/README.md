# Scripts Inventory

* **cleanup.Jenkinsfile**: Jenkinsfile with Declarative Pipeline Multiline sh that cleanups old builds. All the Stages are now visually monitored. It is triggered every saturday night and ends with jenkins restart. These Multi-line bash commands make easier to read Jenkins Projects.
* **daily_restart.Jenkinsfile**: A script that automatically triggers a daily restart of Jenkins due to performance issues (Jenkins is a Java application). Jenkins with Declarative Pipeline multiline sh that restarts Jenkins every night except on Saturday nights (when cleanup.Jenkinsfile is triggered). 
* **confluence6-docker-build.Jenkinsfile**: Declarative Jenkinsfile for building and uploading a docker image to Openshift-DEV, Dockerhub and Openshift-PROD (Stages are disabled via Conditional Build Steps). Tip: A Docker Plugin for Jenkins can easily replace this Jenkinsfile. 

Grab them from here: [awesome-kubernetes/scripts](https://github.com/inafev/awesome-kubernetes/tree/master/scripts)

## Jenkins Configuration as Code on Kubernetes
* [Jenkins Configuration as Code on Kubernetes 🌟](https://github.com/inafev/jenkins-CasC-kubernetes-demo) A Codecentric/Jenkins Helm 3 Sample Chart on Digital Ocean Kubernetes with Spring Petclinic Demo Pipeline

