
# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
import json #biblioteca para arquivos json
import re #biblioteca de regex
import os.path #biblioteca para verificação de existencia de arquivo
from prettytable import PrettyTable #biblioteca para exibição de tabela de simbolos

#"Struct" de token, contendo linha e coluna. Dados a serem apresentados caso um caracter invalido seja
#   encontrado
class pypToken():
    def __init__(self, token, value,line=1,collum=1):
        self.token = token
        self.value = value
        self.line  = line
        self.collum = collum
    
    def setPos(self,line,collum):
        self.line = line
        self.collum = collum
    
        
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

#Verifica se string é um numero
def is_a_number(str):
    try:
        float(str)
        return True
    except:
        return False

#Verifica valor do token (token.value)
# retorna True se a palavra começa com letras, contem ou termina letras, numeros, _
def is_idToken_valid(token):
    tValue = token.value    
    if(pypAlphabet[tValue[0]] == "letter" and tValue[0] != "_" ):        
        if(len(tValue) == 1):
           return True
        for char in tValue:
            if(pypAlphabet[char] != "letter" and pypAlphabet[char] !="digit"):
                return False
        return True
    else:
        return False
            

#Checa se os tokens de identificação são validos
# retorna lista de erros
def check_tokens_id_values(token_source_code):
    errors=[]
    line_count = 1
    for line in token_source_code:
        for token in line:
            if(token.token == "id_token"):
                if(not(is_idToken_valid(token))):                    
                    errors.append(line_count)
                    break
        line_count+=1   
    if(len(errors)!=0):
        print("Error: Invalid variable name found on")
        for error in errors:
            print("Line: {0}".format(error))            
        sys.exit()     

#Separa o código em elementos (virgulas, identificadores, operadores), mas sem tokenização
def split_by_separators(source_code):
    splited_source_code = []
    unclosed_strings=[]
    unclosed_flag=False
    line_count=1
    for line in source_code:        
        if(len(line)>0 and isnt_comment(line)):
            splited_line = re.split('(\W)', line)
            #Opcional: remover o espaço como separador 
            splited_line = filter(lambda a: a != " ", splited_line)     
            splited_line = filter(lambda a: a != "", splited_line) 
            #Junta elementos que formam floats
            item=0           
            while(item<len(splited_line)):                
                if(is_a_number(splited_line[item])):   
                    try:                        
                        if(splited_line[item+1]=="." and is_a_number(splited_line[item+2])):
                            new_logic = splited_line[item]+"."+splited_line[item+2]                      
                            del splited_line[item:item+3]                            
                            splited_line.insert(item,new_logic)                                                        
                    except:
                        pass                
                item+=1                  
            #Junta elementos que formam string        
            item = 0
            while(item<len(splited_line)):                
                if(splited_line[item]=="\""):
                    flag = item+1
                    if(flag==len(splited_line)):
                        unclosed_strings.append(line_count)                        
                        break
                    while(splited_line[flag]!="\""):                        
                        flag+=1
                        if(flag==len(splited_line)):
                            unclosed_strings.append(line_count)
                            unclosed_flag=True
                            break
                    if(unclosed_flag):
                        unclosed_flag=False
                        break
                    str_item = ' '.join(splited_line[item+1:flag])
                    del splited_line[item:flag+1]
                    str_item = "_str:"+str_item
                    splited_line.insert(item,str_item)
                item+=1
            #Junta elementos logicos 
            item=0           
            while(item<len(splited_line)):                
                if(splited_line[item]=="=" or splited_line[item] == "<" or splited_line[item] == ">" or splited_line[item] == "!"):   
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
        line_count+=1
    if(len(unclosed_strings)>0):
        print("Error: unclosed string found on")
        for error in unclosed_strings:
            print("Line: {0}".format(error))
        sys.exit()
    return splited_source_code

def create_symbol_table_map(token_source_code):
    symbolTableMap = {}

    for line in token_source_code:
        for token in line:
            if (token.token in symbolTableMap):
                if(token.value in symbolTableMap[token.token]):
                    symbolTableMap[token.token][token.value]+=1
                else:                    
                    symbolTableMap[token.token][token.value]=1
            else:
                symbolTableMap[token.token]= {}
                symbolTableMap[token.token][token.value]=1

    
    return symbolTableMap

def print_symbol_table(symbolTableMap):
    symbolTable = PrettyTable(['Token Type', 'Token Value:number of occurrences'])
    for token in symbolTableMap:
        if(token != "comment" and token != "empty_line"):
            symbolTable.add_row([token, symbolTableMap[token]])
    print(symbolTable)
    return symbolTable


                    

# def toToken(source_code):
#     global pypAlphabet
#     global pypKeywords
#     splited_source_code = split_by_separators(source_code)
#     token_source_code = []   
#     line_count=1 
#     for line in splited_source_code:                
#         if(len(line)>0):
#             if(not(isnt_comment(line))):
#                 token_obj = pypToken("comment",line[0])
#                 token_obj.setPos(line_count,1)
#                 token_source_code.append([token_obj])
#             else:
#                 new_line=[]
#                 collum_count=1
#                 for item in line:
#                     if(item in pypAlphabet):
#                         token_obj = pypToken(pypAlphabet[item],item)
#                         token_obj.setPos(line_count,collum_count)
#                         new_line.append(token_obj)
#                     elif(item in pypKeywords):                        
#                         token_obj = pypToken(pypKeywords[item],item)                        
#                         token_obj.setPos(line_count,collum_count)
#                         new_line.append(token_obj)
#                     elif(is_a_number(item)):
#                         token_obj = pypToken("numeral_token",item)
#                         token_obj.setPos(line_count,collum_count)
#                         new_line.append(token_obj)
#                     elif(item.startswith('_str:')):
#                         token_obj = pypToken("literal_token",item[5:])
#                         token_obj.setPos(line_count,collum_count)
#                         new_line.append(token_obj)
#                     else:
#                         token_obj = pypToken("id_token",item)
#                         token_obj.setPos(line_count,collum_count)
#                         new_line.append(token_obj)
#                     collum_count+=1
#                 token_source_code.append(new_line)                
#         else:
#             token_obj = pypToken("empty_line","")
#             token_obj.setPos(line_count,1)
#             token_source_code.append([token_obj]) 
#         line_count+=1   
#     return token_source_code


def shrink_token_source_code(token_source_code):
    shrunk_source_code = []
    for line in token_source_code:
        for token in line:
            if(token.token!="comment" and token.token != "empty_line"):
                shrunk_source_code.append(token)
    return shrunk_source_code

#Transforma os elementos em tokens
def toToken(source_code):
    global pypAlphabet
    global pypKeywords
    splited_source_code = split_by_separators(source_code)
    token_source_code = []   
    line_count=1 
    for line in splited_source_code:                
        if(len(line)>0):
            if(not(isnt_comment(line))):
                token_obj = pypToken("comment",line[0],line_count)                
                token_source_code.append([token_obj])
            else:
                new_line=[]
                collum_count=1
                for item in line:
                    if(item in pypAlphabet and pypAlphabet[item]!="letter" and pypAlphabet[item]!="digit"):
                        token_obj = pypToken(pypAlphabet[item],item,line_count,collum_count)                        
                        new_line.append(token_obj)
                    elif(item in pypKeywords):                        
                        token_obj = pypToken(pypKeywords[item],item,line_count,collum_count)                          
                        new_line.append(token_obj)
                    elif(is_a_number(item)):
                        if(type(eval(item)) is int):
                            token_obj = pypToken("int",item,line_count,collum_count)                        
                            new_line.append(token_obj)
                        else:
                            token_obj = pypToken("float",item,line_count,collum_count)                        
                            new_line.append(token_obj)
                    elif(item.startswith('_str:')):
                        token_obj = pypToken("literal_token",item[5:],line_count,collum_count)                        
                        new_line.append(token_obj)
                    else:
                        token_obj = pypToken("id_token",item,line_count,collum_count)                        
                        new_line.append(token_obj)
                    collum_count+=1
                token_source_code.append(new_line)                
        else:
            token_obj = pypToken("empty_line","",line_count)            
            token_source_code.append([token_obj]) 
        line_count+=1   
    return token_source_code

#Procura por "pyp_alphabet.json"
def load_alphabet_from_json():
    try:
        with open('Alphabet/gbm_alphabet.json') as f:
            global pypAlphabet
            pypAlphabet = json.load(f)                    
    except:
        print("Error: Alphabet file 'gbm_alphabet.json' not found in directort 'Alphabet'. Run 'python alphabet_generator.py' to generate it.")
        sys.exit()

#Procura por "pyp_reserved.json"
def load_keywords_from_json():
    try:
        with open('Reserved/gbm_reserved.json') as f:
            global pypKeywords
            pypKeywords = json.load(f)        
    except:
        print("Error: Keywords file 'gbm_reserved.json' not found in directory 'Reserved'. Run 'python reserved_generator.py' to generate it.")
        sys.exit()

#Le o nome do arquivo entrado depois do script no terminal
def read_from_terminal():
    try:
        return sys.argv[1]
    except:
        print("Error: no input file")
        sys.exit()

#Import o arquivo, separando em linhas. Retorna uma lista de linhas
def import_file(source_code_name):
    test_source_code_name = source_code_name+".pyp"    
    if(os.path.exists(source_code_name)):
        try:
            with open (source_code_name, "r") as myfile:
                source_code=myfile.read().splitlines()
            return source_code    
        except:
            print("Error: Attempt to import file \"{0}\" failed.".format(source_code_name))
            sys.exit()
    elif(os.path.exists(test_source_code_name)):
        try:        
            with open ((test_source_code_name), "r") as second_file:
                source_code=second_file.read().splitlines()
            print("Warning: File \"{0}\" not found. File \"{1}\" found and imported".format(source_code_name,test_source_code_name))
            return source_code
        except:    
            print("Error: File \"{0}\" not found. File \"{1}\" found but attempt to import file failed.".format(source_code_name,test_source_code_name))
            sys.exit()
    else:
        print("Error: File \"{0}\" not found. Attempted to import \"{1}\" but such file doesn't exist either.".format(source_code_name,test_source_code_name))
        sys.exit()
        

    

    

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

#Imprime os tokens
def print_token_source_code(token_source_code,position=True):
    for line in token_source_code:
            for item in line:
                if(item.token!="comment" and item.token!="empty_line"):
                    if(position):
                        print ("{0}:'{1}'.({2},{3}) ").format(item.token,item.value,item.line,item.collum),
                    else:
                        print ("{0}:'{1}'").format(item.token,item.value),
            print 

def print_token_code(token_code,position=True):    

    for item in token_code:            
        if(position):
            print ("{0}:'{1}'.({2},{3}) ").format(item.token,item.value,item.line,item.collum),
        else:
            print ("{0}:'{1}'").format(item.token,item.value),
    print

#Procura por chars que nao estao presentes no alfabeto. Flag de correção por padrão é verdadeira, a menos q função
#   chamada seja chamada com parametro false
def charsAnalyser(source_code,correction=True):
    if(correction):
        warnings = {}       
        for line_it in range(len(source_code)):
            if(len(source_code[line_it])>0):
                if(isnt_comment(source_code[line_it])):                   
                    char_it=0
                    while(char_it < len(source_code[line_it])):                
                        if(not(source_code[line_it][char_it] in pypAlphabet)):                            
                            source_code[line_it]= source_code[line_it][:char_it] + source_code[line_it][char_it + 1:]
                            if(not(line_it in warnings)):
                                warnings[line_it]=1
                            else:
                                warnings[line_it]+=1
                            char_it-=1
                        char_it+=1        
        if(len(warnings)>0):
            print("Warning: invalid character(s) found and removed from")
            for warning in warnings:
                print("Line {0}: {1} invalid character(s)".format((warning+1),warnings[warning]))
        return source_code
    else:
        errors = []    
        line_count = 1
        for line in source_code:
            if(len(line)>0):
                if(isnt_comment(line)):                   
                    for char in line:            
                        if(not(char in pypAlphabet)):                
                            errors.append(line_count)
                            break
                            #errors.append(wrongChar(line_count,char_count))                    
            line_count+=1
        
        if(len(errors)!=0):
            print("Error: Invalid characters found on")
            for error in errors:
                print("Line: {0}".format(error))          
            sys.exit() 
        
