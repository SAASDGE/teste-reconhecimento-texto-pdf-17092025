import pdfplumber
import re
import pandas as pd

#############################
# Abre o PDF e extrai o texto:
#############################

with pdfplumber.open("fatura_cpfl.pdf") as pdf:
    texto = ""
    for pagina in pdf.pages:
        texto += pagina.extract_text() + "\n"

##############################
# Extração de dados com Regex:
##############################

# Número da instalação: 12385675
# Procura a palavra "INSTALAÇÃO" e captura os 8 dígitos próximos
instalacao = re.search(r"INSTALAÇÃO[\s\S]{0,50}(\d{8})", texto)
instalacao = instalacao.group(1) if instalacao else None

# Mês da fatura: OUT/2023
mes = re.search(r"([A-Z]{3}[/]\d{4})", texto)
mes = mes.group(1) if mes else None

# Tarifa cheia (com impostos): 0,881145 // soma TUSD + TE
tusd = re.search(r"TUSD.*?kWh\s+([\d,\.]+)", texto)
tusd = float(tusd.group(1).replace(',', '.')) if tusd else 0

te = re.search(r"TE.*?kWh\s+([\d,\.]+)", texto)
te = float(te.group(1).replace(',', '.')) if te else 0

tarifa_cheia = tusd + te

# Total Fatura: 219,14
valor_distribuidora = re.search(r"(\d+,\d{2})", texto)
valor_distribuidora = valor_distribuidora.group(1) if valor_distribuidora else None

# Somatório Energia injetada: 1950  // referentes à tarifa TUSD
# Procura linhas com "Injetada" e "TUSD" e soma os valores em kWh
inj_tusd = re.findall(r"Inj.*?TUSD.*?([\d.,]+)\s*kWh", texto, flags=re.IGNORECASE)
energia_injetada = sum(float(x.replace('.', '').replace(',', '.')) for x in inj_tusd)

#######################
# Tabela de informações
#######################

dados = [
    ("Instalacao", instalacao),
    ("Mes", mes),
    ("Tarifa cheia (com impostos)", tarifa_cheia),
    ("Valor da distribuidora", valor_distribuidora),
    ("Somatorio de energia injetada", int(energia_injetada))
]

# 4. Converte em DataFrame e imprimi
resultado = pd.DataFrame(dados)
print (resultado)
