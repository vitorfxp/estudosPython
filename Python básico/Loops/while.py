# while

contador = 1
while contador <= 5:
    print(f"Contando: {contador}")
    contador+= 1 


senha = ''
while senha != 'python':
    senha = input("Digite sua senha: ")

print("Senha correta !")

for numero in range(1,6): #pode ser 1 a 6 ou so 6
    print(numero)


frutas = ['maça', 'melancia', 'uva', 'kiwi']
for fruta in frutas:
    print(f"Fruta atual: {fruta}")

#tabuada
for multiplicador in range (1,11):
    for multplicado in range (1,11):
        print(F"{multiplicador} x {multplicado} = {multplicado * multiplicador}")

pessoas = ['ana','bruno', 'fernando', 'daniel','felipe']
for nome in pessoas:
    print(f"Verificando:{nome}")
    if nome == 'daniel':
        print(f"Nome encontrado:{nome}")
        break #serve pra quebrar algo, ou seja, se o codigo continuasse, ele iria procurar por felipe tambem, mas nao era necessario, afinal, ele ja encontrou o nome necessario.

print("Busca encerrada!")

for numero in range (1,11):
    if numero % 2 == 0:
        continue #serve para continuar o codigo, um exemplo e isso, ele busca somente os impares, toda vez que ele encontrar um par, ele vai continuar
    print(f"Número:{numero}")