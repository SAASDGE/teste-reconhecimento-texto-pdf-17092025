# Teste Técnico (Extração de informações em Faturas de Energia)

Para garantir o eficiente gerenciamento dos créditos de energia provenientes de usinas de energia renovável, é fundamental a extração precisa e automática de dados das notas fiscais de energia elétrica. Além disso, possuir conhecimento sobre faturas de energia elétrica é importante para o sucesso na gestão desses recursos.

Logo, é proposto dois testes como parte da avaliação dos conhecimentos técnicos e teóricos dos candidatos. Essa avaliação tem o objetivo de medir a compreensão do participante no contexto da extração de dados de notas fiscais e no entendimento básico de faturas de energia elétrica.

# Teste 1

Em busca pela eficiência na leitura de faturas, a equipe de desenvolvimento propõe a criação de uma rotina que, a partir de faturas de energia elétrica em formato de PDF, seja capaz de extrair importantes informações.

Nesta atividade, você deve editar o arquivo read.py e desenvolver uma rotina capaz de realizar a leitura da fatura fatura_cpfl.pdf em formato de PDF e retornar um dataframe contendo as seguintes informações:

- O número da instalação
- Mês ao qual a fatura é referente
- Tarifa cheia (com impostos)
- Valor da distribuidora
- Somatório das componentes de energia injetada

Ao desenvolver a atividade deve ser realizada a leitura do arquivo, extração do texto e por fim análise dos dados. Para a extração de textos dos PDFs, é sugerido o uso da biblioteca pdfplumber. Além disso, para a extração de informações do texto é sugerido o uso de expressões regulares a partir da biblioteca re, e com o objetivo de organizar e visualizar as informações é sugerido o uso da biblioteca pandas. 

As informações obtidas devem ser exibidas e estruturadas de acordo com a seguinte tabela, além disso é possível observar o gabarito da atividade.

|                 Campo                |    Valor    | 
|--------------------------------------|-------------|
|              Instalação              |   12385675  |
|                   Mês                |   OUT/2023  |
|      Tarifa cheia (com impostos)     |   0,881145  |
|         Valor da distribuidora       |    219,14   |
|    Somatório de energia injetada     |     1950    |

# Documentação do Teste 1

- Escreva a documentação do teste 1 abaixo.

## Descrição do Problema :
A partir de uma fatura de energia em PDF, deve ser possível extrair os seus dados como : Numero de Instalação, Mês da Fatura, Tarifa Cheia, Valor da distribuidora, Somatório das componentes de energia injetada

## Solução : 
Para a solução desse problema utilizei as bibliotecas como pdfplumber (bilioteca recomendada) para a leitura e extração do texto do PDF, essa biblioteca consegue fazer um bom parse do problema de uma forma simples, além disso utilizei a Expressões regulares onde achei possível para extrair o texto de uma forma rápida, no fim, para uma apresentação dos dados utilizei um DataFrame do Pandas para manter uma boa organização e leitura

## Python e Bibliotecas

Python - 3.13

pdfplumber - 0.11.7

pandas - 2.3.2

## Como executar :
No diretório do projeto : 

1. Criar o ambiente virtual:
```bash
python -m venv venv
```
2. Ativar o ambiente:

```bash
venv\Scripts\activate
```
3. Instalar as dependencias
```bash
pip install pandas pdfplumber
```
4. Executar o projeto
```bash
python read.py
```
# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:
- Como principais diferenças entra as duas faturas eu pude indentificar : Na fatura_cemig existem campos adicionais na tabela "Valores Faturados", como "Energia compensada GD II" e "Energia SCEE s/ ICMS", o que não existe na fatura_cemig_convencional, além disso também pude identificar uma mudança de "Bifasico" para "Monofasico" na fatura_cemig_convencional.Uma outra mudança é o "SALDO ATUAL DE GERAÇÃO: 234,63 kWh" presente na fatura_cemig
- Na fatura_cemig possui termos diferentes como Energia compensada GD II, esses termos significam : 
  * Energia Compensada GD II : A Geração Distribuída(GD) é um termo para pessoas que possuem uma fonte de energia em casa, e compartilham sua energia com a distribuidora, tendo então tanto um consumo próprio, quanto um distribuído, ele recebe uma compensação por isso, como na fatura possui o valor -67,24
  * Energia SCEE s/ ICMS : Esse termo é a energia que é compartilhada com a concessionária de energia sem os impostos de ICMS
  * Energia comp. adicional : Esse adicional é uma energia que é compensada além daquela produzida pela pessoa, podendo assim gerar um desconto na sua fatura final
  * Bônus Itaipu art 21 Lei 10438 : É um bônus que pode gerar um desconto na fatura final do cliente, com relação a usina de Itaipu
- A informação mais importante pode ser a frase "Unidade faz parte de sistema de compensação de energia", o que nos diz que essa pessoa participa do Sistema de Compensação, além do início do parágrafo com o seu saldo atual de geração
- O consumo referente ao mês de Julho de 2023 foi de 199 kWh na fatura_cemig


# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
