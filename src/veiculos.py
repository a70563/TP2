from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


def cria_novo_veiculo():

    marca = input("marca? ")
    modelo = input("modelo?")
    matricula = input("matricula? ").upper()
    cor = input("Cor? ")
    ano_de_compra = input("Ano de compra? ")

    veiculo = {"marca": marca,
               "modelo": modelo,
               "matricula": matricula,
               "cor": cor,
               "Ano de compra": ano_de_compra}

    return veiculo


def imprime_lista_de_veiculos(lista_de_veiculos):
    """TODO: documentação

    :param marca: marca do veiculo que esta a ser registado
    :param modelo: modelo do veiculo que esta a ser rçegistado
    :param matricula: matricula do veiculo que esta a ser registado
    :param cor: cor do veiculo que esta a ser registado
    :param ano_de_compra: ano de compra do veiculo que esta a ser registado
    """
    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
