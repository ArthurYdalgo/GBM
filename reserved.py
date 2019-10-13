import json

conditional_list = ['if','else','elif','switch','case','default']

loop_list = ['for','while','do','break']

action_list = ['draw','erase','export','import']

data_type_list = ['int','float','struct','canvas','template','circle','square']

logic_list = ['and','or']

literal_list = ['True','False']

return_token = 'return'

pypKeywords = {}
pypKeywords[return_token] = "return_token"

for token in conditional_list:
    pypKeywords[token] = "conditional_token"

for token in loop_list:
    pypKeywords[token] = "loop_token"

for token in data_type_list:
    pypKeywords[token] = "dataType_token"

for token in logic_list:
    pypKeywords[token] = "logic_token"

for token in action_list:
    pypKeywords[token] = "action_token"

for token in literal_list:
    pypKeywords[token] = "literal_token"

try:
    with open('pyp_reserved.json', 'w') as f:
        json.dump(pypKeywords, f)
except:
    print("Error while creating 'pyp_reserved.py'.")


