pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                withAWS(credentials: '834c7752-4341-49d1-a00c-b5244f88e3ac	', region: 'ap-south-1') {
                bat 'C:/Users/Rahul/AppData/Local/Programs/Python/Python37-32/python.exe C:/Users/Rahul/PycharmProjects/boto3demo/Ques_2/Executable.py'
                }
            }
        }
    }
}