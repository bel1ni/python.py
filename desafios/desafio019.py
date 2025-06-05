import random
print('QUEM VAI APAGAR O QUADRO?')
n1=str(input('Digite o 1º nome: '))
n2=str(input('Digite o 2º nome: '))
n3=str(input('Digite o 3º nome: '))
n4=str(input('Digite o 4º nome: '))
nomes=n1,n2,n3,n4
esc=random.choice(nomes)
print(f'O escolhido foi {esc}!')