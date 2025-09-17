import pdfplumber
import re
import pandas as pd

def extrair_dados_fatura(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ''
        for pagina in pdf.pages:
            texto += pagina.extract_text() + '\n'

    #Extração

    match_instalacao = re.search(r"\n\s*(\d{8})\s*\n", texto)
    numero_instalacao = match_instalacao.group(1) if match_instalacao else None

    match_mes = re.search(r"\b([A-Z]{3}/\d{4})\b", texto)
    mes_fatura = match_mes.group(1) if match_mes else None

    match_tarifas = re.findall(r"Consumo kWh\s+([0-9.,]+)\s+([0-9.,]+)", texto)
    if match_tarifas:
        tusd, te = match_tarifas[0]
        tarifa_cheia = float(tusd.replace(',', '.')) + float(te.replace(',', '.'))
        tarifa_cheia = round(tarifa_cheia, 6)
    else:
        tarifa_cheia = None

    match_dist = re.search(r"Total Distribuidora\s+([0-9.,]+)", texto)
    valor_distribuidora = float(match_dist.group(1).replace(',', '.')) if match_dist else None

    matches_inj = re.findall(r"Energ Atv Inj.*?\s([0-9.,]+)\s*kWh", texto)
    if matches_inj:
        soma = sum(float(v.replace('.', '').replace(',', '.')) for v in set(matches_inj))
        somatorio_energia_injetada = int(round(soma, 0))
    else:
        somatorio_energia_injetada = None

    #DataFrame
    
    dados = {
        'Instalacao': [numero_instalacao],
        'Mes': [mes_fatura],
        'Tarifa cheia (com impostos)': [tarifa_cheia],
        'Valor da distribuidora': [valor_distribuidora],
        'Somatorio de energia injetada': [somatorio_energia_injetada]
    }

    return pd.DataFrame(dados)

if __name__ == "__main__":
    caminho_pdf = "fatura_cpfl.pdf"  
    df_fatura = extrair_dados_fatura(caminho_pdf)
    print(df_fatura.to_string(index=False))
