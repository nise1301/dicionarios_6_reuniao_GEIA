"""Rápida revisão de coleções em Python:
Lista: é uma coleção dinâmica e mutavel que pode receber varios tipos
(você pode colocar numeros e strings por ex), mantem os elementos organizados por indice e são definidas com
colchetes []
Tupla: diferente da lista, tupla é imutavel, também é ordenada, de tipos mistos e acessada por indice e deve ser
iniciada com parenteses ()
Dicionarios: são coleções desordenadas, acessadas por chave e valor, onde as chaves funcionam como identificadores
únicos e imutaveis para acessar um valor correspondente que pode ser de tipos diferentes e mutavel. Mesmo que o valor
possa se repetir, a chave deve permanecer única"""

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado com sucesso.")

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ")
    if nome in contatos:
        del contatos[nome] # Sim, descobri outra forma de deletar um valor em python XD Precisei usar del em vez de
        # remove por que remove é uma função que remove somente a primeira ocorrencia, não se aplica pq dicionario
        # não é ordenado por indice, em vez disso, descobri que del é um comando que pode ser usado para exclui a chave
        print(f"Contato {nome} removido com sucesso.")
    else:
        print("Contato não encontrado.")

def atualizar_contato(contatos):
    nome = input("Digite o nome do contato a ser atualizado: ")
    if nome in contatos:
        telefone = input("Digite o novo telefone do contato: ")
        email = input("Digite o novo email do contato: ")
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"Contato {nome} atualizado com sucesso.")
    else:
        print("Contato não encontrado.")

def buscar_contato(contatos):
    nome = input("Digite o nome do contato a ser buscado: ")
    if nome in contatos:
        print(f"Nome: {nome}")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print("Contato não encontrado.")

def listar_contatos(contatos):
    if contatos:
        for nome, info in contatos.items():
            """aqui é um pouco complicado, o metodo do python items() vai quebrar o
             dicionario de volta em duas tuplas (por padrão, mas retorna dicionarios se houiver dicionarios aninhados)
             que são o par chave nome e info, onde info é atribuido a telefone e email.
             O que importa é saber que items() sempre vai retornar uma "visão" do par chave valor em um dicionario"''' """
            print(f"Nome: {nome}")
            print(f"Telefone: {info['telefone']}")
            print(f"Email: {info['email']}\n")
    else:
        print("Nenhum contato cadastrado.")


def menu():
    contatos = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Atualizar Contato")
        print("4. Buscar Contato")
        print("5. Listar Todos os Contatos")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            remover_contato(contatos)
        elif escolha == "3":
            atualizar_contato(contatos)
        elif escolha == "4":
            buscar_contato(contatos)
        elif escolha == "5":
            listar_contatos(contatos)
        elif escolha == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()