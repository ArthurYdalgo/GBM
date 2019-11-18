# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
import networkx as nx
import matplotlib.pyplot as plt
from parseBNF import listOfGraphs,listOfSketches

class Variable():
    def __init__(self,var_type_,token):
        self.type = var_type_
        self.name = token.value
        self.line = token.line

code_variables = {}

derivations={}

code_shortcuts = {}

sketch_shortcuts = {}

var_shortcut = {}

eqSide = "L"

gProbe=0

for graph in listOfGraphs:
    filename = 'parseGraphs/{0}.gml'.format(graph)    
    name = "<{0}>".format(graph)
    derivations[name] = nx.read_gml(filename)
    if(graph != "base_code" and graph != "variable_declaration" and graph != "attribution"):
        code_shortcuts[graph]= name

for graph in listOfSketches:
    filename = 'parseGraphs/{0}.gml'.format(graph)    
    name = "<{0}>".format(graph)
    derivations[name] = nx.read_gml(filename)
    sketch_shortcuts[graph] = name


code_shortcuts["<id_token>"] = "<attribution>"

def is_a_number(str):
    try:
        float(str)
        return True
    except:
        return False

def sError(line,value):
    print("Syntax error (line {0}): unexpected '{1}'".format(line,value))
    sys.exit()

def isnt_Terminal(token_type):
    if(token_type[0]=="<" and token_type[len(token_type)-1]==">"):
        return True
    else:
        return False

def is_Terminal(token_type):
    return not(isnt_Terminal(token_type))

for dataType in data_type_list:
    var_shortcut[dataType] = derivations['<variable_declaration>']
var_shortcut["canvas"] = derivations['<variable_declaration>']

#Syntax parser
def parser(token_code):
    parseError = graphParse(token_code)
    if(len(parseError)>0):
        print("Syntax error (line {0}}): unexpected '{1}' after '{2}'".format(parseError["line"],parseError["nToken"],parseError["cToken"]))
        sys.exit()
    else:
        return token_code

# def statementsGraphParser(token_code,cTokenIndex,cDerivationName):
#     global gProbe
#     nToken = token_code[cTokenIndex+1]
#     cState = token_code[cTokenIndex].value
#     while(True):        
#         if(nToken.value in derivations[cDerivationName][cState]):#walk
#             if(nToken.value == "{"):        
#                 gProbe+=1
#                 cTokenIndex+=1
#                 cState = nToken.value
#                 nToken = token_code[cTokenIndex+1]                
#                 if(nToken.value in code_shortcuts):
#                     cDerivationName = code_shortcuts[nToken.value]
#                 elif("<"+nToken.token+">" in code_shortcuts):
#                     cDerivationName = code_shortcuts["<"+nToken.token+">"]                    
#                 else:
#                     sError(nToken.line,nToken.value)
#                 cTokenIndex = statementsGraphParser(token_code,cTokenIndex,cDerivationName)                    

#         elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="id_token"):
        
#         elif(cDerivationName == "<attribution>"):
#             if(nToken.token == "literal_token"):#atribuiçao de literal
#                 #atribution (later)
#                 cState = "<literal_token>"
#                 cTokenIndex+=1
#                 nToken = token_code[cTokenIndex+1]
#             elif(nToken.token == "sketchType_token"):#desenho
#                 while(True):
#                     #to do...

#             #operaçoes                
#             elif(nToken.token == "id_token" or nToken.token=="boolean_token" or is_a_number(nToken.value) or nToken.value == "("): 
#             opString = ""
#                 while(True):                        
#                     if(cTokenIndex<len(token_code-1)):
#                         cToken = nToken
#                         cTokenIndex+=1
#                         nToken = token_code[cTokenIndex+1]
#                         if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or is_a_number(cToken.value)):
#                             if(cToken.value == "^"):
#                                 cToken.value = "**"
#                             elif(cToken.token == "id_token"):
#                                 cToken.value = ""
#                     else:
#                         print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line)

        
#         elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="literal_token"):

#         elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="boolean_token"):

        
#         elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and (nToken.token!="id_token" or nToken.token!="boolean_token" or nToken.token!="literal_token")):
#             cTokenIndex        

#         elif(cState == ";"):#end of statement
#             if(nToken.value in code_shortcuts):
#                 cDerivationName = code_shortcuts[nToken.value]
#             elif("<"+nToken.token+">" in code_shortcuts):
#                 cDerivationName = code_shortcuts["<"+nToken.token+">"]
#                 cState = "<"+nToken.token+">"
#             else:
#                 sError(nToken.line,nToken.value)
#         elif(nToken.value == "}"):
#             if(gProbe == 0):
#                 sError(nToken.line,nToken.value)
#             else:
#                 gProbe-=1
#                 return cTokenIndex+1
#         elif(nToken.value=="end"):
#             if(gProbe>0):
#                 sError(nToken.line,nToken.value)


                
    
    
    # if(nToken.value in derivations[cDerivationName]):
    #     cTokenIndex+=1
    #     statementsGraphParser(token_code,cTokenIndex,cDerivationName)
    # elif(token_code[cTokenIndex].value=="{"):
    #     gProbe+=1
    #     if(nToken.value in code_shortcut):
    #         cTokenIndex+=1
    #         statementsGraphParser(token_code,cTokenIndex,code_shortcut[nToken])
    #     else:
    #         print("Syntax error (line {0}): unexpected '{1}'".format(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value))
    #         sys.exit()    
    # elif(token_code[cTokenIndex].value=="}"):
    #     gProbe-=1
    #     if(nToken.value in code_shortcut):
    #         cTokenIndex+=1
    #         statementsGraphParser(token_code,cTokenIndex,code_shortcut[nToken])
    #     else:
    #         print("Syntax error (line {0}): unexpected '{1}'".format(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value))
    #         sys.exit()  
    # elif(token_code[cTokenIndex].value==";"):
    #     if(nToken.value in code_shortcut):
    #         cTokenIndex+=1
    #         statementsGraphParser(token_code,cTokenIndex,code_shortcut[nToken])
    #     else:
    #         print("Syntax error (line {0}): unexpected '{1}'".format(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value))
    #         sys.exit()  


    



def graphParse(token_code):
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
        if(nToken.value in cDerivation[cState] or "<"+nToken.token+">" in cDerivation[cState]):            
            if(nToken.value == "begin"):                
                break            
            
            cState = nToken.value                        
            if(nToken.token == "id_token"):                
                declareList.append(Variable(cDataType,nToken))     
                cState = "<id_token>"
            cTokenIndex+=1
            nToken=token_code[cTokenIndex+1]          
            if(nToken.token=="dataType_token"):
                cDataType = nToken.value                          
        else:                                                     
            if(cTokenIndex==-1):
                print("Syntax error (line {0}): unexpected '{1}'".format(nToken.line,nToken.value))
            else:
                print("Syntax error (line {0}): unexpected '{1}'".format(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value))
            sys.exit()                       
        
    
    for var_ in declareList:        
        if(var_.name in code_variables):
            print("Error: variable '{0}' in line {1} already declared previously (in line {2})".format(var_.name,var_.line,code_variables[var_.name].line))
            sys.exit()
        else:
            code_variables[var_.name] = var_      
        

    
    #code statements parser


    # if(nToken.value=="begin"):
    #     cTokenIndex+=1
    #     nToken = token_code[cTokenIndex+1]     
    #     if(nToken.value in code_shortcut):
    #         statementsGraphParser(token_code,cTokenIndex,code_shortcut[nToken.value])
    #     elif("<"+nToken.token+">" in code_shortcut):
    #         statementsGraphParser(token_code,cTokenIndex,code_shortcut["<"+nToken.value+">"])
    #     else:
    #         sError(nToken.line,nToken.value)

    # elif(cTokenIndex+1==len(token_code)):
    #     print("Syntax error: unexpected end of file after line {0}. 'begin' was expected.".format(nToken.line))
    # else:
    #     print("Syntax error (line {0}): unexpected '{1}'. 'begin' was expected.".format(nToken.line,nToken.value))
    # return error



for graph in derivations:
     plt.figure(graph)
     nx.draw(derivations[graph], with_labels=True, font_weight='bold')
#plt.show()



    


 