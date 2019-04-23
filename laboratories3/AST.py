class Node(object):
    pass

###########################
#    Program structure    #
###########################
class Program(Node):
    def __init__(self, multiple_instructions=None):
        self.multiple_instructions = multiple_instructions

class MultipleInstructions(Node):
    def __init__(self, instruction):
        self.multiple_instructions = [instruction]

    def addInstruction(self, instruction):
        self.multiple_instructions.append(instruction)

class MultipleExpressions(Node):
    def __init__(self, expression):
        self.multiple_expressions = [expression]

    def addExpression(self, expression):
        self.multiple_expressions.append(expression)

###########################
#       Control flow      #
###########################
class IfElse(Node):
    def __init__(self, condition, if_instruction, else_instruction):
        self.condition = condition
        self.if_instruction = if_instruction
        self.else_instruction = else_instruction

class IfOnly(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class For(Node):
    def __init__(self, id, range_start, range_end, instruction):
        self.id = id
        self.range_start = range_start
        self.range_end = range_end
        self.instruction = instruction

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class JumpingStatement(Node):
    def __init__(self, name, multiple_expressions=None):
        self.name = name
        self.multiple_expressions = multiple_expressions

###########################
#     Other functions     #
###########################
class Print(Node):
    def __init__(self, multiple_expressions):
        self.multiple_expressions = multiple_expressions

class MatrixConstructor(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

###########################
#        Operators        #
###########################
class Condition(Node):
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

class Assignment(Node):
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

class NumberOperator(Node):
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

class MatrixOperator(Node):
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

class PrefixOperator(Node):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

class PostfixOperator(Node):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

###########################
#        Terminals        #
###########################
class Operand(Node):
    def __init__(self, value):
        self.value = value

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class RealNum(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name, multiple_indexes=None):
        self.name = name
        self.multiple_indexes = multiple_indexes

class MultipleIndexes(Node):
    def __init__(self, index):
        self.multiple_indexes = [index]

    def addIndex(self, index):
        self.multiple_indexes.append(index)

class Matrix(Node):
    def __init__(self, multiple_lists):
        self.multiple_lists = multiple_lists

class MultipleLists(Node):
    def __init__(self, list):
        self.multiple_lists = [list]

    def addList(self, list):
        self.multiple_lists.append(list)

class List(Node):
    def __init__(self, element):
        self.list = [element]

    def addElement(self, element):
        self.list.append(element)

class String(Node):
    def __init__(self, name):
        self.name = name

class Error(Node):
    def __init__(self):
        pass
