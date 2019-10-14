# Descrição dos Códigos
## alphabet.py

### Imports

#### -json

Utilizado para exportação do tipo *dictionary* como arquivo ".json", a ser utilizado pelo compilador

### Lists

A fim de manutenção de código, foram utilizadas listas para cada tipo de caracter presente no alfabeto da linguagem, separando-os em numeros (*digits*), letras (*letter*), elementos de operações matematicas (*math*), logicos (*logic*) e separadores (*separators*).

Tais listas passam por laços e são inclusos ao alfabeto (pypAlphabet) que é um *dictionary*, juntos ao caracter de comentário e de atribuição.

### Exportação

Utiliza-se da função "json.dump()" para exportar o *dictionary* para o arquivo "gbm_Alphabet.json". Tal operação encontra-se dentro de um "*try* ... *except*", a fim de informar caso um erro ocorra durante a exportação do alfabeto.



## reserved.py 

### Imports

#### -json

Utilizado para exportação do tipo *dictionary* como arquivo ".json", a ser utilizado pelo compilador

### Lists

A fim de manutenção de código, foram utilizadas listas para cada tipo de palavra reservada presente na linguagem, separando-as condicionais (*conditional*), laços de repetição (*loop*), ação (*action*), tipo de dado (*dataType*), lógicos (*logic*), literais (*literal*).

Tais listas passam por laços e são inclusos ao alfabeto (pypKeywords) que é um *dictionary*, juntos ao caracter de retorno.

### Exportação

Utiliza-se da função "json.dump()" para exportar o *dictionary* para o arquivo "gbm_reserved.json". Tal operação encontra-se dentro de um "*try* ... *except*", a fim de informar caso um erro ocorra durante a exportação do alfabeto.



## gbm.py

### Imports

#### -sys

Utilizado para executar comendos do sistema, como "sys.exit()", para encerrar o programa.

#### -json

Utilizado para importação do tipo *dictionary* como arquivo ".json", a ser utilizado pelo compilador

#### -re

biblioteca para *regex* (expressões regulares) e separação de elementos a serem *tokenizados*.

### Variáveis globais e classes

#### -pypToken

Uma classe de *token*, que possui o tipo de token (*literal*, *separator*, *id*, *logic*, *numeric* ...) e seu valor ("nome_da_variavel",42,"(","True", ";" ...)

#### -pypAlphabet e pypKeyword

Variáveis tipo *dictionary* que contém respectivamente o alfabeto e as palavras reservadas da linguagem. São importados por funções no decorrer do código.

### Funções (apresentadas em ordem de execução)

#### -main

Executada no inicio do código, responsável por chamar as funções seguintes

#### -load_alphabet_from_json()

Responsável por importar o alfabeto do arquivo "gbm_alphabet.json" para a variável global do tipo *dictionary* "pypAlphabet". Não possui parametros nem retorno e em caso de erro ao importar, informa o erro e a compilação é encerrada.

#### -load_keywords_from_json()

Responsável por importar as palavras reservadas do arquivo "gbm_reserved.json" para a variável global do tipo *dictionary* "pypKeywords". Não possui parametros nem retorno e em caso de erro ao importar, informa o erro e a compilação é encerrada.

#### -read_from_terminal()

Responsável por ler o nome do código fonte a ser compilado que foi entrado como parâmetro junto com a chamada do compilador. Não possui parâmetros. A função tenta ler o sys.argv[1] e retorna o valor para função *main*, e caso não exista, acusa que não há entrada de arquivo e a compilação é encerrada.

#### -import_file(source_code_name)

Responsável por importar o arquivo através do nome inserido. Possui como parâmetro uma *string* com o nome do arquivo. Retorna uma lista de *strings* caso o arquivo seja lido com sucesso, caso contrário um aviso de erro é apresentado e a compilação é encerrada.

#### -space_removal(source_code)

Responsável por chamar as funções "remove_duplicated_first_last_spaces()" e "remove_space_next_to_separators()". Tem como parâmetro "source_code" (lista de *strings*) e retorna uma lista de *strings* que só possui espaços entre letras e digitos.

#### -remove_duplicated_first_and_last_spaces(source_code)

Responsável por remover espaços presentes no começo de cada linha até o primeiro *char* que nao seja um espaço. Possui como parâmetro uma lista de *strings* e retorna uma lista de *strings* com o tratamento descrito.

#### -remove_space_next_to_separators(source_code)

Responsável por remover todos os espaços que não estejam entre letras e numeros. Possui como parâmetro uma lista de *strings* e retorna uma lista de *string* com o tratamento descrito.

#### -between_digits(str,char)

Responsável por informar se uma posição de uma string está entre digitos ou numeros. Utilizada para diminuir poluição na função "remove_space_next_to_separators()". Possui como parâmetro uma *string* ("str") e um inteiro ("char"). Retorna *True* se for verdadeiro, *False* caso contrário.

#### -comment_removal(source_code)

Responsável por eliminar comentários inseridos após um comando em uma determinada linha. Possui como parâmetro uma lista de *strings*, e retorna uma lista de *strings* com o tratamento descrito.

#### -charsAnalyser(source_code)

Responsável por identificar *chars* inválidos, e listar suas ocorrências por linha. Caso seja encontrado um *char* inválido, a linha de ocorrência é inserida numa lista, e a próxima linha é testada. No final da função, caso haja linhas de ocorrência na lista, os valores são exibidos e a compilação é encerrada. Possui como parâmetro uma lista de strings, e não possui retorno.

#### -toToken(source_code)

Responsável por *tokenizar* os elementos presentes no código. Seu retorno é uma lista ("token_source_code") de listas, com cada lista contendo uma instância da classe pypToken.

Inicialmente, as variáveis globais "pypAlphabet" e "pypKeywords" são importadas para o escopo.

A seguir, a variável "splited_source_code" recebe o retorno da função "split_by_separators(source_code)", explicada a seguir:

------------------------------------------------------------------------

##### --split_by_separators(source_code) 

Recebe como parâmetro uma lista de *strings*. Responsável por separar os elementos das *strings* para futura *tokenização*. Cada elemento torna-se um item de uma lista. 

Ao final da função, será retornada uma lista de listas (onde cada lista era anteriormente uma *string*)

Um laço para cara *string* em "source_code" é rodado. Inicialmente confere-se se a linha não é vazia e não é comentário. (Caso seja comentário, o unico elemento é inserido na lista correspondente a linha, contendo o comentário, caso seja uma linha vazia, a lista correspondente a linha é também vazia).

Em caso de linha válida, utiliza-se a função "split()" da biblioteca "re", em que a string é separada por elementos não alphanumericos, gerando uma lista de elementos.

Dois filtros (*filter*) são aplicados na lista, pois espaços são considerados elementos pela função "split()", e elementos vazios são inserios ao final e começo das linhas.

A seguir, procura-se por aspas duplas para juntar elementos que formam *strings*. Caso uma abertura de aspas duplas não possua um encerramento, é adicionada uma lista "unclosed_strings". (No final da função, caso haja elementos nessa lista, as linhas de ocorrência são exibidas e a compilação é encerrada). 

Adiciona-se uma flag "_str:" no inicio da string encontrada, a fim de futura *tokenização*.

É então executada uma rotina de agrupamento de elementos de operações lógicas. Caso haja um "=", "<" ou ">" seguido de "=". Tais elementos são agrupados para futura *tokenização*.

Após a execução de todas as verificações, a lista correspondente a *string* é inserida na lista correspondente a todo o código. 

----------------------------------------------------------------------------------------------------

É iniciado então um laço de repetição para cada lista (por convenção, chamada de "line") presente na lista "splited_source_code", confere-se se mesma não é vazia (caso seja, um pypToken "empty_line" é criado, contendo uma string vazia como seu valor, e inserido em "token_source_code").

Confere-se então se a lista é um comentário, e em caso positivo um pypToken "comment" é criado, contendo o comentário como seu valor.

Caso não seja um comentário. Uma nova lista ("new_line") é criada, e para cada item da *line* realiza-se operações de consulta no *dictionary* "pypAlphabet", caso seja um elemento do mesmo, insere-se na "new_line" uma instância de pypToken (*logic_operator*, *separator*, *math_operator*...) é criada com seu valor de checagem ("(", ";", "<"...) e inserida na new_line. 

Caso contrário, consulta-se então o *dictionary* "pypKeywords", caso seja um elemento do mesmo, insere-se na "new_line" uma instância de pypToken (*logic_token*, *literal_token*, *dataType_token*, *loop_token*...) é criada com o seu valor de chagem ("int","or","True","for" ...) e inserida na new_line .

Caso contrário, consulta-se através da função "is_a_number(item)", se o item é um numero (seja ele float ou inteiro), e caso seja, uma instância de pypToken "numeral_token" é criada com seu valor (42,3.1415,113 ...) e inserida na new_line.

Caso possua a flag de *strings* ("_str:"), uma instância de pypToken "literal_token" é criada com o seu valor ("nome do arquivo", "black", "white"...), removendo a flag localizada no começo da *string*, e inserida na new_line.

Caso não se encaixe em nenhum dos casos a cima, uma instância de pypToken "id_token" é criada com o seu valor ("x","i","nome_da_variavel","quadrado"...)  e inserida na new_line.

Ao final da iteração, a lista "new_line" é inserida na lista "token_source_code"

Ao final de todas as iteraçoes da lista "splited_source_code", a lista "token_source_code" é retornada para a função "main".

#### -isnt_comment(line)

Responsável por informar se uma *string* é um comentário, ou se uma lista possui um comentário como primeiro elemento. Possui com parâmetro uma lista ou uma *string*, e retorna True se não for um comentário, False se for um comentário. Utilizado para reduzir poluição em outras funções.

#### -is_a_number(str)

Responsável por determinar se uma string é um número (seja ele inteiro ou *float*) Retorna True se for, False se não for.

#### -check_tokens_id_values(token_source_code)

Responsável por verificar se os valores de pypTokens do tipo "id_token" estão de acordo com a regra de convenção da linguagem. Recebe como parâmetro uma lista de listas de instâncias de pypToken.

Inicia-se uma lista de erros "errors" vazia, e para cada instância de pypToken de cada lista (por convenção chamada de "line") da lista "token_source_code", chama-se a função "is_idToken_valid(token)", e caso não seja, adiciona-se o index da "line" na lista "errors".

Ao final da função, caso a lista "errors" não esteja vazia, informa-se as linhas onde os erros de nomeação foram encontrados e a compilação é encerrada.

#### -is_idToken_valid(token)

Responsável por informar se o valor de um pypToken "id_token" está de acordo com as regras da linguagem (no caso, o valor pode iniciar apenas com letras maiusculas ou minusculas, e conter ou terminar em numeros, letras maiuscular ou minusculas ou *underline* "_").

Retorna True caso seja válida, False caso contrário.

























