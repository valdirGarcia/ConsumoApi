from StarWars import StarWars

sw_api = StarWars()

while True:
    
    print("\nSelecione uma opção:")
    print("1 - Consultar dados de personagem")
    print("2 - Consultar dados de filme")
    print("3 - Consultar dados de planeta")
    print("4 - Encerrar")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        id_personagem = input("Digite o ID do personagem desejado: ")
        dados_personagem = sw_api.obter_personagem(id_personagem)
        if dados_personagem:
            print(f"\nInformações sobre o personagem {id_personagem}:")
            print("Nome:", dados_personagem['name'])
            print("Altura:", dados_personagem['height'])
            print("Peso:", dados_personagem['mass'])
        else:
            print("\nPersonagem não encontrado ou falha na solicitação da API.")
    elif opcao == "2":
        id_filme = input("Digite o ID do filme desejado: ")
        dados_filme = sw_api.obter_filme(id_filme)
        if dados_filme:
            print(f"\nInformações sobre o filme {id_filme}:")
            print("Título:", dados_filme['title'])
            print("Diretor:", dados_filme['director'])
            print("Lançamento:", dados_filme['release_date'])
        else:
            print("\nFilme não encontrado ou falha na solicitação da API.")
    elif opcao == "3":
        id_planeta = input("Digite o ID do planeta desejado: ")
        dados_planeta = sw_api.obter_planeta(id_planeta)
        if dados_planeta:
            print(f"\nInformações sobre o planeta {id_planeta}:")
            print("Nome:", dados_planeta['name'])
            print("Clima:", dados_planeta['climate'])
            print("Terreno:", dados_planeta['terrain'])
        else:
            print("\nPlaneta não encontrado ou falha na solicitação da API.")
    elif opcao == "4":
        print("\nEncerrando o programa.")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
