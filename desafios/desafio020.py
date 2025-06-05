import random
print('ORDEM DE APRESENTAÇÃO\n')
n1=str(input('Digite o 1º nome: '))
n2=str(input('Digite o 2º nome: '))
n3=str(input('Digite o 3º nome: '))
n4=str(input('Digite o 4º nome: '))
nome=n1,n2,n3,n4
ordem=random.sample(nome, k=4)
resultado='\n'.join(f'{i + 1}º {nome}' for i, nome in enumerate(ordem))
print(f'A ordem de apresentação será \n{resultado}')
