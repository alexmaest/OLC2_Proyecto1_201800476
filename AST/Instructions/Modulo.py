from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Modulo(Instruccion):
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions

    def executeInstruction(self, enviroment):
        #Guardar modulo
        enviroment.saveModule(self.id, self)