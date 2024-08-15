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
