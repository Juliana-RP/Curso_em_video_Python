# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Informe quanto que você tem de dinheiro: R$ '))
dolar = dinheiro / 5.34
print('Eu tenho {} reais e posso comprar {:.2f} dólares'.format(dinheiro, dolar))