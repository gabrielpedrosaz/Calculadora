from lexico import tokens
import ply.yacc as yacc

# Tabela de variáveis
variables = {}

# Definição de precedências
precedence = (
    ('right', 'EQUALS'),
    ('right', 'POWER'),
    ('right', 'ROOT'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS'),
)

# Regras gramaticais
def p_s(p):
    'S : E'
    if -1023 <= p[1] <= 1023:
        p[0] = p[1]
        print("Resultado:", p[0])
    else:
        print("Erro: Resultado fora do intervalo permitido (-1023 a 1023)!")
        p[0] = 0

def p_assignment(p):
    'S : VAR EQUALS E'
    if -1023 <= p[3] <= 1023:
        variables[p[1]] = p[3]
        print(f"Variável {p[1]} atribuída com o valor {p[3]}")
    else:
        print("Erro: Valor fora do intervalo permitido (-1023 a 1023)!")
        variables[p[1]] = 0

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
        if p[2] == '/' and p[3] == 0:
            print("Erro: Divisão por zero!")
            p[0] = 0
        else:
            p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]
    else:
        p[0] = p[1]

def p_f(p):
    '''F : NUMBER
         | VAR
         | LPAR E RPAR
         | F POWER F
         | F ROOT F'''
    if len(p) == 4 and p[2] == '^':  # Exponenciação
        p[0] = p[1] ** p[3]
    elif len(p) == 4 and p[2] == '^^':  # Radiciação
        if p[3] == 0:
            print("Erro: Raiz de índice zero!")
            p[0] = 0
        elif p[1] < 0:
            print("Erro: Raiz de número negativo!")
            p[0] = 0
        else:
            p[0] = p[1] ** (1 / p[3])
    elif len(p) == 4 and p[1] == '(' and p[3] == ')':  # Expressões entre parênteses
        p[0] = p[2]
    elif isinstance(p[1], str):  # Uso de variáveis
        if p[1] in variables:
            p[0] = variables[p[1]]
        else:
            print(f"Erro: Variável '{p[1]}' não definida!")
            p[0] = 0
    else:
        p[0] = p[1]

def p_error(p):
    if p:
        print("Erro de sintaxe em '%s'" % p.value)
    else:
        print("Erro de sintaxe no final da entrada")

# Criação do parser
parser = yacc.yacc()

# Loop da calculadora
if __name__ == '__main__':
    while True:
        try:
            s = input('Calculadora > ')
            if s.strip() == '':
                break
            parser.parse(s)
        except EOFError:
            break
