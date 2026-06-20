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



class TestDeviceManagement():
    def test_add_device(self, driver):
        device_page = DeviceManagementPage(driver)
        self.driver = driver

        # Navigate to device management and add a device using the page object
        device_page.navigate_to_device_management()
        device_page.add_device()

        # Wait for the newly added device row to appear and verify values
        wait = WebDriverWait(driver, 10)
        name_el = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='ROUTER_NCS_540']")))
        assert name_el.text == "ROUTER_NCS_540"

        ip_el = driver.find_element(By.XPATH, "//td[text()='192.168.1.100']")
        assert ip_el.text == "192.168.1.100"

        uname_el = driver.find_element(By.XPATH, "//td[text()='Kiran112']")
        assert uname_el.text == "Kiran112"

        dtype_el = driver.find_element(By.XPATH, "//td[text()='IOS XR']")
        assert dtype_el.text == "IOS XR"

