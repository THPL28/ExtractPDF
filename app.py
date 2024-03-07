from pathlib import Path
# import pandas as pd
from PyPDF2 import PdfReader
from ExtractPdf.helpers.functions import *
import re
import logging

pasta_personalizada = 'logs'
logger = configurar_logger('extract_logg', pasta_personalizada)

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_origin'
PASTA_NOVA = PASTA_RAIZ / 'arquivs_news'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240202.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)



num_pages = len(reader.pages)
i = 0


textOcr ='''
 Expectativas de Mercado 2 de fevereiro de 2024
FocusRelatório de Mercado
Mediana - Agregado Há 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias
úteisResp.
***Há 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias
úteisResp.
***Há 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**Há 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**
IPCA (variação %) 3,90 3,81 3,81 (1) 156 3,76 55 3,50 3,50 3,50 (28) 149 3,50 55 3,50 3,50 3,50 (31) 129 3,50 3,50 3,50 (31) 121
PIB Total (variação % sobre ano anterior) 1,59 1,60 1,60 (2) 113 1,62 28 2,00 2,00 2,00 (8) 91 2,00 21 2,00 2,00 2,00 (26) 77 2,00 2,00 2,00 (28) 75
Câmbio (R$/US$) 5,00 4,92 4,92 (2) 128 4,90 41 5,00 5,00 5,00 (4) 119 5,00 38 5,10 5,05 5,04▼ (1) 87 5,10 5,10 5,10 (4) 83
Selic (% a.a) 9,00 9,00 9,00 (6) 146 9,00 43
8,50 8,50 8,50 (9) 140 8,50 43 8,50 8,50 8,50 (27) 116 8,50 8,50 8,50 (26) 111
IGP-M (variação %) 4,06 4,02 3,81▼ (3) 78 3,61 27 3,98 3,99 3,99 (2) 65 3,81 22 4,00 4,00
4,00 (50) 57 4,00 3,90 3,90 (1) 54
IPCA Administrados (variação %) 4,30 4,13 4,09▼ (9) 96 3,93 28 4,00 3,98 3,96▼ (2) 78 3,57 25 3,53 3,52 3,52 (1) 58 3,50 3,50 3,50 (18) 54
Conta corrente (US$ bilhões) -40,30 -38,00 -37,20 ▲ (1) 31 -34,42 10 -43,00 -39,65 -39,30▲ (1) 27 -35,00 9 -43,55 -42,00 -40,45▲ (1) 20 -50,00 -45,35 -43,90▲ (1) 18
Balança comercial (US$ bilhões) 70,50 78,45 76,90▼ (1) 31 75,00 9 66,59 70,00 68,90▼ (1) 24 70,00 7 68,50 71,50 71,50 (1) 16 63,00 74,00 74,00 (2) 15
Investimento direto no país (US$ bilhões) 65,00 68,42 69,84▲ (2) 27 65,00 7 70,00 75,00 75,65▲ (1) 24 77,50 6 78,00 80,00 80,00 (2) 18
76,50 80,00 80,00 (1) 17
Dívida líquida do setor público (% do PIB) 64,25 63,60 63,60 (1) 25 63,80 7 66,40 66,00 66,00 (1) 24 66,55 6 69,50 68,40 68,65▲ (1) 20
71,62 69,81 69,95▲ (1) 20
Resultado primário (% do PIB) -0,80 -0,80 -0,80 (7) 42 -0,90 9 -0,60 -0,60 -0,60 (2) 39 -0,65 8 -0,50 -0,50 -0,50 (10) 31 -0,20 -0,28 -0,30▼ (2) 29
Resultado nominal (% do PIB) -6,80 -6,80 -6,80 (1) 25 -7,25 8 -6,20 -6,20 -6,29▼ (1) 23 -6,50 7 -5,90 -5,72 -5,83▼ (1) 18 -5,56 -5,56 -5,62▼ (1) 17
* comportamento dos indicadores desde o Focus-Relatório de Mercado anterior; os valores entre parênteses expressam o número de semanas
em que vem ocorrendo o último comportamento ** respondentes nos últimos 30 dias *** respondentes nos últimos 5 dias úteis
 2024  2025  2026  2027
▲Aumento ▼Diminuição  Estabilidade
2024 2025 2026 2027
Focus - Relatório de Mercado Pág. 1/2
Metadados da página 1:
 Expectativas de Mercado 2 de fevereiro de 2024
FocusRelatório de Mercado
 jan/2024  fev/2024  mar/2024  In . 12 m suav.Mediana - Agregado Há 4.Me
diana - Agregado Há 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias
úteisHá 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias
úteisHá 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias
úteisHá 4
semanasHá 1
semanaHojeComp.
semanal *Resp.
**5 dias                                     6 0,65 0,67 0,69▲ (3) 152 0,70 0,32 0,28 0,28 (1) 152 
úteis                                        ) 117 4,91 4,93 4,90 4,90 (3) 118 4,90
IPCA (variação %) 0,37 0,39 0,38▼ (2) 153 0,3 10,75 (26) 145 10,756 0                                          ▼ (3) 73 0,26 0,33 0,33 0,33 (1) 73 0,31 3,98 4,00 4,0
,65 0,67 0,69▲ (3) 152 0,70 0,32 0,28 0,28 (1-Relatório de Mercado anterior; os valores entre parên) 1
52 0,29 3,88 3,82 3,82 (1) 121 3,76
Câmbio (R$/US$) 4,90 4,90 - 4,92 4,90 4,90 (3) 1
17 4,91 4,93 4,90 4,90 (3) 118 4,90
Selic (% a.a) - - - 11,25 11,25 - 10,75 10,75úteis
IPCA (variação %) 0,37 0,39 0,38▼ (2) 153 0,36 0,65 0,67 0,69▲ (3) 152 0,70 0,32 0,28 0,28 (1) 152
0,29 3,88 3,82 3,82 (1) 121 3,76
Câmbio (R$/US$) 4,90 4,90 - 4,92 4,90 4,90 (3) 117 4,91 4,93 4,90 4,90 (3) 118 4,90
Selic (% a.a) - - - 11,25 11,25 - 10,75 10,75 10,75 (26) 145 10,75
IGP-M (variação %) 0,45 0,35 - 0,37 0,32 0,31▼ (3) 73 0,26 0,33 0,33 0,33 (1) 73 0,31 3,98 4,00 4,01▲ (1) 58 3,64
* comportamento dos indicadores desde o Focus-Relatório de Mercado anterior; os valores entre parênteses expressam o número de semanas em que vem ocorrendo o último comportamento ** respondentes nos últimos 30 dias
▲Aumento ▼Diminuição  Estabilidade
jan/2024 fev/2024 mar/2024 In . 12 m suav.
Focus - Relatório de Mercado Pág. 2/2'''

#Retorno experado
# data = {
#     "Indicador Econômico": ["IPCA (variação %)", "PIB Total (variação % sobre ano anterior)", "Câmbio (R$/US$)", "Selic (% a.a)", "IGP-M (variação %)"],
#     "Há 4 semanas": [3.90, 1.59, 5.00, 9.00, 4.06],
#     "Há 1 semana": [3.81, 1.60, 4.92, 9.00, 4.02],
#     "Hoje": [3.81, 1.60, 4.92, 9.00, 3.81],
#     "Comp. semanal *": [1, 2, 2, 6, 3],
#     "Resp. **5 dias úteis": [156, 113, 128, 146, 78],
#     "Há 4 semanas.1": [3.76, 1.62, 4.90, 9.00, 3.61],
#     "Há 1 semana.1": [3.50, 2.00, 5.00, 8.50, 3.98],
#     "Hoje.1": [3.50, 2.00, 5.00, 8.50, 3.99],
#     "Comp. semanal *.1": [28, 8, 4, 27, 2],
#     "Resp. **5 dias úteis.1": [149, 91, 119, 116, 65]
# }


data = {
    "Indicador Econômico": [],
    "Há 4 semanas": [],
    "Há 1 semana": [],
    "Hoje": [],
    "Comp. semanal *": [],
    "Resp. **5 dias úteis": [],
    "Há 4 semanas.1": [],
    "Há 1 semana.1": [],
    "Hoje.1": [],
    "Comp. semanal *.1": [],
    "Resp. **5 dias úteis.1": []
}

for i, pg in  enumerate(range(num_pages)):


    content = reader.pages[i]

    # conteudo da pagina
    text = content.extract_text()
    # Imprimir os metadados da página
    if i == 0:
    #   print(f"Metadados da página {i}: \n", content.extract_text())
      ocrTxtsplit = text.split('\n')
      for palavra in ocrTxtsplit:
        dados = palavra.split()


        try:
       
          if 'IPCA' in dados[:1]:
            if 'Administrados' not in dados[:3]:
              idicadores = unir_lista(dados[:3])
              data['Indicador Econômico'] = idicadores
              # print(data['Indicador Econômico'])
          if 'PIB' in dados[:1]:
              idicadores = unir_lista(dados[:3])
              data['Indicador Econômico'] = idicadores
              print(dados[:3])
          else:
                logger.warning("idicadores não encontrados")
        except AttributeError:
           logger.critical("Dados Inesistentes!")

           print("Dados Inesistentes!")


# # extrai apenas a imagem encontrada determinando a pagina
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)



