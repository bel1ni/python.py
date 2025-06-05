print('{:=^50}'.format('ANALISTA DE NOMES'))

nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print(f'Com letras maiúsculas: {nome.upper()}.')

print(f'Com minúsculas: {nome.lower()}.')

print(f'Ao todo tem {len(nome)} caracteres.')

espaco=int(nome.count(' '))
print(f'São {len(nome)-espaco} letras.')

#print(f'O primeiro nome tem {nome.find(' ')} letras.')
separa=nome.split()
print(f'O primeiro nome tem {len(separa[0])} letras.')

print('{:=^50}'.format('='))