from datetime import date
a = int(input('ANO DE NASCIMENTO: '))
ano = date.today().year
i = ano-a
print(f'quem nasceu em {a} tem {i} anos em {ano}')

if i == 18:
    print('Você precisa se alistar imediatamente!')

elif i<18:
    c = 18-i
    d = a+18
    print(f'''Ainda faltam {c} ano(s) para o seu alistamento
Seu alistamento será em {d}''')

else:
    c = i-18
    d = a+18
    print(f'''Você ja deveria ter se alistado a {c} ano(s)
Seu alistamento foi em {d}''')