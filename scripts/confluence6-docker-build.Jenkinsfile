#!/usr/bin/env groovy
// Description: pipeline script that builds docker images defined with dockerfiles 
// A Declarative Pipeline is defined within a 'pipeline' block.
pipeline {
  agent { 
    node { label 'docker' }
    }     
  environment {
    image_name = 'confluence6'
    openshift_url = 'https://<host_addr>'
    openshift_project = '<openshift-namespace>'
    openshift_credential = 'openshift-mp-dev'
    registry_url = 'https://docker-registry.<host_addr>:443'
    registry_host = 'docker-registry.<host_addr>:443'
    registry_credential = '<openshift-credential>'
    openshift_prod_url = 'https://<host_addr>'
    openshift_prod_project = '<openshift-namespace>'
    openshift_prod_credential = 'openshift-mp-dev'
    registry_prod_url = 'https://docker-registry.<host_addr>:443'
    registry_prod_host = 'docker-registry.<host_addr>:443'
    registry_prod_credential = 'openshift-mp-dev'
    //registry_host_dockerhub = 'registry.hub.docker.com'
    dockerhub_credential = 'dockerhub-credential'
    HTTP_PROXY = 'http://user:password@proxy.domain.net:80'
    HTTPS_PROXY = 'http://user:password@proxy.domain.net:80'
    NO_PROXY = 'localhost,127.0.0.1,.domain.net'
    }   
    parameters {
      choice(
          // choices are a string of newline separated values
          // https://issues.jenkins-ci.org/browse/JENKINS-41180
          choices: 'Openshift-DEV\nDockerhub\nOpenshift-PROD\nOpenshift-DEV-PROD\nALL',
          description: 'Choose between pushing the image to Openshift-DEV, Dockerhub or Openshift-PROD',
          name: 'REQUESTED_ACTION')
    }  
  stages {
    stage('Start') {
      steps {
        sh 'date'
      }
    }
    stage('Clone Repository') {
      /* Let's make sure we have the repository cloned to our workspace */
      steps { 
        checkout scm
        dir('confluence6_atlassian') {
          git credentialsId: 'Bitbucket_Access', url: "ssh://git@git.domain:port/~user/confluence6_atlassian.git"
        }
      }
    }
    stage ('Checking docker environment') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                hostname
                whoami
                id
                systemctl show --property=Environment docker # (/etc/systemd/system/docker.service.d/http-proxy.conf)
                cat /etc/sysconfig/docker
                #sudo cat /etc/docker/daemon.json   # disabled (password requested)
                systemctl status docker
                #sudo systemctl reload docker   # disabled (password requested)
                #sudo systemctl restart docker   # disabled (password requested)
                '''
        }
      }
    }
/*    stage ('Restart docker') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                #sudo systemctl daemon-reload
                #sudo systemctl restart docker
                '''
        }
      }
    }*/
    stage ('List local docker containers and images') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                docker ps -a
                docker images
            '''
        }  
      }
    }
    stage ('oc login Openshift-DEV - oc project <openshift-namespace>') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                oc login ${openshift_url} --username=${oc_user} --password=${oc_pw}
                oc project ${openshift_project}
                '''
        }
      }
    }
    stage ('Dockerhub login') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                # Dockerhub public registry login (https://hub.docker.com):
                docker login -u ${dockerhub_user} -p ${dockerhub_pw}
                '''
        }
      }
    }
    stage ('docker build (Dockerhub base image is pulled)') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                #docker build --add-host dl-cdn.alpinelinux.org:151.101.204.249 --add-host mirror1.hs-esslingen.de:129.143.116.10 -t ${openshift_project}/${image_name}:latest . 
                docker build -t ${openshift_project}/${image_name}:latest . 
                '''
        }
      }
    }
    stage ('docker images') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                docker images
                '''
        }
      }
    }
    /*
    stage ('Openshift-DEV Docker Registry Login Push Logout') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                #####################################################################################
                # Openshift Docker Registry:
                #docker login -u \$(oc whoami) -p \$(oc whoami -t) ${registry_url}
                #docker tag ${openshift_project}/${image_name} ${registry_host}/${openshift_project}/${image_name}
                #docker push ${registry_host}/${openshift_project}/${image_name}
                #docker images ${registry_url}
                #docker logout ${registry_url}
                #####################################################################################
                '''
        }
      }
    }*/
    stage ('oc logout') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                oc logout
                '''
        }
      }
    }
    stage ('Docker push to dockerhub private repo') {
      when {
            // Only push to Dockerhub when it is requested
            expression { params.REQUESTED_ACTION == 'Dockerhub' || params.REQUESTED_ACTION == 'ALL' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                docker tag ${openshift_project}/${image_name} ${dockerhub_user}/${image_name}   
                docker push ${dockerhub_user}/${image_name}   
                '''
        }
      }
    }
    stage ('Dockerhub public registry logout') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                docker logout  # dockerhub public registry logout
              '''
        }
      }
    }
    /*stage('Decide docker push to Openshift-DEV') {
      agent none
      steps {
        script {
          input 'Do you want to push the image to Openshift-Dev?'
        }
      }
    }*/
    stage('oc login + docker push to Openshift-DEV (dockerhub base image already pulled) + oc logout') {
        when {
            // Only push to Openshift-DEV when it is requested
            expression { params.REQUESTED_ACTION == 'Openshift-DEV' || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
        }
        steps {
            script {
                withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user')]) {
                    docker.withRegistry("${registry_url}", "${registry_credential}") {
                        //credentials-id defined in main jenkins for openshift test docker registry: openshift-mp-dev
                        sh "whoami"
                        sh "docker images"

                        sh "oc login ${openshift_url} --username=${oc_user} --password=${oc_pw}"
                        sh "docker login -u \$(oc whoami) -p \$(oc whoami -t) ${registry_url}"

                        // 1st option. We don't build the image, instead we just push the already built image:
                        def image = docker.image('${openshift_project}/${image_name}')
                        image.push("latest")

                        // 2nd option (without declarative pipeline):
                        //sh "docker tag ${openshift_project}/${image_name} ${registry_host}/${openshift_project}/${image_name}"
                        //sh "docker push ${registry_host}/${openshift_project}/${image_name}"

                        // 3rd option: We rebuild the image and push it afterwards:
                        /* Push the container to the custom Registry with declarative docker pipeline */
                        //docker.build("${openshift_project}/${image_name}:${env.BUILD_ID}").push('latest')
                    }
                }
            }
        }
    }
    stage ('Verify that the image stream was created in Openshift-DEV') {
      when {
          // Only push to Openshift-DEV when it is requested
          expression { params.REQUESTED_ACTION == 'Openshift-DEV' || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                #Verify that the image stream was created:
                oc get is -n ${openshift_project}
              '''
        }
      }
    }
    stage ('docker logout Openshift-DEV') {
      when {
          // Only push to Openshift-DEV when it is requested
          expression { params.REQUESTED_ACTION == 'Openshift-DEV'  || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                oc logout
                docker logout ${registry_url}
              '''
        }
      }
    }
    stage('oc login + docker push to Openshift-PROD (dockerhub base image already pulled) + oc logout') {
        when {
            // Only push to Openshift-DEV when it is requested
            expression { params.REQUESTED_ACTION == 'Openshift-PROD'  || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
        }
        steps {
            script {
                withCredentials([usernamePassword(credentialsId: "${openshift_prod_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user')]) {
                    docker.withRegistry("${registry_prod_url}", "${registry_prod_credential}") {
                        //credentials-id defined in main jenkins for openshift test docker registry: openshift-mp-dev
                        sh "whoami"
                        sh "docker images"

                        sh "oc login ${openshift_prod_url} --username=${oc_user} --password=${oc_pw}"
                        sh "docker login -u \$(oc whoami) -p \$(oc whoami -t) ${registry_prod_url}"

                        // 1st option. We don't build the image, instead we just push the already built image:
                        def image = docker.image('${openshift_prod_project}/${image_name}')
                        image.push("latest")

                        // 2nd option (without declarative pipeline):
                        //sh "docker tag ${openshift_project}/${image_name} ${registry_prod_host}/${openshift_project}/${image_name}"
                        //sh "docker push ${registry_prod_host}/${openshift_project}/${image_name}"

                        // 3rd option: We rebuild the image and push it afterwards:
                        /* Push the container to the custom Registry with declarative docker pipeline */
                        //docker.build("${openshift_project}/${image_name}:${env.BUILD_ID}").push('latest')
                    }
                }
            }
        }
    }
    stage ('Verify that the image stream was created in Openshift-PROD') {
      when {
          // Only push to Openshift-DEV when it is requested
          expression { params.REQUESTED_ACTION == 'Openshift-PROD' || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_prod_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                #Verify that the image stream was created:
                oc get is -n ${openshift_prod_project}
              '''
        }
      }
    }
    stage ('docker logout Openshift-PROD') {
      when {
          // Only push to Openshift-DEV when it is requested
          expression { params.REQUESTED_ACTION == 'Openshift-PROD' || params.REQUESTED_ACTION == 'Openshift-DEV-PROD' || params.REQUESTED_ACTION == 'ALL' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: "${openshift_prod_credential}", passwordVariable: 'oc_pw', usernameVariable: 'oc_user'),
                         usernamePassword(credentialsId: "${dockerhub_credential}", passwordVariable: 'dockerhub_pw', usernameVariable: 'dockerhub_user')]) {
            sh '''
                #!/bin/bash
                oc logout
                docker logout ${registry_prod_url}
              '''
        }
      }
    }
  }
}
