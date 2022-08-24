from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.AccessTypeVector import AccessTypeVector

class AccessTypeArray():
    def __init__(self, type):
        self.type = type

    def executeInstruction(self, enviroment):
        returned = self.type.executeInstruction(enviroment)
        if returned != None:
            if not isinstance(self.type,AccessTypeVector):
                return Retorno(returned.typeVar,returned.value,TYPE_DECLARATION.ARRAY)
            else:
                print("Error: Un vector no puede ser un tipo de variable para un array")
                return None
        else:
            return None