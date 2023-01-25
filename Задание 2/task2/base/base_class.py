import datetime
import time


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def get_screenshot(self):
        time.sleep(2)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\koxan\\PycharmProjects\\task2\\screen\\' + name_screenshot)


