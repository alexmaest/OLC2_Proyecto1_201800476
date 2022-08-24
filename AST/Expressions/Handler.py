from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Handler():
    def __init__(self, typeVar, value, typeSingle):
        self.typeVar = typeVar
        self.value = value
        self.typeSingle = typeSingle

    def executeInstruction(self,enviroment):
        return Retorno(self.typeVar,self.value,self.typeSingle)