pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-login') // Jenkins Credential ID
        DOCKER_IMAGE = 'tariqueali1731/flask-cicd-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Checking out the source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📂 Installing dependencies...'
                sh '''
                cd app
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh '''
                docker build -t $DOCKER_IMAGE:$BUILD_NUMBER -t $DOCKER_IMAGE:latest .
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '🚀 Pushing image to DockerHub...'
                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push $DOCKER_IMAGE:$BUILD_NUMBER
                docker push $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '☸️ Deploying to Kubernetes cluster...'
                sh '''
                kubectl set image deployment/python-deployment-nautilus python-container-nautilus=$DOCKER_IMAGE:latest || echo "⚠️ Deployment not found. Skipping..."
                kubectl rollout status deployment/python-deployment-nautilus || true
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs for details.'
        }
    }
}
