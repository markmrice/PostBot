pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key')
        ROYALMAIL_API_KEY = credentials('royalmail-api-key')
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t postbot .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Starting postbot container..."
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                echo "Fetching orders from eBay..."
                sh '''
                docker exec postbot_container python fetch_ebay_orders.py
                docker cp postbot_container:/app/orders.xml logs/orders.xml || echo "No orders.xml found."
                '''
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                echo "Generating Royal Mail CSV..."
                sh '''
                docker exec postbot_container python generate_royal_mail_csv.py
                docker cp postbot_container:/app/royal_mail_orders.csv logs/royal_mail_orders.csv || echo "No CSV file found."
                '''
            }
        }

        stage('Retrieve Tracking Numbers') {
            steps {
                echo "Retrieving tracking numbers..."
                sh '''
                docker exec postbot_container python get_tracking.py
                docker cp postbot_container:/app/logs/tracking.log logs/tracking.log || echo "No tracking log found."
                '''
            }
        }

        stage('Update eBay Orders with Tracking') {
            steps {
                echo "Updating eBay orders with tracking..."
                sh '''
                docker exec postbot_container python update_orders.py
                docker cp postbot_container:/app/logs/update_orders.log logs/update_orders.log || echo "No order update log found."
                '''
            }
        }

        stage('Upload CSV to Royal Mail FTP') {
            steps {
                echo "Uploading CSV file to Royal Mail FTP..."
                sh '''
                docker exec postbot_container python upload_csv.py
                docker cp postbot_container:/app/logs/ftp_upload.log logs/ftp_upload.log || echo "No FTP log found."
                '''
            }
        }

        stage('Check Logs') {
            steps {
                echo "Retrieving logs from the container..."
                sh '''
                docker logs postbot_container > logs/container_logs.txt || echo "No logs available for postbot_container."
                '''
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
            
            echo "Archiving logs..."
            archiveArtifacts artifacts: 'logs/**', fingerprint: true

            echo "Pipeline execution complete."
        }
    }
}
