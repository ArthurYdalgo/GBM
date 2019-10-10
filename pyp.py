#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

pypAlphabet = {}

def load_alphabet_from_json():
    try:
        with open('pyp_alphabet.json') as f:
            pypAlphabet = json.load(f)
        return 1
    except:
        return -1

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

    if(load_alphabet_from_json()==-1):
        print("Error: Alphabet file 'pyp_alphabet.json' not found. Run 'python alphabet.py' to generate it.")
        sys.exit()
    else:
        print("Alphabet loaded successfully")
    
    source_code_name = read_from_terminal()
    
    source_code = import_file(source_code_name)
    if(len(source_code)==0):
        print("Error: File {0} not found".format(source_code_name))
        return
    
    

main()#Chama a main



