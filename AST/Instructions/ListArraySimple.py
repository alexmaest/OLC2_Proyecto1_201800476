from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class ListArraySimple(Instruccion):

    allParameters = []

    def __init__(self, parameters, expression):
        self.parameters = parameters
        self.expression = expression

    def executeInstruction(self, enviroment):
        #Tamaño = exp
        exp = self.expression.executeInstruction(enviroment)
        if isinstance(self.parameters,ListArraySimple):
            #Creacion de array de multiples dimensiones con tamaño limite
            self.createArrays(self.parameters)
            #Tipo integer provicional
            return Retorno(TYPE_DECLARATION.INTEGER,self.allParameters,TYPE_DECLARATION.ARRAY)
        else:
            typeVar = self.parameters.executeInstruction(enviroment)
            #Creacion de array de una dimensión con tamaño limite
            return Retorno(typeVar.typeVar,[],TYPE_DECLARATION.ARRAY)

    def createArrays(parameter):
        pass