# UI Test Automation Framework

Automated UI testing framework for the Automation Exercise website using Python, Pytest and Playwright.

## Tech Stack

* Python 3.12
* Pytest
* Playwright
* Allure Report
* Page Object Model (POM)
* GitHub

## Project Structure

```text
.
├── data/
├── pages/
├── tests/
├── utils/
├── conftest.py
├── requirements.txt
└── README.md
```

### Pages

* Login Page
* Product Catalog Page
* Product Page
* Cart Page
* Header Component

## Test Coverage

### Login

* Valid login
* Invalid login
* Empty email validation
* Empty password validation
* Logout

### Product Catalog

* Open catalog page
* Product search
* Add product to cart

### Product Page

* Open product page
* Change product quantity
* Add product to cart

### Cart

* Open cart page
* Remove product from cart

### End-to-End

* Add product to cart and verify:

  * Product name
  * Product price

## Design Patterns

* Page Object Model
* Fixtures
* Reusable Components
* Test Data Separation

## Installation

Clone repository:

```bash
git clone https://github.com/KozakYan/KozakYan-ui-playwright-pytest-framework0.git
cd KozakYan-ui-playwright-pytest-framework0
```

Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Run Tests

Run all tests:

```bash
pytest
```

Run specific test file:

```bash
pytest tests/test_login.py
```

## Generate Allure Report

Run tests:

```bash
pytest --alluredir=allure-results
```

Generate report:

```bash
allure serve allure-results
```

## Author

Yan Kozak

Learning project created to practice UI test automation with Playwright and Pytest.

## Continuous Integration

GitHub Actions:
- Install dependencies
- Install Playwright browsers
- Run Pytest suite
- Store Allure results
