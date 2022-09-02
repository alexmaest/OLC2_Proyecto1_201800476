from AST.Abstracts.Instruccion import Instruccion
from AST.Expressions.AttAccess import AttAccess
from AST.Abstracts.Retorno import Retorno, TYPE_DECLARATION

class Match(Instruccion):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def executeInstruction(self, enviroment):
        singleExp = self.expression.executeInstruction(enviroment)
        if singleExp != None:
            #Validación si se encuentra el caso '_'
            founded = False
            for arm in self.statement.instructions:
                armExps = arm.getExpressions()
                for singleArmExp in armExps:
                    if isinstance(singleArmExp,AttAccess):
                        if singleArmExp.expList[0].id.id == '_' and self.statement.instructions[-1] == arm:
                            founded = True
                    
            if founded:
                executed = False
                for arm in self.statement.instructions:
                    armExps = arm.getExpressions()
                    for singleArmExp in armExps:
                        if isinstance(singleArmExp,AttAccess):
                            if singleArmExp.expList[0].id.id  == '_':
                                if not executed:
                                    return arm.executeInstruction(enviroment)
                            else:
                                returned = singleArmExp.executeInstruction(enviroment)
                                if returned != None:
                                    if singleExp.typeVar == returned.typeVar:
                                        if singleExp.typeSingle == returned.typeSingle:
                                            print(singleExp.value,"=?",returned.value)
                                            if singleExp.value == returned.value:
                                                executed = True
                                                return arm.executeInstruction(enviroment)
                                            else: continue
                                        else:
                                            print("Error: El valor que desea comparar no posee las dimensiones correctas")
                                            break
                                    else:
                                        print("Error: El valor que desea comparar no posee el tipo correcto")
                                        break
                                else:
                                    print("Error: El valor del brazo es nulo")
                                    break
                        else:
                            returned = singleArmExp.executeInstruction(enviroment)
                            if returned != None:
                                if singleExp.typeVar == returned.typeVar:
                                    if singleExp.typeSingle == returned.typeSingle:
                                        if singleExp.value == returned.value:
                                            executed = True
                                            return arm.executeInstruction(enviroment)
                                        else: continue
                                    else:
                                        print("Error: El valor que desea comparar no posee las dimensiones correctas")
                                        break
                                else:
                                    print("Error: El valor que desea comparar no posee el tipo correcto")
                                    break
                            else:
                                print("Error: El valor del brazo es nulo")
                                break
            else:
                print("Error: El brazo '_' debe de ser el último de la sentencia match")
        else:
            print("Error: No se ha podido ejecutar la sentencia match porque su valor a comparar es nulo")