'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
OBS: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
'''

# Entrada 
idade = int(input())

# Cálculo
anos = idade // 365 
meses = ( idade % 365 ) // 30
dias = ( idade % 365 ) % 30

# Print
print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')