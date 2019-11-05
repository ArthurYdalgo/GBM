import json

file_name = "gbm_reserved.json"

conditional_list = ['if','else','elif','switch','case','default']

loop_list = ['for','while','do','break']

action_list = ['draw','erase','export','import']

data_type_list = ['int','string','float','bool']

sketch_type_list = ['circle','square','swarm','web','tree']

logic_list = ['and','or']

literal_list = ['True','False']

return_token = 'return'
canvas_token = 'canvas'

begin_token = 'begin'
end_token = 'end'

elements_token = 'elements'

pypKeywords = {}
pypKeywords[return_token] = "return_token"
pypKeywords[canvas_token] = "canvas_token"
pypKeywords[begin_token] = "begin_token"
pypKeywords[end_token] = "end_token"
pypKeywords[elements_token] = "element_token"



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

for token in sketch_type_list:
    pypKeywords[token] = "sketchType_token"

try:
    with open(file_name, 'w') as f:
        json.dump(pypKeywords, f)
except:
    print("Error while creating {0}.".format(file_name))


