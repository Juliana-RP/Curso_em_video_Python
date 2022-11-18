# Escreva um programa que leia um valor em metros e o exiba convertido em quilômentros, hectômetros, decâmetros, decímetros centímetros, milímetros.

medida = float(input('Coloque uma medida em metros: '))
hm = medida * 0.01
km = medida * 0.001
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida em {}m corresponde a {}hm e em {}km'.format(medida, hm, km))
print('A medida em {}m corresponde a {}dam e em {}dm'.format(medida, dam, dm))
print('A medida em {}m corresponde a {}cm e a {}mm'.format(medida, cm , mm))