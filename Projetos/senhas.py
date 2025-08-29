
import random 
#aqui aprendemos a da import em random para poder utilizar sua função de radomizar os caracteres, junto com o random tem o choices que esolhe entre os 8 caracteres e organizar em uma senha, junto k = n, determinado quantos caraceteres eu quero

lista = ["1","2","3","a","b","c","@","#"]
senha = "".join(random.choices(lista, k = 12 ))

#print(senha)

#mas se quisermos melhorar e não digitar manualmente podemos importar a função string e utilizar a .ascii_uppercase, .acsii_lowercasa, .digits e .punctuation

import string

tamanho = int(input("Qual o tamanho voce quer sua senha? escolha entre 8 a 12: "))


maiuscula = string.ascii_uppercase
minuscula = string.ascii_lowercase
pontuaçao =   string.punctuation
digitos = string.digits
obrigatorio = [random.choice(maiuscula),random.choice(minuscula),random.choice(pontuaçao),random.choice(digitos)]

todos = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
aleatorio = "".join(random.choices(todos, k = tamanho))
senha2 = aleatorio + "".join(obrigatorio)
sorteio = senha2 - 4
print(sorteio)

