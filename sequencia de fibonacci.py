print('-=-'*10)
print('SEQUENCIA DE FIBONACCI')
print('-=-'*10)

n = int(input('quantos termos  você quer mostrar? '))

a,b = 0,1
c = 0

while c < n :
    print(a, end=' - ')
    a,b = b,a+b
    c += 1
print('FIM')