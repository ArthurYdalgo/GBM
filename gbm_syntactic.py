# -*- coding: utf-8 -*-

import sys #biblioteca para usar comandos de sistema
from parseBNF import * #BNF transformada em grafo

#Syntax parser
def parser(token_code):
    parseError = graphParse(token_code)
    if(len(parseError)>0):
        print("Syntac error (line {0}}): unexpected '{1}' after '{2}'".format(parseError["line"],parseError["nToken"],parseError["cToken"]))
        sys.exit()
    else:
        return token_code

# if(nToken in base_code[cToken]):
#     print("Current token: {0}".format(nToken))
# else:
#     print("Unexpect '{0}' in line {1}, after '{2}' (line {3}).".format(nToken,nTokenLine,cToken,cTokenLine))

def graphParse(token_code):
    error={}



    return error

plt.figure("<base_code>")
nx.draw(base_code, with_labels=True, font_weight='bold')

plt.figure("<variable_declaration>")
nx.draw(variable_declaration, with_labels=True, font_weight='bold')

plt.show()
    


 