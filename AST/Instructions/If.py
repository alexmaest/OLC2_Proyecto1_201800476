from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class If(Instruccion):
    def __init__(self, condition, statement, other, row, column):
        self.condition = condition
        self.statement = statement
        self.other = other
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        condition = self.condition.executeInstruction(enviroment)
        if condition != None:
            if condition.typeVar == TYPE_DECLARATION.BOOLEAN:
                if condition.value == True:
                    return self.statement.executeInstruction(enviroment)
                elif condition.value == False:
                    if self.other != None:
                        return self.other.executeInstruction(enviroment)
                else:
                    listError.append(Error("Error: La condición no se ha podido evaluar","Local",self.row,self.column,"SEMANTICO"))
            else:
                listError.append(Error("Error: La condición no es un booleano","Local",self.row,self.column,"SEMANTICO"))