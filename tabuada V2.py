while True:
    a = int(input("Quer ver a tabuada de qual numero? "))
    if a<0:
        print ("Programa de tabuada encerrado!")
        break
    for t in range(1, 11):
        print(f"{a} x {t} = {a*t}")