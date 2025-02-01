pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key') // Placeholder for now
        ROYALMAIL_API_KEY = credentials('royalmail-api-key') // Placeholder for now
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                git 'https://github.com/markmrice/PostBot.git'
                echo "Repository cloned successfully."
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t postbot . | tee build.log'
                echo "Docker image built successfully."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Starting PostBot container..."
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                -v $(pwd)/logs:/app/logs \  # Mount logs directory
                postbot
                '''
                echo "PostBot container started."
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                echo "Running eBay order fetch script..."
                sh 'docker exec postbot_container python fetch_ebay_orders.py 2>&1 | tee -a logs/fetch_orders.log'
                echo "eBay order fetch completed."
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                echo "Running Royal Mail CSV generator..."
                sh 'docker exec postbot_container python generate_royal_mail_csv.py 2>&1 | tee -a logs/royal_mail.log'
                echo "Royal Mail CSV generation completed."
            }
        }

        stage('Check Logs') {
            steps {
                echo "Retrieving logs..."
                sh 'docker logs postbot_container > logs/container_logs.log || echo "No logs available."'
                echo "Logs retrieved successfully."
            }
        }
    }

    post {
        always {
            echo "Cleaning up resources..."
            sh '''
            docker stop postbot_container || true
            docker rm postbot_container || true
            '''
            echo "Pipeline execution complete."
        }
    }
}
