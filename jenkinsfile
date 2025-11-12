pipeline{
    agent any 
      environment {
        VENV = "venv"
    }
    stages{
        stage('cloning')
        {
          steps {
            echo ' Cloning the GitHub repository'
            git url: 'https://github.com/upkar123-bit/sample-guessing-number-game.git', branch: 'main'
            
        }
        }
        stage('Build Application') {
    steps {
        echo '⚙️ Building the Python application...'
        sh '''#!/bin/bash
        python3 -m venv venv
        source venv/bin/activate
        if [ -f requirements.txt ]; then
            pip install -r requirements.txt
        else
            echo "No requirements.txt found — skipping dependency install."
        fi
        '''
    }
}

stage('Run Tests') {
    steps {
        echo 'Running test cases'
        sh '''#!/bin/bash
        source venv/bin/activate
        python3 -m unittest discover -s tests -p "*.py" || true
        '''
    }
}

    }
     post {
        success {
            echo 'pipeline executed successfully!'
        }
        failure {
            echo 'build or test failed. Check console logs for details.'
        }
        always {
            echo 'CI/CD pipeline completed.'
        }
    }
}
