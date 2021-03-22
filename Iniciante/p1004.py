'''
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. 
A seguir mostre a variável PROD com mensagem correspondente.   

# Exemplos de Entrada/Saída

  Entrada:  3
            9
  Saída: PROD = 27
  -----------------
  Entrada:  -30
            10
  Saída: PROD = -300
  -----------------
  Entrada:  0
            9
  Saída: PROD = 0
'''

# Entrada de informações
A = int(input())
B = int(input())

# Cálculo
P=A*B

# Print
print('PROD = {}'.format(P))