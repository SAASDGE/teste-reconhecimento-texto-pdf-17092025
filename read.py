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

def extrair_informacoes(texto: str) -> dict:
    # Número da instalação
    match_instalacao = re.search(r"\b(\d{8})\b", texto)
    instalacao = match_instalacao.group(1) if match_instalacao else None

    # Mês de referência
    match_mes = re.search(r"INSTALAÇÃO\s+([A-Z]{3}/\d{4})", texto)
    mes_ref = match_mes.group(1) if match_mes else None

    return {
        "Instalação": instalacao,
        "Mês": mes_ref
    }

def main():
    caminho_pdf = "fatura_cpfl.pdf"
    texto = extrair_texto_pdf(caminho_pdf)
    print(texto[:1000])

if __name__ == "__main__":
    main()