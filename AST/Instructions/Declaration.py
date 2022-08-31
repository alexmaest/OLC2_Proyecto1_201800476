from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import TYPE_DECLARATION
from AST.Symbol.Symbol import Symbol

class Declaration(Instruccion):

    def __init__(self, mutable, assignation):
        self.mutable = mutable
        self.assignation = assignation

    def executeInstruction(self, enviroment):
        exp = self.assignation.expression.executeInstruction(enviroment)
        if exp != None:
            if exp.typeVar == None and exp.typeSingle == TYPE_DECLARATION.VECTOR:
                print("Error: La variable no ha podido ser declarada porque no posee un tipo para crear un vector")
            else:
                enviroment.saveVariable(Symbol(exp.typeVar,self.assignation.idList[0].id.id,exp.value,exp.typeSingle,self.mutable))
        else:
            print("Error: La variable no ha podido ser declarada")