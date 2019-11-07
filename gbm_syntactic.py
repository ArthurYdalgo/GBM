# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from Reserved.reserved import *
import networkx as nx
import matplotlib.pyplot as plt
from parseBNF import listOfGraphs

def isnt_Terminal(token_type):
    if(token_type[0]=="<" and token_type[len(token_type)-1]==">"):
        return True
    else:
        return False

derivations={}

shortcut = {}

for graph in listOfGraphs:
    filename = 'parseGraphs/{0}.gml'.format(graph)    
    name = "<{0}>".format(graph)
    derivations[name] = nx.read_gml(filename)

#shortcut["for"] = derivations["<for_statement>"]

#Syntax parser
def parser(token_code):
    parseError = graphParse(token_code)
    if(len(parseError)>0):
        print("Syntac error (line {0}}): unexpected '{1}' after '{2}'".format(parseError["line"],parseError["nToken"],parseError["cToken"]))
        sys.exit()
    else:
        return token_code


def graphParse(token_code):
    error={}
    scopeProbe=0
    cToken = token_code[0]
    cTokenIndex = 0    
    #while(True):



    return error

for graph in derivations:
    plt.figure(graph)
    nx.draw(derivations[graph], with_labels=True, font_weight='bold')
#plt.show()



    


 