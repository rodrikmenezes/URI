'''
Nós temos alguns textos e queremos formatá-los e justificá-los à direita, ou seja, 
alinhar suas linhas à margem direita de cada um. Crie um programa que, após ler um texto, 
reimprima esse texto com apenas um espaço entre as palavras e suas linhas justificadas à direita em todo o texto.
'''

# file = open('teste.txt', 'w')
check = 0
while True:
    n = int(input())
    if n == 0:
        break
    if check == 1:
        print()
        # file.write('\n')
    l = []
    for i in range(n):
        l.append(' '.join(input().split()))
    m = max(len(i) for i in l)

    for i in range(len(l)):
        for j in range(m-len(l[i])):
            print('', end=' ')
            # file.write(' ')
        print(l[i])
        # file.write(l[i])
        # file.write('\n')

    check = 1

# file.close()