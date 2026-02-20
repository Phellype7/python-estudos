lista=[]
with open('lista de tarefas.txt', 'r') as f:
    for linha in f:
        lista.append(linha.strip())
while True:
    print('''\033[36m===LISTA DE TAREFAS===\033[m
\033[31m1\033[m - ADICIONAR TAREFA
\033[32m2\033[m - REMOVER TAREFA
\033[34m3\033[m - VER TAREFAS
\033[35m4\033[m - SAIR''')
    try:
        a=int(input('Escolha: '))
    except:
        print('\033[31mDIGITE UM DOS NUMEROS APRESENTADOS\033[m')
        continue
    if a==1:
        ta=input('Digite a tarefa: ')
        if ta in lista:
            print('\033[31mESSA TAREFA JA ESTA NA LISTA\033[m')
        else:
            lista.append(ta)
            print('\033[32mTAREFA ADICIONADA!\033[m')
            with open('lista de tarefas.txt', 'a') as f:
                f.write(ta + '\n')
    elif a==2:
        try:
            rem=int(input('qual o numero da tarefa que deseja excluir? '))
        except:
            print('\033[31mDIGITE O NUMERO DA TAREFA\033[m')
            continue
        if rem<1 or rem>len(lista):
            print('\033[31mNÃO FOI POSSIVEL REMOVER A TAREFA, TENTE NOVAMENTE\033[m')
        else:
            lista.pop(rem-1)
            print ('\033[32mTAREFA REMOVIDA!\033[m')
        with open('lista de tarefas.txt', 'w') as f:
                for t in lista:
                    f.write(t + '\n')
    elif a==3 and len(lista)==0:
        print('\033[33mVOCÊ NÃO POSSUI TAREFAS\033[m')
    elif a==3:
        print('TAREFAS ATUAIS:')
        for i in range(len(lista)):
            print(f'[{i+1}] {lista[i]}')
    elif a==4:
        print('Saindo...')
        break