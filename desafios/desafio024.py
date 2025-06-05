print('{:=^50}'.format(' NOME SANTO '))

city=str(input('Qual o nome da sua cidade? ').strip().upper().replace('SÃO','SANTO'))
r=bool('SANTO' in city)
if r == True:
    print('Sua cidade tem um nome santo.')
else:
    print('Sua cidade não tem um nome santo.')

print('{:=^50}'.format('='))