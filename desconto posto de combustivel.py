l = float(input("Quantos litros? "))
t = input("Qual o tipo? [A-alcool/G-gasolina] ").upper()

if t == 'A':
    p = l*5
elif t == 'G':
    p = l*7
if 20 <= l <= 30:
    des = p * 5/100
elif l > 30:
    des = p * 10/100
else:
    des = 0

p = p-des

print(f'O valor a ser pago é {p:.2f}')