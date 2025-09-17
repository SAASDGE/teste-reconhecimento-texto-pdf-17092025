# Desenvolva aqui sua atividade

import re
import pandas as pd
import pdfplumber

pdf_src = 'fatura_cpfl.pdf'

def pdf_pipeline(src = pdf_src)-> pd.DataFrame:

    pdf_content = pdfplumber.open(src).pages[0].extract_text()
    values = []

    #create dataframe backbone
    df = {
        'Campo': ['Instalação', 'Mês', 'Tarifa cheia (com impostos)', 'Valor da distribuidora', 'Somatório de energia injetada'],
        'Valor': values
    }

    inst_code = re.findall(r'www\.cpfl\.com\.br\s+(\d+)', pdf_content)[0]
    month = re.search(r'[A-Z]{3}/[0-9]{4}', pdf_content).group()
    tariff = re.findall(r'Energia Ativa Fornecida.*?(0,\d{8})', pdf_content)
    tariff = sum([float(re.sub(',', '.', n)) for n in tariff])
    dist_val = re.search(r'\d+,\d{2}$', pdf_content, re.MULTILINE).group()
    en_inj = re.findall(r'Inj\. oUC mPT - TE.*?(\d+,\d{3}\b|\d\.\d{3},\d{3}\b)', pdf_content)
    en_inj = sum(float(v.replace('.', '').replace(',', '.')) for v in en_inj)

    df['Valor'] = [inst_code, month, tariff, dist_val, en_inj]

    return pd.DataFrame(df)

print(pdf_pipeline())
pdf_pipeline().to_csv('table.csv')