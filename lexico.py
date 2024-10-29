import ply.lex as lex

tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'ROOT', 'NUMBER', 'LPAR', 'RPAR')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_ROOT = r'\^\^'  # Radiciação usando ^^
t_LPAR = r'\('
t_RPAR = r'\)'

t_ignore = ' \t'

def t_NUMBER(t):
    r'-?(102[0-3]|10[0-1][0-9]|[0-9]{1,3})'  # Esta expressão precisa considerar números negativos
    t.value = int(t.value)
    return t

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
