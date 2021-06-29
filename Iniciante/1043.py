"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X
"""

# Testes
# n = '6.0 4.0 2.0'.split()       # Area = 10.0
# n = '6.0 4.0 2.1'.split()       # Perimetro = 12.1

# Entrada de dados
n = input().split()

# Transformar dados
a, b, c = float(n[0]), float(n[1]), float(n[2])

# Cálculo
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {}'.format(a+b+c))
else:
    print('Area = {}'.format( (a+b)*c / 2 ) )

