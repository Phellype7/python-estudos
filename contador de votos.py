py = 0
ja = 0
c = 0

print('''Os votos possíveis são:
1 - Python
2 - Java
3 - C++''')

p = int(input('Quantas pessoas vão votar? '))

for v in range(p):
    print(f'Pessoa {v+1}')
    sv = int(input('Digite seu voto: '))

    if sv == 1:
        py += 1
    elif sv == 2:
        ja += 1
    elif sv == 3:
        c += 1
    else:
        print('Voto inválido!')

if py >= ja and py >= c:
    print(f"1º Python - {py} votos")

    if ja >= c:
        print(f"2º Java - {ja} votos")
        print(f"3º C++ - {c} votos")
    else:
        print(f"2º C++ - {c} votos")
        print(f"3º Java - {ja} votos")

elif ja >= py and ja >= c:
    print(f"1º Java - {ja} votos")

    if py >= c:
        print(f"2º Python - {py} votos")
        print(f"3º C++ - {c} votos")
    else:
        print(f"2º C++ - {c} votos")
        print(f"3º Python - {py} votos")

else:
    print(f"1º C++ - {c} votos")

    if py >= ja:
        print(f"2º Python - {py} votos")
        print(f"3º Java - {ja} votos")
    else:
        print(f"2º Java - {ja} votos")
        print(f"3º Python - {py} votos")