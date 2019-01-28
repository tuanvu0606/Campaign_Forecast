pipeline {
    agent any
    stages 
    {
        stage('Start') {
            steps {
                sh 'ls'
            }
        }

        stage ('AWS_flashing_creatives_pipeline') {
            steps {
                build job: 'AWS_flashing_creatives_pipeline'
            }
        }

        stage('End') {
            steps {
                sh 'ls'
            }
        }
    }
}