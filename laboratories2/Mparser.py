#!/usr/bin/python

import scanner
import ply.yacc as yacc

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

def p_multiple_instructions(p):
    ''' multi_instructions  : multi_instructions instruction
                            | instruction '''

def p_instruction_form(p):
    ''' instruction : '{' multi_instructions '}'
                    | one_line_instruction ';' '''

def p_multiple_expressions(p):
    ''' multi_expressions   : multi_expressions ',' expression
                            | expression '''

###########################
#       Control flow      #
###########################
def p_control_flow(p):
    ''' instruction : IF '(' condition ')' instruction ELSE instruction
                    | IF '(' condition ')' instruction %prec ONLY_IF
                    | FOR variable '=' expression ':' expression instruction
                    | WHILE '(' condition ')' instruction '''

def p_jumping_statements(p):
    ''' one_line_instruction    : BREAK
                                | CONTINUE
                                | RETURN multi_expressions '''

###########################
#     Other functions     #
###########################
def p_print(p):
    ''' one_line_instruction    : PRINT multi_expressions '''

def p_matrix_constructors(p):
    ''' expression  : ZEROS '(' expression ')'
                    | ONES  '(' expression ')'
                    | EYE   '(' expression ')' '''

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
def p_binary_assignment_operators(p):
    ''' one_line_instruction    : variable '=' expression
                                | variable ADDASSIGN expression
                                | variable SUBASSIGN expression
                                | variable MULASSIGN expression
                                | variable DIVASSIGN expression '''

def p_binary_additive_multiplicative_operators(p):
    ''' expression  : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression '''

def p_binary_matrix_operators(p):
    ''' expression  : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression '''

def p_unary_prefix_operators(p):
    ''' expression  : '-' expression %prec UMINUS
                    | '+' expression %prec UPLUS
                    | '!' expression %prec UEXCLAMATION '''

def p_unary_postfix_operators(p):
    ''' expression  : expression '\\'' %prec UTRANSPOSE '''

###########################
#        Terminals        #
###########################
def p_operands(p):
    ''' expression  : factor
                    | variable
                    | matrix '''

def p_intnum(p):
    ''' factor      : INTNUM '''

def p_realnum(p):
    ''' factor      : REALNUM '''

def p_variable(p):
    ''' variable    : ID
                    | ID '[' multi_indexes ']' '''

def p_multiple_indexes(p):
    ''' multi_indexes   : multi_indexes ',' index
                        | index '''

def p_index(p):
    ''' index           : INTNUM '''

def p_matrix(p):
    ''' matrix      : '[' multi_lists ']' '''

def p_multiple_lists(p):
    ''' multi_lists : multi_lists ';' list
                    | list '''
def p_list(p):
    ''' list        : list ',' factor
                    | factor '''

def p_string(p):
    ''' expression  : STRING '''

def p_error(p):
    if(p):
        print("SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value)
    else:
        print("SYNTACTIC ERROR: Unknown syntax error")

parser = yacc.yacc()
