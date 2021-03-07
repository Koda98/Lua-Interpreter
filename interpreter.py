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

    def visit_BinopExp(self, node):
        if node.op == "+":
            return self.visit(node.left) + self.visit(node.right)
        elif node.op == "-":
            return self.visit(node.left) - self.visit(node.right)
        elif node.op == "*":
            return self.visit(node.left) * self.visit(node.right)
        elif node.op == "/":
            return self.visit(node.left) / self.visit(node.right)

    def visit_Numeral(self, node):
        return node.value

    def visit_GroupExp(self, node):
        return self.visit(node.exp)

    def run(self):
        return self.visit(self.ast)


def main():
    # while True:
    # s = input()

    s = "12 / 6 - (3 + 5)"

    ast = parser.parse(s, debug=False)
    interpreter = Interpreter(ast)
    result = interpreter.run()
    print(result)


if __name__ == "__main__":
    main()
