from math import ceil
print('{:=^50}'.format('BALDES DE TINTA'))
l=float(input('Qual a largura da parede? '))
a=float(input('Qual a altura da parede? '))

area=l*a
tinta=area/2

baldes = ceil(tinta)
print('A área tem {} metros² e são necessários {} baldes de tinta para pintá-la.'.format(area,baldes))
print('{:=^50}'.format('='))