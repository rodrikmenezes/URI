"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e
a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

C�digo - Pre�o
1 - 4.0
2 - 4.5
3 - 5.0
4 - 2.0
5 - 1.5

"""

# Entrada
preco = [4.0, 4.5, 5.0, 2.0, 1.5]
n = input()

# C�lculo
cod = int(n[0]) - 1
qtde = int(n[-1])


# Sa�da
print('Total: R$ {:.2f}'.format(qtde * preco[cod]))