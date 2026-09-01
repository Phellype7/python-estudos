par = 0
impar = 0
sp = 0
maior = 0

for i in range(10):
    n = int(input(f'Digite o {i+1}º número: '))

    if n % 2 == 0:
        par += 1
        sp += n
    else:
        impar += 1

    if n>maior:
        maior = n

print (f'Pares: {par}')
print (f'Ímpares: {impar}')
print (f'Soma dos pares: {sp}')
print (f'Maior número: {maior}')