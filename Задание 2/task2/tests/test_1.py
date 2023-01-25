import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import main_page, choose_age_page, under_18_page, from_18_to_24_page, from_25_to_34_page, more_35_page


@allure.description("Test site functionality check")
def test_site_functionality_check():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\koxan\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    url = 'http://u920152e.beget.tech/#'
    driver.get(url)
    print("Start Test 1 ")

    email = '1111@mail.ru'
    password = '1111'

    mp = main_page.Main_page(driver)
    mp.enter_email_and_password(email, password)

    cp = choose_age_page.Choose_page(driver)
    cp.choose_radiobutton_under_18()

    u18 = under_18_page.Under_18(driver)
    u18.check_text_on_page_under_18()

    cp.choose_radiobutton_from_18_to_24()

    f18_t24 = from_18_to_24_page.From_18_to_24(driver)
    f18_t24.check_text_on_page_from_18_to_24()

    cp.choose_radiobutton_from_25_to_34()

    f25_t34 = from_25_to_34_page.From_25_to_34(driver)
    f25_t34.check_text_on_page_from_25_to_34()

    cp.choose_radiobutton_more_35()

    m35 = more_35_page.More_35(driver)
    m35.check_text_on_page_more_35()

    print("Success! Test is pass!")

    driver.quit()






