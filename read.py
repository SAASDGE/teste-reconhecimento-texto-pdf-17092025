import pdfplumber
import re
import pandas as pd
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def extrair_texto_pdf(caminho_pdf: str) -> str:
    logging.info(f"Lendo arquivo PDF: {caminho_pdf}")
    texto = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for i, pagina in enumerate(pdf.pages, start=1):
            page_text = pagina.extract_text()
            if page_text:
                texto += page_text + "\n"
                logging.debug(f"Página {i} extraída ({len(page_text)} caracteres).")
    return texto

def normalizar_numero(valor: str) -> float:
    if not valor:
        return None
    
    valor = valor.strip().replace(" ", "")
    if re.match(r"^\d{1,3}(\.\d{3})*,\d{2,3}$", valor):
        valor = valor.replace(".", "").replace(",", ".")
    else:
        valor = valor.replace(",", ".")
    try:
        return float(valor)
    except ValueError:
        logging.warning(f"Não foi possível converter '{valor}' em número.")
        return None

# ----------------- EXTRATORES -----------------

def extrair_instalacao(texto: str) -> str:
    match = re.search(r"INSTALAÇÃO[\s\S]{0,100}?(\d{7,10})", texto)
    return match.group(1) if match else None

def extrair_mes_referencia(texto: str) -> str:
    match = re.search(r"\b([A-Z]{3}/\d{4})\b", texto)
    return match.group(1) if match else None

def extrair_tarifa_cheia(texto: str) -> float:
    matches = re.findall(
        r"Energia Ativa Fornecida.*?(\d{1,3}(?:\.\d{3})*,\d{3}) kWh\s+[\d.,]+\s+([\d.,]+)",
        texto
    )
    tarifas = []
    for m in matches:
        quantidade = normalizar_numero(m[0].replace(".", "").replace(",", "."))
        valor_total = normalizar_numero(m[1])
        if quantidade and valor_total:
            tarifas.append(valor_total / quantidade)
    if tarifas:
        return round(sum(tarifas), 6)
    return None

def extrair_valor_distribuidora(texto: str) -> float:
    match = re.search(r"Total Distribuidora\s+([\d.,]+)", texto, re.IGNORECASE)
    return normalizar_numero(match.group(1)) if match else None

def extrair_energia_injetada(texto: str) -> float:
    matches = re.findall(r"Inj.*?(\d{1,3}(?:\.\d{3})*,\d{3}) kWh", texto)
    valores = [normalizar_numero(v.replace(".", "").replace(",", ".")) for v in matches]
    if valores:
        return int(round(sum(valores)))
    return None

def extrair_informacoes(texto: str) -> dict:
    logging.info("Extraindo informações da fatura...")
    return {
        "Instalação": extrair_instalacao(texto),
        "Mês": extrair_mes_referencia(texto),
        "Tarifa cheia (com impostos)": extrair_tarifa_cheia(texto),
        "Valor da distribuidora": extrair_valor_distribuidora(texto),
        "Somatório de energia injetada": extrair_energia_injetada(texto)
    }

# ----------------- MAIN -----------------

def main():
    caminho_pdf = "fatura_cpfl.pdf"
    texto = extrair_texto_pdf(caminho_pdf)
    dados = extrair_informacoes(texto)

    df = pd.DataFrame([dados])
    logging.info("Dados extraídos com sucesso!")
    print(df)

if __name__ == "__main__":
    main()
