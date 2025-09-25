import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

tabela = pd.read_csv('horas_extras.csv')
print(tabela)

pasta_relatorios = "Relatorios"
os.makedirs(pasta_relatorios, exist_ok=True) 

for linha in tabela.index:
    nome = tabela.loc[linha, 'Nome']
    departamento = tabela.loc[linha, 'Departamento']
    horas_extras = tabela.loc[linha, 'Horas Extras']
    mes_ref = tabela.loc[linha, 'Referência']

    caminho_pdf = os.path.join(pasta_relatorios, f"Relatorio_de_horas_extras_{nome}.pdf")

    documento_pdf = canvas.Canvas(caminho_pdf, pagesize=A4)

    documento_pdf.setFont("Helvetica-Bold", 18)

    documento_pdf.drawString(100, 750, f"Relatório de horas extras - {nome}")

    distancia = 30

    documento_pdf.setFont("Helvetica", 12)
    documento_pdf.drawString(100, 700, f"Nome: {nome}")
    documento_pdf.drawString(100, 700 - 1 * distancia, f"Departamento: {departamento}")
    documento_pdf.drawString(100, 700 - 2 * distancia, f"Quantidade de horas extras: {horas_extras}")
    documento_pdf.drawString(100, 700 - 3 * distancia, f"Mês de referência: {mes_ref}")
    documento_pdf.drawString(100, 700 - 4 * distancia, "Esse relatório foi gerado automaticamente em Python")

    documento_pdf.save()
