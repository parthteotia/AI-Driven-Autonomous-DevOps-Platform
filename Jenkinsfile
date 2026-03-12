pipeline {
agent any
environment {
AWS_DEFAULT_REGION = 'ap-south-1'
}
stages {
stage('Checkout') {
steps {
git branch: 'main',
credentialsId: 'github-creds',
url: 'https://github.com/parthteotia/AI-Driven-Autonomous-DevOps-Platform'
}
}
stage('Telemetry Setup') {
steps {
echo 'Validating AWS CloudWatch Log Groups...'
sh 'aws logs describe-log-groups --log-group-name-prefix /aws/devops/autonomous-app'
}
}
stage('Deploy & Monitor') {
steps {
echo 'Deploying Application...'
sh 'python3 app-code/monitor_app.py'
}
}
}
}