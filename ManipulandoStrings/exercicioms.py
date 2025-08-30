# *Exercício 1 – Primeira e Última Letra
# *Peça ao usuário para digitar uma palavra. Mostre:
# *A primeira letra
# *A última letra

# *Exercício 2 – Pegando um trecho da frase
# *Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

# *Exercício 3 – Detectando palavras proibidas
# *Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

# *Exercício 4 – Arrumando o texto
# *Dada uma variável frase = "    @prendendo @ progr@m@r   "  com espaços nas pontas e letras bagunçadas, o programa deve:
# *Remover espaços do início/fim
# *Trocar todas as letras "@" por "a"
# *Colocar a primeira letra de cada palavra em maiúsculo

#* ex01
letras = input("Digite uma palavra: ")
primeira_letra = letras[0]
segunda_letra = letras[-1]
print(f"Aqui está a Primeira letra {primeira_letra} e a Última {segunda_letra}")


#* ex02
frase = input("Digite uma frase: ")
num1= int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

print(f"Aqui esta o fatiamento da frase/palavra:{frase[num1:num2]}")


#* ex03
frase = input("Escreva sua mensagem ao usuário: ")
if 'bomba' in frase.lower():
    print("ALERTA: bomba")
else:
    print("Mensagem recebida, logo logo terá sua resposta!")

#* ex04
frase = "    @prendendo @ progr@m@r   "
frase = frase.replace('@','a')
print(frase.strip())
