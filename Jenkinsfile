pipeline {
  agent any
  stages {
    stage("Install Helm"){
      steps {
       sh 'echo hello world'
       sh 'curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3'
       sh 'chmod 700 get_helm.sh'
       sh './get_helm.sh'
       sh 'helm list --all -A'
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