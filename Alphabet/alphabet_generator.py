import json

from alphabet import *

pypAlphabet = {}
pypAlphabet[commentTag] = "comment_tag"
pypAlphabet[attribution_tag] = "attribution_token"
pypAlphabet[semicolon_tag] = "semicolon"

for element in digits_list:
    pypAlphabet[element] = "digit"

for element in letters_list:
    pypAlphabet[element] = "letter"

for element in mathElements_list:
    pypAlphabet[element] = "math_operator"

for element in logicElements_list:
    pypAlphabet[element] = "logic_operator"

for element in separators_list:
    pypAlphabet[element] = "separator"

try:
    with open(file_name, 'w') as f:
        json.dump(pypAlphabet, f)
except:
    print("Error while creating {0}.".format(file_name))