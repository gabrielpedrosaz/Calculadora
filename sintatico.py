from lexico import tokens  # Importar tokens do arquivo lexer
import ply.yacc as yacc

# Definição das precedências
precedence = (
    ('right', 'POWER'),  # Exponenciação à direita
    ('right', 'ROOT'),    # Radiciação à direita
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS'),
)

# Definição das regras da gramática
def p_s(p):
    'S : E'
    p[0] = p[1]
    print("Resultado:", p[0])

def p_e(p):
    '''E : E PLUS T
         | E MINUS T
         | T'''
    if len(p) == 4:
        p[0] = p[1] + p[3] if p[2] == '+' else p[1] - p[3]
    else:
        p[0] = p[1]

def p_t(p):
    '''T : T TIMES F
         | T DIVIDE F
         | F'''
    if len(p) == 4:
        try:
            p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]
        except ZeroDivisionError:
            print("Não é possivel dividir por zero")
    else:
        p[0] = p[1]

def p_f(p):
    '''F : NUMBER
         | LPAR E RPAR
         | F POWER F
         | F ROOT F'''
    if len(p) == 4 and p[2] == '^':  # Exponenciação
        p[0] = p[1] ** p[3]
    elif len(p) == 4 and p[2] == '^^':  # Radiciação
        p[0] = p[1] ** (1 / p[3])  # Raiz enésima (raiz quadrada se p[3] == 2)
    else:
        p[0] = p[1]  # Número ou expressão entre parênteses

def p_error(p):
    if p:
        print("Erro de sintaxe em '%s'" % p.value)
    else:
        print("Erro de sintaxe no final da entrada")

# Criação do parser
parser = yacc.yacc()

# Loop para entrada do usuário
while True:
    try:
        s = input('Calculadora > ')
        if s.strip() == '':
            break
        parser.parse(s)
    except EOFError:
        break
