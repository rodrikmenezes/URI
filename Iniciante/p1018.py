"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
"""

# Entrada
n = int(input())
print(n)

# Saída
m = [100, 50, 20, 10, 5, 2, 1]

for x in m:
    r = int(n / x)
    n = n % x
    print('{} nota(s) de R$ {},00'.format(r, x))

# while n > 0:
#     x = n // m[i]
#     n = n % m[i]
#     print('{} nota(s) de R$ {},00'.format(x, m[i]))
#     i += 1


