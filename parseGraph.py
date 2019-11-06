from parseBNF import *

# if(nToken in base_code[cToken]):
#     print("Current token: {0}".format(nToken))
# else:
#     print("Unexpect '{0}' in line {1}, after '{2}' (line {3}).".format(nToken,nTokenLine,cToken,cTokenLine))


plt.figure("<base_code>")
nx.draw(base_code, with_labels=True, font_weight='bold')

plt.figure("<variable_declaration>")
nx.draw(variable_declaration, with_labels=True, font_weight='bold')

plt.show()