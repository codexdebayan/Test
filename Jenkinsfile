pipeline {
    agent any
    environment {
        Docker_image = 'test-app'  // Replace with the actual image name (e.g., 'calculator-app')
        DOCKER_TAG = 'latest'
    }
    stages {
        stage('scm') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/master']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'GItHUb', url: 'https://github.com/sanjayDatagrokr/Test']]
                )
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build . -t sanjaymatta36/${Docker_image}:${DOCKER_TAG}'
            }
        }
        stage('Test') {
            steps {
                script {
                       sh '''
                    docker run --rm sanjaymatta36/test-app:latest python test_calculator.py 
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
                            echo $Docker_Hub | docker login -u sanjaymatta36 --password-stdin
                        '''
                    }
                    // Push the Docker image to Docker Hub
                    sh 'docker push sanjaymatta36/${Docker_image}'
                }
            }
        }
    }
}
