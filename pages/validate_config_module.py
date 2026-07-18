import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ensure the NDA root directory is on sys.path so pages.login_page can be imported.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import time
from pages.login_page import LoginPage

from helpers.locaters import *
from helpers.variables import *


class ValidateConfigModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_validate_config(self):
        navigate_validate_config = self.wait.until(EC.element_to_be_clickable(validate_config))
        navigate_validate_config.click()
        time.sleep(0.5)

    def validate_hostname(self):
        device_dropdown = Select(self.driver.find_element(*device_config))
        device_dropdown.select_by_value(d_name)
        time.sleep(0.5)
    
    def host_name(self):
        host_name = self.wait.until(EC.visibility_of_element_located(expected_hostname))
        host_name.clear()
        host_name.send_keys(d_host)
        time.sleep(0.3)

    def run_validate(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        run_validate = self.wait.until(EC.element_to_be_clickable(run_validate_1))
        run_validate.click()
        time.sleep(0.5)

        print("host validation sucsusfully done")
    def validate_config_job_status(self):
        self.driver.save_screenshot(validate_config_screenshot_path)
        time.sleep(5)

    print("Screenshot of the validate config job status has been saved at:", validate_config_screenshot_path)
    
    def os_version(self):
        self.driver.execute_script("window.scrollTo(200, 600);")
        time.sleep(0.5)

        device_dropdown = Select(self.driver.find_element(*device_config_os))
        device_dropdown.select_by_value(d_name)
        time.sleep(0.5)

    def expected_os_version(self):
        os_version = self.wait.until(EC.visibility_of_element_located(device_os_version))
        os_version.clear()
        os_version.send_keys(d_version)
        time.sleep(0.5)

    def run_os_validate(self):
        run_btn = self.wait.until(EC.element_to_be_clickable(run_validate_2))
        run_btn.click()
        time.sleep(0.5)

    def validate_os_job_status(self):
        self.driver.execute_script("window.scrollTo(600, 800);")
        time.sleep(3)
        self.driver.save_screenshot(os_validation_screenshot_path)
        time.sleep(2)

        print("Screenshot of the validate os job status has been saved at:", os_validation_screenshot_path)

        print("host name and os version validation sucsusfully done")
    

