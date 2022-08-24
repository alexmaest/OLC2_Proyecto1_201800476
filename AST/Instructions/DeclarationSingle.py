from AST.Abstracts.Instruccion import Instruccion
from AST.Instructions.ListArraySimple import ListArraySimple
from AST.Symbol.Symbol import Symbol
from AST.Abstracts.Retorno import TYPE_DECLARATION

class DeclarationSingle(Instruccion):

    def __init__(self, asignation, expression):
        self.asignation = asignation
        self.expression = expression

    def executeInstruction(self, enviroment):
        content = self.asignation.executeInstruction(enviroment)
        exp = self.expression.executeInstruction(enviroment)
        if content != None and exp != None:
            if content.typeSingle == TYPE_DECLARATION.SIMPLE or content.typeSingle == TYPE_DECLARATION.VECTOR:
                if exp.typeVar == content.typeVar:
                    if content.typeSingle == exp.typeSingle:
                        enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0]))
                    else: print("Error: Está tratando de asignar un valor de diferentes dimensiones a las que intenta declarar")
                else: print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",content.typeVar)
            else:
                #Comparar si las dimensiones a asignar son las mismas
                if exp.typeVar == content.typeVar:
                    if exp.typeSingle == TYPE_DECLARATION.ARRAY:
                        if isinstance(self.asignation.type, ListArraySimple):
                            if self.dimensionalCompare(exp.value, content.value[2]):
                                enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0]))
                            else: print("Error: Está tratando de asignar una lista de diferentes dimensiones a las que intenta declarar")
                        else:
                            enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0]))
                    else: print("Error: No se puede asignar un valor simple a una variable de varias dimensiones")
                else: print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",content.typeVar)
        else: print("Error: No se pudo asignar la variable porque su valor es nulo")

    def dimensionalCompare(self, list1, list2):
        if len(list1) == len(list2):
            if isinstance(list1[0].value,list):
                if isinstance(list2[0],list):
                    return self.dimensionalCompare(list1[0].value,list2[0])
                else:
                    return False
            elif isinstance(list2[0],list):
                if isinstance(list1[0].value,list):
                    return self.dimensionalCompare(list1[0].value,list2[0])
                else:
                    return False
            else:
                return True
        else:
            return False

    '''
        [[1,4],[1,4],[1,4],[1,4],[1,4]]
        [[1,4],4,3,2,1]
    '''