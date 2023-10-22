pipeline {
    agent {
        label 'python3.11'
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 pyalert.py'
            }
        }
    }
}
