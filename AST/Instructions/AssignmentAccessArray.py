from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AssignmentAccessArray(Instruccion):

    def __init__(self,accessArray,expression):
        self.accessArray = accessArray
        self.expression = expression
        self.isDeclaration = False
    
    def executeInstruction(self, enviroment):
        access = self.accessArray.executeInstruction(enviroment)
        exp = self.expression.executeInstruction(enviroment)
        if access != None and exp != None:
            exist = enviroment.getVariable(self.accessArray.id.id)
            if exist != None:
                if self.isDeclaration or exist.mutable:
                    if self.compareTypes(access,exp,enviroment):
                        access.value = exp.value
                    else:
                        #Ya se dijeron los errores así que no se hace nada
                        pass
                else:
                    print("Error: La Variable a la que desea acceder no es mutable")
        else:
            print("Error: La Posición de la variable que desea acceder no pudo ser modificada")

    def compareTypes(self, access, exp, enviroment):
        if access.typeVar == exp.typeVar:
            if access.typeSingle == exp.typeSingle:
                if access.typeSingle == TYPE_DECLARATION.ARRAY and exp.typeSingle == TYPE_DECLARATION.ARRAY:
                    if len(access.value) == len(exp.value):
                        return True
                    else: 
                        print("Error: La longitud del arreglo que desea asignar es diferente a la declarada")
                        return False
                else: return True
            else: 
                print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                return False
        else: 
            print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",access.typeVar)
            return False
    
        '''
        position = [0]
        value = [1,2,3,4,5]

        position = [1,2,0]
        value = [[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]
        '''