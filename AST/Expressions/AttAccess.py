from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno
from AST.Expressions.CallNative import CallNative
from AST.Expressions.Handler import Handler
from AST.Instructions.Native import Native
from enum import Enum

class AttAccess():
    def __init__(self, expList):
        self.expList = expList
    
    def executeInstruction(self, enviroment):
        exist = enviroment.getVariable(self.expList[0].id.id)
        if exist != None:
            singleId = self.expList[0].id.executeInstruction(enviroment)
            if len(self.expList) == 1:
                #Se retornan Variables que sean normales, arrays, vectores y structs
                return singleId
            else:
                #Se retornan atributos de structs
                return self.foundAttribute(exist, self.expList, 1, enviroment)
        else:
            print("Error: La variable",self.expList[0].id.id,"no existe")
    
    def foundAttribute(self, variable, list, number, enviroment):
        if isinstance(list[number].id,CallNative):
            callNativeFunction = Native(Handler(variable.typeVar,variable.value,variable.typeSingle),list[number].id)
            return callNativeFunction.executeInstruction(enviroment)
        else:
            if list[number].id in variable.value:
                if variable.value[list[number].id].value[0]:
                    typeVar = variable.value[list[number].id].typeVar
                    value = variable.value[list[number].id].value
                    typeSingle = variable.value[list[number].id].typeSingle
                    if (number + 1) == len(list):
                        return Retorno(typeVar,value[1],typeSingle)
                    else:
                        return self.foundAttribute(Retorno(typeVar,value[1],typeSingle), list, number+1, enviroment)
                else:
                    print("Error: El atributo",list[number].id,"de la instrucción no es público")
                    return None
            else:
                print("Error: Atributo",list[number].id,"no encontrado de la variable",list[0].id.id) 
                return None