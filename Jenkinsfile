pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker_image = docker.build("${env.DOCKER_IMAGE_TAG}", '-f ./Dockerfile .')
                }
            }
        }
        stage('Test') {
            parallel {
                stage('Unit tests') {
                    agent any
                    steps {
                        script {
                            docker_image.inside("--entrypoint='/start.sh'") {
                                sh 'cd /var/www/app && vendor/bin/phpunit --testsuite=Unittest'
                            }
                        }
                    }
                }
                stage('Health check') {
                    agent any
                    steps {
                        script {
                            docker_image.inside("--entrypoint='/start.sh'") {
                                timeout(time: 1, unit: 'MINUTES') {
                                    retry(5) {
                                        sleep 5
                                        sh "curl -sS http://localhost/info | grep 'My API'"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

