from AST.Abstracts.Instruccion import Instruccion
from AST.Instructions.AssignmentSimple import AssignmentSimple
from AST.Symbol.Symbol import Symbol
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class DeclarationSingle(Instruccion):

    def __init__(self, asignation, expression):
        self.asignation = asignation
        self.expression = expression

    def executeInstruction(self, enviroment):
        content = self.asignation.executeInstruction(enviroment)
        exp = self.expression.executeInstruction(enviroment)
        if content != None and exp != None:
            if isinstance(self.asignation,AssignmentSimple):
                if exp.typeVar == content.typeVar:
                    if exp.typeSingle == TYPE_DECLARATION.SIMPLE:
                        enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0]))
                    else: print("Error: No se puede asignar un valor de varias dimensiones a la variable simple")
                else: print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",content.typeVar)
            else:
                #Comparar si las dimensiones a asignar son las mismas
                if exp.typeVar == content.typeVar:
                    if exp.typeSingle == TYPE_DECLARATION.ARRAY:
                        enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0]))
                    else: print("Error: No se puede asignar un valor simple a una variable de varias dimensiones")
                else: print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",content.typeVar)
        else: print("Error: No se pudo asignar la variable porque su valor es nulo")
