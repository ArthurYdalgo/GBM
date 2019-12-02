# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
import networkx as nx
#import matplotlib.pyplot as plt
from parseBNF import listOfGraphs,listOfSketches
import inspect
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import numpy as np

class Variable():
    def __init__(self,var_type_,token):
        self.type = var_type_
        self.name = token.value
        self.line = token.line
        if(var_type_=="float" or var_type_=="int"):
            self.value = 0
        elif(var_type_=="string"):
            self.value=""
        elif(var_type_ == "bool"):
            self.value=False
        else:
            self.value = []

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

def sError(line,value,errorLine):
    #print("Syntax error (line {0}): unexpected '{1}'...{2}".format(line,value,errorLine))
    print("Syntax error (line {0}): unexpected '{1}'".format(line,value))
    sys.exit()

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def hex_to_rgb(value):        
    value = value[1:]    
    lv = len(value)
    tupla = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return tupla

def isnt_Terminal(token_type):
    if(token_type[0]=="<" and token_type[len(token_type)-1]==">"):
        return True
    else:
        return False

def asToken(str_):
    return "<"+str_+">"

    

def check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName):    
    if(cTokenIndex==len(token_code)-1):        
        if(token_code[cTokenIndex].value=="end" and (token_code[cTokenIndex-1].value==";" or token_code[cTokenIndex-1].value=="}")):              
            if(gProbe>0):
                sError(nToken.line,nToken.value,lineno())
            elif(gProbe==0):
                return
        elif(token_code[cTokenIndex].value=="end"):
            sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())
        else:
            print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
            sys.exit()
    elif(token_code[cTokenIndex].value=="break"):        
        if(not(isLoop)):
            sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno()) 
    elif(token_code[cTokenIndex].token=="id_token" and cDerivationName!="<base_code>"):                    
        if(not(token_code[cTokenIndex].value in code_variables)):
            print("Error (line {0}): variable '{1}' was not declared.".format(token_code[cTokenIndex].line,token_code[cTokenIndex].value))
            sys.exit()  
    elif(cDerivationName!="<if>" and cDerivationName!="<else>"):
        #print("ok... checando proximos")
        if(token_code[cTokenIndex].value=="else"):            
            sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())
            #a = raw_input("")
    
def list_to_sketch(sketch_properties_list):
    image = Image.new('RGBA',(int(sketch_properties_list[1]),int(sketch_properties_list[2])))
    draw = ImageDraw.Draw(image)
    if(sketch_properties_list[0]=="circle"):
        if(sketch_properties_list[3][0]=="%"):            
            hex_color = sketch_properties_list[3][1:]
            print(hex_to_rgb(hex_color))
            draw.ellipse((0, 0, int(sketch_properties_list[1]), int(sketch_properties_list[2])), fill = hex_to_rgb(hex_color))
        else:
            draw.ellipse((0, 0, int(sketch_properties_list[1]), int(sketch_properties_list[2])), fill = sketch_properties_list[3])
    elif(sketch_properties_list[0]=="square"):
        if(sketch_properties_list[3][0]=="%"):
            hex_color = sketch_properties_list[3][1:]
            print(hex_to_rgb(hex_color))
            draw.rectangle((0, 0, int(sketch_properties_list[1]), int(sketch_properties_list[2])), fill = hex_to_rgb(hex_color))
        else:
            draw.rectangle((0, 0, int(sketch_properties_list[1]), int(sketch_properties_list[2])), fill = sketch_properties_list[3])        
    #elif(sketch_properties_list[0]=="circle"):
    image.show()
    return np.array(image)


def is_Terminal(token_type):
    return not(isnt_Terminal(token_type))

for dataType in data_type_list:
    var_shortcut[dataType] = derivations['<variable_declaration>']
var_shortcut["canvas"] = derivations['<variable_declaration>']

def statementsGraphParser(token_code,cTokenIndex,cDerivationName,isLoop):
    global code_variables
    
    global gProbe
    nToken = token_code[cTokenIndex+1]
    cState = token_code[cTokenIndex].value       
    
    while(True):       
        #a = str(raw_input(""))        
        #print("cState:"+cState)                   
        check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)        
        
        if(token_code[cTokenIndex].token=="id_token"):                
            cState = "<id_token>"        
        

        if(nToken.token=="id_token"):            
            if(not(nToken.value in code_variables)):
                print("Error (line {0}): variable '{1}' was not declared.".format(nToken.line,nToken.value))
                sys.exit()  
        
        if(token_code[cTokenIndex].token=="literal_token"):                        
            cState = "<literal_token>"
        
        if(token_code[cTokenIndex].token == "sketchType_token"):                        
            cState = "<sketchType_token>"
     
        #sError(nToken.line,nToken.value,lineno())vationName)
        if(cDerivationName=="<for>"):            
            if(nToken.token=="int" or nToken.token=="float"):
                nToken.value = asToken(nToken.token)+cState                
            

        
        #if(cDerivationName == "<attribution>" and token_code[cTokenIndex].token == "id_token"): #nao sei se vou precisar de novo
        if(token_code[cTokenIndex].token == "id_token"):            
            if(not(token_code[cTokenIndex].value in code_variables)):
                print("Error (line {0}): variable '{1}' was not declared.".format(token_code[cTokenIndex].line,token_code[cTokenIndex].value))
                sys.exit()   

        #print(cDerivationName)     
        
        if((cState=="(" and cDerivationName=="<while>" and token_code[cTokenIndex-1].value=="while")or (cState=="(" and cDerivationName=="<if>" and token_code[cTokenIndex-1].value=="if") or (cState=="(" and cDerivationName=="<else>" and token_code[cTokenIndex-1].value=="if")):            
            #print("tem while")
            cState = "<operation>"            
            opString=""
            sString=""            
            while(True):                
                if(cTokenIndex<len(token_code)-1):
                    cToken = nToken
                    cTokenIndex+=1
                    check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                    
                    nToken = token_code[cTokenIndex+1]
                    if(cToken.value==")" and nToken.value=="{"):
                        cState = ")"
                        break
                    if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

                        if(cToken.value == "^"):               
                            opString+="** "
                            sString+="^ "
                        elif(cToken.token == "id_token"):
                            if(cToken.value in code_variables):
                                opString+='code_variables["'+cToken.value+'"].value '
                                sString+=cToken.value+' '
                            else:
                                print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
                                sys.exit()
                        else:
                            opString+=cToken.value+" "
                            sString+=cToken.value+" "
                else:
                    print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
            if(len(opString)==0):
                print("Syntax error (line {0}): logic operation required.".format(cToken.line))
                sys.exit()
            else:
                try:
                    #print(opString)                    
                    eval(opString)     
                    #print(eval(opString))                                          
                except:
                    print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,sString))    
                    sys.exit()
            
        if(not(cState in derivations[cDerivationName])):
            sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())
        
            
        if(nToken.value in derivations[cDerivationName][cState] or "<"+nToken.token+">" in derivations[cDerivationName][cState]):#walk             
            if(cState=="else"):#MAGIC... DON'T KNOW HOW OR WHY, BUT IT WORKS...
                sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())                
            

            if(nToken.value == "{"):                        
                gProbe+=1
                cTokenIndex+=1
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]                
                if(nToken.value in code_shortcuts):    
                    if(cDerivationName=="<for>" or cDerivationName=="<while>"):                
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value],True) 
                    else:
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value],False) 
                elif("<"+nToken.token+">" in code_shortcuts):                                        
                    if(cDerivationName=="<for>" or cDerivationName=="<while>"):
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"],True) 
                    else:
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"],False) 
                else:
                    sError(nToken.line,nToken.value,lineno())
                
                
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
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
                        sError(nToken.line,nToken.value,lineno())
                    else:                                    
                        gProbe-=1
                        return cTokenIndex+1
                elif(cToken.value=="end"):
                    if(gProbe>0):
                        sError(nToken.line,nToken.value,lineno())
                    elif(gProbe==0):
                        return  
                else:                                   
                    sError(cToken.line,cToken.value,lineno())


            ##ATRIBUICAO DE STRINGS  
            elif(nToken.token == "literal_token" and cDerivationName == "<attribution>"):   
                varName = token_code[cTokenIndex-1].value           
                code_variables[varName].value = nToken.value;
                cTokenIndex+=1
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                cState = token_code[cTokenIndex]
                nToken = token_code[cTokenIndex+1]                                

            ##ATRIBUICAO DE SKETCH
            elif(nToken.token == "sketchType_token" and cDerivationName == "<attribution>"):                
                if(nToken.value in sketch_shortcuts):                    
                    sketchDerivation = sketch_shortcuts[nToken.value]
                    varName = token_code[cTokenIndex-1].value                     
                    cState = nToken.value
                    cTokenIndex+=1
                    check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                    #print(token_code[cTokenIndex].value)
                    
                    nToken = token_code[cTokenIndex+1]  
                    sketch_properties_list=[]                
                    sketch_properties_list.append(cState)    
                    while(True):                        
                        if(token_code[cTokenIndex].token == "int"):
                            if(asToken("int") in derivations[sketchDerivation]):
                                cState = asToken("int")
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                            elif(asToken("int")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("int")+token_code[cTokenIndex-1].value
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                        elif(token_code[cTokenIndex].token == "float"):
                            if(asToken("float") in derivations[sketchDerivation]):
                                cState = asToken("float")
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                            elif(asToken("float")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("float")+token_code[cTokenIndex-1].value
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                        elif(token_code[cTokenIndex].token == "literal_token"):
                            if(asToken("literal_token") in derivations[sketchDerivation]):
                                cState = asToken("literal_token")
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                            elif(asToken("literal_token")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
                                cState = asToken("literal_token")+token_code[cTokenIndex-1].value
                                sketch_properties_list.append(token_code[cTokenIndex].value)
                        

                        if(nToken.value in derivations[sketchDerivation][cState] or "<"+nToken.token+">" in derivations[sketchDerivation][cState] or "<"+nToken.token+">"+cState in derivations[sketchDerivation][cState]):                                  
                            cState = nToken.value
                            cTokenIndex+=1
                            check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                            
                            nToken = token_code[cTokenIndex+1]  
                        elif(nToken.value==";"):      
                            #attribution
                            code_variables[varName].value = list_to_sketch(sketch_properties_list)    
                            cState = nToken.value
                            cTokenIndex+=1
                            check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                            
                            nToken = token_code[cTokenIndex+1]                              
                            if(nToken.value in code_shortcuts):
                                cDerivationName = code_shortcuts[nToken.value]
                                cTokenIndex+=1
                                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                                break;
                            elif("<"+nToken.token+">" in code_shortcuts):
                                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                                cState = "<"+nToken.token+">"
                                cTokenIndex+=1
                                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                                break;
                            elif(nToken.value == "}"):                                
                                if(gProbe == 0):
                                    sError(nToken.line,nToken.value,lineno())
                                else:                                    
                                    gProbe-=1
                                    return cTokenIndex+2
                            elif(nToken.value=="end"):
                                if(gProbe>0):
                                    sError(nToken.line,nToken.value,lineno())
                                elif(gProbe==0):
                                    return
                            else:                                
                                sError(nToken.line,nToken.value,lineno()) 
                        elif(nToken.value == "}"):                                
                            if(gProbe == 0):
                                sError(nToken.line,nToken.value,lineno())
                            else:                                    
                                gProbe-=1
                                return cTokenIndex+2
                        elif(nToken.value=="end"):
                            if(gProbe>0):
                                sError(nToken.line,nToken.value,lineno())
                            elif(gProbe==0):
                                return
                        else:
                            sError(nToken.line,nToken.value,lineno())  

                        #sys.exit()
                else:
                    sError(nToken.line,nToken.value,lineno())
                


                #atribution sketch(later)  
            
            if(token_code[cTokenIndex].value=="end"):
                if(gProbe>0):
                    print("Syntax Error (line {0}): unexpected '{1}'")
                elif(gProbe==0):
                    
                    return
                    pass #codigo terminou
            cTokenIndex+=1
            check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
            
            cState=nToken.value
            nToken = token_code[cTokenIndex+1]                
        #elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="id_token"):
        elif(nToken.value == "}"):
        
            if(gProbe == 0):
                
                sError(nToken.line,nToken.value,lineno())
            else:                
                gProbe-=1
                return cTokenIndex+2
        elif(nToken.value=="end"):
            if(gProbe>0):
                sError(nToken.line,nToken.value,lineno())
            elif(gProbe==0):
                return
        elif(cState == ";"):#end of statement                  
            if(nToken.value in code_shortcuts):
                cDerivationName = code_shortcuts[nToken.value]
                cTokenIndex+=1
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]  
            elif("<"+nToken.token+">" in code_shortcuts):
                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                cState = "<"+nToken.token+">"
                cTokenIndex+=1
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]  
            
            else:                
                sError(nToken.line,nToken.value,lineno())  
        
        ##ATRIBUICAO DE OPERAÇOES
        elif(cDerivationName == "<attribution>"):  
            
            #atribuicao de operaçoes                            
            if(nToken.value == ";"):
                sError(nToken.line,";",lineno())
            if((nToken.token == "id_token" or nToken.token=="boolean_token" or is_a_number(nToken.value) or nToken.value == "(")and token_code[cTokenIndex-1].token=="id_token"): 
                cState = "<operation>"
                varName = token_code[cTokenIndex-1].value                
                opString = ""
                sString=""
                while(True):                        
                    if(cTokenIndex<len(token_code)-1):
                        cToken = nToken
                        cTokenIndex+=1
                        check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                        
                        nToken = token_code[cTokenIndex+1]
                        if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

                            if(cToken.value == "^"):
                                opString+="** "
                                sString+="^ "
                            elif(cToken.token == "id_token"):
                                if(cToken.value in code_variables):
                                    opString+='code_variables["'+cToken.value+'"].value '
                                    sString+=cToken.value+' '
                                else:
                                    print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
                                    sys.exit()
                            else:
                                opString+=cToken.value+" "
                                sString+=cToken.value+" "
                        elif(cToken.value==";"):     
                            try:
                                #print(opString)  
                                eval(opString)                  
                                #print(eval(opString))                                
                                code_variables[varName].value = eval(opString)
                            except:
                                print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,sString))    
                                sys.exit()                                                                          
                            if(nToken.value in code_shortcuts):
                                cDerivationName = code_shortcuts[nToken.value]
                                cTokenIndex+=1
                                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                            elif("<"+nToken.token+">" in code_shortcuts):
                                cDerivationName = code_shortcuts["<"+nToken.token+">"]
                                cState = "<"+nToken.token+">"
                                cTokenIndex+=1
                                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
                                cState = nToken.value
                                nToken = token_code[cTokenIndex+1]  
                            elif(nToken.value == "}"):                                
                                if(gProbe == 0):
                                    sError(nToken.line,nToken.value,lineno())
                                else:                                    
                                    gProbe-=1
                                    return cTokenIndex+2
                            elif(nToken.value=="end"):
                                if(gProbe>0):
                                    sError(nToken.line,nToken.value,lineno())
                                elif(gProbe==0):
                                    return
                            else:                                                        
                                sError(nToken.line,nToken.value,lineno())  
                            break
                        else:
                            sError(cToken.line,cToken.value,lineno())
                    else:
                        print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
            else:
                sError(token_code[cTokenIndex+1].line,token_code[cTokenIndex+1].value,lineno())
                
        elif("<code_instructions>" in derivations[cDerivationName][cState]):                                   
            
            if(cState == "{"):                        
                gProbe+=1
                cTokenIndex+=1
                check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
                cState = nToken.value
                nToken = token_code[cTokenIndex+1]                    
                if(token_code[cTokenIndex].value in code_shortcuts):                    
                    if(cDerivationName=="<for>" or cDerivationName=="<while>"):
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[token_code[cTokenIndex].value],True) 
                    else:
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[token_code[cTokenIndex].value],False) 
                elif("<"+token_code[cTokenIndex].token+">" in code_shortcuts):                                        
                    if(cDerivationName=="<for>" or cDerivationName=="<while>"):
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+token_code[cTokenIndex].token+">"],True) 
                    else:
                        cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+token_code[cTokenIndex].token+">"],False) 
                else:
                    sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())
                
                
                
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
                        sError(nToken.line,nToken.value,lineno())
                    else:                                    
                        gProbe-=1
                        return cTokenIndex+1
                elif(cToken.value=="end"):
                    if(gProbe>0):
                        sError(nToken.line,nToken.value,lineno())
                    elif(gProbe==0):
                        return  
                else:                                   
                    sError(cToken.line,cToken.value,lineno())

            # if(nToken.value in code_shortcuts):
            #     cDerivationName = code_shortcuts[nToken.value]
            #     cTokenIndex+=1
            #     check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
            #     cState = nToken.value
            #     nToken = token_code[cTokenIndex+1]  
            #     print(cState)
            #     print(nToken.token)
            #     print("========")
            # elif("<"+nToken.token+">" in code_shortcuts):
            #     cDerivationName = code_shortcuts["<"+nToken.token+">"]
            #     cState = "<"+nToken.token+">"
            #     cTokenIndex+=1
            #     check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
            #     cState = nToken.value
            #     nToken = token_code[cTokenIndex+1]  
            #     print(cState)
            #     print(nToken.token)
            #     print("========")
            # elif(nToken.value == "}"):                                
            #     if(gProbe == 0):
            #         sError(nToken.line,nToken.value,lineno())
            #     else:                                    
            #         gProbe-=1
            #         return cTokenIndex+2
            # elif(nToken.value=="end"):
            #     if(gProbe>0):
            #         sError(nToken.line,nToken.value,lineno())
            #     elif(gProbe==0):
            #         pass #codigo terminou
            # else:                                                        
            #     sError(nToken.line,nToken.value,lineno())  
           

        else:
            sError(nToken.line,nToken.value,lineno())
                 



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
            check(token_code,cTokenIndex,gProbe,False,cDerivationName)            
            nToken=token_code[cTokenIndex+1]          
            if(nToken.token=="dataType_token" or nToken.token=="canvas_token"):                
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
            


    
    for var in code_variables:
        if(code_variables[var].type=="canvas"):
            print("Nome: {0}. Tipo: {1}, valor: {2}.".format(code_variables[var].name,type(code_variables[var].type),code_variables[var].value))
        else:
            print("Nome: {0}. Tipo: {1}, valor: {2}.".format(code_variables[var].name,code_variables[var].type,code_variables[var].value))
        pass

    
    #code statements parser
    if(nToken.value=="begin"):
        cTokenIndex+=1
        
        if(cTokenIndex == len(token_code)-1):            
            if(token_code[cTokenIndex].value == "end"):
                print("There are no instructions to be executed. =P")
                sys.exit()
            else:                
                print("Syntax error: unexpected end of file after line {0}. 'end' was expected.".format(token_code[cTokenIndex].line))
                sys.exit()
        nToken = token_code[cTokenIndex+1]   
        if(cTokenIndex == len(token_code)-2):          
            print("There are no instructions to be executed. =P")
            sys.exit()
        if(nToken.value in code_shortcuts):                        
            statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value],False)
        elif("<"+nToken.token+">" in code_shortcuts):            
            statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"],False)
        else:        
            sError(nToken.line,nToken.value,lineno())

    elif(cTokenIndex+1==len(token_code)):
        print("Syntax error: unexpected end of file after line {0}. 'begin' was expected.".format(nToken.line))
    else:
        print("Syntax error (line {0}): unexpected '{1}'. 'begin' was expected.".format(nToken.line,nToken.value))

    print("Compilation Finished...")
    for var in code_variables:
        if(code_variables[var].type=="canvas"):
            print("Nome: {0}. Tipo: {1}, valor: {2}.".format(code_variables[var].name,code_variables[var].type,type(code_variables[var].value)))
        else:
            print("Nome: {0}. Tipo: {1}, valor: {2}.".format(code_variables[var].name,code_variables[var].type,code_variables[var].value))
        pass

    return



# for graph in derivations:
#      plt.figure(graph)
#      nx.draw(derivations[graph], with_labels=True,)
# plt.show()



    


 