import datetime
atual = datetime.date.today().year

a = int(input('Ano de nascimento: '))
idade = atual - a

print(f'o atleta tem {idade} anos')

if idade<=9:
    print('CLASSIFICAÇÃO: Mirim')
elif idade<=14:
    print('CLASSIFICAÇÃO: Infantil')
elif idade<=19:
    print('CLASSIFICAÇÃO: Junior')
elif idade<=25:
    print('CLASSIFICAÇÃO: Sênior')
else:
    print('CLASSIFICAÇÃO: Master')