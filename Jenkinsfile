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

        stage('Run eBay Order Fetch Simulation') {
            steps {
                sh '''
                docker run \
                -e EBAY_APP_ID="${EBAY_APP_ID}" \
                -e ROYALMAIL_API_KEY="${ROYALMAIL_API_KEY}" \
                postbot
                '''
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                sh 'docker run postbot python generate_royal_mail_csv.py'
            }
        }

        stage('Upload CSV Simulation') {
            steps {
                sh 'docker run postbot python upload_to_royal_mail.py'
            }
        }

        stage('Retrieve Tracking Simulation') {
            steps {
                sh 'docker run postbot python get_tracking_numbers.py'
            }
        }

        stage('Update eBay Orders Simulation') {
            steps {
                sh 'docker run postbot python update_ebay_orders.py'
            }
        }
    }
}
