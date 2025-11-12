pipeline {
    agent any

    environment {
        IMAGE_NAME = "guessing-game:latest"
        APP_PORT = "5000"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning GitHub repository...'
                git url: 'https://github.com/upkar123-bit/sample-guessing-number-game.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    # Ensure Flask is installed even if requirements.txt is missing
                    if [ ! -f requirements.txt ]; then
                        echo "Flask==2.3.3" > requirements.txt
                    elif ! grep -q "^Flask" requirements.txt; then
                        echo "Flask==2.3.3" >> requirements.txt
                    fi

                    docker build -t guessing-game:latest .
                '''
            }
        }

      stage('Run Tests in Container') {
    steps {
        echo 'Running tests inside Docker container...'
        sh '''
            docker run --rm -e PYTHONPATH=/app guessing-game:latest  pytest
        '''
    }
}


        stage('Deploy Container') {
            steps {
                echo 'Deploying Docker container...'
                sh '''
                    # Stop existing container if running
                    if [ $(docker ps -q -f name=guessing-game:latest) ]; then
                        docker stop guessing-game
                        docker rm guessing-game
                    fi

                    # Run container
                    docker run -d -p 5000:5000 --name guessing-game guessing-game:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD pipeline finished successfully."
        }
        failure {
            echo "build/test/deployment failed. Check console logs!"
        }
    }
}
