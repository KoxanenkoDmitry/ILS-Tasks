import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    email_field = "//input[@type='email']"
    password_field = "//input[@type='password']"
    enter_button = "//button[@class='form_auth_button']"

    # Getters

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # Actions

    def send_email(self, email):
        self.get_email_field().send_keys(email)
        print("email entered")

    def send_password(self, password):
        self.get_password_field().send_keys(password)
        print("email entered")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("enter button click")


    # Methods

    def enter_email_and_password(self, email, password):
        with allure.step("Enter email and password"):
            Logger.add_start_step(method="enter_email_and_password")
            self.get_current_url()
            self.send_email(email)
            self.send_password(password)
            self.click_enter_button()
            print("authorization complete")
            Logger.add_end_step(url=self.driver.current_url, method="enter_email_and_password")

