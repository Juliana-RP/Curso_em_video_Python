#Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual o preço do produto? R$ '))
novo_preco = preco - (preco * 5 / 100)
print('O produto custava R${} e com desconto de 5% está custando R${}'.format(preco, novo_preco))
