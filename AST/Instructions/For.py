from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.ForIterative import ForIterative
from AST.Symbol.Enviroment import Enviroment
from AST.Symbol.Symbol import Symbol

class For(Instruccion):
    def __init__(self, id, iterativeExp, statement):
        self.id = id
        self.iterativeExp = iterativeExp
        self.statement = statement

    def executeInstruction(self, enviroment):
        if isinstance(self.iterativeExp,ForIterative):
            iterativeL = self.iterativeExp.lExp.executeInstruction(enviroment)
            iterativeR = self.iterativeExp.rExp.executeInstruction(enviroment)
            Pass = False
            if iterativeL.typeSingle == TYPE_DECLARATION.SIMPLE and iterativeR.typeSingle == TYPE_DECLARATION.SIMPLE:
                if iterativeL.typeVar == TYPE_DECLARATION.INTEGER and iterativeR.typeVar == TYPE_DECLARATION.INTEGER:
                    Pass = True
                elif iterativeL.typeVar == TYPE_DECLARATION.FLOAT and iterativeR.typeVar == TYPE_DECLARATION.FLOAT:
                    Pass = True
                else:
                    print("Error: No se puede iterar debido a que el rango no es correcto")
            else:
                print("Error: No se puede iterar debido a que el rango no son valores simples")
            if Pass:
                newEnv = Enviroment(enviroment)
                newEnv.saveVariable(Symbol(iterativeL.typeVar,self.id,None,iterativeL.typeSingle,True))
                for single in range(iterativeL.value,iterativeR.value):
                    newEnv.editVariable(self.id,single.value)
                    returned = self.statement.executeInstruction(newEnv)
                    if returned != None:
                        if returned.typeSingle == TYPE_DECLARATION.BREAK:
                            break
                        elif returned.typeSingle == TYPE_DECLARATION.CONTINUE:
                            continue
                        else:
                            return returned
        else:
            iterative = self.iterativeExp.executeInstruction(enviroment)
            if iterative != None:
                if iterative.typeSingle == TYPE_DECLARATION.ARRAY or iterative.typeSingle == TYPE_DECLARATION.VECTOR:
                    newEnv = Enviroment(enviroment)
                    singleIterative = None
                    if iterative.typeSingle == TYPE_DECLARATION.ARRAY:
                        newEnv.saveVariable(Symbol(iterative.typeVar,self.id,None,iterative.value[0].typeSingle,True))
                        singleIterative = iterative.value
                    else:
                        newEnv.saveVariable(Symbol(iterative.typeVar,self.id,None,iterative.value[1][0].typeSingle,True))
                        singleIterative = iterative.value[1]
                    for single in singleIterative:
                        newEnv.editVariable(self.id,single.value)
                        returned = self.statement.executeInstruction(newEnv)
                        if returned != None:
                            if returned.typeSingle == TYPE_DECLARATION.BREAK:
                                break
                            elif returned.typeSingle == TYPE_DECLARATION.CONTINUE:
                                continue
                            else:
                                return returned
                else:
                    print("Error: La expresion no se puede iterar")
            else:
                print("Error: La expresion no se puede iterar porque no existe o no ha sido declarada")