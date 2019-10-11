#!/usr/bin/env python

import sys
import json
from collections import namedtuple #biblioteca utilizada para criar um "struct"

#"Struct" de caracter, contendo linha e coluna. Dados a serem apresentados caso um caracter invalido seja
#   encontrado
wrongChar = namedtuple("charPosition","line collum")
#exemplo: wrongCharsList.append(wrongChar(3,7))

pypAlphabet = {}#Alfabeto (tipo dictionary)
pypKeywords = {}#Palavras reservadas (tipo dictionary)

def load_alphabet_from_json():#Procura por "pyp_alphabet.json"
    try:
        with open('pyp_alphabet.json') as f:
            global pypAlphabet
            pypAlphabet = json.load(f)            
        return 1
    except:
        return -1

def load_keywords_from_json():#Procura por "pyp_reserved.json"
    try:
        with open('pyp_reserved.json') as f:
            global pypKeywords
            pypKeywords = json.load(f)
        return 1
    except:
        return -1

def read_from_terminal():#Le o nome do arquivo entrado depois do script no terminal
    return sys.argv[1]

def import_file(source_code_name):#Import o arquivo, separando em linhas. Retorna uma lista de linhas
    try:
        with open (source_code_name, "r") as myfile:
            source_code=myfile.read().splitlines()
    except:    
        return ""

    return source_code

def charsAnalyser(source_code):
    errors = []    
    line_count = 1
    for line in source_code:
        char_count = 1        
        for char in line:            
            if(not(char in pypAlphabet)):                
                errors.append(line_count)
                break
                #errors.append(wrongChar(line_count,char_count))
            #char_count+=1
        line_count+=1
    return errors

def main():#Main chama as outras funcoes
    #Importacao do alfabeto
    if(load_alphabet_from_json()==-1):
        print("Error: Alphabet file 'pyp_alphabet.json' not found. Run 'python alphabet.py' to generate it.")
        sys.exit()
    else:
        print("Check: Alphabet loaded successfully")

    #Importacao de palavras reservadas
    if(load_keywords_from_json()==-1):
        print("Error: Keywords file 'pyp_reserved.json' not found. Run 'python reserved.py' to generate it.")
        sys.exit()
    else:
        print("Check: Keywords loaded successfully")
    
    #Importacao do codigo fonte
    source_code_name = read_from_terminal()
    source_code = import_file(source_code_name)
    if(len(source_code)==0):
        print("Error: File {0} not found".format(source_code_name))
        sys.exit()
    else:
        print("Check: File readed successfully")    

    #Varredura de caracteres
    listOfErros = charsAnalyser(source_code)
    if(len(listOfErros)!=0):
        print("Error: Invalid characters found on")
        for error in listOfErros:
            print("Line: {0}".format(error))
            #print("Line: {0}, collum: {1}".format(error[0],error[1]))
    else:
        print("Check: No invalid character found")

    

main()#Chama a main



