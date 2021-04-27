"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
"""

# Entrada
s = int(input())

# Cálculo
if s < 3600:
    h = 0
    m = s // 60
    s = s % 60
    
else:
    h = s // 3600
    m = (s - h * 3600) // 60
    s = s - (h * 3600) - (m * 60)
    
# Saída
print('{}:{}:{}'.format(h,m,s))






