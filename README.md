# Network Device Admin (NDA) Automation Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python) ![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium) ![Pytest](https://img.shields.io/badge/Pytest-Testing-red?logo=pytest) ![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-yellow?logo=jenkins)

## 1. Project Title

🚀 Network Device Admin (NDA) - Selenium + Pytest Automation Framework

## 2. Project Overview

This repository contains an automation testing framework for a web-based Network Device Administration application. The project is designed to validate critical workflows such as login, device management, software configuration, software update, and configuration validation.

The framework is built using Python, Selenium WebDriver, and Pytest, following the Page Object Model (POM) design pattern for better maintainability, reusability, and scalability.

## 3. Features

✨ Key features of this framework include:
- UI automation for login and dashboard workflows
- Automated test coverage for device management operations
- Software configuration and software update validation
- Reusable page objects and helper modules
- Screenshot and report generation for failed test cases
- Pytest markers for smoke, regression, and sanity suites
- Structure ready for Jenkins CI/CD integration

## 4. Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| UI Automation | Selenium WebDriver |
| Test Framework | Pytest |
| Design Pattern | Page Object Model (POM) |
| Reporting | HTML / Allure-style reports |
| CI/CD | Jenkins |
| Version Control | Git / GitHub |

## 5. Framework Architecture

The project is organized into clear layers for easier maintenance:

- Tests: Contains end-to-end automated test cases
- Pages: Encapsulates page-specific locators and actions
- Helpers: Stores reusable constants and locator definitions
- Reports: Stores generated HTML and screenshot outputs
- Conftest: Provides shared fixtures and browser setup

This modular structure makes the framework suitable for both small-scale testing and enterprise-level automation projects.

## 6. Project Folder Structure

```text
NDA/
├── conftest.py
├── pages/
│   ├── login_page.py
│   ├── software_config_page.py
│   ├── software_update_page_device_paralell.py
│   └── validate_config_module.py
├── helpers/
│   ├── locaters.py
│   └── variables.py
├── tests/
│   ├── test_login_validation.py
│   ├── test_device_management_ssh_private.py
│   ├── test_software_config_page.py
│   ├── test_software_update_page_device_parlell.py
│   └── test_validate_config.py
├── reports/
├── defects/
├── Manual_testcases/
├── pytest.ini
└── README.md
```

## 7. Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/Kiran112p/NDA
cd nda
pip install selenium pytest pytest-html webdriver-manager
```

## 8. Prerequisites

Before running tests, make sure the following are available:

- Python 3.8 or above
- Google Chrome browser
- ChromeDriver or webdriver-manager support
- Internet access to the application under test
- Basic understanding of Pytest and Selenium

## 9. How to Run the Tests

Run the complete test suite:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_login_validation.py -v
```

## 10. Smoke Test Execution

Smoke tests are used for validating the most critical path flows:

```bash
pytest -m smoke -v
```

## 11. Regression Test Execution

Regression tests help ensure existing functionality remains stable:

```bash
pytest -m regression -v
```

## 12. Generate HTML Report

Generate an HTML report for test execution:

```bash
pytest --html=reports/report.html --self-contained-html
```

If Allure is installed, you can also generate a richer report:

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 13. API Automation

This project currently focuses on UI automation, but the structure is well-suited for future API automation using the Requests library. API testing can be added to validate backend endpoints, response codes, payloads, and data integrity.

## 14. UI Automation

UI automation is implemented with Selenium WebDriver using the Page Object Model.

Typical UI workflow covered in this repository:
- Open the application URL
- Login with valid credentials
- Access device management and configuration screens
- Perform actions such as add, update, or validate device settings
- Capture evidence and report results

## 15. Framework Highlights

💡 Why this framework stands out:
- Clean separation between test logic and UI locators
- Easy to extend with new test cases
- Reusable page objects reduce duplication
- Suitable for both manual-to-automation transition and scalable QA projects
- Supports structured reporting for better visibility

## 16. CI/CD using Jenkins

This framework can be integrated into Jenkins for continuous test execution.

Typical Jenkins workflow:
1. Pull the latest code from GitHub
2. Install dependencies
3. Run the Pytest suite
4. Publish test reports
5. Notify the team on failure or success

Example command used in CI:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## 17. Future Enhancements

🔮 Planned improvements:
- Add more device management and configuration test cases
- Introduce data-driven testing with Excel/CSV support
- Expand API automation coverage using Requests
- Add parallel test execution
- Improve reporting with dashboards and logs
- Support cross-browser execution

## 18. Contributing Guidelines

Contributions are welcome.

To contribute:
1. Fork the repository
2. Create a new feature branch
3. Add or update tests
4. Ensure the code remains clean and documented
5. Submit a pull request

## 19. License

This project is licensed under the MIT License.

## 20. Author

👤 Author: Palle Kiran

---

This framework demonstrates practical automation engineering skills in Selenium, Pytest, and test architecture, making it suitable for showcasing your work to recruiters and hiring managers.
