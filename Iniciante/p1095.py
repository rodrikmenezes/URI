'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
'''

I, J = 1, 60
while J >= 0:
    print('I={} J={}'.format(I, J))
    I += 3
    J -= 5