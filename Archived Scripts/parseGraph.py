import json
from time import gmtime, strftime

def isTerminal(nome):
    size = len(nome)
    if(nome[0]=="<" and nome[size-1]==">"):
        return True
    else:
        return False

class state:
    pathList = {}
    def __init__(self,pypTokenValue,self_pai):   
        if(isTerminal(pypTokenValue)):
            self.terminal = True
        else:
            self.terminal = False
        self.pai = self_pai
        self.token = pypTokenValue
        self.pathList = {}        
    
    def walk(self,pathName):
        if(pathName in pathList):
            return pathList[pathName]
     
    def isPath(self,pathName):
        if(pathName in pathList):
            return True
        else:    
            return False
    
    def setPaths(self,path_):
        if (type(path_) is str):
            self.pathList[path_] = state(path_,self)
        elif(type(path_) is list ):
            for path in path_:
                self.pathList[path_] = state(path_,self)

    def walkBack(self):
        return self.pai

nonTermianlParseGraph = {}
parseGraph={}
print("Importa parser? S/N")  
importChoice = str(raw_input(""))
if(importChoice=="S" or importChoice == "s"):
    name = str(raw_input(""))
    
    with open(name) as f:
        parseGraph
        parseGraph = json.load(f)        
else:
    derivation_name = raw_input("Nome da derivacao: ")

    parseGraph = state("<{0}>".format(derivation_name),-1)
    parseGraph.pai = parseGraph

def menu(cNode):
    print("No atual: {0}.".format(cNode.token))
    print("Atuais caminhos disponivels ({0}):".format(len(cNode.pathList)))
    for path in cNode.pathList:
        print(path)
    
    print ("")
    print("Escolha:")
    print("1-Caminhar")
    print("2-Adicionar")
    print("3-Voltar")
                         

def main():
    cNode = parseGraph
    #try:
    while(True):
        menu(cNode)
        escolha = int(raw_input("Escolha: "))
        if(escolha==1):
            nome = str(raw_input("Insira o token: "))
            cNode = cNode.walk(nome)
        elif(escolha==2):
            qtd = int(raw_input("Quantidade: "))
            print("Insira os tokens:")
            for i in range(qtd):             
                nome = str(raw_input(""))
                cNode.setPaths(nome)
        elif(escolha==3):
            cNode = cNode.pai
    # except:
    #     name = "parseGraph({0})_Backup_{1}".format(derivation_name,strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    #     with open(name, 'w') as f:
    #         json.dump(parseGraph, f)


            


main()