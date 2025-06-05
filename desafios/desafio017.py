import math
co=float(input('Informe o comprimento do cateto oposto: '))
ca=float(input('Informe o comprimento do cateto adjascente: '))
h=math.hypot(co,ca)
print('O valor da hipotenusa é {}.'.format(h))