"""Parser for Lua"""

import lexer
import ply.yacc as yacc
from AST import *

tokens = lexer.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_exp_binop(p):
    """exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp"""
    p[0] = BinopExp(p[1], p[2], p[3])


def p_exp_group(p):
    """exp : '(' exp ')'"""
    p[0] = GroupExp(p[2])

# def p_stat_assign(p):
#     """stat : IDENTIFIER '=' exp"""
#     p[0] = Variable(p[1], p[3])

def p_exp_var(p):
    """exp : IDENTIFIER"""
    p[0] = Variable(p[1])


def p_exp_numeral(p):
    """exp : NUMBER"""
    p[0] = Numeral(p[1])


def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
        print(p)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc(debug=True)

if __name__ == "__main__":
    # Test it out
    data = '''
    3 + 4.4 * .10
      + (20 * 2)
    '''

    # Give the parser some input
    parser.error = 0
    p = parser.parse(data)
    if parser.error:
        print(None)
    print(p)
