from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

navegador = webdriver.Chrome()

def responder_aleatorio(): 
    navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe4TH9w4pHHgmeNsF7b785B8dJ7E0NjbD57Yyjxjm16NnKJZg/viewform")
    assert "SmooLife 🍒" in navegador.title

    esperar = WebDriverWait(navegador, 10)

    checkboxes = esperar.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".docssharedWizToggleLabeledContainer"))
    )

    checkboxes_validos = []
    for checkbox in checkboxes:
        texto = checkbox.text.lower()
        excluir = ["outro"]

        if not any(palavra in texto for palavra in excluir):
            checkboxes_validos.append(checkbox)
        else: 
            print(f'Opção excluída: {checkbox.text}')

    if checkboxes_validos:
        numero_selecoes = random.randint(1, len(checkboxes_validos))
        checkboxes_aleatorios = random.sample(checkboxes_validos, numero_selecoes)

        for checkbox in checkboxes_aleatorios:
            checkbox.click()
            print(f"Selecionado: {checkbox.text}")

if __name__ == "__main__":
    for i in range(1):  
        responder_aleatorio()
        botao_enviar = navegador.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
        botao_enviar.click()



