from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import TYPE_DECLARATION
import re

class Print(Instruccion):
    def __init__(self, expList):
        self.expList = expList
        self.text = ""

    def executeInstruction(self, enviroment):
        self.text = ""
        if len(self.expList) > 1:
            returned = self.expList[0].executeInstruction(enviroment)
            if returned != None:
                if returned.typeSingle == TYPE_DECLARATION.SIMPLE:
                    if returned.typeVar == TYPE_DECLARATION.aSTRING or returned.typeVar == TYPE_DECLARATION.aSTRING:
                        result = re.findall('\{\}|\{\:\?\}',returned.value)
                        if len(self.expList) - 1 == len(result):
                            finalResult = returned.value
                            for i in range(len(result)):
                                self.text = ""
                                returnedSingle = self.expList[i+1].executeInstruction(enviroment)
                                if returnedSingle != None:
                                    if result[i] == '{}':
                                        if returnedSingle.typeSingle == TYPE_DECLARATION.SIMPLE:
                                            finalResult = re.sub('\{\}',str(returnedSingle.value), finalResult, 1)
                                        else:
                                            print("Error: Ha ingresado un valor que no es simple en \'{ }\' de la instrucción print")
                                            break
                                    else:
                                        if returnedSingle.typeSingle == TYPE_DECLARATION.ARRAY:
                                            self.printArray(returnedSingle.value)
                                            finalResult = re.sub('\{\:\?\}',self.text, finalResult, 1)
                                        elif returnedSingle.typeSingle == TYPE_DECLARATION.VECTOR:
                                            self.printArray(returnedSingle.value[1])
                                            finalResult = re.sub('\{\:\?\}',self.text, finalResult, 1)
                                        elif returnedSingle.typeSingle == TYPE_DECLARATION.STRUCT:
                                            print("Error: No puede imprimir un struct, únicamente sus atributos")
                                            break
                                        else:
                                            print("Error: Ha ingresado un valor simple en \'{:?}\' de la instrucción print")
                                            break
                                else:
                                    print("Error: Una de las expresiones que ha ingresado en println es nula")
                                    break
                            print(finalResult)
                        else:
                            print("Error: No ha ingresado el número de expresiones correctas en función de los \'{ }\' que ha escrito")
                    else:
                        print("Error: Solo se puede imprimir una cadena como primera instrucctión de un println")
                else:
                    print("Error: Solo se puede imprimir una cadena como primera instrucctión de un println")
            else:
                print("Error: No se pudo ejecutar la instrucción println")
        else:
            value = self.expList[0].executeInstruction(enviroment)
            if value != None:
                if value.typeSingle == TYPE_DECLARATION.SIMPLE:
                    if value.typeVar == TYPE_DECLARATION.STRING or value.typeVar == TYPE_DECLARATION.aSTRING:
                        print(value.value)
                    else:
                        print("Error: La instrucción println necesita \'{ }\' para imprimir literales que no sean cadenas")
                else:
                    print("Error: La instrucción println necesita \'{:?}\' para imprimir arrays o vectores")
            else:
                print("Error: No se pudo ejecutar la instrucción println")

    def printArray(self, array):
        self.text += "["
        for i in range(len(array)):
            if isinstance(array[i].value,list):
                if (i+1) == len(array):
                    if array[i].typeSingle == TYPE_DECLARATION.VECTOR:
                        self.printArray(array[i].value[1])
                    else:
                        self.printArray(array[i].value)
                else:
                    if array[i].typeSingle == TYPE_DECLARATION.VECTOR:
                        self.printArray(array[i].value[1])
                        self.text += ","
                    else:
                        self.printArray(array[i].value)
                        self.text += ","
            else:
                if (i+1) == len(array):
                    self.text += str(array[i].value)
                else: self.text += str(array[i].value) + ", "
        self.text += "]"