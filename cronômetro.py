import time
m = int(input('Minutos (pode ser 0): '))
s = int(input('Segundos (pode ser 0): '))
c = m*60+s
for a in range(c+1):
    ma = a//60
    sa = a%60
    print(f'{ma:02d}:{sa:02d}')
    time.sleep(1)
print('\nA CONTAGEM ACABOU!!')