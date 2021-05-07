pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                withAWS(credentials: '834c7752-4341-49d1-a00c-b5244f88e3ac	', region: 'ap-south-1') {
                cfnUpdate(stack:'mys3lambdastack', file:'Infrastructure.yaml')
                s3Upload(file:'pattern.py', bucket:'task1-input-bucket', path:'pattern.py')
                }
            }
        }
    }
}