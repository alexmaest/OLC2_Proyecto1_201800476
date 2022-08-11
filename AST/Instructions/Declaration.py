from AST.Abstracts.Instruccion import Instruccion
from AST.Symbol.Symbol import Symbol

class Declaration(Instruccion):

    def __init__(self, mutable, assignation):
        self.mutable = mutable
        self.assignation = assignation

    def executeInstruction(self, enviroment):
        exp = self.assignation.getExpression().executeInstruction(enviroment)
        if exp.value != None:
            enviroment.saveVariable(Symbol(exp.typeVar,self.assignation.id.id,None,exp.typeSingle,self.mutable))
            self.assignation.executeInstruction(enviroment)
        else:
                print("Error: La variable no ha podido ser declarada")