v = []

for c in range(0, 5):
    v.append(int(input('Digite um valor: ')))

ma = 0
me = v[0]

for i in range(len(v)):
    if v[i] >= ma:
        ma = v[i]
        pma = i
    if v[i] <= me:
        me = v[i]
        pme = i

print(f'Você digitou os valorres {v}')

print(f'O maior valor digitado foi {ma} na posição ',end='')

for i in range(len(v)):
    if v[i] == ma:
        print(i, end=' ')

print(f'\nO menor valor digitado foi {me} na posição ',end='')

for i in range(len(v)):
    if v[i] == me:
        print(i, end=' ')