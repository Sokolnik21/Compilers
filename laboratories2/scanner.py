import ply.lex as lex

reserved = {
    'if'        : 'IF',
    'else'      : 'ELSE',
    # 'for'       : 'FOR',
    # 'while'     : 'WHILE',
    'break'     : 'BREAK',
    'continue'  : 'CONTINUE',
    'return'    : 'RETURN',
    'eye'       : 'EYE',
    'zeros'     : 'ZEROS',
    'ones'      : 'ONES',
    # 'print'     : 'PRINT'
}

tokens = [
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'LOWEREQUAL', 'GREATERREQUAL', 'NOTEQUAL', 'EQUAL',
    'ID',
    'INTNUM',
    'REALNUM',
    'STRING'
] + list(reserved.values())

literals = "+-*/=<>!()[]{}:',;"

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'

t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

t_LOWEREQUAL    = r'<='
t_GREATERREQUAL = r'>='
t_NOTEQUAL      = r'!='
t_EQUAL         = r'=='

t_ignore = ' \t'

# The order of t_[sth] definitions is important - higher in code higher priority
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_REALNUM(t):
    r'((\d+\.\d*)|(\.\d+))([eE][-+]?\d+)?'
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\'.*?\')|(".*?")'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    print("(%d,%d): illegal character '%s'"
        %(t.lineno, find_column(lexer.lexdata, token), t.value[0]) )
    t.lexer.skip(1)

lexer = lex.lex()
