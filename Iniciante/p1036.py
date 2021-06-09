"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
"""
# Teste
# valores = '10.0 20.1 5.1'

# Entrada
valores = input()

# Cálculo/Saída
a, b, c = valores.split()
a, b, c = float(a), float(b), float(c)

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    print('R1 = {R1:.5f}\nR2 = {R2:.5f}'.format(R1 = (-b+delta**(1/2)) / (2*a), R2 = (-b-delta**(1/2)) / (2*a)))


