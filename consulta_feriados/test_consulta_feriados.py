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
