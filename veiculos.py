from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


def cria_novo_veiculo():

    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    cor = input("Cor?")
    ano_de_compra = input("Ano de compra?")

    veiculo = {"marca": marca,
               "matricula": matricula,
               "cor": cor,
               "Ano de compra": ano_de_compra}

    return veiculo


def imprime_lista_de_veiculos(lista_de_veiculos):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
