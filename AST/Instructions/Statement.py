from AST.Abstracts.Instruccion import Instruccion
from AST.Symbol.Enviroment import Enviroment

class Statement(Instruccion):
    def __init__(self, instructions):
        self.instructions = instructions

    def executeInstruction(self, enviroment):
        newEnv = Enviroment(enviroment)
        for line in self.instructions:
            instruction = line.executeInstruction(newEnv)
            if(instruction != None):
                return instruction