"""
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) 
este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
"""

# Entrada
n = float(input())

# Cálculo/Saída
if n >= 0.0 and n <= 25.0:
    print('Intervalo [0,25]')
elif n > 25.0 and n <= 50.0:
    print('Intervalo (25,50]')
elif n > 50.0 and n <= 75.0:
    print('Intervalo (50,75]')
elif n > 75.0 and n <= 100.0:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')