# AutoPDF-Reports - Relatórios de horas extras em PDF

Este projeto gera automaticamente **relatórios de horas extras** de funcionários em arquivos PDF, a partir de uma tabela CSV.

## Funcionalidades

- Lê uma tabela CSV com os dados dos funcionários:
  - Nome
  - Departamento
  - Quantidade de horas extras
  - Mês de referência
- Gera um PDF para cada funcionário com as informações detalhadas.
- Salva os PDFs em uma pasta específica (`Relatorios`).
- O processo é automático, gerando todos os relatórios de uma vez.

## Tecnologias

- **Python 3**
- [pandas](https://pandas.pydata.org/) – para leitura do CSV
- [reportlab](https://www.reportlab.com/) – para geração de PDFs
- **os** – para manipulação de pastas e caminhos de arquivos

## Como usar

1. Coloque o arquivo CSV horas_extras.csv na mesma pasta do script.

2. Instale as dependências, se necessário:

        pip install pandas reportlab

3. Execute o script

        python main.py
