pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key') // Ensure this exists in Jenkins
        ROYALMAIL_API_KEY = credentials('royalmail-api-key') // Ensure this exists in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                script { echo 'Cloning repository...' }
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script { echo 'Building Docker image...' }
                sh 'docker build -t postbot .'
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Checking for existing container and removing if necessary...'
                }
                sh '''
                docker stop postbot_container || true
                docker rm postbot_container || true
                echo "Starting the new postbot container..."
                docker run -d --name postbot_container --env-file .env postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                script { echo 'Running eBay order fetch simulation...' }
                sh 'docker exec postbot_container python fetch_ebay_orders.py || echo "Simulation failed, but continuing."'
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                script { echo 'Generating Royal Mail CSV simulation...' }
                sh 'docker exec postbot_container python generate_royal_mail_csv.py || echo "Simulation failed, but continuing."'
            }
        }

        stage('Check Logs') {
            steps {
                script { echo 'Checking logs for postbot_container...' }
                sh 'docker logs postbot_container || echo "No logs available."'
            }
        }
    }

    post {
        always {
            node { // Wrap cleanup in a node block to avoid the MissingContextVariableException
                script {
                    echo 'Cleaning up resources...'
                }
                sh '''
                docker stop postbot_container || true
                docker rm postbot_container || true
                '''
                echo 'Pipeline execution complete.'
            }
        }
    }
}
