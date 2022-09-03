from AST.Abstracts.Expression import Expression
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class Access():
    def __init__(self, id, row, column):
        self.id = id
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        if self.id == '_': return None
        value = enviroment.getVariable(self.id)
        if(value == None):
            listError.append(Error("Error: La variable "+str(self.id)+" no existe","Local",self.row,self.column,"SEMANTICO"))
            return None
        return Retorno(value.typeVar,value.value,value.typeSingle)