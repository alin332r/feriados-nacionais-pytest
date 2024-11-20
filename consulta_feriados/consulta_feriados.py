import requests

def consulta_feriados(ano):
    url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {'erro': 'Não foi possível consultar os feriados.'}

