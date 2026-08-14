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
from helpers.locaters import *
from helpers.variables import *



class SoftwareUpdatePageDeviceParallel:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        

    def navigate_to_software_update(self):
        print("naviagating to module ")
        software_update_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@href="#software-update"]')))
        software_update_icon.click()
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def add_software_update(self):
        upload_zone = self.wait.until(
            EC.presence_of_element_located(file_upload)
        )
       
        upload_zone.send_keys(os.path.abspath(os_path))
        print(f"File uploaded: {os_path}")

        
        
        # Wait for the file to appear in the UI
        self.wait.until(EC.presence_of_element_located(file_appeared))
        print("File confirmed in upload area")

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(su_next_btn1)
        ).click()

        time.sleep(5)
        
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(device_selection)
        ).click()

        install_button = Select(self.driver.find_element(*instalation_type))
        install_button.select_by_value("Parallel")

        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(su_next_btn2)).click()

        # enter a job name (use variable from helpers.variables)
        self.driver.find_element(*su_job_name).send_keys(software_update_job_name)

        self.driver.find_element(*run_now).click()

        self.driver.find_element(*srt_job).click()


        self.driver.save_screenshot(screen_path)

    def validate_job_status(self):
        wait = WebDriverWait(self.driver, 10)
        jb_n=wait.until(EC.presence_of_element_located(job_name)).text
        print("job_name is :: ",jb_n)
        
        jb_s=wait.until(EC.presence_of_element_located(job_status)).text
        assert jb_s == expected_job_status, f"job status was not matching expected '{expected_job_status}'"

        rn_s=wait.until(EC.presence_of_element_located(run_status)).text
        assert rn_s == expected_run_status, f"run status was not matching expected '{expected_run_status}'"

        rn_t=wait.until(EC.presence_of_element_located(run_time)).text
        print("run time was :: ", rn_t)

        self.driver.quit()
        print("software update page sucsusfully test complete")
    

print("Software update job created successfully with parallel installation type and RUN NOW option")


