# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

b = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(b))
print('Só tem espaço?', b.isspace())
print('É alfanumérico?', b.isalnum())
print('É apenas numérico?', b.isnumeric())
print('Esta em letras maiúsculas?', b.isupper())
print('Esta em letras minúsculas?', b.islower())
print('Está capitalizada?', b.istitle())