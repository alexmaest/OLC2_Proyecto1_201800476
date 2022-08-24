from AST.Abstracts.Instruccion import Instruccion
from AST.Symbol.Symbol import Symbol

class Declaration(Instruccion):

    def __init__(self, mutable, assignation):
        self.mutable = mutable
        self.assignation = assignation

    def executeInstruction(self, enviroment):
        exp = self.assignation.expression.executeInstruction(enviroment)
        if exp != None:
            enviroment.saveVariable(Symbol(exp.typeVar,self.assignation.id.id,exp.value,exp.typeSingle,self.mutable))
        else:
            print("Error: La variable no ha podido ser declarada")