pipeline {
  agent any
  stages {
    stage("Build docker image"){
      steps {
        echo 'Build dokcer image for Ruven web!'
          retry(3){
            sh 'docker build . -t ruven:latest'
          }
        }
      }
    stage("Deploy"){
      steps{
        echo " Deploy Ruven image over k8s GKE"
      }
    }
  }

}