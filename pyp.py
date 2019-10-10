#!/usr/bin/env python
import sys

def read_from_terminal():#Lê o nome do arquivo entrado depois do script no terminal
    return sys.argv[1]

def import_file(source_code_name):#Import o arquivo, separando em linhas. Retorna uma lista de linhas
    try:
        with open (source_code_name, "r") as myfile:
            source_code=myfile.readlines()
    except:    
        return ""

    return source_code

def main():#Main chama as outras funções
    
    source_code_name = read_from_terminal()
    
    source_code = import_file(source_code_name)
    if(len(source_code)==0):
        print("Error 0: File {0} not found".format(source_code_name))
        return
    
    

main()#Chama a main



