import ply.lex as lex

# Lista de tokens
tokens = (
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'ROOT',
    'NUMBER', 'LPAR', 'RPAR', 'VAR', 'EQUALS'
)

# Tokens simples
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_ROOT = r'\^\^'
t_LPAR = r'\('
t_RPAR = r'\)'
t_EQUALS = r'='

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Identificar variáveis (letras maiúsculas e minúsculas)
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Reconhecer números entre -1023 e 1023
def t_NUMBER(t):
    r'-?(102[0-3]|10[0-1][0-9]|[0-9]{1,3})'
    t.value = int(t.value)
    return t

# Tratamento de erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()
