from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class While(Instruccion):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement

    def executeInstruction(self, enviroment):
        condition = self.condition.executeInstruction(enviroment)
        if condition != None:
            if condition.typeVar == TYPE_DECLARATION.BOOLEAN:
                while condition.value == False:
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
                        print("Error: La condición no es un booleano")
            else:
                print("Error: La condición no es un booleano")
        else:
            print("Error: No se ha podido ejecutar la sentencia While")