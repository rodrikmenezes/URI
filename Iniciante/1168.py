"""
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, 
e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, 
faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.
"""

# Teste
# n = 3
# l = ['115380', '2819311', '23456']

# Entradas
n = int(input())
l = []
for i in range(n):
    l.append(input())

# Cálculo/Saída
for s in l:
    
    # Totalizador
    tot = 0
    
    # Iteração com os números inseridos
    for t in s:

        if t == '1':
            a = 2
        elif t == '4':
            a = 4
        elif t == '7':
            a = 3
        elif t == '8':
            a = 7
        elif t == '2' or t == '3' or t == '5':
            a = 5   
        else: 
            a = 6
        tot += a
            
    print('{} leds'.format(tot))
        





