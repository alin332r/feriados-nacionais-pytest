# Projeto de Testes: Feriados Nacionais - BrasilAPI

Este projeto utiliza a BrasilAPI para realizar testes automatizados em sua funcionalidade de consulta de feriados nacionais e estaduais. O objetivo principal é validar o comportamento esperado da API, verificando a integridade e consistência dos dados retornados para diferentes cenários. Além disso, o projeto visa garantir que a API esteja sempre atualizada com as datas corretas dos feriados, 
proporcionando uma fonte confiável de informações para os usuários.

## API Utilizada

A API escolhida é a BrasilAPI, que oferece diversos endpoints para acesso a informações públicas no Brasil. O endpoint específico testado é: 
[https://brasilapi.com.br/api/feriados/v1/{ano}]. Este endpoint permite a consulta de feriados nacionais e estaduais para um ano específico, 
retornando uma lista detalhada com as datas e descrições dos feriados.

## Principais Funcionalidades da API

- Consulta de Feriados Nacionais: Retorna uma lista de todos os feriados nacionais para o ano especificado.
* Consulta de Feriados Estaduais: Permite a consulta de feriados específicos de cada estado, proporcionando uma visão completa dos feriados em todo o Brasil.
+ Formato de Resposta: A API retorna os dados em formato JSON, facilitando a integração com diversas aplicações e sistemas.


## 📋 Descrição da API

A BrasilAPI é uma plataforma que fornece dados úteis através de endpoints RESTful. Neste projeto, utilizamos o endpoint `[/api/feriados/v1/{ano}]`
para obter a lista de feriados nacionais de um determinado ano. A API é projetada para ser fácil de usar e integrar, oferecendo respostas rápidas e precisas.

## Benefícios da Utilização da BrasilAPI

- Atualização Constante: A API é mantida e atualizada regularmente para garantir que as informações estejam sempre corretas.
* Facilidade de Integração: Com respostas em JSON, a integração com outras aplicações é simplificada.
+ Confiabilidade: A BrasilAPI é uma fonte confiável de informações públicas, utilizada por diversas aplicações e serviços no Brasil.

### Exemplo de Requisição

Aqui está um exemplo de como fazer uma requisição para o endpoint de feriados:

` GET `"https://brasilapi.com.br/api/feriados/v1/2024"

### Respostas esperadas:

<pre>
<code>
[
  {
    "date": "2024-01-01",
    "name": "Confraternização Universal",
    "type": "national"
  },
  {
    "date": "2024-04-21",
    "name": "Tiradentes",
    "type": "national"
  },
  {
    "date": "2024-05-01",
    "name": "Dia do Trabalhador",
    "type": "national"
  }
]
</code>
</pre>


##  🛠️ Configuração do Ambiente

## Instalar o Python
Certifique-se de ter o [Python 3.7] ou superior instalado. Para instalar, siga as instruções oficiais:

[Instalar o Python no Windows]
>
[Instalar o Python no Mac/Linux]

## Instalar pytest e requests
Execute os seguintes comandos no terminal para instalar o pytest e a requests:

`pip install pytest==7.2.2`
>
`pip install requests==2.28.1`  

Siga os passos abaixo para configurar e rodar os testes:

## Clonar o Repositório
git clone 
>
[https://github.com/seu-usuario/feriados-nacionais-pytest.git]
>
`cd feriados-nacionais-pytest`

### Criar um Ambiente Virtual

`python -m venv venv`
>
No Linux/Mac, use: `source .env/bin/activate`
>
No Windows, use: `venv\Scripts\activate`
>

###  Instalar Dependências
>
As dependências do projeto estão listadas no arquivo requirements.txt.
> 
Instale-as com o comando:

`pip install -r requirements.txt`

### ⚙️ Como Executar os Testes

Certifique-se de que o ambiente virtual está ativo e que as dependências foram instaladas.
>
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

Os testes foram realizados no terminal. Veja alguns exemplos:

A imagem mostra o terminal com os seguintes passos executados:
1. Acesso à pasta `feriados-nacionais-pytest` com o comando `cd`.
2. Ativação do ambiente virtual com o comando `venv\Scripts\activate`.
3. Execução do comando `pytest`, que coletou dois testes no arquivo `test_consulta_feriados.py`.
Os dois testes passaram com sucesso, com uma execução de 2.08 segundos e 100% de aprovação.

![Captura de tela do terminal com execução do pytest mostrando dois testes passados](https://github.com/user-attachments/assets/c1d775a1-00bc-48b0-93bf-2a20a66e5477)


A imagem mostra o terminal com os seguintes comandos Git executados:

1. **Adição do arquivo** `consulta_feriados/test_consulta_feriados.py` ao estágio de commit usando `git add`.
2. **Verificação do status** do Git com o comando `git status`, mostrando que o arquivo foi modificado e está pronto para ser comitado.
3. **Commit das alterações** com a mensagem "Adicionado teste para verificar feriados nacionais e estaduais", utilizando o comando `git commit -m`.
4. **Push das alterações** para o repositório remoto no GitHub com o comando `git push origin main`, atualizando a branch principal com as mudanças.

O processo foi concluído com sucesso, e o commit foi enviado para o repositório remoto.

![Captura de tela do terminal com execução de comandos Git para commit e push](https://github.com/user-attachments/assets/6eae5b1b-8db1-4ada-a716-f0b242969e08)


A imagem mostra a execução de vários testes utilizando o `pytest` com diferentes comandos:

1. **Execução do teste `test_status_code_200`**: O comando `pytest -v -k "test_status_code_200"` foi executado, e o teste passou com sucesso em 0.89 segundos.
2. **Execução do teste `test_ordem_cronologica`**: O comando `pytest -v -k "test_ordem_cronologica"` foi executado, e o teste também passou com sucesso em 0.87 segundos.
3. **Execução do teste `test_feriados_nacionais_estaduais`**: O comando `pytest -v -k "test_feriados_nacionais_estaduais"` foi executado, e o teste passou com sucesso em 0.91 segundos.
4. **Execução do teste `test_chaves_e_feriados`**: A captura de tela também mostra a preparação para rodar o teste `test_chaves_e_feriados`, mas o comando está em execução.

Em todos os casos, os testes foram bem-sucedidos, com todos passando sem falhas, indicando a validade das funcionalidades testadas.

![Captura de tela do terminal mostrando a execução de vários testes com pytest](https://github.com/user-attachments/assets/edae0856-0c0d-48a5-87c4-d74221418954)


A imagem mostra a execução de vários testes utilizando o `pytest` com diferentes comandos:

1. **Execução do teste `test_chaves_e_feriados`**: O comando `pytest -v -k "test_chaves_e_feriados"` foi executado e o teste passou com sucesso em 0.94 segundos.
2. **Execução do teste `test_ano_com_muitos_feriados`**: O comando `pytest -v -k "test_ano_com_muitos_feriados"` foi executado e o teste também passou com sucesso em 0.94 segundos.
3. **Execução do teste `test_ano_invalido`**: O comando `pytest -v -k "test_ano_invalido"` foi executado e o teste passou com sucesso em 0.84 segundos.
4. **Execução do teste `test_url_invalida`**: O comando `pytest -v -k "test_url_invalida"` foi executado e o teste passou com sucesso.

Em todos os casos, os testes foram bem-sucedidos, sem falhas, mostrando que as funcionalidades relacionadas aos testes foram validadas corretamente.

![Captura de tela do terminal mostrando a execução de testes com pytest](https://github.com/user-attachments/assets/4854256b-1e51-492f-8286-9bb1c3bf5700)













