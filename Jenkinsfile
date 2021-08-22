pipeline {
  agent any
  stages {
    stage("Connect to GKE k8s") {
      steps {
        sh 'gcloud container clusters get-credentials ruvencluser --zone us-central1-c --project fast-nexus-323206'

      }
    }
    stage("Install Helm"){
      steps {
       sh '''#!/bin/bash
           echo "hello world"
           helm list --all -A'''
      }
    }
    stage("Build docker image"){
      steps {
        echo 'Build dokcer image for Ruven web!'
        sh 'ls'
        //sh 'docker login docker.io -u ruvenmil -p 1234ynck09'
        //sh 'docker build . -t ruvenmil/ruvenweb:1.0'
        //sh 'docker push ruvenmil/ruvenweb:1.0'
        }
      }
    stage("Deploy"){
      steps{
        echo " Deploy Ruven image over k8s GKE"
        sh 'kubectl get pods'
        sh 'helm upgrade --install ruvenweb helmruvenweb'
      }
    }
  }

}