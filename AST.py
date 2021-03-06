"""Class for AST nodes"""


class AST:
    pass


class BinopExp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"Binop({self.left}, {self.op}, {self.right})"


class GroupExp(AST):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return f"GroupExp({self.exp})"


class Numeral(AST):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Numeral({self.value})"


class Variable(AST):
    def __init__(self, name, value="Nil"):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Identifier({self.name}, {self.value})"
