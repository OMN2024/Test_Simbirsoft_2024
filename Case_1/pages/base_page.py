from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            # return self.browser.find_element(how, what)
            elem = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((how, what))
            )
            self.browser.execute_script('arguments[0].scrollIntoView(true)', elem)
            return elem
        except (NoSuchElementException):
            return False

    def is_elements_present(self, how, what):
        return self.browser.find_elements(how, what)


    def get_screenshot(self):
        self.browser.get_screenshot_as_file("./Case_1/Data/image.png")