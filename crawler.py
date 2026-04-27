import requests
from bs4 import BeautifulSoup
#||||||||||||||||||||||||||||||||||||||||||||||||||||
# Beautiful Soup é uma biblioteca Python usada para extrair dados de arquivos HTML e XML.
#|||||||||||||||||||||||||||||||||||||||||||||||||||||

URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer a requisição")
    except Exception as error:
        print("Erro ao fazer a requisição")
        print(error)

resposta = buscar(URL_AUTOMOVEIS)
if resposta:
    soup = BeautifulSoup(resposta, 'html.parser')
    print(soup.prettify())