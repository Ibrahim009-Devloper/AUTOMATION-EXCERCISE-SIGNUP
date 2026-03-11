import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def setup():
    chrome_option = Options()
    chrome_option.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_option)
    yield driver

    driver.quit()
