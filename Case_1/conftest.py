import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
