import requests
import pytest
from consulta_feriados import consulta_feriados  # Importando a função diretamente da pasta consulta_feriados

# Teste 1: Verificar se todos os feriados têm nomes únicos
def test_nomes_unicos():
    feriados = consulta_feriados(2024)
    nomes = [feriado['name'] for feriado in feriados]
    assert len(nomes) == len(set(nomes)), "Existem nomes de feriados duplicados"  # Verifica se há nomes duplicados



