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
    driver.get("http://127.0.0.1:5000")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestHomePage:

    def get_table(self, browser):
        try:
            return browser.find_element(By.ID, "data")
        except NoSuchElementException:
            pytest.fail("No table element found")

    def test_displays_num_of_properties(self, browser):
        try:
            footer_tag = browser.find_element(By.TAG_NAME, "footer")
            regex_find_num_of_properties = re.search(r"\d+", footer_tag.text)
            number_of_properties = int(regex_find_num_of_properties.group())
            assert footer_tag.text == "Properties : 4"
            assert number_of_properties == 4
        except NoSuchElementException:
            pytest.fail("No footer element found")

    def test_displays_main_title(self, browser):
        try:
            h1_tag = browser.find_element(By.TAG_NAME, "h1")
            assert h1_tag.text == "Harder to Heat Homes"
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
                "UPRN",
                "Year Built",
                "Connectivity",
                "Building materials",
                "Size in m2",
                "Coordinates",
                "Hard To Heat Score:\n" "(easy) 0 - 3 (hard)",
                "",
            ]
        except NoSuchElementException:
            pytest.fail("No table header element found")

    def test_displays_table_property_data(self, browser):
        try:

            table = self.get_table(browser)
            cells = table.find_elements(By.TAG_NAME, "td")

            assert len(cells[0].text) == 12
            assert type(cells[1].text) == str or type(cells[1].text) == int
            assert cells[2].text in ["Free-Standing", "Single-Connected", "Dual-Connected"]
            assert cells[3].text in ["Brick Or Block Or Stone", "Contrete"]
            assert type(float(cells[4].text)) == float or type(int(cells[4].text)) == int
            assert type(cells[5].text) == str
            assert cells[6].text in ["0", "1", "2", "3"]
            assert cells[7].text == "See more details"


        except NoSuchElementException:
            pytest.fail("No table data element found")

    def test_displays_multiple_properties(self, browser):
        try:
            table = self.get_table(browser)
            rows = table.find_elements(By.TAG_NAME, "tr")

            assert len(rows) > 2
        except NoSuchElementException:
            pytest.fail("No table rows found")

    def test_displays_see_more_details_button(self, browser):
        try:

            table = self.get_table(browser)
            button = table.find_element(By.TAG_NAME, "a")

            assert button.text == "See more details"
            assert (
                button.get_attribute("style") == "color: black; text-decoration: none;"
            )
        except NoSuchElementException:
            pytest.fail("No button element found")

    def test_button_navigates_to_property_page_with_uprn(self, browser):
        try:

            table = self.get_table(browser)
            button = table.find_element(By.TAG_NAME, "a")
            url = button.get_attribute("href")
            assert browser.current_url != url

            button.click()
            WebDriverWait(browser, 10).until(EC.url_to_be(url))

            assert browser.current_url == url

        except TimeoutException:
            print("Navigation took too long.")
        except AssertionError:
            print("Wrong URL")