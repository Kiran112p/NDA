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
        software_page.navigate_to_software_update()
        software_page.add_software_update()

        wait = WebDriverWait(driver, 10)
        jb_n=wait.until(EC.presence_of_element_located((job_name))).text
        print("job_name is :: ",jb_n)
        
        jb_s=wait.until(EC.presence_of_element_located((job_status))).text
        assert jb_s == "Completed","job status was not matchi something else"

        rn_s=wait.until(EC.presence_of_element_located((run_status))).text
        assert rn_s == "Success", "run status was not matchin something else"

        rn_t=wait.until(EC.presence_of_element_located((run_status))).text
        print("run time was :: ", rn_t)

        driver.quit()
    print("software update page sucsusfully test complete")
    


