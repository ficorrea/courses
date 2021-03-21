library(udpipe)

# Carrega o arquivo de texto e cria as chaves FILE e ID
arquivo <- read.csv(file.choose(), sep=";", encoding = "UTF-8")
arquivo$ID = as.integer(arquivo$ID)
arquivo$FILE = as.character(arquivo$FILE)

# Dimensões do arquivo
dim(arquivo)
colnames(arquivo)

# Modelo
modelo = udpipe_load_model(file.choose())

# Anotações no formato conll-u
anotar = udpipe_annotate(modelo, x = arquivo$FILE, doc_id = arquivo$ID)
anotar = as.data.frame(anotar)
fix(anotar)
dim(anotar)

# POS 
anotar$upos

# Sumariza frequência upos
frequencia = txt_freq(anotar$upos)
barplot(frequencia$freq, col = gray.colors(14),xlab="Tipo",ylab="Frequência", names.arg = frequencia$key)

# Palavras chave - combinação
anotar$palavra = tolower(anotar$token)
estatisticas = keywords_collocation(x = anotar, term="token", group = "doc_id")
estatisticas$chave = factor(estatisticas$keyword, levels= rev(estatisticas$keyword))
estatisticas2 = head(subset(estatisticas,freq>2))
barplot(estatisticas2$pmi, col = gray.colors(14),xlab="Tipo",ylab="Frequência", names.arg =estatisticas2$chave )
