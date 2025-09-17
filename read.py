# Desenvolva aqui sua atividade

import re # Biblioteca para expressões regulares (regex)
import pdfplumber # Biblioteca para manipulação de PDFs
import pandas as pd 
from typing import Optional # Biblioteca para tipagem opcional

# Função que normaliza números no formato brasileiro para float opcionalmente
def normalize_number(value: str) -> Optional[float]:
    # Testa se value existe
    if not value:
        return None
    v = value.strip().replace('\xa0', '')
    # Remove pontos do milhar e trocar a vírgula por ponto para decimais
    v = v.replace('.', '').replace(',', '.')
    
    # Converte para float
    try:
        return float(v)
    except:
        return None

# Formata número float para string no formato brasileiro com vírgula decimal para o dataframe
def format_brazilian(number: Optional[float], decimals: int) -> str:
    if number is None:
        return ''
    s = f"{number:.{decimals}f}"
    return s.replace('.', ',')

# Função que extrai os dados da fatura no PDF
def extract_fatura(path_pdf: str):
    # Extrai texto do PDF de path_pdf
    with pdfplumber.open(path_pdf) as pdf:
        pages_text = [p.extract_text() or "" for p in pdf.pages]
    # Coloca todas as páginas em uma única string e divide em linhas
    text = "\n".join(pages_text)
    lines = text.splitlines()

    # INSTALAÇÃO: procura linha com "www.cpfl" (mesma linha do número alvo) e a partir dessa linha por um número de 8 dígitos que é o número de instalação
    instalacao = None
    for line in lines:
        if 'www.cpfl' in line.lower():
            m = re.search(r'\b(\d{8})\b', line)
            if m:
                instalacao = m.group(1)
                break

    # 2) MÊS: formato 'OUT/2023' ou 'OUT/23' -> normaliza para 4 dígitos do ano
    mes = None
    m = re.search(r'\b(JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)\/\d{2,4}\b', text, re.IGNORECASE)
    # Coloca tudo maiúsculo e normaliza ano para 4 dígitos
    if m:
        mes = m.group(0).upper()
        if re.search(r'\/\d{2}\b', mes):
            mes = re.sub(r'\/(\d{2})$', r'/20\1', mes)

    # 3) TARIFA CHEIA (com impostos): somar os unitários TUSD + TE (valores com 7-8 casas decimais) em Discriminação da Operação
    tusd = None
    te = None
    for line in lines:
        # Procura por linhas sem Inj pois a tarifa injetada vem depois de TUSD e TE
        if 'TUSD' in line and 'Inj' not in line:
            # Procura número com 6-8 casas decimais
            m = re.search(r'(\d+[.,]\d{6,8})', line)
            # variavel tusd só é preenchida se estiver None (primeiro valor que encontrado)
            if m and tusd is None:
                tusd = normalize_number(m.group(1)) # normaliza número pra float
        # Segue o mesmo processo para TE, procura linha com "TE" e sem "Inj"
        if re.search(r'\bTE\b', line) and 'Inj' not in line:
            # Procura número com 6-8 casas decimais
            m = re.search(r'(\d+[.,]\d{6,8})', line)
            if m and te is None:
                te = normalize_number(m.group(1)) # se for a primeira ocorrencia, normaliza número pra float
        if tusd is not None and te is not None:
            break
    # Se os dois valores foram encontrados, soma e arredonda para 6 casas decimais
    tarifa_cheia = round((tusd or 0) + (te or 0), 6) if (tusd is not None and te is not None) else None

    # 4) VALOR DA DISTRIBUIDORA: 
    valor_distribuidora = None
    # Procura por "Total a Pagar"
    m = re.search(r'Total a Pagar[^\d\n\r]*([\d\.,]+)', text, re.IGNORECASE)
    if m:
        # Se encontrar, normaliza o número
        valor_distribuidora = normalize_number(m.group(1))
    else:
        # Do contrário, procura por "Total Consolidado"
        m = re.search(r'Total Consolidado[^\d\n\r]*([\d\.,]+)', text, re.IGNORECASE)
        if m:
            # Se encontrar, normaliza o número
            valor_distribuidora = normalize_number(m.group(1))
        else:
            # pega último número com vírgula na linha de instalação que é a linha que está o valor da distribuidora no arquivo
            for line in lines:
                if re.search(r'INSTAL', line, re.IGNORECASE):
                    # se achou instal na linha em questão, pega todos os números decimais da linha
                    nums = re.findall(r'([\d\.,]+)', line)
                    for num in nums:
                        if ',' in num:  # tenta pegar valor com vírgula (monetário)
                            valor_distribuidora = normalize_number(num)
                            break
                    break

    # 5) SOMATÓRIO DE ENERGIA INJETADA: capturar (mês, kWh) de linhas com "Inj" escrito
    inj_list = []
    for line in lines:
        if re.search(r'Inj', line, re.IGNORECASE):
            # pega todas as informações mês/ano <kWh> kWh na linha
            pairs = re.findall(r'([A-Z]{3}\/\d{2,4})\s+([\d\.,]+)\s*kWh', line, re.IGNORECASE)
            # mth = mês, kwh_str = valor em kWh
            for (mth, kwh_str) in pairs:
                kwh = normalize_number(kwh_str)
                if kwh is not None:
                    inj_list.append((mth.upper(), kwh)) # se não for o primeiro, adiciona na lista
    unique_by_month = {}
    for mth, kwh in inj_list:
        if mth not in unique_by_month:
            unique_by_month[mth] = kwh # mantém o primeiro valor encontrado por mês para que não haja duplicação
    
    # Esse primeiro valor guardado é somado e arredondado para inteiro, os demais numeros seriam outros valores fora do contexto
    soma_injetada = int(round(sum(unique_by_month.values()))) if unique_by_month else None

    # Monta tabela de saída [Campo | Valor] para df pandas seguindo o formato brasileiro
    rows = [
        ("Instalação", instalacao or ""),
        ("Mês", mes or ""),
        ("Tarifa cheia (com impostos)", format_brazilian(tarifa_cheia, 6) if tarifa_cheia is not None else ""),
        ("Valor da distribuidora", format_brazilian(valor_distribuidora, 2) if valor_distribuidora is not None else ""),
        ("Somatório de energia injetada", str(soma_injetada) if soma_injetada is not None else "")
    ]

    return pd.DataFrame(rows, columns=["Campo", "Valor"])

if __name__ == "__main__":
    df = extract_fatura("fatura_cpfl.pdf")
    print(df.to_string(index=False))
