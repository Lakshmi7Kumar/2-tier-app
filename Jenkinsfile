pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/octocat/Hello-World.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Building project..."
                    ls -la

                    echo "Build Number: $BUILD_NUMBER" > build-info.txt
                    echo "Job Name: $JOB_NAME" >> build-info.txt

                    echo "Build completed."
                '''
            }
        }

    }

    post {
        success {
            archiveArtifacts artifacts: 'build-info.txt'
        }
    }
}
