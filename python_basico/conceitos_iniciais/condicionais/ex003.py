'''nota=int(input('Qual sua avaliação para o filme?[0 a 10] '))
if nota == 9 or nota == 10:
    print('EXCELENTE!')
elif nota == 7 or nota == 8:
    print('MUITO BOM!')
if nota == 5 or nota == 6:
    print('REGULAR.')
elif nota <=5 :
    print('RUIM.')'''

print('frete')
valor=float(input('Insira o valor da compra: '))
cadastro=int(input('É cadastrado na loja? \n[1]SIM \n[2]NÃO \n'))
if valor >=100 and cadastro==1:
    print('Frete aplicado!')
else:
    print('Frete não disponível gratuitamente!')

