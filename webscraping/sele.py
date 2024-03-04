from selenium import webdriver
from time import sleep

navegador  = webdriver.Chrome()

navegador.get("https://portal.inmet.gov.br/dadoshistoricos")

sleep(3)

elemento = navegador.find_element('body')

elemento.send_keyers('ANO')

