# Desenvolva aqui sua atividade

import pandas as pd
import pdfplumber
import re

"""
Instalação	12385675
Mês	OUT/2023
Tarifa cheia (com impostos)	0,881145
Valor da distribuidora	219,14
Somatório de energia injetada	1950
"""

def lerPDF(arquivo):
    with pdfplumber.open(arquivo) as pdf:
        pagina = pdf.pages[0]
        linhas = pagina.extract_text().split("\n")


        #Encontrar Mês, Valor da Distribuidora (com impostos)

        padraoConteudo = r"INSTALAÇÃO\s+([A-Z]{3}/\d{4})\s+(\d{2}/\d{2}/\d{4})\s+(\d+,\d{2})"
        conteudo = re.search(padraoConteudo, pagina.extract_text_simple())
        conteudo = conteudo.groups()

        dados = {"Mes" : [conteudo[0]], "Valor da distribuidora" : [conteudo[2]]}

        # Encontrar Instalação
        instalacao = linhas[18].split(" ")[1]
        dados.update({"Instalação" : [instalacao]})


        #Encontrar Tarifa cheia (com impostos)

        linhasImpostos = []
        for linha in linhas:
            if "Energia Ativa Fornecida" in linha:
                linhasImpostos.append(linha)

        tarifaTotal = 0
        for linha in linhasImpostos:
            tarifa = float(linha.split(" ")[8].replace(",","."))
            tarifaTotal += tarifa

        dados.update({"Tarifa cheia (com impostos)" : [tarifaTotal]})

        #Encontrar Energia Injetada
        padrao = r"Energ Atv Inj\. oUC mPT - TUSD.*"
        energiaInjetada = re.findall(padrao, pagina.extract_text())

        totalEnergia = 0
        for linha in energiaInjetada:
            linha = linha.split(" ")[8].replace(".", "").replace(",", ".")
            totalEnergia += float(linha)

        dados.update({"Somatório de energia injetada": [totalEnergia]})

        #Cria o DataFrame
        pd.set_option('display.max_columns', None)
        df = pd.DataFrame(dados)

        print(df)

if __name__ == '__main__':

    arquivo = "./fatura_cpfl.pdf"
    lerPDF(arquivo)

