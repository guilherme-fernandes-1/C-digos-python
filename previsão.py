import requests
import json

def obter_previsao(cidade, api_key):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    parametros = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt'
    }
    
    response = requests.get(BASE_URL, params=parametros)
    
    if response.status_code == 200:
        dados = response.json()
        
        temperatura = dados['main']['temp']
        condicao_clima = dados['weather'][0]['description']
        humidade = dados['main']['humidity']
        
        print(f"Previsão do tempo para {cidade}:")
        print(f"  Temperatura: {temperatura}°C")
        print(f"  Condição: {condicao_clima.capitalize()}")
        print(f"  Humidade: {humidade}%")
    else:
        print(f"Erro ao obter previsão: {response.status_code}")
        print(response.json()['message'])

cidade_escolhida = input("Digite o nome da cidade: ")
api_key_pessoal = "3d624e3c7bc778943990f210fcde60e4"

obter_previsao(cidade_escolhida, api_key_pessoal)