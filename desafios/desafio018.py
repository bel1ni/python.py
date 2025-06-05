import math
a=int(input('Digite o ângulo: '))
r=math.radians(a)
s=math.sin(r)
c=math.cos(r)
t=math.tan(r)
print('O seno de {}° é {:.3f} \nO cosseno é {:.3f} \nO tangente é {:.3f}'.format(a,s,c,t))
