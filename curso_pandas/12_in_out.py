import pandas as pd

# Feed pd.read_csv() Método URL Argument

URL = 'https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv'
baby_names = pd.read_csv(URL)
baby_names.head()

# Conversões rápidas
baby_names["Child's First Name"].tolist()
baby_names["Child's First Name"].to_frame()
", ".join(str(name) for name in baby_names["Child's First Name"])

# Exportar para CSV .to_csv()
baby_names.to_csv("NYC Baby Names.csv", index=False)
baby_names.to_csv("NYC Baby Names.csv", index=False, columns=["Child's First Name"], encoding="utf-8")

# Importar XLs .read_excel()
pd.read_excel('datasets/Data - Single Worksheet.xlsx')
pd.read_excel('datasets/Data - Multiple Worksheets.xlsx', sheet_name= 1) # ou nome da tabela
data = pd.read_excel('datasets/Data - Multiple Worksheets.xlsx', sheet_name = [0, 1])
data = pd.read_excel('datasets/Data - Multiple Worksheets.xlsx', sheet_name = None) # busca todas as tabelas
data
data[0]
data[1]

# Exportar para XLS .to_excel()
girls = baby_names[baby_names["Gender"] == 'FEMALE']
boys = baby_names[baby_names["Gender"] == 'MALE']
excel_file = pd.ExcelWriter("Baby Names.xlsx")
girls.to_excel(excel_file, sheet_name='Girls', index=False)
boys.to_excel(excel_file, sheet_name='Boys', index=False, columns=["Gender", 'Ethnicity', 'Count'])
excel_file.save()

