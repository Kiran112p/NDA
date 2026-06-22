import os
import sys
import pytest
import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ensure the NDA root directory is on sys.path so pages.login_page can be imported.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'NDA'))

from pages.software_config_page import SoftwareConfig

time.sleep(20)
class TestSoftwareConfig:
    def test_config_page(self, driver):
        self.driver = driver
        self.driver.save_screenshot(r"D:\NDA\reports\_after_config_job.png")
        # time.sleep(0.1)

