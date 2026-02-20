a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
while True:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair''')
    try:
        c = int(input('Qual a sua opção? '))
    except:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
        continue
    if c == 1:
        s = a + b
        print(f'A soma entre {a} e {b} = {s}')
    if c == 2:
        m = a * b
        print(f'A multiplicação entre {a} e {b} = {m}')
    if c == 3:
        if a > b:
            m = a
        else:
            m = b
        print(f'O maior numero entre {a} e {b} é {m}')
    if c == 4:
        print('Informe os números novamente:')
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
    if c == 5:
        print('Saindo...')
        break