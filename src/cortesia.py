from io_terminal import imprime_lista

nome_ficheiro_lista_de_cortesia = "lista_de_cortesia.pk"


def cria_novo_veiculo_cortesia():

    marca_cortesia = input("Marca? ")
    modelo_cortesia = input("Modelo? ")
    matricula_cortesia = input("Matricula? ").upper()
    ## estado_veiculo = input("Estado do veículo? ").upper()  -- pretendemos adicionar mais informações com novas variaveis 

    veiculo_cortesia = {"Marca do Veículo": marca_cortesia,
            "Modelo da Veículo": modelo_cortesia,
            "Matricula da Veículo": matricula_cortesia}
            ## "Estado da Veículo": estado_veiculo

    return veiculo_cortesia


def imprime_lista_de_cortesia(lista_de_cortesia):
    """TODO: documentação

    :param marca: marca do veiculo que esta a ser registado
    :param modelo: modelo do veiculo que esta a ser rçegistado
    :param matricula: matricula do veiculo que esta a ser registado
    :param cor: cor do veiculo que esta a ser registado
    :param ano_de_compra: ano de compra do veiculo que esta a ser registado
    """
    imprime_lista(cabecalho="Lista de Items", lista=lista_de_cortesia)
