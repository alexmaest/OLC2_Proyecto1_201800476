from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Access():
    def __init__(self, id):
        self.id = id

    def executeInstruction(self, enviroment):
        value = enviroment.getVariable(self.id)
        if(value == None):
            print("Error: La variable",self.id,"no existe")
            return None
        return Retorno(value.typeVar,value.value,value.typeSingle)