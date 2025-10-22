peso=float(input(f'DIgite o peso da 1ª pessoa[kg]: '))
menor=peso
maior=peso
for p in range(2,6):
    peso=float(input(f'DIgite o peso da {p}ª pessoa[kg]: '))
    if peso>= maior:
        maior=peso
    elif peso<=menor:
        menor=peso
print(f'O menor peso digitado foi {menor}kg. \nO maior peso digitado foi {maior}kg.')
