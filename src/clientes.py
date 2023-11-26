from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"


def cria_novo_cliente():

    nome = input("Nome? ")
    sobrenome = input("Sobrenome? ")
    telefone = input("Telefone? ")
    morada = input("Morada? ")
    nif = input("NIF? ")
    email = input("Email? ")

    cliente = {"Nome": nome,
               "sobrenome": sobrenome,
               "telefone": telefone,
               "morada": morada,
               "nif": nif,
               "email": email}
    
    return cliente 

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Clientes", lista=lista_de_clientes)

