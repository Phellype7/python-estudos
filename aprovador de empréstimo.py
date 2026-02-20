a = float(input('qual o valor da casa? R$'))
b = float(input('qual o seu salario? R$'))
c = int(input('em quantos anos vai parcelar? '))
e = a/(c*12)
print(f'Para pagar uma casa de R${a} em {c} anos a prestação será de R${e:.2f}')
if e>(b*30)/100:
    print('\033[31mEMPRÉSTIMO NEGADO')
else:
    print('\033[32mEMPRÉSTIMO ACEITO')