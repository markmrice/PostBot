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
                docker run -d --name postbot \
                -e EBAY_APP_ID="${EBAY_APP_ID}" \
                -e ROYALMAIL_API_KEY="${ROYALMAIL_API_KEY}" \
                postbot
                '''
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                sh 'docker exec postbot python fetch_ebay_orders.py'
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                sh 'docker exec postbot python generate_royal_mail_csv.py'
            }
        }

        stage('Upload CSV Simulation') {
            steps {
                sh 'docker exec postbot python upload_to_royal_mail.py'
            }
        }

        stage('Retrieve Tracking Simulation') {
            steps {
                sh 'docker exec postbot python get_tracking_numbers.py'
            }
        }

        stage('Update eBay Orders Simulation') {
            steps {
                sh 'docker exec postbot python update_ebay_orders.py'
            }
        }
    }

    post {
        always {
            steps {
                // Stop and remove the container after the pipeline
                sh '''
                docker stop postbot || true
                docker rm postbot || true
                '''
                echo 'Pipeline execution complete.'
            }
        }
    }
}
