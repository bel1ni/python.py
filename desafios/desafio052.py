print("LEITOR DE NÚMERO PRIMO".center(50,'='))
n=int(input('Digite um número: '))
vezes=0
for c in range(1,n+1):
    if n%c==0:
        print(c)
        vezes+=1
if vezes == 2:
    print(f'O número é primo. Só é divisível por 1 e por ele mesmo.')
else:
    print(f'O número não é primo, pois foi divisível por {vezes} números.')