""" Lexer for Lua interpreter

"""

import ply.lex as lex

keywords = {}


tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
]

literals = ["(", ")", '=']

tokens += keywords.values()

t_ignore = " \t"


# Tokens = (tok.type, tok.value, tok.lineno, tok.lexpos)
def t_NUMBER(t):
    r'([0-9]*[.][0-9]+)|([0-9]+)'
    if "." in t.value:
        t.value = float(t.value)
        return t
    else:
        t.value = int(t.value)
        return t


# def t_IDENTIFIER(t):
#     r'[a-zA-Z_][a-zA-Z0-9]*'
#     t.type = keywords.get(t.value, 'IDENTIFIER')    # Check for reserved words
#     return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex(debug=False)

if __name__ == "__main__":
    # Test it out
    data = '''
    3 + 4.4 * .10
      + (20 * 2)
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


