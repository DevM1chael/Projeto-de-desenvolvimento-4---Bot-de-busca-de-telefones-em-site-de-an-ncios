import requests

URL_AUTOMOVEIS = "https://django-anuncios-solyd.com.br/automoveis/"

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(resposta.text)
        else:
            print(f"Erro ao fazer requisição: {resposta.status_code}")      
    except Exception as e:
        print("Erro ao fazer requisição")
        print(e)

buscar(URL_AUTOMOVEIS)
