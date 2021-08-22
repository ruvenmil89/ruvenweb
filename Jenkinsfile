pipeline {
  agent any
  stages {
    stage("Install Helm"){
      steps {
       sh '''#!/bin/bash
           echo "hello world"
           wget https://get.helm.sh/helm-v3.6.3-linux-amd64.tar.gz
           tar -zxvf helm-v3.6.3-linux-amd64.tar.gz
           sudo mv linux-amd64/helm /usr/local/bin/helm
           helm list --all -A'''
      }
    }
    stage("Connect to GKE k8s") {
      steps {
        sh 'gcloud container clusters get-credentials ruvencluser --zone us-central1-c --project fast-nexus-323206'

      }
    }
    stage("Build docker image"){
      steps {
        echo 'Build dokcer image for Ruven web!'
        sh 'ls'
        sh 'docker login docker.io -u ruvenmil -p 1234ynck09'
        sh 'docker build . -t ruvenmil/ruvenweb:1.0'
        sh 'docker push ruvenmil/ruvenweb:1.0'
        }
      }
    stage("Deploy"){
      steps{
        echo " Deploy Ruven image over k8s GKE"
        sh 'kubectl get pods'
      }
    }
  }

}