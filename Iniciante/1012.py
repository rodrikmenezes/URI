'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''

# Teste
# n = '12.7 10.4 15.2'.split(' ') 
# TRIANGULO: 96.520
# CIRCULO: 725.833
# TRAPEZIO: 175.560
# QUADRADO: 108.160
# RETANGULO: 132.080

# Entrada
n = input().split(' ')

# Converter dados de entrada
A, B, C = float(n[0]), float(n[1]), float(n[2])

# Cálculos
pi = 3.14159
trig = A * C / 2
circ = pi * C ** 2 
trap = (A + B) * C / 2
quad = B ** 2
retg = A * B

# Saída
print('TRIANGULO: {:.3f}'.format(trig))
print('CIRCULO: {:.3f}'.format(circ))
print('TRAPEZIO: {:.3f}'.format(trap))
print('QUADRADO: {:.3f}'.format(quad))
print('RETANGULO: {:.3f}'.format(retg))