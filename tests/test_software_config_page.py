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

from pages.software_config_page import SoftwareConfig

#test software config Locaters
j_name=(By.XPATH,'(//button[@data-id="cfgjob_1782192832459"])[1]')
suc_txt=(By.XPATH,'//*[@id="configJobDetailsMessage"]')
d_name=(By.XPATH,"(//td[text()='ROUTER_NCS_540'])[3]")
status=(By.XPATH,'(//span[@class="status-badge success"])[1]')
run_time=(By.XPATH,"//td[text()='23-Jun-2026 11:03:52 AM IST']")


time.sleep(20)
@pytest.mark.regression
class TestSoftwareConfig:
    def test_config_page(self, driver):
        self.wait=WebDriverWait(driver, 10)
        self.driver = driver
        
        j_n=self.wait.until(
            EC.visibility_of_element_located((j_name))).text
        print("config_job_name :: " , j_n)

        conf_name=self.driver.find_element((d_name)).text
        assert conf_name == 'ROUTER_NCS_540', "device name not matching"
        
        sta=self.driver.find_element((status)).text
        assert sta == 'Completed', "status was not completd"

        time=self.driver.find_element((run_time)).text
        print("run time is :: ",time)






        
        

