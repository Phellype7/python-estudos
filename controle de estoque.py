import copy

estoque = [["Teclado", 15],
           ["Mouse", 40],
           ["Monitor", 8],
           ["Webcam", 12],
           ["Headset", 25],
           ["Mousepad", 50],
           ["Cabo HDMI", 30]]

estoque_original = copy.deepcopy(estoque)

opcao = -1

while opcao != 0:
    print("\n" + "=" * 50)
    print("                 SISTEMA DE CONTROLE DE ESTOQUE                 ")
    print("=" * 50)
    print("1 - Consultar estoque atual")
    print("2 - Consultar estoque inicial")
    print("3 - Cadastrar novo produto")
    print("4 - Inserir produto em posição específica")
    print("5 - Atualizar quantidade de um produto")
    print("6 - Remover produto")
    print("7 - Retirar último item do estoque")
    print("8 - Localizar produto e sua posição")
    print("9 - Exibir indicadores do estoque")
    print("10 - Listar produtos com estoque crítico")
    print("0 - Encerrar sistema")
    print("=" * 50)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nESTOQUE ATUAL")

        for i, (prod, qtd) in enumerate(estoque):
            print(f"{i + 1} - {prod} → Quantidade: {qtd}")

    elif opcao == 2:
        print("ESTOQUE INICIAL")

        for i, (prod, qtd) in enumerate(estoque_original):
            print(f"{i + 1} - {prod} → Quantidade: {qtd}")

    elif opcao == 3:
        item_novo = input("Digite o item novo: ").capitalize()
        quantidade_novo = int(input("Digite a quantidade: "))

        estoque.append([item_novo, quantidade_novo])

        print("Novo item cadastrado!")

    elif opcao == 4:
        item_novo = input("Digite o item novo: ").capitalize()
        quantidade_novo = int(input("Digite a quantidade: "))
        posicao = int(input("Digite a posição desejada: "))

        estoque.insert(posicao - 1, [item_novo, quantidade_novo])

        print("Novo item cadastrado!")

    elif opcao == 5:
        nome = input("Digite o nome do item: ")
        achou = False

        for item in estoque:
            if nome.lower() == item[0].lower():
                achou = True

                quantidade_novo = int(input("Nova quantidade: "))
                item[1] = quantidade_novo

                print("Nova quantidade cadastrada!")

        if not achou:
            print("Este item não existe no estoque!")

    elif opcao == 6:
        nome = input("Digite o nome do item: ")
        achou = False

        for item in estoque:
            if nome.lower() == item[0].lower():
                achou = True

                estoque.remove(item)

                print("Item removido!")

        if not achou:
            print("Este item não existe no estoque!")

    elif opcao == 7:
        if estoque:
            removido = estoque.pop()

            print(f"O item {removido[0]}, com a quantidade {removido[1]} foi removido!")
        else:
            print("Não há mais itens a serem removidos")

    elif opcao == 8:
        nome = input("Digite o nome do item: ")
        achou = False

        for item in estoque:
            if nome.lower() == item[0].lower():
                posicao = estoque.index(item)

                print(f"Indice: {posicao + 1}")
                print(f"Saldo atual: {item[1]}")

                achou = True

        if not achou:
            print("Este item não existe no estoque!")

    elif opcao == 9:
        print("Relatório de estoque")

        print(f"Total de produtos cadastrados: {len(estoque)}")

        quantidades = []

        for prod, qtd in estoque:
            quantidades.append(qtd)

        print(f"Menor estoque encontrado: {min(quantidades)}")
        print(f"Maior estoque encontrado: {max(quantidades)}")

        total = sum(quantidades)

        print(f"Quantidade total de itens no armazém: {total}")
        print(f"Quantidade média por produto: {total / len(quantidades):.1f}")

    elif opcao == 10:
        quantidades = []

        for prod, qtd in estoque:
            quantidades.append(qtd)

        media = sum(quantidades) / len(quantidades)

        print("Produtos com quantidade abaixo da média: ")

        for prod, qtd in estoque:
            if qtd < media:
                print(f"Produto: {prod} - quantidade: {qtd}")

    elif opcao == 0:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida")