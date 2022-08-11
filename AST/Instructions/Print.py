from AST.Abstracts.Instruccion import Instruccion

class Print(Instruccion):
    def __init__(self, expression):
        self.expression = expression

    def executeInstruction(self, enviroment):
        value = self.expression.executeInstruction(enviroment)
        if(value != None):
            print(value.value)
        else:
            print("Error: No se pudo ejecutar la instrucción print")