pipeline {
    agent any
    stages {
        stage('Docker Images before Build') {
            steps {
                sh 'docker images'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build https://github.com/gladkiy-ai/py.git#main --tag gitpy${BUILD_NUMBER}'
            }
        }
        stage('Run Docker Image') {
            steps {
                sh 'docker run --rm gitpy${BUILD_NUMBER}'
            }
        }
        stage('Docker Images after Build') {
            steps {
                sh 'docker images'
            }
        }
        stage('Remove Docker Image') {
            steps {
                sh 'docker rmi gitpy${BUILD_NUMBER}:latest'
            }
        }
        stage('Docker Images after Remove Build') {
            steps {
                sh 'docker images'
            }
        }
    }
}
