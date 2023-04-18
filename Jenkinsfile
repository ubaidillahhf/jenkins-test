pipeline {
    agent any
    environment{
        DOCKERHUB_CREDS = credentials('Dockerhub')
    }
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
                sh 'ls *'
            }
        }
        stage('Build Image') {
            steps {
		         sh 'docker build -t ubedev/jenkinstest:$BUILD_NUMBER .'
            }
        }
        stage('Docker Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'                
            }
         }
        stage('Docker Push') {
            steps {  
                sh 'docker push ubedev/jenkinstest:$BUILD_NUMBER'
            }
         }
         stage('Triggering Step-Deployment') {
            steps {  
                build quietPeriod: 5, job: 'Step-Deployment'
            }
         }
   }
    post {
		always {
			sh 'docker logout'
		}
	 }
    }
