def menu():
    proximo = str

    while proximo:
        proximo = str(
            input("[C] Cadastrar\n" +
                  "[L] Listar\n" +
                  "[B] Buscar\n" +
                  "[A] Atualizar\n" +
                  "[R] Remover\n"))
        if proximo == 'L':
            listar()
        elif proximo == 'C':
            cadastrar()
        elif proximo == 'A':
            atualizar()
        elif proximo == 'B':
            buscar()
        elif proximo == 'R':
            remover()
        else:
            print("Error! Opção invalida!")


def listar():
    for nome in produtos.keys():
        print("Produto: ", nome, " - Quantidade: ", produtos[nome])


def cadastrar():
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Quantidade dele: "))

    if produtos.get(nome):
        print("Ja existe o produto ", nome)
    else:
        produtos[nome] = quantidade


def atualizar():
    nome = input("Produto a mudar a quantidade: ")
    quantidade = float(input("Nova quantidade: "))

    if nome in produtos.keys():
        produtos[nome] = quantidade
    else:
        print("Não existe esse produto")


def buscar():
    nome = input("Digite o nome do produto: ")

    if produtos.get(nome):
        print("Quantidade de ", nome, ": ", produtos[nome])
    else:
        print("Nao existe tal produto")


def remover():
    nome = input("Apagar qual produto: ")

    if produtos.get(nome):
        produtos.pop(nome)
    else:
        print("Não existe o produto ", nome)


produtos = {}
menu()