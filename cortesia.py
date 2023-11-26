from io_terminal import imprime_lista

nome_ficheiro_lista_de_cortesia = "lista_de_cortesia.pk"


def cria_novo_viatura_cortesia():

    marca_cortesia = input("Marca de viatura de cortesia? ")
    modelo_cortesia = input("Modelo da viatura de cortesia?")
    matricula_cortesia = input("Matricula da viatura? ").upper()
    estado_viatura = input("Estado da viatura? ").upper()

    viatura_cortesia = {"Marca da Viatura": marca_cortesia,
            "Modelo da Viatura": modelo_cortesia,
            "Matricula da Viatura": matricula_cortesia,
            "Estado da Viatura": estado_viatura}

    return viatura_cortesia


def imprime_lista_de_cortesia(lista_de_cortesia):
    """TODO: documentação

    :param marca: marca do veiculo que esta a ser registado
    :param modelo: modelo do veiculo que esta a ser rçegistado
    :param matricula: matricula do veiculo que esta a ser registado
    :param cor: cor do veiculo que esta a ser registado
    :param ano_de_compra: ano de compra do veiculo que esta a ser registado
    """
    imprime_lista(cabecalho="Lista de Items", lista=lista_de_cortesia)