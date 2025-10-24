pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tariqueali17/flask-k8s-app"
        DOCKER_TAG = "v${BUILD_NUMBER}"
        KUBECONFIG_CRED = 'kubeconfig-cred'  // Jenkins credential ID for K8s
        DOCKERHUB_CRED = 'dockerhub-cred'    // Jenkins credential ID for DockerHub
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
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKERHUB_CRED", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: "$KUBECONFIG_CRED", variable: 'KUBECONFIG_FILE')]) {
                    script {
                        sh """
                        export KUBECONFIG=$KUBECONFIG_FILE
                        kubectl set image deployment/flask-app-deployment flask-app-container=$DOCKER_IMAGE:$DOCKER_TAG -n default
                        kubectl rollout status deployment/flask-app-deployment -n default
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Build: ${BUILD_NUMBER}"
        }
        failure {
            echo "❌ Deployment failed. Please check Jenkins logs."
        }
    }
}
