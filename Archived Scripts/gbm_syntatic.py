

# def statementsGraphParser_old(token_code,cTokenIndex,cDerivationName,isLoop):
#     global gProbe
#     nToken = token_code[cTokenIndex+1]
#     cState = token_code[cTokenIndex].value       
    
#     while(True):       
#         #a = str(raw_input(""))        
#         #print("cState:"+cState)                   
#         check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)        
        
#         if(token_code[cTokenIndex].token=="id_token"):                
#             cState = "<id_token>"        
        

#         if(nToken.token=="id_token"):            
#             if(not(nToken.value in code_variables)):
#                 print("Error (line {0}): variable '{1}' was not declared.".format(nToken.line,nToken.value))
#                 sys.exit()  
        
#         if(token_code[cTokenIndex].token=="literal_token"):                        
#             cState = "<literal_token>"
        
#         if(token_code[cTokenIndex].token == "sketchType_token"):                        
#             cState = "<sketchType_token>"
     
#         #sError(nToken.line,nToken.value,lineno())vationName)
#         if(cDerivationName=="<for>"):            
#             if(nToken.token=="int" or nToken.token=="float"):
#                 nToken.value = asToken(nToken.token)+cState
        
        
#         #if(cDerivationName == "<attribution>" and token_code[cTokenIndex].token == "id_token"): #nao sei se vou precisar de novo
#         if(token_code[cTokenIndex].token == "id_token"):            
#             if(not(token_code[cTokenIndex].value in code_variables)):
#                 print("Error (line {0}): variable '{1}' was not declared.".format(token_code[cTokenIndex].line,token_code[cTokenIndex].value))
#                 sys.exit()   

#         #print(cDerivationName)     
        
#         if((cState=="(" and cDerivationName=="<while>" and token_code[cTokenIndex-1].value=="while")or (cState=="(" and cDerivationName=="<if>" and token_code[cTokenIndex-1].value=="if") or (cState=="(" and cDerivationName=="<else>" and token_code[cTokenIndex-1].value=="if")):            
#             #print("tem while")
#             cState = "<operation>"            
#             opString=""
#             sString=""            
#             while(True):                
#                 if(cTokenIndex<len(token_code)-1):
#                     cToken = nToken
#                     cTokenIndex+=1
#                     check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                    
#                     nToken = token_code[cTokenIndex+1]
#                     if(cToken.value==")" and nToken.value=="{"):
#                         cState = ")"
#                         break
#                     if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

#                         if(cToken.value == "^"):               
#                             opString+="** "
#                             sString+="^ "
#                         elif(cToken.token == "id_token"):
#                             if(cToken.value in code_variables):
#                                 opString+='code_variables["'+cToken.value+'"].value '
#                                 sString+=cToken.value+' '
#                             else:
#                                 print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
#                                 sys.exit()
#                         else:
#                             opString+=cToken.value+" "
#                             sString+=cToken.value+" "
#                 else:
#                     print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
#             if(len(opString)==0):
#                 print("Syntax error (line {0}): logic operation required.".format(cToken.line))
#                 sys.exit()
#             else:
#                 try:
#                     #print(opString)                    
#                     eval(opString)     
#                     #print(eval(opString))                                          
#                 except:
#                     print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,sString))    
#                     sys.exit()
            

#         if(nToken.value in derivations[cDerivationName][cState] or "<"+nToken.token+">" in derivations[cDerivationName][cState]):#walk             
#             if(cState=="else"):#MAGIC...
#                 sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())                
            

#             if(nToken.value == "{"):                        
#                 gProbe+=1
#                 cTokenIndex+=1
#                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
#                 cState = nToken.value
#                 nToken = token_code[cTokenIndex+1]                
#                 if(nToken.value in code_shortcuts):    
#                     #print(code_shortcuts[nToken.value])
#                     if(cDerivationName=="<for>" or cDerivationName=="<while>"):                
#                         cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value],True) 
#                     else:
#                         cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[nToken.value],False) 
#                 elif("<"+nToken.token+">" in code_shortcuts):                                        
#                     print(nToken.value)
#                     print(code_shortcuts["<"+nToken.token+">"])
#                     if(cDerivationName=="<for>" or cDerivationName=="<while>"):
#                         cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"],True) 
#                     else:
#                         cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+nToken.token+">"],False) 
#                 else:
#                     sError(nToken.line,nToken.value,lineno())
                
                
#                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
#                 cToken = token_code[cTokenIndex]                         
                                       
#                 if(cToken.value in code_shortcuts):
#                     cDerivationName = code_shortcuts[cToken.value]
#                     cState = cToken.value
#                     nToken = token_code[cTokenIndex+1]     
#                 elif("<"+cToken.token+">" in code_shortcuts):
#                     cDerivationName = code_shortcuts["<"+cToken.token+">"]                    
#                     cState = cToken.value
#                     nToken = token_code[cTokenIndex+1]  
#                 elif(cToken.value == "}"):                                                                
#                     if(gProbe == 0):
#                         sError(nToken.line,nToken.value,lineno())
#                     else:                                    
#                         gProbe-=1
#                         return cTokenIndex+1
#                 elif(cToken.value=="end"):
#                     if(gProbe>0):
#                         sError(nToken.line,nToken.value,lineno())
#                     elif(gProbe==0):
#                         print("Compilation finished")
#                         sys.exit()
#                         pass #codigo terminou    
#                 else:                                   
#                     sError(cToken.line,cToken.value,lineno())


#             ##ATRIBUICAO DE STRINGS  
#             elif(nToken.token == "literal_token" and cDerivationName == "<attribution>"):                
#                 pass
                
                
#                 #atribution (later)  

#             ##ATRIBUICAO DE SKETCH
#             elif(nToken.token == "sketchType_token" and cDerivationName == "<attribution>"):                
#                 if(nToken.value in sketch_shortcuts):
#                     sketchDerivation = sketch_shortcuts[nToken.value]
#                     cState = nToken.value
#                     cTokenIndex+=1
#                     check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                    
#                     nToken = token_code[cTokenIndex+1]  
#                     while(True):                        
#                         if(token_code[cTokenIndex].token == "int"):
#                             if(asToken("int") in derivations[sketchDerivation]):
#                                 cState = asToken("int")
#                             elif(asToken("int")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
#                                 cState = asToken("int")+token_code[cTokenIndex-1].value
#                         elif(token_code[cTokenIndex].token == "float"):
#                             if(asToken("float") in derivations[sketchDerivation]):
#                                 cState = asToken("float")
#                             elif(asToken("float")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
#                                 cState = asToken("float")+token_code[cTokenIndex-1].value
#                         elif(token_code[cTokenIndex].token == "literal_token"):
#                             if(asToken("literal_token") in derivations[sketchDerivation]):
#                                 cState = asToken("literal_token")
#                             elif(asToken("literal_token")+token_code[cTokenIndex-1].value in derivations[sketchDerivation]):
#                                 cState = asToken("literal_token")+token_code[cTokenIndex-1].value
                        

#                         if(nToken.value in derivations[sketchDerivation][cState] or "<"+nToken.token+">" in derivations[sketchDerivation][cState] or "<"+nToken.token+">"+cState in derivations[sketchDerivation][cState]):        
#                             cState = nToken.value
#                             cTokenIndex+=1
#                             check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                            
#                             nToken = token_code[cTokenIndex+1]  
#                         elif(nToken.value==";"):                            
#                             #atribution (later)                                   
#                             cState = nToken.value
#                             cTokenIndex+=1
#                             check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                            
#                             nToken = token_code[cTokenIndex+1]                              
#                             if(nToken.value in code_shortcuts):
#                                 cDerivationName = code_shortcuts[nToken.value]
#                                 cTokenIndex+=1
#                                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
#                                 cState = nToken.value
#                                 nToken = token_code[cTokenIndex+1]  
#                                 break;
#                             elif("<"+nToken.token+">" in code_shortcuts):
#                                 cDerivationName = code_shortcuts["<"+nToken.token+">"]
#                                 cState = "<"+nToken.token+">"
#                                 cTokenIndex+=1
#                                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
#                                 cState = nToken.value
#                                 nToken = token_code[cTokenIndex+1]  
#                                 break;
#                             elif(nToken.value == "}"):                                
#                                 if(gProbe == 0):
#                                     sError(nToken.line,nToken.value,lineno())
#                                 else:                                    
#                                     gProbe-=1
#                                     return cTokenIndex+2
#                             elif(nToken.value=="end"):
#                                 if(gProbe>0):
#                                     sError(nToken.line,nToken.value,lineno())
#                                 elif(gProbe==0):
#                                     print("Compilation finished")
#                                     sys.exit()
#                                     pass #codigo terminou 
#                             else:                                
#                                 sError(nToken.line,nToken.value,lineno()) 
#                         elif(nToken.value == "}"):                                
#                             if(gProbe == 0):
#                                 sError(nToken.line,nToken.value,lineno())
#                             else:                                    
#                                 gProbe-=1
#                                 return cTokenIndex+2
#                         elif(nToken.value=="end"):
#                             if(gProbe>0):
#                                 sError(nToken.line,nToken.value,lineno())
#                             elif(gProbe==0):
#                                 print("Compilation finished")
#                                 sys.exit()
#                                 pass #codigo terminou 
#                         else:
#                             sError(nToken.line,nToken.value,lineno())  

#                         #sys.exit()
#                 else:
#                     sError(nToken.line,nToken.value,lineno())
                


#                 #atribution sketch(later)  
            
#             if(token_code[cTokenIndex].value=="end"):
#                 if(gProbe>0):
#                     print("Syntax Error (line {0}): unexpected '{1}'")
#                 elif(gProbe==0):
                    
#                     return
#                     pass #codigo terminou
#             cTokenIndex+=1
#             check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
            
#             cState=nToken.value
#             nToken = token_code[cTokenIndex+1]                
#         #elif("<"+nToken.token+">" in derivations[cDerivationName][cState] and nToken.token=="id_token"):
#         elif(nToken.value == "}"):
        
#             if(gProbe == 0):
                
#                 sError(nToken.line,nToken.value,lineno())
#             else:                
#                 gProbe-=1
#                 return cTokenIndex+2
#         elif(nToken.value=="end"):
#             if(gProbe>0):
#                 sError(nToken.line,nToken.value,lineno())
#             elif(gProbe==0):
#                 print("Compilation finished")
#                 sys.exit()
#                 pass #codigo terminou
#         elif(cState == ";"):#end of statement                  
#             if(nToken.value in code_shortcuts):
#                 cDerivationName = code_shortcuts[nToken.value]
#                 cTokenIndex+=1
#                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
#                 cState = nToken.value
#                 nToken = token_code[cTokenIndex+1]  
#             elif("<"+nToken.token+">" in code_shortcuts):
#                 cDerivationName = code_shortcuts["<"+nToken.token+">"]
#                 cState = "<"+nToken.token+">"
#                 cTokenIndex+=1
#                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
#                 cState = nToken.value
#                 nToken = token_code[cTokenIndex+1]  
            
#             else:                
#                 sError(nToken.line,nToken.value,lineno())  
        
#         ##ATRIBUICAO DE OPERAÇOES
#         elif(cDerivationName == "<attribution>"):  
#             print("tem atribuição")
#             #atribuicao de operaçoes                            
#             if(nToken.value == ";"):
#                 sError(nToken.line,";")
#             if(nToken.token == "id_token" or nToken.token=="boolean_token" or is_a_number(nToken.value) or nToken.value == "("): 
#                 cState = "<operation>"
#                 opString = ""
#                 sString=""
#                 while(True):                        
#                     if(cTokenIndex<len(token_code)-1):
#                         cToken = nToken
#                         cTokenIndex+=1
#                         check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                        
#                         nToken = token_code[cTokenIndex+1]
#                         if(cToken.token == "math_operator" or cToken.value == "(" or cToken.value == ")" or cToken.token == "id_token" or cToken.token == "boolean_token" or cToken.token=="logic_token" or is_a_number(cToken.value) or cToken.token=="logic_operator"):

#                             if(cToken.value == "^"):
#                                 opString+="** "
#                                 sString+="^ "
#                             elif(cToken.token == "id_token"):
#                                 if(cToken.value in code_variables):
#                                     opString+='code_variables["'+cToken.value+'"].value '
#                                     sString+=cToken.value+' '
#                                 else:
#                                     print("Error (line {0}): variable '{1}' was not declared.".format(cToken.line,cToken.value))
#                                     sys.exit()
#                             else:
#                                 opString+=cToken.value+" "
#                                 sString+=cToken.value+" "
#                         elif(cToken.value==";"):                                                                               
#                             if(nToken.value in code_shortcuts):
#                                 cDerivationName = code_shortcuts[nToken.value]
#                                 cTokenIndex+=1
#                                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
#                                 cState = nToken.value
#                                 nToken = token_code[cTokenIndex+1]  
#                             elif("<"+nToken.token+">" in code_shortcuts):
#                                 cDerivationName = code_shortcuts["<"+nToken.token+">"]
#                                 cState = "<"+nToken.token+">"
#                                 cTokenIndex+=1
#                                 check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                                
#                                 cState = nToken.value
#                                 nToken = token_code[cTokenIndex+1]  
#                             elif(nToken.value == "}"):                                
#                                 if(gProbe == 0):
#                                     sError(nToken.line,nToken.value,lineno())
#                                 else:                                    
#                                     gProbe-=1
#                                     return cTokenIndex+2
#                             elif(nToken.value=="end"):
#                                 if(gProbe>0):
#                                     sError(nToken.line,nToken.value,lineno())
#                                 elif(gProbe==0):
#                                     print("Compilation finished")
#                                     sys.exit()
#                                     pass #codigo terminou
#                             else:                                                        
#                                 sError(nToken.line,nToken.value,lineno())  
#                             break
#                         else:
#                             sError(cToken.line,cToken.value,lineno())
#                     else:
#                         print("Syntax error: unexpected end of file after line {0}.".format(token_code[cTokenIndex].line))
#                 try:
#                     print(opString)  
#                     eval(opString)                  
#                     #print(eval(opString))
#                 except:
#                     print("Syntax error (line {0}): operation '{1}' is invalid. Check for parenthesis, variables, numbers and literals.".format(cToken.line,sString))    
#                     sys.exit()
#         # elif("<code_instructions>" in derivations[cDerivationName][cState]):                                   
            
#         #     if(cState == "{"):                        
#         #         gProbe+=1
#         #         cTokenIndex+=1
#         #         check(token_code,cTokenIndex,gProbe,isLoop,cDerivationName)
                
#         #         cState = nToken.value
#         #         nToken = token_code[cTokenIndex+1]                    
#         #         print(cState)
#         #         if(token_code[cTokenIndex].value in code_shortcuts):          
#         #             print(code_shortcuts[token_code[cTokenIndex].value])          
#         #             if(cDerivationName=="<for>" or cDerivationName=="<while>"):
#         #                 cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[token_code[cTokenIndex].value],True) 
#         #             else:
#         #                 cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts[token_code[cTokenIndex].value],False) 
#         #         elif("<"+token_code[cTokenIndex].token+">" in code_shortcuts):                                        
#         #             print(code_shortcuts["<"+token_code[cTokenIndex].token+">"])
#         #             if(cDerivationName=="<for>" or cDerivationName=="<while>"):
#         #                 cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+token_code[cTokenIndex].token+">"],True) 
#         #             else:
#         #                 cTokenIndex = statementsGraphParser(token_code,cTokenIndex+1,code_shortcuts["<"+token_code[cTokenIndex].token+">"],False) 
#         #         else:
#         #             sError(token_code[cTokenIndex].line,token_code[cTokenIndex].value,lineno())
                
                
                
#         #         cToken = token_code[cTokenIndex]                
                
#         #         if(cToken.value in code_shortcuts):
#         #             cDerivationName = code_shortcuts[cToken.value]
#         #             cState = cToken.value
#         #             nToken = token_code[cTokenIndex+1]     
#         #         elif("<"+cToken.token+">" in code_shortcuts):
#         #             cDerivationName = code_shortcuts["<"+cToken.token+">"]                    
#         #             cState = cToken.value
#         #             nToken = token_code[cTokenIndex+1]  
#         #         elif(cToken.value == "}"):                                            
                    
#         #             if(gProbe == 0):
#         #                 sError(nToken.line,nToken.value,lineno())
#         #             else:                                    
#         #                 gProbe-=1
#         #                 return cTokenIndex+1
#         #         elif(cToken.value=="end"):
#         #             if(gProbe>0):
#         #                 sError(nToken.line,nToken.value,lineno())
#         #             elif(gProbe==0):
#         #                 print("Compilation finished")
#         #                 sys.exit()
#         #                 pass #codigo terminou    
#         #         else:                                   
#         #             sError(cToken.line,cToken.value,lineno())

        

#         else:
#             sError(nToken.line,nToken.value,lineno())
                