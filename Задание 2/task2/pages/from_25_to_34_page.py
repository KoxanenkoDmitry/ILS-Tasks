import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class From_25_to_34(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    text_on_page = '/html/body/h1'

    # Getters

    def get_text_on_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_on_page)))

    # Actions

    def read_text_on_page(self):
        read = self.get_text_on_page().text
        print("text is: " + read)


    # Methods

    def check_text_on_page_from_25_to_34(self):
        with allure.step("check text on page from 25 to 34"):
            Logger.add_start_step(method="check_text_on_page_from_25_to_34")
            self.get_current_url()
            self.read_text_on_page()
            self.assert_word(self.get_text_on_page(), "Not Found")
            self.get_screenshot()
            print("check page from 25 to 34 is okay")
            self.driver.back()
            Logger.add_end_step(url=self.driver.current_url, method="check_text_on_page_from_25_to_34")

