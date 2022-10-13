from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://selenium.dunossauro.live/aula_04_a.html')

a = driver.find_elements(By.TAG_NAME, 'li')
print(a)
print(len(a))

list_ul = driver.find_element(By.TAG_NAME, 'ul') # 1 - Buscamos a 'ul'
lis = list_ul.find_elements(By.TAG_NAME, 'li') # 2 - Buscamos todos 'li'
print(lis[0].text)
print(lis[1].text)
print(lis[0].find_element('a').text) # 3 - No primeiro 'li' buscamos 'a' e pegamos seu texto



sleep(20)