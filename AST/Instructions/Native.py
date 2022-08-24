from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Symbol.Enviroment import Enviroment
from AST.Expressions.CallNative import CallNative, TYPE_NATIVE

class Native(Instruccion):
    def __init__(self, value, function):
        self.value = value
        self.function = function

    def executeInstruction(self, enviroment):
        returnedValue = self.value.executeInstruction(enviroment)
        function = self.function.executeInstruction(enviroment)
        if returnedValue != None and function != None:
            if function.typeVar == TYPE_NATIVE.TO_STRING:
                if returnedValue.typeSingle == TYPE_DECLARATION.SIMPLE:
                    if returnedValue.typeVar == TYPE_DECLARATION.STRING or returnedValue.typeVar == TYPE_DECLARATION.aSTRING:
                        return Retorno(TYPE_DECLARATION.STRING,returnedValue.value,TYPE_DECLARATION.SIMPLE)
                    else:
                        print("Error: La función to_string() solo funciona con variables tipo String o &str")
                        return Retorno(TYPE_DECLARATION.NULL,None,TYPE_DECLARATION.SIMPLE)
                else:
                    print("Error: La función to_string() solo funciona con variables tipo String o &str, no con arreglos ni vectores")
                    return Retorno(TYPE_DECLARATION.NULL,None,TYPE_DECLARATION.SIMPLE)
            elif function.typeVar == TYPE_NATIVE.TO_OWNED:
                if returnedValue.typeSingle == TYPE_DECLARATION.SIMPLE:
                    if returnedValue.typeVar == TYPE_DECLARATION.STRING or returnedValue.typeVar == TYPE_DECLARATION.aSTRING:
                        return Retorno(TYPE_DECLARATION.STRING,returnedValue.value,TYPE_DECLARATION.SIMPLE)
                    else:
                        print("Error: La función to_owned() solo funciona con variables tipo String o &str")
                        return None
                else:
                    print("Error: La función to_owned() solo funciona con variables tipo String o &str, no con arreglos ni vectores")
                    return None
            elif function.typeVar == TYPE_NATIVE.CLONE:
                return Retorno(returnedValue.typeVar,returnedValue.value,returnedValue.typeSingle)
            elif function.typeVar == TYPE_NATIVE.LEN:
                if returnedValue.typeSingle == TYPE_DECLARATION.VECTOR:
                    return Retorno(TYPE_DECLARATION.INTEGER,len(returnedValue.value),TYPE_DECLARATION.SIMPLE)
                else: 
                    print("Error: La función len() solo funciona con vectores")
                    return None
            elif function.typeVar == TYPE_NATIVE.CAPACITY:pass
            elif function.typeVar == TYPE_NATIVE.REMOVE:
                if returnedValue.typeSingle == TYPE_DECLARATION.VECTOR:
                    indexValue = function.value.executeInstruction(enviroment)
                    if indexValue != None:
                        del returnedValue.value[indexValue.value]
                        return Retorno(returnedValue.typeVar,returnedValue.value,TYPE_DECLARATION.VECTOR)
                    else:
                        print("Error: El indice de la función remove() es nulo")
                        return None
                else: 
                    print("Error: La función remove() solo funciona con vectores")
                    return None
            elif function.typeVar == TYPE_NATIVE.CONTAINS:pass
            elif function.typeVar == TYPE_NATIVE.PUSH:
                if returnedValue.typeSingle == TYPE_DECLARATION.VECTOR:
                    indexValue = function.value.executeInstruction(enviroment)
                    if indexValue != None:
                        if indexValue.typeVar == returnedValue.typeVar:
                            if indexValue.typeSingle == returnedValue.typeSingle:
                                returnedValue.value.append(indexValue)
                                return Retorno(returnedValue.typeVar,returnedValue.value,TYPE_DECLARATION.VECTOR)
                            else:
                                print("Error: El elemento que desea agregar a la lista no posee las mismas dimensiones de los objetos de esta")
                                return None
                        else:
                            print("Error: El elemento que desea agregar a la lista no posee el mismo tipo de esta")
                            return None
                    else:
                        print("Error: El indice de la función push() es nulo")
                        return None
                else: 
                    print("Error: La función push() solo funciona con vectores")
                    return None
            elif function.typeVar == TYPE_NATIVE.INSERT:
                if returnedValue.typeSingle == TYPE_DECLARATION.VECTOR:
                    if len(function.value) == 2:
                        indexValue = function.value[0].executeInstruction(enviroment)
                        valueValue = function.value[1].executeInstruction(enviroment)
                        if indexValue != None and valueValue != None:
                            if valueValue.typeVar == valueValue.typeVar:
                                if valueValue.typeSingle == valueValue.typeSingle:
                                    returnedValue.value.insert(indexValue.value,valueValue)
                                    return Retorno(returnedValue.typeVar,returnedValue.value,TYPE_DECLARATION.VECTOR)
                                else:
                                    print("Error: El elemento que desea agregar a la lista no posee las mismas dimensiones de los objetos de esta")
                                    return None
                            else:
                                print("Error: El elemento que desea agregar a la lista no posee el mismo tipo de esta")
                                return None
                        else:
                            print("Error: Uno o ambos indices de la función insert() son nulos")
                            return None
                    else:
                        print("Error: La función insert() tiene la cantidad de parametros incorrectos")
                        return None
                else: 
                    print("Error: La función insert() solo funciona con vectores")
                    return None
            elif function.typeVar == TYPE_NATIVE.NEW:
                if returnedValue.typeSingle == TYPE_DECLARATION.VECTOR:
                    return Retorno(returnedValue.typeVar,[],TYPE_DECLARATION.VECTOR)
                else: 
                    print("Error: La función ::new() solo funciona con vectores")
                    return None
            else:
                #WITH_CAPACITY
                pass
        else:
            print("Error: No se ha podido ejecutar la función nativa")
            return None