import pdfplumber
import re
import pandas as pd

pdf_file = 'fatura_cpfl.pdf'
texto_completo = ''

with pdfplumber.open(pdf_file) as pdf:
    primeira_pagina = pdf.pages[0]
    texto_completo = primeira_pagina.extract_text()

# --- DADOS EXTRAÍDOS ---

# 1. Instalação
match = re.search(r'INSTALAÇÃO\s+.*?\n.*?(\d{8})', texto_completo, re.DOTALL)
instalacao = match.group(1) if match else None

# 2. Mês
match = re.search(r'INSTALAÇÃO\s+([A-Z]{3}/\d{4})', texto_completo)
mes = match.group(1) if match else None

# 3. Tarifa Cheia (LÓGICA CORRIGIDA PARA SOMAR TUSD + TE)
tarifa_cheia = None
match_tusd = re.search(r'Energia Ativa Fornecida - TUSD.*?kWh\s+([\d,]+)', texto_completo)
match_te = re.search(r'Energia Ativa Fornecida - TE.*?kWh\s+([\d,]+)', texto_completo)

if match_tusd and match_te:
    valor_tusd = float(match_tusd.group(1).replace(',', '.'))
    valor_te = float(match_te.group(1).replace(',', '.'))
    soma_tarifas = valor_tusd + valor_te

    soma_arredondada = round(soma_tarifas, 6)

    tarifa_cheia = str(soma_arredondada).replace('.', ',')

# 4. Valor da distribuidora
match = re.search(r'Total Consolidado\s+([\d,]+)', texto_completo)
valor_distribuidora = match.group(1) if match else None

# 5. Somatório de energia injetada
padrao_energia_injetada = r'Energ Atv Inj.*?TUSD.*? ([\d\.,]+)\s+kWh'
matches = re.findall(padrao_energia_injetada, texto_completo)
soma_energia_injetada = 0
if matches:
    for valor_str in matches:
        valor_limpo = valor_str.replace('.', '').replace(',', '.')
        soma_energia_injetada += float(valor_limpo)

# --- MONTAGEM DO DATAFRAME ---

lista_para_df = [
    {'Campo': 'Instalação', 'Valor': instalacao},
    {'Campo': 'Mês', 'Valor': mes},
    {'Campo': 'Tarifa cheia (com impostos)', 'Valor': tarifa_cheia},
    {'Campo': 'Valor da distribuidora', 'Valor': valor_distribuidora},
    {'Campo': 'Somatório de energia injetada', 'Valor': int(soma_energia_injetada) if soma_energia_injetada > 0 else 0}
]

df_resultado = pd.DataFrame(lista_para_df)

print("--- INFORMAÇÕES EXTRAÍDAS DA FATURA ---")
print(df_resultado)

# df_resultado.to_csv('resultado_fatura.csv', index=False)