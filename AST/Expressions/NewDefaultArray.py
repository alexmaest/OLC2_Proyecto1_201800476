from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class NewDefaultArray():

    finalArray = []

    def __init__(self, value, size):
        self.value = value
        self.size = size
        self.finalArray = []

    def executeInstruction(self,enviroment):
        self.finalArray = []
        singleValue = self.value.executeInstruction(enviroment)
        singleSize = self.size.executeInstruction(enviroment)
        if singleSize.typeVar == TYPE_DECLARATION.INTEGER:
            for number in range(singleSize.value):
                self.finalArray.append(singleValue.value)
            return Retorno(singleValue.typeVar,self.finalArray,TYPE_DECLARATION.ARRAY)
        else:
            print("Error: No se ha podido crear la lista debido a que el tamaño para la lista no es un entero")    
            return Retorno(singleValue.typeVar,None,TYPE_DECLARATION.ARRAY)