pares= 0
coluna= 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

        coluna += matriz[l][2]

maior = matriz[1][0]
for c in range(3):
    if maior < matriz[1][c]:
        maior = matriz[1][c]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {maior}')