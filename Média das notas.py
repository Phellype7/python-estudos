a = int(input('Primeira nota: '))
b = int(input('Segunda nota: '))
c = int(input('Terceira nota: '))
d = int(input('quarta nota: '))
med = (a+b+c+d)/4
print(f'A média das 4 notas é {med}')
if 8>med>=6:
    print('O ALUNO ESTÁ \033[32mAPROVADO\033[m')
elif med>=8:
    print('WOW! O ALUNO FOI MUITO BEM, ESTÁ \033[32mAPROVADO\033[m')
elif 6>med>=4:
    print('O ALUNO ESTÁ DE \033[33mRECUPERAÇÃO\033[m')
else:
    print('O ALUNO ESTÁ \033[31mREPROVADO\033[m')