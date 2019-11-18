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

def asToken(str_):
    return "<"+str_+">"

def is_Terminal(token_type):
    return not(isnt_Terminal(token_type))

for dataType in data_type_list:
    var_shortcut[dataType] = derivations['<variable_declaration>']
var_shortcut["canvas"] = derivations['<variable_declaration>']

def statementsGraphParser(token_code,cTokenIndex,cDerivationName):
    global gProbe
    nToken = token_code[cTokenIndex+1]
    cState = token_code[cTokenIndex].value       
    
    while(True):       
        #a = str(raw_input(""))        
        #print("cState:"+cState)   
        
        if(token_code[cTokenIndex].token=="id_token"):                 
            cState = "<id_token>"
        
        if(token_code[cTokenIndex].token=="literal_token"):                        
            cState = "<literal_token>"
        
        if(token_code[cTokenIndex].token == "sketchType_token"):                        
            cState = "<sketchType_token>"
     
        #print(cDerivationName)
        if(cDerivationName=="<for>"):            
            if(nToken.token=="int" or nToken.token=="float"):
                nToken.value = asToken(nToken.token)+cState
        
                
        #if(cDerivationName == "<attribution>" and token_code[cTokenIndex].token == "id_token"): #nao sei se vou precisar de novo
        if(token_code[cTokenIndex].token == "id_token"):            
            if(not(token_code[cTokenIndex].value in code_variables)):
                print("Error (line {0}): variable '{1}' was not declared.".format(token_code[cTokenIndex].line,token_code[cTokenIndex].value))
                sys.exit()        
        
        if(cState=="(" and cDerivationName=="<while>" and token_code[cTokenIndex-1].value=="while"):
            #print("tem while")
            cState = "<operation>"            
            opString=""
            while(True):                
                if(cTokenIndex<len(token_code)-1):
                    cToken = nToken
                    cTokenIndex+=1
                    nToken = token_code[cTokenIndex+1]
                    if(cToken.value==")" and nToken.value=="{"):
                        cState = ")"
                        break
                    if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

                        if(cToken.value == "^"):
                            opString+="**"
                        elif(cToken.token == "id_token"):
                            if(cToken.value in code_variables):
                                opString+='code_variables["'+cToken.value+'"] '
                            else:
                                print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
                                sys.exit()
                        else:
                            opString+=cToken.value+" "
                else:
                    print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
            if(len(opString)==0):
                print("Syntax error (line {0}): logic operation required.".format(cToken.line))
                sys.exit()
            else:
                try:
                    eval("'"+opString+"'")              
                except:
                    print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,opString))    
                    sys.exit()
            

        if(nToken.value in derivations[cDerivationName][cState] or "<"+nToken.token+">" in derivations[cDerivationName][cState]):#walk  

            #  
            

            if(nToken.value == "{"):                        
                gProbe+=1
                cTokenIndex+=1
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]                
                if(nToken.value in code_shortcuts):
                    cDerivationName = code_shortcuts[nToken.value]
                elif("<"+nToken.token+">" in code_shortcuts):
                    cDerivationName = code_shortcuts["<"+nToken.token+">"]                    
                else:
                    sError(nToken.line,nToken.value)
                
                cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,cDerivationName)   
                cToken = token_code[cTokenIndex]                
                if(cToken.value in code_shortcuts):
                    cDerivationName = code_shortcuts[cToken.value]
                    cState = cToken.value
                    nToken = token_code[cTokenIndex+1]     
                elif("<"+cToken.token+">" in code_shortcuts):
                    cDerivationName = code_shortcuts["<"+cToken.token+">"]                    
                    cState = cToken.value
                    nToken = token_code[cTokenIndex+1]  
                elif(cToken.value == "}"):                                            
                    if(gProbe == 0):
                        sError(nToken.line,nToken.value)
                    else:                                    
                        gProbe-=1
                        return cTokenIndex+1
                elif(cToken.value=="end"):
                    if(gProbe>0):
                        sError(nToken.line,nToken.value)
                    elif(gProbe==0):
                        pass #codigo terminou    
                else:                                   
                    sError(cToken.line,cToken.value)


            ##ATRIBUICAO DE STRINGS  
            elif(nToken.token == "literal_token" and cDerivationName == "<attribution>"):                
                pass
                
                
                #atribution (later)  

            ##ATRIBUICAO DE SKETCH
            elif(nToken.token == "sketchType_token" and cDerivationName == "<attribution>"):                
                if(nToken.value in sketch_shortcuts):
                    sketchDerivation = sketch_shortcuts[nToken.value]
                    cState = nToken.value
                    cTokenIndex+=1
                    nToken = token_code[cTokenIndex+1]  
                    while(True):                        
                        if(token_code[cTokenIndex].token == "int"):
                            if(asToken("int") in derivations[sketchDerivation]):
                                cState = asToken("int")
                            elif(asToken("int")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("int")+token_code[cTokenIndex-1].value
                        elif(token_code[cTokenIndex].token == "float"):
                            if(asToken("float") in derivations[sketchDerivation]):
                                cState = asToken("float")
                            elif(asToken("float")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("float")+token_code[cTokenIndex-1].value
                        elif(token_code[cTokenIndex].token == "literal_token"):
                            if(asToken("literal_token") in derivations[sketchDerivation]):
                                cState = asToken("literal_token")
                            elif(asToken("literal_token")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("literal_token")+token_code[cTokenIndex-1].value
                        

                        if(nToken.value in derivations[sketchDerivation][cState] or "<"+nToken.token+">" in derivations[sketchDerivation][cState] or "<"+nToken.token+">"+cState in derivations[sketchDerivation][cState]):        
                            cState = nToken.value
                            cTokenIndex+=1
                            nToken = token_code[cTokenIndex+1]  
                        elif(nToken.value==";"):                            
                            #atribution (later)                                   
                            cState = nToken.value
                            cTokenIndex+=1
                            nToken = token_code[cTokenIndex+1]                              
                            if(nToken.value in code_shortcuts):
                                cDerivationName = code_shortcuts[nToken.value]
                                cTokenIndex+=1
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                                break;
                            elif("<"+nToken.token+">" in code_shortcuts):
                                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                                cState = "<"+nToken.token+">"
                                cTokenIndex+=1
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                                break;
                            elif(nToken.value == "}"):                                
                                if(gProbe == 0):
                                    sError(nToken.line,nToken.value)
                                else:                                    
                                    gProbe-=1
                                    return cTokenIndex+2
                            elif(nToken.value=="end"):
                                if(gProbe>0):
                                    sError(nToken.line,nToken.value)
                                elif(gProbe==0):
                                    pass #codigo terminou 
                            else:                                
                                sError(nToken.line,nToken.value) 
                        elif(nToken.value == "}"):                                
                            if(gProbe == 0):
                                sError(nToken.line,nToken.value)
                            else:                                    
                                gProbe-=1
                                return cTokenIndex+2
                        elif(nToken.value=="end"):
                            if(gProbe>0):
                                sError(nToken.line,nToken.value)
                            elif(gProbe==0):
                                pass #codigo terminou 
                        else:
                            sError(nToken.line,nToken.value)  

                        #sys.exit()
                else:
                    sError(nToken.line,nToken.value)
                


                #atribution sketch(later)  
            cTokenIndex+=1
            cState=nToken.value
            nToken = token_code[cTokenIndex+1]                
        #elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="id_token"):
        elif(nToken.value == "}"):
        
            if(gProbe == 0):
                
                sError(nToken.line,nToken.value)
            else:                
                gProbe-=1
                return cTokenIndex+2
        elif(nToken.value=="end"):
            if(gProbe>0):
                sError(nToken.line,nToken.value)
            elif(gProbe==0):
                pass #codigo terminou
        elif(cState == ";"):#end of statement                  
            if(nToken.value in code_shortcuts):
                cDerivationName = code_shortcuts[nToken.value]
                cTokenIndex+=1
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]  
            elif("<"+nToken.token+">" in code_shortcuts):
                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                cState = "<"+nToken.token+">"
                cTokenIndex+=1
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]  
            
            else:                
                sError(nToken.line,nToken.value)  
        
        ##ATRIBUICAO DE OPERAÇOES
        elif(cDerivationName == "<attribution>"):  
                             
            #atribuicao de operaçoes                            
            if(nToken.value == ";"):
                sError(nToken.line,";")
            if(nToken.token == "id_token" or nToken.token=="boolean_token" or is_a_number(nToken.value) or nToken.value == "("): 
                cState = "<operation>"
                opString = ""
                while(True):                        
                    if(cTokenIndex<len(token_code)-1):
                        cToken = nToken
                        cTokenIndex+=1
                        nToken = token_code[cTokenIndex+1]
                        if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

                            if(cToken.value == "^"):
                                opString+="**"
                            elif(cToken.token == "id_token"):
                                if(cToken.value in code_variables):
                                    opString+='code_variables["'+cToken.value+'"] '
                                else:
                                    print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
                                    sys.exit()
                            else:
                                opString+=cToken.value+" "
                        elif(cToken.value==";"):                                                                               
                            if(nToken.value in code_shortcuts):
                                cDerivationName = code_shortcuts[nToken.value]
                                cTokenIndex+=1
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                            elif("<"+nToken.token+">" in code_shortcuts):
                                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                                cState = "<"+nToken.token+">"
                                cTokenIndex+=1
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                            elif(nToken.value == "}"):                                
                                if(gProbe == 0):
                                    sError(nToken.line,nToken.value)
                                else:                                    
                                    gProbe-=1
                                    return cTokenIndex+2
                            elif(nToken.value=="end"):
                                if(gProbe>0):
                                    sError(nToken.line,nToken.value)
                                elif(gProbe==0):
                                    pass #codigo terminou
                            else:                                                        
                                sError(nToken.line,nToken.value)  
                            break
                        else:
                            sError(cToken.line,cToken.value)
                    else:
                        print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
                try:
                    eval("'"+opString+"'")       
                except:
                    print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,opString))    
                    sys.exit()
       
        else:
            sError(nToken.line,nToken.value)
                    


                
    
    
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
    if(nToken.value=="begin"):
        cTokenIndex+=1
        nToken = token_code[cTokenIndex+1]             
        if(nToken.value in code_shortcuts):                        
            statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value])
        elif("<"+nToken.token+">" in code_shortcuts):            
            statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"])
        else:        
            sError(nToken.line,nToken.value)

    elif(cTokenIndex+1==len(token_code)):
        print("Syntax error: unexpected end of file after line {0}. 'begin' was expected.".format(nToken.line))
    else:
        print("Syntax error (line {0}): unexpected '{1}'. 'begin' was expected.".format(nToken.line,nToken.value))
    return error



# for graph in derivations:
#      plt.figure(graph)
#      nx.draw(derivations[graph], with_labels=True,)
#plt.show()



    


 