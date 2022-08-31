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
    CHARS = 9,
    SQRT = 10,
    ABS = 11,
    #Creacion de Arrays
    NEW = 12,
    WITH_CAPACITY = 13

class CallNative():
    def __init__(self, exp, type):
        self.exp = exp
        self.type = type

    def executeInstruction(self,enviroment):
        returnedValue = None
        if self.exp != None:
            returnedValue = self.exp.executeInstruction(enviroment).value

        if self.type == 0:
            return Retorno(TYPE_NATIVE.TO_STRING,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 1:
            return Retorno(TYPE_NATIVE.TO_OWNED,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 2:
            return Retorno(TYPE_NATIVE.CLONE,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 3:
            return Retorno(TYPE_NATIVE.LEN,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 4:
            return Retorno(TYPE_NATIVE.CAPACITY,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 5:
            return Retorno(TYPE_NATIVE.REMOVE,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 6:
            return Retorno(TYPE_NATIVE.CONTAINS,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 7:
            return Retorno(TYPE_NATIVE.PUSH,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 8:
            return Retorno(TYPE_NATIVE.INSERT,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 9:
            return Retorno(TYPE_NATIVE.CHARS,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 10:
            return Retorno(TYPE_NATIVE.SQRT,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 11:
            return Retorno(TYPE_NATIVE.ABS,returnedValue,TYPE_DECLARATION.NULL)
        elif self.type == 12:
            return Retorno(TYPE_NATIVE.NEW,returnedValue,TYPE_DECLARATION.NULL)
        else:
            return Retorno(TYPE_NATIVE.WITH_CAPACITY,returnedValue,TYPE_DECLARATION.NULL)