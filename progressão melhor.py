print('-=-'*10)
print('10 TERMOS DE UMA P.A')
print('-=-'*10)
pr = int(input('Primeiro termo: '))
ra = int(input('Razão: '))

t = pr
c = 1
to = 10

while c <= to:
    print(f'{t}', end=' - ')
    t += ra
    c += 1
print('PAUSA')

while True:
    ma = int(input('\nQuantos termos você quer mostrar mais? '))
    if ma == 0:
        break
    to += ma
    while c <= to:
        print(f'{t}', end=' - ')
        t += ra
        c += 1
print(f'\nProgressão finalizada com {to} termos mostrados.')