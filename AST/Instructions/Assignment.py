from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Assignment(Instruccion):

    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
    
    def executeInstruction(self, enviroment):
        exp = self.expression.executeInstruction(enviroment)
        if exp.value != None:
            if enviroment.getVariable(self.id.id) != None:
                if self.compareTypes(enviroment):
                    enviroment.editVariable(self.id.id, exp.value)
            else:
                print("Error: La variable aún no ha sido declarada")

    def compareTypes(self, enviroment):
        singleId = self.id.executeInstruction(enviroment)
        value = self.expression.executeInstruction(enviroment)
        if singleId.typeVar == value.typeVar:
            if singleId.typeSingle == value.typeSingle:
                return True
            else: 
                print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                return False
        else: 
            print("Error: No se puede asignar un valor",value.typeVar,"a una variable tipo",singleId.typeVar)
            return False
    
    def getExpression(self):
        return self.expression