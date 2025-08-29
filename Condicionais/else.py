#else 

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

numero = float(input("Digite um número: "))
if numero % 2 == 0:
    print("Esse número é par!")
else: 
    print("esse número é impar!")

nota = 50
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("D")

idade = 20 
carteira = True
if idade >= 18:
    print("Você tem iadade para dirigir.")
    if carteira:
        print("Você tem uma carteira de motorista.")
    else:
        print("Você não tem uma carteira de motorista.")
else:
    print("Você não tem idade para dirirgir.")


#Operadores de comparação: and, or e not

animal_fav = "cachorro"
if animal_fav == "cachorro" or animal_fav == "gato":
    print("Ótima escolha")
else:
    print("meh")

idade = 20 
if idade >= 13 and idade <= 19 :
    print("voce esta na adolescencia")

chovendo = True
if not chovendo:
    print("Não está chovendo!")
else:
    print("Está chovendo<3")