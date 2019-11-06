from reserved import *
import networkx as nx
import matplotlib.pyplot as plt

graphs = {}

base_code = nx.DiGraph()
variable_declaration = nx.DiGraph()
code_instructions = nx.DiGraph()

def connectTokenToTokens(Graph,originToken,endToken_):    
    if (type(endToken_) is str):
        Graph.add_edge(originToken,endToken_)
            
    elif(type(endToken_) is list ):
        for token in endToken_:
            Graph.add_edge(originToken,token)
    return Graph

#<base_code>
base_code = connectTokenToTokens(base_code,"var","<variable_declaration>")
base_code = connectTokenToTokens(base_code,"<variable_declaration>","begin")
base_code = connectTokenToTokens(base_code,"begin","<code_instruction>")
base_code = connectTokenToTokens(base_code,"<code_instruction>",";")
base_code = connectTokenToTokens(base_code,";","end")

nx.draw(base_code, with_labels=True, font_weight='bold')

#plt.show()