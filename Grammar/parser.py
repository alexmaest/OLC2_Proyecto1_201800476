from argparse import ArgumentDefaultsHelpFormatter
from AST.Abstracts.Retorno import TYPE_DECLARATION, Retorno
from AST.Expressions.CallFunction import CallFunction
from AST.Expressions.Literal import Literal
from AST.Expressions.Access import Access
from AST.Expressions.AccessArray import AccessArray
from AST.Expressions.NewArray import NewArray
from AST.Expressions.NewDefaultArray import NewDefaultArray
from AST.Expressions.Arithmetic import Arithmetic, TYPE_OPERATION
from AST.Expressions.Relational import TYPE_RELATIONAL, Relational
from AST.Expressions.Logic import TYPE_LOGICAL, Logic
from AST.Instructions.Assignment import Assignment
from AST.Instructions.AssignmentSimple import AssignmentSimple
from AST.Instructions.AssignmentSimpleArray import AssignmentSimpleArray
from AST.Instructions.Declaration import Declaration
from AST.Instructions.DeclarationSingle import DeclarationSingle
from AST.Instructions.ListArraySimple import ListArraySimple
from AST.Instructions.ListArrayMultiple import ListArrayMultiple
from AST.Instructions.Statement import Statement
from AST.Instructions.Function import Function
from AST.Instructions.Print import Print
from AST.Instructions.If import If
from AST.Instructions.Match import Match
from AST.Instructions.Arm import Arm
from AST.Instructions.Loop import Loop
from AST.Instructions.While import While
from AST.Instructions.Break import Break
from AST.Instructions.Continue import Continue
from AST.Instructions.Return import Return
from AST.Symbol.Enviroment import Enviroment
from AST.Symbol.Symbol import Symbol
from Grammar.lexer import tokens

# Parsing precedence rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'AD'), 
    ('left', 'DIF', 'IGUALI', 'MENORI', 'MAYORI', 'MENOR', 'MAYOR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('nonassoc', 'RPAR' , 'LPAR'),
    ('right', 'UMENOS')
)

def p_init(t):
    'init : instrucciones_g'
    t[0] = t[1]

def p_instrucciones_g(t):
    '''instrucciones_g : instrucciones_g instruccion_g
    | instruccion_g'''
    if t.slice[1].type == 'instrucciones_g':
        t[1].append(t[2])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_instruccion(t):
    'instruccion_g : funcion'
    t[0] = t[1]

def p_instrucciones_l(t):
    '''instrucciones_l : instrucciones_l instruccion_l
    | instruccion_l'''
    if t.slice[1].type == 'instrucciones_l':
        t[1].append(t[2])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_instruccion_l(t):
    '''instruccion_l : print PCOMA
    | declaracion PCOMA
    | asignacion PCOMA
    | llamada PCOMA
    | sentencia
    | transferencia PCOMA
    '''
    t[0] = t[1]

def p_funcion(t):
    '''
    funcion : FN ID LPAR lista_parametros RPAR ARROW tipo_var statement
    | FN ID LPAR lista_parametros RPAR statement
    | FN ID LPAR RPAR ARROW tipo_var statement
    | FN ID LPAR RPAR statement
    '''
    if t.slice[4].type == 'lista_parametros':
        if t.slice[3].type == 'ARROW': t[0] = Function(t[2],t[4],t[7],t[8])
        else: t[0] = Function(t[2],t[4],None,t[6])
    else:
        if t.slice[5].type == 'ARROW': t[0] = Function(t[2],[],t[6],t[7])
        else: t[0] = Function(t[2],[],None,t[5])

def p_sentencia(t):
    '''sentencia : if
    | match
    | loop
    | while'''
    t[0] = t[1]

def p_if(t):
    'if : IF exp statement else'
    t[0] = If(t[2],t[3],t[4])

def p_else(t):
    #| #epsilon
    '''else : ELSE statement
    | ELSE if'''
    if t.slice[1].type == 'ELSE': t[0] = t[2]

def p_match(t):
    'match : MATCH exp match_statement'
    t[0] = Match(t[2],t[3])

def p_match_statement(t):
    '''match_statement : LLLAV lista_brazos RLLAV
    | LLLAV RLLAV'''
    if t.slice[2].type == 'RLLAV': t[0] = Statement([])
    else: t[0] = Statement(t[2])

def p_lista_brazos(t):
    '''lista_brazos : lista_brazos brazo
    | brazo'''
    if t.slice[1].type == 'lista_brazos':
        t[1].append(t[2])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_brazo(t):
    '''brazo : lista_exp_brazos ARROW2 instruccion_match COMA
    | lista_exp_brazos ARROW2 statement COMA
    | lista_exp_brazos ARROW2 statement'''
    t[0] = Arm(t[1],t[3])

def p_lista_exp_brazos(t):
    '''lista_exp_brazos : lista_exp_brazos ORSINGLE exp
    | exp'''
    if t.slice[1].type == 'lista_exp_brazos':
        t[1].append(t[3])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_instruction_match(t):
    '''instruccion_match : print
    | llamada
    | sentencia
    | transferencia'''
    t[0] = t[1]

def p_loop(t):
    'loop : LOOP statement'
    t[0] = Loop(t[2])

def p_while(t):
    'while : WHILE exp statement'
    t[0] = While(t[2],t[3])

def p_transferencia(t):
    '''transferencia : BREAK
    | RETURN
    | RETURN exp
    | CONTINUE'''
    if t.slice[1].type == 'BREAK': t[0] = Break()
    elif t.slice[1].type == 'CONTINUE': t[0] = Continue()
    else:
        print(t.slice[1].type)
        print(len(t.slice))
        if len(t.slice) > 1: t[0] = Return(t[2])
        else: t[0] = Return(None)

def p_statement(t):
    '''statement : LLLAV instrucciones_l RLLAV
    | LLLAV RLLAV'''
    if t.slice[2].type == 'RLLAV': t[0] = Statement([])
    else: t[0] = Statement(t[2])

def p_lista_parametros(t):
    '''lista_parametros : lista_parametros COMA asignacion_simple
    | asignacion_simple'''
    if t.slice[1].type == 'lista_parametros':
        t[1].append(t[3])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_declaracion(t):
    '''declaracion : LET asignacion_simple IGUAL exp
    | LET MUT asignacion
    | LET asignacion'''
    if t.slice[2].type == 'asignacion_simple': t[0] = DeclarationSingle(t[2],t[4])
    elif t.slice[2].type == 'MUT': t[0] = Declaration(True,t[3])
    else: t[0] = Declaration(False,t[2])

def p_asignacion(t):
    #| lista_att IGUAL exp
    '''asignacion : ID IGUAL exp
    | ID lista_arr IGUAL exp'''
    if t.slice[2].type == 'IGUAL': t[0] = Assignment(Access(t[1]),t[3])
    else: pass

def p_lista_arr(t):
    ''' lista_arr : lista_arr LCOR exp RCOR
    | LCOR exp RCOR'''
    if t.slice[1].type == 'lista_arr': 
        t[1].append(ListArrayMultiple(t[3]))
        t[0] = t[1]
    else: t[0] = [ListArrayMultiple(t[2])]

def p_lista_exp(t):
    '''lista_exp : lista_exp COMA exp
    | exp'''
    if t.slice[1].type == 'lista_exp':
        t[1].append(t[3])
        t[0] = t[1]
    else: t[0] = [t[1]]

def p_asignacion_simple(t):
    #| ID DPUNTOS aMUT LCOR tipo_var RCOR
    '''asignacion_simple : ID DPUNTOS tipo_var
    | ID DPUNTOS lista_arr2
    | MUT ID DPUNTOS tipo_var
    | MUT ID DPUNTOS lista_arr2'''
    if t.slice[1].type == 'ID' :
        if t.slice[3].type == 'tipo_var' : t[0] = AssignmentSimple(False,t[1],t[3])
        else: t[0] = AssignmentSimpleArray(False,t[1],t[3])
    else: 
        if t.slice[4].type == 'tipo_var' : t[0] = AssignmentSimple(True,t[2],t[4])
        else: t[0] = AssignmentSimpleArray(True,t[2],t[4])

def p_lista_arr2(t):
    '''lista_arr2 : LCOR lista_arr2 PCOMA exp RCOR
    | LCOR tipo_var PCOMA exp RCOR'''
    if t.slice[2].type == 'tipo_var': t[0] = ListArraySimple(t[2],t[4])
    else: t[0] = ListArraySimple(t[2],t[4])

def p_exp(t):
    '''exp : valores
    | LPAR valores LPAR
    | expmath
    | explog
    | exprel
    | exparr
    | ID'''
    if t.slice[1].type == 'valores': t[0] = t[1]
    elif t.slice[1].type == 'LPAR': t[0] = t[2]
    elif t.slice[1].type == 'expmath': t[0] = t[1]
    elif t.slice[1].type == 'explog': t[0] = t[1]
    elif t.slice[1].type == 'exprel': t[0] = t[1]
    elif t.slice[1].type == 'exparr': t[0] = t[1]
    elif t.slice[1].type == 'ID': t[0] = Access(t[1])

def p_expmath(t):
    """expmath : exp MAS exp
    | exp MENOS exp
    | exp MULTIPLICACION exp
    | exp DIVISION exp
    | MENOS exp %prec UMENOS"""
    if t.slice[1].type == 'MENOS': t[0] = Arithmetic(t[2], TYPE_OPERATION.RESTA, None, True)
    else:
        if t.slice[2].type == 'MAS': t[0] = Arithmetic(t[1], TYPE_OPERATION.SUMA, t[3], False)
        elif t.slice[2].type == 'MENOS': t[0] = Arithmetic(t[1], TYPE_OPERATION.RESTA, t[3], False)
        elif t.slice[2].type == 'MULTIPLICACION': t[0] = Arithmetic(t[1], TYPE_OPERATION.MULTIPLICACION, t[3], False)
        else: t[0] = Arithmetic(t[1], TYPE_OPERATION.DIVISION, t[3], False)

def p_explog(t):
    '''explog : exp AND exp
    | exp OR exp
    | AD exp'''
    if t.slice[1].type == 'AD': Logic(t[1], TYPE_LOGICAL.NOT, Literal(False,TYPE_DECLARATION.BOOLEAN))
    else:
        if t.slice[2].type == 'AND': t[0] = Logic(t[1], TYPE_LOGICAL.AND, t[3])
        else: t[0] = Logic(t[1], TYPE_LOGICAL.OR, t[3])

def p_exprel(t):
    '''exprel : exp IGUALI exp
    | exp DIF exp
    | exp MAYOR exp
    | exp MENOR exp
    | exp MAYORI exp
    | exp MENORI exp'''
    if t.slice[2].type == 'IGUALI': t[0] = Relational(t[1],TYPE_RELATIONAL.IGUALI,t[3])
    elif t.slice[2].type == 'DIF': t[0] = Relational(t[1],TYPE_RELATIONAL.DIF,t[3])
    elif t.slice[2].type == 'MAYOR': t[0] = Relational(t[1],TYPE_RELATIONAL.MAYOR,t[3])
    elif t.slice[2].type == 'MENOR': t[0] = Relational(t[1],TYPE_RELATIONAL.MENOR,t[3])
    elif t.slice[2].type == 'MAYORI': t[0] = Relational(t[1],TYPE_RELATIONAL.MAYORI,t[3])
    else: t[0] = Relational(t[1],TYPE_RELATIONAL.MENORI,t[3])

def p_exparr(t):
    '''exparr : ID lista_arr
    | LCOR lista_exp RCOR
    | LCOR exp PCOMA exp RCOR
    '''
    if t.slice[1].type == 'ID': t[0] = AccessArray(t[1],t[2])
    else:
        if t.slice[2].type == 'lista_exp': t[0] = NewArray(t[2])
        else: t[0] = NewDefaultArray(t[2],t[4])

def p_valores(t):
    '''valores : ENTERO
    | DECIMAL
    | CADENA
    | BOOLEANO'''
    if t.slice[1].type == 'ENTERO': t[0] = Literal(t[1],0)
    elif t.slice[1].type == 'DECIMAL': t[0] = Literal(t[1],1)
    elif t.slice[1].type == 'CADENA': t[0] = Literal(t[1],2)
    elif t.slice[1].type == 'BOOLEANO': t[0] = Literal(t[1],4)

def p_tipo_var(t):
#   | 'Vec' '<' LISTA_CLASS '>'
    '''
    tipo_var : I64
    | F64
    | BOOL
    | CHAR
    | aSTR
    | STRING
    | USIZE
    | ID
    '''
    if t.slice[1].type == 'I64' : t[0] = Literal(None,0)
    elif t.slice[1].type == 'F64' : t[0] = Literal(None,1)
    elif t.slice[1].type == 'STRING' : t[0] = Literal(None,2)
    elif t.slice[1].type == 'aSTR' : t[0] = Literal(None,3)
    elif t.slice[1].type == 'BOOL' : t[0] = Literal(None,4)
    elif t.slice[1].type == 'CHAR' : t[0] = Literal(None,5)
    elif t.slice[1].type == 'USIZE' : t[0] = Literal(None,6)
    else: t[0] = Access(t[1])

def p_llamada(t):
    '''llamada : ID LPAR RPAR
    | ID LPAR lista_exp RPAR'''
    if t.slice[3].type == 'RPAR': t[0] = CallFunction(t[1],[])
    else: t[0] = CallFunction(t[1],t[3])

def p_print(t):
    'print : PRINT AD LPAR exp RPAR'
    t[0] = Print(t[4])

def p_error(t):
    print(t)
    print("Syntax error at: ", t.value)

import Grammar.ply.yacc as yacc
parser = yacc.yacc()

def startParser(text):
    content = parser.parse(text)
    if text != '':
        globalEnv = Enviroment(None)
        for instruction in content:
            if isinstance(instruction, Function):
                instruction.executeInstruction(globalEnv)
        founded = globalEnv.getFunction('Main')
        if founded != None:
            founded.statement.executeInstruction(globalEnv)
        else:
            print("Error: No fué encontrada una función main")
            #except:
            #    print("Error: La instrucción no se puede ejecutar de forma global")