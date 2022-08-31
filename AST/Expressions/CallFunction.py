from AST.Expressions.Handler import Handler
from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.Access import Access
from AST.Expressions.ParamReference import ParamReference
from AST.Instructions.DeclarationSingle import DeclarationSingle
from AST.Symbol.Enviroment import Enviroment

class CallFunction():
    def __init__(self, id, parameters):
        self.id = id
        self.parameters = parameters
        self.newEnviroment = None 
        self.newFunction = None
        self.positions = []

    def executeInstruction(self,enviroment):
        #Buscar función
        self.positions = []
        Fail = False
        founded = None
        newEnv = None
        if self.newEnviroment != None:
            founded = self.newFunction
            newEnv = Enviroment(self.newEnviroment)
        else:
            founded = enviroment.getFunction(self.id)
            newEnv = Enviroment(enviroment.getGlobal())
        if founded != None or self.newEnviroment != None:
            #Ejecución de parametros
            if len(self.parameters) == len(founded.parameters):
                count = 0
                for param in founded.parameters:
                    if isinstance(self.parameters[count], Access) or isinstance(self.parameters[count], ParamReference):
                        exist = None
                        if isinstance(self.parameters[count], Access):
                            exist = enviroment.getVariable(self.parameters[count].id)
                        else:
                            exist = enviroment.getVariable(self.parameters[count].id.id)
                        if exist != None:
                            if exist.mutable == param.mutable:
                                #Validar referencia
                                if not isinstance(self.parameters[count], Access):
                                    if self.parameters[count].reference == param.reference:
                                        if param.reference:
                                            self.positions.append(count)
                                            singleValue = self.parameters[count].executeInstruction(enviroment)
                                            singleParam = DeclarationSingle(param,Handler(singleValue.typeVar,singleValue.value,singleValue.typeSingle))   
                                            singleParam.executeInstruction(newEnv)             
                                            count+=1
                                        else:
                                            singleValue = self.parameters[count].executeInstruction(enviroment)
                                            singleParam = DeclarationSingle(param,Handler(singleValue.typeVar,singleValue.value,singleValue.typeSingle))   
                                            singleParam.executeInstruction(newEnv)             
                                            count+=1
                                    else:
                                        print("Error: Se esperaba una referencia diferente de la variable que ingresó como parametro")
                                        Fail = True
                                        break
                                else:
                                    if not param.reference:
                                        singleValue = self.parameters[count].executeInstruction(enviroment)
                                        singleParam = DeclarationSingle(param,Handler(singleValue.typeVar,singleValue.value,singleValue.typeSingle))   
                                        singleParam.executeInstruction(newEnv)             
                                        count+=1
                                    else:
                                        print("Error: Se esperaba una referencia diferente de la variable que ingresó como parametro")
                                        Fail = True
                                        break
                            else:
                                print("Error: La mutabilidad de la variable que ingresó como parametro es diferente a la declarada")
                                Fail = True
                                break
                        else:
                            print("Error: La variable que ingresó como parametro no existe")
                            Fail = True
                            break
                    else:
                        singleParam = DeclarationSingle(param,self.parameters[count])   
                        singleParam.executeInstruction(newEnv)             
                        count+=1
                
                if not Fail:
                    #Ejecutar instrucciones de la función
                    returnedValue = founded.statement.executeInstruction(newEnv)
                    #Retornar valor si lo tiene
                    if returnedValue != None and founded.type != None:
                        if returnedValue.typeSingle != TYPE_DECLARATION.BREAK and returnedValue.typeSingle != TYPE_DECLARATION.CONTINUE:
                            typeReturned = founded.type.executeInstruction(newEnv)
                            if typeReturned != None:
                                if typeReturned.typeVar == returnedValue.typeVar:
                                    if typeReturned.typeSingle == returnedValue.typeSingle:
                                        return returnedValue
                                    else: print("Error: Está retornando un valor de diferentes dimensiones a las de la función") 
                                else: print("Error: Está retornando un valor que no es del tipo de la función")
                            else: print("Error: La función",founded.id,"no puede retornar un valor porque no tiene un tipo de valor declarado")
                        else: print("Error: Una función no puede retornar una sentencia break sin expresión o continue")
                    elif returnedValue != None and founded.type == None:
                        print("Error: No puede retornar valores en la función",self.id,"tipo void")
                    elif returnedValue == None and founded.type != None:
                        print("Error: Debe de retonar algún valor en esta función")
                    else: pass #ya se validó todo

                #Modificar de regreso las variables que se enviaron con referencia
                    for number in self.positions:
                        returned = founded.statement.newEnv.getVariable(founded.parameters[number].id)
                        if returned != None:
                            if isinstance(self.parameters[number], Access):
                                exist = enviroment.editVariable(self.parameters[number].id, returned.value)
                            else:
                                exist = enviroment.editVariable(self.parameters[number].id.id, returned.value)
            else:
                print("Error: El número de parametros que ingresó para la función",self.id,"no son los correctos")
        else:
            print("Error: No se pudo encontrar la función con id", self.id)