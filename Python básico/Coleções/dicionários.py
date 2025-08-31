#dicionarios

pessoa = {
    "nome" : "Julio",
    "idade" : 25,
    "cidade": 'São Paulo',
    "profissoes": ['programador','designer','Bombeiro']
}

pessoa["idade"] = 26 #atualiza um valor dentro da chaves
print(pessoa["idade"]) #printa um valor especifico na chave
del pessoa["cidade"] #deleta algo (del)
print(pessoa)
print(pessoa["profissoes"][1]) #printa algum valor especifico da chves, e sua posiçao se criaod uma lista dentro dessa posiçao

print(pessoa.keys())#retorna as chaves dentro do dicionario
print(pessoa.values())#retornar os valores do dicionario
valores = list(pessoa.values()) #aqui foi feito um casting, parecido com o do input, com int ou float, fizemos  isso para criar uma lista e procurar por sua posiçao logo em baixo, entao acharemos o valor: sao paulo.
print(valores[2])
print(pessoa.get('telefone','não existe')) #busca um valor ou uma chave no dicionario
item_removido = pessoa.pop('profissoes') #elimina um item
print(f"Item removido: {item_removido}")
print(pessoa)
