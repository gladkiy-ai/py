pipeline {
         agent any
  stage('Run') {
    steps {
        echo "Run docker image"
        script {
            pipelineContext.dockerContainer = pipelineContext.dockerImage.run()
        }
    }
  }
  post {
    always {
        echo "Stop Docker image"
        script {
            if (pipelineContext && pipelineContext.dockerContainer) {
                pipelineContext.dockerContainer.stop()
            }
        }
    }
  }

}