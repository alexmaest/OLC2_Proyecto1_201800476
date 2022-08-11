from enum import Enum

class TYPE_DECLARATION(Enum):
    #Tipos de variables
    INTEGER = 0,
    FLOAT = 1,
    STRING = 2,
    aSTRING = 3,
    BOOLEAN = 4,
    CHAR = 5,
    UZISE = 6,
    #Tipos de 'dimensiones' de variables
    SIMPLE = 7,
    ARRAY = 8,
    VECTOR = 9,
    STRUCT = 10
    NULL = 11

class Retorno():
    def __init__(self, typeVar, value, typeSingle):
        self.typeVar = typeVar
        self.value = value
        self.typeSingle = typeSingle