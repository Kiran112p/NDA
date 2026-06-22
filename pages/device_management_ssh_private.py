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


time.sleep(5)
class DeviceManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_device_management(self):    
        server_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@href="#device-management"]')))
        server_icon.click()
    def add_device(self):
        self.driver.find_element(By.ID,"deviceName").send_keys("ROUTER_NCS_540")
        self.driver.find_element(By.ID,"deviceIp").send_keys("192.168.1.100")
        self.driver.find_element(By.ID,"deviceUname").send_keys("Kiran112")
        self.driver.find_element(By.ID,"devicePassword").send_keys("Kiran@112")
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        device_type= Select(self.driver.find_element(By.ID,"deviceType"))
        device_type.select_by_visible_text("IOS XR")
        
        device_version=Select(self.driver.find_element(By.ID,"deviceVersion"))
        device_version.select_by_visible_text("7.0")

        host_name=self.driver.find_element(By.ID,"deviceHostname")
        host_name.clear()
        host_name.send_keys("Private")

        protocol=Select(self.driver.find_element(By.ID,"deviceProtocol"))
        protocol.select_by_visible_text("SSH")

        self.driver.find_element(By.XPATH,'(//button[@class="btn-primary"])[4]').click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

        print("Device added successfully")






