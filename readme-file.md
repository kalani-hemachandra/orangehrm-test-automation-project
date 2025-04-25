# OrangeHRM Test Automation Framework

A comprehensive test automation framework for OrangeHRM built using Python, Selenium, and pytest following the Page Object Model design pattern.

## Project Overview

This framework automates testing of the OrangeHRM demo site, specifically focusing on:
- Login functionality
- Dashboard verification
- Leave page navigation and verification
- Logout functionality

## Project Structure

```
OrangeHRM-Test-Automation/
├── Config/
│   └── config.py
├── PageObjects/
│   ├── base_page.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   └── leave_page.py
├── TestCases/
│   ├── Reports/
│   ├── Screenshots/
│   ├── conftest.py
│   ├── test_title.py
│   ├── test_login.py
│   ├── test_leave.py
│   └── test_logout.py
├── Screenshots/
├── pytest.ini
└── requirements.txt
```

## Features

- **Page Object Model**: Separation of page specific code from test logic
- **Screenshots**: Automatic screenshot capture on test failures
- **HTML Reports**: Detailed test execution reports
- **Cross-browser Testing**: Framework supports multiple browsers (currently configured for Chrome)
- **Configuration Management**: Test data and configuration centralized

## Prerequisites

- Python 3.7+
- pip package manager

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/OrangeHRM-Test-Automation.git
   cd OrangeHRM-Test-Automation
   ```

2. Set up virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

Run all tests:
```
pytest -v
```

Run specific test file:
```
pytest TestCases/test_login.py -v
```

Generate HTML report:
```
pytest -v --html=Reports/report.html
```

## Configuration

Default test data is configured in the `Config/config.py` file. Update the values as needed:

```python
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
```

## Test Reports

- HTML reports are generated in the `Reports` directory
- Screenshots are captured automatically on test failures in the `Screenshots` directory

## Key Components

### Page Objects
- **login_page.py**: Login page actions and elements
- **dashboard_page.py**: Dashboard page actions and elements
- **leave_page.py**: Leave page actions and elements

### Test Cases
- **test_title.py**: Tests for verifying page titles
- **test_login.py**: Tests for login functionality
- **test_leave.py**: Tests for leave page functionality
- **test_logout.py**: Tests for logout functionality

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [pytest](https://docs.pytest.org/)
- [OrangeHRM](https://opensource-demo.orangehrmlive.com/)

