pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key')
        ROYALMAIL_API_KEY = credentials('royalmail-api-key')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t postbot .'
            }
        }

        stage('Start Container') {
            steps {
                sh '''
                docker run -d --name postbot_container \
                -e EBAY_APP_ID="${EBAY_APP_ID}" \
                -e ROYALMAIL_API_KEY="${ROYALMAIL_API_KEY}" \
                postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                sh 'docker exec postbot_container python fetch_ebay_orders.py'
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                sh 'docker exec postbot_container python generate_royal_mail_csv.py'
            }
        }

        stage('Upload CSV Simulation') {
            steps {
                sh 'docker exec postbot_container python upload_to_royal_mail.py'
            }
        }

        stage('Retrieve Tracking Simulation') {
            steps {
                sh 'docker exec postbot_container python get_tracking_numbers.py'
            }
        }

        stage('Update eBay Orders Simulation') {
            steps {
                sh 'docker exec postbot_container python update_ebay_orders.py'
            }
        }
    }

    post {
        always {
            steps {
                // Stop and remove the container after the pipeline
                sh '''
                docker stop postbot_container || true
                docker rm postbot_container || true
                '''
                echo 'Pipeline execution complete.'
            }
        }
    }
}
