import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://curso-python-selenium.netlify.app/aula_03.html')
time.sleep(1)
a = driver.find_element(By.TAG_NAME, 'a')
p = driver.find_element(By.TAG_NAME, 'p')
p.text
a.text
# Parei em 44m54s da aula 03


time.sleep(10)