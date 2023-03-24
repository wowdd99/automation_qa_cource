import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    webdriver.Chrome(ChromeDriverManager().install())
    options = Options()
    options.add_argument("user-data-dir=С:\\profile")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
