pipeline {
    agent any
    stages 
    {
        stage('Install dependencies') {
            steps {
                sh "pip install countryinfo"
                sh 'ls'
            }
        }

        stage ('AWS_flashing_creatives_pipeline') {
            steps {
                //build job: 'AWS_flashing_creatives_pipeline'
                echo "haha"
            }
        }

        stage('End') {
            steps {
                sh 'ls'
            }
        }
    }
}