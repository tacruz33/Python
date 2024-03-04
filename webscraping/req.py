
# Requests acessando o site e extraindo dados
import requests

response = requests.get('https://g1.globo.com/')

print(response.status_code)
print (' Header')
print (response.headers)

print('\n  Content(Conteúdo)')
print(response.content) #  extrair conteúdo html