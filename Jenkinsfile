pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key') // eBay API Key
        ROYALMAIL_API_KEY = credentials('royalmail-api-key') // Royal Mail API Key
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning repository...'
                }
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image for postbot...'
                }
                sh '''
                docker build -t postbot .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Starting the postbot container...'
                }
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                script {
                    echo 'Running eBay order fetch simulation...'
                }
                sh '''
                docker exec postbot_container python fetch_ebay_orders.py || echo "Simulation failed, but continuing."
                '''
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                script {
                    echo 'Generating Royal Mail CSV simulation...'
                }
                sh '''
                docker exec postbot_container python generate_royal_mail_csv.py || echo "Simulation failed, but continuing."
                '''
            }
        }

        stage('Check Logs') {
            steps {
                script {
                    echo 'Checking logs for postbot_container...'
                }
                sh '''
                docker logs postbot_container || echo "No logs available for postbot_container."
                '''
            }
        }
    }

    post {
        always {
            script {
                echo 'Cleaning up resources...'
            }
            sh '''
            docker stop postbot_container || true
            docker rm postbot_container || true
            '''
            echo 'Pipeline execution complete.'
        }
        failure {
            script {
                echo 'Pipeline failed! Check the logs and errors above.'
            }
        }
    }
}
