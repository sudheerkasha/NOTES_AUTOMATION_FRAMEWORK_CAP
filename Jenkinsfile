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

