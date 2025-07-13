pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage("Cloning from Github....."){
            steps{
                script{
                    echo 'Cloning from Github......'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-project-2', url: 'https://github.com/dusaurabh/MLOPS-Project-2.git']])
                }
            }
        }

        stage("Making a virtual enviornment....."){
            steps{
                script{
                    echo 'Making a virtual enviornment......'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc
                    '''
                }
            }
        }

        stage("DVC Pull"){
            steps{
                withCredentials([file(credentialsId:'gcp-key-project-2', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC Pull....'
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }
            }
        }

    }
}