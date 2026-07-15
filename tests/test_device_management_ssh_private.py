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


from pages.device_management_ssh_private import DeviceManagementPage
from helpers.locaters import *
from helpers.variables import *

@pytest.mark.regression
class TestDeviceManagement():
    def test_add_device(self, driver):
        device_page = DeviceManagementPage(driver)
        self.driver = driver
        
        # Navigate to device management and add a device using the page object
        print("\n=== Test: Navigate to Device Management ===")
        device_page.navigate_to_device_management()

        print("\n=== Test: Add Device ===")
        device_page.add_device()

        # Wait for the newly added device row to appear and verify values
        print("\n=== Test: Validate Device Added ===")
        device_page.validate_device_added()
        