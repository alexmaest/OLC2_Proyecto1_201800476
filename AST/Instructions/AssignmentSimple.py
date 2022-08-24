from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class AssignmentSimple(Instruccion):

    def __init__(self,mutable,id,type,reference):
        self.mutable = mutable
        self.id = id
        self.type = type
        self.reference = reference
    
    def executeInstruction(self, enviroment):
        typeVar = self.type.executeInstruction(enviroment)
        if typeVar != None:
            if typeVar.typeSingle == TYPE_DECLARATION.VECTOR:
                content = []
                content.append(self.mutable)
                content.append(self.id)
                content.append(self.reference)
                return Retorno(typeVar.typeVar,content,TYPE_DECLARATION.VECTOR)
            elif typeVar.typeSingle == TYPE_DECLARATION.ARRAY:
                content = []
                content.append(self.mutable)
                content.append(self.id)
                content.append(typeVar.value)
                content.append(self.reference)
                return Retorno(typeVar.typeVar,content,TYPE_DECLARATION.ARRAY)
            else:
                content = []
                content.append(self.mutable)
                content.append(self.id)
                content.append(self.reference)
                return Retorno(typeVar.typeVar,content,TYPE_DECLARATION.SIMPLE)