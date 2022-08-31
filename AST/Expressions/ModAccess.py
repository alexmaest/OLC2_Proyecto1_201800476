from unicodedata import name
from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno
from AST.Expressions.CallFunction import CallFunction
from AST.Expressions.Handler import Handler
from AST.Expressions.Access import Access
from AST.Instructions.Function import Function
from AST.Instructions.Modulo import Modulo
from AST.Symbol.Enviroment import Enviroment
from enum import Enum

class ModAccess():
    def __init__(self, nameList, functionCall):
        self.nameList = nameList
        self.functionCall = functionCall
    
    def executeInstruction(self, enviroment):
        #Se retornan funciones dentro de modulos
        found = enviroment.getModule(self.nameList[0])#Modulo()
        if found != None:
            self.nameList.append(self.functionCall.id)
            return self.saveModuleInstructions(self.nameList, found, enviroment.getGlobal(), 1, enviroment)
        else: 
            print("Error: El modulo con id",self.nameList[0],"no existe")
            return None

    def saveModuleInstructions(self, nameList, module, enviroment, number, permanentEnv):
        newEnv = Enviroment(enviroment)
        for instruction in module.instructions.instructions:
            instruction.executeInstruction(newEnv)

        for instruction in module.instructions.instructions:
            if instruction.instruction.id == nameList[number]:
                if (number + 1) == len(nameList):
                    returned = newEnv.getFunction(nameList[number])
                    if returned != None:
                        if instruction.isPublic:
                            #Si el id coincide con la funcion dentro del modulo
                            self.functionCall.newFunction = returned
                            self.functionCall.newEnviroment = newEnv
                            return self.functionCall.executeInstruction(permanentEnv)
                        else:
                            print("Error: La función",nameList[number],"no es pública")
                            return None
                    else:
                        print("Error: El modulo",module.id,"no tiene ninguna función llamada",nameList[number])
                        return None
                else:
                    returned = newEnv.getModule(nameList[number])
                    if returned != None:
                        if instruction.isPublic:
                            return self.saveModuleInstructions(nameList, instruction.instruction, newEnv, number+1, permanentEnv)
                        else:
                            print("Error: El modulo",nameList[number],"no es público")
                            return None
                    else:
                        print("Error: El modulo",module.id,"no tiene ningún modulo llamado",nameList[number])
                        return None
        print("Error: No existe ningún modulo, struct o función con el nombre",nameList[number])
        return None

