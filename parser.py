"""Parser for Lua"""

import lexer
import ply.yacc as yacc
from AST import *

tokens = lexer.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)


def p_chunk(p):
    """chunk : block"""
    p[0] = Chunk(p[1])


def p_block(p):
    """block : stat_list"""
    p[0] = Block(p[1])


def p_stat_list(p):
    """stat_list : stat stat_list
                 | empty"""
    if len(p) == 3:
        p[0] = StatList(p[1], p[2])
    else:
        p[0] = Empty()


def p_stat_semi(p):
    """stat : ';'"""
    p[0] = Empty()


def p_stat_assign(p):
    """stat : varlist '=' explist"""
    p[0] = AssignStat(p[1], p[3])


def p_stat_return(p):
    """stat : RETURN
            | RETURN exp
            | RETURN ';'
            | RETURN exp ';'"""
    if len(p) == 2:
        p[0] = RetStat()
    elif p[2] == ";":
        p[0] = RetStat()
    else:
        p[0] = RetStat(p[2])


def p_varlist(p):
    """varlist : var
               | var ',' varlist"""
    if len(p) == 2:
        p[0] = Varlist(p[1])
    else:
        p[0] = Varlist(p[1], p[3])


def p_var(p):
    """var : IDENTIFIER"""
    p[0] = Variable(p[1])


def p_explist(p):
    """explist : exp
               | exp ',' explist"""
    if len(p) == 2:
        p[0] = Explist(p[1])
    else:
        p[0] = Explist(p[1], p[3])


def p_exp_binop(p):
    """exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp"""
    p[0] = BinopExp(p[1], p[2], p[3])


def p_exp_group(p):
    """exp : '(' exp ')'"""
    p[0] = GroupExp(p[2])


def p_exp_var(p):
    """exp : var"""
    p[0] = VarExp(p[1])


def p_exp_numeral(p):
    """exp : NUMBER"""
    p[0] = Numeral(p[1])


def p_exp_unop(p):
    """exp : MINUS exp %prec UMINUS"""
    p[0] = UnopExp(p[1], p[2])


def p_empty(p):
    """empty :"""
    p[0] = Empty()


def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
        print(p)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p


if __name__ == "__main__":
    # Test it out
    data = '''
    a, b, c = 1, 2, 3
    '''

    # Give the parser some input
    parser.error = 0
    p = parser.parse(data, debug=False)
    if parser.error:
        print(None)
    print(p)
