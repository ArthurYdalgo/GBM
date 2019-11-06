import json

from reserved import *

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


