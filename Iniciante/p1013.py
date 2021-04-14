'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
'''

# Entrada
a, b, c = input().split(' ')

# Converter em número int
a = int(a)
b = int(b)
c = int(c)

# Cálculo
d = (a + b + abs(a - b) ) / 2
maior = (d + c + abs(d - c) ) / 2

# Saída
print('{:.0f} eh o maior'.format(maior))