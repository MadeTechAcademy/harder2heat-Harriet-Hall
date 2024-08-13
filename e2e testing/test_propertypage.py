import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/100090062297")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestPropertyPage:

    def test_page_header(self, browser):
        try:
            h2_tag = browser.find_element(By.TAG_NAME, "h2")
            assert h2_tag.text == "100090062297"

        except NoSuchElementException:
            pytest.fail("No h1 element found")
