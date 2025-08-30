# 🧪 Exercício 1 – Acesso por índice
# Crie uma lista com 3 animais e mostre o primeiro e o último elemento.

# 🧪 Exercício 2 – Manipulando uma lista
# Dada a lista abaixo:
# livros = ["Python", "Java", "C++"]
# Realize as seguintes ações:
# Adicione o livro "JavaScript"
# Remova o livro "Java"
# Troque "Python" por "Go"
# Mostre o tamanho da lista

# 🧪 Exercício 3 – Trabalhando com contagem e localização
# Dada a lista abaixo:
# nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]
# Mostre:
# Quantas vezes o nome Carla aparece
# Qual o índice da primeira vez que ele aparece

#ex01
Animais = ['Cachorro', 'gato', 'papagaio']
print(f"O primeiro animal é {Animais[0]} e o ultimo é {Animais[2]}")

#ex02
livros = ["Python", "Java", "C++"]
livros.append('JavaScript')
livros.pop(1)
livros[0] = 'Go'
print(len(livros))
print(livros)

#ex03
nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]
contagem = nomes.count('Carla')
primeira_pos = nomes.index('Carla')
print(f"Aparece: {contagem} e a primeira posição é: {primeira_pos}")
