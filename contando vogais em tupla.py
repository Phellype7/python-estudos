p = ('jogar','cooperar','programar','presente','cachorro','pai','tecnologia','revolver')
for i in p:
    print(f'Na palavra {i.upper()} temos: ',end='')
    for v in i:
        if v in 'aeiou':
            print(v, end=' ')
    print()