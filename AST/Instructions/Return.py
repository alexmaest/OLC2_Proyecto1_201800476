from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Return(Instruccion):
    def __init__(self, exp):
        self.exp = exp
    
    def executeInstruction(self, enviroment):
        if self.exp != None:
            returned = self.exp.executeInstruction(enviroment)
            if returned != None:
                return Retorno(returned.typeVar,returned.value,returned.typeSingle)
            else:
                None
        else:
            None