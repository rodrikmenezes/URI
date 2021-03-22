'''
Leia dois valores inteiros, no caso para variáveis A e B. A seguir, 
calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

# Exemplos de Entrada/Saída

  Entrada:  30
            10
  Saída: SOMA = 40
  -----------------
  Entrada:  -30
            10
  Saída: SOMA = -20
  -----------------
  Entrada:  0
            0
  Saída: SOMA = 0
'''

# Entrada de informações
A = int(input())
B = int(input())

# Cálculo
S=A+B

# Print
print('SOMA = {}'.format(S))
