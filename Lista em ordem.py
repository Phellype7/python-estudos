l = []

for c in range(5):
    n = int(input('Digite um número: '))

    if not l:
        l.append(n)
        print('Adicionado na posição 0')

    else:
        for pos, v in enumerate(l):

            if n <= v:
                l.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
        else:
            l.append(n)
            print(f'Adicionado na posição {len(l) - 1}')

print(f'Os valores digitados em ordem foram {l}')