from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"


def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir os dados de uma nova fatura

    :return: dicionario com uma fatura, na forma
        {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """

    id_cliente = pergunta_id(questao="Qual o ID do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o ID do veiculo?", lista=lista_de_veiculos, mostra_lista=True)
    fatura_lista_pecas = pergunta_id(questao="Qual o ID da peça?", lista=lista_de_items, mostra_lista=True)
    nif = input("NIF?")
    desconto = input("Desconto? 0 - 100 ")
    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionario
    # ...

    fatura = {"Cliente": id_cliente,
              "Veiculo": id_veiculo,
              "NIF": nif,
              "Lista de Peças": fatura_lista_pecas,
              "Data": date.today()}

    return fatura


def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Faturas", lista=lista_de_faturas)