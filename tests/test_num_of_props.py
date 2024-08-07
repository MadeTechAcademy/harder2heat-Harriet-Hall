import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_displays_num_of_properties(browser):

    footer_tag = browser.find_element(By.TAG_NAME, "footer")
    regex_find_num_of_properties = re.search(r"\d+", footer_tag.text)
    number_of_properties = int(regex_find_num_of_properties.group())
    assert footer_tag.text == "Properties : 4"
    assert number_of_properties == 4


def test_displays_main_title(browser):

    h1_tag = browser.find_element(By.TAG_NAME, "h1")
    assert h1_tag.text == "Hard to Heat Homes"


def test_displays_table_with_propery_features_as_headers(browser):

    table = browser.find_element(By.ID, "properties-table")
    headers = table.find_elements(By.TAG_NAME, "th")

    assert len(headers) == 9
    list_of_headers = []

    for header in headers:
        text = header.text
        list_of_headers.append(text)

    assert list_of_headers == [
        "UPRN",
        "OSID",
        "Year Built",
        "Updated on",
        "Connectivity",
        "Building materials",
        "Size in m2",
        "Coordinates",
        "Score",
    ]


def test_displays_table_property_data(browser):
    table = browser.find_element(By.ID, "properties-table")
    cells = table.find_elements(By.TAG_NAME, "td")
    cell_data_list = []
    for cell in cells[0:9]:
        text = cell.text
        cell_data_list.append(text)

    assert cell_data_list == [
        "100090062297",
        "0b1107e5-00f8-4d89-b6ae-67f0f98a6517",
        "1918",
        "2024-03-13",
        "Free-Standing",
        "Brick Or Block Or Stone",
        "120.143",
        "[[0.0471489, 52.4569721], [0.0472922, 52.4569964], [0.0473205, 52.4569337], [0.0473576, 52.45694], [0.0473707, 52.4569112], [0.0473336, 52.4569049], [0.0473464, 52.4568765], [0.0472657, 52.4568629], [0.0472642, 52.4568662], [0.0472467, 52.4568633], [0.0472399, 52.4568621], [0.0472175, 52.4569117], [0.0472229, 52.4569126], [0.0472151, 52.4569296], [0.0472085, 52.456944], [0.047165, 52.4569366], [0.0471489, 52.4569721]]",
        "2",
    ]
    

def test_displays_multiple_properties(browser):
    table = browser.find_element(By.ID, "properties-table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    assert len(rows) > 2

