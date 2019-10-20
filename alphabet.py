import json

file_name = "gbm_alphabet.json"

digits_list = ['0','1','2','3','4','5','6','7','8','9']

lowerCase_list = ['_',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters_list = lowerCase_list+upperCase_list

mathElements_list = ['+','-','/','*','%','^']

logicElements_list = ['<','>','<=','==','>=','!']

separators_list = ['(',')','[',']','{','}','"','\'','.',',',':']
#separators_list = ['(',')','[',']','{','}','"','\'','.',';',',',':']

commentTag = '#'
attribution_tag = "="
semicolon_tag = ";"

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