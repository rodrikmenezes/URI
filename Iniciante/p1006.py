'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. 
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''

# Entrada
n1 = float(input())
n2 = float(input())
n3 = float(input())

# Cálculo
M = ( (n1 * 2)  + (n2 * 3) + (n3 * 5) ) / 10

# Saída
print('MEDIA = {:.1f}'.format(M)) 