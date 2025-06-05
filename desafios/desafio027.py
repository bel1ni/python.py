print('{:=^50}'.format(' ANALISTA DE NOME '))

nome=input('Digite seu nome completo: ')
sepa=nome.split()

print(f'Seu primeiro nome é {sepa[0]}.')

print(f'Seu último nome é {sepa[-1]}.')

print(f'Olá, {sepa[0]} {sepa[1][0]}. {sepa[-1]}.')

print('{:=^50}'.format('='))