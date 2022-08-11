from abc import ABC, abstractmethod

class Instruccion(ABC):

    @abstractmethod
    def executeInstruction(self, enviroment):
        pass