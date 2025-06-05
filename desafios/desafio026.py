print('{:=^50}'.format(' CONTABILIZADOR DE A '))

frase=str(input('Digite uma frase: ').upper()).strip()

print(f'A letra "A" aparece {frase.count('A')} vezes.')

print(f'Ela aparece pela primeira vez na {frase.find('A')+1}ª posição \ne aparece pela última vez na {frase.rfind('A')+1}ª.')

print('{:=^50}'.format('='))