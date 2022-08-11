from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AssignmentSimple(Instruccion):

    def __init__(self,mut,id,type):
        self.mut = mut
        self.id = id
        self.type = type
    
    def executeInstruction(self, enviroment):
        typeVar = self.type.executeInstruction(enviroment)
        content = []
        content.append(self.mut)
        content.append(self.id)
        return Retorno(typeVar.typeVar,content,TYPE_DECLARATION.SIMPLE)