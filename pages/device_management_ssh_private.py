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


time.sleep(5)
class DeviceManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _click(self, locator, delay=0.10):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        time.sleep(delay)

    def _type(self, locator, value, delay=0.6):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
        time.sleep(delay)

    def navigate_to_device_management(self):
        self._click((By.XPATH, '//*[@href="#device-management"]'))

    def add_device(self):
        self._type(d_name_id, d_name)
        self._type(d_ip_id, d_ip)
        self._type(d_uname_id, d_uname)
        self._type(d_pwd_id, d_pwd)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

        device_type = Select(self.wait.until(EC.element_to_be_clickable(d_type_id)))
        device_type.select_by_visible_text(d_type)
        time.sleep(0.5)

        device_version = Select(self.wait.until(EC.element_to_be_clickable(d_version_id)))
        device_version.select_by_visible_text(d_version)
        time.sleep(0.5)

        host_name = self.wait.until(EC.visibility_of_element_located(d_host_id))
        host_name.clear()
        host_name.send_keys(d_host)
        time.sleep(0.3)

        protocol = Select(self.wait.until(EC.element_to_be_clickable(d_proto_id)))
        protocol.select_by_visible_text(d_protocol)
        time.sleep(0.5)

        self._click(save_button)

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        time.sleep(0.5)

        print("Device added successfully")






