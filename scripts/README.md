# Scripts Inventory

* **cleanup.Jenkinsfile**: Jenkinsfile with Declarative Pipeline Multiline sh that cleanups old builds. All the Stages are now visually monitored. It is triggered every saturday night and ends with jenkins restart. These Multi-line bash commands make easier to read Jenkins Projects.
* **daily_restart.Jenkinsfile**: A script that automatically triggers a daily restart of Jenkins due to performance issues (Jenkins is a Java application). Jenkins with Declarative Pipeline multiline sh that restarts Jenkins every night except on Saturday nights (when Jenkinsfile is triggered). 
* **confluence6-docker-build.Jenkinsfile**: Declarative Jenkinsfile for building and uploading a docker image to Openshift-DEV, Dockerhub and Openshift-PROD (Stages are disabled via Conditional Build Steps). Tip: A Docker Plugin for Jenkins can easily replace this Jenkinsfile. [This script can be found here](https://github.com/inafevwork/confluence6-atlassian).

## Configuration requirements 
This cleanup.Jenkinsfile script is supposed to be run in jenkins master nodes, where all the legacy build artifacts are achived ($JENKINS_HOME/jobs/YourProjectName/builds).  
### Jenkins-CLI Authentication 
Authentication is preferably with an -auth option, which takes a **username:apitoken** argument. Get your API token from **[jenkins_url]/me/configure**

The corresponding q-number's password can be used instead of the mentioned **"apitoken"**. The former one is LDAP based, while **apitoken is unique to each Jenkins Master node.**

Username and password credentials (or username and apitoken) need to be saved in each jenkins master server in **$JENKINS_HOME/.jenkins-cli** with the following format: **"username:password"** or **"username:apitoken"**.

The chosen username requires **Overall/Administer permission** in order to restart Jenkins. Otherwise you will obtain the following error:
```bash
ERROR: q-username is missing the Overall/Administer permission
```
### Setup a new Pipeline Job in Jenkins 
1. Jenkins job -> New Item -> "job name" Pipeline -> Pipeline SCM: git , Repository: "this repo", **Script Path: cleanup.Jenkinsfile**     
2. Jenkins job -> New Item -> "job name" Pipeline -> Pipeline SCM: git , Repository: "this repo", **Script Path: daily_restart.Jenkinsfile**     
3. Trigger a first manual build of the created job to load configuration from Jenkinsfile

## Technical details 
### Where Jenkins stores build files 
* **Jenkins Master nodes**: jenkins master nodes archive all the legacy build artifacts in **$JENKINS_HOME/jobs/YourProjectName/builds**.
* **Jenkins Slave nodes**: jenkins slaves keep the latest build in their corresponding Workspace in **/home/cloud/jenkins_slave/workspace/YourJobName**. 
### Jenkins reload-configuration after cleaning up old builds 
Once old build folders have been deleted, jenkins' index of builds needs to be updated by reloading its configuration (fast) or by restarting jenkins (slow). This **"reload-configuration"** of Jenkins **is finally not run in Jenkinsfile cleanup pipeline** as we are proceeding with an automated jenkins restart in its last stage. This restart needs to be done every night and it makes sense to be included in this cleanup job.  
### Jenkins restart VS safe-restart 
- [jenkins_url]/safeRestart. – This will restart Jenkins after the current builds have completed.
- [jenkins_url]/restart – This will force a restart. Builds will not wait to complete.

**daily_restart.Jenkinsfile** and **cleanup.Jenkinsfile** apply a hard **restart** of Jenkins Master when run in **Main Jenkins Master Enterprise**. A **safe-restart** was initially setup for all Jenkins Master nodes but it could easily last for 2-3 hours in Main Jenkins (sometimes requiring the Jenkins Admin to kill the remaining zombie jobs).

The current configuration is the following:
- **Main Jenkins Master: restart**
- Remaining Jenkins Master nodes: safeRestart

### Unusual characters in foldernames/filenames and IFS env var 
IFS env var is modified within this script in order to avoid errors when find command tries to navigate through a Project's folder with spaces in its name. By setting this up we make sure that all the existing folders related to Jenkins Projects are treated correctly and no errors arise when this script is run. 
### Summary of lines and parameters found in cleanup script 

Item | Parameter | Details
------------ | ------------ |-------------
IFS env var | IFS=$(echo -en "\n\b") | IFS lines discard any space and meta char in a folder's name
find command | -xdev | Don't descend directories on other filesystems
find command | -mtime n | File's data was last modified n*24 hours ago
find command | -delete | removes a file , not valid with directories
find command | -mindepth 1 -maxdepth 1 -type d | no recursive search for directories inside the current directory
find command | -print0 | ASCII NUL character to separate the entries in the file list that it produces (Unusual characters in filenames)
xargs command | -0 | assume that arguments are separated with ASCII NUL instead of white space
df command | cut -d" " -f2- | first column output is removed as device name is too long to be displayed
xargs command | -t | Used in cleanup-script.sh to show a list of old build folders to be deleted. Used in Jenkinsfile to get traces of deleted data. 

## Troubleshooting an OpenShift POD running Jenkins Master node 
This chapter is necessary to understand how to deal with a trouble Jenkins Enterprise POD (unresponsive and/or with more restarts than the ones triggered by this daily restart).

### Solutions to Known Errors Matrix Table
The below matrix table aims to help with solutions to well known incidents: 

Error | Solution or Workaround | 
------------ | ------------ | 
Jenkins Enterprise is unresponsive or extremely slow | Force a POD Restart by **A)** Scaling the POD to 0 and then to 1 from Openshift GUI, or by **B)** killing the Java Process of Jenkins: **kill 7**|
Restart of Jenkins Enterprise and its POD is taking too long > 1 hour | Deploy Jenkins Microservice: **A)** "oc rollout latest jenkins", or **B)** clicking on 'Deploy' button in Openshift GUI|

### Container State. Pod exitCode errors
- Exit codes seen when using oc get pods or kubectl get pods are unix shell exit codes (echo $?).
- Google "bash error code 137", "bash error code 143", etc.
- Signal 15 is a SIGTERM (see "kill -l" for a complete list). It's the way most programs are gracefully terminated, and is relatively normal
behaviour.This indicates system has delivered a SIGTERM to the processes. This is usually at the request of some other process (via kill()) but could also be sent by your process to itself (using raise()). This signal requests an orderly shutdown of process or system itself. **The real question is "Who/what is sending the SIGTERM?"**

Exit Code Number | Meaning | Example | Comments | 
------------ | ------------ | ------------ | ------------ |
128 +n | Fatal error signal "n"	| kill -n $PPID of script	| $? returns 128 + n|
137 (128 + 9) | Fatal error signal "9"	(SIGKILL) | kill -9 $PPID of script	| $? returns 137 (128 + 9)|
143 (128 + 15) | Fatal error signal "15" (SIGTERM)	| kill -15 $PPID of script	| $? returns 143 (128 + 15)|

#### List of SIGTERM signals
```bash
user@jumphost:~> kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
 5) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
 9) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
13) SIGPIPE     14) SIGALRM     15) SIGTERM     16) SIGSTKFLT
17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU
25) SIGXFSZ     26) SIGVTALRM   27) SIGPROF     28) SIGWINCH
29) SIGIO       30) SIGPWR      31) SIGSYS      34) SIGRTMIN
35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4
39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12
47) SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14
51) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10
55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7  58) SIGRTMAX-6
59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```
#### No errors arise after a new POD deployment
1. No errors are seen when Jenkins Microservice has been deployed again via OpenShift GUI (deploy button) or via "oc rollout latest jenkins_id". Deployment number will be increased by 1 (like deployment #20, or "revision number 20" in 'oc rollout history'). Restart Count is 0:
    ```
    Container jenkins
    State:
    Running since May 10, 2019 11:24:11 AM
    Ready:
    true
    Restart Count:
    0
    ```
#### Kubernetes/Openshift exit code 137
- Container with Out of Memory Kill. OutOfMemory error in Jenkins ("OOM" error code). Container/POD is using too much memory and is killed automatically (new restart triggered)
- Java Process killed manually with a "kill -9 [PID]" (as explained above)
#### Kubernetes/Openshift exit code 143
- When scaling down number of pods, the following error is reported in the OpenShift console, even though the pod is stopped correctly:
  ```
  The container spring-boot did not stop cleanly when terminated (exit code 143).
  ```
  Root Cause: This issue is related to the exit codes returned from the JVM when it receives signals such as SIGINT, SIGTERM, etc. The JVM default is to return an exit code of 128+signal-id. E.g for SIGTERM one would see an exit code of 143 (128+15). This causes Red Hat OpenShift Container Platform to display a warning message on pod scale down stating that that the container did not stop cleanly (when in actual fact, it did).
- This error also arises when Jenkins is restarted: 
  - A manual or automated restart of Jenkins also implies a new Container/POD restart.
  - Container **restartCount** is increased
  - A Jenkins Restart is triggered automatically by **Jenkinsfile-daily-restart** found in this repo (Jenkins cli).
  - A Jenkins Restart can also be accomplished from the Jenkins GUI: This is not available when Jenkins is overloaded and unresponsive.
  - **Simple workaround to force a Jenkins Restart:** In the following example we force a Container/POD restart by killing Jenkins Java process with a **"kill PID"** (SIGTERM signal, instead of SIGKILL signal with "kill -9"): 
    ```bash
      user@jumpserver:~/> oc get pods | grep ^jenkins-2
      jenkins-20-1d4vm                     1/1       Running   0          45m
      user@jumpserver:~/> oc rsh jenkins-20-1d4vm
      sh-4.2$ ps ux
      USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
      1019710+      1  0.0  0.0   4324   560 ?        Ss   11:24   0:00 /bin/tini -vv
      1019710+      7  109  0.5 61154992 5864592 ?    Sl   11:24  49:43 java -Djava.aw
      1019710+    938  0.0  0.0  13520  2076 ?        Ss+  11:27   0:00 /bin/sh
      1019710+   3037  0.0  0.0  13520  2000 ?        Ss+  11:31   0:00 /bin/sh
      1019710+   7723  0.0  0.0  13516  2064 ?        Ss+  11:44   0:00 /bin/sh
      1019710+  16464  2.0  0.0  13516  1936 ?        Ss   12:09   0:00 /bin/sh
      1019710+  16474  0.0  0.0  49060  1828 ?        R+   12:09   0:00 ps ux
      sh-4.2$ kill 7
    ```
### Openshift oc cli examples 
- oc get pods
- **oc get pods -o wide**
- oc describe pod jenkins-as-a-service-73-07xwx
- oc describe svc jaas-test
- **oc get svc**
- oc set env pods --all --list
- **ps -eo pid,lstart,cmd | fold -w 130**  (checking Jenkins Java process with arguments and start time)
  ```bash
  user@jumpserver:~> oc rsh jenkins-19-0n5jm
  sh-4.2$ ps -eo pid,lstart,cmd | fold -w 130
    PID                  STARTED CMD
      1 Sat Apr 28 00:54:42 2019 /usr/bin/dumb-init -- /usr/libexec/s2i/run
      7 Sat Apr 28 00:54:42 2019 java -XX:+UseParallelGC -XX:MinHeapFreeRatio=20 -XX:MaxHeapFreeRatio=40 -XX:GCTimeRatio=4 -XX:Adap
  tiveSizePolicyWeight=90 -XX:MaxMetaspaceSize=100m -Duser.home=/var/lib/jenkins -XX:MaxMetaspaceSize=512m -Djavamelody.application-
  name=JENKINS -Dfile.encoding=UTF8 -jar /usr/lib/jenkins/jenkins.war --prefix=/myjenkins
  45744 Sun Apr 29 15:12:43 2018 /bin/sh
  47707 Wed May  9 16:51:16 2018 /bin/sh
  54481 Wed May  9 18:20:04 2018 /bin/sh
  54656 Wed May  9 18:22:41 2018 ps -eo pid,lstart,cmd
  54657 Wed May  9 18:22:41 2018 fold -w 130
  ```
- oc get pod jenkins-19-0n5jm
- POD Status: **oc get pod jenkins-19-0n5jm -o yaml**
  - In the following example, LastState: 
    - startedAt  2019-05-02T05:40:30Z (05:40:30 UTC -> 07:40:30 CEST)
    - finishedAt 2019-05-03T04:38:08Z (04:38:08 UTC -> 06:38:08 CEST)
  - CurrentState startedAt: ...

  ```bash
    containerStatuses:
    - containerID: docker://9ad7f3a23d6328405090a380ed01305a9e21fefca91a49021db9b3848f208d09
      image: myip:5000/prod/jenkins
      imageID: docker-pullable://myip:5000/delivery-prod/jenkins@sha256:8f5d31f51cef106df8e68ed432e190f9f6bf0e9307d3f35490584cc4db808c0d
      lastState:
        terminated:
          containerID: docker://de0a32ddab499573fe7cd79745751b6eb2d1e3d84e4c0f529929985ed5c9947a
          exitCode: 137
          finishedAt: 2019-05-03T04:38:08Z
          reason: Error
          startedAt: 2019-05-02T05:40:30Z
      name: jenkins
      ready: true
      restartCount: 9
      state:
        ...
  ```
- **POD Status: oc get pod jenkins-20-1d4vm -o yaml**
  - **In the following example, LastState:** 
    - **startedAt:** 2019-05-14T03:01:40Z (3:01:40 UTC -> **5:01:40 CEST , daily restart**)
    - **finishedAt:** 2019-05-14T12:06:03Z (12:06:03 UTC -> **14:06:03 CEST**)
  - **CurrentState:**
    - **startedAt:** 2019-05-14T12:06:09Z (12:06:09 UTC -> **14:06:09 CEST**)

  ```bash
  containerStatuses:
  - containerID: docker://ed4e7b3c2e427d0f5e3940bafe21737173a00df3f09e6853f53b85a47e023c30
    image: myip:5000/delivery-prod/jenkins
    imageID: docker-pullable://myip:5000/delivery-prod/jenkins@sha256:8f5d31f51cef106df8e68ed432e190f9f6bf0e9307d3f35490584cc4db808c0d
    lastState:
      terminated:
        containerID: docker://92f7db3fbb442d1609abdad498051355266ef0072e97f226e2f9374932671044
        exitCode: 137
        finishedAt: 2019-05-14T12:06:03Z
        reason: Error
        startedAt: 2019-05-14T03:01:40Z
    name: jenkins
    ready: true
    restartCount: 5
    state:
      running:
        startedAt: 2019-05-14T12:06:09Z
  hostIP: myip
  phase: Running
  podIP: ip-addr
  startTime: 2019-05-10T09:24:04Z
  ```
- **oc get dc**
  ```bash
  user@jumphost:~/> oc get dc
  NAME                        REVISION   DESIRED   CURRENT   TRIGGERED BY
  cjoc                        11         1         1
  jenkins                     19         1         1
  jenkins-1                   27         0         0
  jenkins-2                   20         1         1
  jenkins-3                   1          0         0
  jenkins-4                   0          1         0
  jenkins-5                   9          1         1
  jenkins-6                   14         1         1
  jenkins-7                   9          1         1
  nexus                       7          1         1
  sonar6                      4          1         1
  sonar6-postgresql           1          1         1         config,image(postgresql:9.5)
  ```
- oc deploy --latest jenkins  (deprecated, use "oc rollout jenkins" instead)
  ```bash
  user@jumphost:~/> oc deploy --latest jenkins
  Flag --latest has been deprecated, use 'oc rollout latest' instead
  Started deployment #20
  Use 'oc logs -f dc/jenkins' to track its progress.
  user@jumphost:~/>
  ```
- **oc rollout latest jenkins**: This is like clicking on "deploy" button on Openshift GUI when we want to deploy a POD. **PROCEED WITH THIS IN CASE A RESTART OF JENKINS IS STUCK FOR MORE THAN 1 HOUR**. Deployment number will be increased by 1 (like deployment #20, or "revision number 20" in 'oc rollout history').
- **oc logs -f dc/jenkins**
- oc rollout history dc/jenkins
  ```bash
  user@jumphost:~/> oc rollout history dc/jenkins
  deploymentconfigs "jenkins"
  REVISION        STATUS          CAUSE
  1               Complete        manual change
  2               Complete        manual change
  4               Complete        manual change
  5               Complete        manual change
  6               Complete        manual change
  7               Complete        manual change
  8               Complete        manual change
  9               Failed          The deployment was cancelled by the user
  10              Complete        manual change
  11              Failed          manual change
  12              Failed          The deployment was cancelled by the user
  13              Failed          The deployment was cancelled by the user
  14              Failed          The deployment was cancelled by the user
  15              Failed          manual change
  16              Failed          The deployment was cancelled by the user
  17              Failed          manual change
  18              Failed          manual change
  19              Complete        manual change
  20              Running         manual change
  ```
- **Force the termination of POD:**
  ```bash
  $ oc delete pod jenkins-10-6095v --force=true --grace-period=0
  warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
  pod "jenkins-10-6095v" deleted
  ```
- **oc describe quota** 
- oc describe quota quota-48gi -n delivery-prod    ("oc describe quota" in default delivery-prod Project)
  ```bash
  user@jumphost:~/> oc describe quota 
  Name:           quota-48gi
  Namespace:      delivery-prod
  Resource        Used            Hard
  --------        ----            ----
  requests.cpu    22750m          30
  requests.memory 36467264Ki      48Gi
  ```
- oc status
- **oc status -v** (warnings can be seen)
- **oc get all**
- **oc logs -f po/jenkins-19-0n5jm | less -S**
- oc scale --replicas=0 dc jenkins   (Change the number of pods in a deployment)
- oc scale --replicas=3 dc jenkins   (Change the number of pods in a deployment)
- **oc rollout history po/jenkins-19-0n5jm**  (viewing a deployment)
- **oc rollout history dc/jenkins --revision=19**
- **oc get builds**
- oc edit: Edit a resource on the server
- oc new-build: Create a new build configuration
- oc start-build: Start a new build
- oc cancel-build: Cancel running, pending, or new builds
- oc import-image: Imports images from a Docker registry
- oc tag: Tag existing images into image streams
- **oc debug jenkins-52-167c9** (Launch a new instance of a pod for **debugging**)
- oc explain: Documentation of resources
- oc explain deploy  (Deployment enables declarative updates for Pods and ReplicaSets)
- oc exec: Execute a command in a container
- oc cp: Copy files and directories to and from containers.

### Openshift GUI examples 
- We can see the following output in OpenShift GUI after a jenkins restart (which implies a POD restart, with this POD's "restartCount" increased by 1):
  ```
  Status:
  Running Deployment:
  jenkins, #19
  IP:
  ipaddr.ip
  Node:
  nodeaddr.net (ipaddr)Restart Policy:
  Always
  Container jenkins
  State:
  Running since May 4, 2019 6:37:11 AM
  Last State
  Terminated at May 4, 2019 6:37:01 AM with exit code 143 (Error)
  Ready:
  false
  Restart Count:
  10
  Debug in Terminal
  ```

# Jenkins Slaves Cleanup Scripts
It can be easily automated via a jenkins job that triggers the following shell script:
  * ```bash
    mv /home/cloud/jenkins_slave/workspace /home/cloud/jenkins_slave/workspace.old && rm -Rf /home/cloud/jenkins_slave/workspace.old &
    mv /global/apps/cdbuilt/build_server/maven/<myproject>/local-repo-maven-3 /global/apps/cdbuilt/build_server/maven/<myproject>/local-repo-maven-3.old && rm -Rf /global/apps/cdbuilt/build_server/maven/<myproject>/local-repo-maven-3.old &
    ```
* Alternative: Workspace cleanup plugin: https://plugins.jenkins.io/ws-cleanup 

# References
* [Jenkins.io: **Jenkins CLI Authentication**](https://jenkins.io/doc/book/managing/cli/)
* [Stackoverflow: How to restart jenkins manually](https://stackoverflow.com/questions/8072700/how-to-restart-jenkins-manually) 
* [**Cloudbees Support Guideline: Cleanup and disk space management**](https://support.cloudbees.com/hc/en-us/articles/215549798-Deleting-Old-Builds-Best-Strategy-for-Cleanup-and-disk-space-management)
* [GNU.org: Deleting files with find](https://www.gnu.org/software/findutils/manual/html_node/find_html/Deleting-Files.html)
* [Dzone.com: **Declarative Pipeline Refcard**](https://dzone.com/refcardz/declarative-pipeline-with-jenkins)
* [Cloudbees: Declarative Pipeline Quick Reference](https://www.cloudbees.com/sites/default/files/declarative-pipeline-refcard.pdf)
* [Kubernetes Docs](https://kubernetes.io/docs/home)
* [Kubernetes.io: **Pod Lifecycle**](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
* [Openshift: Application memory sizing](https://docs.openshift.com/container-platform/3.9/dev_guide/application_memory_sizing.html)
* [**Openshift: Openshift Container Platform 3.9 CLI Reference**](https://docs.openshift.com/container-platform/3.9/cli_reference/index.html)
* [**Openshift: Basic CLI Operations - Object types**](https://docs.openshift.com/enterprise/3.2/cli_reference/basic_cli_operations.html#object-types)
* [**Youtube: Introduction to OpenShift Enterprise CLI**](https://www.youtube.com/watch?v=iRrAYnDSF4c)
* [**redhat.com Video: OpenShift Enterprise 3.2 - Creating your first application from the CLI**](https://access.redhat.com/videos/2481041/)
* [Openshift: Exit Code 137](https://blog.danman.eu/openshift-exit-code-137/)
* [**redhat.com: Openshift. Diagnosing an OOM Kill**](https://access.redhat.com/documentation/en-us/openshift_container_platform/3.9/html/developer_guide/dev-guide-application-memory-sizing#diagnosing-an-oom-kill)
* [redhat.com: Scaling down pods with a running Java process results in a warning message (exit code 143)](https://access.redhat.com/solutions/3100021)
* [redhat.com: Bash exit codes with special meanings](https://access.redhat.com/solutions/196563)
* [redhat.com: What is 'Signal 15' ?](https://access.redhat.com/solutions/737033)
* [redhat.com: How to find out who sent the 'signal-15'](https://access.redhat.com/solutions/360993)
* [Stackoverflow: How to debug container images using openshift](https://stackoverflow.com/questions/41771430/how-to-debug-container-images-using-openshift)
* [Stackoverflow: How to restart pod in OpenShift?](https://stackoverflow.com/questions/49562433/how-to-restart-pod-in-openshift)
* [Reddit.com: jenkinsci](https://www.reddit.com/r/jenkinsci/)

