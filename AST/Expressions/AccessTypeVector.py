from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.CallFunction import CallFunction

class AccessTypeVector():
    def __init__(self, listId):
        self.listId = listId

    def executeInstruction(self, enviroment):
        for single in self.listId:
            returned = single.executeInstruction(enviroment)
            if returned != None:
                if not isinstance(single,CallFunction):
                    if len(self.listId) == 1:
                        return Retorno(returned.typeVar,returned.value,TYPE_DECLARATION.VECTOR)
                else:
                    print("Error: Una llamada de una función no puede ser un tipo de variable, lista o vector")
                    return None
            else:
                return None