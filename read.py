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

def main():
    caminho_pdf = "fatura_cpfl.pdf"
    texto = extrair_texto_pdf(caminho_pdf)
    print(texto[:1000])

if __name__ == "__main__":
    main()