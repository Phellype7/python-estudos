n = int(input('Digite um número: '))
t = 0
for a in range(1,n+1):
    if n%a==0:
        print('\033[34m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print (f'{a}' , end=' ')
print(f'\n\033[mO número {n} foi divisível {t} vezes')
if t == 2:
    print(f'Por causa disso ele é PRIMO')
else:
    print(f'Por causa disso ele não é PRIMO')