install.packages("udpipe", dependencies = T)
library(udpipe)

FILE = 'Nossa vida é controlada por algoritmos,'
ID = 1L

arquivo = data.frame(FILE, ID)
arquivo$FILE = as.character(arquivo$FILE)

# Download do modelo
modelo = udpipe_download_model(language = 'portuguese-br')

# Carregar modelo
modelo = udpipe_load_model(file.choose())

# Anotações no formato Conll-U
anotar = udpipe_annotate(modelo, x = arquivo$FILE, doc_id = arquivo$ID)
anotar
anotar = as.data.frame(anotar)
colnames(anotar)

fix(anotar)
