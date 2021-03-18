""" Lexer for Lua interpreter

"""

import ply.lex as lex

keywords = {
    "nil": "NIL",
    "return": "RETURN",
    "do": "DO",
    "end": "END",
    "false": "FALSE",
    "true": "TRUE",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "while": "WHILE",
    "break": "BREAK",
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
}


tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'INTEGER_DIVIDE',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'NE',
    'EQUALS',
]

literals = ["(", ")", '=', ';', ',']

tokens += keywords.values()

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_INTEGER_DIVIDE = r'\/\/'
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_NE = r'~='
t_EQUALS = r'=='

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


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')    # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    pass
    # t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex(debug=False)

if __name__ == "__main__":
    # Test it out
    data = '''
    a = 1
    if 9 >= 2 then
        a = 3
    else
        a = 2
    end
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
