from AST.Abstracts.Instruccion import Instruccion

class Function(Instruccion):
    def __init__(self, id, parameters, type, statement):
        self.id = id
        self.parameters = parameters
        self.type = type
        self.statement = statement

    def executeInstruction(self, enviroment):
        #Guardar función
        enviroment.saveFunction(self.id, self)