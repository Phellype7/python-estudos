co = 0
e = input('Digite a expressão: ')
for c in e:
    if c == '(':
        co+=1
    elif c == ')':
        co-=1
if co < 0 or co > 0:
    print('Sua expressão está errada.')
elif co == 0:
    print('Sua expressão está correta')