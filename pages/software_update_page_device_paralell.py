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

#Locaters

job_name="routers_Parallel_Update"

file_upload='//input[@type="file"]'
os_path=r"D:\resume\overview1.txt"
device_selection="selectAllDevices"
instalation_type="installationType"
screen_path="D:\\NDA\\reports\\Screenshots\\software_update_parallel.png"

class SoftwareUpdatePageDeviceParallel:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_software_update(self):
        software_update_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@href="#software-update"]')))
        software_update_icon.click()
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def add_software_update(self):
        upload_zone = self.wait.until(
            EC.presence_of_element_located((By.XPATH, file_upload))
        )
       
        upload_zone.send_keys(os.path.abspath(os_path))
        print(f"File uploaded: {os_path}")

        
        
        # Wait for the file to appear in the UI
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//strong[contains(text(), "overview1.txt")]')))
        print("File confirmed in upload area")

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.ID,'nextStep1'))
        ).click()

        time.sleep(5)
        
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.ID,device_selection))
        ).click()

        install_button = Select(self.driver.find_element(By.ID,instalation_type))
        install_button.select_by_value("Parallel")

        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.ID,'nextStep2'))).click()

        self.driver.find_element(By.ID,"jobName").send_keys(job_name)

        self.driver.find_element(By.XPATH,'(//*[text()="Run now"])[1]').click()

        self.driver.find_element(By.ID,"startJob").click()


        self.driver.save_screenshot(screen_path)

        print("Software update job created successfully with parallel installation type and RUN NOW option")

# inst_login = LoginPage(webdriver.Chrome())
# inst_login.open()   
# inst_login.login()

# inst_software_update = SoftwareUpdatePageDeviceParallel(inst_login.driver)
# inst_software_update.navigate_to_software_update()
# inst_software_update.add_software_update()
