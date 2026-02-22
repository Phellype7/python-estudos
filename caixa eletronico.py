print('BANCO ITAÚ')
sa = int(input('Que valor você quer sacar? R$'))
total = sa
ced = 100
toced = 0
while True:
    if total >= ced:
        total -= ced
        toced += 1
    else:
        if toced > 0:
            print(f'Deu o total {toced} cédulas de R$ {ced}')
        if ced == 100:
            ced=50
        elif ced == 50:
            ced=20
        elif ced == 20:
            ced=10
        elif ced == 10:
            ced=5
        elif ced == 5:
            ced=1
        toced = 0
        if total == 0:
            break