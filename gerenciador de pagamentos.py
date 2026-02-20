while True:
    try:
        p=float(input('Preço das compras: R$'))
    except:
        print('\033[31mDIGITE O VALOR DAS COMPRAS\033[m')
        continue
    print("""FORMAS DE PAGAMENTO
\033[33m1\033[m - A VISTA DINHEIRO/CHEQUE
\033[34m2\033[m - A VISTA CARTÃO
\033[35m3\033[m - 2X NO CARTÃO
\033[36m4\033[m - 3X OU MAIS NO CARTÃO""")
    try:
        o = int(input('Escolha: '))
    except:
        print('\033[31mDIGITE UM DOS NUMEROS APRESENTADOS\033[m')
        continue
    if o == 1:
        d = p-(p*10)/100
        print(f'Sua compra de R${p:.2f} vai custar R${d:.2f} no final')
        break
    elif o == 2:
        d = p-(p*5)/100
        print(f'Sua compra de R${p:.2f} vai custar R${d:.2f} no final')
        break
    elif o == 3:
        t = p/2
        print(f'Sua compra de R${p:.2f} será parcelada em 2x de R${t:.2f}')
        break
    elif o==4:
        try:
            pa=int(input('Quantas parcelas? '))
        except:
            print('VALOR INVALIDO')
            continue
        if pa <= 3:
            print('\033[31mNÚMERO DE PARCELAS PRECISA SER NO MÍNIMO 3\033[m')
            continue
        j = (p*(20/100))+p
        a = j/pa
        print(f'Sua compra será parcelada em {pa}x de R${a:.2f}')
        print(f'Sua compra de R${p:.2f} vai custar R${j:.2f} no final')
        break
    else:
        print('OPÇÃO INVALIDA.')