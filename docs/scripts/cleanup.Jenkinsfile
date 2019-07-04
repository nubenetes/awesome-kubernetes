#!/usr/bin/env groovy
// Description: Cleanup-script that removes old builds 
// A Declarative Pipeline is defined within a 'pipeline' block.
pipeline {
  agent { 
    node { label 'master' }
  } 
  triggers {
    // “At 05:00 on Saturday.”
    // Cleanup script that removes old builds. It ends with jenkins reload-configuration and jenkins restart
    cron('0 3 * * 6')
  }
  stages {
    stage('Start') {
      steps {
        sh 'date'
        sh 'df -hP | cut -d" " -f2- | column -t'
        sh 'pgrep -d, java | xargs ps -eo pcpu,pmem,pid,lstart,cmd | sort -r |  grep -v while | head -2'
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
    stage('File System Usage Before Cleanup') {
      steps {
        sh '''
            #!/bin/bash
            echo "1) Diplaying file system usage _before_ running this job:"
            echo;
            date;
            df -hP | cut -d" " -f2- | column -t;
            echo;echo;
        '''
      }
    }

    stage('Cleanup Old Build Folders') {
      steps {
        sh '''
            #!/bin/bash
            # IFS lines discard any space and meta char 
            SAVEIFS=IFS;
            IFS=$(echo -en "\n\b");

            echo "=================================================================================================";
            echo "2) REMOVING build folders last modified 30 days ago or more (please ignore empty 'rm -rf' lines):"
            echo;echo;
	          date;
            for u in $(find $JENKINS_HOME/jobs/ -xdev -not -empty -type d -name "builds");do find $u -xdev -mindepth 1 -maxdepth 1 -mtime +30 -type d -print0 | xargs -0 -t rm -rf; done;
            date;
            echo;echo;
            
	          #IFS lines discard any space and meta char
            IFS=$SAVEIFS
        '''
      }
    }

    stage('File System Usage') {
      steps {
        sh '''
            #!/bin/bash
            echo "=================================================================================";
            echo "4) Diplaying file system usage _before_ running cleanup workspace.tar.gz:";
            echo;echo;
            date;
            df -hP | cut -d" " -f2- | column -t;
            echo;echo;
            
        '''
      }
    }

    stage('Cleanup workspace.tar.gz') {
      steps {
        sh '''
            #!/bin/bash
            # IFS lines discard any space and meta char 
            SAVEIFS=IFS;
            IFS=$(echo -en "\n\b");

            echo "=================================================================================";
            echo "3) REMOVING workspace.tar.gz last modified 7 days ago or more:";
            echo;echo;
            date;
            find $JENKINS_HOME/jobs -type f -name "workspace.tar.gz" -mtime +7 -delete;
            date;
            
            #IFS lines discard any space and meta char
            IFS=$SAVEIFS;
        '''
      }
    }

    stage('File System Usage After Cleanup') {
      steps {
        sh '''
            #!/bin/bash
            echo "=================================================================================";
            echo "4) Displaying file system usage _after_ running this job:";
            echo;echo;
            date;
            df -hP | cut -d" " -f2- | column -t;
            echo;echo;
            
        '''
      }
    }
// This "reload-configuration" of Jenkins is not finally run in Jenkinsfile cleanup pipeline as we are proceeding with an 
// automated jenkins restart in its last stage. This restart needs to be done every night and it makes sense 
// to be included in this cleanup job.
/*    stage('Jenkins Reload Configuration') {
      steps {
        sh '''
          #!/bin/bash
          echo "=============================================================================="
          echo "5) Reload Jenkins Configuration (required to update jenkins links in builds folder):"
          echo;echo;
          JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
          if [ -e $JENKINS_HOME/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
          elif [ -e /usr/share/jenkins/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=/usr/share/jenkins/war/WEB-INF/jenkins-cli.jar
         fi

          #PREFIX is unique to each jenkins master server. It is obtained from the running process:
          PREFIX=\$(ps -efj | egrep java | awk -F"--prefix=" '{ print $2 }' | cut -d" " -f1)
          date
          if [ -e $JENKINS_CLI -a -e $JENKINS_HOME/.jenkins-cli ]; then
           echo "reloading jenkins config!"
           java -jar $JENKINS_CLI -s "http://localhost:8080$PREFIX" -auth @$JENKINS_HOME/.jenkins-cli reload-configuration
           date
          else 
           ls -l $JENKINS_CLI
           ls -l $JENKINS_HOME/.jenkins-cli
           echo "jenkins-cli.jar or .jenkins-cli not found"
          fi
	  echo;echo;
        '''
      }
    }*/

    stage('Daily Jenkins Restart (Saturday)') {
      steps {
        sh '''
          #!/bin/bash
          echo "=============================================================================="
          echo "6) Jenkins needs to be restarted automatically every night";
          echo;echo;
          JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
          if [ -e $JENKINS_HOME/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=$JENKINS_HOME/war/WEB-INF/jenkins-cli.jar
          elif [ -e /usr/share/jenkins/war/WEB-INF/jenkins-cli.jar ]; then
            JENKINS_CLI=/usr/share/jenkins/war/WEB-INF/jenkins-cli.jar
         fi

          #PREFIX is unique to each jenkins master server. It is obtained from the running process:
          PREFIX=\$(ps -efj | egrep java | awk -F"--prefix=" '{ print $2 }' | cut -d" " -f1)
          date
	        if [ $PREFIX == "/jenkins" ]; then 
            RESTART_TYPE=restart
	        else
	          RESTART_TYPE=safe-restart
	        fi
          date;
          if [ -e $JENKINS_CLI -a -e $JENKINS_HOME/.jenkins-cli ]; then
           echo "reloading jenkins config!";
           java -jar $JENKINS_CLI -s "http://localhost:8080$PREFIX" -auth @$JENKINS_HOME/.jenkins-cli $RESTART_TYPE ; 
           date;
          else 
           ls -l $JENKINS_CLI
           ls -l $JENKINS_HOME/.jenkins-cli
           echo "jenkins-cli.jar or .jenkins-cli not found"
          fi
	        date;
        '''
      }
    }

    stage('End') {
      steps {
        sh 'date'
        sh 'df -hP | cut -d" " -f2- | column -t'
        sh 'pgrep -d, java | xargs ps -eo pcpu,pmem,pid,lstart,cmd | sort -r |  grep -v while | head -2'
        sh 'uptime'
      }
    }
  }
}
