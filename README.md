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


##  Objetivo
Meu objetivo neste desafio foi desenvolver um script em Python para parsear uma fatura de energia da CPFL em PDF. A meta era extrair dados-chave de forma automatizada e, ao final, estruturar essas informações em um DataFrame do Pandas para fácil manipulação.

### Desafios Encontrados
O principal desafio que encontrei foi a natureza caótica do texto extraído do PDF. A biblioteca pdfplumber lineariza o conteúdo visual, o que gerou alguns obstáculos bem específicos:

- **Dessincronização de Rótulos e Dados**: Percebi rapidamente que a extração quebrava a estrutura visual da fatura. Por exemplo, o número da instalação (12385675) aparecia em uma linha completamente diferente do seu rótulo "INSTALAÇÃO". Por causa disso, uma busca simples pelo rótulo para depois pegar o dado adjacente falhava consistentemente.

- **Concatenação Inesperada de Dados**: Em vários pontos, o texto extraído juntava um código de serviço com sua descrição (ex: 0605Energia). Isso me forçou a criar expressões regulares que não presumi-sem um espaço entre esses elementos, o que tornou a lógica de busca mais complexa.

- **Necessidade de Cálculos Derivados**: Notei que informações cruciais, como a "Tarifa cheia" e o "Somatório de energia injetada", não existiam como valores únicos na fatura. Ficou claro que eu precisaria encontrar os valores componentes e implementar a lógica de cálculo diretamente no script, em vez de apenas extrair um dado pronto.

### Solução Implementada
Para superar esses desafios, utilizei regex, utilizando:

- Âncoras : Em vez de confiar na proximidade do texto, decidi usar "âncoras" – textos que apareciam consistentemente no formato esperado, como o site www.cpfl.com.br ou a unidade kWh. Fiz isso para ter um ponto de partida confiável para buscas, garantindo que o script encontrasse a informação correta independentemente das variações de layout na extração.

- Flexibilização dos Padrões: Para lidar com a concatenação de dados, construí padrões de regex que aceitassem variações, como a presença opcional de números no início das strings (ex: \d*Energia...). Isso tornou o script resiliente a essas inconsistências e menos propenso a falhas.


A Tarifa Cheia é a soma das tarifas TUSD e TE, que são extraídas individualmente.

O Somatório de Energia Injetada é calculado usando re.findall para capturar todos os componentes de injeção e, em seguida, somá-los.

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:
# Resumo das Diferenças Essenciais (Fatura Convencional vs. Geração Distribuída)
A análise comparativa mostra  duas diferenças fundamentais que distinguem uma fatura com Geração Distribuída de uma convencional: a lógica de faturamento e a presença de um saldo de créditos energéticos.

1. Estrutura de Faturamento
Enquanto uma fatura convencional apenas cobra pela energia consumida, a fatura com GD funciona como um balanço entre débitos (consumo) e créditos (energia compensada).


Fatura Convencional: Apresenta somente itens de cobrança, como "Energia Elétrica" e taxas (CIP).


Fatura com GD: Mostra o consumo da rede como uma cobrança ("Energia Elétrica", "Energia SCEE"), mas introduz o conceito de compensação, com itens de valor negativo que abatem a dívida (ex: "Energia compensada GD II").

2.  O Saldo de Créditos Energéticos
A diferença mais significativa para o consumidor é a presença do saldo de geração, uma informação inexistente na fatura comum.



Fatura com GD: Exibe o campo "SALDO ATUAL DE GERAÇÃO" (neste caso, 234,63 kWh). Este é o "banco de créditos" do cliente, indicando a energia acumulada disponível para abater o consumo em meses futuros.




Fatura Convencional: Não possui este campo, pois não há geração de energia para compensar.

3. Interpretação do Consumo Mensal
O valor de consumo do mês (para Julho de 2023, foi de 

199 kWh)  também muda de significado. Em uma fatura normal, ele representa o valor a ser pago. Na fatura com GD, ele representa a "dívida" de energia que será parcialmente ou totalmente quitada pelos créditos de geração existentes.

# Como Executar a Solução (Teste 1)

Para executar o script de extração de dados `read.py`, siga os passos abaixo.

### Pré-requisitos
- Python 3.x instalado.
- O arquivo da fatura `fatura_cpfl.pdf` deve estar no mesmo diretório que o script.

### Instalação das Dependências
O script utiliza as bibliotecas `pandas` e `pdfplumber`. Para instalá-las, execute o seguinte comando no seu terminal:

```bash
pip install pandas pdfplumber
```
Com as dependências instaladas, basta executar o script read.py diretamente pelo terminal:
```bash
python read.py
```
# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
