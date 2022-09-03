from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import TYPE_DECLARATION
from AST.Symbol.Symbol import Symbol
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class Declaration(Instruccion):

    def __init__(self, mutable, assignation, row, column):
        self.mutable = mutable
        self.assignation = assignation
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        exp = self.assignation.expression.executeInstruction(enviroment)
        if exp != None:
            if exp.typeVar == None and exp.typeSingle == TYPE_DECLARATION.VECTOR:
                listError.append(Error("Error: La variable no ha podido ser declarada porque no posee un tipo para crear un vector","Local",self.row,self.column,"SEMANTICO"))
            else:
                enviroment.saveVariable(Symbol(exp.typeVar,self.assignation.idList[0].id.id,exp.value,exp.typeSingle,self.mutable,self.row,self.column))
        else:
            listError.append(Error("Error: La variable no ha podido ser declarada","Local",self.row,self.column,"SEMANTICO"))