pipeline {
  agent any
  stages {
     stage('Pull image') {
        steps {
           catchError {
              script {
      	    docker.image('python:3.8')
      	      }
           }
        }
     }
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("python-for-test", ".")
      	     }
          }
       }
    }
     stage('Run image') {
        steps {
           catchError {
              script {
              	docker.image('python-for-test').run("python3 main.py")
		}              
      	    }
         }
     }
  }
}
