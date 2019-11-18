import json

from reserved import *

pypKeywords = {}
pypKeywords[return_token] = "return_token"
pypKeywords[canvas_token] = "canvas_token"
pypKeywords[begin_token] = "begin_token"
pypKeywords[end_token] = "end_token"
pypKeywords[elements_token] = "element_token"

for token in sketch_properties:
    pypKeywords[token] = "sketchProperty_token"    

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
    pypKeywords[token] = "boolean_token"

for token in sketch_type_list:
    pypKeywords[token] = "sketchType_token"

for token in misc:
    pypKeywords[token] = "misc_token"

try:
    with open(file_name, 'w') as f:
        json.dump(pypKeywords, f)
except:
    print("Error while creating {0}.".format(file_name))


