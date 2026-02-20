t=4
si = 0
ve = 0
mu = 0
nve=''

for a in range (1,t+1):
    print(f'----- {a}º PESSOA -----')
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').strip().upper()
    si += i

    if s=='M' and i>ve:
        ve=i
        nve=n
    if s=='F' and i<20:
        mu+=1

m = si / t

print('\nRESULTADO:')
print(f'A média de idade do grupo é de {m} anos')
print(f'O homem mais velho é o {nve} com {ve} anos')
print(f'Ao todo são {mu} mulheres com menos de 20 anos')