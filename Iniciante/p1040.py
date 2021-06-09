"""
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal,
correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1,respectivamente, para cada uma destas
notas e mostre esta média acompanhada
pela mensagem "Media: ". Se esta média for maior ou igual a 7.0,
imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0,
imprima a mensagem "Aluno reprovado.".
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas,
o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame
obtida pelo aluno. Imprima então a mensagem "Nota do exame:
"acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame
com a média anteriormente calculada e divida por 2). e imprima a mensagem
"Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.",
(caso a média tenha ficado 4.9 ou menos). Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma
mensagem "Media final: " seguido da média final para esse aluno.

# Exemplo

[2.0, 4.0, 7.5, 8.0, 6.4]

Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9
"""

# Entrada de dados
p = [2, 3, 4, 1]
n = input().split()

# Transformar lista de strings para float
q = []
for i in n:
    q.append(float(i))

# Cálculo da média
s = 0
for i in range(4):
    s += p[i] * q[i]
m = s / sum(p)

# Saída
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
elif m < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: {:.1f}'.format(e))
    me = (m + e) / 2
    if me >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(me))