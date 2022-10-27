from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Client_Information_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input Zip Code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")


    # Methods

    def input_info(self):

        self.get_current_url()
        self.input_first_name("Nick")
        self.input_last_name("YG")
        self.input_zip_code("644122")
        self.click_continue_button()