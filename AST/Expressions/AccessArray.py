from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AccessArray():
    def __init__(self, id, listAccess):
        self.id = id
        self.listAccess = listAccess

    def executeInstruction(self,enviroment):
        pass