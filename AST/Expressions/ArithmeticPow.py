from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
import math

class ArithmeticPow():

    def __init__(self, type, lExp, rExp):
        self.type = type
        self.lExp = lExp
        self.rExp = rExp

    def executeInstruction(self, enviroment):
        lReturn = self.lExp.executeInstruction(enviroment)
        rReturn = self.rExp.executeInstruction(enviroment)
        if self.type == True:
            if lReturn.typeVar == TYPE_DECLARATION.INTEGER and rReturn.typeVar == TYPE_DECLARATION.INTEGER:
                return Retorno(TYPE_DECLARATION.INTEGER,int(math.pow(lReturn.value,rReturn.value)),TYPE_DECLARATION.SIMPLE)
            else:
                print("Error: La función pow() solo funciona con ambas expresiones enteras")
        else:
            if lReturn.typeVar == TYPE_DECLARATION.FLOAT and rReturn.typeVar == TYPE_DECLARATION.FLOAT:
                return Retorno(TYPE_DECLARATION.FLOAT,float(math.pow(lReturn.value,rReturn.value)),TYPE_DECLARATION.SIMPLE)
            else:
                print("Error: La función powf() solo funciona con ambas expresiones decimales")
