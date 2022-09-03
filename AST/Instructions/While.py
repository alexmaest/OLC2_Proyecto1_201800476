from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class While(Instruccion):
    def __init__(self, condition, statement, row, column):
        self.condition = condition
        self.statement = statement
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        condition = self.condition.executeInstruction(enviroment)
        if condition != None:
            if condition.typeVar == TYPE_DECLARATION.BOOLEAN:
                while condition.value == True:
                    returned = self.statement.executeInstruction(enviroment)
                    if returned != None:
                        if returned.typeSingle == TYPE_DECLARATION.BREAK:
                            break
                        elif returned.typeSingle == TYPE_DECLARATION.CONTINUE:
                            condition = self.condition.executeInstruction(enviroment)
                            continue
                        else:
                            return returned
                    condition = self.condition.executeInstruction(enviroment)
                    if condition.typeVar != TYPE_DECLARATION.BOOLEAN:
                        listError.append(Error("Error: La condición no es un booleano","Local",self.row,self.column,"SEMANTICO"))
            else:
                listError.append(Error("Error: La condición no es un booleano","Local",self.row,self.column,"SEMANTICO"))
        else:
            listError.append(Error("Error: No se ha podido ejecutar la sentencia While","Local",self.row,self.column,"SEMANTICO"))