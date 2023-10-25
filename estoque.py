import pickle


try:
    with open('estoque.pkl', 'rb') as file:
        estoque = pickle.load(file)
except FileNotFoundError:
    estoque = {}

def salvar_estoque():
    with open('estoque.pkl', 'wb') as file:
        pickle.dump(estoque, file)

def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    if codigo in estoque:
        print("Produto já cadastrado. Atualizando informações...")
        estoque[codigo]["quantidade"] += quantidade
    else:
        estoque[codigo] = {"nome": nome, "quantidade": quantidade}
    
    print(f"Produto {nome} cadastrado com sucesso!")
    salvar_estoque()

def repor_estoque():
    codigo = input("Digite o código do produto que deseja repor: ")
    if codigo in estoque:
        quantidade = int(input("Digite a quantidade a ser reposta: "))
        estoque[codigo]["quantidade"] += quantidade
        print(f"Estoque do produto {estoque[codigo]['nome']} reposto com sucesso!")
        salvar_estoque()
    else:
        print("Produto não encontrado no estoque.")

def reposicao_solicitada():
    codigo = input("Digite o código do produto que teve a reposição solicitada: ")
    if codigo in estoque:
        quantidade_solicitada = int(input("Digite a quantidade solicitada: "))
        if quantidade_solicitada <= estoque[codigo]["quantidade"]:
            estoque[codigo]["quantidade"] -= quantidade_solicitada
            print(f"Reposição de {quantidade_solicitada} unidades do produto {estoque[codigo]['nome']} foi solicitada.")
            salvar_estoque()

            # Registra a solicitação em um arquivo TXT
            with open('solicitacoes.txt', 'a') as arquivo_solicitacoes:
                arquivo_solicitacoes.write(f"Código: {codigo}, Nome: {estoque[codigo]['nome']}, Quantidade solicitada: {quantidade_solicitada}\n")
        else:
            print("Quantidade solicitada excede o estoque disponível.")
    else:
        print("Produto não encontrado no estoque.")

def consultar_estoque():
    print("\nEstoque atual:")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo}, Nome: {produto['nome']}, Quantidade em estoque: {produto['quantidade']}")

while True:
    print("\nOpções:")
    print("1. Cadastrar Produto")
    print("2. Repor Estoque")
    print("3. Reposição Solicitada")
    print("4. Consultar Estoque")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        repor_estoque()
    elif opcao == "3":
        reposicao_solicitada()
    elif opcao == "4":
        consultar_estoque()
    elif opcao == "5":
        salvar_estoque()
        break
    else:
        print("Opção inválida. Tente novamente.")

4