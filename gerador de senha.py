import random
import string
while True:
    a = int(input('qual o tamanho da senha? '))
    b = string.ascii_letters+string.digits+string.punctuation
    f = ''.join(random.choices(b,k=a))
    print(f'sua senha é {f}')
    a1 = str(input('Quer gerar outra senha? (digite [s] para sim e [n] para não): '))
    if a1 == 's':
        continue
    else:
        print('Saindo...')
        break