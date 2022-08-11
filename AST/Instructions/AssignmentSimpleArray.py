from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AssignmentSimpleArray(Instruccion):

    def __init__(self,mut,id,arrays):
        self.mut = mut
        self.id = id
        self.arrays = arrays

    def executeInstruction(self, enviroment):
        exp = self.arrays.executeInstruction(enviroment)
        content = []
        content.append(self.mut)
        content.append(self.id)
        content.append(exp.value)
        return Retorno(exp.typeVar,content,exp.typeSingle)