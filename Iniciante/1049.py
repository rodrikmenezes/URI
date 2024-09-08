"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
"""

# testes
# n = "vertebrado mamifero onivoro".split()   # homem
# n = "vertebrado ave carnivoro".split()   # aguia
n = "invertebrado anelideo onivoro".split()   # minhoca


# Entrada de dados
n = input().split()
a, b, c = n

a = input()
b = input()
c = input()

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if c == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if c == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
