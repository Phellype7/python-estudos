print('-=-'*10)
print('10 TERMOS DE UMA P.A')
print('-=-'*10)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p+(10-1)*r

for c in range(p ,d+r, r):
    print(c,end=' - ')

print('ACABOU')