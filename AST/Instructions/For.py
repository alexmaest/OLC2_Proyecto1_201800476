from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Instructions.Declaration import Declaration
from AST.Instructions.Assignment import Assignment
from AST.Expressions.Access import Access
from AST.Expressions.Literal import Literal
from AST.Symbol.Symbol import Symbol

class For(Instruccion):
    def __init__(self, id, iterativeExp, statement):
        self.id = id
        self.iterativeExp = iterativeExp
        self.statement = statement

    def executeInstruction(self, enviroment):
        iterative = self.iterativeExp.executeInstruction(enviroment)
        if iterative != None:
            if iterative.typeSingle == TYPE_DECLARATION.ARRAY or iterative.typeSingle == TYPE_DECLARATION.VECTOR:
                enviroment.saveVariable(Symbol(iterative.typeVar,self.id,None,iterative.value[0].typeSingle,True))
                for single in iterative.value:
                    enviroment.editVariable(self.id,single.value)
                    returned = self.statement.executeInstruction(enviroment)
                    if returned != None:
                        if returned.typeSingle == TYPE_DECLARATION.BREAK:
                            break
                        elif returned.typeSingle == TYPE_DECLARATION.CONTINUE:
                            condition = self.condition.executeInstruction(enviroment)
                            continue
                        else:
                            return returned
            else:
                print("Error: La expresion no se puede iterar")
        else:
            print("Error: La expresion no se puede iterar porque no existe o no ha sido declarada")