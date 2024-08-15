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
