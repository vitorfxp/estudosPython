#ex01
# Crie um programa que imprime os números de 10 até 1 usando um loop while.

#ex02
# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

#ex03
# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
# Quando o usuário digitar 0, o programa para e mostra o total economizado.

#ex04
# Crie um sistema de votação onde o usuário escolhe entre:
# 1."Pizza"
# 2."Hambúrguer"
# 3."Sair"
# Enquanto ele não digitar "3", continue perguntando
# No final, mostre quantos votos cada item recebeu


#ex01
# contador = 10
# while contador >= 1:
#     print(f"Contando em decrescente:{contador} ")
#     contador -= 1

#ex02
# numeros = []
# for n in range (1, 6):
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)

# resultado = 0
# for numero in numeros:
#     resultado += numero

# print(f"O resultado é:{resultado}")

#ex03
# total = 0.0
# while True:
#     valor = float(input("Insira algo no cofrinho: "))
#     if valor == 0:
#         break
#     total += valor
# print(f"Aqui esta o valor no cofrinho:{total}")

#ex04
pizza = 0
amburgui = 0
while True:
    voto = int(input("Escolha entre: \n1.pizza\n2.amburgui\n3.sair\n"))
    match voto:
        case 1:
            pizza += 1
        case 2:
            amburgui += 1
        case 3:
            break
        case _:
            print("Opção inválida")

    
print(f"Resultados:\n1.total em pizza:{pizza}\n2.total em amburgui:{amburgui}")