'''import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url ="https://portal.inmet.gov.br/dadoshistoricos"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

driver.quit()'''

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

def obter_anos_disponiveis():
    try:
        url = "https://portal.inmet.gov.br/dadoshistoricos"
        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)
        driver.get(url)

        # Aguarda um curto período de tempo para garantir que a página seja totalmente carregada
        time.sleep(3)

        # Encontra o elemento de seleção de anos
        select_element = driver.find_element_by_id("selYear")

        # Obtém todas as opções de anos disponíveis
        anos_disponiveis = [option.get_attribute("value") for option in select_element.find_elements_by_tag_name("option")]

        driver.quit()

        return anos_disponiveis
    except Exception as e:
        print("Erro:", e)
        return None

# Função para exibir os anos disponíveis
def exibir_anos_disponiveis():
    anos = obter_anos_disponiveis()
    if anos is not None:
        if anos:
            print("Anos disponíveis:")
            for ano in anos:
                print(ano)
        else:
            print("Nenhum ano disponível encontrado.")
    else:
        print("Erro ao acessar o site. Verifique sua conexão com a internet.")

# Chama a função para exibir os anos disponíveis
exibir_anos_disponiveis()

