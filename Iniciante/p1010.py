'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
'''

# Teste
# n = '13 2 15.30'.split(' ')
# m = '161 4 5.20'.split(' ') # VALOR A PAGAR: R$ 15.50

# Entrada
n = input().split(' ')
m = input().split(' ')

# Cálculo/Saída
print('VALOR A PAGAR: R$ {:.2f}'.format( int(n[1]) * float(n[2]) + int(m[1]) * float(m[2])) )

