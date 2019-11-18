# -*- coding: utf-8 -*-
import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
from Alphabet.alphabet import *
import networkx as nx
import matplotlib.pyplot as plt

listOfGraphs=["base_code","variable_declaration","attribution","draw","erase","import","export","copy"]

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
    connectTokenToTokens(name,"<id_token>",",")    
    connectTokenToTokens(name,"<id_token>","=")
    connectTokenToTokens(name,",","<id_token>")        
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
    connectTokenToTokens(name,"(","RADIUS")
    connectTokenToTokens(name,"RADIUS","<int>")
    connectTokenToTokens(name,"<int>","COLOR")
    connectTokenToTokens(name,"COLOR","<literal_token>")
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
    connectTokenToTokens(name,"<int>Y","COLOR")
    connectTokenToTokens(name,"COLOR","<literal_token>")
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
    connectTokenToTokens(name,"<int>Y","COLOR")
    connectTokenToTokens(name,"COLOR","<literal_token>")
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
    connectTokenToTokens(name,"<int>Y","RATE")
    connectTokenToTokens(name,"RATE","<int>R")
    connectTokenToTokens(name,"RATE","<float>R")
    connectTokenToTokens(name,"<float>R","COLOR")
    connectTokenToTokens(name,"<int>R","COLOR")
    connectTokenToTokens(name,"COLOR","<literal_token>")
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
    connectTokenToTokens(name,"<int>Y","TRUNK")
    connectTokenToTokens(name,"TRUNK","<literal_token>")
    connectTokenToTokens(name,"<literal_token>","LEAF")
    connectTokenToTokens(name,"LEAF","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")    
    
    #import
    name = "<import>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"import")
    connectTokenToTokens(name,"import","(")
    connectTokenToTokens(name,"(","<literal_token>")
    connectTokenToTokens(name,"<literal_token>","IN")
    connectTokenToTokens(name,"IN","<id_token>")
    connectTokenToTokens(name,"<id_token>",")")
    connectTokenToTokens(name,")",";")

    #export
    name = "<export>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"export")
    connectTokenToTokens(name,"export","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","TO")
    connectTokenToTokens(name,"TO","<literal_token>")
    connectTokenToTokens(name,"<literal_token>",")")
    connectTokenToTokens(name,")",";")

    #copy
    name = "<copy>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"copy")
    connectTokenToTokens(name,"copy","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","TO")
    connectTokenToTokens(name,"TO","<id_token>TO")
    connectTokenToTokens(name,"<id_token>TO",")")
    connectTokenToTokens(name,")",";")

    #draw
    name = "<draw>"
    graphs[name] = nx.DiGraph()
    
    connectTokenToTokens(name,name,"draw")
    connectTokenToTokens(name,"draw","(")
    connectTokenToTokens(name,"(","<id_token>")
    connectTokenToTokens(name,"<id_token>","IN")
    connectTokenToTokens(name,"IN","<id_token>IN")
    connectTokenToTokens(name,"<id_token>IN","X")
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


    #for
    






try:
    if(sys.argv[1]=="run"):    
        generateParseGraph()        
        exportGraph()
except:        
    pass



