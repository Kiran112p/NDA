import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pages.software_update_page_device_paralell import SoftwareUpdatePageDeviceParallel
from helpers.locaters import *
from helpers.variables import *




@pytest.mark.regression
class TestSoftwarePage:
    def test_software_update_page(self, driver):
        """this func will verify after creating a job"""
        self.driver = driver
        software_page = SoftwareUpdatePageDeviceParallel(driver)
        print("\n=== Step 1: Navigate to Software Update Page ===")
        software_page.navigate_to_software_update()

        print("\n=== Step 2: Add Software Update ===")
        software_page.add_software_update()
        
        print("\n=== Step 3: Validate Job Status ===")
        software_page.validate_job_status()
        


