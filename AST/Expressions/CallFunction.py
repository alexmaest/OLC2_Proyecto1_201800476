from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Instructions.AssignmentSimple import AssignmentSimple
from AST.Instructions.DeclarationSingle import DeclarationSingle

class CallFunction():
    def __init__(self, id, parameters):
        self.id = id
        self.parameters = parameters

    def executeInstruction(self,enviroment):
        #Buscar función
        founded = enviroment.getFunction(self.id)
        if(founded != None):
            #Ejecución de parametros
            if len(self.parameters) == len(founded.parameters):
                count = 0
                for param in founded.parameters:
                    singleParam = DeclarationSingle(param,self.parameters[count])   
                    singleParam.executeInstruction(enviroment)             
                    count+=1

                #Ejecutar instrucciones de la función
                founded.statement.executeInstruction(enviroment)
            else:
                print("Error: El número de parametros que ingresó para la función",self.id,"no son los correctos")
        else:
            print("Error: No se pudo encontrar la función con id", self.id)