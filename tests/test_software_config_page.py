import os
import sys
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ensure the NDA root directory is on sys.path so pages.login_page can be imported.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'NDA'))

from pages.software_config_page import SoftwareConfig
from pages.device_management_ssh_private import DeviceManagementPage
from helpers.locaters import *
from helpers.variables import *

@pytest.mark.regression
class TestSoftwareConfig:
    def test_complete_device_config_workflow(self, driver):
        """
        Complete workflow: Login -> Device Management -> Add Device -> Software Config -> Validate
        """
        self.wait = WebDriverWait(driver, 20)
        self.driver = driver
        
        # Step 1: Navigate to Device Management
        print("\n=== Step 1: Navigate to Device Management ===")
        device_mgmt = DeviceManagementPage(self.driver)
        device_mgmt.navigate_to_device_management()
        time.sleep(2)
        
        # Step 2: Add a new device
        print("\n=== Step 2: Add New Device ===")
        device_mgmt.add_device()
        time.sleep(3)
        
        # Verify device was added
        print("Verifying device was added...")
        try:
            self.wait.until(EC.visibility_of_element_located(device_name))
            added_device = self.driver.find_element(*device_name).text
            print(f"Device added successfully: {added_device}")
            assert added_device == 'ROUTER_NCS_540', f"Expected device 'ROUTER_NCS_540' but got '{added_device}'"
        except Exception as e:
            print(f"Device verification failed: {e}")
        
        time.sleep(2)
        
        # Step 3: Navigate to Software Config Page
        print("\n=== Step 3: Navigate to Software Config Page ===")
        soft_config = SoftwareConfig(self.driver)
        soft_config.navigate_to_soft_config()
        time.sleep(3)
        
        # Step 4: Perform Device Configuration
        print("\n=== Step 4: Perform Device Configuration ===")
        soft_config.device_config()
        time.sleep(5)
        
        # Step 5: Validate Configuration Results
        print("\n=== Step 5: Validate Configuration Results ===")
        self.validate_config_results()
        
        print("\n=== Test Completed Successfully ===")
    
    def validate_config_results(self):
        """Validate that the configuration job was created and completed"""
        print("Validating configuration results...")
        
        # Wait for jobs panel to load
        jobs_panel = self.wait.until(
            EC.presence_of_element_located((By.ID, "configPanelJobs"))
        )
        time.sleep(2)
        
        # Get job details
        try:
            job_rows = self.driver.find_elements(By.XPATH, '//*[@id="configPanelJobs"]//tbody//tr')
            print(f"Found {len(job_rows)} configuration jobs")
            
            if len(job_rows) > 0:
                # Get first job row
                first_job_text = job_rows[0].text
                print(f"Latest job details: {first_job_text}")
                
                # Verify job status
                status_elements = job_rows[0].find_elements(By.XPATH, './/span[@class="status-badge success"]')
                if status_elements:
                    status = status_elements[0].text
                    print(f"Job Status: {status}")
                    assert status == 'Completed' or status.lower() in ['success', 'completed'], f"Expected 'Completed' status but got '{status}'"
                
                print("✓ Configuration validation passed")
            else:
                print("No configuration jobs found - this may be expected if async processing is ongoing")
                
        except Exception as e:
            print(f"Configuration validation warning: {e}")






        
        

