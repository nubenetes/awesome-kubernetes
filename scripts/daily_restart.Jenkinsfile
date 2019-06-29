#!/usr/bin/env groovy
// Description: Daily restart of jenkins with declarative pipeline
// A Declarative Pipeline is defined within a 'pipeline' block.
pipeline {
  agent { label 'master' } 
  triggers {
    // “At 05:00 on every day-of-week from Sunday through Friday.”
    // Not triggered on Saturday as Jenkinsfile is launched instead (cleanup pipeline script of the same repo that finishes with a restart)
    cron('0 3 * * 0-5')
  }
  stages {
    stage('Start') {
      steps {
        sh 'ls'
        sh 'date'
        sh 'pgrep -d, java | xargs ps -eo pcpu,pmem,pid,lstart,cmd | sort -r | grep -v while | head -2'
        sh 'uptime'
      }
    }
    stage('Clone Repository') {
      /* Let's make sure we have the repository cloned to our workspace */
      steps { 
        checkout scm
        dir('cleanup-script') {
          git credentialsId: 'Bitbucket_Access', url: "ssh://git@mybitbucketserver.com:999/cicd/cleanup-script.git"
        }
      }
    }

    stage('Restart Jenkins') {
      steps {
        sh '''
        #!/bin/bash  
        echo "===================================="
        echo "Automated daily restart of Jenkins: "  
        echo;
        JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
        if [ -e $JENKINS_HOME/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
        elif [ -e /usr/share/jenkins/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=/usr/share/jenkins/war/WEB-INF/jenkins-cli.jar
        fi

        #PREFIX is unique to each jenkins master server. It is obtained from the running process:
        PREFIX=\$(ps -efj | egrep java | awk -F"--prefix=" '{ print $2 }' | cut -d" " -f1)
        RESTART_TYPE=safe-restart
	      AUTH="-auth @$JENKINS_HOME/.jenkins-cli"
	      #AUTH="-i $JENKINS_HOME/.ssh/id_rsa"  
	      if [ $PREFIX == "/jenkins" ]; then 
          RESTART_TYPE=restart
        else
          RESTART_TYPE=safe-restart
        fi
        date;
        if [ -e $JENKINS_CLI -a -e $JENKINS_HOME/.jenkins-cli ]; then
          echo "Restarting jenkins with jenkins-cli $RESTART_TYPE";
          java -jar $JENKINS_CLI -s "http://localhost:8080$PREFIX/" $AUTH $RESTART_TYPE ; 
        else 
          ls -l $JENKINS_CLI;
          ls -l $JENKINS_HOME/.jenkins-cli;
          echo "jenkins-cli.jar or .jenkins-cli not found";
        fi
        date;
        '''
      }
    }

    stage('End') {
      steps {
        sh 'date'
        sh 'pgrep -d, java | xargs ps -eo pcpu,pmem,pid,lstart,cmd | sort -r | grep -v while | head -2'
        sh 'uptime'
      }
    }

  }
}






