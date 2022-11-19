# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

c = float(input('A temperatura em °C é: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}°F.'.format(c, f))