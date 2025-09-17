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

## Instruções para execução do código

1. **Clonar repositório**: 
   ```bash
   git clone https://github.com/SAASDGE/teste-reconhecimento-texto-pdf-17092025.git
   ```
2. **Navegar até o diretório do projeto**:
   ```bash
   cd teste-reconhecimento-texto-pdf-17092025
    ```
3. **Criar e ativar um ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Se no Windows use `venv\Scripts\activate`
    ```
4. **Instalar as dependências necessárias**:
   ```bash
    pip install -r requirements.txt
   ```
5. **Executar o script**:
   ```bash
   python read.py
   # Opcionalmente:
   python3 read.py
   ```  

# Teste 2

Contexto: Você recebeu a fatura "fatura_cemig.pdf" e deve desenvolver um script para extrair seus dados. Antes de iniciar a programação, é essencial compreender e interpretar as informações presentes nesta fatura.

Atividade: Analise a fatura e redija um documento respondendo os pontos abaixo. As respostas podem ser inseridas neste 'README'.

 - Identifique as principais diferenças entre a fatura "fatura_cemig.pdf" e uma fatura convencional de energia elétrica "fatura_cemig_convencional.pdf".
 - Descreva e explique os termos e valores apresentados na seção "Valores Faturados" da fatura "fatura_cemig.pdf".
 - Considerando que a instalação da "fatura_cemig.pdf" participa do Sistema de Compensação de Energia Elétrica, identifique e explique qual informação na seção "Informações Gerais" da fatura é considerada a mais importante.
 - Identifique o consumo da instalação referente ao mês de julho de 2023.

Respostas teste 2:

### 1. 
A fatura convencional (`fatura_cemig_convencional.pdf`) apresenta apenas itens básicos em “Valores Faturados” como consumo de energia elétrica em kWh, contribuição de iluminação pública e o total a ser pago.
A fatura `fatura_cemig.pdf` possui outros itens relacionados ao SCEE, como “Energia SCEE s/ ICMS”, “Energia compensada GD II”, “Energia comp. adicional”, bônus Itaipu por lei e saldo de geração (na sessão “Informações Técnicas”). Ou seja, enquanto `fatura_cemig_convencional.pdf` reflete apenas o consumo, a fatura `fatura_cemig.pdf` detalha créditos e compensações de energia.

### 2. 
Na `fatura_cemig.pdf`, a seção “Valores Faturados” mostra diferentes componentes: “Energia Elétrica” é consumo efetivo de energia em kWh, “Energia SCEE s/ ICMS” é energia usada sujeita ao sistema de compensação, “Energia SCEE s/ ICMS” é energia compensada, pode-se dizer "devolvida" ao sistema, “Energia comp. adicional” é um termo que a CEMIG usa para indicar compensação extra, “Bônus Itaipu art 21 Lei 10438” é um bônus previsto em lei decorrente da geração de energia pela Usina de Itaipu para consumidores do estado de Minas Gerais, “Ass Combt Câncer (37)3512-1528” é uma taxa externa cobrada na fatura por escolha do cliente, e “Contribuição de Iluminação Pública” é uma cobrança obrigatória para a manutenção da iluminação pública. Todos esses itens revelam como o consumo bruto, descontos por geração própria e os créditos de energia que mudam o valor final a ser pago, barateando a conta.

### 3. 
Na fatura `fatura_cemig.pdf`, a informação mais relevante em “Informações Gerais” é o “SALDO ATUAL DE GERAÇÃO: 234,63 kWh”, pois indica o crédito acumulado de energia da unidade consumidora no sistema de compensação. Esse saldo define quanto de energia gerada e não consumida poderá ser usado para abater valores em contas futuras, sendo essencial para a gestão dos benefícios do SCEE.

### 4. 
De acordo com o histórico de consumo da fatura `fatura_cemig.pdf`, o consumo registrado em **julho de 2023 foi de 199 kWh**. Esse valor corresponde ao uso líquido da instalação no período de 31 dias e serve de base para o cálculo dos créditos e compensações de energia daquele mês.



# Requisitos dos Desafios:

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
