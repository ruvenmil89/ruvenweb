pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Hello world'
        publishHTML(target: 'localhost:8082')
      }
    }

    stage('deploy') {
      steps {
        echo 'Deploy step '
      }
    }

  }
}