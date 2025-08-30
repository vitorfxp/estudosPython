#fatiamento de strings

fruta = "melancia"
print(fruta[0])

fruta = "melancia"
print(fruta[-1])

fruta = "melancia"
print(fruta[0:3])

fruta = "melancia"
print(fruta[:6])

fruta = "melancia"
print(fruta[2:])


frase ="  eu amo python!  "

# função do python: len, serve para retornar o tamanho de alguma coisa no codigo
frase_tamanho = len(frase)
print(f"A frase: {frase} tem {frase_tamanho} caracteres!")

#o ponto count conta quantas letras tem dentrod de uma variavel, mas tambem calcula outras coias
contagem = frase.count('a')
print(contagem)

# O find pode tanto retorna uma posiçao do index com a eltra, qaunto retornar a letra com a posiçao do index
print(frase.find('m'))

# podemos colocar in no python, para perguntar ou afirma se tem algo dentro (in = dentro)
if 'python' in frase:
    print("Python está na frase")
else:
    print("Não está na frase")

#Temos o upper: deixa as letras em caixa alta, e o lower: deixa todas as letras em minusculo
#se eu quiser mudar a frase para sempre: frase = frase.upper
print(frase.upper())
print(frase.lower())

#Captalize: primeira letra da frase com maiuscula
print(frase.capitalize())

#Strip: tira espaços desnecessarios na frase
print(frase.strip())

#Replace: substituir uma letra por outra 
print(frase.replace('o','a'))

#Tittle: deixa a primeira letar de cada palavra na frase em maiusculo
print(frase.title())