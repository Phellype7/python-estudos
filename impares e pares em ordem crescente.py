valores = [[],[]]
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')