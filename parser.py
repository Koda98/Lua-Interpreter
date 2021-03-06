"""Parser for Lua"""

import lexer
import ply.yacc as yacc
from AST import *

tokens = lexer.tokens


def p_exp(p):
    """exp : exp binop exp
           | numeral"""
    pass


def p_binop(p):
    """binop : PLUS | MINUS | TIMES | DIVIDE"""
    pass


def p_numeral(p):
    """numeral : NUMBER"""
