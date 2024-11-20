import requests
import pytest
from consulta_feriados import consulta_feriados  # Importando a função diretamente da pasta consulta_feriados

# Teste 1: Verificar se todos os feriados têm nomes únicos
def test_nomes_unicos():
    feriados = consulta_feriados(2024)
    nomes = [feriado['name'] for feriado in feriados]
    assert len(nomes) == len(set(nomes)), "Existem nomes de feriados duplicados"  # Verifica se há nomes duplicados


# Teste 2: Verificar se a resposta contém feriados em ordem cronológica
def test_ordem_cronologica():
    feriados = consulta_feriados(2024)
    datas = [feriado['date'] for feriado in feriados]
    assert datas == sorted(datas), "Os feriados não estão em ordem cronológica"  # Verifica se as datas estão ordenadas
    
    
# Teste 3: Verificar se a resposta contém feriados nacionais e estaduais
def test_feriados_nacionais_estaduais():
    feriados = consulta_feriados(2024)
    
    # Filtra os feriados nacionais
    feriados_nacionais = [feriado for feriado in feriados if feriado['type'] == 'national']
    # Filtra os feriados estaduais
    feriados_estaduais = [feriado for feriado in feriados if feriado['type'] == 'state']
    
    # Verifica se há pelo menos um feriado nacional
    assert len(feriados_nacionais) > 0, "Nenhum feriado nacional encontrado"
    
    # Verifica se há pelo menos um feriado estadual (condicional)
    if feriados_estaduais:
        
        assert len(feriados_estaduais) > 0, "Nenhum feriado estadual encontrado"
        
        
# Teste 4: Verificar se todos os feriados contêm as chaves esperadas
def test_chaves_esperadas():
    # Consulta os feriados para o ano de 2024
    feriados = consulta_feriados(2024)
    
    # Itera sobre cada feriado na lista de feriados
    for feriado in feriados:
        # Verifica se a chave 'name' está presente no dicionário do feriado
        assert 'name' in feriado, "A chave 'name' não está presente no feriado"
        # Verifica se a chave 'date' está presente no dicionário do feriado
        assert 'date' in feriado, "A chave 'date' não está presente no feriado"