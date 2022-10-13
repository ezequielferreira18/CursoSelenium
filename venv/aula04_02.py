from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def find_by_text(driver, tag, text):
    """ --Encontrar o elemento com o texto 'text'--

    Argumentos:
     - driver: Instância do browser (Chrome)
     - text:  conteúdo que estará na tag
     - tag: onde o texto será buscado
    """
    elements = driver.find_elements(By.TAG_NAME, tag) # Retorna lista, pois há vários elementos com a mesma TAG_NAME
    for e in elements:
        if e.text == text:
            return e

driver.get('http://selenium.dunossauro.live/aula_04_a.html')

element_ddg = find_by_text(driver, 'li', 'DuckDuckGo')
print(element_ddg)
print(element_ddg.text)