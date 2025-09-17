# Desenvolva aqui sua atividade

import pdfplumber
import re
import pandas as pd

def extrair_texto_pdf(caminho_pdf: str) -> str:
    texto = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            page_text = pagina.extract_text()
            if page_text:
                texto += page_text + "\n"
    return texto

def normalizar_numero(valor: str) -> float:
    if not valor:
        return None
    valor = valor.replace(".", "").replace(",", ".")
    return float(valor)

def extrair_instalacao(texto: str) -> str:
    match = re.search(r"\b\d{8,11}\b", texto)
    return match.group(0) if match else None

def extrair_mes(texto: str) -> str:
    match = re.search(r"(JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)/\d{2,4}", texto)
    return match.group(0) if match else None

def extrair_tarifa(texto: str) -> float:
    matches = re.findall(r"\d{1,3}(?:\.\d{3})*,\d{5,}", texto)
    if matches:
        return normalizar_numero(matches[-1])
    return None

def extrair_valor_distribuidora(texto: str) -> float:
    match = re.search(r"Total Distribuidora\s+([\d\.,]+)", texto, re.IGNORECASE)
    if match:
        return normalizar_numero(match.group(1))
    return None

def extrair_soma_injecao(texto: str) -> float:
    matches = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d+)-", texto)
    if matches:
        return sum(normalizar_numero(m) for m in matches if m)
    return None

def extrair_informacoes(texto: str) -> dict:
    return {
        "Instalação": extrair_instalacao(texto),
        "Mês": extrair_mes(texto),
        "Tarifa cheia (com impostos)": extrair_tarifa(texto),
        "Valor da distribuidora": extrair_valor_distribuidora(texto),
        "Somatório de energia injetada": extrair_soma_injecao(texto)
    }

def processar_faturas(lista_arquivos: list) -> pd.DataFrame:
    resultados = []
    for arquivo in lista_arquivos:
        texto = extrair_texto_pdf(arquivo)
        info = extrair_informacoes(texto)
        resultados.append(info)
    return pd.DataFrame(resultados)

def main():
    arquivos = ["fatura_cpfl.pdf", "fatura_cemig.pdf", "fatura_cemig_convencional.pdf"]
    df = processar_faturas(arquivos)
    print(df)

if __name__ == "__main__":
    main()