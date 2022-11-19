# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o salário do funcionário? R$ '))
novo_salario = salario + (salario * 15 / 100)
print('O salário era R${} e com 15% de aumento ficou R${:.2f}.'.format(salario, novo_salario))
