from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class NewArray():

    finalArray = []

    def __init__(self, listExp):
        self.listExp = listExp
        self.finalArray = []

    def executeInstruction(self,enviroment):
        self.finalArray = []
        typeArray = None
        typeDimension = None
        for singleExp in self.listExp:
            exp = singleExp.executeInstruction(enviroment)
            if typeArray == None and typeDimension == None:
                typeArray = exp.typeVar
                typeDimension = exp.typeSingle
                self.finalArray.append(exp.value)
            else:
                if exp.typeVar == typeArray:
                    if exp.typeSingle == typeDimension:
                        self.finalArray.append(exp.value)
                    else:
                        print("Error: No se ha podido crear la lista debido a que todas las expresiones no son de la misma dimensión")    
                        return Retorno(typeArray,None,TYPE_DECLARATION.ARRAY)
                else:
                    print("Error: No se ha podido crear la lista debido a que todas las expresiones no son del mismo tipo")    
                    return Retorno(typeArray,None,TYPE_DECLARATION.ARRAY)
        return Retorno(typeArray,self.finalArray,TYPE_DECLARATION.ARRAY)