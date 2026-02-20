while True:
    print('''ESCOLHA O OPERADOR
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Sair''')
    try:
        op = int(input("Digite o operador: "))
    except:
        print('DIGITE O NÚMERO RELACIONADO AO OPERADOR ESCOLHIDO')
        continue
    if op not in [1,2,3,4,5]:
        print('DIGITE O NÚMERO RELACIONADO AO OPERADOR ESCOLHIDO')
        continue
    if op == 5:
        print('Saindo...')
        break
    try:
        n1 = int(input("Digite o primeiro numero: "))
    except:
        print('PRECISA SER UM NÚMERO')
        continue
    try:
        n2 = int(input("Digite o segundo numero: "))
    except:
        print('PRECISA SER UM NÚMERO')
        continue
    if op == 1:
        print(n1 + n2)
    elif op == 2:
        print(n1 - n2)
    elif op == 3:
        print(n1 * n2)
    elif op == 4:
        print(n1 / n2)
    print('FIM DO CÁLCULO')