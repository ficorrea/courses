# Texto
x = read.csv(file.choose(),header = TRUE, sep = ';')
x

# ODBC
install.packages("RODBC", dependencies = TRUE)
library(RODBC)
conexao = odbcDriverConnect('driver={SQL SERVER};server=...\\SQLEXPRESS;database=VENDAS;trusted_connection=true')
resultado <- sqlQuery(conexao, "select * from dbo.vendas")
resultado
odbcClose(conexao)

# Planilha
install.packages('xlsx', dependencies = TRUE)
library(xlsx)
dados = read.xlsx(file.choose(), sheetIndex=1)
dados

# ARFF
install.packages('foreign', dependencies = TRUE)
library(foreign)
dados = read.arff(file.choose())
dados
