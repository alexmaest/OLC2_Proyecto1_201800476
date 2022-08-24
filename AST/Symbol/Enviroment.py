from AST.Symbol.Symbol import Symbol

class Enviroment():

    variables = []
    functions = []

    def __init__(self, previous):
        self.previous = previous
        self.variables = []
        self.functions = []

    def saveVariable(self, variable):
        env = self
        while (env != None):
            for single in env.variables:
                if single.id == variable.id:
                    print("Error: La Variable con id",variable.id,"ya existe")
                    return
            env = env.previous
        self.variables.append(variable)
        print("Información: La Variable con id",variable.id,"fué agregada")

    def editVariable(self, id, value):
        env = self
        while (env != None):
            for single in env.variables:
                if single.id == id:
                    single.value = value
                    break
            env = env.previous

    def saveFunction(self, id, function):
        env = self
        while (env != None):
            for single in env.functions:
                if single.id == id:
                    print("Error: La Función con id",id,"ya existe")
                    return False
            env = env.previous
        self.functions.append(function)
        print("Información: La Función con id",id,"fué agregada")
        return True
    
    def getVariable(self, id):
        env = self
        while(env != None):
            for single in env.variables:
                if single.id == id:
                    return single
            env = env.previous
        return None
    
    def getFunction(self, id):
        env = self
        while(env != None):
            for single in env.functions:
                if single.id == id:
                    return single
            env = env.previous
        return None
    
    def getGlobal(self):
        env = self
        while(env.previous != None):
            env = env.previous
        return env