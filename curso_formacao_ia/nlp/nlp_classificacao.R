library(udpipe)

# Carrega arquivo
arquivo <- read.csv(file.choose(), sep=",", encoding = "UTF-8", header = F, quote="\"")

# Dimensões do arquivo 
# Nomeia as colunas
colnames(arquivo) = c("FILE","CLASS")
dim(arquivo)[1]
head(arquivo)

# Transforma o arquivo em caracter
arquivo$FILE = as.character(arquivo$FILE)
arquivo$CLASS = as.character(arquivo$CLASS)

# Cria ID para texto
arquivo$ID = seq(1:dim(arquivo)[1])

# Download modelo
modelo = udpipe_download_model(language = "english")

# Modelo
modelo = udpipe_load_model(file.choose())

# Cria anotações 
anotar = udpipe_annotate(modelo, x = arquivo$FILE, doc_id = arquivo$ID)

# Transforma anotações em dataframe
anotar = as.data.frame(anotar)
head(anotar)
dim(anotar)

# Filtra apenas verbos, substantivos e adjetivos
anotar2 = anotar[anotar$upos %in% c("VERB", "NOUN", "ADJ","ADV"), ]
dim(anotar2)

# Apenas colunas  doc_id, lemma
anotar2 = anotar2[,c(1,7)]

# Obtem frequências de termos
x <- document_term_frequencies(anotar2[, c("doc_id", "lemma")])
dtm <- document_term_matrix(x)
dim(dtm)
summary(dtm)
colnames(dtm)
rownames(dtm)
head(dtm)

# Transforma em dataframe
df = as.data.frame(as.matrix(dtm))

# Número do doc está no nome da linha, vamos passar para um coluna 
# para fazer um merge com o documento original e pegar a classe
df$doc_id =   rownames(df)
df$doc_id = as.integer(df$doc_id)

# Efetuando merge
df2 = merge(df,arquivo, by.x =c("doc_id") ,by.y = c("ID")  )

# REMOVER COLUNA COM ARQUIVO QUE FOI CRIADA NO MERGE
df2$FILE =  NULL
head(df2$CLASS,n=100)
dim(df2)

library(caret)
library(FSelector)

# Seleção de atributos
atributos <- information.gain(CLASS ~., df2)
atributos2 = cutoff.k(atributos,20)
formula =  as.simple.formula(atributos2, class="CLASS")

# Classe em fator
df2$CLASS = as.factor(df2$CLASS)

# Partição
particao = createDataPartition(1:dim(df2)[1],p=.7)
dftreino = df2[particao$Resample1,]
dfteste = df2[- particao$Resample1,]
dim(dftreino)
dim(dfteste)

# Executa random forest
library(randomForest)

# Criação do modelo
modelo = randomForest(formula, data = dftreino, ntree=500 ) 
previsao  = predict(modelo, dfteste)
previsao
confusionMatrix(previsao, dfteste$CLASS)
