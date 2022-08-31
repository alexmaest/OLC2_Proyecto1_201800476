from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Assignment(Instruccion):

    def __init__(self,idList,expression):
        self.idList = idList
        self.expression = expression
    
    def executeInstruction(self, enviroment):
        exp = self.expression.executeInstruction(enviroment)
        if exp != None:
            exist = enviroment.getVariable(self.idList[0].id.id)
            if exist != None:
                if exist.mutable:
                    singleId = self.idList[0].id.executeInstruction(enviroment)
                    if len(self.idList) == 1:
                        #Se buscan Variables que sean normales, arrays, vectores y structs
                        if exp.typeVar == None and exp.typeSingle == TYPE_DECLARATION.VECTOR:
                            if singleId.typeSingle == TYPE_DECLARATION.VECTOR:
                                enviroment.editVariable(self.idList[0].id.id, exp.value)
                            else: 
                                print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                        else:
                            if singleId.typeVar == exp.typeVar:
                                if singleId.typeSingle == exp.typeSingle:
                                    enviroment.editVariable(self.idList[0].id.id, exp.value)
                                else: 
                                    print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                            else: 
                                print("Error: No se puede asignar un valor",exp.typeVar,"a una variable tipo",singleId.typeVar)
                    else:
                        #Se buscan atributos de structs
                        if exist.typeSingle == TYPE_DECLARATION.STRUCT:
                            founded = self.foundAttribute(exist, self.idList, 1)
                            if founded != None:
                                if founded.typeVar == exp.typeVar:
                                    if founded.typeSingle == exp.typeSingle:
                                        founded.value = exp.value
                                    else: 
                                        print("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable")
                                else: 
                                    print("Error: No se puede asignar un valor",exp.typeVar,"a un atributo tipo",founded.typeVar)
                        else: 
                            print("Error: La variable",self.idList[0].id.id,"no es un struct para que acceda a sus atributos")
                else:
                    print("Error: La variable no es mutable")
            else:
                print("Error: La variable aún no ha sido declarada")

    def foundAttribute(self, variable, list, number):
        if list[number].id in variable.value:
            if (number + 1) == len(list):
                return variable.value[list[number].id]
            else:
                return self.foundAttribute(variable.value[list[number].id], list, number+1)
        else:
            print("Error: Atributo",list[number].id,"no encontrado de la variable",list[0].id.id) 
            return None
