# 01 -  Crie um dicionário chamado livro com as chaves: "titulo", "autor" e "ano".
# Depois, mostre cada valor usando print().

# 02 - Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
# Depois, verifique se a idade é maior ou igual a 18:
# Se sim, imprima: "Acesso liberado para {nome}"
# Se não, imprima: "Acesso negado para {nome}"

# 03 - Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.
# Se o usuário e a senha estão corretos → "Login bem-sucedido"
# Senão → "Usuário ou senha incorretos"

#ex01  
livro = {
    "titulo": "Harry Potter",
    "autor": "j.k. Rowling",
    "ano": 2007
}
print(livro.values())


#ex02
dados = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: "))
}
if dados["idade"] >= 18:
    print(f"Acesso liberado para {dados['nome']}")
else:
    print(f"Acesso negado para {dados['nome']}")

print(dados)

#ex03
dados_sistema = {
    "usuario": 'joao vitor',
    "senha": 4573
}

dados_entrada = {
    "Usuario": input("Digite seu usuario: "),
    "Senha": int(input("Digite sua senha (somente numeros!): "))
}

if dados_entrada["Usuario"] == dados_sistema["Usuario"] and dados_entrada["Senha"] == dados_sistema["senha"] :
    print("login bem-sucedido")
else:
    print("Usuario ou senha incorretos")
