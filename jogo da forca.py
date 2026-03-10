import random

lista_p = ["amarelo","amiga","amor","ave","aviao","avo","balao","bebe","bolo","branco",
"cama","caneca","celular","ceu","clube","copo","doce","elefante","escola",
"estojo","faca","foto","garfo","geleia","girafa","janela","limonada","mae",
"meia","noite","oculos","onibus","ovo","pai","pao","parque","passaro",
"peixe","pijama","rato","umbigo","cachorro","gato","leao","tigre","vaca","cavalo","porco","galinha",
"banana","maca","uva","pera","manga","melancia","abacaxi","arroz","feijao","carne","leite","queijo","pao",
"mesa","cadeira","porta","janela","telhado","parede","bola","boneca","pipa","patins","bicicleta",
"sol","lua","estrela","nuvem","chuva","vento","rio","mar","lago","praia","ilha",
"verde","azul","preto","rosa","roxo","camisa","calca","sapato","tenis","meia"]

boneco = [
"""
______
|    O
|
|
|
|
""",
"""
______
|    O
|    |
|
|
|
""",
"""
______
|    O
|   /|
|
|
|
""",
"""
______
|    O
|   /|\\
|
|
|
""",
"""
______
|    O
|   /|\\
|   / 
|
|
""",
"""
______
|    O
|   /|\\
|   / \\
|
|
"""]

letras_us = []

pa = random.choice(lista_p)
d = ['_']*len(pa)
e = 0

print('-=-'*10,'JOGO DA FORCA','-=-'*10)
while True:
    print(' '.join(d))

    chute = input('Escolha uma letra: ').strip().lower()

    if chute in letras_us:
        print ('Você já usou essa letra')
        continue
    else:
        letras_us.append(chute)

    if len(chute) != 1:
        print('Escolha apenas uma letra!!')
        continue

    if chute in pa:
        for i in range(len(pa)):
            if pa[i] == chute:
                d[i] = chute
        if '_' not in d:
            print('Parabéns, Você ganhou!')
            print(f'A palavra era {pa}')
            break
        else:
            print('Acertou!')
    else:
        print('Errou!')
        print(boneco[e])
        e+=1

    if e == 6:
        print('Você perdeu!')
        print(f'A palavra era {pa}')
        break