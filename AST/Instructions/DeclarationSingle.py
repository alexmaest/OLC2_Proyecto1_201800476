from AST.Abstracts.Instruccion import Instruccion
from AST.Instructions.ListArraySimple import ListArraySimple
from AST.Symbol.Symbol import Symbol
from AST.Abstracts.Retorno import TYPE_DECLARATION
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class DeclarationSingle(Instruccion):

    def __init__(self, asignation, expression, row, column):
        self.asignation = asignation
        self.expression = expression
        self.newEnv = None
        self.row = row
        self.column = column

    def executeInstruction(self, enviroment):
        content = self.asignation.executeInstruction(enviroment)
        exp = self.expression.executeInstruction(enviroment)
        if self.newEnv != None:
            enviroment = self.newEnv
        if content != None and exp != None:
            if content.typeSingle == TYPE_DECLARATION.SIMPLE or content.typeSingle == TYPE_DECLARATION.VECTOR:
                if exp.typeVar == None and exp.typeSingle == TYPE_DECLARATION.VECTOR:
                    enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                elif content.typeSingle == exp.typeSingle:
                    if exp.typeVar == content.typeVar:
                        enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                    elif self.uSizeValidation(exp.typeVar,content.typeVar):
                        enviroment.saveVariable(Symbol(TYPE_DECLARATION.USIZE,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                    else: listError.append(Error("Error: No se puede asignar un valor"+str(exp.typeVar)+"a una variable tipo"+str(content.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                else: listError.append(Error("Error: Está tratando de asignar un valor de diferentes dimensiones a las que intenta declarar","Local",self.row,self.column,"SEMANTICO"))
            else:
                #Comparar si las dimensiones a asignar son las mismas
                if exp.typeVar == content.typeVar:
                    if exp.typeSingle == TYPE_DECLARATION.ARRAY:
                        if isinstance(self.asignation.type, ListArraySimple):
                            if self.dimensionalCompare(exp.value, content.value[2]):
                                enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                            else: listError.append(Error("Error: Está tratando de asignar una lista de diferentes dimensiones a las que intenta declarar","Local",self.row,self.column,"SEMANTICO"))
                        else:
                            enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                    elif exp.typeSingle == content.typeSingle:
                        enviroment.saveVariable(Symbol(content.typeVar,content.value[1],exp.value,content.typeSingle,content.value[0],self.row,self.column))
                    else: listError.append(Error("Error: No se puede asignar un valor simple a una variable de varias dimensiones","Local",self.row,self.column,"SEMANTICO"))
                else: listError.append(Error("Error: No se puede asignar un valor"+str(exp.typeVar)+"a una variable tipo"+str(content.typeVar),"Local",self.row,self.column,"SEMANTICO"))
        else: listError.append(Error("Error: No se pudo asignar la variable porque su valor es nulo","Local",self.row,self.column,"SEMANTICO"))

    def uSizeValidation(self, assignation, expression):
        if assignation == TYPE_DECLARATION.USIZE and expression == TYPE_DECLARATION.INTEGER:
            return True
        elif assignation == TYPE_DECLARATION.INTEGER and expression == TYPE_DECLARATION.USIZE:
            return True
        else:
            return False

    def dimensionalCompare(self, list1, list2):
        if len(list1) == len(list2):
            if isinstance(list1[0].value,list):
                if isinstance(list2[0],list):
                    return self.dimensionalCompare(list1[0].value,list2[0])
                else:
                    return False
            elif isinstance(list2[0],list):
                if isinstance(list1[0].value,list):
                    return self.dimensionalCompare(list1[0].value,list2[0])
                else:
                    return False
            else:
                return True
        else:
            return False

    '''
        [[1,4],[1,4],[1,4],[1,4],[1,4]]
        [[1,4],4,3,2,1]
    '''