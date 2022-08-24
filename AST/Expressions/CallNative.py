from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

from enum import Enum

class TYPE_NATIVE(Enum):
    #Nativas
    TO_STRING = 0,
    TO_OWNED = 1,
    CLONE = 2,
    LEN = 3,
    CAPACITY = 4,
    REMOVE = 5,
    CONTAINS = 6,
    PUSH = 7,
    INSERT = 8,
    #Creacion de Arrays
    NEW = 9,
    WITH_CAPACITY = 10

class CallNative():
    def __init__(self, exp, type):
        self.exp = exp
        self.type = type

    def executeInstruction(self,enviroment):
        if self.type == 0:
            return Retorno(TYPE_NATIVE.TO_STRING,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 1:
            return Retorno(TYPE_NATIVE.TO_OWNED,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 2:
            return Retorno(TYPE_NATIVE.CLONE,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 3:
            return Retorno(TYPE_NATIVE.LEN,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 4:
            return Retorno(TYPE_NATIVE.CAPACITY,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 5:
            return Retorno(TYPE_NATIVE.REMOVE,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 6:
            return Retorno(TYPE_NATIVE.CONTAINS,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 7:
            return Retorno(TYPE_NATIVE.PUSH,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 8:
            return Retorno(TYPE_NATIVE.INSERT,self.exp,TYPE_DECLARATION.NULL)
        elif self.type == 9:
            return Retorno(TYPE_NATIVE.NEW,self.exp,TYPE_DECLARATION.NULL)
        else:
            return Retorno(TYPE_NATIVE.WITH_CAPACITY,self.exp,TYPE_DECLARATION.NULL)