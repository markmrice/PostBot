pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key') // Placeholder for now
        ROYALMAIL_API_KEY = credentials('royalmail-api-key') // Placeholder for now
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t postbot .' // Build the Docker image
            }
        }

        stage('Run Docker Container') {
            steps {
                // Explicitly name the container as "postbot_container"
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                // Execute the script inside the container
                sh 'docker exec postbot_container python fetch_ebay_orders.py'
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                sh 'docker exec postbot_container python generate_royal_mail_csv.py'
            }
        }

        stage('Check Logs') {
            steps {
                // Retrieve logs for the explicitly named container
                sh 'docker logs postbot_container || echo "No logs available for postbot_container."'
            }
        }
    }

    post {
        always {
            steps {
                // Stop and remove the container after pipeline completion
                sh '''
                docker stop postbot_container || true
                docker rm postbot_container || true
                '''
                echo 'Pipeline execution complete.'
            }
        }
    }
}
