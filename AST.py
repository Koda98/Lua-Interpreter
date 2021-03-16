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


class UnopExp(AST):
    def __init__(self, op, exp):
        self.op = op
        self.exp = exp

    def __str__(self):
        return f"Unop({self.op}, {self.exp})"


class GroupExp(AST):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return f"GroupExp({self.exp})"


class Numeral(AST):
    def __init__(self, value, negative=False):
        self.value = value
        self.negative = negative
        # if negative:
        #     self.value = value
        # else:
        #     self.value = value

    def __str__(self):
        if self.negative:
            return f"Numeral(-{self.value}"
        else:
            return f"Numeral({self.value})"


class Variable(AST):
    def __init__(self, name, value="Nil"):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Identifier({self.name}, {self.value})"
