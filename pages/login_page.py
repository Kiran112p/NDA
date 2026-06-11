from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

        # Locators
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.CSS_SELECTOR, ".btn-login")

    def open(self, url: str = "https://networkmangement.netlify.app/"):
        self.driver.get(url)

    def login(self, username="Kiran112", password="Kiran@112"):

        # Wait + enter username
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

        # Wait + enter password
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

        # Wait + click button
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

        print("Login successful")

driver = webdriver.Chrome()
driver.maximize_window()

login_page = LoginPage(driver)
login_page.open()
login_page.login()