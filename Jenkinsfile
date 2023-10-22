pipeline {
    agent any
    stages {
        stage('version') {            
            steps{ 
               sh 'python3 --version'
            }
        }    
        stage('Run Python Script') {
            steps {
                sh 'python3 pyalert.py'
            }
        }
    }
}

