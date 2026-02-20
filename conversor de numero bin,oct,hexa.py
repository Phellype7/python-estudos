while True:
    print('''ESCOLHA A BASE DE CONVERSÃO
DIGITE \033[33m[1]\033[m PRA BINÁRIO
DIGITE \033[31m[2]\033[m PRA OCTAL
DIGITE \033[34m[3]\033[m PRA HEXADECIMAL
DIGITE \033[35m[4]\033[m PRA SAIR''')
    try:
        b = int(input('Escolha: '))
    except:
        print('DIGITE O NÚMERO RELACIONADO A BASE DE CONVERSÃO ESCOLHIDA')
        continue
    if b not in [1,2,3,4]:
        print('DIGITE O NÚMERO RELACIONADO A BASE DE CONVERSÃO ESCOLHIDO')
        continue
    if b == 4:
        print('Saindo...')
        break
    try:
        a = int(input('ESCOLHA UM NUMERO: '))
    except:
        print('PRECISA SER UM NÚMERO!!')
        continue

    if b == 1:
        print(f'{a} convertido para binário é {bin(a)[2:]}')
    elif b == 2:
        print(f'{a} convertido para octal é {oct(a)[2:]}')
    elif b == 3:
        print(f'{a} convertido para hexadecimal é {hex(a)[2:]}')
    else:
        print('Opção inválida. Tente novamente')