#ok wyrażenia binarne, w tym operacje macierzowe 'element po elemencie'
# wyrażenia relacyjne,
#ok negację unarną,
#ok transpozycję macierzy,
# inicjalizację macierzy konkretnymi wartościami,
# macierzowe funkcje specjalne,
# instrukcję przypisania, w tym różne operatory przypisania
# instrukcję warunkową if-else,
# pętle: while and for,
# instrukcje break, continue oraz return,
#ok instrukcję print,
# instrukcje złożone,
# tablice oraz ich zakresy.

import ply.yacc as yacc
import scanner
import numpy as np

tokens = scanner.tokens

precedence = (
    # ('nonassoc', 'IF', 'FOR', 'WHILE', 'BREAK', 'CONTINUE', 'RETURN', 'EYE', 'ONES', 'PRINT'),
    ('nonassoc', 'IF', 'BREAK', 'CONTINUE', 'RETURN'),
    ('nonassoc', 'IF_ELSE'),
    ('left', ','),
    ('right', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('left', 'EQUAL', 'NOTEQUAL'),
    ('left', '<', '>', 'LOWEREQUAL', 'GREATERREQUAL'),
    ('left', '+', '-', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS', 'UPLUS', 'UEXCLAMATION'),
    ('left', 'UTRANSPOSE'),
    ('nonassoc', 'CIRCLEPARENS'),
)

def p_lines(p):
    ''' lines   : lines expression ';'
                | lines ';'
                | lines '{' lines '}'
                | '''

def p_controlf_flow(p):
    ''' expression  : IF '(' expression ')' f_body ELSE expression %prec IF_ELSE
                    | IF '(' expression ')' expression %prec IF
        f_body      : expression ';' '''
#                     | FOR expression '=' expression ':' expression expression %prec FOR
#                     | WHILE '(' expression ')' expression %prec WHILE '''
    # what's below doesn't work
    # if p[1] == 'if' and p[6] == 'else' :
    #     if p[3] :
    #         p[0] = p[5]
    #     else :
    #         p[0] = p[7]
    # elif p[1] == 'if' :
    #     if p[3] :
    #         p[0] = p[5]
    # elif p[1] == 'while' :
    #     while p[3] :
    #         p[5]

def p_single_statements(p):
    ''' expression  : BREAK
                    | CONTINUE
                    | RETURN expression'''

def p_create_matrix(p):
    ''' expression  : ZEROS '(' expression ')'
                    | ONES '(' expression ')'
                    | EYE '(' expression ')' '''
    # if p[1] == 'zeros' :
    #     p[0] = np.zeros(shape=(p[3], p[3]))
    # elif p[1] == 'ones' :
    #     p[0] = np.ones(shape=(p[3], p[3]))
    # elif p[1] == 'eye' :
    #     p[0] = np.eye(p[3])

# def p_print(p):
#     ''' expression  : PRINT expression '''
    # print(p[2])

def p_binary_additive_multiplicative_operators(p):
    ''' expression  : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression '''
    # if p[2] == '+' :
    #     p[0] = p[1] + p[3]
    # elif p[2] == '-' :
    #     p[0] = p[1] - p[3]
    # elif p[2] == '*' :
    #     p[0] = p[1] * p[3]
    # elif p[2] == '/' :
    #     p[0] = p[1] / p[3]

def p_binary_matrix_operators(p):
    ''' expression  : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression '''
    # if p[2] == '.+' :
    #     p[0] = np.add(p[1], p[3])
    # elif p[2] == '.-' :
    #     p[0] = np.subtract(p[1], p[3])
    # elif p[2] == '.*' :
    #     p[0] = np.multiply(p[1], p[3])
    # elif p[2] == './' :
    #     p[0] = np.divide(p[1], p[3])

def p_binary_assignment_operators(p):
    ''' expression  : expression '=' expression
                    | expression ADDASSIGN expression
                    | expression SUBASSIGN expression
                    | expression MULASSIGN expression
                    | expression DIVASSIGN expression '''
    # if p[2] == '=' :
    #     p[0] = p[3]
    #     p[1] = p[3]
    # elif p[2] == 'ADDASSIGN' :
    #     p[0] = p[1] + p[3]
    #     p[1] = p[1] + p[3]
    # elif p[2] == 'SUBASSIGN' :
    #     p[0] = p[1] - p[3]
    #     p[1] = p[1] - p[3]
    # elif p[2] == 'MULASSIGN' :
    #     p[0] = p[1] * p[3]
    #     p[1] = p[1] * p[3]
    # elif p[2] == 'DIVASSIGN' :
    #     p[0] = p[1] / p[3]
    #     p[1] = p[1] / p[3]

def p_binary_relational_operators(p):
    ''' expression  : expression '<' expression
                    | expression '>' expression
                    | expression LOWEREQUAL expression
                    | expression GREATERREQUAL expression
                    | expression NOTEQUAL expression
                    | expression EQUAL expression '''
    # if p[2] == '<' :
    #     p[0] = p[1] < p[3]
    # elif p[2] == '>' :
    #     p[0] = p[1] > p[3]
    # elif p[2] == 'LOWEREQUAL' :
    #     p[0] = p[1] <= p[3]
    # elif p[2] == 'GREATERREQUAL' :
    #     p[0] = p[1] >= p[3]
    # elif p[2] == 'NOTEQUAL' :
    #     p[0] = p[1] != p[3]
    # elif p[2] == 'EQUAL' :
    #     p[0] = p[1] == p[3]

def p_list_operators(p):
    ''' expression  : expression ',' expression '''
    # if p[2] == ',' :
    #     if(type(p[1]) is list):
    #         p[0] = p[1] + [p[3]]
    #     else:
    #         p[0] = [p[1]] + [p[3]]

def p_unary_prefix_operators(p):
    ''' expression  : '-' expression %prec UMINUS
                    | '+' expression %prec UPLUS
                    | '!' expression %prec UEXCLAMATION '''
    # if p[1] == '-' :
    #     p[0] = -p[2]
    # elif p[1] == '+' :
    #     p[0] = p[2]
    # elif p[1] == '!' :
    #     p[0] = not p[2]

def p_unary_postfix_operators(p):
    ''' expression  : expression '\\'' %prec UTRANSPOSE '''
    # if p[2] == '\'' :
    #     p[0] = np.transpose(p[1])

def p_circle_parens(p):
    ''' expression  : '(' expression ')' %prec CIRCLEPARENS
                    | '[' expression ']' %prec CIRCLEPARENS'''
    # p[0] = p[2]

def p_operand(p):
    ''' expression  : ID
                    | INTNUM
                    | REALNUM
                    | STRING '''
    # p[0] = p[1]

def p_error(p):
    print("Syntax error in line %d" % p.lineno)

parser = yacc.yacc()
