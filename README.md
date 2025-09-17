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

# 📄 Documentação do Código `read.py`

## 📌 Objetivo
Este script tem como finalidade **extrair informações específicas de uma fatura de energia elétrica em PDF (CPFL)**, estruturando os dados em formato tabular (DataFrame do Pandas).  
As informações extraídas são:

- **Instalação** (número da instalação do cliente)  
- **Mês de referência**  
- **Tarifa cheia (com impostos)**  
- **Valor da distribuidora**  
- **Somatório de energia injetada**  

---

## ⚙️ Estrutura Geral
1. **Leitura do PDF** → Utiliza a biblioteca `pdfplumber` para converter o conteúdo em texto.  
2. **Normalização de números** → Converte valores monetários e de consumo de kWh no formato brasileiro para `float`.  
3. **Funções extratoras** → Regex (expressões regulares) para localizar e processar os valores dentro do texto.  
4. **Agrupamento das informações** → Junta todas as informações relevantes em um dicionário.  
5. **Saída** → Cria um DataFrame (`pandas`) para exibir os resultados.

---

## 🔎 Funções

### `extrair_texto_pdf(caminho_pdf: str) -> str`
- **Descrição:**  
  Lê um arquivo PDF e retorna todo o texto concatenado.  
- **Entradas:**  
  - `caminho_pdf` → caminho do arquivo PDF da fatura.  
- **Saída:**  
  - String contendo o texto do PDF.  
- **Detalhes:**  
  Usa `pdfplumber` para iterar sobre todas as páginas e aplicar `extract_text()`.

---

### `normalizar_numero(valor: str) -> float`
- **Descrição:**  
  Converte valores numéricos no padrão brasileiro (com vírgula decimal e ponto de milhar) em `float`.  
- **Entradas:**  
  - `valor` → string representando um número (ex: `"1.165,120"`).  
- **Saída:**  
  - `float` correspondente (ex: `1165.120`).  
- **Tratamento de erros:**  
  Caso não consiga converter, retorna `None` e gera um log de aviso.

---

### `extrair_instalacao(texto: str) -> str`
- **Descrição:**  
  Localiza o número de **instalação** no texto da fatura.  
- **Regex usada:**  
  ```regex
  INSTALAÇÃO[\s\S]{0,100}?(\d{7,10})
  ```
- **Saída:**  
  - Número da instalação como `string`.

---

### `extrair_mes_referencia(texto: str) -> str`
- **Descrição:**  
  Localiza o **mês/ano de referência** da fatura (ex: `OUT/2023`).  
- **Regex usada:**  
  ```regex
  \b([A-Z]{3}/\d{4})\b
  ```
- **Saída:**  
  - Mês/ano no formato `MMM/YYYY`.

---

### `extrair_tarifa_cheia(texto: str) -> float`
- **Descrição:**  
  Calcula a **tarifa cheia (com impostos)** a partir das linhas de *Energia Ativa Fornecida*.  
- **Processo:**  
  - Extrai a quantidade de energia (kWh) e o valor total (R$).  
  - Divide o valor total pela quantidade → tarifa unitária.  
  - Retorna a média ponderada das tarifas.  
- **Saída:**  
  - Valor `float` arredondado com 6 casas decimais.

---

### `extrair_valor_distribuidora(texto: str) -> float`
- **Descrição:**  
  Captura o **Total Consolidado** da fatura (valor final da distribuidora).  
- **Regex usada:**  
  ```regex
  Total Consolidado\s+([\d.,]+)
  ```
- **Saída:**  
  - Valor em `float`.

---

### `extrair_energia_injetada(texto: str) -> float`
- **Descrição:**  
  Calcula o **somatório da energia injetada** (energia devolvida pelo consumidor à rede).  
- **Processo:**  
  - Busca linhas de energia injetada por mês/ano.  
  - Garante que cada mês seja contado apenas uma vez (evitando duplicações TUSD/TE).  
  - Soma os valores.  
- **Regex usada:**  
  ```regex
  Inj[^\n\r]*?([A-Z]{3}/\d{2,4})\s+(\d{1,3}(?:\.\d{3})*,\d{2,3})\s*kWh
  ```
- **Saída:**  
  - Valor inteiro representando o total injetado.

---

### `extrair_informacoes(texto: str) -> dict`
- **Descrição:**  
  Centraliza a extração chamando todas as funções anteriores.  
- **Saída:**  
  - Dicionário com as informações:  
    ```python
    {
        "Instalação": ...,
        "Mês": ...,
        "Tarifa cheia (com impostos)": ...,
        "Valor da distribuidora": ...,
        "Somatório de energia injetada": ...
    }
    ```

---

### `main()`
- **Descrição:**  
  Função principal do script.  
- **Processo:**  
  1. Define o caminho do PDF.  
  2. Extrai o texto.  
  3. Obtém os dados processados.  
  4. Cria um DataFrame com `pandas`.  
  5. Imprime os resultados no console.  

---

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:
- Escreva suas respostas para o teste 2 abaixo.

# Análise Detalhada da Fatura de Energia com Geração Distribuída

### 1. Principais diferenças entre a fatura de Geração Distribuída e a Convencional

[cite_start]A diferença fundamental é que a "fatura_cemig.pdf" é de uma unidade consumidora que participa do Sistema de Compensação de Energia Elétrica (Geração Distribuída)[cite: 112, 114], enquanto a "fatura_cemig_convencional.pdf" é de um consumidor padrão. Isso se reflete em:

* [cite_start]**Itens de Faturamento**: A fatura com Geração Distribuída detalha itens de crédito e débito relacionados à energia gerada, como "Energia SCEE s/ ICMS" [cite: 79][cite_start], "Energia compensada GD II" [cite: 85] [cite_start]e "Energia comp. adicional"[cite: 91]. [cite_start]A fatura convencional possui uma estrutura mais simples, mostrando apenas o consumo de "Energia Elétrica" [cite: 23] [cite_start]e a "Contrib Ilum Publica Municipal"[cite: 23].
* [cite_start]**Informações sobre Geração**: A fatura "fatura_cemig.pdf" contém informações específicas para quem gera energia, como a menção explícita de que a "Unidade faz parte de sistema de compensação de energia" [cite: 114] [cite_start]e o "SALDO ATUAL DE GERAÇÃO: 234,63 kWh"[cite: 112]. Essas informações são ausentes na fatura convencional.
* [cite_start]**Itens Adicionais**: A fatura com geração distribuída pode incluir outros créditos, como o "Bônus Itaipu" [cite: 97][cite_start], e débitos de terceiros, como doações[cite: 99], que não estão presentes na fatura convencional analisada.

### 2. Detalhamento dos "Valores Faturados" ("fatura_cemig.pdf")

[cite_start]A seção "Valores Faturados" da "fatura_cemig.pdf" detalha os componentes que formam o total a pagar de R$ 76,66[cite: 104]. São eles:

* [cite_start]**Energia Elétrica**: Refere-se a um consumo de 50 kWh [cite: 75] [cite_start]faturado pela tarifa cheia, resultando em um débito de R$ 47,96[cite: 77].
* [cite_start]**Energia SCEE s/ ICMS**: Corresponde a 149 kWh [cite: 81] [cite_start]do consumo que é compensado pelos créditos de geração, com um valor de R$ 76,26[cite: 83].
* [cite_start]**Energia compensada GD II**: É o crédito em reais pela injeção de 149 kWh [cite: 87] [cite_start]na rede da distribuidora, que abate **-R$ 67,24** da conta[cite: 89].
* [cite_start]**Energia comp. adicional**: Um crédito adicional referente a 7 kWh [cite: 93][cite_start], que resulta em um abatimento de **-R$ 5,24**[cite: 95].
* [cite_start]**Bônus Itaipu**: Um benefício creditado na fatura, gerando um desconto de **-R$ 9,79**[cite: 98].
* [cite_start]**Ass Combt Câncer**: Uma doação a uma instituição, debitada no valor de R$ 10,00[cite: 100].
* [cite_start]**Contrib llum Publica Municipal**: A taxa para o custeio do serviço de iluminação pública municipal, no valor de R$ 24,71[cite: 102].

### 3. Informação mais importante na seção "Informações Gerais"

[cite_start]Considerando que a instalação participa do Sistema de Compensação de Energia Elétrica, a informação mais importante na seção "Informações Gerais" é o **"SALDO ATUAL DE GERAÇÃO: 234,63 kWh"**[cite: 112].

**Explicação**: Este saldo representa o "banco de horas" de energia. É a quantidade de créditos em kWh que o consumidor acumulou por gerar mais energia do que consumiu e que poderá ser utilizada para abater o consumo dos meses seguintes. Para o proprietário do sistema, este é o principal indicador para acompanhar a performance da geração e a economia obtida.

### 4. Consumo da instalação em julho de 2023

[cite_start]O consumo da instalação referente ao mês de julho de 2023 foi de **199 kWh**[cite: 106, 109]. Esta informação pode ser verificada em dois locais na fatura "fatura_cemig.pdf":

* [cite_start]Na tabela "Histórico de Consumo", na linha correspondente ao MÊS/ANO "JUL/23"[cite: 106].
* [cite_start]Na tabela "Informações Técnicas", como o "Consumo. kWh", calculado pela diferença entre a "Leitura Atual" (421) e a "Leitura Anterior" (222)[cite: 109].

# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
