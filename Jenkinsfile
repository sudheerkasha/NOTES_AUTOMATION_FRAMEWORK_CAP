// // ============================================
// // Jenkins CI/CD Pipeline
// // UI + API Automation Framework
// // ============================================

// pipeline {

//     agent any

//     parameters {

//         choice(
//             name: 'BROWSER',
//             choices: ['chrome', 'firefox', 'edge'],
//             description: 'Browser for UI tests'
//         )

//         booleanParam(
//             name: 'HEADLESS',
//             defaultValue: true,
//             description: 'Run tests in headless mode'
//         )
//     }

//     environment {

//         PYTHONPATH = "${WORKSPACE}"
//         BROWSER = "${params.BROWSER}"
//         HEADLESS = "${params.HEADLESS}"
//     }

//     stages {

//         // ============================================
//         // Clean Workspace
//         // ============================================

//         stage('Clean Workspace') {

//             steps {

//                 cleanWs()

//                 echo "Workspace cleaned successfully"
//             }
//         }

//         // ============================================
//         // Checkout Source Code
//         // ============================================

//         stage('Checkout Code') {

//             steps {

//                 git(
//                     branch: 'main',
//                     url: 'https://github.com/sudheerkasha/NOTES_AUTOMATION_FRAMEWORK_CAP.git'
//                 )

//                 echo "GitHub repository cloned successfully"
//             }
//         }

//         // ============================================
//         // Setup Python Environment
//         // ============================================

//         stage('Setup Environment') {

//             steps {

//                 bat '''
//                 python -m venv venv

//                 call venv\\Scripts\\activate

//                 python -m pip install --upgrade pip

//                 pip install -r requirements.txt
//                 '''

//                 echo "Python environment setup completed"
//             }
//         }

//         // ============================================
//         // Debug Test Collection
//         // ============================================

//         stage('Collect Test Cases') {

//             steps {

//                 bat '''
//                 call venv\\Scripts\\activate

//                 echo ===== CURRENT DIRECTORY =====
//                 cd

//                 echo ===== TEST FILES =====
//                 dir /s tests

//                 echo ===== PYTHON VERSION =====
//                 python --version

//                 echo ===== PYTEST VERSION =====
//                 pytest --version

//                 echo ===== COLLECTING TESTS =====
//                 pytest --cache-clear --collect-only -vv
//                 '''
//             }
//         }

//         // ============================================
//         // Run Test Suite
//         // ============================================

//         stage('Run Tests') {

//             steps {

//                 bat '''
//                 call venv\\Scripts\\activate

//                 if exist reports\\allure-results (
//                     rmdir /s /q reports\\allure-results
//                 )

//                 if not exist reports (
//                     mkdir reports
//                 )

//                 pytest ^
//                 tests ^
//                 -v ^
//                 -s ^
//                 --cache-clear ^
//                 --junitxml=reports/results.xml ^
//                 --alluredir=reports/allure-results ^
//                 --reruns 2 ^
//                 --reruns-delay 2
//                 '''
//             }
//         }

//         // ============================================
//         // Generate Allure Report
//         // ============================================

//         stage('Generate Allure Report') {

//             steps {

//                 allure(
//                     includeProperties: false,
//                     jdk: '',
//                     results: [[path: 'reports/allure-results']]
//                 )

//                 echo "Allure report generated successfully"
//             }
//         }
//     }

//     // ============================================
//     // Post Build Actions
//     // ============================================

//     post {

//         always {

//             archiveArtifacts(
//                 artifacts: 'reports/**/*',
//                 allowEmptyArchive: true
//             )

//             junit(
//                 testResults: 'reports/results.xml',
//                 allowEmptyResults: true
//             )

//             echo "Reports archived successfully"
//         }

//         success {

//             echo "Pipeline executed successfully"
//         }

//         failure {

//             echo "Pipeline execution failed"
//         }

//         cleanup {

//             cleanWs()
//         }
//     }
// }


pipeline {

```
agent any

parameters {

    choice(
        name: 'BROWSER',
        choices: ['chrome', 'firefox', 'edge'],
        description: 'Browser for UI tests'
    )

    booleanParam(
        name: 'HEADLESS',
        defaultValue: true,
        description: 'Run tests in headless mode'
    )
}

environment {
    PYTHONPATH = "${WORKSPACE}"
    BROWSER = "${params.BROWSER}"
    HEADLESS = "${params.HEADLESS}"
}

stages {

    stage('Clean Workspace') {
        steps {
            cleanWs()
            echo "Workspace cleaned successfully"
        }
    }

    stage('Checkout Code') {
        steps {
            git(
                branch: 'main',
                url: 'https://github.com/sudheerkasha/NOTES_AUTOMATION_FRAMEWORK_CAP.git'
            )
            echo "GitHub repository cloned successfully"
        }
    }

    stage('Setup Environment') {
        steps {
            sh '''
                python3 -m venv venv

                . venv/bin/activate

                python -m pip install --upgrade pip

                pip install -r requirements.txt
            '''

            echo "Python environment setup completed"
        }
    }

    stage('Collect Test Cases') {
        steps {
            sh '''
                . venv/bin/activate

                echo "===== CURRENT DIRECTORY ====="
                pwd

                echo "===== TEST FILES ====="
                find tests -type f

                echo "===== PYTHON VERSION ====="
                python --version

                echo "===== PYTEST VERSION ====="
                pytest --version

                echo "===== COLLECTING TESTS ====="
                pytest --cache-clear --collect-only -vv
            '''
        }
    }

    stage('Run Tests') {
        steps {
            sh '''
                . venv/bin/activate

                rm -rf reports/allure-results

                mkdir -p reports

                pytest tests \
                -v \
                -s \
                --cache-clear \
                --junitxml=reports/results.xml \
                --alluredir=reports/allure-results \
                --reruns 2 \
                --reruns-delay 2
            '''
        }
    }

    stage('Generate Allure Report') {
        steps {
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports/allure-results']]
            )

            echo "Allure report generated successfully"
        }
    }
}

post {

    always {

        archiveArtifacts(
            artifacts: 'reports/**/*',
            allowEmptyArchive: true
        )

        junit(
            testResults: 'reports/results.xml',
            allowEmptyResults: true
        )

        echo "Reports archived successfully"
    }

    success {
        echo "Pipeline executed successfully"
    }

    failure {
        echo "Pipeline execution failed"
    }

    cleanup {
        cleanWs()
    }
}
```

}

