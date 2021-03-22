'''
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# Exemplos de Entrada/Saída
Entrada:    2.00
Saída:      A=12.5664

Entrada:    100.64
Saída:      A=31819.3103

Entrada:    150.00
Saída:      A=70685.7750
'''

# Entrada
raio = float(input())

# Saída
print('A={:.4f}'.format(3.14159 * raio ** 2))