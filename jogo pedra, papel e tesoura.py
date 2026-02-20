import random
print('\033[36m-=-\033[m'*15)
print('PEDRA / PAPEL / TESOURA')
print('\033[37mquem ganhar 3 rodadas primeiro ganha a partida\033[m')
print('\033[36m-=-\033[m'*15)
p=0
b=0
l={1:'pedra', 2:'papel', 3:'tesoura'}
while True:
    r=random.choice(list(l.values()))
    print('''1 - PEDRA
2 - PAPEL
3 - TESOURA''')
    try:
        a=int(input('Qual a sua jogada? '))
    except:
        print('\033[31mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')
        continue
    if a not in l:
        print('\033[31mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')
        continue
    j = l.get(a)
    print(f'Eu joguei {r}')
    if j==r:
        print('\033[33mDEU EMPATE, JOGUE NOVAMENTE\033[m')
    elif (j=='pedra' and r=='tesoura')or(j=='papel' and r=='pedra')or(j=='tesoura' and r=='papel'):
        print('\033[32mVOCÊ VENCEU!\033[m')
        p+=1
    else:
        print('\033[31mVOCÊ PERDEU A RODADA\033[m')
        b+=1
    print(f'PLACAR: Você {p} x {b} Computador')
    if p==3:
        print('\033[35mPARABÉNS!!VOCê VENCEU A PARTIDA\033[m')
        break
    elif b==3:
        print('\033[35mQUE PENA! VOCÊ PERDEU A PARTIDA\033[m')
        break