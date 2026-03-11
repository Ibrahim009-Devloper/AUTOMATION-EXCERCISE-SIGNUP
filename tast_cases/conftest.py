import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def setup():
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_option)
    driver.implicitly_wait(20)
    yield driver

    driver.quit()
