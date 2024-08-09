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
