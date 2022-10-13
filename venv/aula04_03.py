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
     - text: Conteúdo que estará na tag
     - tag: Onde o texto será buscado
    """
    elements = driver.find_elements(By.TAG_NAME, tag) # Retorna lista, pois há vários elementos com a mesma TAG_NAME
    for e in elements:
        if e.text == text:
            return e

driver.get('http://selenium.dunossauro.live/aula_04_b.html')

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']

for n in nome_das_caixas:
    find_by_text(driver, 'div', n).click()
    sleep(0.5)

for n in nome_das_caixas:
    driver.back()
    sleep(0.3)

for n in nome_das_caixas:
    driver.forward()
    sleep(0.2)