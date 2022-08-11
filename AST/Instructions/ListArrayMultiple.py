from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class ListArrayMultiple(Instruccion):

    def __init__(self, expression):
        self.expression = expression