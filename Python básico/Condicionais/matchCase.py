# basicamente uma escolha, se nao escolheu nenhuma das opçoes case _


opcao = int(input("Escolha uma opcao (1 a 3): "))
match opcao:
    case 1:
        print("Voce escolheu a opcao 1")
    case 2: 
        print("Voce escolheu a opcao 2")
    case 3:
        print("Voce escolheu a opcao 3")
    case _: 
        print("Nenhuma das opcoes")