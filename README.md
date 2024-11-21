# Projeto de Testes: Feriados Nacionais - BrasilAPI

Este projeto utiliza a BrasilAPI para realizar testes automatizados em sua funcionalidade de consulta de feriados nacionais e estaduais. 
O objetivo principal é validar o comportamento esperado da API, verificando a integridade e consistência dos dados retornados para diferentes cenários.

## API Utilizada
A API escolhida é a BrasilAPI, que oferece diversos endpoints para acesso a informações públicas no Brasil. O endpoint específico testado é:
`[https://brasilapi.com.br/api/feriados/v1/{ano}]`

## 📋 Descrição da API

A BrasilAPI é uma plataforma que fornece dados úteis através de endpoints RESTful. 
Neste projeto, utilizamos o endpoint [/api/feriados/v1/{ano}] para obter a lista de feriados nacionais de um determinado ano.

Exemplo de requisição:

[GET https://brasilapi.com.br/api/feriados/v1/2024]

Resposta esperada:
`[
  {
    "date": "2024-01-01",
    "name": "Confraternização Universal",
    "type": "national"
  }
]`

##  🛠️ Configuração do Ambiente

###  Instalar o Python
Certifique-se de ter o [Python 3.7] ou superior instalado. Para instalar, siga as instruções oficiais:

[Instalar o Python no Windows]
[Instalar o Python no Mac/Linux]

### Instalar pytest e requests
Execute os seguintes comandos no terminal para instalar o pytest e a requests:

`pip install pytest==7.2.2`
`pip install requests==2.28.1`

Siga os passos abaixo para configurar e rodar os testes:

Clonar o Repositório
`git clone [https://github.com/seu-usuario/feriados-nacionais-pytest.git]`
`cd feriados-nacionais-pytest`

Criar um Ambiente Virtual

`python -m venv venv`
No Linux/Mac, use: `source .env/bin/activate`  
No Windows, use: `venv\Scripts\activate`

Instalar Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. 
Instale-as com o comando:

`pip install -r requirements.txt`

### ⚙️ Como Executar os Testes

Certifique-se de que o ambiente virtual está ativo e que as dependências foram instaladas.
Execute os testes com o comando:

`pytest`

Os resultados dos testes aparecerão no terminal, indicando o sucesso ou falha de cada caso.

## 📊 Testes Implementados

> #### Os seguintes cenários foram testados para garantir a funcionalidade da API
>
> - Status Code: Verifica se a API retorna o status 200 ao consultar um ano válido.
> - Ordem Cronológica: Garante que os feriados retornados estão ordenados por data.
> - Feriados Nacionais e Estaduais: Confirma a presença de feriados nacionais e estaduais, se aplicável.
> - Chaves e Integridade dos Dados: Valida que os feriados retornados incluem as chaves esperadas (name, date, type).
> - Ano com Muitos Feriados: Verifica se o ano retorna mais de 10 feriados.
> - Cenários Negativos:
> - Ano Inválido: Resposta para um ano inexistente (ex.: 9999).
> - URL Inválida: Valida o comportamento ao consultar uma URL incorreta.

## 📷 Execução dos Testes
Os testes foram realizados no terminal. Veja abaixo um exemplo:










