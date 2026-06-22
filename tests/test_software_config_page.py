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

#Locaters
suc_txt=(By.XPATH,'//*[@id="configJobDetailsMessage"]')
d_name=(By.XPATH,'//*[@id="configJobDetailsDevice"]')
status=(By.XPATH,'//*[@id="configJobDetailsStatus"]')


time.sleep(20)
@pytest.mark.regression
class TestSoftwareConfig:
    def test_config_page(self, driver):
        self.driver = driver
        
        

