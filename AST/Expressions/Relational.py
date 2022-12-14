from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError
from enum import Enum

class TYPE_RELATIONAL(Enum):
    IGUALI = 0,
    DIF = 1,
    MAYOR = 2,
    MENOR = 3,
    MAYORI = 4,
    MENORI = 5

class Relational():
    def __init__(self, lExp, type, rExp, row, column):
        self.lExp = lExp
        self.type = type
        self.rExp = rExp
        self.row = row
        self.column = column
    
    def executeInstruction(self, enviroment):
        leftValue = self.lExp.executeInstruction(enviroment)
        rightValue = self.rExp.executeInstruction(enviroment)
        if leftValue != None and rightValue != None:
            if self.type == TYPE_RELATIONAL.IGUALI:
                result = leftValue.value == rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_RELATIONAL.DIF:
                result = leftValue.value != rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_RELATIONAL.MAYOR:
                result = leftValue.value > rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_RELATIONAL.MENOR:
                result = leftValue.value < rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_RELATIONAL.MAYORI:
                result = leftValue.value >= rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            elif self.type == TYPE_RELATIONAL.MENORI:
                result = leftValue.value <= rightValue.value
                return Retorno(TYPE_DECLARATION.BOOLEAN, result, TYPE_DECLARATION.SIMPLE)
            else:
                listError.append(Error("Error: No se ha podido realizar la comparaci??n","Local",self.row,self.column,"SEMANTICO"))
                return None
        else:
            listError.append(Error("Error: No se ha podido realizar la comparaci??n","Local",self.row,self.column,"SEMANTICO"))
            return None