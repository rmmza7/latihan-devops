pipeline {
    agent any

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Mengambil kode terbaru dari GitHub...'
                checkout scm
            }
        }

        stage('2. Unit Testing') {
            steps {
                echo 'Menjalankan Unit Test Python...'
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('3. SonarQube Code Analysis') {
            steps {
                echo 'Memindai kualitas kode dengan SonarQube...'
                // Di server Jenkins asli, perintah ini memanggil SonarScanner
                sh 'sonar-scanner'
            }
        }

        stage('4. Quality Gate Check') {
            steps {
                echo 'Menunggu hasil Quality Gate...'
                // Menghentikan pipeline otomatis jika SonarQube statusnya FAILED
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline SUKSES! Kode siap dibungkus ke Docker.'
        }
        failure {
            echo 'Pipeline GAGAL! Periksa log error atau laporan SonarQube.'
        }
    }
}
