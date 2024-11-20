import requests
import pytest
from consulta_feriados import consulta_feriados  # Importa a função de consulta de feriados

# Teste 1: Verificar se a requisição retorna status code 200
def test_status_code_200():
    response = requests.get('https://brasilapi.com.br/api/feriados/v1/2024')
    assert response.status_code == 200, "O status code não é 200"  # Verifica se a resposta é OK

# Teste 2: Verificar se a resposta contém feriados em ordem cronológica
def test_ordem_cronologica():
    feriados = consulta_feriados(2024)
    datas = [feriado['date'] for feriado in feriados]
    assert datas == sorted(datas), "Os feriados não estão em ordem cronológica"  # Verifica se as datas estão ordenadas
    
# Teste 3: Verificar se a resposta contém feriados nacionais e estaduais
def test_feriados_nacionais_estaduais():
    feriados = consulta_feriados(2024)
    feriados_nacionais = [feriado for feriado in feriados if feriado['type'] == 'national']
    feriados_estaduais = [feriado for feriado in feriados if feriado['type'] == 'state']
    
    assert len(feriados_nacionais) > 0, "Nenhum feriado nacional encontrado"  # Verifica feriados nacionais
    if feriados_estaduais:
        assert len(feriados_estaduais) > 0, "Nenhum feriado estadual encontrado"  # Verifica feriados estaduais
        
# Teste 4: Verificar se todos os feriados contêm as chaves esperadas
def test_chaves_e_feriados():
    feriados = consulta_feriados(2024)
    for feriado in feriados:
        assert 'name' in feriado, "A chave 'name' não está presente"  # Verifica se o nome do feriado está presente
        assert 'date' in feriado, "A chave 'date' não está presente"  # Verifica se a data do feriado está presente
        assert feriado['type'] in ['national', 'state'], "Tipo de feriado inválido"  # Verifica o tipo de feriado

# Teste 5: Verificar se a resposta para um ano com muitos feriados retorna corretamente
def test_ano_com_muitos_feriados():
    feriados = consulta_feriados(2024)
    assert len(feriados) > 10, "O ano 2024 deveria ter mais de 10 feriados"  # Verifica se há mais de 10 feriados

def test_ano_invalido():
    # Faz uma requisição para a API com um ano inválido (9999)
    response = requests.get('https://brasilapi.com.br/api/feriados/v1/9999')
    
    # Verifica se o código de status retornado é 404, indicando que o ano não existe
    assert response.status_code == 404, "A API não retornou erro com ano inválido"  # Ajuste o código para 404

def test_url_invalida():
    # Faz uma requisição para a API com uma URL inválida
    response = requests.get('https://brasilapi.com.br/api/feriados/v1/ano_inexistente')
    
    # Verifica se o código de status retornado é 500, indicando erro interno no servidor
    assert response.status_code == 500, "A API não retornou erro para URL inválida"  # Ajuste o código para 500
