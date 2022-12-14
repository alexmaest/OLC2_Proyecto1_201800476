from enum import Enum
from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class TYPE_OPERATION(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    MAYOR = 5,
    MENOR = 6,
    MAYORIGUAL = 7,
    MENORIGUAL = 8,
    DIFERENTE = 9,
    IGUALIGUAL = 10,
    AND = 11,
    OR = 12,
    NOT = 13,
    MODULO = 14

class Arithmetic():

    def __init__(self, lExp, type, rExp, single, row, column):
        self.lExp = lExp
        self.type = type
        self.rExp = rExp
        self.single = single
        self.row = row
        self.column = column

    SUMA = [
        [TYPE_DECLARATION.INTEGER, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.USIZE, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.FLOAT, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.STRING, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.USIZE, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.USIZE, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL]
    ]

    OTHER = [
        [TYPE_DECLARATION.INTEGER, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.USIZE, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.FLOAT, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.USIZE, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL],
        [TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL, TYPE_DECLARATION.NULL]
    ]

    def executeInstruction(self, enviroment):
        lReturn = None
        rReturn = None
        singleReturn = None

        if self.single:
            singleReturn = self.lExp.executeInstruction(enviroment)
        else:
            lReturn = self.lExp.executeInstruction(enviroment)
            rReturn = self.rExp.executeInstruction(enviroment)
        if lReturn != None and rReturn != None or singleReturn != None:
            if self.type == TYPE_OPERATION.SUMA:
                typeResult = Arithmetic.SUMA[lReturn.typeVar.value[0]][rReturn.typeVar.value[0]]
                if typeResult == TYPE_DECLARATION.INTEGER or typeResult == TYPE_DECLARATION.USIZE:
                    return Retorno(typeResult, lReturn.value + rReturn.value, TYPE_DECLARATION.SIMPLE)
                elif typeResult == TYPE_DECLARATION.FLOAT:
                    return Retorno(typeResult, lReturn.value + rReturn.value, TYPE_DECLARATION.SIMPLE)
                elif typeResult == TYPE_DECLARATION.STRING:
                    return Retorno(typeResult, str(lReturn.value) + str(rReturn.value), TYPE_DECLARATION.SIMPLE)
                else:
                    listError.append(Error("Error: No se puede operar "+str(lReturn.typeVar)+" con "+str(rReturn.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                    return None

            elif self.type == TYPE_OPERATION.RESTA:
                if self.single:
                    return Retorno(singleReturn.typeVar, singleReturn.value * -1, TYPE_DECLARATION.SIMPLE)
                else:
                    typeResult = Arithmetic.OTHER[lReturn.typeVar.value[0]][rReturn.typeVar.value[0]]
                    if typeResult == TYPE_DECLARATION.INTEGER or typeResult == TYPE_DECLARATION.USIZE:
                        return Retorno(typeResult, lReturn.value - rReturn.value, TYPE_DECLARATION.SIMPLE)
                    elif typeResult == TYPE_DECLARATION.FLOAT:
                        return Retorno(typeResult, lReturn.value - rReturn.value, TYPE_DECLARATION.SIMPLE)
                    else:
                        listError.append(Error("Error: No se puede operar "+str(lReturn.typeVar)+" con "+str(rReturn.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                        return None
            
            elif self.type == TYPE_OPERATION.MULTIPLICACION:
                typeResult = Arithmetic.OTHER[lReturn.typeVar.value[0]][rReturn.typeVar.value[0]]
                if typeResult == TYPE_DECLARATION.INTEGER or typeResult == TYPE_DECLARATION.USIZE:
                    return Retorno(typeResult, lReturn.value * rReturn.value, TYPE_DECLARATION.SIMPLE)
                elif typeResult == TYPE_DECLARATION.FLOAT:
                    return Retorno(typeResult, lReturn.value * rReturn.value, TYPE_DECLARATION.SIMPLE)
                else:
                    listError.append(Error("Error: No se puede operar "+str(lReturn.typeVar)+" con "+str(rReturn.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                    return None
            
            elif self.type == TYPE_OPERATION.DIVISION:
                typeResult = Arithmetic.OTHER[lReturn.typeVar.value[0]][rReturn.typeVar.value[0]]
                if typeResult == TYPE_DECLARATION.INTEGER or typeResult == TYPE_DECLARATION.USIZE:
                    if rReturn.value != 0:
                        return Retorno(typeResult, int(lReturn.value / rReturn.value), TYPE_DECLARATION.SIMPLE)
                    else:
                        listError.append(Error("Error: No se puede dividir entre cero","Local",self.row,self.column,"SEMANTICO"))
                        return None
                elif typeResult == TYPE_DECLARATION.FLOAT:
                    if rReturn.value != 0.0:
                        return Retorno(typeResult, float(lReturn.value / rReturn.value), TYPE_DECLARATION.SIMPLE)
                    else:
                        listError.append(Error("Error: No se puede dividir entre cero","Local",self.row,self.column,"SEMANTICO"))
                        return None
                else:
                    listError.append(Error("Error: No se puede operar "+str(lReturn.typeVar)+" con "+str(rReturn.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                    return None
          
            else:
                #MODULO
                if lReturn.typeVar == TYPE_DECLARATION.INTEGER and rReturn.typeVar == TYPE_DECLARATION.INTEGER:
                    return Retorno(TYPE_DECLARATION.INTEGER, lReturn.value % rReturn.value, TYPE_DECLARATION.SIMPLE)
                elif lReturn.typeVar == TYPE_DECLARATION.FLOAT and rReturn.typeVar == TYPE_DECLARATION.FLOAT:
                    return Retorno(TYPE_DECLARATION.FLOAT, lReturn.value % rReturn.value, TYPE_DECLARATION.SIMPLE)
                else:
                    listError.append(Error(f"Error: No se puede realizar la operaci??n modulo con "+str(lReturn.typeVar)+" y "+str(rReturn.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                    return None
        else:
            return None