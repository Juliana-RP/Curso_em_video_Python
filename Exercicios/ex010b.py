#Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar.

dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = dinheiro / 5.34
euro = dinheiro / 5.55
print('Com {:.2f} reais eu compro {:.2f} em dólar e {:.2f} em euros.'.format(dinheiro, dolar, euro))
