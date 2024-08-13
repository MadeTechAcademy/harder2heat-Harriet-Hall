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


    def test_displays_table_property_data(self, browser):
        try:
            
            table = self.get_table(browser)
            cells = table.find_elements(By.TAG_NAME, "td")
            cell_data_list = []
            for cell in cells:
                text = cell.text
                cell_data_list.append(text)

            assert cell_data_list == [
                "0b1107e5-00f8-4d89-b6ae-67f0f98a6517",
                "1918",
                "2024-03-13",
                "Free-Standing",
                "Brick Or Block Or Stone",
                "120.143",
                "[[0.0471489, 52.4569721], [0.0472922, 52.4569964], [0.0473205, 52.4569337], [0.0473576, 52.45694], [0.0473707, 52.4569112], [0.0473336, 52.4569049], [0.0473464, 52.4568765], [0.0472657, 52.4568629], [0.0472642, 52.4568662], [0.0472467, 52.4568633], [0.0472399, 52.4568621], [0.0472175, 52.4569117], [0.0472229, 52.4569126], [0.0472151, 52.4569296], [0.0472085, 52.456944], [0.047165, 52.4569366], [0.0471489, 52.4569721]]",
                "2",
            ]
        except NoSuchElementException:
            pytest.fail("No table data element found")

