# Scripts Inventory

* **cleanup.Jenkinsfile**: Jenkinsfile with Declarative Pipeline Multiline sh that cleanups old builds. All the Stages are now visually monitored. It is triggered every saturday night and ends with jenkins restart. These Multi-line bash commands make easier to read Jenkins Projects.
* **daily_restart.Jenkinsfile**: A script that automatically triggers a daily restart of Jenkins due to performance issues (Jenkins is a Java application). Jenkins with Declarative Pipeline multiline sh that restarts Jenkins every night except on Saturday nights (when Jenkinsfile is triggered). 

Grab them from here: [awesome-kubernetes/scripts](https://github.com/inafev/awesome-kubernetes/tree/master/scripts)

