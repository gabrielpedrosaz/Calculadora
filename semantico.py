import ply.yacc as yacc
from lexico import tokens  # Importar tokens do arquivo lexer

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER', 'ROOT'),
)

# Definição das regras da gramática
def p_s(p):
    'S : E'
    p[0] = p[1]
    print("Resultado:", p[0])

def p_e_plus(p):
    'E : E PLUS T'
    p[0] = p[1] + p[3]

def p_e_minus(p):
    'E : E MINUS T'
    p[0] = p[1] - p[3]

def p_t_times(p):
    'T : T TIMES F'
    p[0] = p[1] * p[3]

def p_t_divide(p):
    'T : T DIVIDE F'
    p[0] = p[1] / p[3]

def p_t_power(p):
    'T : T POWER F'
    p[0] = p[1] ** p[3]

def p_f_root(p):
    'F : ROOT F'
    p[0] = p[2] ** 0.5  # Radiciação

def p_f_parens(p):
    'F : LPAR E RPAR'
    p[0] = p[2]

def p_f_number(p):
    'F : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p:
        print("Erro de sintaxe em '%s'" % p.value)
    else:
        print("Erro de sintaxe no final da entrada")

# Criação do parser
parser = yacc.yacc()

while True:
    try:
        s = input('Calculadora > ')
        if s.strip() == '':
            break
        parser.parse(s)
    except EOFError:
        break
