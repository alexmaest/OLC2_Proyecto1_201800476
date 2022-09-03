from AST.Abstracts.Instruccion import Instruccion
from AST.Symbol.Enviroment import Enviroment

class Statement(Instruccion):
    def __init__(self, instructions):
        self.instructions = instructions
        self.newEnv = None

    def executeInstruction(self, enviroment):
        self.newEnv = Enviroment(enviroment,enviroment.console)
        for line in self.instructions:
            instruction = line.executeInstruction(self.newEnv)
            if instruction != None:
                return instruction