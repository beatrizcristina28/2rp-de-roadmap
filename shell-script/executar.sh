#!/bin/bash

#source para importar o arquivo 
source funcoes.sh

declare array

#listar os arquivos de um diretório passados por parametro
array=lista_arquivos $1
echo ${array[*]}

for i in $(seq 1 ${#array[@]})
    do
        insere_texto $2 ${array[i-1]} 
    done
