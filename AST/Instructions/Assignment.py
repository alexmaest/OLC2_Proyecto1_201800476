from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Assignment(Instruccion):

    def __init__(self,id,expression):
        self.id = id
        self.expression = expression
        self.exp = None
    
    def executeInstruction(self, enviroment):
        self.exp = self.expression.executeInstruction(enviroment)
        if self.exp != None:
            exist = enviroment.getVariable(self.id.id)
            if exist != None:
                if exist.mutable:
                    if self.compareTypes(enviroment):
                        enviroment.editVariable(self.id.id, self.exp.value)
                else:
                    print("Error: La variable no es mutable")
            else:
                print("Error: La variable aún no ha sido declarada")

    def compareTypes(self, enviroment):
        singleId = self.id.executeInstruction(enviroment)
        if singleId.typeVar == self.exp.typeVar:
            if singleId.typeSingle == self.exp.typeSingle:
                return True
            else: 
                print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                return False
        else: 
            print("Error: No se puede asignar un valor",self.exp.typeVar,"a una variable tipo",singleId.typeVar)
            return False