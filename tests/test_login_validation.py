import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ensure the NDA root directory is on sys.path so pages.login_page can be imported.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
#@pytest.mark.regression
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_validation_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    wait = WebDriverWait(driver, 10)

    actual_title = driver.title
    expected_title = "NETWORK_MANAGE — Dashboard"
    print(f"Actual Title: {actual_title}")

    if expected_title == actual_title:
        print("Login successful, title matches expected.")
    else:
        print("Login but dashboard title does not match expected.")