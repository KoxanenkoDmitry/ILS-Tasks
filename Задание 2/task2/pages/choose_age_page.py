import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Choose_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    radiobutton_under_18 = "//input[@value='18']"
    radiobutton_from_18_to_24 = "//input[@value='18-24']"
    radiobutton_from_25_to_34 = "//input[@value='25-34']"
    radiobutton_more_35 = "//input[@value='35-50']"
    send_button = "// input[ @ type = 'submit']"


    # Getters

    def get_radiobutton_under_18(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_under_18)))

    def get_radiobutton_from_18_to_24(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_from_18_to_24)))

    def get_radiobutton_from_25_to_34(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_from_25_to_34)))

    def get_radiobutton_more_35(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_more_35)))

    def get_send_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_button)))

    # Actions

    def click_radiobutton_under_18(self):
        self.get_radiobutton_under_18().click()
        print("under 18 button click")

    def click_radiobutton_from_18_to_24(self):
        self.get_radiobutton_from_18_to_24().click()
        print("18-24 button click")

    def click_radiobutton_from_25_to_34(self):
        self.get_radiobutton_from_25_to_34().click()
        print("25-34 button click")

    def click_radiobutton_more_35(self):
        self.get_radiobutton_more_35().click()
        print("more 35 button click")

    def click_send_button(self):
        self.get_send_button().click()
        print("send button click")


    # Methods

    def choose_radiobutton_under_18(self):
        with allure.step("choose radiobutton under 18"):
            Logger.add_start_step(method="choose_radiobutton_under_18")
            self.click_radiobutton_under_18()
            self.click_send_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_radiobutton_under_18")

    def choose_radiobutton_from_18_to_24(self):
        with allure.step("choose radiobutton from 18 to 24"):
            Logger.add_start_step(method="choose_radiobutton_from_18_to_24")
            self.click_radiobutton_from_18_to_24()
            self.click_send_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_radiobutton_from_18_to_24")

    def choose_radiobutton_from_25_to_34(self):
        with allure.step("choose radiobutton from 25 to 34"):
            Logger.add_start_step(method="choose_radiobutton_from_25_to_34")
            self.click_radiobutton_from_25_to_34()
            self.click_send_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_radiobutton_from_25_to_34")

    def choose_radiobutton_more_35(self):
        with allure.step("choose radiobutton more 35"):
            Logger.add_start_step(method="choose_radiobutton_more_35")
            self.click_radiobutton_more_35()
            self.click_send_button()
            Logger.add_end_step(url=self.driver.current_url, method="choose_radiobutton_more_35")





