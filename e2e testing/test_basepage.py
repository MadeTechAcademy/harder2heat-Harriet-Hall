import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_title(browser):
    assert browser.title == "Harder to Heat Homes"  

def test_base_page_has_correct_gov_uk_content(browser):
    assert browser.find_element(By.CLASS_NAME, "govuk-header__logotype").text == "GOV.UK"
    assert browser.find_element(By.CLASS_NAME, "govuk-footer__licence-description").text == "All content is available under the Open Government Licence v3.0, except where otherwise stated"
