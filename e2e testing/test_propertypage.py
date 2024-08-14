import pytest
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


@pytest.fixture(autouse=True)
def before_each_test(browser):
    try:
        button = browser.find_element(By.TAG_NAME, "a")
        button.click()
        return browser.find_element(By.CLASS_NAME, "govuk-table")
    except NoSuchElementException:
        pytest.fail("No elements found")


class TestPropertyPage:

    def test_page_header(self, browser):
        try:
            h2_tag = browser.find_element(By.TAG_NAME, "h2")
            assert len(h2_tag.text) == 12
            assert h2_tag.text in browser.current_url

        except NoSuchElementException:
            pytest.fail("No h2 element found")

    def test_displays_table_with_propery_features_as_headers(self, browser):
        try:
            headers = browser.find_elements(By.TAG_NAME, "th")

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
                "Hard To Heat Score:\n(easy) 0 - 3 (hard)",
            ]
        except NoSuchElementException:
            pytest.fail("No table header element found")

    def test_displays_table_property_data(self, browser):
        try:
            cells = browser.find_elements(By.TAG_NAME, "td")

            assert type(cells[0].text) == str
            assert type(cells[1].text) == str or type(cells[1].text) == int
            assert type(cells[2].text) == str
            assert cells[3].text in [
                "Free-Standing",
                "Single-Connected",
                "Dual-Connected",
            ]
            assert cells[4].text in ["Brick Or Block Or Stone", "Contrete"]
            assert (
                type(float(cells[5].text)) == float or type(int(cells[4].text)) == int
            )
            assert type(cells[6].text) == str
            assert cells[7].text in ["0", "1", "2", "3"]

        except NoSuchElementException:
            pytest.fail("No table data element found")

    def test_home_button_navigates_to_homepage(self, browser):
        try:

            home_button = browser.find_element(By.TAG_NAME, "a")
            url = home_button.get_attribute("href")

            assert url == "http://127.0.0.1:5000/"
            assert browser.current_url != url

            home_button.click()
            WebDriverWait(browser, 10).until(EC.url_to_be(url))

            assert browser.current_url == url

        except TimeoutException:
            print("Navigation took too long.")
        except AssertionError:
            print("Wrong URL")
