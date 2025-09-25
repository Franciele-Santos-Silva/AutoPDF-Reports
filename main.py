import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

tabela = pd.read_csv('horas_extras.csv')
print(tabela)

nome = 'Franciele Santos da Silva'
departamento = 'TI'
horas_extras = 12   
mes_ref = 'Março/2025'

documento_pdf = canvas.Canvas(f"Relatório de horas extras - {nome}.pdf", pagesize = A4)

documento_pdf.setFont("Helvetica-Bolde", 18)
documento_pdf.drawString(30, 750, f"Relatório de horas extras - {nome}")
