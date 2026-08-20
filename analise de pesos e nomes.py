pessoas = []

while True:
    n = input('Nome: ')
    p = int(input('Peso: '))

    pessoas.append([n, p])

    c = input('Quer continuar? [S/N] ').upper()

    if c == 'N':
        break


ma = pessoas[0][1]
me = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] > ma:
        ma = pessoa[1]

    if pessoa[1] < me:
        me = pessoa[1]


print(f"\nMaior peso: {ma} kg")
print("Pessoas mais pesadas:")

for pessoa in pessoas:
    if pessoa[1] == ma:
        print(pessoa[0])


print(f"\nMenor peso: {me} kg")
print("Pessoas mais leves:")

for pessoa in pessoas:
    if pessoa[1] == me:
        print(pessoa[0])