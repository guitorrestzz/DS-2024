from click import clear
def cadastrar_pessoa():
    nome = input('Escreva o nome que será registrado: ')
    email = input('Escreva o e-mail que será registrado: ')
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}\n')

    print('Cadastrado com sucesso!')

cadastrar_pessoa()

def listar_pessoas():
    with open('cadastro.txt', 'r') as arquivo:
     print('Pessoas cadastradas:')
     for linha in arquivo:
            nome, email = linha.strip().split(',')
            print(f'Nome: {nome}, E-mail: {email}')

listar_pessoas()
