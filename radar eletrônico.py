print('-=-'*14)
a = int(input('QUAL A VELOCIDADE DO CARRO? '))
print('-=-'*14)
if a<=60:
    print('TENHA UM BOM DIA E DIRIJA COM SEGURANÇA!')
else:
    c = (a-60)*7
    print('VOCÊ FOI MULTADO! POR EXEDER O LIMITE DE 60KM/H'
          f' SUA MULTA É DE R${c}')