import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_displays_num_of_properties(chrome_browser):

    chrome_browser.get("http://127.0.0.1:5000")
    footer_tag = chrome_browser.find_element(By.TAG_NAME, "footer")
    regex_find_num_of_properties = re.search(r"\d+", footer_tag.text)
    number_of_properties = int(regex_find_num_of_properties.group())
    assert footer_tag.text == "Properties : 4"
    assert number_of_properties == 4
    
def test_displays_main_title(chrome_browser):
    chrome_browser.get("http://127.0.0.1:5000")
    h1_tag = chrome_browser.find_element(By.TAG_NAME, "h1")
    assert h1_tag.text == "Hard to Heat Homes"
    
