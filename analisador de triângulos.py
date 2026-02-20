a = float(input('primeiro número: '))
b = float(input('segundo número: '))
c = float(input('terceiro número: '))

if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('Os números acima podem formar um triangulo \033[32mEQUILÁTERO\033[m')
    elif a==b or b==c or c==a:
        print('Os números acima podem formar um triangulo \033[32mISÓSCELES\033[m')
    else:
        print('Os números acima podem formar um triangulo \033[32mESCALENO\033[m')
else:
    print('\033[31mAs medidas acima não formam um triangulo\033[m')