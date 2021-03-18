"""Interpreter for Lua"""

import parser


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, ast):
        self.state = {}
        self.ast = ast

    def visit_Chunk(self, node):
        self.visit(node.block)

    def visit_Block(self, node):
        self.visit(node.stat_list)

    def visit_StatList(self, node):
        self.visit(node.stat)
        if node.stat_list:
            self.visit(node.stat_list)

    def visit_AssignStat(self, node):
        varlist = self.visit(node.varlist)
        explist = self.visit(node.explist)
        for var, exp in zip(varlist, explist):
            name = var.name
            exp = self.visit(exp)
            self.state[name] = exp

    def visit_RetStat(self, node):
        return self.visit(node.exp)

    def visit_Varlist(self, node):
        varlist = [node.var]
        if node.other:
            varlist += self.visit(node.other)
        return varlist

    def visit_Explist(self, node):
        explist = [node.exp]
        if node.other:
            explist += self.visit(node.other)
        return explist

    def visit_BinopExp(self, node):
        if node.op == "+":
            return self.visit(node.left) + self.visit(node.right)
        elif node.op == "-":
            return self.visit(node.left) - self.visit(node.right)
        elif node.op == "*":
            print("left node:", node.left)
            print("right node:", node.right)
            return self.visit(node.left) * self.visit(node.right)
        elif node.op == "/":
            return self.visit(node.left) / self.visit(node.right)
        elif node.op == "//":
            return self.visit(node.left) // self.visit(node.right)
        elif node.op == "<":
            return self.visit(node.left) < self.visit(node.right)
        elif node.op == ">":
            return self.visit(node.left) > self.visit(node.right)
        elif node.op == "<=":
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op == ">=":
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op == "==":
            return self.visit(node.left) == self.visit(node.right)
        elif node.op == "~=":
            return self.visit(node.left) != self.visit(node.right)

    def visit_UnopExp(self, node):
        if node.op == "-":
            return -1 * self.visit(node.exp)
        elif node.op == "not":
            return not self.visit(node.exp)

    def visit_GroupExp(self, node):
        return self.visit(node.exp)

    def visit_VarExp(self, node):
        return self.visit(node.var)

    def visit_BoolExp(self, node):
        if node.value == "true":
            return True
        else:
            return False

    def visit_Numeral(self, node):
        if node.negative:
            return -1 * node.value
        else:
            return node.value

    def visit_Variable(self, node):
        name = node.name
        value = self.state.get(name)
        if value:
            return value
        else:
            return "nil"

    def visit_Empty(self, node):
        return node.value

    def run(self):
        return self.visit(self.ast)


def main(inter_debug=False, parse_debug=False):
    # while True:
    # s = input()

    s = """
    do
    a = 1 < 2
    c = not (4 == 1)
    end
    """

    ast = parser.parse(s, debug=parse_debug)
    if inter_debug:
        print("AST:", ast)
    interpreter = Interpreter(ast)
    result = interpreter.run()
    if inter_debug:
        print("State:", interpreter.state)
    # print(result)


if __name__ == "__main__":
    main(inter_debug=True, parse_debug=False)
