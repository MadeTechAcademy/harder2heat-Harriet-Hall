from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('I am on the property page')
def step_given_i_am_on_the_property_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://127.0.0.1:5000")
    context.browser.implicitly_wait(10)
    button = context.browser.find_element(By.TAG_NAME, "a")
    button.click()

@then('the page header should be the uprn of the property')
def step_then_page_header_should_be_the_uprn_of_the_property(context):

        h2_tag = context.browser.find_element(By.TAG_NAME, "h2")
        h2 = h2_tag.text[6:]
        assert len(h2) == 12
        assert h2 in context.browser.current_url

@then('the property table should have the following headers')
def step_then_table_should_have_headers(context):

    headers = context.browser.find_elements(By.TAG_NAME, "th")

    assert context.table[0][0] == headers[0].text
    assert context.table[1][0] == headers[1].text
    assert context.table[2][0] == headers[2].text
    assert context.table[3][0] == headers[3].text
    assert context.table[4][0] == headers[4].text
    assert context.table[5][0] == headers[5].text
    assert context.table[6][0] == headers[6].text.replace("\n", "")

@then('the property table should have 8 headers in total')
def step_and_the_table_should_have_8_headers(context):
    headers = context.browser.find_elements(By.TAG_NAME, "th")
    assert len(headers) == 8
    
@then('the table should display valid property data')
def step_then_table_should_display_valid_property_data(context):

        cells = context.browser.find_elements(By.TAG_NAME, "td")

        assert type(cells[0].text) == str
        assert type(cells[1].text) in [str, int]
        assert type(cells[2].text) == str
        assert cells[3].text in ["Free-Standing", "Single-Connected", "Dual-Connected"]
        assert cells[4].text in ["Brick Or Block Or Stone", "Concrete"]
        assert type(float(cells[5].text)) in [float, int]
        assert type(cells[6].text) == str
        assert cells[7].text in ["0", "1", "2", "3"]

