import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Under_18(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    text_on_page = '/html/body/p'

    # Getters

    def get_text_on_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_on_page)))

    # Actions

    def read_text_on_page(self):
        read = self.get_text_on_page().text
        print("text is: " + read)

    # Methods

    def check_text_on_page_under_18(self):
        with allure.step("check text on page under 18"):
            Logger.add_start_step(method="check_text_on_page_under_18")
            self.get_current_url()
            self.read_text_on_page()
            self.assert_word(self.get_text_on_page(), "Никоторые считают что человек взраслеит в каком нибудь "
                                                      "оприделённом возрасте например, к 18 лет , когда он становиться "
                                                      "совершенно летним. Но есть люди, которые и в более старшем "
                                                      "возрасте остаются детьми. Что же значит быть взрослым? Взрослость "
                                                      "озночает самостоятельность, то есть умение обходится без чьей-либо "
                                                      "помощи опеки. Человек обладающий этим качеством всё делает сам, "
                                                      "и не ждёт поддержки от других. Он понимает, что свои трудности "
                                                      "должен преодалевать сам. Конечно бывают ситуации, когда человеку "
                                                      "одному не справится. Понимая это, ему приходиться просить помощи у "
                                                      "друзей, родственников, и знакомых. Однако в целом "
                                                      "самостоятельному, взрослому человеку не свойственно надеяться на "
                                                      "других. Есть такое выражение: руке следует ждать помощи только от "
                                                      "плеча. Самостоятельный человек умеет отвечать за себя свои дела и "
                                                      "поступки. Он сам планирует свою жизнь, и оценивает себя не "
                                                      "пологаясь на чьё-то мнение. Он понимает, что многое в жизни "
                                                      "зависет от него самого. Быть взрослым - значит отвечать за кого-то "
                                                      "ещё. Но для этого тоже надо стать самостоятельным, уметь принимать "
                                                      "решения. Взрослость зависет не от возраста, а от жизненного опыта "
                                                      "от стремления прожить жизнь без нянек.")
            self.get_screenshot()
            print("check page under 18 is okay")
            self.driver.back()
            Logger.add_end_step(url=self.driver.current_url, method="check_text_on_page_under_18")

