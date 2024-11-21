# Projeto de Testes: Feriados Nacionais - BrasilAPI

Este projeto utiliza a BrasilAPI para realizar testes automatizados em sua funcionalidade de consulta de feriados nacionais e estaduais. O objetivo principal é validar o comportamento esperado da API, verificando a integridade e consistência dos dados retornados para diferentes cenários.

## 📋 Descrição da API

A BrasilAPI é uma plataforma que fornece dados úteis através de endpoints RESTful. Neste projeto, utilizamos o endpoint:

```bash
/api/feriados/v1/{ano}

Este endpoint retorna a lista de feriados nacionais para um ano específico, possibilitando validações precisas sobre as informações fornecidas.

Exemplo de requisição:

bash
Copiar código
GET https://brasilapi.com.br/api/feriados/v1/2024

Resposta esperada:

json
Copiar código
[
  {
    "date": "2024-01-01",
    "name": "Confraternização Universal",
    "type": "national"
  },
  ...
]

🛠️ Configuração do Ambiente
Instalar o Python
Certifique-se de ter o Python 3.7 ou superior instalado. Para instalar, siga as instruções oficiais:

Instalar o Python no Windows
Instalar o Python no Mac/Linux
Instalar pytest e requests

Execute os seguintes comandos no terminal para instalar o pytest e o requests:

bash
Copiar código
pip install pytest==7.2.2
pip install requests==2.28.1
Essas versões são as que estão sendo utilizadas neste projeto.

Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/feriados-nacionais-pytest.git

cd feriados-nacionais-pytest
Crie um Ambiente Virtual:

bash
Copiar código
python -m venv .env
Ative o Ambiente Virtual:

Windows:
bash
Copiar código
.env\Scripts\activate
Linux/Mac:
bash
Copiar código
source .env/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt


⚙️ Como Executar os Testes


Certifique-se de que o ambiente virtual está ativo e que as dependências foram instaladas.

Execute os testes com o comando:

bash
Copiar código
pytest
Os resultados dos testes aparecerão no terminal, indicando o sucesso ou falha de cada caso.


✅ Testes Implementados


Os seguintes testes foram desenvolvidos para cobrir diferentes cenários e validar a funcionalidade da API:

Testes Positivos:

Testar Status Code: Verifica se a API retorna o status 200 ao consultar um ano válido.
Ordem Cronológica: Garante que os feriados retornados estão ordenados por data.
Feriados Nacionais e Estaduais: Confirma a presença de feriados nacionais e estaduais (se aplicável).
Chaves e Integridade dos Dados: Certifica que cada feriado contém as chaves esperadas (name, date, type) e valida os tipos de feriados.
Ano com Muitos Feriados: Verifica se o ano consultado retorna mais de 10 feriados.

Testes Negativos:

Ano Inválido: Testa a resposta da API para um ano inexistente (ex.: 9999).
URL Inválida: Valida o comportamento da API ao consultar uma URL incorreta.


🖥️ Execução dos Testes


Os testes foram realizados no terminal utilizando a biblioteca pytest. Abaixo estão os prints que mostram a execução e os resultados obtidos:

Print 1: Resultado dos testes positivos e negativos
Print 2: Detalhes da execução dos cenários

markdown
Copiar código



