# -*- coding: utf-8 -*-
import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
from Alphabet.alphabet import *
import networkx as nx
import matplotlib.pyplot as plt

listOfGraphs=["base_code","variable_declaration","attribution","draw","erase","import","export","copy","for","while","break","if","else"]

listOfSketches = ["circle","swarm","tree","square"]

graphs = {}

#exportação dos grafos de derivação
def exportGraph():
    global graphs
    for graph in graphs:          
        nx.write_gml(graphs[graph], "parseGraphs/{0}.gml".format(unTokenName(graph)))
    
    

def unTokenName(name):
    return name[1:len(name)-1]

def connectTokenToTokens(Graph,originToken,endToken_):   
    global graphs
    if (type(endToken_) is str):
        graphs[Graph].add_edge(originToken,endToken_)
            
    elif(type(endToken_) is list ):
        for token in endToken_:
            graphs[Graph].add_edge(originToken,token)
        
    
def generateParseGraph():
    #<base_code>
    global graphs
    name = "<base_code>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"var")
    connectTokenToTokens(name,"var","begin")
    connectTokenToTokens(name,"var",data_type_list)
    connectTokenToTokens(name,";",data_type_list)
    connectTokenToTokens(name,"var","canvas")
    connectTokenToTokens(name,";","canvas")
    for dataType in data_type_list:
        connectTokenToTokens(name,dataType,"<id_token>")
    connectTokenToTokens(name,"canvas","<id_token>")
    connectTokenToTokens(name,"<id_token>",",")
    connectTokenToTokens(name,"<id_token>",";")  
    connectTokenToTokens(name,";","begin")  
    
    connectTokenToTokens(name,",","<id_token>")
    connectTokenToTokens(name,"begin","<code_instruction>")
    connectTokenToTokens(name,"<code_instruction>","<code_instruction>")
    connectTokenToTokens(name,"<code_instruction>","end")

    #<variable_declaration>
    name = "<variable_declaration>"
    graphs[name] = nx.DiGraph()

    connectTokenToTokens(name,name,data_type_list)
    connectTokenToTokens(name,name,"canvas")
    for dataType in data_type_list:
        connectTokenToTokens(name,dataType,"<id_token>")
    connectTokenToTokens(name,"canvas","<id_token>")
    connectTokenToTokens(name,"<id_token>",",")
    connectTokenToTokens(name,"<id_token>",";")    
    connectTokenToTokens(name,",","<id_token>")   

    #atribuição
    name = "<attribution>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"<id_token>")        
    connectTokenToTokens(name,"<id_token>","=")       
    connectTokenToTokens(name,"=","<operation>")   
    connectTokenToTokens(name,"<operation>",";")    
    connectTokenToTokens(name,"=","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",";")
    connectTokenToTokens(name,"=","<sketchType_token>")
    connectTokenToTokens(name,"<sketchType_token>",";")

    #sketchType Circle
    name = "<circle>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"circle")
    connectTokenToTokens(name,"circle","(")
    connectTokenToTokens(name,"(","radius")
    connectTokenToTokens(name,"radius","<int>")
    connectTokenToTokens(name,"<int>","color")
    connectTokenToTokens(name,"color","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")    
    
    #sketchType Square
    name = "<square>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"square")
    connectTokenToTokens(name,"square","(")
    connectTokenToTokens(name,"(","X")
    connectTokenToTokens(name,"X","<int>X")
    connectTokenToTokens(name,"<int>X","Y")
    connectTokenToTokens(name,"Y","<int>Y")
    connectTokenToTokens(name,"<int>Y","color")
    connectTokenToTokens(name,"color","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")

    #sketchType Web
    name = "<web>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"web")
    connectTokenToTokens(name,"web","(")
    connectTokenToTokens(name,"(","X")
    connectTokenToTokens(name,"X","<int>X")
    connectTokenToTokens(name,"<int>X","Y")
    connectTokenToTokens(name,"Y","<int>Y")
    connectTokenToTokens(name,"<int>Y","color")
    connectTokenToTokens(name,"color","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")    
    

    #sketchType Swarm
    name = "<swarm>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"swarm")
    connectTokenToTokens(name,"swarm","(")
    connectTokenToTokens(name,"(","X")
    connectTokenToTokens(name,"X","<int>X")
    connectTokenToTokens(name,"<int>X","Y")
    connectTokenToTokens(name,"Y","<int>Y")
    connectTokenToTokens(name,"<int>Y","rate")
    connectTokenToTokens(name,"rate","<int>rate")
    connectTokenToTokens(name,"rate","<float>rate")
    connectTokenToTokens(name,"<float>rate","color")
    connectTokenToTokens(name,"<int>rate","color")
    connectTokenToTokens(name,"color","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")    

    #sketchType Tree
    name = "<tree>"
    graphs[name] = nx.DiGraph()
    connectTokenToTokens(name,name,"tree")
    connectTokenToTokens(name,"tree","(")
    connectTokenToTokens(name,"(","X")
    connectTokenToTokens(name,"X","<int>X")
    connectTokenToTokens(name,"<int>X","Y")
    connectTokenToTokens(name,"Y","<int>Y")
    connectTokenToTokens(name,"<int>Y","trunk")
    connectTokenToTokens(name,"trunk","<literal_token>trunk")
    connectTokenToTokens(name,"<literal_token>trunk","leaf")
    connectTokenToTokens(name,"leaf","<literal_token>leaf")
    connectTokenToTokens(name,"<literal_token>leaf",")")    
    
    #import
    name = "<import>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"import")
    connectTokenToTokens(name,"import","(")
    connectTokenToTokens(name,"(","<literal_token>")
    connectTokenToTokens(name,"<literal_token>","in")
    connectTokenToTokens(name,"in","<id_token>")
    connectTokenToTokens(name,"<id_token>",")")
    connectTokenToTokens(name,")",";")

    #export
    name = "<export>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"export")
    connectTokenToTokens(name,"export","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","to")
    connectTokenToTokens(name,"to","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")
    connectTokenToTokens(name,")",";")

    #copy
    name = "<copy>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"copy")
    connectTokenToTokens(name,"copy","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","to")
    connectTokenToTokens(name,"to","<id_token>to")
    connectTokenToTokens(name,"<id_token>to",")")
    connectTokenToTokens(name,")",";")

    #draw
    name = "<draw>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"draw")
    connectTokenToTokens(name,"draw","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","in")
    connectTokenToTokens(name,"in","<id_token>in")
    connectTokenToTokens(name,"<id_token>in","X")
    connectTokenToTokens(name,"X","<int>X")
    connectTokenToTokens(name,"<int>X","Y")
    connectTokenToTokens(name,"Y","<int>Y")
    connectTokenToTokens(name,"<int>Y",")")
    connectTokenToTokens(name,")",";")

    #erase
    name = "<erase>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"erase")
    connectTokenToTokens(name,"erase","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>",")")
    connectTokenToTokens(name,")",";")
    

    #for (conferir)
    name = "<for>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"for")
    connectTokenToTokens(name,"for","<id_token>")
    connectTokenToTokens(name,"<id_token>","from")

    connectTokenToTokens(name,"from","<int>from")
    connectTokenToTokens(name,"from","<float>from")
    connectTokenToTokens(name,"<int>from","to")
    connectTokenToTokens(name,"<float>from","to")
    connectTokenToTokens(name,"to","<int>to")
    connectTokenToTokens(name,"to","<float>to")
    connectTokenToTokens(name,"<int>to","step")
    connectTokenToTokens(name,"<float>to","step")                         
    connectTokenToTokens(name,"step","<int>step")
    connectTokenToTokens(name,"step","<float>step")   
    connectTokenToTokens(name,"<int>step","{")
    connectTokenToTokens(name,"<float>step","{")               
    connectTokenToTokens(name,"{","<code_instructions>")
    connectTokenToTokens(name,"<code_instructions>","}")

                         
     #while (conferir)
    name = "<while>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"while")
    connectTokenToTokens(name,"while","(")    
    connectTokenToTokens(name,"(","<operation>")                      
    connectTokenToTokens(name,"<operation>",")")            
    connectTokenToTokens(name,")","{")
    connectTokenToTokens(name,"{","<code_instructions>")
    connectTokenToTokens(name,"<code_instructions>","}")    

    #break
    name = "<break>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"break")
    connectTokenToTokens(name,"break",";")        
                 
     #if (conferir)
    name = "<if>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"if")
    connectTokenToTokens(name,"if","(")
    connectTokenToTokens(name,"(","<conditional>")          
    connectTokenToTokens(name,"<conditional>",")")        
    connectTokenToTokens(name,")","{")
    connectTokenToTokens(name,"{","<code_instructions>")
    connectTokenToTokens(name,"<code_instructions>","}")          
    connectTokenToTokens(name,"}","<else>")   
                        
     #elif (conferir)
    # name = "<elif>"
    # graphs[name] = nx.DiGraph()    
    # connectTokenToTokens(name,name,"elif")
    # connectTokenToTokens(name,"elif","(")
    # connectTokenToTokens(name,"(","<conditional>")          
    # connectTokenToTokens(name,"<conditional>",")")        
    # connectTokenToTokens(name,")","{")
    # connectTokenToTokens(name,"{","<code_instructions>")
    # connectTokenToTokens(name,"<code_instructions>","}")   
    # connectTokenToTokens(name,"}","<elif>")   
    # connectTokenToTokens(name,"}","<else>")                                               

    #else
    name = "<else>"
    graphs[name] = nx.DiGraph()    
    connectTokenToTokens(name,name,"else")
    connectTokenToTokens(name,"else","if")
    connectTokenToTokens(name,"if","(")
    connectTokenToTokens(name,"(","<conditional>")          
    connectTokenToTokens(name,"<conditional>",")")        
    connectTokenToTokens(name,")","{")
    connectTokenToTokens(name,"else","{")    
    connectTokenToTokens(name,"{","<code_instructions>")
    connectTokenToTokens(name,"<code_instructions>","}")    
    
                         
try:
    if(sys.argv[1]=="run"):    
        generateParseGraph()        
        exportGraph()
except:        
    pass



