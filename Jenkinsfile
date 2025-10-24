pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tariqueali1731/flask-app"
        DOCKER_TAG = "v${BUILD_NUMBER}"
        DOCKERHUB_CRED = "dockerhub-cred" // Jenkins credential ID
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Tariqueali17/jenkins-cicd-flask-k8s.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CRED}", usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    script {
                        sh """
                        echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                        """
                    }
                }
            }
        }

        stage('Deploy Container on EC2') {
            steps {
                script {
                    sh """
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app $DOCKER_IMAGE:$DOCKER_TAG
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! App running on port 5000"
        }
        failure {
            echo "❌ Build or deployment failed. Check Jenkins logs."
        }
    }
}
