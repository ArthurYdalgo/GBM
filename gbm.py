#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
import json #biblioteca para arquivos json
import re #biblioteca de regex
from gbm_lexical import *


#Main chama as outras funcoes
def main():
    #Importacao do alfabeto
    load_alphabet_from_json()
    
    #Importacao de palavras reservadas
    load_keywords_from_json()
    
    #Importacao do codigo fonte
    source_code_name = read_from_terminal()
    source_code = import_file(source_code_name)    

    #Remocao de espacos
    source_code = space_removal(source_code)

    #Remocao de comentarios no final da linha
    source_code = comment_removal(source_code)

    #Imprime código apos tratamentos
    #print_code(source_code)

    #Varredura de caracteres
    source_code = charsAnalyser(source_code)
    
    #Transforma o código fonte em tokens
    token_source_code = toToken(source_code)

    #print_token_code(token_source_code)

    #Checagem de nomeclatura de tokens de indentificação
    check_tokens_id_values(token_source_code)    
    
   
main()#Chama a main



