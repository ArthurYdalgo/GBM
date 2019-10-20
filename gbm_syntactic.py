# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from lark import Lark #biblioteca de bnf

def variable_mapper(token_source_code):
    
    l = Lark('''start: WORD "," WORD "!"
            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
         ''')



#def variable_checker(token_source_code,variable_map):
