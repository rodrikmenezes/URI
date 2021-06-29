"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.
"""

# Entrada
n = input().split()

# Cálculo
m = [int(i) for i in n]

# Cópia de m
s = m[:]
s.sort()

# Saída
print(*s, sep='\n')
print('')
print(*n, sep='\n')

