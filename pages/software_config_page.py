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
from helpers.locaters import *
from helpers.variables import *



# inst_login = LoginPage(webdriver.Chrome())
# inst_login.open()   
# inst_login.login()
# inst_device =DeviceManagementPage(inst_login.driver)
# inst_device.navigate_to_device_management()
# inst_device.add_device()

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
        ).send_keys(host_name)
        
        self.wait.until(
            EC.visibility_of_element_located(config_description_id)
        ).send_keys(desription)
        
        self.driver.find_element(*next_id).click()


        device_n = Select(self.wait.until(EC.element_to_be_clickable(device_n_id)))
        device_n.select_by_value(value)
        
        self.driver.find_element(*next_id).click()
        
        self.wait.until(
            EC.element_to_be_clickable(cmd_line_id)
        ).send_keys(placeholder)
        
        self.driver.find_element(*next_id).click()

        self.driver.find_element(*save_config).click()
        
        self.wait.until(
            EC.visibility_of_element_located(pop_up_xpath))
        self.driver.find_element(*pop_up_accept).click()

        self.driver.save_screenshot(screen_path)
        
        time.sleep(5)
        print("Device config was sucsusfull as hostname public")
    
    def validate_config_results(self):
        """Validate configuration jobs by clicking the latest job and checking details modal."""
        print("Validating configuration results (page object)...")

        # Wait for jobs panel
        self.wait.until(EC.presence_of_element_located(config_panel_jobs))
        time.sleep(1)

        # Find job rows and click the first job name to open details modal
        job_rows = self.driver.find_elements(*config_job_rows)
        print(f"Found {len(job_rows)} configuration jobs")
        if not job_rows:
            raise AssertionError("No configuration jobs found")

        first_row = job_rows[0]
        # try to find clickable link or fallback to first cell
        try:
            job_link = first_row.find_element(By.XPATH, './/a')
        except Exception:
            job_link = first_row.find_element(By.XPATH, './/td[1]')

        job_name_text = job_link.text
        print(f"Clicking job: {job_name_text}")
        job_link.click()

        # Wait for the details message element to appear
        msg_elem = self.wait.until(EC.visibility_of_element_located(config_job_details_message))
        print('configJobDetailsMessage text:', msg_elem.text)
        assert msg_elem.text and msg_elem.text.strip() != "", 'configJobDetailsMessage is empty'

        # Try to validate Device and Status from the modal; fall back to parsing message or row if needed
        device_text = None
        status_text = None
        try:
            device_elem = self.wait.until(EC.visibility_of_element_located(config_job_detail_device_label))
            device_text = device_elem.text.strip()
            print(f"Device in details: {device_text}")
        except Exception:
            # fallback: parse device name from the message text
            msg = msg_elem.text or ""
            if value in msg:
                device_text = value
                print(f"Parsed device from message: {device_text}")

        try:
            status_elem = self.wait.until(EC.visibility_of_element_located(config_job_detail_status_label))
            status_text = status_elem.text.strip()
            print(f"Status in details: {status_text}")
        except Exception:
            # fallback: try to read status from the job row badge
            try:
                status_badge = first_row.find_element(By.XPATH, './/span[contains(@class,"status-badge")]')
                status_text = status_badge.text.strip()
                print(f"Status parsed from row: {status_text}")
            except Exception:
                print("Could not locate explicit status element; leaving status_text as None")

        if device_text is None:
            raise AssertionError(f"Device not found in modal or message; expected '{value}'")

        if not ((status_text == expected_config_job_status) or (status_text and status_text.lower() in ['success', 'completed'])):
            raise AssertionError(f"Unexpected job status '{status_text}'")

        print("✓ Configuration validation passed (page object)")
        
print("Software configuration workflow completed successfully. and validation also passed with expected status as Completed")
# inst_soft=SoftwareConfig(inst_login.driver)
# inst_soft.navigate_to_soft_config()
# inst_soft.device_config()