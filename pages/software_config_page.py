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
from pages.login_page import LoginPage
from pages.device_management_ssh_private import DeviceManagementPage

#locaters
sotware_config=(By.XPATH,'//*[@href="#device-config"]')
confi_name_id=(By.ID,'cfgName')
config_description_id=(By.ID,'cfgDescription')
next_id=(By.ID,'cfgNext')
device_n_id=(By.ID,'cfgDeviceSelect')
cmd_line_id=(By.ID,'cfgScript')
save_config=(By.ID,'cfgSave')
pop_up_xpath=(By.XPATH, '//*[@class="version-modal-box config-push-success-box"]')
pop_up_accept=(By.ID,"configPushSuccessOk")

value="ROUTER_NCS_540"
placeholder=("hostname {{public_host}}\
            ip domain-name {{domain}}")



inst_login = LoginPage(webdriver.Chrome())
inst_login.open()   
inst_login.login()
inst_device =DeviceManagementPage(inst_login.driver)
inst_device.navigate_to_device_management()
inst_device.add_device()

time.sleep(3)

class SoftwareConfig:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_soft_config(self):
        navigate = self.wait.until(
            EC.element_to_be_clickable((sotware_config))
        )
        navigate.click()
        
    
    def device_config(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(
            EC.element_to_be_clickable(confi_name_id)
        ).send_keys("public_host")
        
        self.wait.until(
            EC.visibility_of_element_located(config_description_id)
        ).send_keys("This config changing the device host like private host to public host")
        
        self.driver.find_element(*next_id).click()


        device_n = Select(self.wait.until(EC.element_to_be_clickable(device_n_id)))
        device_n.select_by_value("ROUTER_NCS_540")
        
        self.driver.find_element(*next_id).click()
        
        self.wait.until(
            EC.element_to_be_clickable(cmd_line_id)
        ).send_keys(placeholder)
        
        self.driver.find_element(*next_id).click()

        self.driver.find_element(*save_config).click()
        
        self.wait.until(
            EC.visibility_of_element_located(pop_up_xpath))
        self.driver.find_element(*pop_up_accept).click()

        self.driver.save_screenshot(r"D:\NDA\reports\_after_config_job.png")
        
        time.sleep(500)
        print("Device config was sucsusfull as hostname public")
        

inst_soft=SoftwareConfig(inst_login.driver)
inst_soft.navigate_to_soft_config()
inst_soft.device_config()