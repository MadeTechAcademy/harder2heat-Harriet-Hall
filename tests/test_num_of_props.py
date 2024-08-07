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
            
    assert list_of_headers == ["UPRN", "OSID", "Year Built", "Updated on", "Connectivity", "Building materials", "Size in m2","Coordinates", "Score" ]

