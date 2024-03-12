pipeline {
    agent any

    environment {
        registry = "883889909700.dkr.ecr.us-east-1.amazonaws.com/my-docker-repo"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/sagarkulkarni1989/docker-spring-boot']])
            }
        }
        
        stage ("Build JAR") {
            steps {
                sh "mvn clean install"
            }
        }
        
        stage ("Build Image") {
            steps {
                script {
                    dockerImage = docker.build registry
                    dockerImage.tag("$BUILD_NUMBER")

                }
            }
        }
        
        stage ("Push to ECR") {
            steps {
                script {
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 883889909700.dkr.ecr.us-east-1.amazonaws.com"
                    sh "docker push 883889909700.dkr.ecr.us-east-1.amazonaws.com/my-docker-repo:$BUILD_NUMBER"
                    
                }
            }
        }
        
        // stage ("Helm package") {
        //     steps {
        //             sh "helm package springboot"
        //         }
        //     }
                
        stage ('Helm Deploy') {
          steps {
            script {
                sh "helm upgrade first --install mychart --namespace helm-deployment --set image.tag=$BUILD_NUMBER"
                }
            }
        }
    }
}
