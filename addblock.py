from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=С:\\profile")
driver = webdriver.Chrome(options=options)
