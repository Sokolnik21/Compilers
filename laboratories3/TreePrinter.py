from __future__ import print_function
import AST

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Node)
    def printIntented(self, content, indent=0):
        print(indent * "| " + content)

    ###########################
    #    Program structure    #
    ###########################
    @addToClass(AST.Program)
    def printTree(self, indent=0):
        if(self.multiple_instructions == None):
            pass
        else:
            self.multiple_instructions.printTree(indent)

    @addToClass(AST.MultipleInstructions)
    def printTree(self, indent=0):
        for instruction in self.multiple_instructions:
            instruction.printTree(indent)

    @addToClass(AST.MultipleExpressions)
    def printTree(self, indent=0):
        for expression in self.multiple_expressions:
            expression.printTree(indent)

    ###########################
    #       Control flow      #
    ###########################
    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        self.printIntented("IF", indent)
        self.condition.printTree(indent + 1)
        self.printIntented("THEN", indent)
        self.if_instruction.printTree(indent + 1)
        self.printIntented("ELSE", indent)
        self.else_instruction.printTree(indent + 1)

    @addToClass(AST.IfOnly)
    def printTree(self, indent=0):
        self.printIntented("IF", indent)
        self.condition.printTree(indent + 1)
        self.printIntented("THEN", indent)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        self.printIntented("FOR", indent)
        self.id.printTree(indent + 1)
        self.printIntented("RANGE", indent + 1)
        self.range_start.printTree(indent + 2)
        self.range_end.printTree(indent + 2)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        self.printIntented("WHILE", indent)
        self.condition.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.JumpingStatement)
    def printTree(self, indent=0):
        self.printIntented(self.name, indent)
        if(self.multiple_expressions == None):
            pass
        else:
            self.multiple_expressions.printTree(indent + 1)

    ###########################
    #     Other functions     #
    ###########################
    @addToClass(AST.Print)
    def printTree(self, indent=0):
        self.printIntented("PRINT", indent)
        self.multiple_expressions.printTree(indent + 1)

    @addToClass(AST.MatrixConstructor)
    def printTree(self, indent=0):
        self.printIntented(self.name, indent)
        self.value.printTree(indent + 1)

    ###########################
    #        Operators        #
    ###########################
    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        self.printIntented(self.operator, indent)
        self.left_operand.printTree(indent + 1)
        self.right_operand.printTree(indent + 1)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        self.printIntented(self.operator, indent)
        self.left_operand.printTree(indent + 1)
        self.right_operand.printTree(indent + 1)

    @addToClass(AST.NumberOperator)
    def printTree(self, indent=0):
        self.printIntented(self.operator, indent)
        self.left_operand.printTree(indent + 1)
        self.right_operand.printTree(indent + 1)

    @addToClass(AST.MatrixOperator)
    def printTree(self, indent=0):
        self.printIntented(self.operator, indent)
        self.left_operand.printTree(indent + 1)
        self.right_operand.printTree(indent + 1)

    @addToClass(AST.PrefixOperator)
    def printTree(self, indent=0):
        self.printIntented(self.operator, indent)
        self.expression.printTree(indent + 1)

    @addToClass(AST.PostfixOperator)
    def printTree(self, indent=0):
        if self.operator == "\'":
            self.printIntented("TRANSPOSE", indent)
        else:
            pass
        self.expression.printTree(indent + 1)

    ###########################
    #        Terminals        #
    ###########################
    @addToClass(AST.Operand)
    def printTree(self, indent=0):
        self.value.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        self.printIntented(str(self.value), indent)

    @addToClass(AST.RealNum)
    def printTree(self, indent=0):
        self.printIntented(str(self.value), indent)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        if(self.multiple_indexes == None):
            self.printIntented(self.name, indent)
        else:
            self.printIntented("REF", indent)
            self.printIntented(self.name, indent + 1)
            self.multiple_indexes.printTree(indent + 1)

    @addToClass(AST.MultipleIndexes)
    def printTree(self, indent=0):
        for index in self.multiple_indexes:
            index.printTree(indent)

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        self.multiple_lists.printTree(indent)

    @addToClass(AST.MultipleLists)
    def printTree(self, indent=0):
        self.printIntented("VECTOR", indent)
        for list in self.multiple_lists:
            list.printTree(indent + 1)

    @addToClass(AST.List)
    def printTree(self, indent=0):
        self.printIntented("VECTOR", indent)
        for element in self.list:
            element.printTree(indent + 1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        self.printIntented(self.name, indent)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
