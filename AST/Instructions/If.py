from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class If(Instruccion):
    def __init__(self, condition, statement, other):
        self.condition = condition
        self.statement = statement
        self.other = other

    def executeInstruction(self, enviroment):
        condition = self.condition.executeInstruction(enviroment)
        if condition.typeVar == TYPE_DECLARATION.BOOLEAN:
            if condition.value == True:
                return self.statement.executeInstruction(enviroment)
            elif condition.value == False:
                if self.other != None:
                    return self.other.executeInstruction(enviroment)
            else:
                print("Error: La condición no se ha podido evaluar")
        else:
            print("Error: La condición no es un booleano")