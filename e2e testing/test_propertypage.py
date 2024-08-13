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

    def get_table(self, browser):
        try:
            return browser.find_element(By.CLASS_NAME, "govuk-table")
        except NoSuchElementException:
            pytest.fail("No table element found")
            

    def test_page_header(self, browser):
        try:
            h2_tag = browser.find_element(By.TAG_NAME, "h2")
            assert h2_tag.text == "100090062297"

        except NoSuchElementException:
            pytest.fail("No h1 element found")



    def test_displays_table_with_propery_features_as_headers(self, browser):
        try:
                
            table = self.get_table(browser)
            headers = table.find_elements(By.TAG_NAME, "th")

            assert len(headers) == 8
            list_of_headers = []

            for header in headers:
                text = header.text
                list_of_headers.append(text)

            assert list_of_headers == [
              
                "OSID:",
                "Year Built:",
                "Updated on:",
                "Connectivity:",
                "Building materials:",
                "Size in m2:",
                "Coordinates:",
                "Hard To Heat Score:\n(easy) 0 - 4 (hard)"
            ]
        except NoSuchElementException:
            pytest.fail("No table header element found")



