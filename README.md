
## SonarQube Analysis

SonarQube is a code quality analysis platform that helps identify:
- Bugs
- Code smells
- Security vulnerabilities
- Code duplication
- Code coverage

### 1. Start SonarQube

Make sure Docker is installed and running.

```bash
docker run -d --name sonarqube \
  -p 9000:9000 \
  sonarqube:community
```

Open SonarQube in your browser:

http://localhost:9000

Default credentials for a fresh installation:
- Username: admin
- Password: admin

You will be asked to change the password.

### 2. Configure the project

Create a file named `sonar-project.properties` in the project root.

```properties
sonar.projectKey=credit-risk
sonar.projectName=Credit Risk Prediction
sonar.projectVersion=0.1.0

sonar.sources=src
sonar.tests=tests
sonar.sourceEncoding=UTF-8

sonar.python.coverage.reportPaths=coverage.xml
```

### 3. Generate the test coverage report

Install pytest-cov:

```bash
pip install pytest-cov
```

Execute:

```bash
pytest --cov=credit_risk --cov-report=xml:coverage.xml
```

This generates `coverage.xml`, containing information about which parts of the code are covered by tests.

### 4. Install SonarScanner

Install SonarScanner CLI using the official SonarQube documentation.

Make sure the `sonar-scanner` command is available in your terminal.

### 5. Run SonarQube analysis

Generate a project analysis token from the SonarQube interface.

Windows PowerShell:

```powershell
$env:SONAR_TOKEN="your_token"
sonar-scanner
```

Linux/macOS:

```bash
export SONAR_TOKEN="your_token"
sonar-scanner
```

### 6. Analyze the results

Open:

http://localhost:9000

Select the Credit Risk Prediction project.

Review the following indicators:
- Bugs
- Vulnerabilities
- Code Smells
- Code Coverage
- Duplicated Lines
- Maintainability

### 7. Compare code quality tools

| Tool | Main responsibility |
|---|---|
| Ruff | Static code analysis and linting |
| Black | Automatic code formatting |
| SonarQube | Overall code quality analysis |
| pytest | Unit testing |
| pytest-cov | Test coverage measurement |

**Conclusion:**

SonarQube complements Ruff and Black by providing a centralized view of code quality. It helps developers identify potential problems and monitor the maintainability of a software project.
