"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. 
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
"""

# Testes
# n = '7.0 5.0 7.0'.split()       # TRIANGULO ACUTANGULO / TRIANGULO ISOSCELES
# n = '6.0 6.0 10.0'.split()      # TRIANGULO OBTUSANGULO / TRIANGULO ISOSCELES
# n = '6.0 6.0 6.0'.split()       # TRIANGULO ACUTANGULO / TRIANGULO EQUILATERO
# n = '5.0 7.0 2.0'.split()       # NAO FORMA TRIANGULO
# n = '6.0 8.0 10.0'.split()      # TRIANGULO RETANGULO

# Entrada de dados
n = input().split()

# Ordenar dados
n = [float(i) for i in n]
n.sort(reverse=True)

# Converter dados
A, B, C = n
A = float(A)
B = float(B)
C = float(C)

# Configurar mensagem
msg=[]
if A >= B + C:
    msg.append('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2:
    msg.append('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2:
    msg.append('TRIANGULO OBTUSANGULO')
elif A**2 < B**2 + C**2:
    msg.append('TRIANGULO ACUTANGULO')
if A == B == C:
    msg.append('TRIANGULO EQUILATERO')
elif A == B or B == C or C == A:
    msg.append('TRIANGULO ISOSCELES')

# Print
print(*msg, sep='\n')




