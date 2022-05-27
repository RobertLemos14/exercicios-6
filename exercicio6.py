
produtosdiferentes = input("Digite  a quantidade de produtos diferentes")
produtosdiferentes = int(produtosdiferentes)
produtos = 0
listaprodutos = []
i = 0
valortotal = 0
for produtos in range(0, produtosdiferentes):
    nomeproduto = input("digite o nome do produto " + str(i + 1) + ":")
    quantidadeprodutos = input("digite a quantidade de produtos " + str(i + 1) + ":")
    valor = float(input("digite o valor unitario do produto " + str(i + 1)+ ":") )
    discdeprodutos = {
        "nome" : nomeproduto,
        "quantidade" : quantidadeprodutos,
        "valor" : valor

    }
    listaprodutos.append(discdeprodutos)
    i += 1
    valortotal += valor




print("nome | quantidade | valor")
for nome in listaprodutos:
    print("{} | {} | {}".format(nome["nome"], nome["quantidade"], nome["valor"]))

print("O valor total da compra foi: " , valortotal)
