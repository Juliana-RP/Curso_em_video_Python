# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Informe quanto você tem na carteira R$ '))
dolar = dinheiro / 5.34
print('Com {} reais eu posso comprar {:.2f} dólares.'.format(dinheiro, dolar))