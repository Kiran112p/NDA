import pytest
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Ensure project root is on sys.path so imports like `pages.login_page` work
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import the project's LoginPage to perform login in the fixture
from pages.login_page import LoginPage

def _get_chrome_service():
    try:
        # Prefer webdriver-manager if available to auto-download driver
        from webdriver_manager.chrome import ChromeDriverManager
        return Service(ChromeDriverManager().install())
    except Exception:
        # Fallback to chromedriver on PATH
        return Service()


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    # change or add options as needed
    options.add_argument("--disable-gpu")
    try:
        service = _get_chrome_service()
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        # Re-raise with a helpful message
        raise

    driver.maximize_window()
    driver.implicitly_wait(10)
    # Perform application login so tests start from an authenticated state
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login()
        # brief wait for post-login page to load
        time.sleep(2)
    except Exception:
        # If login fails, continue and let tests report the failure
        pass
    yield driver
    driver.quit()
