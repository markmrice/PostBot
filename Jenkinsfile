pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key') // Placeholder for API credentials
        ROYALMAIL_API_KEY = credentials('royalmail-api-key')
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image for PostBot...'
                sh 'docker build -t postbot .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Starting PostBot container...'
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                postbot
                '''
            }
        }

        stage('Run Scripts and Generate Logs') {
            steps {
                echo 'Running scripts inside PostBot container and generating logs...'
                sh '''
                docker exec postbot_container python fetch_ebay_orders.py > fetch_ebay_orders.log 2>&1
                docker exec postbot_container python generate_royal_mail_csv.py > generate_csv.log 2>&1
                docker exec postbot_container python get_tracking.py > get_tracking.log 2>&1
                docker exec postbot_container python update_orders.py > update_orders.log 2>&1
                docker exec postbot_container python upload_csv.py > upload_csv.log 2>&1
                '''
            }
        }

        stage('Archive Logs') {
            steps {
                echo 'Archiving logs for all scripts...'
                sh '''
                docker cp postbot_container:/app/fetch_ebay_orders.log .
                docker cp postbot_container:/app/generate_csv.log .
                docker cp postbot_container:/app/get_tracking.log .
                docker cp postbot_container:/app/update_orders.log .
                docker cp postbot_container:/app/upload_csv.log .
                '''
                archiveArtifacts artifacts: '*.log', fingerprint: true
            }
        }
    }

    post {
        always {
            steps {
                echo 'Cleaning up resources...'
                sh '''
                docker stop postbot_container || true
                docker rm postbot_container || true
                '''
            }
        }
    }
}
