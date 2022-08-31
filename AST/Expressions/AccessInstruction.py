from AST.Abstracts.Expression import Expression
from AST.Instructions.Modulo import Modulo
from AST.Instructions.Struct import Struct
from AST.Instructions.Function import Function
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AccessInstruction():
    def __init__(self, idList):
        self.idList = idList

    def executeInstruction(self, enviroment):
        if len(self.idList) == 1:
            if self.idList == '_': return None
            value = enviroment.getStruct(self.idList[0])
            if(value == None):
                print("Error: El struct",self.idList[0],"no existe")
                return None
            else:
                return Retorno(self.idList[0],value.attributes,TYPE_DECLARATION.STRUCT)
        else:
            value = enviroment.getModule(self.idList[0])
            if(value == None):
                print("Error: El módulo",self.idList[0],"no existe")
                return None
            else:
                return self.searchInstruction(value.instructions.instructions, 1)

    def searchInstruction(self, insList, number):
        for single in insList:
            if single.instruction.id == self.idList[number]:
                if single.isPublic:
                    if isinstance(single.instruction,Struct):
                        if (number + 1) == len(self.idList):
                            return Retorno(single.instruction.id,single.instruction.attributes,TYPE_DECLARATION.STRUCT)
                        else:
                            print("Error: No se puede acceder a un atributo de un struct para devolver un tipo de dato")
                            return None
                    elif isinstance(single.instruction,Modulo):
                        if (number + 1) == len(self.idList):
                            print("Error: Un modulo no es un tipo de dato, debe de acceder a uno de sus atributos que sean structs")
                            return None
                        else:
                            return self.searchInstruction(single.instruction.instructions.instructions, number+1)
                    else:
                        #Función
                        print("Error: No se puede acceder a una función de un struct para devolver un tipo de dato")
                        return None
                else:
                    print("Error: El atributo",self.idList[number],"de la instrucción",self.idList[number-1],"no es público")
                    return None
            else: continue
        print("Error: El modulo",self.idList[number-1],"no tiene ningún modulo, struct o función con el nombre",self.idList[number])
        return None
