import random
c = 0
print('-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*10)

while True:
    a = int(input('Diga um valor: '))
    b = input('Par ou ímpar? [P/I] ').strip().lower()

    r = random.randint(1, 50)
    to = a + r

    if to % 2 == 0:
        resultado = 'p'
        print(f'Você jogou {a} e o computador {r}. Total {to} deu PAR')
    else:
        resultado = 'i'
        print(f'Você jogou {a} e o computador {r}. Total {to} deu ÍMPAR')

    if b == resultado:
        print('Você venceu! Bora dnv')
        c += 1
    else:
        print(f'GAME OVER! Você venceu {c} vezes.')
        break