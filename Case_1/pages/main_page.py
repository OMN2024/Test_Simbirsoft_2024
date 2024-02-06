from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CLASS_NAME, 'custom-control.custom-radio.custom-control-inline')
    MOBILE = (By.XPATH, '//*[@id="userNumber"]')
    D_BIRTH = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    SUBJECTS = (By.ID, 'subjectsInput')
    HOBBIES = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label')
    PICTURE = (By.ID, 'uploadPicture')
    ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.ID, 'state')
    STATE= (By.ID, 'react-select-3-option-2')
    SELECT_CITY = (By.ID, 'city')
    CITY = (By.ID, 'react-select-4-option-0')
    SUBMIT = (By.ID, 'submit')


class MainPage(BasePage):
    def first_name(self):
        try:
            return self.is_element_present(*MainPageLocators.FIRST_NAME)
        except NoSuchElementException:
            self.fail("ERROR_first_name")

    def last_name(self):
        try:
            return self.is_element_present(*MainPageLocators.LAST_NAME)
        except NoSuchElementException:
            self.fail("ERROR_last_name")

    def email(self):
        try:
            return self.is_element_present(*MainPageLocators.EMAIL)
        except NoSuchElementException:
            self.fail("ERROR_email")

    def genders(self):
        try:
            list_gender = self.is_elements_present(*MainPageLocators.GENDER)
            if len(list_gender) == 0:
                raise
            return list_gender
        except:
            self.fail("ERROR_genders")

    def mobile(self):
        try:
            return self.is_element_present(*MainPageLocators.MOBILE)
        except NoSuchElementException:
            self.fail("ERROR_mobile")

    def date_of_birth(self):
        try:
            return self.is_element_present(*MainPageLocators.D_BIRTH)
        except NoSuchElementException:
            self.fail("ERROR_date_of_birth")

    def subjects(self):
        try:
            return self.is_element_present(*MainPageLocators.SUBJECTS)
        except NoSuchElementException:
            self.fail("ERROR_subjects")

    def check_box(self):
        try:
            return self.is_element_present(*MainPageLocators.HOBBIES)
        except NoSuchElementException:
            self.fail("ERROR_check_box")

    def picture_load(self):
        try:
            return self.is_element_present(*MainPageLocators.PICTURE)
        except NoSuchElementException:
            self.fail("ERROR_picture_load")

    def adress(self):
        try:
            return self.is_element_present(*MainPageLocators.ADDRESS)
        except NoSuchElementException:
            self.fail("ERROR_adress")

    def select_state(self):
        try:
            return self.is_element_present(*MainPageLocators.SELECT_STATE)
        except:
            self.fail("ERROR_select_state")
    def sel_state(self):
        try:
            return self.is_element_present(*MainPageLocators.STATE)
        except:
            self.fail("ERROR_state")


    def select_city(self):
        try:
            return self.is_element_present(*MainPageLocators.SELECT_CITY)
        except:
            self.fail("ERROR_select_city")

    def sel_city(self):
        try:
            return self.is_element_present(*MainPageLocators.CITY)
        except:
            self.fail('ERROR_city')

    def button_submit(self):
        try:
            return self.is_element_present(*MainPageLocators.SUBMIT)
        except NoSuchElementException:
            self.fail("ERROR_button_submit")

    def get_final_screen(self):
        self.get_screenshot()