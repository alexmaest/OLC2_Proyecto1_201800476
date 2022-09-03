from AST.Abstracts.Expression import Expression
from enum import Enum

class Symbol():
    def __init__(self, typeVar, id, value, typeSingle, mutable, row, column):
        self.typeVar = typeVar
        self.id = id
        self.value = value
        self.typeSingle = typeSingle
        self.mutable = mutable
        self.row = row
        self.column = column