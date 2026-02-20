a = int(input('DIGITE O ANO PRA SER ANALISADO: '))

if a%4==0 and a%100 !=0 or a%400==0:
    print(f'O ANO DE \033[36m{a}\033[m É BISSEXTO')

else:
    print(f'O ANO DE \033[36m{a}\033[m NÃO É BISSEXTO')