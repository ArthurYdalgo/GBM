#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re
from collections import namedtuple #biblioteca utilizada para criar um "struct"

#"Struct" de caracter, contendo linha e coluna. Dados a serem apresentados caso um caracter invalido seja
#   encontrado
wrongChar = namedtuple("charPosition","line collum")
#exemplo: wrongCharsList.append(wrongChar(3,7))

#"Struct" de token, contendo linha e coluna. Dados a serem apresentados caso um caracter invalido seja
#   encontrado
#pypToken = namedtuple("pypToken","token value")
class pypToken():
    def __init__(self, token, value):
        self.token = token
        self.value = value
        
pypAlphabet = {}#Alfabeto (tipo dictionary)
pypKeywords = {}#Palavras reservadas (tipo dictionary)

#Confere se a linha nao e' comentario
# retorna verdadeiro se a linha nao for comentario
def isnt_comment(line):    
    if (type(line) is str):
        if(line[0]!="#"):
            return True
    elif(type(line) is list ):
        if(line[0][0]!="#"):
            return True
    return False

def is_a_number(str):
    try:
        float(str)
        return True
    except:
        return False

#Verifica valor do token (token.value)
# retorna True se a palavra começa com letras, contem ou termina letras, numeros, _
#TO DO...
def is_idToken_valid(token):
    tValue = token.value
    for char in 

#Checa se os tokens de identificação são validos
# retorna lista de erros
def check_tokens_id_values(token_source_code):
    errors=[]
    line_count = 0
    for line in token_source_code:
        for token in line:
            if(not(is_idToken_valid(token))):
                errors.append(line_count)
                break
        line_count+=1
    return errors

#Separa o código em elementos (virgulas, identificadores, operadores), mas sem tokenização
def split_by_separators(source_code):
    splited_source_code = []
    for line in source_code:        
        if(len(line)>0 and isnt_comment(line)):
            splited_line = re.split('(\W)', line)
            #Opcional: remover o espaço como separador 
            splited_line = filter(lambda a: a != " ", splited_line)     
            splited_line = filter(lambda a: a != "", splited_line)           
            #Junta elementos que formam string        
            item = 0
            while(item<len(splited_line)):                
                if(splited_line[item]=="\""):
                    flag = item+1
                    while(splited_line[flag]!="\""):
                        flag+=1
                    str_item = ' '.join(splited_line[item+1:flag])
                    del splited_line[item:flag+1]
                    splited_line.insert(item,str_item)
                item+=1
            #Junta elementos logicos 
            item=0           
            while(item<len(splited_line)):                
                if(splited_line[item]=="=" or splited_line[item] == "<" or splited_line[item] == ">"):
                    
                    try:                        
                        if(splited_line[item+1]=="="):                                                        
                            new_logic = splited_line[item]+"="                                                        
                            del splited_line[item:item+2]                            
                            splited_line.insert(item,new_logic)                                                        
                    except:
                        pass
                item+=1                  
            splited_source_code.append(splited_line)    
        elif(len(line)>0 and not(isnt_comment(line))):
            splited_source_code.append([line])
        else:
            splited_source_code.append([])
    return splited_source_code

#Transforma os elementos em tokens
def toToken(source_code):
    global pypAlphabet
    global pypKeywords
    splited_source_code = split_by_separators(source_code)
    token_source_code = []    
    for line in splited_source_code:        
        if(len(line)>0):
            if(not(isnt_comment(line))):
                token_source_code.append([pypToken("comment",line[0])])
            else:
                new_line=[]
                for item in line:
                    if(item in pypAlphabet):
                        new_line.append(pypToken(pypAlphabet[item],item))
                    elif(item in pypKeywords):                        
                        new_line.append(pypToken(pypKeywords[item],item))
                    elif(is_a_number(item)):
                        new_line.append(pypToken("numeral_token",item))
                    else:
                        new_line.append(pypToken("id_token",item))
                token_source_code.append(new_line)
        else:
            token_source_code.append([pypToken("empty_line","")])

    for line in token_source_code:
        for item in line:
            print "{0}:'{1}' ".format(item.token,item.value),
        print 

#Procura por "pyp_alphabet.json"
def load_alphabet_from_json():
    try:
        with open('pyp_alphabet.json') as f:
            global pypAlphabet
            pypAlphabet = json.load(f)            
        return 1
    except:
        return -1

#Procura por "pyp_reserved.json"
def load_keywords_from_json():
    try:
        with open('pyp_reserved.json') as f:
            global pypKeywords
            pypKeywords = json.load(f)
        return 1
    except:
        return -1

#Le o nome do arquivo entrado depois do script no terminal
def read_from_terminal():
    return sys.argv[1]

#Import o arquivo, separando em linhas. Retorna uma lista de linhas
def import_file(source_code_name):
    try:
        with open (source_code_name, "r") as myfile:
            source_code=myfile.read().splitlines()
    except:    
        return ""

    return source_code

#Remove espaços indiferentes ao começo, final, ou duplicados
def remove_duplicated_first_last_spaces(source_code):
    for line in range(len(source_code)):
        source_code[line] = " ".join(source_code[line].split())
    return source_code

#Confere se um dado character esta entre letras (ou numeros)
#   (usado para remover espaços entre chars que nao sao letras ou numeros)
def between_digits(str,char):
    global pypAlphabet        
    if((pypAlphabet[str[char-1]]=="letter" or pypAlphabet[str[char-1]]=="digit")and (pypAlphabet[str[char+1]]=="letter" or pypAlphabet[str[char+1]]=="digit")):        
        return True
    return False

#Remoção de comentários no final da linha
def comment_removal(source_code):
    for line in range(len(source_code)):
        if(len(source_code[line])>0):
            if(isnt_comment(source_code[line])):
                char = 0
                while(char!=len(source_code[line])):
                    if(source_code[line][char]=="#"):
                        source_code[line] = source_code[line][:char]
                        break
                    char+=1
    return source_code

#Remocao de espacos entre separadores e operadores
def remove_spaces_next_to_separators(source_code):
    global pypAlphabet
    for line in range(len(source_code)):
        char = 0
        while(char!=len(source_code[line])):
            if(source_code[line][char]==" "):
                if(not(between_digits(source_code[line],char))):                    
                    source_code[line] = source_code[line][:char] + source_code[line][(char+1):]
                    char-=1
            char+=1
    return source_code
        
#Remocao geral de espacos (chama as outras funcoes de remocao)
def space_removal(source_code):  
    source_code = remove_duplicated_first_last_spaces(source_code)    
    source_code = remove_spaces_next_to_separators(source_code)    
    return source_code

#Imprime o codigo enviado
def print_code(source_code):
    for line in source_code:
        print(line)

#Procura por chars que nao estao presentes no alfabeto
#   retorna lista de inteiros referentes as linhas onde estao chars invalidos
def charsAnalyser(source_code):
    errors = []    
    line_count = 1
    for line in source_code:
        if(len(line)>0):
            if(isnt_comment(line)):
                char_count = 1        
                for char in line:            
                    if(not(char in pypAlphabet)):                
                        errors.append(line_count)
                        break
                        #errors.append(wrongChar(line_count,char_count))
                    #char_count+=1
        line_count+=1
    return errors

#Main chama as outras funcoes
def main():
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

    #Remocao de espacos
    source_code = space_removal(source_code)

    #Remocao de comentarios no final da linha
    source_code = comment_removal(source_code)

    #Imprime código apos tratamentos
    #print_code(source_code)

    #Varredura de caracteres
    listofErrors = charsAnalyser(source_code)
    if(len(listofErrors)!=0):
        print("Error: Invalid characters found on")
        for error in listofErrors:
            print("Line: {0}".format(error))
            #print("Line: {0}, collum: {1}".format(error[0],error[1]))
        sys.exit()
    else:
        print("Check: No invalid character found")

    #Transforma o código fonte em tokens
    token_source_code = toToken(source_code)

    #Checagem de nomeclatura de tokens de indentificação
    listOfErrors = check_tokens_id_values(token_source_code)
    if(len(listofErrors)!=0):
        print("Error: Invalid variable name found on")
        for error in listofErrors:
            print("Line: {0}".format(error))            
        sys.exit()
    else:
        print("Check: No invalid variable name found")


   
main()#Chama a main



