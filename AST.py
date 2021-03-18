"""Class for AST nodes"""


class AST:
    pass


class Chunk(AST):
    def __init__(self, block):
        self.block = block

    def __str__(self):
        return f"Chunk({self.block})"


class Block(AST):
    def __init__(self, stat_list, retstat=None):
        self.stat_list = stat_list
        self.retstat = retstat

    def __str__(self):
        if self.retstat:
            return f"Block({self.stat_list} {self.retstat})"
        else:
            return f"Block({self.stat_list})"


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
    def __init__(self, varlist, explist):
        self.varlist = varlist
        self.explist = explist

    def __str__(self):
        return f"AssignStat({self.varlist} = {self.explist})"


class BreakStat(AST):
    def __init__(self):
        self.value = "break"

    def __str__(self):
        return "break"


class WhileStat(AST):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def __str__(self):
        return f"WhileStat({self.exp} do {self.block} end)"


class IfStat(AST):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def __str__(self):
        return f"IfStat({self.exp} then {self.block} end)"


class RetStat(AST):
    def __init__(self, exp=None):
        self.exp = exp

    def __str__(self):
        return f"RetStat({self.exp})"


class Varlist(AST):
    def __init__(self, var, other=None):
        self.var = var
        self.other = other

    def __str__(self):
        if self.other:
            return f"Varlist({self.var}, {self.other})"
        else:
            return f"Varlist({self.var})"


class Explist(AST):
    def __init__(self, exp, other=None):
        self.exp = exp
        self.other = other

    def __str__(self):
        if self.other:
            return f"Explist({self.exp}, {self.other})"
        else:
            return f"Explist({self.exp})"


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


class VarExp(AST):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return f"VarExp({self.var})"


class BoolExp(AST):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"BoolExp({self.value})"


class Numeral(AST):
    def __init__(self, value, negative=False):
        self.value = value
        self.negative = negative

    def __str__(self):
        if self.negative:
            return f"Numeral(-{self.value}"
        else:
            return f"Numeral({self.value})"


class Variable(AST):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Variable({self.name})"


class Empty(AST):
    def __init__(self):
        self.value = 'nil'

    def __str__(self):
        return "Empty()"
