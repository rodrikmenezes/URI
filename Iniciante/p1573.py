### OBS: SEM SOLUÇÃO

'''
Uma fábrica produz barras de chocolates no formato de paralelepípedos e de cubos, com o mesmo volume. 
Porém, como a máquina que produz os chocolates em formato de cubo está apresentando alguns problemas, 
os donos da fábrica pediram a sua ajuda para resolver este problema.

Sua tarefa é, dadas as dimensões das arestas do chocolate em formato de paralelepípedo, 
dizer qual é o tamanho que a aresta em formato de cubo deve ter.
'''

# Teste
n = '170 867 253' # 334
# n = '452 378 368' # 397
# n = '0 0 0'

# Entrada
# n = input()

# Cálculo
a, b, c = n.split(' ')

a = int(a)
b = int(b)
c = int(c)

# Saída
if a > 0 and b > 0 and c > 0:
    
    d = int((a*b*c)**(1/3))
    print(d)

# Saída
# print(d)

