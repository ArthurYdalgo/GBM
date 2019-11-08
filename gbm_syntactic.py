# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
import networkx as nx
import matplotlib.pyplot as plt
from parseBNF import listOfGraphs

class Variable():
    def __init__(self,var_type_,token):
        self.type = var_type_
        self.name = token.value
        self.line = token.line


code_variables = {}

derivations={}

var_shortcut = {}
code_shortcut = {}



for graph in listOfGraphs:
    filename = 'parseGraphs/{0}.gml'.format(graph)    
    name = "<{0}>".format(graph)
    derivations[name] = nx.read_gml(filename)


for dataType in data_type_list:
    var_shortcut[dataType] = derivations['<variable_declaration>']
var_shortcut["canvas"] = derivations['<variable_declaration>']


def isnt_Terminal(token_type):
    if(token_type[0]=="<" and token_type[len(token_type)-1]==">"):
        return True
    else:
        return False

def is_Terminal(token_type):
    return not(isnt_Terminal(token_type))

#Syntax parser
def parser(token_code):
    parseError = graphParse(token_code)
    if(len(parseError)>0):
        print("Syntax error (line {0}}): unexpected '{1}' after '{2}'".format(parseError["line"],parseError["nToken"],parseError["cToken"]))
        sys.exit()
    else:
        return token_code


def graphParse(token_code):
    error={}
    gProbe=0
    if(len(token_code)==0):
        print("Source code is empty. Nothing to be done here =P")
        sys.exit()
    cTokenIndex = -1
    nToken = token_code[0]
    cDerivationName = "<base_code>"
    cDerivation = derivations[cDerivationName]
    
    cState = '<base_code>'
    nState = 'var'
    cDataType = ""
    #var declaration parser
    declareList = []
    while(True):
        if(nToken.value in cDerivation[cState]):            
            if(nToken.value == "begin"):                
                break            
            cState = nToken.value                        
            if(nToken.token == "id_token"):
                
                cState = "<id_token>"
            cTokenIndex+=1
            nToken=token_code[cTokenIndex+1]          
            if(nToken.token=="dataType_token"):
                cDataType = nToken.value                        
        else:                  
            if(nToken.token=="id_token" and cDerivationName=="<variable_declaration>"): 
                declareList.append(Variable(cDataType,nToken))                                
                cState = nToken.value                                
                if(nToken.token == "id_token"):                        
                    cState = "<id_token>"
                cTokenIndex+=1
                nToken=token_code[cTokenIndex+1]   
            elif(len(cDerivation[cState])==0 and gProbe>0):    
                
                gProbe-=1
                cState = "<variable_declaration>"
                cDerivationName = "<base_code>"
                cDerivation = derivations[cDerivationName]  
            elif(nToken.value in var_shortcut):
                
                cDerivationName = "<variable_declaration>"
                cDerivation = derivations[cDerivationName]
                cState = "<variable_declaration>"
                gProbe+=1
            else:
                if(cTokenIndex==-1):
                    print("Syntax error (line {0}): unexpected '{1}'".format(nToken.line,nToken.value))
                else:
                    print("Syntax error (line {0}): unexpected '{1}'".format(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value))
                sys.exit()

    for var_ in declareList:        
        if(var_.name in code_variables):
            print("Error: variable '{0}' already declared".format(var_.name))
            sys.exit()
        else:
            code_variables[var_.name] = var_           
            

    # #code instructions parser
    # while(True):
    #     if(is_Terminal( cState ) and cState == cToken.value):
    #         if(cTokenIndex!=len(token_code)-1):#Ainda tem tokens a serem analisados
                
    #         else:#fim do codigo
    #             if(cState == "end" and gProbe==0):


    #     elif(isnt_Terminal(cState)):
    #         cDerivation = shortcut[cToken.value]
    #         gProbe+=1
    return error



# for graph in derivations:
#     plt.figure(graph)
#     nx.draw(derivations[graph], with_labels=True, font_weight='bold')
#plt.show()



    


 