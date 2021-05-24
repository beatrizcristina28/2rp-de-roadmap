#!/bin/bash

#retorna todos os arquivos existentes no path passado via params
#o comando -f junto com o -type, indica que são todos os tipos de arquivo
#também é possível passar a extensão ou o nome do arquivo desejado

lista_arquivos(){
    files=(`find $1 -type f`)
    echo ${files[*]}
}

#lista_arquivos $1 $2

#insere no fim do arquivo p1, o texto passado no p2
#usando >> o texto é inserido ao final sem sobrescrever o file

insere_texto(){
    echo -e "\n"$1 >> $2
}

#o comando tee pode ser utilizado para inserção em mais de um arquivo
#usando o -a (--append), o tee não irá sobrescrever o file e sim adicionar informações
#-e permite que o newline seja executado

insere_texto2(){
    echo -e "\n"$1 | tee -a $2
}

#insere_texto2 $1 $2