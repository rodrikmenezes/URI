'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, 
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
'''

# Teste
# p1 = '12.1 7.3'.split(' ')
# p2 = '-2.5 0.4'.split(' ') # 16.1484

# Entrada
p1 = input().split(' ')
p2 = input().split(' ')

# Atribuir valores x1,x2,y1,y2
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

# Cálculo
d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

# Saída
print('{:.4f}'.format(d))




