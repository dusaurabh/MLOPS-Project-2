pipeline {
    agent any

    stages{
        stage("Cloning from Github....."){
            steps{
                script{
                    echo 'Cloning from Github......'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-project-2', url: 'https://github.com/dusaurabh/MLOPS-Project-2.git']])
                }
            }
        }
    }
}