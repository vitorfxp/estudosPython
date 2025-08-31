#* listas = [], prcorure pelo index ou epla valor que ou t=retonara o valor ou o index dessa valor( o index seria a posiçao do valor na lista)

frutas = ['maça', 'banana', 'laranja']
print(frutas[0]) #utiliza a posiçao da lista para poder chamar o valor la dentro

frutas.append('melancia') #adiciona um item na ultima posiçao da lista
frutas.remove('banana') # remove um valor da lista
print(frutas)


frutas[1] = 'uva' #substitui um item na lista por outro
frutas.insert(1, 'kiwi') #insere um item, porem voce pode escolher a posiçao dele
fruta_removida = frutas.pop(3) #remove um item em base a posiçao dele
print(len(frutas))
print(f"A fruta removida foi {fruta_removida}")
print(frutas)

frutas.sort()#organiza em ordem alfabetica
frutas.clear()#limpa a lista
print(frutas.index('banana'))
print(frutas)

frutas2 = frutas.copy()# faz uma copia da lista, e portanto sao duas listas separadas

frutas2.append('uva')
frutas2.append('kiwi')

print(frutas2)


#Tuplas, são imutaveis, não podem ser substituidas

cores = ('vermelho', 'azul', 'verde')