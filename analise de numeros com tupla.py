n = (
int(input('digite o primeiro numero: ')),
int(input('digite mais um numero: ')),
int(input('digite outro numero: ')),
int(input('digite o ultimo numero: '))
)

print('Você digitou os valores',n)

se = n.count(7)
print(f'O valor 7 apareceu {se} vezes')

if 4 in n:
    qu = n.index(4)
    print(f'O valor 4 apareceu na {qu+1}º posição ')

print(f'Os valores pares digitados foram',end=' ')
for p in n:
    if p % 2 == 0:
        print (p,end=' ')