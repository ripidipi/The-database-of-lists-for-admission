import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

o = Options()
o.add_experimental_option("detach", True)
url = webdriver.Chrome(options=o)
url.get("https://priem.mai.ru/rating/")
select = url.find_element(By.CSS_SELECTOR,'select')
options = select.find_element(By.CSS_SELECTOR, 'option')
select = Select(select)
select.select_by_value("p20240715140008_1")
