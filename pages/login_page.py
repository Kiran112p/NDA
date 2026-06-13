from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.CLASS_NAME, "btn-login")

    def open(self, url: str = "https://networkmangement.netlify.app/"):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username="Kiran112", password="Kiran@112"):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        
        print("Login successful")


