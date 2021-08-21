pipeline {
  agent any
  stages {
    stage("Build docker image"){
      steps {
        echo 'Build dokcer image for Ruven web!'
        }
      }
    stage("Deploy"){
      steps{
        echo " Deploy Ruven image over k8s GKE"
      }
    }
  }

}