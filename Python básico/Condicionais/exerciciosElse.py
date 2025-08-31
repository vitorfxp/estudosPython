# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:

# Nota 9 ou 10: "Excelente!"

# Nota 7 ou 8: "Muito bom"

# Nota 5 ou 6: "Regular"

# Menor que 5: "Ruim"
#---------------------------------------------------------------
# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:

# O valor da compra deve ser maior ou igual a 100

# E o cliente precisa estar cadastrado no programa de fidelidade

# Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"

# Caso contrário: "Frete não disponível gratuitamente.



# exercício 1

nota_filme = int(input("Dê uma nota de 0 a 10 para avaliação: "))
if nota_filme >= 9:
    print("Excelente!!")
elif nota_filme >= 7:
    print("Muito Bom!")
elif nota_filme >= 6:
    print("Regular")
else:
    print("Ruim")

# exercício 2

Verficaçao_cliente_valor = int(input("Vamos verificar se você tem direito a frete grátis,Qual valor da sua compra?: "))
Verficaçao_cliente_fidelidade = input("Certo, você participa do nosso prgramo de fidelidade? respondo com sim ou não: ")
if Verficaçao_cliente_valor >= 100 and Verficaçao_cliente_fidelidade == "sim":
    print("Parabéns,você tem direito a frete grátis!!")
else:
    print("Infelizmente você não tem direito a frete grátis")
    


