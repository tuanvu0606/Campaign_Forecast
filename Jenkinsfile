pipeline {
    agent any
    stages 
    {
        stage('Install dependencies') {
            steps {
                //sh "pip install countryinfo"
                sh 'ls'
            }
        }

        stage ('Query_country_population') {
            steps {
                //build job: 'AWS_flashing_creatives_pipeline'
                sh "python3 ${workspace}/get_country_information.py"
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