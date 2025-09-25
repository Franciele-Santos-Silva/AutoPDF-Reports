import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

tabela = pd.read_csv('horas_extras.csv')
print(tabela)

nome = 'Franciele Santos da Silva'
departamento = 'TI'
horas_extras = 12   
mes_ref = 'Março/2025'

documento_pdf = canvas.Canvas(f"Relatório de horas extras - {nome}.pdf", pagesize=A4)

documento_pdf.setFont("Helvetica-Bold", 12)
distancia = 30

documento_pdf.drawString(100, 700, f"Nome: {nome}")
documento_pdf.drawString(100, 700 - 1 * distancia, f"Departamento: {departamento}")
documento_pdf.drawString(100, 700 - 2 * distancia, f"Quantidade de horas extras: {horas_extras}")
documento_pdf.drawString(100, 700 - 3 * distancia, f"Mês de referência: {mes_ref}")
documento_pdf.drawString(100, 700 - 4 * distancia, "Esse relatório foi gerado automaticamente em Python")

documento_pdf.save()
