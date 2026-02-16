# Playwright Python Automation Framework

![Build Status](https://github.com/nzr-22/Playwright-Python-Framework/actions/workflows/playwright.yml/badge.svg)

## 🚀 Overview
A modern, high-speed automation framework built with Playwright and Python. It features robust tracing, video recording, and parallel execution for the SauceDemo e-commerce application.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Automation Tool:** Playwright
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML & Allure
* **CI/CD:** GitHub Actions
* **Design Pattern:** Page Object Model (POM)

## 💡 Key Features
* **Auto-Wait:** Built-in waiting mechanism reduces flaky tests.
* **Trace Viewer:** captures full test execution traces (snapshots, console logs, network) for debugging.
* **Parallel Execution:** Runs tests simultaneously for faster feedback.
* **Headless Support:** optimized for CI/CD environments.

## ⚡ How to Run

### Prerequisites
* Python 3.8+ installed.

### Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nzr-22/Playwright-Python-Framework.git](https://github.com/nzr-22/Playwright-Python-Framework.git)

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install

### Execution Commands

1. **Run all tests:** 
   ```bash
   pytest
2. **Run with HTML Report:**
   ```bash
   pytest --html=report.html

3. **Run in Parallel (2 workers):**
   ```bash
   pytest -n 2

## 📊 Viewing Reports
To generate and view the Allure report:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results