from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Loop(Instruccion):
    def __init__(self, statement):
        self.statement = statement

    def executeInstruction(self, enviroment):
        while True:
            returned = self.statement.executeInstruction(enviroment)
            if returned != None:
                if returned.typeSingle == TYPE_DECLARATION.BREAK:
                    break
                elif returned.typeSingle == TYPE_DECLARATION.CONTINUE:
                    continue
                else:
                    return returned