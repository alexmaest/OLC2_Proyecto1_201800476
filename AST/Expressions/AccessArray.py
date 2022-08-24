from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AccessArray():
    def __init__(self, id, listAccess):
        self.id = id
        self.listAccess = listAccess
        self.dimensions = 0

    def executeInstruction(self,enviroment):
        singleId = self.id.executeInstruction(enviroment)
        if singleId != None:
            if singleId.typeSingle == TYPE_DECLARATION.ARRAY or singleId.typeSingle == TYPE_DECLARATION.VECTOR:
                self.countDimensions(singleId.value)
                if self.dimensions >= len(self.listAccess):
                    return self.returnValue(singleId.value,self.listAccess,0,enviroment)
                else:
                    print("Error: La lista no posee esa cantidad de dimensiones")
                    return None
            else:
                print("Error: La variable no es una lista")
                return None
        else:
            return None

    def returnValue(self, value, position, number, enviroment):
        returned = position[number].executeInstruction(enviroment)
        if returned.typeVar == TYPE_DECLARATION.INTEGER:
            for j in range(len(value)):
                if (position[number].value + 1) <= len(value):
                    if position[number].value == j:
                        if len(position) > (number+1):
                            return self.returnValue(value[j].value,position,number+1,enviroment)
                        else:
                            return value[j]
                else:
                    print("Error: El indice excede el tamaño del arreglo")
                    return None
        else:
            print("Error: El indice no es un entero")
            return None
        '''
        position = [0]
        value = [1]

        position = [1,2,0]
        value = [[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]
        '''
    def getId(self):
        return self.id

    def countDimensions(self,value):
        self.dimensions += 1
        if isinstance(value,list):
            if isinstance(value[0].value,list):
                self.countDimensions(value[0].value)
