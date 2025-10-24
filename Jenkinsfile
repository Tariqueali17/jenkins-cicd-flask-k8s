pipeline {
    agent any

    environment {
        DOCKERHUB_CRED = credentials('dockerhub-login')
        IMAGE_NAME = "tariqueali1731/flask-cicd-app"
        KUBECONFIG_CRED = credentials('kubeconfig-cred')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-cred',
                    url: 'https://github.com/Tariqueali17/jenkins-cicd-flask-k8s.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME:${BUILD_NUMBER} -t $IMAGE_NAME:latest .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh '''
                        echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin
                        docker push $IMAGE_NAME:${BUILD_NUMBER}
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: 'kubeconfig-cred']) {
                    script {
                        sh '''
                            kubectl set image deployment/flask-app-deployment flask-app=$IMAGE_NAME:latest -n default || true
                            kubectl rollout status deployment/flask-app-deployment -n default || true
                        '''
                    }
                }
            }
        }

        stage('Post-Deployment Verification') {
            steps {
                script {
                    sh '''
                        echo "Verifying Deployment..."
                        kubectl get pods -n default
                        kubectl get svc -n default
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Version: ${BUILD_NUMBER}"
        }
        failure {
            echo "❌ Build or deployment failed. Check logs."
        }
    }
}
