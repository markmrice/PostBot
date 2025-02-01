pipeline {
    agent any

    environment {
        EBAY_APP_ID = credentials('ebay-api-key')
        ROYALMAIL_API_KEY = credentials('royalmail-api-key')
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "📥 Cloning the repository..."
                git 'https://github.com/markmrice/PostBot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh 'docker build -t postbot .'
            }
        }

        stage('Check Existing Containers') {
            steps {
                echo "🔍 Checking for existing containers..."
                sh 'docker ps -a || echo "No existing containers found."'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "🚀 Starting the container..."
                sh '''
                docker run -d --name postbot_container \
                --env-file .env \
                postbot
                '''
                sleep 3  # Give the container time to start
                sh 'docker ps -a'
            }
        }

        stage('Run eBay Order Fetch Simulation') {
            steps {
                echo "📦 Running eBay order fetch..."
                sh '''
                docker exec postbot_container python fetch_ebay_orders.py \
                | tee -a postbot.log || echo "❌ Error running fetch_ebay_orders.py"
                '''
            }
        }

        stage('Generate Royal Mail CSV Simulation') {
            steps {
                echo "📄 Generating Royal Mail CSV..."
                sh '''
                docker exec postbot_container python generate_royal_mail_csv.py \
                | tee -a postbot.log || echo "❌ Error running generate_royal_mail_csv.py"
                '''
            }
        }

        stage('Check Logs') {
            steps {
                echo "📜 Retrieving container logs..."
                sh '''
                docker logs postbot_container | tee -a postbot.log || echo "⚠️ No logs available."
                '''
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up resources..."
            /*sh '''
            docker stop postbot_container || echo "⚠️ Container was not running."
            docker rm postbot_container || echo "⚠️ Container not found."
            '''*/
            echo "✅ Pipeline execution complete."
        }
    }
}
