
for p in range(1,6):
    peso=float(input(f'DIgite o peso da {p}ª pessoa[kg]: '))
    if p == 1:
        maior=peso
        menor=peso
    else:
        if peso>= maior:
        maior=peso
        elif peso<=menor:
        menor=peso
print(f'O menor peso digitado foi {menor}kg. \nO maior peso digitado foi {maior}kg.')
