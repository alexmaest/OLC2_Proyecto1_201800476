from AST.Expressions.Handler import Handler
from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.Access import Access
from AST.Expressions.ParamReference import ParamReference
from AST.Instructions.DeclarationSingle import DeclarationSingle
from AST.Symbol.Enviroment import Enviroment

class CallStruct():
    def __init__(self, id, parameters):
        self.id = id
        self.parameters = parameters
        self.content = {}

    def executeInstruction(self,enviroment):
        #Buscar struct
        single = self.id.executeInstruction(enviroment)
        self.content = {}
        if(single != None):
            founded = single.value
            if len(self.parameters) == len(founded):
                for param in range(len(self.parameters)):
                    if self.parameters[param].id == founded[param].id:
                        callExp = self.parameters[param].executeInstruction(enviroment)
                        callType = founded[param].executeInstruction(enviroment)
                        if callExp != None and callType != None:
                            if callExp.typeVar == callType.typeVar and callExp.typeSingle == callType.typeSingle:
                                content = []
                                content.append(founded[param].isPublic)
                                content.append(callExp.value)
                                self.content[self.parameters[param].id] = Retorno(callExp.typeVar,content,callExp.typeSingle)
                            else:
                                print("Error: El parámetro no coincide con el tipo de dato declarado en el struct",self.id.idList[0])
                                return None
                        else:
                            print("Error: El parámetro o tipo que ha ingresado en el struct",self.id.idList[0],"es nulo")
                            return None
                    else:
                        print("Error: No coincide el parámetro \'",self.parameters[param].id,"\' para el struct",self.id.idList[0])
                        return None
                return Retorno(self.id.idList[-1],self.content,TYPE_DECLARATION.STRUCT)
            else:
                print("Error: El número de atributos del struct",self.id,"no es el correcto")
                return None