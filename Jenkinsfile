pipeline {
  agent any
  stages {
    stage("Build docker image"){
      steps {
        echo 'Build dokcer image for Ruven web!'
        sh 'ls'
        sh 'docker build . -t ruvenweb:latest'
        }
      }
    stage("Deploy"){
      steps{
        echo " Deploy Ruven image over k8s GKE"
      }
    }
  }

}