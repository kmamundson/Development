pipeline {
  agent any
  stages {
    stage('Log Versions') {
      steps {
        sh '''python --version 
python3 -m django --version'''
      }
    }

  }
}