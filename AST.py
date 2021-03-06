"""Class for AST nodes"""


class AST:
    pass


class Binop(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Numeral(AST):
    def __init__(self, value):
        self.value = value
