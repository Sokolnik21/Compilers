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

def p_program(p):
    ''' program             : multi_instructions
                            |
        multi_instructions  : instruction multi_instructions
                            | instruction '''

def p_control_flow(p):
    ''' instruction : IF '(' condition ')' instruction ELSE instruction
                    | IF '(' condition ')' instruction %prec ONLY_IF
                    | FOR ID '=' expression ':' expression instruction
                    | WHILE '(' condition ')' instruction '''

def p_instruction_form(p):
    ''' instruction : '{' multi_instructions '}'
                    | one_line_instruction ';' '''

def p_single_statements(p):
    ''' one_line_instruction    : BREAK
                                | CONTINUE
                                | RETURN multi_expressions '''

def p_print(p):
    ''' one_line_instruction    : PRINT multi_expressions '''

def p_binary_assignment_operators(p):
    ''' one_line_instruction    : variable '=' expression
                                | variable ADDASSIGN expression
                                | variable SUBASSIGN expression
                                | variable MULASSIGN expression
                                | variable DIVASSIGN expression '''

def p_create_matrix(p):
    ''' expression  : ZEROS '(' expression ')'
                    | ONES  '(' expression ')'
                    | EYE   '(' expression ')' '''

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

def p_binary_relational_operators(p):
    ''' condition   : expression '<' expression
                    | expression '>' expression
                    | expression LOWEREQUAL expression
                    | expression GREATERREQUAL expression
                    | expression NOTEQUAL expression
                    | expression EQUAL expression '''

def p_multiple_expressions(p):
    ''' multi_expressions   : expression ',' multi_expressions
                            | expression '''

def p_unary_prefix_operators(p):
    ''' expression  : '-' expression %prec UMINUS
                    | '+' expression %prec UPLUS
                    | '!' expression %prec UEXCLAMATION '''

def p_unary_postfix_operators(p):
    ''' expression  : expression '\\'' %prec UTRANSPOSE '''

def p_matrix(p):
    ''' matrix      : '[' multi_lists ']'
        multi_lists : list ';' multi_lists
                    | list
        list        : factor ',' list
                    | factor '''

def p_operands(p):
    ''' expression  : variable
        variable    : ID
                    | ID '[' multi_indexes ']'

        expression  : factor
        factor      : INTNUM
                    | REALNUM

        expression  : matrix
                    | STRING '''

def p_multiple_indexes(p):
    ''' multi_indexes   : index ',' multi_indexes
                        | index

        index           : INTNUM '''

def p_error(p):
    if(p):
        print("SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value)
    else:
        print("SYNTACTIC ERROR: Unknown syntax error")

parser = yacc.yacc()
