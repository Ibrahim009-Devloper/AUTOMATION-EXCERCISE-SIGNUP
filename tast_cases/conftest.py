import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def setup():
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()),options=chrome_option)
    driver.implicitly_wait(30)
    yield driver

    driver.quit()
