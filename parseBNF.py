# -*- coding: utf-8 -*-
import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
from Alphabet.alphabet import *
import networkx as nx
import matplotlib.pyplot as plt

listOfGraphs=["base_code","variable_declaration"]

graphs = {}

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

    connectTokenToTokens(name,"var","begin")
    connectTokenToTokens(name,"var","<variable_declaration>")
    connectTokenToTokens(name,"<variable_declaration>","begin")
    connectTokenToTokens(name,"begin","<code_instruction>")
    connectTokenToTokens(name,"<code_instruction>","<code_instruction>")
    connectTokenToTokens(name,"<code_instruction>","end")


    #<variable_declaration>
    name = "<variable_declaration>"
    graphs[name] = nx.DiGraph()


    connectTokenToTokens(name,"<variable_declaration>",data_type_list)
    for dataType in data_type_list:
        connectTokenToTokens(name,dataType,"<id_token>")
    connectTokenToTokens(name,"<id_token>",",")
    connectTokenToTokens(name,"<id_token>",";")
    connectTokenToTokens(name,",","<id_token>")

    

#exportação dos grafos de derivação
def exportGraph():
    global graphs
    for graph in graphs:        
        nx.write_gml(graphs[graph], "parseGraphs/{0}.gml".format(unTokenName(graph)))

try:
    if(sys.argv[1]=="run"):    
        generateParseGraph()        
        exportGraph()
except:        
    pass



