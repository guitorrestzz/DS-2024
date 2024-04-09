"""from click import clear
letra = 's'
while letra == 's':


    produtos = []
    valores = []
    quantidade = []
    descricao = []

    p = (input('Digite o nome do produto: '))
    produtos.append(p)

    v = float(input('Digite o valor do produto: '))
    valores.append(v)

    qtd = int(input('Digite a quantidade do produto: '))
    quantidade.append(qtd)


    desc = (input('Digite a descrição do produto: '))
    descricao.append(desc)

    letra = (input('Deseja continuar? [s/n] '))


    clear()
opcao = input('Deseja exibir os Produtos? [sim/não] ')
if opcao == 'sim':
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(produtos)):
        print(f' \t {produtos[i]} \t\t\t {valores[i]} \t\t {quantidade[i]} \t\t {descricao[i]}')

opcao = input('Deseja deletar os produtos [sim/nao]')
if opcao == 'sim':
    opcao = int(input('Qual registro deseja deletar?'))
    produtos.pop(opcao)
    valores.pop(opcao)
    descricao.pop(opcao)
    quantidade.pop(opcao)


clear()
opcao = input('Deseja exibir os produtos [sim/nao]')
if opcao == 'sim':
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(produtos)):
        print(f'{produtos[i]} \t\t {valores[i]} \t\t\t {quantidade[i]} \t\t {descricao[i]}')"""

from click import clear

opcao = 0
nome_produto = []
valor_produto = []
descricao_produto = []
quantidade_produto = []

def adicionar():
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome_produto.append(nome)
    valor_produto.append(valor)
    descricao_produto.append(descricao)
    quantidade_produto.append(quantidade)

    with open('Cadastroprodutos.txt', 'a') as arquivo:
        arquivo.write(f'{nome_produto},{valor_produto},{descricao_produto},{quantidade_produto}\n')

def mostrar():
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ')
    for i in range(0, len(nome_produto)):
        print(f'{nome_produto[i]} \t\t {valor_produto[i]} \t\t\t {quantidade_produto[i]} \t\t {descricao_produto[i]}')
    input("pressione ENTER para continuar...")

def excluir():
    opcao = int(input('Qual registro deseja deletar?'))
    nome_produto.pop(opcao)
    valor_produto.pop(opcao)
    descricao_produto.pop(opcao)
    quantidade_produto.pop(opcao)


while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar um produto")
    print("2 - Para mostrar produtos")
    print("3 - Para excluir um produto")
    print("4 - Para sair")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        mostrar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        break

def listar_produtos():
    nome_produto = input('Digite o produto: ')

    with open('Cadastroprodutos.txt', 'a') as arquivo:
        arquivo.write(f'{nome_produto}\n')

    print("Pessoa cadastrada com sucesso!!!")
    for linha in arquivo:
        nome, email = linha.strip().split(',')
        print(f'Produto {nome_produto}')


def listar():
    with open('Cadastroprodutos.txt', 'r') as arquivo:
        for linha in arquivo:
            nome_produto = linha.strip().split(',')
            print(f'Produto: {nome_produto}')

#adicionar_pessoa()
#listar_pessoas()

listar()




