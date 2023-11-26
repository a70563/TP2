from io_terminal import imprime_lista

nome_ficheiro_lista_de_items = "lista_de_items.pk"


def cria_novo_item():

    nome_item = input("Item? ")
    valor_item = input("Valor do Item?")
    quantidade_item = input("Quantos Items? ")

    item = {"Nome do Item": nome_item,
            "valor do Item": valor_item,
            "Quantidade do Item": quantidade_item}

    return item


def imprime_lista_de_items(lista_de_items):
    """TODO: documentação

    :param marca: marca do veiculo que esta a ser registado
    :param modelo: modelo do veiculo que esta a ser rçegistado
    :param matricula: matricula do veiculo que esta a ser registado
    :param cor: cor do veiculo que esta a ser registado
    :param ano_de_compra: ano de compra do veiculo que esta a ser registado
    """
    imprime_lista(cabecalho="Lista de Items", lista=lista_de_items)