# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota_minima = int(input("Qual foi sua nota ?: "))
if nota_minima >= 6:
    print("Você atingiu a nota mínima!")

# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

nomes1 = input("Insira o primeiro nome: ")
nome2 = input("insira o segundo nome: ")
if nomes1 != nome2:
    print("os nomes são diferentes!")

# Elegibilidade para um Evento (Idade Mínima): Imagine um evento para maiores de 15 anos. Crie um código que pergunte a idade do usuário. Verifique se a idade do usuário é maior ou igual a 15. Se for, exiba "Você pode participar do evento!".

Idade = int(input("Qual sua idade?: "))
if Idade >= 15:
    print("Prabéns, você pode participar do evento!")