from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import TYPE_DECLARATION

class Print(Instruccion):
    def __init__(self, expression):
        self.expression = expression
        self.text = ""

    def executeInstruction(self, enviroment):
        value = self.expression.executeInstruction(enviroment)
        if value != None:
            if value.typeSingle == TYPE_DECLARATION.ARRAY or value.typeSingle == TYPE_DECLARATION.VECTOR:
                self.printArray(value.value)
                print(self.text)
            else:print(value.value)
        else:
            print("Error: No se pudo ejecutar la instrucción print")

    def printArray(self, array):
        self.text += "["
        for i in range(len(array)):
            if isinstance(array[i].value,list):
                if (i+1) == len(array):
                    self.printArray(array[i].value)
                else:
                    self.printArray(array[i].value)
                    self.text += ","
            else:
                if (i+1) == len(array):
                    self.text += str(array[i].value)
                else: self.text += str(array[i].value) + ", "
        self.text += "]"