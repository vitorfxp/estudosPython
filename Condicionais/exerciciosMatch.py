# Crie um menu com 3 opções:
# 1. Pizza
# 2. Sushi
# 3. Salada
# O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."

#-----------------------------------------------------------------------------------------------------

# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:
# "carro" → "Veículo terrestre"
# "bicicleta" → "Transporte sustentável"
# "avião" ou "helicóptero" → "Transporte aéreo"
# Qualquer outro → "Transporte desconhecido"

# Exercício 1

menu_opcao = int(input("Escolha entre 1-Pizza, 2-Sushi e 3-Salada: "))
match menu_opcao:
    case 1:
        print("Você escolheu pizza!")
    case 2:
        print("Você escolheu sushi!")
    case 3:
        print("Você escolheu salada!")
    case _:
        print("Opção Inválida")

# Exercício 2

meio_de_transporte = input("Qual seu meio de transporte? ")
match meio_de_transporte:
    case "carro":
        print("Veículo terrestre")
    case "bicicleta": 
        print("Voce escolheu bicicleta")
    case "avião" | "helicoptero":
        print("veiculo aereo")
    case _:
        print("Transporte de desconhecido")
    






