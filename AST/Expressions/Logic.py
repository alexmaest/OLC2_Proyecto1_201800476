from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from enum import Enum

class TYPE_LOGICAL(Enum):
    AND = 0,
    OR = 1,
    NOT = 2,

class Logic():
    def __init__(self, lExp, type, rExp):
        self.lExp = lExp
        self.type = type
        self.rExp = rExp
    
    def executeInstruction(self, enviroment):
        leftValue = self.lExp.executeInstruction(enviroment)
        rightValue = self.rExp.executeInstruction(enviroment)
        
        if leftValue != None and rightValue != None:
            if self.type == TYPE_LOGICAL.AND:
                result = leftValue.value and rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_LOGICAL.OR:
                result = leftValue.value or rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_LOGICAL.NOT:
                result = not(leftValue.value)
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            else:
                print("Error: No se ha podido realizar la logica de comparación")
                return None
        else:
            print("Error: No se ha podido realizar la logica de comparación")
            return None