from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class NewVector():

    def __init__(self, list):
        self.list = list

    def executeInstruction(self,enviroment):
        vector = self.list.executeInstruction(enviroment)
        if vector != None:
            return Retorno(vector.typeVar, vector.value, TYPE_DECLARATION.VECTOR)        
        else: return None    