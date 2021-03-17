"""Class for AST nodes"""


class AST:
    pass


class Chunk(AST):
    def __init__(self, block):
        self.block = block

    def __str__(self):
        return f"Chunk({self.block})"


class Block(AST):
    def __init__(self, stat, retstat=None):
        self.stat = stat
        self.retstat = retstat

    def __str__(self):
        if self.retstat:
            return f"Block({self.stat} {self.retstat})"
        else:
            return f"Block({self.stat})"


class StatList(AST):
    def __init__(self, stat, stat_list=None):
        self.stat = stat
        self.stat_list = stat_list

    def __str__(self):
        if self.stat_list:
            return f"StatList({self.stat}, {self.stat_list})"
        else:
            return f"StatList({self.stat})"


class AssignStat(AST):
    def __init__(self, var, exp):
        self.var = var
        self.exp = exp

    def __str__(self):
        return f"AssignStat({self.var} = {self.exp})"


class RetStat(AST):
    def __init__(self, exp=None):
        self.exp = exp

    def __str__(self):
        return f"RetStat({self.exp})"


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


class Empty(AST):
    def __init__(self):
        self.value = 'nil'

    def __str__(self):
        return "Empty()"
