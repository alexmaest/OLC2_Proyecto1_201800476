from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AssignmentAccessArray(Instruccion):

    def __init__(self,accessArray,expression,attributes):
        self.accessArray = accessArray
        self.expression = expression
        self.attributes = attributes
        self.isDeclaration = False
    
    def executeInstruction(self, enviroment):
        access = self.accessArray.executeInstruction(enviroment)
        exp = self.expression.executeInstruction(enviroment)
        if access != None and exp != None:
            exist = enviroment.getVariable(self.accessArray.id.id)
            if exist != None:
                if self.attributes == None:
                    if self.isDeclaration or exist.mutable:
                        if self.compareTypes(access,exp,enviroment):
                            access.value = exp.value
                        else:
                            #Ya se dijeron los errores así que no se hace nada
                            pass
                    else:
                        print("Error: La Variable a la que desea acceder no es mutable")
                else:
                    founded = self.foundAttribute(access,self.attributes,0)
                    if founded != None:
                        if founded.typeVar == exp.typeVar:
                            if founded.typeSingle == exp.typeSingle:
                                newValue = []
                                newValue.append(founded.value[0])
                                newValue.append(exp.value)
                                founded.value = newValue
                            else: 
                                print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                        else: 
                            print("Error: No se puede asignar un valor",exp.typeVar,"a un atributo tipo",founded.typeVar)
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
    

    def foundAttribute(self, variable, list, number):
        if list[number].id in variable.value:
            if (number + 1) == len(list):
                return variable.value[list[number].id]
            else:
                typeVar = variable.value[list[number].id].typeVar
                value = variable.value[list[number].id].value
                typeSingle = variable.value[list[number].id].typeSingle
                return self.foundAttribute(Retorno(typeVar,value[1],typeSingle), list, number+1)
        else:
            print("Error: Atributo",list[number].id,"no encontrado de la variable",list[0].id.id) 
            return None
        '''
        position = [0]
        value = [1,2,3,4,5]

        position = [1,2,0]
        value = [[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]
        '''