import random
c = random.randint(0,100)
pa = 0
print('\033[36m-=-\033[m'*20)
print('ESCOLHI UM NUMÉRO ENTRE 0 A 100, TENTE ADIVINHAR')
print('\033[36m-=-\033[m'*20)
while True:
    try:
        a = int(input('que número eu escolhi? '))
        pa+=1
    except:
        print('DIGITE UM NÚMERO!!')
        continue
    if a == c:
        print('\033[32mPARABENS!! VOCE VENCEU O JOGO\033[m')
        print(f'\033[36mVOCÊ PRECISOU DE {pa} PALPITES\033[m')
        break
    elif a > c:
        print('\033[33mMAIS BAIXO!\033[m')
    else:
        print('\033[34mMAIS ALTO!\033[m')