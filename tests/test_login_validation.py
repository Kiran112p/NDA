import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ensure the NDA root directory is on sys.path so pages.login_page can be imported.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




from pages.login_page import LoginPage


class TestLoginValidation:

    def test_validation_login(self):
        wait = WebDriverWait(driver, 2)
        wait.until(lambda d: d.title != "")  # wait until title loads
        actual_title = driver.title
        expected_title = "NETWORK_MANAGE — Dashboard"

        assert actual_title == expected_title, f"Expected {expected_title} but got {actual_title}"

        driver.quit()

if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    test_login_validation = TestLoginValidation(driver)
    test_login_validation.test_validation_login()
