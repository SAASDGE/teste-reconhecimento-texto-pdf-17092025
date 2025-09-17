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

| Campo                          | Valor    |
| ------------------------------ | -------- |
| Instalação                   | 12385675 |
| Mês                           | OUT/2023 |
| Tarifa cheia (com impostos)    | 0,881145 |
| Valor da distribuidora         | 219,14   |
| Somatório de energia injetada | 1950     |

# Documentação do Teste 1

#### Bibliotecas Utilizadas

* **`pdfplumber`** : Para a leitura e extração de texto do arquivo PDF.
* **`re`** : Para a busca e extração de dados específicos do texto através de expressões regulares.
* **`pandas`** : Para a estruturação e exibição final dos dados em formato de tabela.

#### Passo a Passo da Execução

O processo foi dividido em quatro etapas principais:

1. **Leitura e Extração de Texto do PDF**
   * A biblioteca `pdfplumber` foi utilizada através da função `pdfplumber.open()`.
   * O arquivo `fatura_cpfl.pdf` foi aberto e a função `pagina.extract_text()` foi chamada na primeira página (`pdf.pages[0]`) para converter todo o conteúdo visual em uma única variável de texto (string), que serve como base para as extrações.
2. **Busca de Padrões com Expressões Regulares (Regex)**
   * A biblioteca `re` foi o principal mecanismo para a extração dos dados.
   * **`re.search()`** : Esta função foi usada para a maioria dos campos (`Instalação`, `Mês`, `Valor da distribuidora` e as tarifas TUSD/TE). Ela busca pela primeira ocorrência de um padrão no texto e retorna um objeto de correspondência. A função `.group(1)` foi usada para obter apenas o valor capturado dentro dos parênteses `()` na expressão.
   * **`re.findall()`** : Utilizada especificamente para o `Somatório de energia injetada`. Como era necessário somar múltiplos valores de energia injetada (de diferentes meses), esta função foi usada para encontrar *todas* as ocorrências que correspondiam ao padrão e retorná-las em uma lista.
3. **Tratamento e Cálculos Específicos**
   * **Tarifa Cheia** : Este valor não foi extraído diretamente. Em vez disso, as tarifas TUSD e TE foram extraídas individualmente. Seus valores foram convertidos para números de ponto flutuante (`float`), somados, e o resultado foi arredondado para 6 casas decimais com a função `round()` para corrigir imprecisões numéricas.
   * **Somatório de Energia Injetada** : Os valores retornados por `re.findall()` foram percorridos em um loop. Cada valor foi tratado para remover caracteres de formatação (`.` e `,`) antes de ser convertido para `float` e somado ao total.
4. **Estruturação e Exibição com Pandas**
   * Todos os dados finais foram organizados em uma lista de dicionários, onde cada dicionário representa uma linha da tabela final.
   * A função `pd.DataFrame()` foi utilizada para converter essa lista em uma tabela estruturada (DataFrame).
   * Por fim, a função `print()` aplicada ao DataFrame exibe os resultados de forma organizada e legível no console, cumprindo o requisito de apresentação da atividade.

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

- Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
- Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
- Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
- Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:

1. **Principais Diferenças entre as Faturas `fatura_cemig.pdf` e `fatura_cemig_convencional.pdf`:**
   * A fatura convencional (`fatura_cemig_convencional.pdf`) apresenta um modelo de cobrança mais simples, baseado apenas no consumo de energia elétrica, que é multiplicado por uma tarifa para se chegar ao valor final. Em contrapartida, a `fatura_cemig.pdf` possui uma estrutura de débitos e créditos. Nela, são apresentados tanto a energia consumida da rede quanto os créditos provenientes da energia injetada, que são utilizados para abater o valor a pagar. Essa diferença é refletida nos itens faturados, onde a `fatura_cemig.pdf` exibe termos como "Energia compensada GD II" com valores negativos e na seção "Informações Gerais", que contém o "SALDO ATUAL DE GERAÇÃO", um campo inexistente na fatura convencional.
2. **Descrição dos Termos em "Valores Faturados" da `fatura_cemig.pdf`:**
   * A seção "Valores Faturados" da `fatura_cemig.pdf` detalha o balanço entre o consumo e os créditos de energia. O item "Energia Elétrica" corresponde a uma parcela do consumo faturada diretamente. A "Energia SCEE s/ ICMS" representa a energia consumida da rede que pode ser abatida por créditos. A compensação é evidenciada pelo item "Energia compensada GD II", que é o crédito em valor negativo referente à energia injetada na rede. Adicionalmente, a fatura pode apresentar "Energia comp. adicional", que é um crédito extra para abater outros débitos, e outros valores como o "Bônus Itaipu" e taxas de terceiros, como a Contribuição de Iluminação Pública Municipal.
3. **Informação Mais Importante em "Informações Gerais" na `fatura_cemig.pdf`**:
   * A informação mais importante é o "SALDO ATUAL DE GERAÇÃO: 234,63 kWh", pois representa o total de créditos de energia, medido em kWh, que o consumidor acumulou por ter injetado mais energia na rede do que consumiu. Esse saldo funciona como um "banco de energia" utilizado automaticamente para abater o consumo e reduzir o valor das faturas futuras. Portanto, é o principal indicador para o consumidor acompanhar a o funcionamento do seu sistema de geração e a economia obtida.
4. **Consumo Referente a Julho de 2023 na `fatura_cemig.pdf`**:
   * Conforme a tabela "Histórico de Consumo", o consumo de energia elétrica da instalação referente ao mês de julho de 2023 foi de **199 kWh**.

# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
