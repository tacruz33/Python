#Extrair arquivos do site 

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser') # pega e converter o conteúdo para html

noticias = site.find_all('div', attrs={'class' :'feed-post-body'}) # pegar html especifica, attrs  : pega o dado especifico do

for noticias in noticias :
    titulo = noticias.find('a', attrs={'class' : 'feed-post-link gui-color-primary gui-color-hover'})
    print(titulo.text)
    print(titulo['href']) #consigo pegar o link da noticia
    
    subtitulo = noticias.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    if (subtitulo):
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'', titulo['href']])

    print(lista_noticias)
    
news = pd.DataFrame(lista_noticias, columns=['Título','Subtítulo','Link'])

news.to_csv('NoticiasGlobo.csv', index=False)

#print(news)