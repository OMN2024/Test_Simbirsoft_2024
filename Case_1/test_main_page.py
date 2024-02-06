import os
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from .pages.main_page import MainPage

@allure.feature('Open page')
@allure.story('Открываем страницу demoqa.com')
@allure.severity('trivial')
def test_page(browser):
    link = "https://demoqa.com/automation-practice-form"
    page = MainPage(browser,link)
    page.open()

    f_name = page.first_name()
    f_name.send_keys("Ivan")
    l_name = page.last_name()
    l_name.send_keys("Petrov")

    e_mail = page.email()
    e_mail.send_keys("i_petrov@gmail.com")

    genders = page.genders()
    if len(genders) > 0:
        genders[0].click()

    tel = page.mobile()
    tel.send_keys("1234567890")

    date_birth = page.date_of_birth()
    date_birth.click()
    date_birth.send_keys(Keys.CONTROL, "a")
    date_birth.send_keys("01.01.2000")
    tel.click()

    subj = page.subjects()
    subj.click()
    subj.send_keys('Maths')
    # time.sleep(1)
    subj.send_keys(Keys.ENTER)
    # time.sleep(1)

    subj.send_keys('a')
    # time.sleep(1)
    subj.send_keys(Keys.DOWN)
    subj.send_keys(Keys.ENTER)

    hobbies = page.check_box()
    hobbies.click()

    picture = page.picture_load()
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "./Data", "picture.png")
    )
    picture.send_keys(upload_file)

    addr = page.adress()
    addr.send_keys("111111\n2222222222")

    cl_state = page.select_state()
    cl_state.click()
    state = page.sel_state()
    state.click()

    cl_city = page.select_city()
    cl_city.click()
    city = page.sel_city()
    city.click()

    b_submit = page.button_submit()
    b_submit.click()

    with allure.step('Делаем скриншот'):
        allure.attach(page.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    page.get_final_screen()


