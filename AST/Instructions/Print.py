from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError
import tkinter
import re

class Print(Instruccion):
    def __init__(self, expList, row, column):
        self.expList = expList
        self.row = row
        self.column = column
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
                                            listError.append(Error("Error: Ha ingresado un valor que no es simple en \'{ }\' de la instrucción print","Local",self.row,self.column,"SEMANTICO"))
                                            break
                                    else:
                                        if returnedSingle.typeSingle == TYPE_DECLARATION.ARRAY:
                                            self.printArray(returnedSingle.value)
                                            finalResult = re.sub('\{\:\?\}',self.text, finalResult, 1)
                                        elif returnedSingle.typeSingle == TYPE_DECLARATION.VECTOR:
                                            self.printArray(returnedSingle.value[1])
                                            finalResult = re.sub('\{\:\?\}',self.text, finalResult, 1)
                                        elif returnedSingle.typeSingle == TYPE_DECLARATION.STRUCT:
                                            listError.append(Error("Error: No puede imprimir un struct, únicamente sus atributos","Local",self.row,self.column,"SEMANTICO"))
                                            break
                                        else:
                                            listError.append(Error("Error: Ha ingresado un valor simple en \'{:?}\' de la instrucción print","Local",self.row,self.column,"SEMANTICO"))
                                            break
                                else:
                                    listError.append(Error("Error: Una de las expresiones que ha ingresado en println es nula","Local",self.row,self.column,"SEMANTICO"))
                                    break
                            enviroment.console.insert(tkinter.END,finalResult+"\n")
                        else:
                            listError.append(Error("Error: No ha ingresado el número de expresiones correctas en función de los \'{ }\' que ha escrito","Local",self.row,self.column,"SEMANTICO"))
                    else:
                        listError.append(Error("Error: Solo se puede imprimir una cadena como primera instrucctión de un println","Local",self.row,self.column,"SEMANTICO"))
                else:
                    listError.append(Error("Error: Solo se puede imprimir una cadena como primera instrucctión de un println","Local",self.row,self.column,"SEMANTICO"))
            else:
                listError.append(Error("Error: No se pudo ejecutar la instrucción println","Local",self.row,self.column,"SEMANTICO"))
        else:
            value = self.expList[0].executeInstruction(enviroment)
            if value != None:
                if value.typeSingle == TYPE_DECLARATION.SIMPLE:
                    if value.typeVar == TYPE_DECLARATION.STRING or value.typeVar == TYPE_DECLARATION.aSTRING:
                        enviroment.console.insert(tkinter.END,value.value+"\n")
                    else:
                        listError.append(Error("Error: La instrucción println necesita \'{ }\' para imprimir literales que no sean cadenas","Local",self.row,self.column,"SEMANTICO"))
                else:
                    listError.append(Error("Error: La instrucción println necesita \'{:?}\' para imprimir arrays o vectores","Local",self.row,self.column,"SEMANTICO"))
            else:
                listError.append(Error("Error: No se pudo ejecutar la instrucción println","Local",self.row,self.column,"SEMANTICO"))

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
