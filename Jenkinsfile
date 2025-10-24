pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tariqueali17/flask-k8s-app"
        DOCKER_TAG = "v${BUILD_NUMBER}"
        KUBECONFIG_CRED = 'kubeconfig-cred'   // Jenkins credential ID for K8s config file
        DOCKERHUB_CRED = 'dockerhub-cred'     // Jenkins credential ID for DockerHub
        APP_NAME = "flask-app-deployment"
        NAMESPACE = "default"
    }

    options {
        ansiColor('xterm')
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 20, unit: 'MINUTES')
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                echo "📦 Checking out source code..."
                git branch: 'main', url: 'https://github.com/Tariqueali17/jenkins-cicd-flask-k8s.git'
            }
        }

        stage('Install Dependencies (Lint Check)') {
            steps {
                echo "🔍 Running basic syntax checks..."
                sh '''
                    pip install -r app/requirements.txt
                    python -m py_compile app/app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                    docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                echo "🚀 Pushing image to DockerHub..."
                withCredentials([usernamePassword(credentialsId: "$DOCKERHUB_CRED", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "☸️ Deploying updated image to Kubernetes..."
                withCredentials([file(credentialsId: "$KUBECONFIG_CRED", variable: 'KUBECONFIG_FILE')]) {
                    sh '''
                        export KUBECONFIG=$KUBECONFIG_FILE
                        kubectl set image deployment/$APP_NAME flask-app-container=$DOCKER_IMAGE:$DOCKER_TAG -n $NAMESPACE
                        kubectl rollout status deployment/$APP_NAME -n $NAMESPACE
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Build #${BUILD_NUMBER} deployed successfully!"
        }
        failure {
            echo "❌ FAILURE: Build #${BUILD_NUMBER} failed. Check logs for details."
        }
        always {
            cleanWs()
        }
    }
}
