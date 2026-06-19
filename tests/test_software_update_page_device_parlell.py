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

# Locators
job_name = (By.XPATH, '//*[@class="jobs-table"]//tbody/tr[1]/td[2]')
job_status = (By.ID, "detailStatus")
run_status = (By.ID, "detailRunStatus")
run_time = (By.ID, "detailRunTime")
installation_type = (By.ID, "detailInstallationType")
software_image = (By.ID, "detailImage")

class TestSoftwarePage:
    def test_software_update_page(self, driver):
        """this func will verify after creating a job"""
        self.driver = driver
        software_page = SoftwareUpdatePageDeviceParallel(driver)
        software_page.navigate_to_software_update()
        software_page.add_software_update()

        wait = WebDriverWait(driver, 60)

        def _get_text(element):
            return (element.text or element.get_attribute("textContent") or element.get_attribute("innerText") or "").strip()

        job_row = wait.until(EC.element_to_be_clickable(job_name))
        assert _get_text(job_row) == "routers_Parallel_Update", "job name was not matching"
        job_row.click()
        time.sleep(2)

        status_el = wait.until(EC.visibility_of_element_located(job_status))
        j_s = _get_text(status_el)
        assert j_s == "Completed", "actual status was not matching"

        run_el = wait.until(EC.visibility_of_element_located(run_status))
        r_s = _get_text(run_el)
        assert r_s == "Success", "actual status was failed"

        runtime_el = wait.until(EC.visibility_of_element_located(run_time))
        r_t = _get_text(runtime_el)
        print("run time was ::", r_t)

        inst_el = wait.until(EC.visibility_of_element_located(installation_type))
        in_t = _get_text(inst_el)
        assert in_t == "Parallel", "not matching, its sequential"

        image_el = wait.until(EC.visibility_of_element_located(software_image))
        image = _get_text(image_el)
        print("updated os image was ::", image)



