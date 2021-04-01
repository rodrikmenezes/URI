'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
o valor que recebe por hora e calcula o salário desse funcionário. A seguir, 
mostre o número e o salário do funcionário, com duas casas decimais.
'''

# Entradas
Num = int(input())
Horas = float(input())
Valor = float(input())

# Cálculo
Salario = Horas * Valor

# Print
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(Num, Salario))

