#!/bin/bash

echo "Quantidade de arquivos: "
read num;
((num=$num-1))

echo "Arquivo final: "
read nome_final
nome_final=$nome_final."pdf"

i=0
while [ $i -le $num ];
do
	echo "nome do arquivo $i:"
	read geral[$i]
	((i=$i+1))
done

for ((i=0;i<=num;i++));
do
	geral[$i]=${geral[$i]}."pdf"
done

pdftk ${geral[@]} output $nome_final
echo -e "\nArquivos mesclados com sucesso!!!"
sleep 10

