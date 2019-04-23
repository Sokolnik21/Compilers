#!/usr/bin/python

import scanner
import ply.yacc as yacc
import AST as AST

tokens = scanner.tokens

precedence = (
   ('left', 'ONLY_IF'),
   ('left', 'ELSE'),
   ('right', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
   ('left', 'EQUAL', 'NOTEQUAL'),
   ('left', '<', '>', 'LOWEREQUAL', 'GREATERREQUAL'),
   ('left', '+', '-', 'DOTADD', 'DOTSUB'),
   ('left', '*', '/', 'DOTMUL', 'DOTDIV'),
   ('right', 'UMINUS', 'UPLUS', 'UEXCLAMATION'),
   ('left', 'UTRANSPOSE'),
)

###########################
#    Program structure    #
###########################
def p_program(p):
    ''' program             : multi_instructions
                            | '''
    if len(p) == 2:
        p[0] = AST.Program(p[1])
    else:
        p[0] = AST.Program()

def p_multiple_instructions(p):
    ''' multi_instructions  : multi_instructions instruction
                            | instruction '''
    if len(p) == 2:
        p[0] = AST.MultipleInstructions(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        p[0].addInstruction(p[2])


def p_instruction_form(p):
    ''' instruction : '{' multi_instructions '}'
                    | one_line_instruction ';' '''
    if len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]

def p_multiple_expressions(p):
    ''' multi_expressions   : multi_expressions ',' expression
                            | expression '''
    if len(p) == 2:
        p[0] = AST.MultipleExpressions(p[1])
    elif len(p) == 4:
        p[0] = p[1]
        p[0].addExpression(p[3])

###########################
#       Control flow      #
###########################
def p_control_flow(p):
    ''' instruction : IF '(' condition ')' instruction ELSE instruction
                    | IF '(' condition ')' instruction %prec ONLY_IF
                    | FOR variable '=' expression ':' expression instruction
                    | WHILE '(' condition ')' instruction '''
    if len(p) == 8 and p[1] == 'if' and p[6] == 'else':
        p[0] = AST.IfElse(p[3], p[5], p[7])
    elif p[1] == 'if':
        p[0] = AST.IfOnly(p[3], p[5])
    elif p[1] == 'for':
        p[0] = AST.For(p[2], p[4], p[6], p[7])
    elif p[1] == 'while':
        p[0] = AST.While(p[3], p[5])

def p_jumping_statements(p):
    ''' one_line_instruction    : BREAK
                                | CONTINUE
                                | RETURN multi_expressions '''
    if len(p) == 2:
        p[0] = AST.JumpingStatement(p[1])
    elif len(p) == 3:
        p[0] = AST.JumpingStatement(p[1], p[2])

###########################
#     Other functions     #
###########################
def p_print(p):
    ''' one_line_instruction    : PRINT multi_expressions '''
    p[0] = AST.Print(p[2])

def p_matrix_constructors(p):
    ''' expression  : ZEROS '(' expression ')'
                    | ONES  '(' expression ')'
                    | EYE   '(' expression ')' '''
    p[0] = AST.MatrixConstructor(p[1], p[3])

###########################
#        Operators        #
###########################
def p_binary_relational_operators(p):
    ''' condition   : expression '<' expression
                    | expression '>' expression
                    | expression LOWEREQUAL expression
                    | expression GREATERREQUAL expression
                    | expression NOTEQUAL expression
                    | expression EQUAL expression '''
    p[0] = AST.Condition(p[1], p[2], p[3])

def p_binary_assignment_operators(p):
    ''' one_line_instruction    : variable '=' expression
                                | variable ADDASSIGN expression
                                | variable SUBASSIGN expression
                                | variable MULASSIGN expression
                                | variable DIVASSIGN expression '''
    p[0] = AST.Assignment(p[1], p[2], p[3])

def p_binary_additive_multiplicative_operators(p):
    ''' expression  : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression '''
    p[0] = AST.NumberOperator(p[1], p[2], p[3])

def p_binary_matrix_operators(p):
    ''' expression  : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression '''
    p[0] = AST.MatrixOperator(p[1], p[2], p[3])

def p_unary_prefix_operators(p):
    ''' expression  : '-' expression %prec UMINUS
                    | '+' expression %prec UPLUS
                    | '!' expression %prec UEXCLAMATION '''
    p[0] = AST.PrefixOperator(p[1], p[2])

def p_unary_postfix_operators(p):
    ''' expression  : expression '\\'' %prec UTRANSPOSE '''
    p[0] = AST.PostfixOperator(p[1], p[2])

###########################
#        Terminals        #
###########################
def p_operands(p):
    ''' expression  : factor
                    | variable
                    | matrix '''
    p[0] = AST.Operand(p[1])

def p_intnum(p):
    ''' factor      : INTNUM '''
    p[0] = AST.IntNum(p[1])

def p_realnum(p):
    ''' factor      : REALNUM '''
    p[0] = AST.RealNum(p[1])

def p_variable(p):
    ''' variable    : ID
                    | ID '[' multi_indexes ']' '''
    if len(p) == 2:
        p[0] = AST.Variable(p[1])
    elif len(p) == 5:
        p[0] = AST.Variable(p[1], p[3])

def p_multiple_indexes(p):
    ''' multi_indexes   : multi_indexes ',' index
                        | index '''
    if len(p) == 2:
        p[0] = AST.MultipleIndexes(p[1])
    elif len(p) == 4:
        p[0] = p[1]
        p[0].addIndex(p[3])

def p_index(p):
    ''' index           : INTNUM '''
    p[0] = AST.IntNum(p[1])

def p_matrix(p):
    ''' matrix      : '[' multi_lists ']' '''
    p[0] = AST.Matrix(p[2])

def p_multiple_lists(p):
    ''' multi_lists : multi_lists ';' list
                    | list '''
    if len(p) == 2:
        p[0] = AST.MultipleLists(p[1])
    elif len(p) == 4:
        p[0] = p[1]
        p[0].addList(p[3])

def p_list(p):
    ''' list        : list ',' factor
                    | factor '''
    if len(p) == 2:
        p[0] = AST.List(p[1])
    elif len(p) == 4:
        p[0] = p[1]
        p[0].addElement(p[3])

def p_string(p):
    ''' expression  : STRING '''
    p[0] = AST.String(p[1])

def p_error(p):
    if(p):
        print("SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value)
    else:
        print("SYNTACTIC ERROR: Unknown syntax error")

parser = yacc.yacc()
