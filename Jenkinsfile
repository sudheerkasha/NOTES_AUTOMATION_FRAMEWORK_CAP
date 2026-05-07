// ============================================
// Jenkins CI/CD Pipeline
// UI + API Hybrid Automation Framework
// ============================================

pipeline {

    agent any

    parameters {

        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'edge'],
            description: 'Browser for UI tests'
        )

        choice(
            name: 'ENV',
            choices: ['dev', 'staging', 'production'],
            description: 'Target environment'
        )

        booleanParam(
            name: 'HEADLESS',
            defaultValue: true,
            description: 'Run in headless mode'
        )

        string(
            name: 'PARALLEL_WORKERS',
            defaultValue: '4',
            description: 'Number of parallel workers'
        )
    }

    environment {

        TEST_ENV = "${params.ENV}"
        BROWSER = "${params.BROWSER}"
        HEADLESS = "${params.HEADLESS}"
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {

        // ============================================
        // Clean Workspace
        // ============================================

        stage('Clean Workspace') {

            steps {

                cleanWs()

                echo "Workspace cleaned successfully"
            }
        }

        // ============================================
        // Checkout Source Code
        // ============================================

        stage('Checkout') {

            steps {

                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/sudheerkasha/NOTES_AUTOMATION_FRAMEWORK_CAP.git'
                    ]]
                ])

                echo "Code checked out successfully"
            }
        }

        // ============================================
        // Setup Python Environment
        // ============================================

        stage('Setup Environment') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate

                            python -m pip install --upgrade pip

                            pip install -r requirements.txt
                        '''

                    } else {

                        bat '''
                            python -m venv venv

                            call venv\\Scripts\\activate

                            python -m pip install --upgrade pip

                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        // ============================================
        // Debug Test Collection
        // ============================================

        stage('Debug Test Collection') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                            . venv/bin/activate

                            echo ===== CURRENT DIRECTORY =====
                            pwd

                            echo ===== TEST FILES =====
                            find tests

                            echo ===== PYTHON VERSION =====
                            python --version

                            echo ===== PYTEST VERSION =====
                            pytest --version

                            echo ===== COLLECTING TESTS =====
                            pytest --cache-clear --collect-only -v
                        '''

                    } else {

                        bat '''
                            call venv\\Scripts\\activate

                            echo ===== CURRENT DIRECTORY =====
                            cd

                            echo ===== TEST FILES =====
                            dir tests

                            echo ===== PYTHON VERSION =====
                            python --version

                            echo ===== PYTEST VERSION =====
                            pytest --version

                            echo ===== COLLECTING TESTS =====
                            pytest --cache-clear --collect-only -v
                        '''
                    }
                }
            }
        }

        // ============================================
        // API Health Check
        // ============================================

        stage('API Health Check') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                            . venv/bin/activate

                            python -c "import requests; r=requests.get('https://practice.expandtesting.com/notes/api/health-check'); print(f'API Status: {r.status_code}')"
                        '''

                    } else {

                        bat '''
                            call venv\\Scripts\\activate

                            python -c "import requests; r=requests.get('https://practice.expandtesting.com/notes/api/health-check'); print(f'API Status: {r.status_code}')"
                        '''
                    }
                }
            }
        }

        // ============================================
        // Run Complete Test Suite
        // ============================================

        stage('Run Tests') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                            . venv/bin/activate

                            rm -rf reports/allure-results

                            pytest \
                            -v \
                            -s \
                            tests \
                            --cache-clear \
                            --junitxml=reports/results.xml \
                            --alluredir=reports/allure-results \
                            --reruns=2 \
                            --reruns-delay=2
                        '''

                    } else {

                        bat '''
                            call venv\\Scripts\\activate

                            if exist reports\\allure-results (
                                rmdir /s /q reports\\allure-results
                            )

                            pytest ^
                            -v ^
                            -s ^
                            tests ^
                            --cache-clear ^
                            --junitxml=reports/results.xml ^
                            --alluredir=reports/allure-results ^
                            --reruns=2 ^
                            --reruns-delay=2
                        '''
                    }
                }
            }
        }

        // ============================================
        // Generate Allure Report
        // ============================================

        stage('Generate Allure Report') {

            steps {

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports/allure-results']]
                )
            }
        }
    }

    // ============================================
    // Post Actions
    // ============================================

    post {

        always {

            echo 'Archiving test artifacts...'

            archiveArtifacts(
                artifacts: 'reports/**/*',
                allowEmptyArchive: true
            )

            junit(
                testResults: 'reports/results.xml',
                allowEmptyResults: true
            )
        }

        success {

            echo 'All tests PASSED!'
        }

        failure {

            echo 'Some tests FAILED. Check Allure report.'
        }

        cleanup {

            cleanWs()
        }
    }
}
