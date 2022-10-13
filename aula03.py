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

for click in range(10):
    ps = driver.find_elements(By.TAG_NAME, 'p')
    a.click()
    print(f'Valor do úlitmo p: {ps[-1].text} X Valor do click: {click}')
    if ps[-1].text == str(click): print(f'Os valores são iguais.')
    else: print('Os valores não são iguais.')

time.sleep(10)