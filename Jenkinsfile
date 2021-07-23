pipeline {
  agent any
  stages {
    stage('Log Versions') {
      parallel {
        stage('Log Versions') {
          steps {
            sh '''python --version 
python3 -m django --version'''
          }
        }

        stage('Unit Tests') {
          steps {
            sh '''cd tests
    python -m pip install -e ..
    python -m pip install -r requirements/py3.txt
    ./runtests.py'''
          }
        }

      }
    }

    stage('Email Test Results') {
      steps {
        emailext(subject: 'Unit Tests Complete', body: 'Unit Tests have completed', from: 'keith.amundson@wolterskluwer.com', to: 'keith.amundson@wolterskluwer.com')
      }
    }

  }
}