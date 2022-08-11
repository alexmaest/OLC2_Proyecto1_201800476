reserved = {
    'pub' : 'PUB',
    'mod' : 'MOD',
    'mut' : 'MUT',
    '&mut' : 'aMUT',
    'fn' : 'FN',
    'println' : 'PRINT',
    'let' : 'LET',
    'i64' : 'I64',
    'f64' : 'F64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    '&str' : 'aSTR',
    'String' : 'STRING',
    'usize' : 'USIZE',
    'vec' : 'VEC',
}

tokens = [
    'ID','ENTERO','CADENA','DECIMAL',
    'MAS','MENOS','MULTIPLICACION','DIVISION',
    'IGUAL','LCOR','RCOR','LPAR','RPAR','LLLAV','RLLAV','COMA','PCOMA','DPUNTOS','AD','ARROW'
] + list(reserved.values())

t_MAS    = r'\+'
t_MENOS   = r'-'
t_MULTIPLICACION   = r'\*'
t_DIVISION  = r'/'
t_IGUAL  = r'='
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_LLLAV  = r'\{'
t_RLLAV  = r'\}'
t_LCOR  = r'\['
t_RCOR  = r'\]'
t_COMA = r','
t_PCOMA = r';'
t_DPUNTOS = r':'
t_AD = r'!'
t_ARROW = r'[\-][\>]'

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_CADENA(t):
    r'[\"][^\"\n]*[\"]'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        print("Error al reconocer la cadena")
        t.value="Error"
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

import Grammar.ply.lex as lex
lexer = lex.lex()