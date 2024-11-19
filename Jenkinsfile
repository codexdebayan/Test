pipeline {
    agent any
    environment {
        Docker_image = 'app'  // Replace with the actual image name (e.g., 'calculator-app')
        DOCKER_TAG = 'latest'
    }
    stages {
        stage('scm') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/master']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'GItHUb', url: 'https://github.com/codexdebayan/Test']]
                )
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build . -t codexdebayan/${Docker_image}:${DOCKER_TAG}'
            }
        }
        stage('Test') {
            steps {
                script {
                       sh '''
                    docker run --rm codexdebayan/test:latest python test_calculator.py 
                    '''
                    }
                }
            }
        
        stage('Push to Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'Docker_HUb', variable: 'Docker_Hub')]) {
                        // Login to Docker Hub
                        sh '''
                            echo $Docker_Hub | docker login -u codexdebayan --password-stdin
                        '''
                    }
                    // Push the Docker image to Docker Hub
                    sh 'docker push codexdebayan/${Docker_image}'
                }
            }
        }
    }
}
