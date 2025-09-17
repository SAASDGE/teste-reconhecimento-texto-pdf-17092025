import pandas as pd
import pdfplumber
import re

def analisar_fatura_cpfl(caminho_pdf):
    """
    Lê a fatura CPFL, extrai campos principais de forma dinâmica e devolve em DataFrame.
    """
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto = pdf.pages[0].extract_text()
    except Exception as e:
        print(f"Erro ao abrir PDF: {e}")
        return None

    # Número da instalação
    inst_match = re.search(r"www\.cpfl\.com\.br\s+(\d+)", texto)
    num_instalacao = inst_match.group(1) if inst_match else "Não encontrado"

    # Mês de referência
    # Localiza a palavra 'INSTALAÇÃO' como âncora e captura o padrão de data 
    # ([A-Z]{3}/\d{4}) que a segue (ex: 'OUT/2023').
    mes_match = re.search(r"INSTALAÇÃO\s+([A-Z]{3}/\d{4})", texto)
    mes_referencia = mes_match.group(1) if mes_match else "Não encontrado"

    # Valor da distribuidora
     # Tenta encontrar 'Total Consolidado' e captura o valor monetário ([\d.,]+).
    # Se falhar, usa 'Total a Pagar' como alternativa, garantindo a extração.
    valor_match = re.search(r"Total Consolidado\s+([\d.,]+)", texto)
    if not valor_match:
        valor_match = re.search(r"Total a Pagar.*?([\d.,]+)", texto, re.DOTALL)
    valor_distribuidora = float(valor_match.group(1).replace('.', '').replace(',', '.')) if valor_match else 0.0

    # Tarifas TUSD e TE
    try:
        # Localiza as linhas TUSD e TE, aceitando números no início (\d*). 
        # Usa 'kWh' como referência e captura a tarifa ([\d,]+) logo após.
        tusd_match = re.search(r"\d*Energia Ativa Fornecida - TUSD.*?kWh\s+([\d,]+)", texto)
        te_match = re.search(r"\d*Energia Ativa Fornecida - TE.*?kWh\s+([\d,]+)", texto)

        tarifa_tusd = float(tusd_match.group(1).replace(',', '.'))
        tarifa_te = float(te_match.group(1).replace(',', '.'))
        tarifa_cheia = tarifa_tusd + tarifa_te
    except:
        tarifa_cheia = 0.0

    # Somatório da energia injetada (CÁLCULO DINÂMICO)
    # Encontra todas as linhas de "Energia Injetada" e captura os valores em kWh.
    energia_injetada_kwh = 0.0
    try:
        # re.findall encontra TODAS as ocorrências que casam com o padrão
        # O padrão procura por "Energ Atv Inj" e captura o número antes de "kWh", como por (ex: 1.165,120) 
        valores_injetados_str = re.findall(r"Energ Atv Inj.*? ([\d.,]+)\s+kWh", texto)
        
        # Converte os valores para float (removendo duplicatas)
        valores_unicos = set(valores_injetados_str)
        valores_injetados_float = [float(v.replace('.', '').replace(',', '.')) for v in valores_unicos]
        
        # Soma os valores encontrados
        energia_injetada_kwh = sum(valores_injetados_float)
    except:
        energia_injetada_kwh = 0.0

    # Organiza resultados
    dados = {
        "Campo": [
            "Instalação",
            "Mês",
            "Tarifa cheia (com impostos)",
            "Valor da distribuidora",
            "Somatório de energia injetada"
        ],
        "Valor": [
            num_instalacao,
            mes_referencia,
            f"{tarifa_cheia:.6f}",
            f"{valor_distribuidora:.2f}",
            int(energia_injetada_kwh) # Converte para inteiro
        ]
    }

    return pd.DataFrame(dados)


if __name__ == "__main__":
    df = analisar_fatura_cpfl("fatura_cpfl.pdf")
    if df is not None:
        print(df.to_string(index=False))