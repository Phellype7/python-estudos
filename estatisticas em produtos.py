mil = s = bar = 0
nbar = ''

print('MERCADINHO DA ESQUINA')

while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))
    c = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    s += p

    if p>1000:
        mil += 1
    if bar==0 or p<bar:
        nbar = n
        bar = p
    if c == 'n':
        print('-'*5,'FIM DO PROGRAMA','-'*5)
        break

print(f'O total da compra foi R${s:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbar} que custa R${bar:.2f}')