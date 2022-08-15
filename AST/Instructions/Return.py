from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Return(Instruccion):
    def __init__(self, exp):
        self.exp = exp
    
    def executeInstruction(self, enviroment):
        if self.exp != None:
            returned = self.exp.executeInstruction(enviroment)
            return Retorno(returned.typeVar,returned.value,returned.typeSingle)
        else:
            return Retorno(None,None,TYPE_DECLARATION.RETURN)