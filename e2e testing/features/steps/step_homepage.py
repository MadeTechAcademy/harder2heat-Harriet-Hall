from behave import given, when, then
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on the home page")
def step_open_home_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://127.0.0.1:5000")
    context.browser.implicitly_wait(10)

@then('the browser title bar should display "Harder to Heat Homes"')
def step_check_browser_bar_title(context):
    
    assert context.browser.title == "Harder to Heat Homes"  


@then('the main title should be "{title}"')
def step_check_main_title(context, title):

    h1_tag = context.browser.find_element(By.TAG_NAME, "h1")
    assert h1_tag.text == title


@then("the homepage table should have the following headers")
def step_check_table_headers(context):

    headers = context.browser.find_elements(By.TAG_NAME, "th")

    assert context.table[0][0] == headers[0].text
    assert context.table[1][0] == headers[1].text
    assert context.table[2][0] == headers[2].text
    assert context.table[3][0] == headers[3].text
    assert context.table[4][0] == headers[4].text
    assert context.table[5][0] == headers[5].text
    assert context.table[6][0] == headers[6].text.replace("\n", " ")
    assert context.table[7][0] == headers[7].text


@then("the homepage table should have 8 headers in total")
def step_and_the_table_should_have_8_headers(context):
    headers = context.browser.find_elements(By.TAG_NAME, "th")
    assert len(headers) == 8


@then("the table data should be accurate")
def step_check_table_data(context):
    table = context.browser.find_element(By.ID, "data")
    cells = table.find_elements(By.TAG_NAME, "td")
    assert len(cells[0].text) == 12
    assert isinstance(cells[1].text, (str, int))
    assert cells[2].text in ["Free-Standing", "Single-Connected", "Dual-Connected"]
    assert cells[3].text in ["Brick Or Block Or Stone", "Concrete"]
    assert isinstance(float(cells[4].text), float) or isinstance(
        int(cells[4].text), int
    )
    assert isinstance(cells[5].text, str)
    assert cells[6].text in ["0", "1", "2", "3"]
    assert cells[7].text == "See more details"


@then("the table should display more than 1 properties")
def step_check_multiple_properties(context):

    table = context.browser.find_element(By.ID, "data")
    rows = table.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 2

