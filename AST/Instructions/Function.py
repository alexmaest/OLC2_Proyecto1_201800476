from AST.Abstracts.Instruccion import Instruccion

class Function(Instruccion):
    def __init__(self, id, parameters, type, statement, row, column):
        self.id = id
        self.parameters = parameters
        self.type = type
        self.statement = statement
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        #Guardar función
        enviroment.saveFunction(self.id, self)