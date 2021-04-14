'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.
'''

# Entrada
num = float(input()) + 0.0001 # ajuste para correção de arrendondamento

# Cédulas
m100 = num // 100
m50 = num % 100 // 50
m20 = num % 100 % 50 // 20
m10 = num % 100 % 50 % 20 // 10
m5 = num % 100 % 50 % 20 // 5
m2 = num % 100 % 50 % 20 % 5 // 2

# Moedas
n1 = num % 100 % 50 % 20 % 5 % 2 // 1
n050 = num % 100 % 50 % 20 % 5 % 2 % 1 // 0.5
n025 = num % 100 % 50 % 20 % 5 % 2 % 1 % 0.5 // 0.25
n010 = num % 100 % 50 % 20 % 5 % 2 % 1 % 0.5 % 0.25 // 0.10
n005 = num % 100 % 50 % 20 % 5 % 2 % 1 % 0.5 % 0.25 % 0.10 // 0.05
n001 = num % 100 % 50 % 20 % 5 % 2 % 1 % 0.5 % 0.25 % 0.10 % 0.05 // 0.01

# Saída
print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(m100))
print('{:.0f} nota(s) de R$ 50.00'.format(m50))
print('{:.0f} nota(s) de R$ 20.00'.format(m20))
print('{:.0f} nota(s) de R$ 10.00'.format(m10))
print('{:.0f} nota(s) de R$ 5.00'.format(m5))
print('{:.0f} nota(s) de R$ 2.00'.format(m2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(n1))
print('{:.0f} moeda(s) de R$ 0.50'.format(n050))
print('{:.0f} moeda(s) de R$ 0.25'.format(n025))
print('{:.0f} moeda(s) de R$ 0.10'.format(n010))
print('{:.0f} moeda(s) de R$ 0.05'.format(n005))
print('{:.0f} moeda(s) de R$ 0.01'.format(n001))