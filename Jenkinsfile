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

        /* .. snip .. */
        stage('run-parallel-Jobs') {
          steps {
            parallel(
              a: {
                build job: 'Parallel_Job_1'
              },
              b: {
                build job: 'Parallel_Job_2'
              }
            )
          }
        }

        stage ('AWS_flashing_creatives_pipeline') {
            steps {
                build job: 'AWS_flashing_creatives_pipeline'                
            }
        }

        stage ('Query_country_population') {
            steps {                
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