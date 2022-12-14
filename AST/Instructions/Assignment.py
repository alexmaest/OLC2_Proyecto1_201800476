from AST.Abstracts.Instruccion import Instruccion
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION
from AST.Expressions.Arithmetic import TYPE_OPERATION
from AST.Instructions.AssignmentAccessArray import AssignmentAccessArray
from AST.Error.Error import Error
from AST.Error.ErrorList import listError

class Assignment(Instruccion):

    def __init__(self,idList,expression, row, column):
        self.idList = idList
        self.expression = expression
        self.row = row
        self.column = column
    
    def executeInstruction(self, enviroment):
        exp = self.expression.executeInstruction(enviroment)
        if exp != None:
            exist = enviroment.getVariable(self.idList[0].id.id)
            if exist != None:
                if exist.mutable:
                    singleId = self.idList[0].id.executeInstruction(enviroment)
                    if len(self.idList) == 1:
                        #Se buscan Variables que sean normales, arrays, vectores y structs
                        if exp.typeVar == None and exp.typeSingle == TYPE_DECLARATION.VECTOR:
                            if singleId.typeSingle == TYPE_DECLARATION.VECTOR:
                                enviroment.editVariable(self.idList[0].id.id, exp.value)
                            else: 
                                listError.append(Error("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable","Local",self.row,self.column,"SEMANTICO"))
                        else:
                            if singleId.typeSingle == exp.typeSingle:

                                if singleId.typeVar == exp.typeVar:
                                        enviroment.editVariable(self.idList[0].id.id, exp.value)
                                elif singleId.typeVar == TYPE_DECLARATION.INTEGER and exp.typeVar == TYPE_DECLARATION.USIZE:
                                        enviroment.editVariable(self.idList[0].id.id, exp.value)
                                elif singleId.typeVar == TYPE_DECLARATION.USIZE and exp.typeVar == TYPE_DECLARATION.INTEGER:
                                        enviroment.editVariable(self.idList[0].id.id, exp.value)
                                else: 
                                    listError.append(Error("Error: No se puede asignar un valor "+str(exp.typeVar)+" a una variable tipo "+str(singleId.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                            else: 
                                listError.append(Error("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable","Local",self.row,self.column,"SEMANTICO"))

                    else:
                        #Se buscan atributos de structs
                        if exist.typeSingle == TYPE_DECLARATION.STRUCT:
                            founded = self.foundAttribute(exist, self.idList, 1)
                            if founded != None:
                                if founded.typeVar == exp.typeVar:
                                    if founded.typeSingle == exp.typeSingle:
                                        newValue = []
                                        newValue.append(founded.value[0])
                                        newValue.append(exp.value)
                                        founded.value = newValue
                                    else: 
                                        listError.append(Error("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable","Local",self.row,self.column,"SEMANTICO"))
                                else: 
                                    listError.append(Error("Error: No se puede asignar un valor "+str(exp.typeVar)+" a un atributo tipo "+str(founded.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                        elif isinstance(self.idList[0],AssignmentAccessArray):
                            founded = self.foundAttribute(exist, self.idList, 1)
                            if founded != None:
                                if founded.typeVar == exp.typeVar:
                                    if founded.typeSingle == exp.typeSingle:
                                        newValue = []
                                        newValue.append(founded.value[0])
                                        newValue.append(exp.value)
                                        founded.value = newValue
                                    else: 
                                        listError.append(Error("Error: No se puede asignar un valor de diferentes dimensiones a las de la variable","Local",self.row,self.column,"SEMANTICO"))
                                else: 
                                    listError.append(Error("Error: No se puede asignar un valor "+str(exp.typeVar)+" a un atributo tipo "+str(founded.typeVar),"Local",self.row,self.column,"SEMANTICO"))
                        else:
                            listError.append(Error("Error: La variable "+str(self.idList[0].id.id)+" no es un struct para que acceda a sus atributos","Local",self.row,self.column,"SEMANTICO"))
                else:
                    listError.append(Error("Error: La variable no es mutable","Local",self.row,self.column,"SEMANTICO"))
            else:
                listError.append(Error("Error: La variable a??n no ha sido declarada","Local",self.row,self.column,"SEMANTICO"))

    def foundAttribute(self, variable, list, number):
        if list[number].id in variable.value:
            if (number + 1) == len(list):
                return variable.value[list[number].id]
            else:
                return self.foundAttribute(variable.value[list[number].id], list, number+1)
        else:
            listError.append(Error("Error: Atributo "+str(list[number].id)+" no encontrado de la variable "+str(list[0].id.id),"Local",self.row,self.column,"SEMANTICO"))
            return None
