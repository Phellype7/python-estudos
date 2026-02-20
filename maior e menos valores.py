c = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if c == 0:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    c += 1
    s += n
    l = input('Quer continuar? [S/N] ').strip().lower()[0]
    if l == 'n':
        break
media = s / c
print(f'Você digitou {c} números e a média foi {media:.2f}')
print(f'O maior valor foi {ma} e o menor foi {me}')
