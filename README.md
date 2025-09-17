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

Bibliotecas utilizadas:
    pdfplumber
    Pandas
    re

    para utilizar a ferramenta basta rodar o código:

        python3 read.py

    para testar com outros arquivos basta informar o caminho como parâmetro 'src' da função.
    a função criada retorna um objeto DataFrame da biblioteca Pandas, portanto, para visualizar a tabela é necessário printar a função sendo chamada, ou exportar para csv ou qualquer outra forma viável para dataframes pandas.

    Note que, devido ao tempo e pressão, a ferramenta foi escrita em cima da estrutura do pdf determinado pelo enunciado do desafio. Utilizar a ferramenta com pdfs com estruturas diferentes muito provavelmente ocasionará em uma saída insatisfatória. 

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:

### 1ª Pergunta:
    - A fatura fatura_cemig apresenta muito mais informações na seção Valores Faturados em comparação à fatura_cemig_convencional.
    - A fatura_cemig apresenta dados referentes à valores compensados por, acredito eu, geração de energia própria, além dos custos da geração própria. 
    - A fatura_cemig também apresenta o saldo atual de geração na seção "Informações Gerais".
    - Conclui-se que a fatura_cemig é a fatura de uma instação participante do Sistema de Compensação de Energia Elétrica, enquanto o cliente da fatura_cemig_convencional não é.
### 2ª Pergunta:
    - Energia Elétrica: Energia elétrica consumida pelo cliente.
    - Energia SCEE s/ ICMS: Energia do Sistema de Compensação de Energia Elétrica isenta do imposto Imposto sobre Circulação de Mercadorias e Serviços.
    - Energia compensada GD II: Energia injetada na rede elétrica pelo sistema de geração de energia do cliente.
    - Energia comp. adicional: Compensação da diferença entre a energia SCEE ISENTA  e a energia compensada GD II. (https://www.cemig.com.br/atendimento/entenda-sua-conta/)
    - Bônus Itaipu art 21 Lei 10438: Repasse ao consumidor do saldo positivo da conta de comercialização da energia produzida pela hidrelétrica. 
    - Ass Combt Câncer (37)3512-1528: Valor de uma assinatura descontada na fatura da conta de energia do cliente.
    - Contrib Ilum Publica Municipal: Valor referente à contribuição com os gastos da iluminação pública municipal.
### 3ª Pergunta:
    - A seção mais importante das Informações Gerais da fatura de uma instalação que participa do SCEE é o 'SALDO ATUAL DE GERAÇÂO' que indica os saldos, em kWh, que a instalação tem como crédito para abatimento das próximas faturas.
### 4º Pergunta:
    - O consumo total pode ser verificado no Histórico de Consumo. O consumo do mês Julho de 2023 foi 199 kWh. O valor também pode ser obtido da soma dos valores de Energia Elétrica e Energia SCEE s/ ICMS na seção Valores Faturados.

# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
